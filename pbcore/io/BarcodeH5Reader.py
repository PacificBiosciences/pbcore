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

from pbcore.io import BasH5Reader, BaxH5Reader
from pbcore.io import CmpH5Reader, CmpH5Alignment

BARCODE_DELIMITER = "--"
BC_DS_PATH        = "BarcodeCalls/best"
BC_DS_ALL_PATH    = "BarcodeCalls/all"

class LabeledZmw(object):
    """A scored ZMW represents a ZMW object and its corresponding
    barcode scores. Some fields are considered optional"""
    def __init__(self, holeNumber, nScored, bestIdx, bestScore, 
                 secondBestIdx = -1, secondBestScore = 0, 
                 allScores = None):
        self._holeNumber = holeNumber
        self._nScored = nScored
        self._bestIdx = bestIdx
        self._bestScore = bestScore
        self._secondBestIdx = secondBestIdx
        self._secondBestScore = secondBestScore
        self._allScores = allScores

    def toBestRecord(self):
        """Return a summary record suitable for storage"""
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
    """Write a barcode file from a list of labeled ZMWs. In addition
    to labeledZmws, this function takes a
    pbtools.pbbarcode.BarcodeLabeler."""
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
    # close the file at the very end.
    outH5.close()

class BarcodeH5Reader(object):
    def __init__(self, fname):
        self.h5File = h5.File(fname, 'r')
        self.bestDS = self.h5File[BC_DS_PATH]

        self._scoreMode = self.bestDS.attrs['scoreMode']
        self._barcodeLabels = self.bestDS.attrs['barcodes']
        self._movieName = self.bestDS.attrs['movieName']
        # zmw => LabeledZmw
        labeledZmws = [LabeledZmw.fromBestRecord(self.bestDS[i,:]) for i in 
                       xrange(0, self.bestDS.shape[0])]
        self.labeledZmws = dict([(lZmw.holeNumber, lZmw) for lZmw in labeledZmws])
        
        # barcode => LabeledZmws
        self.bcLabelToLabeledZmws = {l:[] for l in self.barcodeLabels}
        for lZmw in self.labeledZmws.values():
            d = self.bcLabelToLabeledZmws[self.barcodeLabels[lZmw.bestIdx]]
            d.append(lZmw)

    @property
    def holeNumbers(self):
        return self.labeledZmws.keys()
    @property
    def barcodeLabels(self):
        return self._barcodeLabels
    @property
    def scoreMode(self):
        return self._scoreMode
    @property 
    def movieName(self):
        return self._movieName
    
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

class MPBarcodeH5Reader(object):
    def __init__(self, parts):
        self._parts = parts
        def rng(x):
            return (n.min(x), n.max(x))
        # these aren't the ranges of ZMWs, but the ranges for the
        # scored ZMWs.
        self._bins = map(lambda z : rng(z.holeNumbers), self._parts)

    def choosePart(self, holeNumber):
        for i,b in enumerate(self._bins):
            if holeNumber >= b[0] and holeNumber <= b[1]:
                return self._parts[i]
        # Return None meaning the zmw is ouf of the range of
        # the scored ZMWs for all parts.
        return None

    @property
    def barcodeLabels(self):
        return self._parts[0].barcodeLabels
    @property
    def scoreMode(self):
        return self._parts[0].scoreMode
    
    def labeledZmwFromHoleNumber(self, holeNumber):
        """Returns a LabeledZmw object from the holeNumber"""
        part = self.choosePart(holeNumber)
        if part:
            return part.labeledZmwFromHoleNumber(holeNumber)
        else:
            raise KeyError("holeNumber: %d not labeled" % holeNumber)
    
    def labeledZmwsFromBarcodeLabel(self, bcLabel):
        return reduce(lambda x,y: x + y, 
                      map(lambda z: z.labeledZmwsFromBarcodeLabel(bcLabel), 
                          self._parts))

class BarcodeH5Fofn(object):
    def __init__(self, inputFofn):
        self._bcH5s = [BarcodeH5Reader(fname) for fname in 
                       open(inputFofn).read().splitlines()]
        self._byMovie = {}
        for bc in self._bcH5s:
            if bc.movieName not in self._byMovie:
                self._byMovie[bc.movieName] = [bc]
            else:
                self._byMovie[bc.movieName].append(bc)
        
        self.mpReaders = {movieName: parts[0] if len(parts) == 1 else \
                              MPBarcodeH5Reader(parts) for movieName, parts in
                          self._byMovie.iteritems()}
    
    def readerForMovie(self, movieName):
        """Return a BarcodeH5Reader for a movieName"""
        return self.mpReaders[movieName]

    @property
    def barcodeLabels(self):
        return self._bcH5s[0].barcodeLabels

    @property
    def scoreMode(self):
        return self._bcH5s[0].scoreMode
    
