#################################################################################$$
# Copyright (c) 2011,2012, Pacific Biosciences of California, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of Pacific Biosciences nor the names of its contributors
#   may be used to endorse or promote products derived from this software
#   without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY PACIFIC BIOSCIENCES AND ITS CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR ITS
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#################################################################################$$

# Author: David Alexander


__all__ = [ "BasH5Reader" ]

import h5py, numpy as np, os.path
from bisect import bisect_left, bisect_right

def arrayFromDataset(ds, offsetBegin, offsetEnd):
    shape = (offsetEnd - offsetBegin,)
    a = np.ndarray(shape=shape, dtype=ds.dtype)
    mspace = h5py.h5s.create_simple(shape)
    fspace = ds.id.get_space()
    fspace.select_hyperslab((offsetBegin,), shape, (1,))
    ds.id.read(mspace, fspace, a)
    return a

def intersectRanges(r1, r2):
    b1, e1 = r1
    b2, e2 = r2
    b, e = max(b1, b2), min(e1, e2)
    return (b, e) if (b < e) else None

def rangeLength(r):
    b, e = r
    return e - b

def removeNones(lst):
    return filter(lambda x: x!=None, lst)

# ZMW hole Types
SEQUENCING_ZMW = 0

# Region types
ADAPTER_REGION = 0
INSERT_REGION  = 1
HQ_REGION      = 2

# Region table column numbers
HOLENUMBER_COLUMN  = 0
REGIONTYPE_COLUMN  = 1
REGIONSTART_COLUMN = 2
REGIONEND_COLUMN   = 3
REGIONSCORE_COLUMN = 4


def _makeQvAccessor(featureName):
    def f(self):
        return self.qv(featureName)
    return f

class Zmw(object):
    """
    A Zmw represents all data from a Zmw hole within a BasH5 movie
    file.  Accessor methods provide convenient access to the read (or
    subreads), and to the region table entries for this hole.

    Note that access is only permitted to data within the "HQ region"
    defined by Primary; intervals are clipped to the bounds defined by
    the HQ region.
    """
    __slots__ = [ "basH5", "holeNumber",
                  "regionTableStartRow", "regionTableEndRow" ]

    def __init__(self, basH5, holeNumber,
                 regionTableStartRow, regionTableEndRow):
        self.basH5               = basH5
        self.holeNumber          = holeNumber
        self.regionTableStartRow = regionTableStartRow
        self.regionTableEndRow   = regionTableEndRow

    @property
    def regionTable(self):
        return self.basH5.regionTable[self.regionTableStartRow:self.regionTableEndRow]

    #
    # The following calls return one or more intervals ( (int, int) ).
    # All intervals are clipped to the hqRegion.
    #

    def adapterRegions(self):
        unclippedAdapterRegions = \
           [ self.regionTable[rowNumber, (REGIONSTART_COLUMN, REGIONEND_COLUMN)]
             for rowNumber in np.where(self.regionTable[:, REGIONTYPE_COLUMN] == ADAPTER_REGION)[0] ]
        hqRegion = self.hqRegion()
        return removeNones([ intersectRanges(hqRegion, region)
                             for region in unclippedAdapterRegions ])

    def insertRegions(self):
        unclippedInsertRegions = \
           [ self.regionTable[rowNumber, (REGIONSTART_COLUMN, REGIONEND_COLUMN)]
             for rowNumber in np.where(self.regionTable[:, REGIONTYPE_COLUMN] == INSERT_REGION)[0] ]
        hqRegion = self.hqRegion()
        return removeNones([ intersectRanges(hqRegion, region)
                             for region in unclippedInsertRegions ])

    def hqRegion(self):
        isHqRegion  = (self.regionTable[:, REGIONTYPE_COLUMN] == HQ_REGION)
        return tuple(self.regionTable[isHqRegion, (REGIONSTART_COLUMN, REGIONEND_COLUMN)])

    #
    # The following calls return one or more ZmwRead objects.
    #
    def read(self, rStart=None, rEnd=None):
        hqStart, hqEnd = self.hqRegion()
        rStart = rStart or hqStart
        rEnd   = rEnd   or hqEnd
        if ((rStart > rEnd) or
            (rStart < hqStart) or
            (hqEnd  < rEnd)):
            raise IndexError, "Invalid slice of ZMW"
        else:
            return ZmwRead(self.basH5,
                           self.holeNumber,
                           rStart, rEnd)

    def subreads(self):
        return [ self.read(rStart, rEnd)
                 for (rStart, rEnd) in self.insertRegions() ]

    def adapters(self):
        return [ self.read(rStart, rEnd)
                 for (rStart, rEnd) in self.adapterRegions() ]


