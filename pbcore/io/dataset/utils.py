###############################################################################
# Copyright (c) 2011-2016, Pacific Biosciences of California, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Pacific Biosciences nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE.  THIS SOFTWARE IS PROVIDED BY PACIFIC BIOSCIENCES AND ITS
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT
# NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR
# ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
###############################################################################

# Author: Martin D. Smith


"""
Utils that support fringe DataSet features.
"""
import os
import tempfile
import logging
import json
import shutil
import datetime
import pysam
from pbcore.util.Process import backticks

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
            shutil.rmtree(tmpout)
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
    cmd = "pbindex {i}".format(i=fname)
    log.info(cmd)
    o, r, m = backticks(cmd)
    if r != 0:
        raise RuntimeError(m)
    return fname + ".pbi"

def _indexBam(fname):
    pysam.samtools.index(fname, catch_stdout=False)
    return fname + ".bai"

def _indexFasta(fname):
    pysam.samtools.faidx(fname, catch_stdout=False)
    return fname + ".fai"

def _pbmergeXML(indset, outbam):
    cmd = "pbmerge -o {o} {i} ".format(i=indset,
                                       o=outbam)
    log.info(cmd)
    o, r, m = backticks(cmd)
    if r != 0:
        raise RuntimeError("Pbmerge command failed: {c}\n Message: "
                           "{m}".format(c=cmd, m=m))
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

