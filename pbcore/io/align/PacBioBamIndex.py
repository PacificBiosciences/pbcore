# Author: David Alexander

from __future__ import absolute_import

from os.path import abspath, expanduser
from ._bgzf import BgzfReader
from struct import unpack

import numpy as np
import numpy.lib.recfunctions as nlr

from ._BamSupport import IncompatibleFile

__all__ = [ "PacBioBamIndex" ]


PBI_HEADER_LEN              = 32

PBI_FLAGS_BASIC             = 0
PBI_FLAGS_MAPPED            = 1
PBI_FLAGS_COORDINATE_SORTED = 2
PBI_FLAGS_BARCODE           = 4


class PacBioBamIndex(object):
    """
    The PacBio BAM index is a companion file allowing modest
    *semantic* queries on PacBio BAM files without iterating over the
    entire file.  By convention, the PacBio BAM index has extension
    "bam.pbi".
    """
    def _loadHeader(self, f):
        buf = f.read(PBI_HEADER_LEN)
        header = unpack("< 4s BBBx H I 18x", buf)
        (self.magic, self.vPatch, self.vMinor,
         self.vMajor, self.pbiFlags, self.nReads) = header
        try:
            assert (self.vMajor, self.vMinor, self.vPatch) >= (3, 0, 1)
        except:
            raise IncompatibleFile(
                "This PBI file is incompatible with this API "
                "(only PacBio PBI files version >= 3.0.1 are supported)")

    @property
    def hasMappingInfo(self):
        # N.B.: Or'ing in (nReads==0) is HACKish fix for issue with
        # empty mapped BAM files---the "Mapped" bit doesn't get set
        # correctly in pbi_flags if the file is empty. So in the empty
        # file case, assume it may be mapped.  The downside is we
        # don't get an exception on attempting to access the mapped
        # columns for empty unmapped BAM pbis.  Not a big deal, I
        # suppose
        return ((self.nReads == 0) or
                (self.pbiFlags & PBI_FLAGS_MAPPED))

    @property
    def hasCoordinateSortedInfo(self):
        return (self.pbiFlags & PBI_FLAGS_COORDINATE_SORTED)

    @property
    def hasBarcodeInfo(self):
        return (self.pbiFlags & PBI_FLAGS_BARCODE)

    def _loadMainIndex(self, f):
        # Main index holds basic, mapping, and barcode info
        BASIC_INDEX_DTYPE = [
            ("qId"               , "i4"),
            ("qStart"            , "i4"),
            ("qEnd"              , "i4"),
            ("holeNumber"        , "i4"),
            ("readQual"          , "f4"),
            ("contextFlag"       , "u1"),
            ("virtualFileOffset" , "i8") ]

        MAPPING_INDEX_DTYPE = [
            ("tId"               , "i4"),
            ("tStart"            , "u4"),
            ("tEnd"              , "u4"),
            ("aStart"            , "u4"),
            ("aEnd"              , "u4"),
            ("isReverseStrand"   , "u1"),
            ("nM"                , "u4"),
            ("nMM"               , "u4"),
            ("mapQV"             , "u1") ]

        COORDINATE_SORTED_DTYPE = [
            ("tId"               , "u4"),
            ("beginRow"          , "u4"),
            ("endRow"            , "u4")]

        BARCODE_INDEX_DTYPE = [
            ("bcForward"         , "i2"),
            ("bcReverse"         , "i2"),
            ("bcQual"            , "i1")]

        COMPUTED_COLUMNS_DTYPE = [
            ("nIns"              , "u4"),
            ("nDel"              , "u4") ]

        joint_dtype = BASIC_INDEX_DTYPE[:]

        if self.hasMappingInfo:
            joint_dtype += MAPPING_INDEX_DTYPE
            joint_dtype += COMPUTED_COLUMNS_DTYPE
        if self.hasBarcodeInfo:
            joint_dtype += BARCODE_INDEX_DTYPE
        tbl = np.zeros(shape=(self.nReads,),
                       dtype=joint_dtype).view(np.recarray)

        def peek(type_, length):
            flavor, width = type_
            return np.frombuffer(f.read(length*int(width)), "<" + type_)

        if True:
            # BASIC data always present
            for columnName, columnType in BASIC_INDEX_DTYPE:
                tbl[columnName] = peek(columnType, self.nReads)

        if self.hasMappingInfo:
            for columnName, columnType in MAPPING_INDEX_DTYPE:
                tbl[columnName] = peek(columnType, self.nReads)

            # Computed columns
            tbl.nIns = tbl.aEnd - tbl.aStart - tbl.nM - tbl.nMM
            tbl.nDel = tbl.tEnd - tbl.tStart - tbl.nM - tbl.nMM

        # TODO: do something with these:
        # TODO: remove nReads check when the rest of this code can handle empty
        # mapped bam files (columns are missing, flags don't reflect that)
        if self.hasCoordinateSortedInfo and self.nReads:
            ntId = int(peek("u4", 1))
            for columnName, columnType in COORDINATE_SORTED_DTYPE:
                peek(columnType, ntId)

        if self.hasBarcodeInfo:
            for columnName, columnType in BARCODE_INDEX_DTYPE:
                tbl[columnName] = peek(columnType, self.nReads)

        self._tbl = tbl
        self._checkForBrokenColumns()

    def _loadOffsets(self, f):
        if (self.pbiFlags & PBI_FLAGS_COORDINATE_SORTED):
            # TODO!
            pass

    def __init__(self, pbiFilename):
        pbiFilename = abspath(expanduser(pbiFilename))
        with BgzfReader(pbiFilename) as f:
            try:
                self._loadHeader(f)
                self._loadMainIndex(f)
                self._loadOffsets(f)
            except Exception as e:
                raise IOError("Malformed bam.pbi file: " + str(e))

    @property
    def version(self):
        return (self.vMajor, self.vMinor, self.vPatch)

    @property
    def columnNames(self):
        return list(self._tbl.dtype.names)

    def __getattr__(self, columnName):
        if columnName in self.columnNames:
            return self._tbl[columnName]
        else:
            raise AttributeError("pbi has no column named '%s'" % columnName)

    def __getitem__(self, rowNumber):
        # We do this dance to get a useable recarray slice--to
        # work around https://github.com/numpy/numpy/issues/3581
        if not np.isscalar(rowNumber):
            raise Exception("Unimplemented!")
        return np.rec.fromrecords([self._tbl[rowNumber]],
                                  dtype=self._tbl.dtype)[0]

    def __dir__(self):
        # Special magic for IPython tab completion
        basicDir = dir(self.__class__)
        return basicDir + self.columnNames

    def __len__(self):
        return len(self._tbl)

    def __iter__(self):
        for i in xrange(len(self)):
            yield self[i]

    def rangeQuery(self, winId, winStart, winEnd):
        #
        # A read overlaps the window if winId == tid and
        #
        #  (tStart < winEnd) && (tEnd > winStart)     (1)
        #
        # We are presently doing this naively right now, just
        # computing the predicate over all rows. If/when we determine
        # this is too slow, we can accelerate using the nBackread
        # approach we use int he cmph5, doing binary search to
        # identify a candidate range and then culling the range.
        #
        ix = np.flatnonzero((self.tId    == winId)  &
                            (self.tStart  < winEnd) &
                            (self.tEnd    > winStart))
        return ix

    def _checkForBrokenColumns(self):
        if ((self.pbiFlags & PBI_FLAGS_MAPPED) and
            (len(self) > 0) and  np.all((self.nM  == 0) & (self.nMM == 0))):
            raise IncompatibleFile("This bam.pbi file was generated by a version of pbindex with" \
                " a bug.  Please rerun pbindex.")
