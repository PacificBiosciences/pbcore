# Author: Martin D. Smith


"""
Utils that support fringe DataSet features.
"""

import warnings
import subprocess
import os
import re
import tempfile
import logging
import shutil
import datetime

import numpy as np
import pysam

log = logging.getLogger(__name__)


def getTimeStampedName(mType):
    """Generate a timestamped name using the given metatype 'mType' and the
    current UTC time"""
    mType = mType.lower()
    mType = '_'.join(mType.split('.'))
    time = datetime.datetime.utcnow().strftime("%y%m%d_%H%M%S%f")[:-3]
    return "{m}-{t}".format(m=mType, t=time)


def getCreatedAt():
    """Generate a CreatedAt string using the current UTC time"""
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S%f")[:-6]


def which(exe):
    if os.path.exists(exe) and os.access(exe, os.X_OK):
        return exe
    path = os.getenv('PATH')
    for this_path in path.split(os.path.pathsep):
        this_path = os.path.join(this_path, exe)
        if os.path.exists(this_path) and os.access(this_path, os.X_OK):
            return this_path
    return None


def consolidateXml(indset, outbam, useTmp=True, cleanup=True):
    log.debug("Consolidating to {o}".format(o=outbam))

    final_free_space = disk_free(os.path.split(outbam)[0])
    projected_size = sum(file_size(infn)
                         for infn in indset.toExternalFiles())
    log.debug("Projected size:            {p}".format(p=projected_size))
    log.debug("In place free space:       {f}".format(f=final_free_space))
    # give it a 5% buffer
    if final_free_space < (projected_size * 1.05):
        raise RuntimeError("Not enough space available in {o} to consolidate, "
                           "{p} required, {a} available".format(
                               o=os.path.split(outbam)[0],
                               p=projected_size * 1.05,
                               a=final_free_space
                           ))
    # indset is a dataset, not a filename. So we need to write the dataset out
    # to a file anyway. We'll use tmp for that, but we won't go so far as to
    # copy the actual resources:
    tmpout = tempfile.mkdtemp(suffix="consolidate-xml")
    tmp_xml = os.path.join(tmpout,
                           "orig.{t}.xml".format(
                               t=indset.__class__.__name__.lower()))
    tmp_free_space = disk_free(tmpout)

    # need 2x for tmp in and out, plus 10% buffer
    if useTmp:
        log.debug("Tmp free space (need ~2x): {f}".format(f=tmp_free_space))
    if (tmp_free_space > (projected_size * 2.1)) and useTmp:
        log.debug("Using tmp storage: " + tmpout)
        indset.copyTo(tmp_xml)
        origOutBam = outbam
        outbam = os.path.join(tmpout, "outfile.bam")
    else:
        log.debug("Using in place storage")
        indset.write(tmp_xml)
        useTmp = False
    _pbmergeXML(tmp_xml, outbam)
    if useTmp:
        shutil.copy(outbam, origOutBam)
        shutil.copy(outbam + ".pbi", origOutBam + ".pbi")
    if cleanup:
        def _handle_error(function, path, excinfo):
            log.error("Can't remove %s", path)
            log.error(excinfo)
        shutil.rmtree(tmpout, ignore_errors=True, onerror=_handle_error)
    return outbam


def _tmpFiles(inFiles, tmpout=None):
    tmpInFiles = []
    if tmpout is None:
        tmpout = tempfile.mkdtemp(suffix="consolidation-filtration")
    for i, fname in enumerate(inFiles):
        newfn = _infixFname(os.path.join(tmpout, os.path.basename(fname)), i)
        shutil.copy(fname, newfn)
        tmpInFiles.append(newfn)
    return tmpInFiles


def disk_free(path):
    if path == '':
        path = os.getcwd()
    space = os.statvfs(path)
    return space.f_bavail * space.f_frsize


def file_size(path):
    return os.stat(path).st_size


def _pbindexBam(fname):
    args = ["pbindex", fname]
    log.info(" ".join(args))
    subprocess.check_call(args)
    return fname + ".pbi"


def _indexBam(fname):
    pysam.samtools.index(fname, catch_stdout=False)
    return fname + ".bai"


def _indexFasta(fname):
    pysam.samtools.faidx(fname, catch_stdout=False)
    return fname + ".fai"


def _pbmergeXML(indset, outbam):
    args = ["pbmerge", "-o", outbam, indset]
    log.info(" ".join(args))
    subprocess.check_call(args)
    return outbam


def _infixFname(fname, infix):
    prefix, extension = os.path.splitext(fname)
    return prefix + str(infix) + extension


def _earlyInfixFname(fname, infix):
    path, name = os.path.split(fname)
    tokens = name.split('.')
    tokens.insert(1, str(infix))
    return os.path.join(path, '.'.join(tokens))


def _swapPath(dest, infile):
    return os.path.join(dest, os.path.split(infile)[1])


def _fileCopy(dest, infile, uuid=None):
    fn = _swapPath(dest, infile)
    if os.path.exists(fn):
        if uuid is None:
            raise IOError("File name exists in destination: "
                          "{f}".format(f=infile))
        subdir = os.path.join(dest, uuid)
        if not os.path.exists(subdir):
            os.mkdir(subdir)
        fn = _swapPath(subdir, fn)
    shutil.copyfile(infile, fn)
    assert os.path.exists(fn)
    return fn

