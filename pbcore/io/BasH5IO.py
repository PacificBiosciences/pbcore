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

# Authors: David Alexander, Jim Bullard

__all__ = [ "BasH5Reader"     ,
            "BaxH5Reader"     ,
            "BasH5Collection" ]

import h5py, numpy as np, os.path as op
from bisect import bisect_left, bisect_right
from operator import getitem
from itertools import groupby
from collections import OrderedDict

from pbcore.io.FofnIO import readFofn
from pbcore.chemistry import (decodeTriple,
                              tripleFromMetadataXML,
                              ChemistryLookupError)
from pbcore.model import ExtraBaseRegionsMixin, HQ_REGION
from ._utils import arrayFromDataset, CommonEqualityMixin


# ZMW hole Types
SEQUENCING_ZMW = 0

# This seems to be the magic incantation to get a RecArray that can be
# indexed to yield a record that can then be accessed using dot
# notation.
def toRecArray(dtype, arr):
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

class Zmw(CommonEqualityMixin, ExtraBaseRegionsMixin):
    """
    A Zmw represents all data from a ZMW (zero-mode waveguide) hole
    within a bas.h5 movie file.  Accessor methods provide convenient
    access to the read (or subreads), and to the region table entries
    for this hole.
    """
    __slots__ = [ "baxH5", "holeNumber", "index"]

    def __init__(self, baxH5, holeNumber):
        self.baxH5               = baxH5
        self.holeNumber          = holeNumber
        self.index               = self.baxH5._holeNumberToIndex[holeNumber]

    @property
    def regionTable(self):
        if self.holeNumber in self.baxH5._regionTableIndex:
            startRow, endRow = self.baxH5._regionTableIndex[self.holeNumber]
            return self.baxH5.regionTable[startRow:endRow]
        else:
            # Broken region table---primary pipeline bug (see bugs
            # 23585, 25273).  Work around this by returning a fake
            # regiontable consisting of an empty HQ region
            return toRecArray(REGION_TABLE_DTYPE,
                              [ (self.holeNumber, HQ_REGION, 0, 0, 0) ])


    @property
    def readScore(self):
        """
        Return the "read score", a prediction of the accuracy (between 0 and 1) of the
        basecalls from this ZMW, from the `ReadScore` dataset in the
        file
        """
        return self.zmwMetric("ReadScore")

    @property
    def productivity(self):
        """
        Return the 'productivity' of this ZMW, which is the estimated
        number of polymerase reactions taking place within it.  For
        example, a doubly-loaded ZMW would have productivity 2.
        """
        return self.zmwMetric("Productivity")

    @property
    def hqRegionSnr(self):
        """
        Return the SNRs, as a vector by channel.
        """
        return self.zmwMetric("HQRegionSNR")

    def zmwMetric(self, name):
        """
        Return the value of metric 'name' from the ZMW metrics.
        """
        return self.baxH5.zmwMetric(name, self.index)

    def listZmwMetrics(self):
        """
        List the available ZMW metrics for this bax.h5 file.
        """
        return self.baxH5.listZmwMetrics()

    @property
    def numPasses(self):
        """
        Return the number of passes (forward + back) across the SMRTbell
        insert, used to forming the CCS consensus.
        """
        if not self.baxH5.hasConsensusBasecalls:
            raise ValueError, "No CCS reads in this file"
        return self.baxH5._ccsNumPasses[self.index]

    @property
    def numEvents(self):
        """
        Total number of basecall events in the ZMW
        """
        offsets = self.baxH5._offsetsByHole[self.holeNumber]
        return offsets[1] - offsets[0]

    #
    # The following calls return one or more ZmwRead objects.
    #
    def read(self, readStart=None, readEnd=None):
        """
        Given no arguments, returns the entire (HQ-clipped) polymerase
        read.  With readStart, readEnd arguments, returns the
        specified extent of the polymerase read.
        """
        if not self.baxH5.hasRawBasecalls:
            raise ValueError, "No raw reads in this file"
        hqStart, hqEnd = self.hqRegion
        readStart = hqStart if readStart is None else readStart
        readEnd   = hqEnd if readEnd is None else readEnd
        return ZmwRead(self.baxH5, self.holeNumber, readStart, readEnd)

    def readNoQC(self, readStart=None, readEnd=None):
        """
        Given no arguments, returns the entire polymerase read, *not
        HQ-clipped*.  With readStart, readEnd arguments, returns the
        specified extent of the polymerase read.

        .. warning::

            It is not recommended that production code use this method
            as we make no guarantees about what happens outside of the
            HQ region.
        """
        polymeraseBegin = 0
        polymeraseEnd = self.numEvents
        readStart = polymeraseBegin if readStart is None else readStart
        readEnd   = polymeraseEnd   if readEnd   is None else readEnd
        return ZmwRead(self.baxH5, self.holeNumber, readStart, readEnd)


    @property
    def ccsRead(self):
        if not self.baxH5.hasConsensusBasecalls:
            raise ValueError, "No CCS reads in this file"
        baseOffset  = self.baxH5._ccsOffsetsByHole[self.holeNumber]
        if (baseOffset[1] - baseOffset[0]) <= 0:
            return None
        else:
            return CCSZmwRead(self.baxH5, self.holeNumber, 0,
                              baseOffset[1] - baseOffset[0])

    @property
    def zmwName(self):
        return "%s/%d" % (self.baxH5.movieName,
                          self.holeNumber)

    def __repr__(self):
        return "<Zmw: %s>" % self.zmwName


