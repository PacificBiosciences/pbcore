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

# Authors: David Alexander

__all__ = [ "PlxH5Reader" ]

from .BasH5IO import (BaxH5Reader, Zmw, ZmwRead, _makeOffsetsDataStructure, arrayFromDataset)

import numpy as np

class PlxZmw(Zmw):
    __slots__ = [ "plxH5", "plxIndex"]

    def __init__(self, plxH5, holeNumber):
        super(PlxZmw, self).__init__(plxH5, holeNumber)
        self.plxH5 = plxH5
        self.plxIndex = self.plxH5._plxHoleNumberToIndex[holeNumber]

        # It's structurally possible that plxIndex differs from index,
        # but it really should never happen.
        assert self.index == self.plxIndex

    def baseline(self):
        pass

    def baselineSigma(self):
        pass

    def holeXY(self):
        pass

    def pulsesByBaseInterval(self, beginBase, endBase):
        pulseIndex = self.readNoQC().PulseIndex()
        pulseStart = pulseIndex[beginBase]
        pulseEnd   = pulseIndex[endBase]
        return ZmwPulses(self.plxH5, self.holeNumber, pulseStart, pulseEnd)

    def pulsesByPulseInterval(self, beginPulse, endPulse):
        return ZmwPulses(self.plxH5, self.holeNumber, beginPulse, endPulse)

    def pulses(self):
        zmwOffsetBegin, zmwOffsetEnd = self._getPlxOffsets()[self.holeNumber]
        numEvents = zmwOffsetEnd - zmwOffsetBegin
        return ZmwPulses(self.plxH5, self.holeNumber, 0, numEvents)

    # metrics? pulserate, pulseratevst


class ZmwPulses(object):

    __slots__ = [ "plxH5", "holeNumber",
                  "pulseStart", "pulseEnd",
                  "plxOffsetBegin", "plxOffsetEnd" ]

    def __init__(self, plxH5, holeNumber, pulseStart, pulseEnd):
        self.plxH5       = plxH5
        self.holeNumber  = holeNumber
        self.pulseStart  = pulseStart
        self.pulseEnd    = pulseEnd
        zmwOffsetBegin, zmwOffsetEnd = self._getPlxOffsets()[self.holeNumber]
        self.plxOffsetBegin = zmwOffsetBegin + self.pulseStart
        self.plxOffsetEnd   = zmwOffsetBegin + self.pulseEnd
        if not (zmwOffsetBegin   <=
                self.plxOffsetBegin <=
                self.plxOffsetEnd   <=
                zmwOffsetEnd):
            raise IndexError, "Invalid slice of PlxZmw!"

    def _getPulsecallsGroup(self):
        return self.plxH5._pulsecallsGroup

    def _getPlxOffsets(self):
        return self.plxH5._plxOffsetsByHole

    def channel(self):
        return arrayFromDataset(self._getPulsecallsGroup()["Channel"],
                                self.plxOffsetBegin, self.plxOffsetEnd)
    def channelBases(self):
        CHANNEL_BASES = np.fromstring("TGAC", dtype=np.uint8)
        return CHANNEL_BASES[self.channel()].tostring()

    def startFrame(self):
        return arrayFromDataset(self._getPulsecallsGroup()["StartFrame"],
                                self.plxOffsetBegin, self.plxOffsetEnd)

    def widthInFrames(self):
        return arrayFromDataset(self._getPulsecallsGroup()["WidthInFrames"],
                                self.plxOffsetBegin, self.plxOffsetEnd)

    def prePulseFrames(self):
        begin, end = (self.plxOffsetBegin, self.plxOffsetEnd)
        begin_ = max(0, begin - 1)
        prePulseFrames_ = arrayFromDataset(self._getPulsecallsGroup()["StartFrame"],
                                           begin_, end)
        widthInFrames_  = arrayFromDataset(self._getPulsecallsGroup()["WidthInFrames"],
                                           begin_, end)
        prePulseFrames_[1:] -= prePulseFrames_[:-1] + widthInFrames_[:-1]
        if (begin > 0): return prePulseFrames_[1:]
        else:           return prePulseFrames_

    def midSignal(self):
        return arrayFromDataset(self._getPulsecallsGroup()["MidSignal"],
                                self.plxOffsetBegin, self.plxOffsetEnd)

    def meanSignal(self):
        return arrayFromDataset(self._getPulsecallsGroup()["MeanSignal"],
                                self.plxOffsetBegin, self.plxOffsetEnd)

    def maxSignal(self):
        return arrayFromDataset(self._getPulsecallsGroup()["MaxSignal"],
                                self.plxOffsetBegin, self.plxOffsetEnd)

    def isPulse(self):
        return arrayFromDataset(self._getPulsecallsGroup()["IsPulse"],
                                self.plxOffsetBegin, self.plxOffsetEnd)

    def isBase(self):
        numEvents = len(self)
        isBase_ = np.zeros((numEvents,), dtype=np.bool)
        pulseIndex = self.plxH5[self.holeNumber].readNoQC().PulseIndex()
        pulseIndex = pulseIndex[self.pulseStart:self.pulseEnd]
        isBase_[pulseIndex] = True
        return isBase_

    def __len__(self):
        return self.pulseEnd - self.pulseStart


class PlxH5Reader(BaxH5Reader):

    def __init__(self, filename):
        super(PlxH5Reader, self).__init__(filename)
        self._pulsecallsGroup = self.file["/PulseData/PulseCalls"]
        holeNumbers = self._pulsecallsGroup["ZMW/HoleNumber"][:]
        self._plxHoleNumberToIndex = dict(zip(holeNumbers, range(len(holeNumbers))))
        self._plxOffsetsByHole = _makeOffsetsDataStructure(self._pulsecallsGroup)

        # convenience array to hold pre-pulse frames
        prePulseFrames = np.copy(self._pulsecallsGroup["StartFrame"].value)
        prePulseFrames[1:] -= prePulseFrames[:-1] + self._pulseCallsGroup["WidthInFrames"].value[:-1]
        self._prePulseFrames = prePulseFrames

    def __getitem__(self, holeNumber):
        return PlxZmw(self, holeNumber)