# FIXME this is *not* numerically identical to the pbbam result!
# FIXME also it would be better to use numpy array ops, but the code below
# does not work for ndarray as written.


def hash_combine_zmw(zmw):
    """
    Generate a unique hash for a ZMW, for use in downsampling filter.
    """
    mask = 0xFFFF
    upper = (zmw >> 16) & mask
    lower = zmw & mask
    result = 0
    result ^= upper + 0x9e3779b9 + (result << 6) + (result >> 2)
    result ^= lower + 0x9e3779b9 + (result << 6) + (result >> 2)
    return result


def hash_combine_zmws(zmws):
    return [hash_combine_zmw(zmw) for zmw in zmws]


def divideKeys(keys, chunks):
    """Returns all of the keys in a list of lists, corresponding to evenly
    sized chunks of the original keys"""
    if chunks < 1:
        return []
    if chunks > len(keys):
        chunks = len(keys)
    chunksize = len(keys)//chunks
    key_chunks = [keys[(i * chunksize):((i + 1) * chunksize)] for i in
                  range(chunks-1)]
    key_chunks.append(keys[((chunks - 1) * chunksize):])
    return key_chunks


def splitKeys(keys, chunks):
    """
    Returns key pairs for each chunk defining the bounds of each chunk.
    """
    if chunks < 1:
        return []
    if chunks > len(keys):
        chunks = len(keys)
    chunksize = len(keys)//chunks
    chunksizes = [chunksize] * chunks
    i = 0
    while sum(chunksizes) < len(keys):
        chunksizes[i] += 1
        i += 1
        i %= chunks
    key_chunks = []
    start = 0
    for cs in chunksizes:
        key_chunks.append((keys[start], keys[start + cs - 1]))
        start += cs
    return key_chunks


def split_keys_around_read_groups(keys, chunks):
    """
    Wrapper for splitKeys that avoids grouping multiple movies in the same
    chunk if possible.
    """
    qids = np.unique(keys.qId)
    sub_chunks = []
    if len(qids) > 1:
        n_sub_chunks = chunks // len(qids)
        if n_sub_chunks == 0:
            raise RuntimeError("{c} chunks requested but there are {g} read groups present in the dataset".format(c=chunks, g=len(qids)))
        for qId in qids:
            sub_keys = keys[keys.qId == qId]
            sub_chunks.extend(splitKeys(sub_keys, n_sub_chunks))
        assert len(sub_chunks) <= chunks
        return sub_chunks
    else:
        return splitKeys(keys, chunks)


def collection_file_resolver(start_path, extension):
    """
    Given a path to a PacBio instrument output, for example the main dataset
    XML payload, determine the path for a related resource file by extension,
    taking into account differences in directory layout between software
    versions and products.  This is mainly intended as a workaround for
    internal uses where we generate additional files not declared in the
    primary consensusreadset.xml delivered by the production instruments.
    """
    # XXX this should not be used anywhere in the SMRT Link code
    if "SMRT_CHEMISTRY_BUNDLE_DIR" in os.environ:
        warnings.warn("This function should not be used in customer-facing production code.", FutureWarning)
    DATASET_SUBDIRS = ["pb_internal", "pb_formats", "metadata", "statistics", "hifi_reads"]
    if not os.path.isfile(os.path.realpath(start_path)):
        raise ValueError(f"{start_path} is not a valid file")
    base_dir = os.path.dirname(os.path.realpath(start_path))
    if not extension.startswith(".") or extension.startswith("_"):
        extension = "." + extension
    base_file_name = os.path.basename(start_path)
    base_name, base_ext = os.path.splitext(base_file_name)
    base_ext2 = ""
    movie_context = base_name.split(".")[0]
    if base_ext in {".xml", ".h5", ".bam"}:
        base_name, base_ext2 = os.path.splitext(base_name)
    base_ext = f"{base_ext2}{base_ext}"
    target_file_name = f"{movie_context}{extension}"
    candidate_path_1 = os.path.join(base_dir, target_file_name)
    if os.path.isfile(candidate_path_1):
        log.debug(f"Found {extension} file at {candidate_path_1}")
        return candidate_path_1
    else:
        log.debug(f"Path {candidate_path_1} is not a valid file")
    base_subdir = os.path.basename(base_dir)
    if base_subdir in DATASET_SUBDIRS:
        dataset_root_dir = os.path.dirname(base_dir)
        log.info(f"New dataset contents found, looking under {dataset_root_dir}")
        for subdir in DATASET_SUBDIRS:
            candidate_path_2 = os.path.join(dataset_root_dir, subdir, target_file_name)
            if os.path.isfile(candidate_path_2):
                log.debug(f"Found {extension} file at {candidate_path_2}")
                return candidate_path_2
    contents = " ".join(os.listdir(base_dir))
    log.warn(f"Can't find file matching '{extension}' in directory {base_dir}: {contents}")
    raise IOError(f"Can't find instrument file with extension {extension} associated with {start_path}")
