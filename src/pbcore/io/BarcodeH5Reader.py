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
import os
import logging

import h5py as h5
import numpy as n

from pbcore.io.BasH5Reader import *
from pbcore.io.CmpH5Reader import *

BARCODE_DELIMITER = "--"
BC_DS_PATH        = "BarcodeCalls/best"
BC_DS_ALL_PATH    = "BarcodeCalls/all"

class LabeledZmw(object):
    """A scored ZMW represents a ZMW object and its corresponding
    barcode scores."""
    def __init__(self, holeNumber, nScored, bestIdx, bestScore, 
                 secondBestIdx, secondBestScore, allScores):
        self._holeNumber = holeNumber
        self._nScored = nScored
        self._bestIdx = bestIdx
        self._bestScore = bestScore
        self._secondBestIdx = secondBestIdx
        self._secondBestScore = secondBestScore
        self._allScores = allScores

    def toBestRecord(self):
        return (self.holeNumber, self.nScored, self.bestIdx, 
                self.bestScore, self.secondBestIdx, self.secondBestScore)
    
    @staticmethod
    def fromBestRecord(npRow):
        return LabeledZmw(npRow[0], npRow[1], npRow[2],
                          npRow[3], npRow[4], npRow[5], None) 
    @property
    def holeNumber(self):
        return self._holeNumber
    @property
    def nScored(self):
        return self._nScored
    @property
    def bestIdx(self):
        return self._bestIdx
    @property
    def bestScore(self):
        return self._bestScore
    @property
    def averageScore(self):
        return 0 if self.nScored <= 0 else self.bestScore/self.nScored
    @property
    def scoreRatio(self):
        return 1 if self.secondBestScore == 0 or self.bestScore == 0 else \
            self.bestScore/(1.0 * self.secondBestScore)
    @property
    def secondBestIdx(self):
        return self._secondBestIdx
    @property
    def secondBestScore(self):
        return self._secondBestScore
    @property
    def allScores(self):
        return self._allScores

    def __repr__(self):
        return "(holeNumber = %d, nScored = %d, bestIdx = %d, bestScore = %d, averageScore = %d)" % \
            (self.holeNumber, self.nScored, self.bestIdx, self.bestScore, self.averageScore)


def writeBarcodeH5(labeledZmws, labeler, outFile, 
                   writeExtendedInfo = False):
    """Write a barcode file from a list of labeled ZMWs"""
    bestScores = map(lambda z: z.toBestRecord(), labeledZmws)
    outDta = n.vstack(bestScores)
    outH5 = h5.File(outFile, 'a')

    if BC_DS_PATH in outH5:
        del outH5[BC_DS_PATH]

    bestDS = outH5.create_dataset(BC_DS_PATH, data = outDta, dtype = "int32")
    bestDS.attrs['movieName'] = labeler.movieName
    bestDS.attrs['barcodes'] = n.array(labeler.barcodeLabels, dtype = h5.new_vlen(str))
    bestDS.attrs['columnNames'] = n.array(['holeNumber', 'nAdapters', 'barcodeIdx1', 
                                           'barcodeScore1', 'barcodeIdx2', 'barcodeScore2'], 
                                          dtype = h5.new_vlen(str))
    bestDS.attrs['scoreMode'] = labeler.scoreMode

    if writeExtendedInfo:
        # here we use the 'names' because each barcode is scored
        # individually.
        nBarcodes = len(labeler.barcodeNames)

        def makeArray(l, v):
            a = n.zeros(l, dtype = type(v))
            a.fill(v)
            return a
        
        def makeRecord(lZmw):
            zmws = makeArray(nBarcodes * lZmw.nScored, lZmw.holeNumber)
            adapters = n.concatenate([makeArray(nBarcodes, i) for i in \
                                          xrange(1, lZmw.nScored + 1)])
            idxs = n.concatenate([range(0, nBarcodes) for i in \
                                      xrange(0, lZmw.nScored)])
            scores = n.concatenate(lZmw.allScores)
            return n.transpose(n.vstack((zmws, adapters, idxs, scores)))

        records = [makeRecord(lZmw) for lZmw in labeledZmws if lZmw.allScores]
        records = n.vstack(records)
    
        if BC_DS_ALL_PATH in outH5:
            del outH5[BC_DS_ALL_PATH]
        allDS = outH5.create_dataset(BC_DS_ALL_PATH, data = records, dtype = 'int32')
        allDS.attrs['movieName'] = labeler.movieName
        # note names versus labels.
        allDS.attrs['barcodes'] = n.array(labeler.barcodeNames, dtype = h5.new_vlen(str))
        allDS.attrs['columnNames'] = n.array(['holeNumber', 'adapter', 'barcodeIdx', 'score'], 
                                             dtype = h5.new_vlen(str))

    outH5.close()