class ZmwRead(CommonEqualityMixin):
    """
    A ZmwRead represents the data features (basecalls as well as pulse
    features) recorded from the ZMW, delimited by readStart and readEnd.
    """
    __slots__ = [ "baxH5", "holeNumber",
                  "readStart", "readEnd",
                  "offsetBegin", "offsetEnd" ]

    def __init__(self, baxH5, holeNumber, readStart, readEnd):
        self.baxH5        = baxH5
        self.holeNumber   = holeNumber
        self.readStart    = readStart
        self.readEnd      = readEnd
        zmwOffsetBegin, zmwOffsetEnd = self._getOffsets()[self.holeNumber]
        self.offsetBegin = zmwOffsetBegin + self.readStart
        self.offsetEnd   = zmwOffsetBegin + self.readEnd
        if not (zmwOffsetBegin   <=
                self.offsetBegin <=
                self.offsetEnd   <=
                zmwOffsetEnd):
            raise IndexError, "Invalid slice of Zmw!"

    def _getBasecallsGroup(self):
        return self.baxH5._basecallsGroup

    def _getOffsets(self):
        return self.baxH5._offsetsByHole

    @property
    def zmw(self):
        return self.baxH5[self.holeNumber]

    @property
    def readName(self):
        return "%s/%d_%d" % (self.zmw.zmwName,
                             self.readStart,
                             self.readEnd)

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__,
                             self.readName)

    def __len__(self):
        return self.readEnd - self.readStart

    def basecalls(self):
        return arrayFromDataset(self._getBasecallsGroup()["Basecall"],
                                self.offsetBegin, self.offsetEnd).tostring()

    def qv(self, qvName):
        return arrayFromDataset(self._getBasecallsGroup()[qvName],
                                self.offsetBegin, self.offsetEnd)

    PreBaseFrames  = _makeQvAccessor("PreBaseFrames")
    IPD            = _makeQvAccessor("PreBaseFrames")

    WidthInFrames  = _makeQvAccessor("WidthInFrames")
    PulseWidth     = _makeQvAccessor("WidthInFrames")

    QualityValue   = _makeQvAccessor("QualityValue")
    InsertionQV    = _makeQvAccessor("InsertionQV")
    DeletionQV     = _makeQvAccessor("DeletionQV")
    DeletionTag    = _makeQvAccessor("DeletionTag")
    MergeQV        = _makeQvAccessor("MergeQV")
    SubstitutionQV = _makeQvAccessor("SubstitutionQV")
    SubstitutionTag = _makeQvAccessor("SubstitutionTag")

    PulseIndex     = _makeQvAccessor("PulseIndex")

class CCSZmwRead(ZmwRead):
    """
    Class providing access to the CCS (circular consensus sequencing)
    data calculated for a ZMW.
    """
    def _getBasecallsGroup(self):
        return self.baxH5._ccsBasecallsGroup

    def _getOffsets(self):
        return self.baxH5._ccsOffsetsByHole

    @property
    def readName(self):
        return "%s/ccs" % self.zmw.zmwName

