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
__all__ = [ "CmpH5Reader" ]

import h5py, numpy as np
from bisect import bisect_left, bisect_right
from collections import Counter
from os.path import abspath, expanduser
from .rangeQueries import makeReadLocator
from ._utils import rec_join, drop_fields

# ========================================
#  Data manipulation routines.
#
GAP = 0b0000

_basemap =  { 0b0000 : ord("-"),
              0b0001 : ord("A"),
              0b0010 : ord("C"),
              0b0100 : ord("G"),
              0b1000 : ord("T"),
              0b1111 : ord("N") }

_cBasemap = { 0b0000 : ord("-"),
              0b0001 : ord("T"),
              0b0010 : ord("G"),
              0b0100 : ord("C"),
              0b1000 : ord("A"),
              0b1111 : ord("N") }

_basemapArray  = np.ndarray(shape=(max(_basemap.keys()) + 1,), dtype=np.byte)
_cBasemapArray = np.ndarray(shape=(max(_basemap.keys()) + 1,), dtype=np.byte)

for (e, v) in _basemap.iteritems():
    _basemapArray[e] = v
for (e, v) in _cBasemap.iteritems():
    _cBasemapArray[e] = v

_baseEncodingToInt = np.array(
    [ 0,   # 0000
      1,   # 0001
      2,   # 0010
     -1,   # 0011
      3,   # 0100
     -1,   # 0101
     -1,   # 0110
     -1,   # 0111
      4 ]) # 1000

# These are 2D tables indexed by (readInt, refInt)
_gusfieldTranscriptTable = \
    np.fromstring("ZDDDDZ"
                  "IMRRRZ"
                  "IRMRRZ"
                  "IRRMRZ"
                  "IRRRMZ"
                  "ZZZZZZ", dtype=np.uint8).reshape(6, 6)
_exonerateTranscriptTable = \
    np.fromstring("Z    Z"
                  " |   Z"
                  "  |  Z"
                  "   | Z"
                  "    |Z"
                  "ZZZZZZ", dtype=np.uint8).reshape(6, 6)
_exoneratePlusTranscriptTable = \
    np.fromstring("Z    Z"
                  " |***Z"
                  " *|**Z"
                  " **|*Z"
                  " ***|Z"
                  "ZZZZZZ", dtype=np.uint8).reshape(6, 6)

def arrayFromDataset(ds, offsetBegin, offsetEnd):
    shape = (offsetEnd - offsetBegin,)
    a = np.ndarray(shape=shape, dtype=ds.dtype)
    mspace = h5py.h5s.create_simple(shape)
    fspace = ds.id.get_space()
    fspace.select_hyperslab((offsetBegin,), shape, (1,))
    ds.id.read(mspace, fspace, a)
    return a

def readFromAlignmentArray(a, gapped=True, complement=False):
    if complement:
        r = _cBasemapArray[a >> 4]
    else:
        r = _basemapArray[a >> 4]
    if not gapped:
        r = r[r != ord("-")]
    return  r.tostring()

def referenceFromAlignmentArray(a, gapped=True, complement=False):
    if complement:
        r = _cBasemapArray[a & 0b1111]
    else:
        r = _basemapArray[a & 0b1111]
    if not gapped:
        r = r[r != ord("-")]
    return  r.tostring()

def ungappedPulseArray(a):
    dtype = a.dtype
    if dtype == np.float32:
        return a[~np.isnan(a)]
    elif dtype == np.uint8:
        return a[a != np.uint8(-1)]
    elif dtype == np.uint16:
        return a[a != np.uint16(-1)]
    elif dtype == np.int8:
        return a[a != ord("-")]
    else:
        raise Exception, "Invalid pulse array type"



# ========================================
# Alignment record type
#

ALIGNMENT_INDEX_COLUMNS = ("AlnID", "AlnGroupID", "MovieID", "RefGroupID",
                           "tStart", "tEnd", "RCRefStrand", "HoleNumber",
                           "SetNumber", "StrobeNumber", "MoleculeID",
                           "rStart", "rEnd", "MapQV", "nM", "nMM", "nIns",
                           "nDel", "Offset_begin", "Offset_end", "nBackRead",
                           "nReadOverlap")

