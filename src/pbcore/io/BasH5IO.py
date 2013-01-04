#################################################################################
# Copyright (c) 2011-2013, Pacific Biosciences of California, Inc.
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

#!/usr/bin/env python
import os
import sys
import argparse
import logging

from h5py import File
import numpy as n

#
# These APIs are deprecated.  Please use `BasH5Reader` instead.
#


QVTYPES = ['SubstitutionQV', 'DeletionQV', 'InsertionQV', 'QualityValue']

###########
# Core bas.h5 Data Group classes

class BaseCallsDataGroup(object):
    """
    .. deprecated:

        Use `BasH5Reader` instead.

    """
    def __init__(self, bash5file, baseCallRoot, allowCaching=True):
        self.allowCaching = allowCaching
        self.baseCallType = 'Raw'
        self.baseCallsDG = bash5file[baseCallRoot]
        self.ZMWDG = self.baseCallsDG['ZMW']
        self.numEvent = self.ZMWDG['NumEvent'][:]
        self.holeNumber = self.ZMWDG['HoleNumber'][:]
        self.holeStatus = self.ZMWDG['HoleStatus'][:]
        self.hn2status = dict(zip(self.holeNumber, self.holeStatus))

        holeType = self.ZMWDG['HoleStatus'].attrs['LookupTable']
        self._holeTypeDict = dict(zip(range(len(holeType)), list(holeType)))

        endOffset = n.cumsum(self.numEvent)
        beginOffset = n.hstack( (n.array([0]), endOffset[0:-1] ) )
        offsets = n.vstack ( (beginOffset, endOffset) )
        self.hn2offsets = dict(zip(self.holeNumber, zip(*offsets)))

        self._QVCache = {}
        
        self.hn2readscore = {}
        if 'ZMWMetrics' in self.baseCallsDG.keys():
            self.hn2readscore = dict(zip(self.holeNumber, self.baseCallsDG['ZMWMetrics/ReadScore'][:]))

    def getReadScoreForZMW(self, hn):
        return self.hn2readscore.get(hn, n.nan)

    def getQVDataSet(self, qvtype):
        QVDS = None
        if qvtype in QVTYPES:            
            if self._QVCache.has_key(qvtype):
                QVDS = self._QVCache[qvtype]
            else:
                QVDS = self.baseCallsDG[qvtype][:]
                QVDS = (QVDS.astype(int) + 33).clip(min=None, max=126)
                if self.allowCaching:
                    self._QVCache[qvtype] = QVDS
        return QVDS

    def getQVForZMW(self, hn, qvtype):
        b, e = self.hn2offsets[hn]
        QVS = None
        if qvtype in QVTYPES:
            QVS = self.getQVDataSet(qvtype)[b:e]
        return QVS

    def getBaseCallLenForZMW(self, hn):
        b, e = self.getSliceForZMW(hn)
        return e - b

    def getBaseCallForZMW(self, hn):
        b, e = self.getSliceForZMW(hn)
        if b != e:
            return ''.join([chr(c) for c in self.baseCallsDG['Basecall'][b:e]])
        else:
            return ''

    def getSliceForZMW(self, hn):
        return self.hn2offsets[hn]

    def getStatusForZMW(self, hn):
        return self.hn2status[hn]

    def getStatusStringForZMW(self, hn):
        return self._holeTypeDict[self.getStatusForZMW(hn)]

class CCSBaseCallsDataGroup(BaseCallsDataGroup):
    """
    .. deprecated:

        Use `BasH5Reader` instead.

    """

    def __init__(self, bash5file, baseCallRoot):
        super(CCSBaseCallsDataGroup, self).__init__(bash5file, baseCallRoot)
        self.baseCallType = 'CCS'
        self.CCSNumPasses = self.baseCallsDG['Passes/NumPasses']
        self.passDirection = self.baseCallsDG['Passes/PassDirection']
        self.passNumBases = self.baseCallsDG['Passes/PassNumBases']
        self.passStartBase = self.baseCallsDG['Passes/PassStartBase']
        self.adapterHitAfter = self.baseCallsDG['Passes/AdapterHitAfter']
        self.adapterHitBefore = self.baseCallsDG['Passes/AdapterHitBefore']
        self.hn2NumPasses = dict(zip(self.holeNumber, self.CCSNumPasses[:]))

        endOffset = n.cumsum(self.CCSNumPasses)
        beginOffset = n.hstack( (n.array([0]), endOffset[0:-1] ) )
        offsets = n.vstack ( (beginOffset, endOffset) )
        self.hn2passesOffset = dict(zip(self.holeNumber, zip(*offsets)))
        
    def getNumberOfPassesForZMW(self, hn):
        return self.hn2NumPasses[hn]

    def getCCSSubreadsRegionsForZMW(self, hn):
        b, e = self.hn2passesOffset[hn]
        start = self.passStartBase[b:e]
        nbases = self.passNumBases[b:e]
        directions = self.passDirection[b:e]
        return zip(start, start+nbases, directions)

