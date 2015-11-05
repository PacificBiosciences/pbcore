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

__all__ = [ "AlignmentReaderMixin",
            "AlignmentRecordMixin",
            "IndexedAlignmentReaderMixin" ]

from pbcore.io import BasH5Collection
import numpy as np

class AlignmentReaderMixin(object):
    """
    Mixin class for higher-level functionality of alignment file
    readers.
    """
    def attach(self, fofnFilename):
        """
        Attach the actual movie data files that were used to create this
        alignment file.
        """
        self.basH5Collection = BasH5Collection(fofnFilename)

    @property
    def moviesAttached(self):
        return (hasattr(self, "basH5Collection") and self.basH5Collection is not None)


class IndexedAlignmentReaderMixin(AlignmentReaderMixin):
    """
    Mixin class for alignment readers that have access to an alignment
    index.
    """
    def readsByName(self, query):
        """
        Identifies reads by name query.  The name query is interpreted as follows:

         - "movieName/holeNumber[/[*]]"      => gets all records from a chosen movie, ZMW
         - "movieName/holeNumber/rStart_rEnd => gets all records *overlapping* read range query in movie, ZMW
         - "movieName/holeNumber/ccs"        => gets CCS records from chose movie, ZMW (zero or one)

        Records are returned in a list in ascending order of rStart
        """
        def rgIDs(movieName):
            return self.readGroupTable.ID[self.readGroupTable.MovieName == movieName]
            #return self.movieInfoTable.ID[self.movieInfoTable.Name == movieName]

        def rangeOverlap(w1, w2):
            s1, e1 = w1
            s2, e2 = w2
            return (e1 > s2) and (e2 > s1)

        def rQueryMatch(readName, rQuery):
            if rQuery == "*" or rQuery == "":
                return True
            elif rQuery == "ccs":
                return readName.endswith("ccs")
            elif readName.endswith("ccs"):
                return False
            else:
                q = map(int, rQuery.split("_"))
                r = map(int, readName.split("/")[-1].split("_"))
                return rangeOverlap(q, r)

        fields = query.split("/")
        movieName = fields[0]
        holeNumber = int(fields[1])
        if len(fields) > 2: rQuery = fields[2]
        else:               rQuery = "*"

        rgs = rgIDs(movieName)
        rns = np.flatnonzero(np.in1d(self.qId, rgs) &
                             (self.holeNumber == holeNumber))
        alns = [ a for a in self[rns]
                 if rQueryMatch(a.readName, rQuery) ]
        return sorted(alns, key=lambda a: a.readStart)


    def readsByHoleNumber(self, hn):
        """
        Identify reads by hole number, for single-movie alignment files.

        Raises a ValueError for alignment files that are not single-movie
        """
        movieNames = list(self.movieNames)
        if len(movieNames) != 1:
            raise ValueError, "readsByHoleNumber expects a single-movie file"
        else:
            return self.readsByName(movieNames[0] + "/" + str(hn))


class AlignmentRecordMixin(object):
    """
    Mixin class providing some higher-level functionality for
    alignment records.
    """
    @property
    def zmw(self):
        if not self.reader.moviesAttached:
            raise ValueError("Movies not attached!")
        return self.reader.basH5Collection[self.zmwName]

    @property
    def zmwRead(self):
        if not self.reader.moviesAttached:
            raise ValueError("Movies not attached!")
        return self.reader.basH5Collection[self.readName]

    @property
    def referenceStart(self):
        """
        The left bound of the alignment, in reference coordinates.
        """
        return self.tStart

    @property
    def referenceEnd(self):
        """
        The right bound of the alignment, in reference coordinates.
        """
        return self.tEnd

    @property
    def readStart(self):
        """
        The left bound of the alignment, in read coordinates (from the BAS.H5 file).
        """
        return self.aStart

    @property
    def readEnd(self):
        """
        The right bound of the alignment, in read coordinates (from the BAS.H5 file).
        """
        return self.aEnd

    @property
    def referenceSpan(self):
        """
        The length along the reference implied by this alignment.
        """
        return self.tEnd - self.tStart

    @property
    def readLength(self):
        """
        The length of the read.
        """
        return self.aEnd - self.aStart

    def __len__(self):
        return self.readLength

    @property
    def readName(self):
        """
        Return the name of the read that was aligned, in standard
        PacBio format.
        """
        zmwName = self.zmwName
        if self.readType == "CCS":
            return "%s/ccs" % (zmwName,)
        else:
            return "%s/%d_%d" % (zmwName, self.aStart, self.aEnd)

    @property
    def zmwName(self):
        return "%s/%d" % (self.movieName, self.HoleNumber)

    def spansReferencePosition(self, pos):
        """
        Does the alignment span the given reference position?
        """
        return self.tStart <= pos < self.tEnd

    def spansReferenceRange(self, start, end):
        """
        Does the alignment span the given reference range, in its entirety?
        """
        assert start <= end
        return (self.tStart <= start <= end <= self.tEnd)

    def overlapsReferenceRange(self, start, end):
        """
        Does the alignment overlap the given reference interval?
        """
        assert start <= end
        return (self.tStart < end) and (self.tEnd > start)

    def containedInReferenceRange(self, start, end):
        """
        Is the alignment wholly contained within a given reference interval?
        """
        assert start <= end
        return (start <= self.tStart <= self.tEnd <= end)