ALIGNMENT_INDEX_DTYPE = [(COLUMN_NAME, np.uint32)
                         for COLUMN_NAME in ALIGNMENT_INDEX_COLUMNS]

def _makePulseFeatureAccessor(featureName):
    def f(self, aligned=True, orientation="native"):
        return self.pulseFeature(featureName, aligned, orientation)
    return f

class CmpH5Alignment(object):
    """
    Access to all columns of a single row of the alignment index,
    and on-demand access to the corresponding sequence and pulse
    features.

    The `orientation` argument to some data access methods determines
    how reverse-strand alignments are returned to the user.  `.cmp.h5`
    files natively encode reverse strand reads in read-order,
    uncomplemented, with the *reference* reverse-complemented.  Most
    analysis applications will want to use the data in this order,
    which we term the *NATIVE* orientation.

    Some applications that involve collating or displaying the reads
    aligned to the reference genome want the reference to be presented
    in its genomic order, and the *read* to be reverse-complemented.
    We term this *GENOMIC* orientation.

    Methods prefixed with *aligned* return data (bases or features)
    that include gaps, which are encoded according to the data type.
    Methods not prefixed with *aligned* excise the gaps.

    Sequence and pulse features are not cached.
    """
    __slots__ = ["cmpH5", "rowNumber"]

    def __init__(self, cmph5, rowNumber):
        self.cmpH5 = cmph5
        self.rowNumber = rowNumber

    def clippedTo(self, refStart, refEnd):
        # Caution: linear time in alignment length
        return ClippedCmpH5Alignment(self, refStart, refEnd)

    @property
    def alignmentGroup(self):
        return self.cmpH5.alignmentGroup(self.AlnGroupID)

    @property
    def referenceInfo(self):
        return self.cmpH5.referenceInfo(self.RefGroupID)

    @property
    def referenceName(self):
        return self.referenceInfo.Name

    @property
    def readName(self):
        return "%s/%d/%d_%d" % (self.movieInfo.Name,
                                self.HoleNumber,
                                self.rStart,
                                self.rEnd)
    @property
    def movieInfo(self):
        return self.cmpH5.movieInfo(self.MovieID)

    @property
    def isForwardStrand(self):
        return self.RCRefStrand == 0

    @property
    def isReverseStrand(self):
        return self.RCRefStrand == 1

    @property
    def referenceStart(self):
        return self.tStart

    @property
    def referenceEnd(self):
        return self.tEnd

    @property
    def readStart(self):
        return self.rStart

    @property
    def readEnd(self):
        return self.rEnd

    @property
    def referenceSpan(self):
        return self.tEnd - self.tStart

    @property
    def readLength(self):
        return self.alignedLength - self.nDel

    @property
    def alignedLength(self):
        return self.Offset_end - self.Offset_begin

    @property
    def accuracy(self):
        return 1 - float(self.nMM + self.nIns + self.nDel)/self.readLength

    @property
    def numPasses(self):
        return self.cmpH5.numPasses[self.rowNumber]

    @property
    def barcode(self):
        return self.cmpH5.barcode[self.rowNumber]

    def spansReferencePosition(self, pos):
        return self.tStart <= pos < self.tEnd

    def spansReferenceRange(self, start, end):
        assert start <= end
        return (self.tStart <= start <= end <= self.tEnd)

    def alignmentArray(self, orientation="native"):
        alnDs = self.alignmentGroup["AlnArray"]
        alnArray = arrayFromDataset(alnDs, self.Offset_begin, self.Offset_end)
        if self.isReverseStrand and (orientation == "genomic"):
            return alnArray[::-1]
        else:
            return alnArray

    def transcript(self, orientation="native", style="gusfield"):
        """
        A text representation of the alignment moves (see Gusfield).
        """
        if style == "exonerate+":
            tbl = _exoneratePlusTranscriptTable
        elif style == "exonerate":
            tbl = _exonerateTranscriptTable
        else:
            tbl = _gusfieldTranscriptTable
        alnArr = self.alignmentArray(orientation)
        readBaseInts = _baseEncodingToInt[alnArr >> 4]
        refBaseInts  = _baseEncodingToInt[alnArr  & 0b1111]
        return tbl[readBaseInts, refBaseInts].tostring()

    def read(self, aligned=True, orientation="native"):
        return readFromAlignmentArray(self.alignmentArray(orientation),
                                      gapped=aligned,
                                      complement=(self.isReverseStrand and
                                                  orientation == "genomic"))

    def reference(self, aligned=True, orientation="native"):
        return referenceFromAlignmentArray(self.alignmentArray(orientation),
                                           gapped=aligned,
                                           complement=(self.isReverseStrand and
                                                       orientation == "genomic"))

    def referencePositions(self, aligned=True, orientation="native"):
        """
        Returns an array of reference positions such that
        referencePositions[i] = reference position of the i'th column
        in the alignment.  Insertions are grouped with the following
        reference base, in the specified orientation.

        Length of output array = length of alignment.

        Example:

          0123455567
          GATTG--ACC

        """
        if aligned:
            referenceNonGapMask = (self.alignmentArray(orientation) & 0b1111) != GAP
            if self.isReverseStrand and orientation=="native":
                return self.tEnd - np.cumsum(referenceNonGapMask)
            else:
                return self.tStart + np.hstack([0, np.cumsum(referenceNonGapMask[:-1])])
        else:
            if self.isReverseStrand and orientation=="native":
                return np.arange(self.tEnd, self.tStart, -1) - 1
            else:
                return np.arange(self.tStart, self.tEnd)

    def pulseFeature(self, featureName, aligned=True, orientation="native"):
        pulseDataset = self.alignmentGroup[featureName]
        pulseArray = arrayFromDataset(pulseDataset, self.Offset_begin, self.Offset_end)
        if self.isReverseStrand and orientation == "genomic":
            alignedPulseArray = pulseArray[::-1]
        else:
            alignedPulseArray = pulseArray
        if aligned:
            return alignedPulseArray
        else:
            return ungappedPulseArray(alignedPulseArray)

    IPD            = _makePulseFeatureAccessor("IPD")
    PulseWidth     = _makePulseFeatureAccessor("PulseWidth")
    QualityValue   = _makePulseFeatureAccessor("QualityValue")
    InsertionQV    = _makePulseFeatureAccessor("InsertionQV")
    DeletionQV     = _makePulseFeatureAccessor("DeletionQV")
    DeletionTag    = _makePulseFeatureAccessor("DeletionTag")
    MergeQV        = _makePulseFeatureAccessor("MergeQV")
    SubstitutionQV = _makePulseFeatureAccessor("SubstitutionQV")

    def __getattr__(self, key):
        return self.cmpH5.alignmentIndex[self.rowNumber][key]

    def __repr__(self):
        return "CmpH5 alignment: %s  %3d  %9d  %9d" \
            % (("+" if self.isForwardStrand else "-"),
               self.RefGroupID, self.tStart, self.tEnd)

    def __str__(self):
        COLUMNS = 80
        val = ""
        val += repr(self) + "\n\n"
        val += "Read:        " + self.readName          + "\n"
        val += "Reference:   " + self.referenceName     + "\n\n"
        val += "Read length: " + str(self.readLength)   + "\n"
        val += "Accuracy:    " + "%0.3f" % self.accuracy + "\n"

        alignedRead = self.read()
        alignedRef = self.reference()
        transcript = self.transcript(style="exonerate+")
        refPos = self.referencePositions()
        refPosString = "".join([str(pos % 10) for pos in refPos])
        for i in xrange(0, len(alignedRef), COLUMNS):
            val += "\n"
            val += "  " + refPosString[i:i+COLUMNS] + "\n"
            val += "  " + alignedRef  [i:i+COLUMNS] + "\n"
            val += "  " + transcript  [i:i+COLUMNS] + "\n"
            val += "  " + alignedRead [i:i+COLUMNS] + "\n"
            val += "\n"
        return val

    def __cmp__(self, other):
        return cmp((self.RefGroupID, self.tStart, self.tEnd),
                   (other.RefGroupID, other.tStart, other.tEnd))