class RegionTable(object):
    """
    .. deprecated:

        Use `BasH5Reader` instead.

    """
    def __init__(self, bash5file, datagroup='/PulseData/Regions'):
        self.rgnDS = bash5file[datagroup]
        # [Adapter Insert HQRegion]
        index2rt = dict(zip(range(len(self.rgnDS.attrs['RegionTypes'])), self.rgnDS.attrs['RegionTypes']))
        rt2index = dict( [ (x[1],x[0]) for x in index2rt.items()])
        HQRegionIndex = rt2index['HQRegion']
        insertIndex = rt2index['Insert']
        adapterIndex = rt2index['Adapter']

        # index2rtname = dict(zip(range(len(self.rgnDS.attrs['ColumnNames'])), self.rgnDS.attrs['ColumnNames']))
        # {0: HoleNumber, 1: Region type index, 2: Region start in bases, 3: Region end in bases, 4: Region score}
        rgnDS = self.rgnDS[:]
        rgnType = rgnDS[...,1]
        self.hn2HQRegion = dict( zip(rgnDS[rgnType == HQRegionIndex,0], rgnDS[rgnType == HQRegionIndex,2:]))
        hn2Inserts = zip(rgnDS[rgnType == insertIndex,0], rgnDS[rgnType == insertIndex,2:4])
        self.hn2Inserts = {}
        for hn, insertRgn in hn2Inserts:
            self.hn2Inserts.setdefault(hn, [])
            self.hn2Inserts[hn].append(insertRgn)
            
        hn2Adapters = zip(rgnDS[rgnType == adapterIndex,0], rgnDS[rgnType == adapterIndex,2:4])
        self.hn2Adapters = {}
        for hn, aptRgn in hn2Adapters:
            self.hn2Adapters.setdefault(hn, [])
            self.hn2Adapters[hn].append(aptRgn)

    def getHQRegionForZMW(self, hn):
        r = self.hn2HQRegion[hn]
        return r[0:2], r[2]/1000.0

    def getInsertRegionForZMW(self, hn):
        return self.hn2Inserts.get(hn, [])

    def getAdapterRegionForZMW(self, hn):
        return self.hn2Adapters.get(hn, [])

###########
# Core bas.h5 File handling classes

class BasH5(object):
    """
    This class is deprecated.

    .. deprecated:: 0.3.0
        Use `BasH5Reader` instead.

    """
    def __init__(self, filename, readType='Raw'):
        self._h5f = File(filename, 'r')
        self.rgnTable = RegionTable(self._h5f)
        self.baseCallsDG = None        
        if readType == 'Raw':
            self.baseCallsDG = BaseCallsDataGroup(self._h5f, '/PulseData/BaseCalls')
        elif readType == 'CCS':
            self.baseCallsDG = CCSBaseCallsDataGroup(self._h5f, '/PulseData/ConsensusBaseCalls') 
            self.rbaseCallsDG = BaseCallsDataGroup(self._h5f, '/PulseData/BaseCalls')


    def __del__(self):
        self._h5f.close()
                
    def getZMWs(self):
        for hn in self.baseCallsDG.holeNumber:
            yield hn            

    def getSequencingZMWs(self):
        for hn in self.getZMWs():
            if self.baseCallsDG.getStatusStringForZMW(hn) == 'SEQUENCING' and self.baseCallsDG.getBaseCallLenForZMW(hn):
                yield hn


