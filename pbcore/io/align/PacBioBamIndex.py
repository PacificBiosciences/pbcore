# Author: David Alexander

from __future__ import absolute_import, division, print_function

from builtins import range
from os.path import abspath, expanduser
from struct import unpack
import math
import gc

import numpy as np
import numpy.lib.recfunctions as nlr

from Bio.bgzf import BgzfReader, BgzfBlocks, make_virtual_offset
from ._BamSupport import IncompatibleFile

__all__ = ["PacBioBamIndex"]


PBI_HEADER_LEN = 32

PBI_FLAGS_BASIC = 0
PBI_FLAGS_MAPPED = 1
PBI_FLAGS_COORDINATE_SORTED = 2
PBI_FLAGS_BARCODE = 4


class PbIndexBase(object):

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


class PacBioBamIndex(PbIndexBase):
    """
    The PacBio BAM index is a companion file allowing modest
    *semantic* queries on PacBio BAM files without iterating over the
    entire file.  By convention, the PacBio BAM index has extension
    "bam.pbi".
    """

    @property
    def isChunk(self):
        return self._chunk_start is not None and self._chunk_size is not None

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

    def _loadMainIndex(self, f, to_virtual_offset=None, zmw_only=False):
        # Main index holds basic, mapping, and barcode info
        BASIC_INDEX_DTYPE = [
            ("qId", "i4"),
            ("qStart", "i4"),
            ("qEnd", "i4"),
            ("holeNumber", "i4"),
            ("readQual", "f4"),
            ("contextFlag", "u1"),
            ("virtualFileOffset", "i8")]

        MAPPING_INDEX_DTYPE = [
            ("tId", "i4"),
            ("tStart", "u4"),
            ("tEnd", "u4"),
            ("aStart", "u4"),
            ("aEnd", "u4"),
            ("isReverseStrand", "u1"),
            ("nM", "u4"),
            ("nMM", "u4"),
            ("mapQV", "u1")]

        COORDINATE_SORTED_DTYPE = [
            ("tId", "u4"),
            ("beginRow", "u4"),
            ("endRow", "u4")]

        BARCODE_INDEX_DTYPE = [
            ("bcForward", "i2"),
            ("bcReverse", "i2"),
            ("bcQual", "i1")]

        COMPUTED_COLUMNS_DTYPE = [
            ("nIns", "u4"),
            ("nDel", "u4")]

        joint_dtype = BASIC_INDEX_DTYPE[:]

        if self.hasMappingInfo:
            joint_dtype += MAPPING_INDEX_DTYPE
            joint_dtype += COMPUTED_COLUMNS_DTYPE
        if self.hasBarcodeInfo:
            joint_dtype += BARCODE_INDEX_DTYPE
        index_len = self.nReads
        if self.isChunk:
            index_len = self._chunk_size

        self._array_start = PBI_HEADER_LEN

        def peek(type_, length):
            flavor, width_ = type_
            width = int(width_)
            if self.isChunk:
                start_pos = self._array_start + self._chunk_start * width
                virtual_offset = to_virtual_offset(start_pos)
                f.seek(virtual_offset)
                length = self._chunk_size
            data = np.frombuffer(f.read(length * width), "<" + type_)
            if self.isChunk:
                self._array_start += self.nReads * width
            return data

        if zmw_only:
            # NOTE very important to limit memory consumption here, so we
            # skip creating the combined table and return the extracted array
            # instead
            assert not self.isChunk
            start_pos = self._array_start + index_len * 12 # qId+qStart+qEnd
            virtual_offset = to_virtual_offset(start_pos)
            f.seek(virtual_offset)
            return peek("i4", index_len)
        else:
            tbl = np.zeros(shape=(index_len,),
                           dtype=joint_dtype).view(np.recarray)
            # BASIC data always present
            for columnName, columnType in BASIC_INDEX_DTYPE:
                tbl[columnName] = peek(columnType, index_len)

            if self.hasMappingInfo:
                for columnName, columnType in MAPPING_INDEX_DTYPE:
                    tbl[columnName] = peek(columnType, index_len)

                # Computed columns
                tbl.nIns = tbl.aEnd - tbl.aStart - tbl.nM - tbl.nMM  # pylint: disable=no-member
                tbl.nDel = tbl.tEnd - tbl.tStart - tbl.nM - tbl.nMM  # pylint: disable=no-member

            # TODO: do something with these:
            # TODO: remove nReads check when the rest of this code can handle empty
            # mapped bam files (columns are missing, flags don't reflect that)
            if self.hasCoordinateSortedInfo and self.nReads:
                ntId = int(peek("u4", 1))
                for columnName, columnType in COORDINATE_SORTED_DTYPE:
                    peek(columnType, ntId)

            if self.hasBarcodeInfo:
                for columnName, columnType in BARCODE_INDEX_DTYPE:
                    tbl[columnName] = peek(columnType, index_len)

            self._tbl = tbl
            self._checkForBrokenColumns()

    def _loadOffsets(self, f):
        if (self.pbiFlags & PBI_FLAGS_COORDINATE_SORTED):
            # TODO!
            pass

    def __init__(self, pbiFilename, chunk_start=None, chunk_size=None,
                 to_virtual_offset=None):
        self._chunk_start = chunk_start
        self._chunk_size = chunk_size
        pbiFilename = abspath(expanduser(pbiFilename))
        with BgzfReader(pbiFilename) as f:
            try:
                self._loadHeader(f)
                self._loadMainIndex(f, to_virtual_offset)
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
        for i in range(len(self)):
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
        ix = np.flatnonzero((self.tId == winId) &
                            (self.tStart < winEnd) &
                            (self.tEnd > winStart))
        return ix

    def _checkForBrokenColumns(self):
        if ((self.pbiFlags & PBI_FLAGS_MAPPED) and
                (len(self) > 0) and np.all((self.nM == 0) & (self.nMM == 0))):
            raise IncompatibleFile("This bam.pbi file was generated by a version of pbindex with"
                                   " a bug.  Please rerun pbindex.")

    @property
    def identity(self):
        assert (self.pbiFlags & PBI_FLAGS_MAPPED)
        return 1 - ((self.nMM + self.nIns + self.nDel) /
                    (self.aEnd.astype(float) - self.aStart.astype(float)))


