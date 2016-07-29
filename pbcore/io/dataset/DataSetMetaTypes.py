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


import logging
from pbcore.io.dataset.DataSetErrors import (InvalidDataSetIOError,)

log = logging.getLogger(__name__)

def toDsId(name):
    """Translate a class name into a MetaType/ID"""
    return "PacBio.DataSet.{x}".format(x=name)

class DataSetMetaTypes(object):
    """
    This mirrors the PacBioSecondaryDataModel.xsd definitions and be used
    to reference a specific dataset type.
    """
    SUBREAD = toDsId("SubreadSet")
    HDF_SUBREAD = toDsId("HdfSubreadSet")
    ALIGNMENT = toDsId("AlignmentSet")
    BARCODE = toDsId("BarcodeSet")
    CCS_ALIGNMENT = toDsId("ConsensusAlignmentSet")
    CCS = toDsId("ConsensusReadSet")
    REFERENCE = toDsId("ReferenceSet")
    GMAPREFERENCE = toDsId("GmapReferenceSet")
    CONTIG = toDsId("ContigSet")

    ALL = (SUBREAD, HDF_SUBREAD, ALIGNMENT,
           BARCODE, CCS, CCS_ALIGNMENT, REFERENCE, CONTIG, GMAPREFERENCE)

    @classmethod
    def isValid(cls, dsId):
        return dsId in cls.ALL

def dsIdToName(dsId):
    """Translate a MetaType/ID into a class name"""
    if DataSetMetaTypes.isValid(dsId):
        return dsId.split('.')[-1]
    else:
        raise InvalidDataSetIOError("Invalid DataSet MetaType")

def dsIdToSuffix(dsId):
    """Translate a MetaType/ID into a file suffix"""
    dsIds = DataSetMetaTypes.ALL
    suffixMap = {dsId: dsIdToName(dsId) for dsId in dsIds}
    suffixMap[toDsId("DataSet")] = 'DataSet'
    if DataSetMetaTypes.isValid(dsId):
        suffix = suffixMap[dsId]
        suffix = suffix.lower()
        suffix += '.xml'
        return suffix
    else:
        raise InvalidDataSetIOError("Invalid DataSet MetaType")

