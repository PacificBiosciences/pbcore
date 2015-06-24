"""Doctest resources"""

import os
from pkg_resources import Requirement, resource_filename

XML_FILES = ["ali1.xml", #0
             "ali2.xml",
             "ali3.xml",
             "ali4.xml",
             "barcode.dataset.xml", #4
             "ccsread.dataset.xml",
             "contig.dataset.xml",
             "reference.dataset.xml",
             "subread_dataset1.xml",
             "subread_dataset2.xml", #9
             "subread_dataset3.xml",
             "transformed_rs_subread_dataset.xml",
             "hdfsubread_dataset.xml",
             "pbalchemy10kbp.xml",
             "lambda_contigs.xml", #14
             "bam_mapping_staggered.xml",
             os.path.join('yieldtest', 'yieldtest.xml'),
             os.path.join('..', 'chunking',
                          '90240.winTest.chunk0contigs.xml'),
             os.path.join('yieldtest', 'yieldContigsRef.xml'),
             'subreadSetWithStats.xml', #19
            ]
BAM_FILES = ["bam_mapping.bam", "pbalchemy10kbp.pbalign.sorted.pbver1.bam"]
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
    return _getAbsPath(XML_FILES[19])

def getBam(no=0):
    return _getAbsPath(BAM_FILES[no])

def getStats(no=0):
    return _getAbsPath(STATS_FILES[no])

def getFofn(no=0):
    return _getAbsPath(FOFN_FILES[no])

def getRef():
    return _getAbsPath(XML_FILES[14])

def getSubreadSet(no=0):
    return _getAbsPath(XML_FILES[no + 8])

def getHdfSubreadSet():
    return _getAbsPath(XML_FILES[12])
