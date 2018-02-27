#################################################################################
# Copyright (c) 2015-2018, Pacific Biosciences of California, Inc.
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
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR
# ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#################################################################################

"""Doctest resources"""
from __future__ import absolute_import

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