def _makeOffsetsDataStructure(h5Group):
    numEvent   = h5Group["ZMW/NumEvent"].value
    holeNumber = h5Group["ZMW/HoleNumber"].value
    endOffset = np.cumsum(numEvent, dtype=np.uint32)
    singleZero = np.array([0], dtype=np.uint32)
    beginOffset = np.hstack((singleZero, endOffset[0:-1]))
    offsets = zip(beginOffset, endOffset)
    return dict(zip(holeNumber, offsets))

def _makeRegionTableIndex(regionTableHoleNumbers):
    #  returns a dict: holeNumber -> (startRow, endRow)
    diffs = np.ediff1d(regionTableHoleNumbers,
                       to_begin=[1], to_end=[1])
    changepoints = np.flatnonzero(diffs)
    startsAndEnds = zip(changepoints[:-1],
                        changepoints[1:])
    return dict(zip(np.unique(regionTableHoleNumbers),
                    startsAndEnds))

class BaxH5Reader(object):
    """
    The `BaxH5Reader` class provides access to bax.h5 file and
    single-part bas.h5 files.
    """
    def __init__(self, filename, regionH5Filename=None):
        try:
            self.filename = op.abspath(op.expanduser(filename))
            self.file = h5py.File(self.filename, "r")
        except IOError:
            raise IOError, ("Invalid or nonexistent bax/bas file %s" % filename)

        #
        # Raw base calls?
        #
        if "/PulseData/BaseCalls/Basecall" in self.file:
            self._basecallsGroup = self.file["/PulseData/BaseCalls"]
            self._offsetsByHole  = _makeOffsetsDataStructure(self._basecallsGroup)
            self.hasRawBasecalls = True
        else:
            self.hasRawBasecalls = False
        #
        # CCS base calls?
        #
        if "/PulseData/ConsensusBaseCalls" in self.file:
            self._ccsBasecallsGroup = self.file["/PulseData/ConsensusBaseCalls"]
            self._ccsOffsetsByHole  = _makeOffsetsDataStructure(self._ccsBasecallsGroup)
            self._ccsNumPasses      = self._ccsBasecallsGroup["Passes/NumPasses"]
            self.hasConsensusBasecalls = True
        else:
            self.hasConsensusBasecalls = False

        self._mainBasecallsGroup = self._basecallsGroup if self.hasRawBasecalls \
                                   else self._ccsBasecallsGroup

        if regionH5Filename is None:
            # load region information from the bas/bax file
            self._loadRegions(self.file)
        else:
            # load region information from a separate region file
            self.loadExternalRegions(regionH5Filename)

        # Create a variable to store the chemistry information
        self._sequencingChemistry = None
        #
        # ZMW metric cache -- probably want to move prod and readScore
        # here.
        #
        self.__metricCache = {}

    def _loadRegions(self, fh):
        """
        Loads region table information from the given file handle and applies
        it to the ZMW data.
        """
        holeNumbers = self._mainBasecallsGroup["ZMW/HoleNumber"].value
        self._holeNumberToIndex = dict(zip(holeNumbers, range(len(holeNumbers))))

        #
        # Region table
        #
        self.regionTable = toRecArray(REGION_TABLE_DTYPE,
                                      fh["/PulseData/Regions"].value)

        self._regionTableIndex = _makeRegionTableIndex(self.regionTable.holeNumber)
        isHqRegion     = self.regionTable.regionType == HQ_REGION
        hqRegions      = self.regionTable[isHqRegion]

        if len(hqRegions) != len(holeNumbers):
            # Bug 23585: pre-2.1 primary had a bug where a bas file
            # could get a broken region table, lacking an HQ region
            # entry for a ZMW.  This happened fairly rarely, mostly on
            # very long traces.  Workaround here is to rebuild HQ
            # regions table with empty HQ region entries for those
            # ZMWs.
            hqRegions_ = toRecArray(REGION_TABLE_DTYPE,
                                    np.zeros(shape=len(holeNumbers),
                                             dtype=REGION_TABLE_DTYPE))
            hqRegions_.holeNumber = holeNumbers
            for record in hqRegions:
                hn = record.holeNumber
                hqRegions_[self._holeNumberToIndex[hn]] = record
            hqRegions = hqRegions_

        hqRegionLength = hqRegions.regionEnd - hqRegions.regionStart
        holeStatus     = self._mainBasecallsGroup["ZMW/HoleStatus"].value

        #
        # Sequencing ZMWs - Note: this differs from Primary's
        # definition. To obtain those values, one would use the
        # `allSequencingZmws` property.
        #
        self._sequencingZmws = \
            holeNumbers[(holeStatus == SEQUENCING_ZMW)                       &
                        (self._mainBasecallsGroup["ZMW/NumEvent"].value > 0) &
                        (hqRegionLength >  0)]

        self._allSequencingZmws = holeNumbers[holeStatus == SEQUENCING_ZMW]

    def loadExternalRegions(self, regionH5Filename):
        """
        Loads regions defined in the given file, overriding those found in the
        bas/bax file.
        """
        try:
            fh = h5py.File(op.abspath(op.expanduser(regionH5Filename)), "r")
        except IOError:
            raise IOError, ("Invalid or nonexistent file %s" % regionH5Filename)

        self._loadRegions(fh)
        fh.close()

        # A sanity check that the given region table provides information for
        # hole numbers contain in this base file.
        baxHoleNumbers = self._mainBasecallsGroup["ZMW/HoleNumber"].value
        rgnHoleNumbers = self.regionTable.holeNumber
        if not np.in1d(rgnHoleNumbers, baxHoleNumbers).all():
            msg = "Region file (%s) does not contain the same hole numbers as " \
                  "bas/bax file (%s)"
            raise IOError, (msg % (regionH5Filename, self.filename))

    @property
    def sequencingZmws(self):
        """
        A list of the hole numbers that produced useable sequence data.
        Specifically, this means ZMWs that have an HQ region.
        """
        return self._sequencingZmws

    @property
    def allSequencingZmws(self):
        """
        A list of the hole numbers that are capable of producing
        sequencing data. This differs from the `sequencingZmws` in
        that zmws are not filtered according to their HQ status. This
        number is fixed per chip, whereas the `sequencingZmws` depends
        on things such as loading.
        """
        return self._allSequencingZmws

    def __getitem__(self, holeNumber):
        return Zmw(self, holeNumber)

    #
    # Iterators over Zmws, ZmwReads
    #

    def __iter__(self):
        for holeNumber in self.sequencingZmws:
            yield self[holeNumber]

    def reads(self):
        if self.hasRawBasecalls:
            for zmw in self:
                yield zmw.read()

    def subreads(self):
        if self.hasRawBasecalls:
            for zmw in self:
                for subread in zmw.subreads:
                    yield subread

    def ccsReads(self):
        if self.hasConsensusBasecalls:
            for zmw in self:
                if zmw.ccsRead is not None:
                    yield zmw.ccsRead

    # ------------------------------

    @property
    def movieName(self):
        movieNameAttr = self.file["/ScanData/RunInfo"].attrs["MovieName"]

        # In old bas.h5 files, attributes of ScanData/RunInfo are stored as
        # strings in arrays of length one.
        if (isinstance(movieNameAttr, (np.ndarray, list)) and
                len(movieNameAttr) == 1):
            movieNameString = movieNameAttr[0]
        else:
            movieNameString = movieNameAttr

        if not isinstance(movieNameString, basestring):
            raise TypeError("Unsupported movieName {m} of type {t}."
                             .format(m=movieNameString,
                                     t=type(movieNameString)))
        return movieNameString

    @property
    def _chemistryBarcodeTripleInFile(self):
        """
        The chemistry barcode triple consists of (BindingKit,
        SequencingKit, SoftwareVersion) and is written on the
        instrument to the bax file as of primary version 2.1.  Prior
        to that, it was only written in the metadata.xml.
        """
        try:
            bindingKit      = self.file["/ScanData/RunInfo"].attrs["BindingKit"]
            sequencingKit   = self.file["/ScanData/RunInfo"].attrs["SequencingKit"]
            # version string in bas file looks like "2.1.1.1.x", we have to extract
            # the "2.1"
            tmp = self.file["/PulseData/BaseCalls"].attrs["ChangeListID"]
            swVersion= ".".join(tmp.split(".")[0:2])
            return (bindingKit, sequencingKit, swVersion)
        except:
            return None

    @property
    def _chemistryBarcodeTripleFromMetadataXML(self):
        try:
            movieName = self.movieName
            _up = op.dirname(op.dirname(self.filename))
            metadataLocation = op.join(_up, movieName + ".metadata.xml")
            triple = tripleFromMetadataXML(metadataLocation)
            return triple
        except ChemistryLookupError:
            return None

    @property
    def chemistryBarcodeTriple(self):
        triple = self._chemistryBarcodeTripleInFile or self._chemistryBarcodeTripleFromMetadataXML
        if triple:
            return triple
        else:
            raise ChemistryLookupError, "Could not find chemistry barcodes in file or companion metadata.xml"

    @property
    def sequencingChemistry(self):
        """
        Find the name of the chemistry by consulting, in order of preference:
          1) Barcode triple in file
          2) "SequencingChemistry" attr in file (chemistry override)
          3) metadata.xml companion file
        """
        if self._sequencingChemistry is None:
            triple = self._chemistryBarcodeTripleInFile
            if triple is not None:
                self._sequencingChemistry = decodeTriple(*triple)
            elif "SequencingChemistry" in self.file["/ScanData/RunInfo"].attrs:
                self._sequencingChemistry = self.file["/ScanData/RunInfo"].attrs["SequencingChemistry"]
            else:
                tripleFromXML = self._chemistryBarcodeTripleFromMetadataXML
                if tripleFromXML is not None:
                    self._sequencingChemistry = decodeTriple(*tripleFromXML)
                else:
                    raise ChemistryLookupError, "Chemistry information could not be found for this file"
        return self._sequencingChemistry

    def __len__(self):
        return len(self.sequencingZmws)

    def close(self):
        if hasattr(self, "file") and self.file is not None:
            self.file.close()
            self.file = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def listZmwMetrics(self):
        return self._basecallsGroup["ZMWMetrics"].keys()

    def zmwMetric(self, name, index):
        # we are going to cache these lazily because it is very likely
        # that if one ZMW asked for the metric others aren't far
        # behind.
        if name not in self.__metricCache:
            k = "/".join(("ZMWMetrics", name))
            self.__metricCache[name] = self._mainBasecallsGroup[k].value

        v = self.__metricCache[name]
        if len(v.shape) > 1:
            return v[index,]
        else:
            return v[index]


