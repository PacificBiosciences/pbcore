"""Doctest resources"""

import os
from pkg_resources import Requirement, resource_filename

XML_FILES = ["alignment.dataset.xml", #0
             "barcode.dataset.xml",
             "ccsread.dataset.xml",
             "contig.dataset.xml",
             "reference.dataset.xml", #4
             "subread.dataset.xml",
             "transformed_rs_subread_dataset.xml",
             "hdfsubread_dataset.xml",
             "pbalchemysim0.alignmentset.xml",
             "pbalchemysim0.referenceset.xml", #9
             "pbalchemysim0.subreadset.xml",
             "pbalchemysim1.alignmentset.xml",
             "pbalchemysim.alignmentset.xml", # both sim0 and sim1 bam files
             "pbalchemysim1.subreadset.xml",
             "subreadSetWithStats.xml", #14
             "pbalchemysim0.alignmentset.chunk0contigs.xml",
             "pbalchemysim0.alignmentset.chunk1contigs.xml",
             "pbalchemysim0.hdfsubreadset.xml",
             "pbalchemysim1.hdfsubreadset.xml",
             "pbalchemysim.hdfsubreadset.xml", #19
             "ccsaligned.dataset.xml",
            ]
BAM_FILES = ["pbalchemysim0.pbalign.bam",
             "pbalchemysim1.pbalign.bam",
             os.path.join('..', 'bam_mapping.bam'),
             "empty_lambda.aligned.bam",]
STATS_FILES = [
    "m150430_142051_Mon_p1_b25.sts.xml",
    "m150616_053259_ethan_c100710482550000001823136404221563_s1_p0.sts.xml"]
FOFN_FILES = ["fofn.fofn"]

def _getAbsPath(fname):
    return resource_filename(Requirement.parse('pbcore'),
                             'pbcore/data/datasets/%s' % fname)

def getXml(no=0):
    return _getAbsPath(XML_FILES[no])

def getXmlWithStats():
    return _getAbsPath(XML_FILES[14])

def getBam(no=0):
    return _getAbsPath(BAM_FILES[no])

def getEmptyAlignedBam():
    return _getAbsPath(BAM_FILES[3])

def getStats(no=0):
    return _getAbsPath(STATS_FILES[no])

def getFofn(no=0):
    return _getAbsPath(FOFN_FILES[no])

def getRef():
    return _getAbsPath(XML_FILES[9])

def getSubreadSet():
    return _getAbsPath(XML_FILES[5])

def getHdfSubreadSet():
    return _getAbsPath(XML_FILES[7])

def getBarcodedBam():
    return _getAbsPath(BAM_FILES[3])
