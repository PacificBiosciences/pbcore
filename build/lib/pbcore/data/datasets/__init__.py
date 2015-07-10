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
             "pbalchemysim0.pbalign.xml",
             "pbalchemysim0.reference.xml", #9
             "pbalchemysim0.subread.xml",
             "pbalchemysim1.pbalign.xml",
             "pbalchemysim.pbalign.xml", # both 0 and 1 bam files
             "pbalchemysim1.subread.xml",
             "subreadSetWithStats.xml", #14 # TODO: replace w regenable+new XSD
             "pbalchemysim0.pbalign.chunk0contigs.xml",
             "pbalchemysim0.pbalign.chunk1contigs.xml",
            ]
BAM_FILES = ["pbalchemysim0.pbalign.bam",
             "pbalchemysim1.pbalign.bam",
             os.path.join('..', 'bam_mapping.bam')]
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
    return _getAbsPath(XML_FILES[9])

def getBam(no=0):
    return _getAbsPath(BAM_FILES[no])

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