class BasH5Reader(object):
    """
    .. testsetup:: *

       from pbcore.io import BasH5Reader
       from pbcore import data
       filename = data.getBasH5s()[0]
       b = BasH5Reader(filename)
       zmw8 = b[8]

    The `BasH5Reader` provides access to the basecall and pulse metric
    data encoded in PacBio bas.h5 files.  To access data using a
    `BasH5Reader`, the standard idiom is:

    1. Index into the `BasH5Reader` using the ZMW hole number to get a `Zmw` object::

        >>> b
        <BasH5Reader: m110818_075520_42141_c100129202555500000315043109121112_s1_p0>
        >>> zmw8 = b[8]
        >>> zmw8
        <Zmw: m110818_075520_42141_c100129202555500000315043109121112_s1_p0/8>

    2. Extract `ZmwRead` objects from the `Zmw` object by:

       - Using the `.subreads` property to extract the subreads, which
         are the subintervals of the raw read corresponding to the
         SMRTbell insert::

           >>> subreads = zmw8.subreads
           >>> print subreads
           [<ZmwRead: m110818_075520_42141_c100129202555500000315043109121112_s1_p0/8/3381_3881>,
           <ZmwRead: m110818_075520_42141_c100129202555500000315043109121112_s1_p0/8/3924_4398>,
           <ZmwRead: m110818_075520_42141_c100129202555500000315043109121112_s1_p0/8/4445_4873>,
           <ZmwRead: m110818_075520_42141_c100129202555500000315043109121112_s1_p0/8/4920_5354>,
           <ZmwRead: m110818_075520_42141_c100129202555500000315043109121112_s1_p0/8/5413_5495>]

       - For CCS bas files, using the `.ccsRead` property to extract
         the CCS (consensus) read, which is a consensus sequence
         precomputed from the subreads.  Older bas files, from when
         CCS was computed on the instrument, may contain both CCS- and
         sub- reads.

           >>> zmw8.ccsRead
           <CCSZmwRead: m110818_075520_42141_c100129202555500000315043109121112_s1_p0/8/ccs>

       - Use the `.read()` method to get the full raw read, or
         `.read(start, end)` to extract a custom subinterval.

           >>> zmw8.read()
           <ZmwRead: m110818_075520_42141_c100129202555500000315043109121112_s1_p0/8/3381_5495>
           >>> zmw8.read(3390, 3400)
           <ZmwRead: m110818_075520_42141_c100129202555500000315043109121112_s1_p0/8/3390_3400>

    3. With a `ZmwRead` object in hand, extract the desired
       basecalls and pulse metrics::

         >>> subreads[0].readName
         "m110818_075520_42141_c100129202555500000315043109121112_s1_p0/8/3381_3881"
         >>> subreads[0].basecalls()
         "AGCCCCGTCGAGAACATACAGGTGGCCAATTTCACAGCCTCTTGCCTGGGCGATCCCGAACATCGCACCGGA..."
         >>> subreads[0].InsertionQV()
         array([12, 12, 10,  2,  7, 14, 13, 18, 15, 16, 16, 15, 10, 12,  3, 14, ...])

    Note that not every ZMW on a chip produces usable sequencing
    data.  The `BasH5Reader` has a property `sequencingZmws` is a list
    of the hole numbers where usable sequence was recorded.
    Iteration over the `BasH5Reader` object allows you to iterate over
    the `Zmw` objects providing usable sequence.
    """
    def __init__(self, *args):
        assert len(args) > 0

        if len(args) == 1:
            filename = args[0]
            try:
                self.filename = op.abspath(op.expanduser(filename))
                self.file = h5py.File(self.filename, "r")
            except IOError:
                raise IOError, ("Invalid or nonexistent bas/bax file %s" % filename)


            # Is this a multi-part or single-part?
            if self.file.get("MultiPart"):
                directory = op.dirname(self.filename)
                self._parts = [ BaxH5Reader(op.join(directory, fn))
                                for fn in self.file["/MultiPart/Parts"] ]
                self._holeLookupDict = dict(zip(self.file["/MultiPart/HoleLookup"][:,0],
                                                self.file["/MultiPart/HoleLookup"][:,1]))
                self._holeLookup = self._holeLookupDict.get
            else:
                self._parts = [ BaxH5Reader(self.filename) ]
                self._holeLookup = (lambda holeNumber: 1)
        else:
            partFilenames    = args
            self.filename    = None
            self.file        = None
            self._parts      = [ BaxH5Reader(fn) for fn in partFilenames ]
            holeLookupDict   = { hn : (i + 1)
                                 for i in xrange(len(self._parts))
                                 for hn in self._parts[i]._holeNumberToIndex }
            self._holeLookup = lambda hn: holeLookupDict[hn]
        self._sequencingZmws = np.concatenate([ part.sequencingZmws
                                                for part in self._parts ])

    @property
    def parts(self):
        return self._parts

    @property
    def sequencingZmws(self):
        return self._sequencingZmws

    @property
    def allSequencingZmws(self):
        return np.concatenate([ part.allSequencingZmws
                                for part in self._parts ])

    @property
    def hasConsensusBasecalls(self):
        return all(part.hasConsensusBasecalls for part in self._parts)

    @property
    def hasRawBasecalls(self):
        return all(part.hasRawBasecalls for part in self._parts)


    #
    # Iterators
    #

    def __iter__(self):
        """
        Iterate over ZMWs
        """
        for holeNumber in self.sequencingZmws:
            yield self[holeNumber]

    def reads(self):
        for part in self._parts:
            for read in part.reads():
                yield read

    def subreads(self):
        for part in self._parts:
            for subread in part.subreads():
                yield subread

    def ccsReads(self):
        for part in self._parts:
            for ccsRead in part.ccsReads():
                yield ccsRead

    # ----------

    def __len__(self):
        return len(self.sequencingZmws)

    def _getitemScalar(self, holeNumber):
        part = self.parts[self._holeLookup(holeNumber)-1]
        return part[holeNumber]

    def __getitem__(self, holeNumbers):
        if (isinstance(holeNumbers, int) or
            issubclass(type(holeNumbers), np.integer)):
            return self._getitemScalar(holeNumbers)
        elif isinstance(holeNumbers, slice):
            return [ self._getitemScalar(r)
                     for r in xrange(*holeNumbers.indices(len(self)))]
        elif isinstance(holeNumbers, list) or isinstance(holeNumbers, np.ndarray):
            if len(holeNumbers) == 0:
                return []
            else:
                entryType = type(holeNumbers[0])
                if entryType == int or issubclass(entryType, np.integer):
                    return [ self._getitemScalar(r) for r in holeNumbers ]
                elif entryType == bool or issubclass(entryType, np.bool_):
                    return [ self._getitemScalar(r) for r in np.flatnonzero(holeNumbers) ]
        raise TypeError, "Invalid type for BasH5Reader slicing"

    @property
    def movieName(self):
        return self._parts[0].movieName

    @property
    def chemistryBarcodeTriple(self):
        return self._parts[0].chemistryBarcodeTriple

    @property
    def sequencingChemistry(self):
        return self._parts[0].sequencingChemistry

    def __len__(self):
        return len(self.sequencingZmws)

    def close(self):
        if hasattr(self, "file") and self.file is not None:
            self.file.close()
            self.file = None
        for part in self.parts:
            part.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __iter__(self):
        for holeNumber in self.sequencingZmws:
            yield self[holeNumber]

    def __repr__(self):
        return "<BasH5Reader: %s>" % self.movieName

    # Make cursor classes available
    Zmw        = Zmw
    ZmwRead    = ZmwRead
    CCSZmwRead = CCSZmwRead