#
# The reader interface
#
def create(movieName):
    # XXX : Detecting multi-part; pretty ugly. 
    if os.path.exists(movieName + '.bc.h5'):
        logging.debug("Instantiating BarcodeH5Reader")
        return BarcodeH5Reader(movieName + '.bc.h5')
    else:
        logging.debug("Instantiating MPBarcodeReader")
        # XXX : that 1,2,3 needs to be fixed
        parts = map(lambda z : '.'.join((movieName, str(z), 'bc.h5')), [1,2,3])
        logging.debug("Trying to load parts:" + '\n'.join(parts))
        parts = filter(lambda p : os.path.exists(p), parts)

        if parts:
            return MPBarcodeH5Reader(parts)
        else:
            raise Exception("Unable to instantiate a BarcodeH5Reader")

class MPBarcodeH5Reader(object):
    def __init__(self, fnames):
        self.parts = map(BarcodeH5Reader, fnames)
        def rng(x):
            return (n.min(x), n.max(x))
        # these aren't the ranges of ZMWs, but the ranges for the
        # scored ZMWs.
        self.bins = map(lambda z : rng(z.bestDS[:,0]), self.parts)

    def choosePart(self, holeNumber):
        for i,b in enumerate(self.bins):
            if holeNumber >= b[0] and holeNumber <= b[1]:
                return self.parts[i]
        # Return None meaning the zmw is ouf of the range of
        # the scored ZMWs for all parts.
        return None

    @property
    def barcodeLabels(self):
        return self.parts[0].barcodeLabels
    @property
    def scoreMode(self):
        return self.parts[0].scoreMode
    
    def labeledZmwFromHoleNumber(self, holeNumber):
        """Returns a LabeledZmw object from the holeNumber"""
        part = self.choosePart(holeNumber)
        if part:
            return part.labeledZmwFromHoleNumber(holeNumber)
        else:
            raise KeyError("holeNumber: %d not labeled" % holeNumber)
    
    def labeledZmwsFromBarcodeLabel(self, bcLabel):
        return reduce(lambda x,y: x+y, 
                      map(lambda z: z.labeledZmwsFromBarcodeLabel(bcLabel), 
                          self.parts))
    
    
    # def getBarcodeTupleForZMW(self, holeNumber):
    #     part = self.choosePart(holeNumber)
    #     if part:
    #         return part.getBarcodeTupleForZMW(holeNumber)
    #     else:
    #         # I have not scored this alignment, therefore we return the
    #         # NULL tuple
    #         return self.parts[0].nullBarcodeTuple()

    # def getExtendedBarcodeInfoForZMW(self, holeNumber):
    #     part = self.choosePart(holeNumber)
    #     if part:
    #         return part.getExtendedBarcodeInfoForZMW(holeNumber)
    #     else:
    #         return None

    # def getZMWsForBarcode(self, barcodeName):
    #     raise NotImplementedError("Directly use BarcodeH5Reader for this task")
    
    # def getBarcodeLabels(self):
    #     return self.parts[0].getBarcodeLabels()
    # def getScoreMode(self):
    #     return self.parts[0].getScoreMode()
    # def nullBarcodeTuple(self):
    #     return self.parts[0].nullBarcodeTuple()
    
    
