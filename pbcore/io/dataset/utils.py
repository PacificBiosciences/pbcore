"""
Utils that support fringe DataSet features.
"""
import os
import tempfile
import logging
import json
import shutil
from pbcore.util.Process import backticks

log = logging.getLogger(__name__)

def consolidateBams(inFiles, outFile, filterDset=None, useTmp=True):
    """Take a list of infiles, an outFile to produce, and optionally a dataset
    (filters) to provide the definition and content of filtrations."""
    if useTmp:
        tmpout = tempfile.mkdtemp(suffix="consolidation-filtration")
        tmpInFiles = []
        for i, fname in enumerate(inFiles):
            newfn = os.path.join(tmpout, _infixFname("file.bam", str(i)))
            shutil.copy(fname, newfn)
            tmpInFiles.append(newfn)
        origOutFile = outFile
        inFiles = tmpInFiles
        outFile = os.path.join(tmpout, "outfile.bam")

    if filterDset and filterDset.filters:
        finalOutfile = outFile
        outFile = _infixFname(outFile, "_unfiltered")
    _mergeBams(inFiles, outFile)
    if filterDset and filterDset.filters:
        _filterBam(outFile, finalOutfile, filterDset)
        outFile = finalOutfile
    _indexBam(outFile)
    _pbindexBam(outFile)
    if useTmp:
        shutil.copy(outFile, origOutFile)
        shutil.copy(outFile + ".bai", origOutFile + ".bai")
        shutil.copy(outFile + ".pbi", origOutFile + ".pbi")

def _pbindexBam(fname):
    cmd = "pbindex {i}".format(i=fname)
    log.info(cmd)
    o, r, m = backticks(cmd)
    if r != 0:
        raise RuntimeError(m)

def _sortBam(fname):
    tmpname = _infixFname(fname, "_sorted")
    cmd = "bamtools sort -in {i} -out {o}".format(i=fname, o=tmpname)
    log.info(cmd)
    o, r, m = backticks(cmd)
    if r != 0:
        raise RuntimeError(m)
    shutil.move(tmpname, fname)

def _indexBam(fname):
    cmd = "samtools index {i}".format(i=fname)
    log.info(cmd)
    o, r, m = backticks(cmd)
    if r != 0:
        raise RuntimeError(m)

def _indexFasta(fname):
    cmd = "samtools faidx {i}".format(i=fname)
    log.info(cmd)
    o, r, m = backticks(cmd)
    if r != 0:
        raise RuntimeError(m)

def _mergeBams(inFiles, outFile):
    if len(inFiles) > 1:
        cmd = "bamtools merge -in {i} -out {o}".format(i=' -in '.join(inFiles),
                                                       o=outFile)
        log.info(cmd)
        o, r, m = backticks(cmd)
        if r != 0:
            raise RuntimeError(m)
    else:
        shutil.copy(inFiles[0], outFile)

def _filterBam(inFile, outFile, filterDset):
    tmpout = tempfile.mkdtemp(suffix="consolidation-filtration")
    filtScriptName = os.path.join(tmpout, "filtScript.json")
    _emitFilterScript(filterDset, filtScriptName)
    cmd = "bamtools filter -in {i} -out {o} -script {s}".format(
        i=inFile, o=outFile, s=filtScriptName)
    log.info(cmd)
    o, r, m = backticks(cmd)
    if r != 0:
        raise RuntimeError(m)

def _infixFname(fname, infix):
    prefix, extension = os.path.splitext(fname)
    return prefix + infix + extension

def _emitFilterScript(filterDset, filtScriptName):
    """Use the filter script feature of bamtools. Use with specific filters if
    all that are needed are available, otherwise filter by readname (easy but
    uselessly expensive)"""
    filterMap = {'rname': 'reference',
                 'pos': 'position',
                 'length': 'queryBases',
                 'qname': 'name',
                 'rq': 'mapQuality'}
    cheapFilters = True
    for filt in filterDset.filters:
        for req in filt:
            if not filterMap.get(req.name):
                cheapFilters = False
    if cheapFilters:
        script = {"filters":[]}
        for filt in filterDset.filters:
            filtDict = {}
            for req in filt:
                name = filterMap[req.name]
                if name == 'reference':
                    if req.operator == '=' or req.operator == '==':
                        filtDict[name] = req.value
                    else:
                        raise NotImplementedError()
                else:
                    filtDict[name] = req.operator + req.value
            script['filters'].append(filtDict)
    else:
        names = [rec.qName for rec in filterDset]
        script = {"filters":[{"name": name} for name in names]}
    with open(filtScriptName, 'w') as scriptFile:
        scriptFile.write(json.dumps(script))

