# Author: Martin D. Smith

from __future__ import absolute_import, division, print_function

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
    TRANSCRIPT = toDsId("TranscriptSet")
    TRANSCRIPT_ALIGNMENT = toDsId("TranscriptAlignmentSet")

    ALL = (SUBREAD, HDF_SUBREAD, ALIGNMENT,
           BARCODE, CCS, CCS_ALIGNMENT, REFERENCE, CONTIG, GMAPREFERENCE,
           TRANSCRIPT, TRANSCRIPT_ALIGNMENT)

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