class BarcodeH5Reader(object):
    def __init__(self, fname):
        self.h5File = h5.File(fname, 'r')
        self.bestDS = self.h5File[BC_DS_PATH]

        self._scoreMode = self.bestDS.attrs['scoreMode']
        self._barcodeLabels = self.bestDS.attrs['barcodes']
        
        # zmw => LabeledZmw
        labeledZmws = [LabeledZmw.fromBestRecord(self.bestDS[i,:]) for i in 
                       xrange(0, self.bestDS.shape[0])]
        self.labeledZmws = dict([(lZmw.holeNumber, lZmw) for lZmw in labeledZmws])
        
        # barcode => LabeledZmws
        self.bcLabelToLabeledZmws = {l:[] for l in self.barcodeLabels}
        for lZmw in self.labeledZmws.values():
            # XXX : why doesn't LabeledZmw have a .bestLabel?
            d = self.bcLabelToLabeledZmws[self.barcodeLabels[lZmw.bestIdx]]
            d.append(lZmw)

        # from IPython import embed; embed()
        
        # ## note: I hack off the ZMW.
        # self.holeNumberToBC = dict(zip(self.bestDS[:,0],
        #                                self.bestDS[:,1:self.bestDS.shape[1]]))
             
        # ## init the bcLabels according to the scoreMode. 
        # if self.scoreMode == 'symmetric':
        #     bcLabels = [makeBCLabel(a, b) for a,b in zip(self.barcodes, self.barcodes)]
            
        # elif self.scoreMode == 'paired':
        #     bcLabels = [makeBCLabel(self.barcodes[i], self.barcodes[i+1]) 
        #                 for i in xrange(0, len(self.barcodes), 2)]
        # else:
        #     raise Exception("Unknown scoreMode in BarcodeH5Reader:" + self.scoreMode)
        # ## add the null.
        # bcLabels.append(NULL_BARCODE)

        # ## initialize the labels and the label map.
        # self.bcLabels   = bcLabels
        # self.labelToIdx = dict([(v,k) for (k,v) in enumerate(self.bcLabels)])

        # ## it is a little confusing because, given a scoreMode then
        # ## there is a new indexing system.
        # self.scoreModeIdx = n.array([self.getBarcodeTupleForZMW(hn)[0] 
        #                              for hn in self.bestDS[:,0]])

        # ## This will be used if we are using the extended "All" dataset.
        # self.mapToAll = None

    @property
    def barcodeLabels(self):
        return self._barcodeLabels
    @property
    def scoreMode(self):
        return self._scoreMode
    
    def labeledZmwFromHoleNumber(self, holeNumber):
        """Returns a LabeledZmw object from the holeNumber"""
        try:
            return self.labeledZmws[holeNumber]
        except KeyError:
            raise KeyError("holeNumber %d not labeled" % holeNumber)
    
    def labeledZmwsFromBarcodeLabel(self, bcLabel):
        """Returns a list of LabeledZmw objects for the particular
        barcode label, an empty list if there are no ZMWs for this
        barcode."""
        return self.bcLabelToLabeledZmws[bcLabel]


    # def getBarcodeTupleForZMW(self, holeNumber):
    #     try:
    #         d = self.holeNumberToBC[holeNumber]
    #         if self.scoreMode == 'symmetric':
    #             return (d[1], d[2], d[0])
    #         elif self.scoreMode == 'paired':
    #             return (d[1]/2, d[2], d[0])
    #         else:
    #             raise Exception("Unknown scoreMode in BarcodeH5Reader:" + 
    #                             self.scoreMode)
    #     except:
    #         return self.nullBarcodeTuple()


    # def nullBarcodeTuple(self):
    #     return (len(self.bcLabels) - 1, 0, 0)

    # def getExtendedBarcodeInfoForZMW(self, holeNumber):
    #     # we'll do this on demand
    #     if not self.mapToAll:
    #         self.mapToAll = {}
    #         self.bcAllDS  = self.h5File[BC_DS_ALL_PATH][:]
    #         for r in xrange(0, self.bcAllDS.shape[0]):
    #             z = self.bcAllDS[r, 0]
    #             if not z in self.mapToAll:
    #                 self.mapToAll[z] = (r, r)
    #             else:
    #                 self.mapToAll[z] = (self.mapToAll[z][0], r)

    #     if holeNumber in self.mapToAll:
    #         extents = self.mapToAll[holeNumber]
    #         return self.bcAllDS[extents[0]:(extents[1]+1),:]
    #     else:
    #         return None

    

    # def getZMWsForBarcode(self, barcodeName):
    #     """Returns all the ZMWs that had barcodeName mapping to it,
    #     throws a BarcodeIdxException if there aren't any ZMWs for this
    #     barcode."""
    #     bcID = self.labelToIdx[barcodeName]
    #     msk = bcID == self.scoreModeIdx
       
    #     # if msk is all false then it won't return a 0-row data
    #     # structure. Furthermore, I can't return None because then
    #     # 'if' isn't happy because in some cases it is an array and in
    #     # others it is None. Have to raise an Exception.
    #     if n.any(msk):
    #         return self.bestDS[msk,:]
    #     else:
    #         raise BarcodeIdxException()