class StreamingBamIndex(PacBioBamIndex):
    """
    Wrapper that iterates over the bam.pbi index in chunks, yielding a
    PacBioBamIndex object representing the current chunk.  The arrays in each
    chunk, if concatenated, are guaranteed to be identical to the arrays in
    the full non-streamed index.  They are also guaranteed not to split ZMWs
    across chunk boundaries; for SubreadSets coming directly off an instrument
    this will also mean that each chunk contains only complete ZMWs.  As a
    result the actual chunk size (and possibly the number of chunks) will not
    be consistent or predictable, although it will be close to the requested
    size.

    The memory overhead to instantiate this object will be proportional to the
    size of the extracted array of ZMW numbers (4 bytes each, but computing an
    index from this array effectively doubles this), but after the internal
    indices have been generated it is proportional to the number of unique
    ZMWs plus the number of GZIP blocks.  The memory overhead for each chunk
    will be approximately chunk_size*29 bytes (plus a small slop factor) for
    off-instrument subread BAM files.

    In practice, for a 6.5GB compressed pbi (indexing a 550GB subreads BAM)
    the memory consumption briefly maxes at slightly over 6GB to initialize,
    and 3.125 for streaming chunks.

    This sacrifices some computational efficiency due to the combination of
    BGZF format peculiarities and the requirement that we keep ZMW-grouped
    subreads together, both of which add expensive (and seemingly redundant)
    file reads.  However the ZMW grouping makes it possible to collect
    statistics using fast numpy array operations which more than compensates
    for the initial setup time.
    """

    def __init__(self, pbiFilename, chunk_size=10000000):
        self._chunk_start = None
        self._pbiFilename = abspath(expanduser(pbiFilename))
        self._get_blocks()
        with BgzfReader(self._pbiFilename) as f:
            self._loadHeader(f)
            holeNumbers = self._loadMainIndex(f, self._to_virtual_offset,
                                              zmw_only=True)
            self._make_chunks(chunk_size, holeNumbers)

    def _make_chunks(self, chunk_size, holeNumbers):
        """
        Use the array of ZMW numbers to divide the index into chunks of
        approximately the requested chunk size, plus or minus up to NPASSES-1
        subreads in either direction to avoid splitting ZMWs.
        """
        flag = np.concatenate(([True], holeNumbers[1:] != holeNumbers[:-1]))
        self._zmw_idx = np.flatnonzero(flag)
        self._chunks = []
        self._chunk_idx = []
        last_start_idx = 0
        k = 1
        while last_start_idx < self.nReads:
            last_start = self._zmw_idx[last_start_idx]
            next_start_idx = np.argmax(self._zmw_idx > k * chunk_size)
            if next_start_idx == 0:
                self._chunks.append((last_start, self.nReads - last_start))
                self._chunk_idx.append(
                    self._zmw_idx[last_start_idx:] - last_start)
                break
            next_start = self._zmw_idx[next_start_idx]
            self._chunks.append((last_start, next_start - last_start))
            idx_sel = self._zmw_idx[last_start_idx:next_start_idx]
            self._chunk_idx.append(idx_sel - last_start)
            last_start_idx = next_start_idx
            k += 1

    def _get_blocks(self):
        # start_offset, block_length, data_start, data_len
        self._blocks = list(BgzfBlocks(open(self._pbiFilename, "rb")))
        self._data_start = np.array([b[2] for b in self._blocks])

    def _to_virtual_offset(self, offset):
        """
        Convert an offset in uncompressed bytes to a virtual offset that the
        bgzf reader can use.
        """
        isel = np.where(self._data_start <= offset)[0]
        start_offset, block_length, data_start, data_len = self._blocks[
            isel[-1]]
        return make_virtual_offset(start_offset, offset - data_start)

    def get_chunk(self, i_chunk):
        chunk_start, chunk_size = self._chunks[i_chunk]
        return PacBioBamIndex(self._pbiFilename, chunk_start, chunk_size,
                              self._to_virtual_offset)

    def __iter__(self):
        i_chunk = 0
        while i_chunk < self.nchunks:
            yield self.get_chunk(i_chunk)
            i_chunk += 1

    def iter_with_zmw_index(self):
        """
        Iterate over chunks of the index, also yielding the sub-index of
        ZMW start indices in to the chunk arrays.  This allows relatively
        rapid iteration over ZMWs rather than individual subreads.
        """
        assert len(self._chunk_idx) == self.nchunks
        i_chunk = 0
        while i_chunk < self.nchunks:
            yield self.get_chunk(i_chunk), self._chunk_idx[i_chunk]
            i_chunk += 1

    def __len__(self):
        return self.nReads

    @property
    def nchunks(self):
        return len(self._chunks)
