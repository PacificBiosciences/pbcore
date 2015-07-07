#################################################################################
# Copyright (c) 2011-2015, Pacific Biosciences of California, Inc.
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

# Author: David Alexander

from os.path import abspath, expanduser
from _bgzf import BgzfReader
from struct import unpack

import numpy as np
import numpy.lib.recfunctions as nlr


PBI_HEADER_LEN              = 32

PBI_FLAGS_BASIC             = 0
PBI_FLAGS_MAPPED            = 1
PBI_FLAGS_COORDINATE_SORTED = 2
PBI_FLAGS_BARCODE_ADAPTER   = 4


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

    def _loadMainIndex(self, f):

        def peek(type_, length):
            flavor, width = type_
            return np.frombuffer(f.read(length*int(width)), "<" + type_)

        if True:
            # BASIC data always present
            qId               = peek("i4", self.nReads)
            qStart            = peek("i4", self.nReads)
            qEnd              = peek("i4", self.nReads)
            holeNumber        = peek("i4", self.nReads)
            readQual          = peek("u2", self.nReads)
            virtualFileOffset = peek("i8", self.nReads)

            tbl = np.rec.fromarrays(
                [qId, qStart, qEnd, holeNumber, readQual, virtualFileOffset],
                names="qId, qStart, qEnd, holeNumber, readQual, virtualFileOffset")

        if (self.pbiFlags & PBI_FLAGS_MAPPED):
            tId               = peek("i4", self.nReads)
            tStart            = peek("u4", self.nReads)
            tEnd              = peek("u4", self.nReads)
            aStart            = peek("u4", self.nReads)
            aEnd              = peek("u4", self.nReads)
            isReverseStrand   = peek("u1", self.nReads)
            nM                = peek("u4", self.nReads)
            nMM               = peek("u4", self.nReads)
            mapQV             = peek("u1", self.nReads)

            mapping = np.rec.fromarrays(
                [tId, tStart, tEnd, aStart, aEnd, isReverseStrand, nM, nMM, mapQV],
                names="tId, tStart, tEnd, aStart, aEnd, isReverseStrand, nM, nMM, mapQV")

            tbl = nlr.merge_arrays([tbl, mapping], flatten=True).view(np.recarray)

        if (self.pbiFlags & PBI_FLAGS_BARCODE_ADAPTER):
            # TODO!
            pass

        self._tbl = tbl

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
                raise IOError, "Malformed bam.pbi file: " + str(e)

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
            raise AttributeError, "pbi has no column named '%s'" % columnName

    def __getitem__(self, rowNumber):
        # We do this dance to get a useable recarray slice--to
        # work around https://github.com/numpy/numpy/issues/3581
        if not np.isscalar(rowNumber):
            raise Exception, "Unimplemented!"
        return np.rec.fromrecords([self._tbl[rowNumber]],
                                  dtype=self._tbl.dtype)[0]

    def __dir__(self):
        # Special magic for IPython tab completion
        return self.columnNames

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


f = PacBioBamIndex("/Users/dalexander/Dropbox/Sources/git-bifx/PostPrimary/pbbam/tests/data/test_group_query/test2.bam.pbi")