class ClippedCmpH5Alignment(CmpH5Alignment):

    # We use these fields to shadow fields in the
    # alignment index row.
    __slots__ = [ "tStart",
                  "tEnd",
                  "Offset_begin",
                  "Offset_end",
                  "nM",
                  "nMM",
                  "nIns",
                  "nDel"  ]

    def __init__(self, aln, refStart, refEnd):
        # The clipping region must intersect the alignment, though it
        # does not have to be contained wholly within it.
        refStart = max(aln.referenceStart, refStart)
        refEnd   = min(aln.referenceEnd,   refEnd)
        assert refStart <= refEnd

        super(ClippedCmpH5Alignment, self).__init__(aln.cmpH5, aln.rowNumber)
        positions = aln.referencePositions(orientation="genomic")
        clipStart = bisect_right(positions, refStart) - 1
        clipEnd   = bisect_left(positions, refEnd)

        # overlay the bounds
        self.tStart = refStart
        self.tEnd   = refEnd
        if aln.isForwardStrand:
            self.Offset_begin = aln.Offset_begin + clipStart
            self.Offset_end   = aln.Offset_begin + clipEnd
        else:
            self.Offset_begin = aln.Offset_end - clipEnd
            self.Offset_end   = aln.Offset_end - clipStart
        alnMoveCounts = Counter(self.transcript(style="gusfield"))
        self.nM   = alnMoveCounts["M"]
        self.nMM  = alnMoveCounts["R"]
        self.nIns = alnMoveCounts["I"]
        self.nDel = alnMoveCounts["D"]