def sniffMovieName(basFilename):
    # The clean way to do this is the get the moviename attribute from
    # the file, but unfortunately that approach is unusable slow.
    # Here we assume that the filename follows the standard PacBio
    # naming convention.
    movieName = op.basename(basFilename).split(".")[0]
    return movieName

class BasH5Collection(object):
    """
    Class representing a collection of base call (bas/bax) files.

    Can be initialized from a list of bas/bax files, or an input.fofn
    file containing a list of bas/bax files
    """

    def __init__(self, *args):
        #
        # Implementation notes: find all the bas/bax files, and group
        # them together by movieName
        #
        basFilenames = []
        for arg in args:
            if arg.endswith(".fofn"):
                for fn in readFofn(arg):
                    basFilenames.append(fn)
            else:
                basFilenames.append(arg)

        movieNames = map(sniffMovieName, basFilenames)
        movieNamesAndFiles = sorted(zip(movieNames, basFilenames))

        self.readers = OrderedDict(
            [ (k , BasH5Reader(*[val[1] for val in v]))
              for k, v in groupby(movieNamesAndFiles, lambda t: t[0]) ])

    @property
    def movieNames(self):
        return self.readers.keys()

    def __getitem__(self, key):
        """
        Slice by movie name, zmw name, or zmw range name, using standard
        PacBio naming conventions.  Examples:

          - ["m110818_..._s1_p0"]             -> BasH5Reader
          - ["m110818_..._s1_p0/24480"]       -> Zmw
          - ["m110818_..._s1_p0/24480/20_67"] -> ZmwRead
          - ["m110818_..._s1_p0/24480/ccs"]   -> CCSZmwRead
        """
        indices = key.rstrip("/").split("/")

        if len(indices) < 1:
            raise KeyError("Invalid slice of BasH5Collection")

        if len(indices) >= 1:
            result = self.readers[indices[0]]
        if len(indices) >= 2:
            result = result[int(indices[1])]
        if len(indices) >= 3:
            if indices[2] == "ccs":
                result = result.ccsRead
            else:
                start, end = map(int, indices[2].split("_"))
                result = result.read(start, end)
        return result

    #
    # Iterators over Zmw, ZmwRead objects
    #

    def __iter__(self):
        for reader in self.readers.values():
            for zmw in reader: yield zmw

    def reads(self):
        for reader in self.readers.values():
            for read in reader.reads():
                yield read

    def subreads(self):
        for reader in self.readers.values():
            for read in reader.subreads():
                yield read

    def ccsReads(self):
        for reader in self.readers.values():
            for read in reader.ccsReads():
                yield read
