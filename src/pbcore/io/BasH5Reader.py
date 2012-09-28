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


__all__ = [ "BasH5Reader", "CCSBasH5Reader" ]

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

# This seems to be the magic incantation to get a RecArray that can be
# indexed to yield a record that can then be accessed using dot
# notation.
def arrayToRecArray(dtype, arr):
    return np.rec.array(arr, dtype=dtype).flatten()

REGION_TABLE_DTYPE = [("holeNumber",  np.int32),
                      ("regionType",  np.int32),
                      ("regionStart", np.int32),
                      ("regionEnd",   np.int32),
                      ("regionScore", np.int32) ]

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
           [ (region.regionStart, region.regionEnd)
             for region in self.regionTable
             if region.regionType == ADAPTER_REGION ]
        hqRegion = self.hqRegion()
        return removeNones([ intersectRanges(hqRegion, region)
                             for region in unclippedAdapterRegions ])

    def insertRegions(self):
        unclippedInsertRegions = \
           [ (region.regionStart, region.regionEnd)
             for region in self.regionTable
             if region.regionType == INSERT_REGION ]
        hqRegion = self.hqRegion()
        return removeNones([ intersectRanges(hqRegion, region)
                             for region in unclippedInsertRegions ])

    def hqRegion(self):
        hqRegions = [ (region.regionStart, region.regionEnd)
                      for region in self.regionTable
                      if region.regionType == HQ_REGION ]
        assert len(hqRegions) == 1
        return hqRegions[0]

    #
    # The following calls return one or more ZmwRead objects.
    #
    def read(self, readStart=None, readEnd=None):
        hqStart, hqEnd = self.hqRegion()
        readStart = readStart or hqStart
        readEnd   = readEnd   or hqEnd
        if ((readStart > readEnd) or
            (readStart < hqStart) or
            (hqEnd  < readEnd)):
            raise IndexError, "Invalid slice of ZMW"
        else:
            return ZmwRead(self.basH5,
                           self.holeNumber,
                           readStart, readEnd)

    def subreads(self):
        return [ self.read(readStart, readEnd)
                 for (readStart, readEnd) in self.insertRegions() ]

    def adapters(self):
        return [ self.read(readStart, readEnd)
                 for (readStart, readEnd) in self.adapterRegions() ]


class ZmwRead(object):
    """
    A ZmwRead represents the data features (basecalls as well as pulse
    features) recorded from the ZMW, delimited by readStart and readEnd.
    """
    __slots__ = [ "basH5", "holeNumber", "readStart", "readEnd" ]

    def __init__(self, basH5, holeNumber, readStart=None, readEnd=None):
        self.basH5      = basH5
        self.holeNumber = holeNumber
        self.readStart  = readStart
        self.readEnd    = readEnd

    @property
    def readName(self):
        return "%s/%d/%d_%d" % (self.basH5.movieName,
                                self.holeNumber,
                                self.readStart,
                                self.readEnd)

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__,
                             self.readName)

    def basecalls(self):
        baseOffset  = self.basH5._offsetsByHole[self.holeNumber][0]
        offsetBegin = baseOffset + self.readStart
        offsetEnd   = baseOffset + self.readEnd
        return arrayFromDataset(self.basH5.basecallsGroup["Basecall"],
                                offsetBegin, offsetEnd).tostring()

    def qv(self, qvName):
        baseOffset  = self.basH5._offsetsByHole[self.holeNumber][0]
        offsetBegin = baseOffset + self.readStart
        offsetEnd   = baseOffset + self.readEnd
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

class CCSBasH5Reader(BasH5ReaderBase):
    def __init__(self, filename):
        super(CCSBasH5Reader, self).__init__(filename, "/PulseData/ConsensusBaseCalls")
        holeStatus  = self.basecallsGroup["ZMW/HoleStatus"].value
        self.sequencingZmws = \
            self.holeNumber[(holeStatus == SEQUENCING_ZMW) &
                            (self.numEvent  >  0)]

    def __getitem__(self, holeNumber):
        if holeNumber in self.sequencingZmws:
            ## I am grabbing the entire read here, where length is
            ## computed as below.
            offsetStart, offsetEnd = self._offsetsByHole[holeNumber]
            return ZmwRead(self, holeNumber, 0, offsetEnd - offsetStart)
        else:
            return None

class BasH5Reader(BasH5ReaderBase):
    def __init__(self, filename):
        super(BasH5Reader, self).__init__(filename, "/PulseData/BaseCalls")
        self.regionTable = arrayToRecArray(REGION_TABLE_DTYPE,
                                           self.file["/PulseData/Regions"].value)
        isHqRegion = self.regionTable.regionType == HQ_REGION
        hqRegions  = self.regionTable[isHqRegion, :]
        hqRegionLength = hqRegions.regionEnd - hqRegions.regionStart
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
            regionTableStartRow = bisect_left(self.regionTable.holeNumber, holeNumber)
            regionTableEndRow   = bisect_right(self.regionTable.holeNumber, holeNumber,
                                               lo=regionTableStartRow)
            return Zmw(self, holeNumber, regionTableStartRow, regionTableEndRow)
        else:
            return None