# ========================================
# CmpH5 reader class
#
class CmpH5Reader(object):
    """
    A fairly straightforward CmpH5Reader class.
    """
    def __init__(self, filename):
        self.filename = abspath(expanduser(filename))
        self.file = h5py.File(self.filename, "r")
        rawAlignmentIndex = self.file["/AlnInfo/AlnIndex"].value
        self.alignmentIndex = rawAlignmentIndex.view(dtype = ALIGNMENT_INDEX_DTYPE) \
                                               .view(np.recarray)                   \
                                               .flatten()
        def makeIdToGroupMapping(idDatasetPath, groupPathDatasetPath):
            return dict(zip(self.file[idDatasetPath],
                            [self.file[groupPath]
                             for groupPath in self.file[groupPathDatasetPath]]))
        self._alignmentGroupById  = makeIdToGroupMapping("/AlnGroup/ID", "/AlnGroup/Path")

        numMovies = len(self.file["/MovieInfo/ID"])
        hasFrameRate = ("FrameRate" in self.file["/MovieInfo"])
        self.movieTable = np.rec.fromrecords(
            zip(self.file["/MovieInfo/ID"],
                self.file["/MovieInfo/Name"],
                self.file["/MovieInfo/FrameRate"] if hasFrameRate else [np.nan] * numMovies,
                1.0/self.file["/MovieInfo/FrameRate"].value if hasFrameRate else [1.0] * numMovies),
            dtype=[("ID"       , int),
                   ("Name"     , object),
                   ("FrameRate", float),
                   ("TimeScale", float)])

        self._movieDict = {}
        for record in self.movieTable:
            assert record.ID not in self._movieDict
            self._movieDict[record.ID] = record

        referenceGroupTbl = np.rec.fromrecords(
            zip(self.file["/RefGroup/ID"],
                self.file["/RefGroup/RefInfoID"],
                [path[1:] for path in self.file["/RefGroup/Path"]]),
            dtype=[("ID"       , int),
                   ("RefInfoID", int),
                   ("Name"     , object)])

        referenceInfoTbl = np.rec.fromrecords(
            zip(self.file["/RefInfo/ID"],
                self.file["/RefInfo/FullName"],
                self.file["/RefInfo/Length"],
                self.file["/RefInfo/MD5"]) ,
            dtype=[("RefInfoID", int),
                   ("FullName" , object),
                   ("Length"   , int),
                   ("MD5"      , object)])

        self.referenceTable = \
            rec_join("RefInfoID", referenceGroupTbl, referenceInfoTbl, jointype="inner")

        self._referenceDict = {}
        for record in self.referenceTable:
            if record.ID != -1:
                assert record.ID != record.Name
                assert record.ID    not in self._referenceDict \
                    and record.Name not in self._referenceDict \
                    and record.MD5  not in self._referenceDict
                self._referenceDict[record.ID]   = record
                self._referenceDict[record.Name] = record
                self._referenceDict[record.MD5]  = record

        self._readLocatorById = {}
        if self.isSorted:
            for refId in self.file["/RefGroup/ID"]:
                self._readLocatorById[refId] = makeReadLocator(self, refId)

        if self.readType == "CCS":
            self.numPasses = self.file["/AlnInfo/NumPasses"].value

        if "Barcode" in self.file["/AlnInfo"]:
            barcodeIdToName = dict(zip(self.file["/BarcodeInfo/ID"],
                                       self.file["/BarcodeInfo/Name"]))
            self.barcode = map(barcodeIdToName.get,
                               self.file["/AlnInfo/Barcode"].value[:,0])

    @property
    def readType(self):
        return self.file.attrs["ReadType"]

    @property
    def version(self):
        return self.file.attrs["Version"]

    def versionAtLeast(self, minimalVersion):
        myVersionTuple = map(int, self.version.split(".")[:3])
        minimalVersionTuple = map(int, minimalVersion.split(".")[:3])
        return myVersionTuple >= minimalVersionTuple

    @property
    def primaryVersion(self):
        return self.file.attrs["PrimaryVersion"]

    def primaryVersionAtLeast(self, minimalVersion):
        myVersionTuple = map(int, self.primaryVersion.split("."))
        minimalVersionTuple = map(int, minimalVersion.split("."))
        return myVersionTuple >= minimalVersionTuple

    def softwareVersion(self, programName):
        filelog = dict(zip(self.file["/FileLog/Program"],
                           self.file["/FileLog/Version"]))
        return filelog.get(programName, None)

    @property
    def isSorted(self):
        return "Index" in self.file.attrs

    @property
    def isEmpty(self):
        return len(self.file["/AlnInfo"]) == 0

    def alignmentGroup(self, id):
        return self._alignmentGroupById[id]

    def movieInfo(self, id):
        return self._movieDict[id]

    def referenceInfo(self, key):
        """
        Key can be reference ID (integer), name (e.g. "ref000001"), or
        MD5 sum hex string (e.g. "a1319ff90e994c8190a4fe6569d0822a").
        """
        return self._referenceDict[key]

    def readsInRange(self, refId, refStart, refEnd, justIndices=False):
        if not self.isSorted: raise Exception, "CmpH5 is not sorted"
        rowNumbers = self._readLocatorById[refId](refStart, refEnd, justIndices=True)
        if justIndices:
            return rowNumbers
        else:
            return self[rowNumbers]

    def hasPulseFeature(self, featureName):
        return featureName in self._alignmentGroupById.values()[0].keys()

    def __repr__(self):
        return "<CmpH5Reader for %s>" % self.filename

    def __getitem__(self, rowNumbers):
        if (isinstance(rowNumbers, int) or
            issubclass(type(rowNumbers), np.integer)):
            return CmpH5Alignment(self, rowNumbers)
        elif isinstance(rowNumbers, slice):
            return [CmpH5Alignment(self, r)
                    for r in xrange(*rowNumbers.indices(len(self)))]
        elif isinstance(rowNumbers, list) or isinstance(rowNumbers, np.ndarray):
            if len(rowNumbers) == 0:
                return []
            else:
                entryType = type(rowNumbers[0])
                if entryType == int or issubclass(entryType, np.integer):
                    return [CmpH5Alignment(self, r) for r in rowNumbers]
                elif entryType == bool or issubclass(entryType, np.bool_):
                    return [CmpH5Alignment(self, r) for r in np.flatnonzero(rowNumbers)]
        raise TypeError, "Invalid type for CmpH5Reader slicing"

    def __iter__(self):
        return (self[i] for i in xrange(len(self)))

    def __len__(self):
        return len(self.alignmentIndex)

    def __getattr__(self, key):
        # Avoid infinite recursion in degenerate cases.
        return self.__getattribute__("alignmentIndex")[key]

    def close(self):
        if hasattr(self, "file") and self.file != None:
            self.file.close()
            self.file = None

    def __del__(self):
        self.close()