class ZmwRead(object):
    """
    A ZmwRead represents the data features (basecalls as well as
    pulse features) recorded from a subinterval of the span of the

    """
    __slots__ = [ "basH5", "holeNumber", "rStart", "rEnd" ]

    def __init__(self, basH5, holeNumber, rStart=None, rEnd=None):
        self.basH5      = basH5
        self.holeNumber = holeNumber
        self.rStart     = rStart
        self.rEnd       = rEnd

    @property
    def readName(self):
        return "%s/%d/%d_%d" % (self.basH5.movieName,
                                self.holeNumber,
                                self.rStart,
                                self.rEnd)

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__,
                             self.readName)

    def basecalls(self):
        baseOffset  = self.basH5._offsetsByHole[self.holeNumber][0]
        offsetBegin = baseOffset + self.rStart
        offsetEnd   = baseOffset + self.rEnd
        return arrayFromDataset(self.basH5.basecallsGroup["Basecall"],
                                offsetBegin, offsetEnd).tostring()

    def qv(self, qvName):
        baseOffset  = self.basH5._offsetsByHole[self.holeNumber][0]
        offsetBegin = baseOffset + self.rStart
        offsetEnd   = baseOffset + self.rEnd
        return arrayFromDataset(self.basH5.basecallsGroup[qvName],
                                offsetBegin, offsetEnd)

    QualityValue   = _makeQvAccessor("QualityValue")
    InsertionQV    = _makeQvAccessor("InsertionQV")
    DeletionQV     = _makeQvAccessor("DeletionQV")
    DeletionTag    = _makeQvAccessor("DeletionTag")
    MergeQV        = _makeQvAccessor("MergeQV")
    SubstitutionQV = _makeQvAccessor("SubstitutionQV")


class BasH5ReaderBase(object):

    def __init__(self, filename, basecallsGroupPath):
        self.filename = filename
        self.file = h5py.File(self.filename, "r")
        self.basecallsGroup = self.file[basecallsGroupPath]
        self.numEvent   = self.basecallsGroup["ZMW/NumEvent"].value
        self.holeNumber = self.basecallsGroup["ZMW/HoleNumber"].value
        endOffset = np.cumsum(self.numEvent)
        beginOffset = np.hstack(([0], endOffset[0:-1]))
        offsets = zip(beginOffset, endOffset)
        self._offsetsByHole = dict(zip(self.holeNumber, offsets))

    @property
    def movieName(self):
        return os.path.basename(self.filename).split('.')[0]

    def __len__(self):
        return len(self.sequencingZmws)

    def close(self):
        if hasattr(self, "file") and self.file != None:
            self.file.close()
            self.file = None
    
    def __del__(self):
        self.close()
        
    def __iter__(self):
        for holeNumber in self.sequencingZmws:
            yield self[holeNumber]

class BasH5Reader(BasH5ReaderBase):
    def __init__(self, filename):
        super(BasH5Reader, self).__init__(filename, "/PulseData/BaseCalls")
        self.regionTable = self.file["/PulseData/Regions"].value
        isHqRegion = self.regionTable[:, REGIONTYPE_COLUMN] == HQ_REGION
        hqRegions  = self.regionTable[isHqRegion, :]
        hqRegionLength = hqRegions[:, REGIONEND_COLUMN] - \
                         hqRegions[:, REGIONSTART_COLUMN]
        holeStatus  = self.basecallsGroup["ZMW/HoleStatus"].value
        self.sequencingZmws = \
            self.holeNumber[(holeStatus == SEQUENCING_ZMW) &
                            (self.numEvent  >  0)          &
                            (hqRegionLength >  0)]
        del self.numEvent
        del self.holeNumber

    def __getitem__(self, holeNumber):
        if holeNumber in self.sequencingZmws:
            offsetStart, offsetEnd = self._offsetsByHole[holeNumber]
            regionTableStartRow = bisect_left(self.regionTable[:, HOLENUMBER_COLUMN], holeNumber)
            regionTableEndRow   = bisect_right(self.regionTable[:, HOLENUMBER_COLUMN], holeNumber,
                                               lo=regionTableStartRow)
            return Zmw(self, holeNumber, regionTableStartRow, regionTableEndRow)
        else:
            return None

