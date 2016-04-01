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
__all__ = [ "CmpH5Reader",
            "CmpH5Alignment",
            "EmptyCmpH5Error" ]

import h5py, numpy as np, warnings
from bisect import bisect_left, bisect_right
from collections import Counter, OrderedDict
from itertools import groupby
from os.path import abspath, expanduser
from pbcore.io.rangeQueries import makeReadLocator
from pbcore.io._utils import rec_join, arrayFromDataset
from pbcore.io.FastaIO import splitFastaHeader
from pbcore.io.base import ReaderBase
from pbcore.chemistry import decodeTriple, ChemistryLookupError
from pbcore.util.decorators import deprecated

from ._AlignmentMixin import AlignmentRecordMixin, IndexedAlignmentReaderMixin

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

_baseEncodingToInt = np.array([-1]*16)
_baseEncodingToInt[0b0000] = 0
_baseEncodingToInt[0b0001] = 1
_baseEncodingToInt[0b0010] = 2
_baseEncodingToInt[0b0100] = 3
_baseEncodingToInt[0b1000] = 4
_baseEncodingToInt[0b1111] = 5  # 'N' base

# These are 2D tables indexed by (readInt, refInt)
# 'N' base is never considered a mismatch.
_gusfieldTranscriptTable = \
    np.fromstring("ZDDDDDZ"
                  "IMRRRMZ"
                  "IRMRRMZ"
                  "IRRMRMZ"
                  "IRRRMMZ"
                  "IMMMMMZ"
                  "ZZZZZZZ", dtype=np.uint8).reshape(7, 7)
_cigarTranscriptTable = \
    np.fromstring("ZDDDDDZ"
                  "IMMMMMZ"
                  "IMMMMMZ"
                  "IMMMMMZ"
                  "IMMMMMZ"
                  "IMMMMMZ"
                  "ZZZZZZZ", dtype=np.uint8).reshape(7, 7)
_exonerateTranscriptTable = \
    np.fromstring("Z     Z"
                  " |   |Z"
                  "  |  |Z"
                  "   | |Z"
                  "    ||Z"
                  " |||||Z"
                  "ZZZZZZZ", dtype=np.uint8).reshape(7, 7)
_exoneratePlusTranscriptTable = \
    np.fromstring("Z     Z"
                  " |***|Z"
                  " *|**|Z"
                  " **|*|Z"
                  " ***||Z"
                  " |||||Z"
                  "ZZZZZZZ", dtype=np.uint8).reshape(7, 7)

class EmptyCmpH5Error(Exception):
    """An exception raised when CmpH5Reader tries to read from a
    cmp.h5 with no alignments.
    """
    pass

def readFromAlignmentArray(a, gapped=True, complement=False):
    """
    Decode the read component of an alignment array.
    """
    if complement:
        r = _cBasemapArray[a >> 4]
    else:
        r = _basemapArray[a >> 4]
    if not gapped:
        r = r[r != ord("-")]
    return  r.tostring()

def referenceFromAlignmentArray(a, gapped=True, complement=False):
    """
    Decode the reference component of an alignment array.
    """
    if complement:
        r = _cBasemapArray[a & 0b1111]
    else:
        r = _basemapArray[a & 0b1111]
    if not gapped:
        r = r[r != ord("-")]
    return  r.tostring()

def ungappedPulseArray(a):
    """
    Return a pulse array with encoded gaps removed.
    """
    dtype = a.dtype
    if dtype == np.float32:
        return a[~np.isnan(a)]
    elif dtype == np.uint8:
        return a[a != np.uint8(-1)]
    elif dtype == np.uint16:
        return a[a != np.uint16(-1)]
    elif dtype == np.uint32:
        return a[a != np.uint32(-1)]
    elif dtype == np.int8:
        return a[a != ord("-")]
    else:
        raise Exception, "Invalid pulse array type"



# ========================================
# Alignment record type
#

ALIGNMENT_INDEX_COLUMNS = ["AlnID", "AlnGroupID", "MovieID", "RefGroupID",
                           "tStart", "tEnd", "RCRefStrand", "HoleNumber",
                           "SetNumber", "StrobeNumber", "MoleculeID",
                           "rStart", "rEnd", "MapQV", "nM", "nMM", "nIns",
                           "nDel", "Offset_begin", "Offset_end", "nBackRead",
                           "nReadOverlap"]

ALIGNMENT_INDEX_DTYPE = [(COLUMN_NAME, np.uint32)
                         for COLUMN_NAME in ALIGNMENT_INDEX_COLUMNS]


OFFSET_TABLE_DTYPE = [ ("ID",       np.uint32),
                       ("StartRow", np.uint32),
                       ("EndRow",   np.uint32) ]


def _makeBaseFeatureAccessor(featureName):
    def f(self, aligned=True, orientation="native"):
        return self.baseFeature(featureName, aligned, orientation)
    return f

class CmpH5Alignment(AlignmentRecordMixin):
    """
    A lightweight class representing a single alignment record in a
    CmpH5 file, providing access to all columns of a single row of the
    alignment index, and on-demand access to the corresponding
    sequence and pulse features.

    `CmpH5Alignment` objects are obtained by slicing a
    `CmpH5Reader` object:

    .. doctest::

        >>> c[26]
        CmpH5 alignment: +    1       7441       7699

        >>> print c[26]
        CmpH5 alignment: +    1       7441       7699
        <BLANKLINE>
        Read:        m110818_075520_42141_c100129202555500000315043109121112_s2_p0/1009/44_322
        Reference:   lambda_NEB3011
        <BLANKLINE>
        Read length: 278
        Concordance: 0.871
        <BLANKLINE>
          12345678901234567890123456789001223456789012345678890112345678990112344567890011
          AACTGGTCACGGTCGTGGCACTGGTGAAG-CT-GCATACTGATGCACTT-CAC-GCCACGCG-GG-ATG-AACCTG-T-G
          |||||||  ||||  ||||||||| |||| || ||||||||| |||||  ||| |||||||| || ||| |||||| | |
          AACTGGT--CGGT--TGGCACTGG-GAAGCCTTGCATACTGA-GCACT-CCACGGCCACGCGGGGAATGAAACCTGGTGG
        <BLANKLINE>
        <BLANKLINE>
          23456789012345678900123456678901234456789012345678901234566789011234556789012345
          GCATTTGTGCTGCCGGGA-ACGGCG-TTTCGTGT-CTCTGCCGGTGTGGCAGCCGAA-ATGAC-AGAG-CGCGGCCTGGC
          |||||||||||||||||| |||||| |||||| | |||||||||||||||||||||| ||||| |||| |||||||||||
          GCATTTGTGCTGCCGGGAAACGGCGTTTTCGT-TCCTCTGCCGGTGTGGCAGCCGAAAATGACAAGAGCCGCGGCCTGGC
        <BLANKLINE>
        <BLANKLINE>
          67899012345677890123456789901123456789901233456789012345678901234556778901223455
          CAG-AATGCAAT-AACGGGAGGCGC-TG-TGGCTGAT-TTCG-ATAACCTGTTCGATGCTGCCAT-TG-CCCGC-GCC-G
          ||| |||||||| |||||||||||| || |||||||| |||| |||||||||||||||||||||| || ||||| ||| |
          CAGAAATGCAATAAACGGGAGGCGCTTGCTGGCTGATTTTCGAATAACCTGTTCGATGCTGCCATTTGACCCGCGGCCGG
        <BLANKLINE>
        <BLANKLINE>
          6678901234567889012345667890123456789012345678
          -ATGAAACGATAC-GCGGGTAC-ATGGGAACGTCAGCCACCATTAC
           |||||||||||| |||||||| |||||||||||||||||||||||
          AATGAAACGATACGGCGGGTACAATGGGAACGTCAGCCACCATTAC
        <BLANKLINE>
        <BLANKLINE>

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

    @property
    def reader(self):
        return self.cmpH5

    def clippedTo(self, refStart, refEnd):
        """
        Return a new `CmpH5Alignment` that refers to a subalignment of
        this alignment, as induced by clipping to reference
        coordinates `refStart` to `refEnd`.

        .. warning::
            This function takes time linear in the length of the alignment.
        """
        if (refStart >= refEnd or
            refStart >= self.tEnd or
            refEnd   <= self.tStart):
            raise IndexError, "Clipping query does not overlap alignment"
        else:
            return ClippedCmpH5Alignment(self, refStart, refEnd)

    @property
    def _alignmentGroup(self):
        return self.cmpH5._alignmentGroup(self.AlnGroupID)

    @property
    def referenceInfo(self):
        return self.cmpH5.referenceInfo(self.RefGroupID)

    @property
    def referenceName(self):
        return self.referenceInfo.FullName

    @property
    def ReadGroupID(self):
        return np.int32(self.MovieID)

    @property
    def qId(self):
        # Forward compatibility with BAM API
        return self.ReadGroupID

    @property
    def aStart(self):
        # Forward compatibility with BAM API
        return self.rStart

    @property
    def aEnd(self):
        return self.rEnd

    @property
    def holeNumber(self):
        # Forward compatibility with BAM API
        return self.HoleNumber

    @property
    def mapQV(self):
        # Forward compatibility with BAM API
        return self.MapQV

    @property
    def readGroupInfo(self):
        """
        Returns the corresponding record from the `readGroupTable`.
        """
        # TODO: add doctest
        return self.cmpH5.readGroupInfo(self.ReadGroupID)

    @property
    def movieInfo(self):
        """
        .. deprecated:: 0.9.2
           Use :attr:`readGroupInfo`, which is compatible with BAM usage

        Returns a record (extracted from the cmph5's `movieInfoTable`)
        containing information about the movie that the read was
        extracted from.  This record should be accessed using
        dot-notation, according to the column names documented in
        `movieInfoTable`.
        """
        return self.cmpH5.movieInfo(self.MovieID)

    @property
    def movieName(self):
        return self.cmpH5._movieInfo(self.MovieID).Name

    @property
    def isForwardStrand(self):
        return self.RCRefStrand == 0

    @property
    def isReverseStrand(self):
        return self.RCRefStrand == 1

    @property
    def referenceId(self):
        return self.RefGroupID

    @property
    def identity(self):
        """
        Return the identity of this alignment, calculated as
        (#matchs / read length)

        .. doctest::

            >>> c[26].identity
            0.87050359712230219
        """
        if self.readLength == 0:
            return 0.
        else:
            return 1. - float(self.nMM + self.nIns + self.nDel)/self.readLength

    @property
    def accuracy(self):
        """
        Return the identity of this alignment, calculated as
        (#matchs / read length)

        .. deprecated:: 0.9.5
           Use :attr:`identity`
        """
        return self.identity

    @property
    def similarity(self):
        """
        Replicates the pctsimilarity field from blasr, calculated as
        #matches/mean(aligned_length, read_length)
        """
        meanLength = (self.readLength + self.referenceSpan)/2.0

        if meanLength == 0:
            return 0.
        else:
            return float(self.nM/meanLength)

    @property
    def numPasses(self):
        """
        (CCS only) The number subreads that were used to produce this CCS read.
        """
        return self.cmpH5.numPasses[self.rowNumber]

    @property
    def zScore(self):
        """
        (PacBio internal files only)

        The z-score of the alignment, using a null model of a random
        sequence alignment.
        """
        return self.cmpH5.zScore[self.rowNumber]

    @property
    def barcode(self):
        """
        The barcode ID (integer key) for this alignment's read
        Behavior undefined if file is not barcoded.
        """
        return self.cmpH5.barcodes[self.rowNumber]

    @property
    def barcodeName(self):
        """
        The barcode name (string) for this alignment's read
        Behavior undefined if file is not barcoded.
        """
        return self.cmpH5.barcodeName[self.barcode]

    @property
    def sequencingChemistry(self):
        return self.cmpH5.sequencingChemistry[self.MovieID-1]

    @property
    def hqRegionSnr(self):
        raise Exception, "CmpH5 does not support hqRegionSnr"

    def alignmentArray(self, orientation="native"):
        """
        Direct access to the raw, encoded aligment array, which is a
        packed representation of the aligned read and reference.
        """
        alnDs = self._alignmentGroup["AlnArray"]
        alnArray = arrayFromDataset(alnDs, self.Offset_begin, self.Offset_end)
        if self.RCRefStrand and (orientation == "genomic"):
            return alnArray[::-1]
        else:
            return alnArray

    def transcript(self, orientation="native", style="gusfield"):
        """
        A text representation of the alignment moves (see Gusfield).
        This can be useful in pretty-printing an alignment.
        """
        if style == "exonerate+":
            tbl = _exoneratePlusTranscriptTable
        elif style == "exonerate":
            tbl = _exonerateTranscriptTable
        elif style == "cigar":
            tbl = _cigarTranscriptTable
        else:
            tbl = _gusfieldTranscriptTable
        alnArr = self.alignmentArray(orientation)
        readBaseInts = _baseEncodingToInt[alnArr >> 4]
        refBaseInts  = _baseEncodingToInt[alnArr  & 0b1111]
        return tbl[readBaseInts, refBaseInts].tostring()

    def read(self, aligned=True, orientation="native"):
        """
        Return the read portion of the alignment as a string.

        If `aligned` is true, the aligned representation is returned,
        including gaps; otherwise the unaligned read basecalls are
        returned.

        If `orientation` is "native", the returned read bases are
        presented in the order they were read by the sequencing
        machine.  If `orientation` is "genomic", the returned read
        bases are presented in such a way as to collate with the
        forward strand of the reference---which requires reverse
        complementation of reverse-strand reads.
        """
        return readFromAlignmentArray(self.alignmentArray(orientation),
                                      gapped=aligned,
                                      complement=(self.RCRefStrand and
                                                  orientation == "genomic"))

    @property
    def readType(self):
        return self.cmpH5.readType

    def reference(self, aligned=True, orientation="native"):
        """
        Return the read portion of the alignment as a string.

        If `aligned` is true, the aligned representation of the
        reference is returned, including gaps; otherwise the unaligned
        reference bases are returned.

        If `orientation` is "native", the reference is presented in
        the order it is stored in the cmp.h5 file---for reverse-strand
        reads, the reference is reverse-complemented.  If
        `orientation` is "genomic", the forward strand reference is returned.
        """
        return referenceFromAlignmentArray(self.alignmentArray(orientation),
                                           gapped=aligned,
                                           complement=(self.RCRefStrand and
                                                       orientation == "genomic"))

    def referencePositions(self, orientation="native"):
        """
        Returns an array of reference positions such that
        referencePositions[i] = reference position of the i'th column
        in the alignment.  Insertions are grouped with the following
        reference base, in the specified orientation.

        Length of output array = length of alignment
        """
        referenceNonGapMask = (self.alignmentArray(orientation) & 0b1111) != GAP
        if self.RCRefStrand and orientation == "native":
            return self.tEnd - 1 - np.hstack([0, np.cumsum(referenceNonGapMask[:-1])])
        else:
            return self.tStart + np.hstack([0, np.cumsum(referenceNonGapMask[:-1])])

    def readPositions(self, orientation="native"):
        """
        Returns an array of read positions such that
        readPositions[i] = read position of the i'th column
        in the alignment.  Insertions are grouped with the following
        read base, in the specified orientation.

        Length of output array = length of alignment
        """
        readNonGapMask = (self.alignmentArray(orientation) >> 4) != GAP
        if self.RCRefStrand and orientation == "genomic":
            return self.rEnd - 1 - np.hstack([0, np.cumsum(readNonGapMask[:-1])])
        else:
            return self.rStart + np.hstack([0, np.cumsum(readNonGapMask[:-1])])

    def baseFeature(self, featureName, aligned=True, orientation="native"):
        """
        Access a base feature by name.
        """
        pulseDataset = self._alignmentGroup[featureName]
        pulseArray = arrayFromDataset(pulseDataset, self.Offset_begin, self.Offset_end)
        if self.RCRefStrand and orientation == "genomic":
            alignedPulseArray = pulseArray[::-1]
        else:
            alignedPulseArray = pulseArray
        if aligned:
            return alignedPulseArray
        else:
            return ungappedPulseArray(alignedPulseArray)

    IPD            = _makeBaseFeatureAccessor("IPD")
    PulseWidth     = _makeBaseFeatureAccessor("PulseWidth")
    QualityValue   = _makeBaseFeatureAccessor("QualityValue")
    InsertionQV    = _makeBaseFeatureAccessor("InsertionQV")
    DeletionQV     = _makeBaseFeatureAccessor("DeletionQV")
    DeletionTag    = _makeBaseFeatureAccessor("DeletionTag")
    MergeQV        = _makeBaseFeatureAccessor("MergeQV")
    SubstitutionQV = _makeBaseFeatureAccessor("SubstitutionQV")

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
        val += "Read:        " + self.readName           + "\n"
        val += "Reference:   " + self.referenceName      + "\n\n"
        val += "Read length: " + str(self.readLength)    + "\n"
        val += "Concordance: " + "%0.3f" % self.identity + "\n"

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

    def __dir__(self):
        # Special magic improving IPython completion
        basicDir = dir(self.__class__)
        return basicDir + ALIGNMENT_INDEX_COLUMNS

class ClippedCmpH5Alignment(CmpH5Alignment):
    """
    An alignment from a cmp.h5 file that has been clipped to specified
    reference bounds using the `CmpH5Alignment.clippedTo` method.
    """
    # We use these fields to shadow fields in the
    # alignment index row.
    __slots__ = [ "tStart",
                  "tEnd",
                  "rStart",
                  "rEnd",
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
        refPositions = aln.referencePositions(orientation="genomic")
        readPositions = aln.readPositions(orientation="genomic")

        # Clipping positions within the alignment array
        clipStart = bisect_right(refPositions, refStart) - 1
        clipEnd   = bisect_left(refPositions, refEnd)

        # Overlay the new bounds.
        self.tStart = refStart
        self.tEnd   = refEnd
        if aln.isForwardStrand:
            self.Offset_begin = aln.Offset_begin + clipStart
            self.Offset_end   = aln.Offset_begin + clipEnd
            self.rStart = readPositions[clipStart]
        else:
            self.Offset_begin = aln.Offset_end - clipEnd
            self.Offset_end   = aln.Offset_end - clipStart
            self.rEnd   = readPositions[clipStart] + 1
        alnMoveCounts = Counter(self.transcript(style="gusfield"))
        self.nM   = alnMoveCounts["M"]
        self.nMM  = alnMoveCounts["R"]
        self.nIns = alnMoveCounts["I"]
        self.nDel = alnMoveCounts["D"]
        readLength = self.nM + self.nMM + self.nIns
        if aln.isForwardStrand:
            self.rEnd = self.rStart + readLength
        else:
            self.rStart = self.rEnd - readLength
        assert self.rStart <= self.rEnd


# ========================================
# CmpH5 reader class
#
class CmpH5Reader(ReaderBase, IndexedAlignmentReaderMixin):
    """
    The `CmpH5Reader` class is a lightweight and efficient API for
    accessing PacBio ``cmp.h5`` alignment files.  Alignment records
    can be obtained via random access (via Python indexing/slicing),
    iteration, or range queries (via readsInRange).

    .. testsetup:: *

        from pbcore import data
        from pbcore.io import CmpH5Reader
        filename = data.getCmpH5()
        c = CmpH5Reader(filename)
        a0 = c[0]
        a1 = c[1]

    .. doctest::

        >>> import pbcore.data                # For an example data file
        >>> from pbcore.io import CmpH5Reader
        >>> filename = pbcore.data.getCmpH5()
        >>> c = CmpH5Reader(filename)
        >>> c[0]
        CmpH5 alignment: -    1          0        290
        >>> c[0:2]  # doctest: +NORMALIZE_WHITESPACE
        [CmpH5 alignment: -    1          0        290,
         CmpH5 alignment: +    1          0        365]
        >>> sum(aln.readLength for aln in c)
        26103

    """
    def __init__(self, filenameOrH5File, sharedIndex=None):

        # The sharedIndex is a copy of the /AlnInfo/AlnIndex dataset
        # for the file indicated by filenameOrH5File that's already opened and
        # held in memory by another process. When it isn't None, this process
        # doesn't have to keep its own copy of the dataset, which can save
        # memory. This is useful for quiver and kineticsTools where there's a
        # master process that opens the cmph5 file and schedules slaves that
        # only need a read-only copy of the reader.

        # It is an unchecked runtime error to supply a sharedIndex
        # that is not identical to the AlnIndex in the filenameOrH5File

        if isinstance(filenameOrH5File, h5py.File):
            if filenameOrH5File.mode != "r":
                raise ValueError("HDF5 files used by CmpH5Reader must be opened read-only!")
            self.filename = filenameOrH5File.filename
            self.file = filenameOrH5File
        else:
            try:
                self.filename = abspath(expanduser(filenameOrH5File))
                self.file = h5py.File(self.filename, "r")
            except IOError:
                raise IOError, ("Invalid or nonexistent cmp.h5 file %s" % filenameOrH5File)

        self._loadAlignmentInfo(sharedIndex)
        self._loadMovieInfo()
        self._loadReferenceInfo()
        self._loadMiscInfo()

        # These are loaded on demand
        self._readGroupTable = None
        self._readGroupDict  = None

    def _loadAlignmentInfo(self, sharedIndex=None):
        # If a sharedIndex is not provided, read it from the file. If
        # it is provided, don't read anything from the file or store anything
        # else in memory
        if sharedIndex is None:
            if len(self.file["/AlnInfo/AlnIndex"]) == 0:
                raise EmptyCmpH5Error("Empty cmp.h5 file, cannot be read by CmpH5Reader")
            rawAlignmentIndex = self.file["/AlnInfo/AlnIndex"].value
            self._alignmentIndex = (rawAlignmentIndex.view(dtype = ALIGNMENT_INDEX_DTYPE)
                                                     .view(np.recarray)
                                                     .flatten())
        else:
            self._alignmentIndex = sharedIndex
            self._alignmentIndex.setflags(write=False)

        # This is the only sneaky part of this whole class.  We do not
        # store the raw h5py group object; rather we cache a dict of {
        # dataset_name -> dataset }.  This way we avoid B-tree
        # scanning in basic data access.
        self._alignmentGroupById = {}
        for (alnGroupId, alnGroupPath) in zip(self.file["/AlnGroup/ID"][:],
                                              self.file["/AlnGroup/Path"][:]):
            alnGroup = self.file[alnGroupPath]
            self._alignmentGroupById[alnGroupId] = dict(alnGroup.items())


    def _loadMovieInfo(self):
        numMovies = len(self.file["/MovieInfo/ID"])

        if "FrameRate" in self.file["/MovieInfo"]:
            frameRate = self.file["/MovieInfo/FrameRate"].value
            timeScale = 1.0/frameRate
        else:
            frameRate = [np.nan] * numMovies
            timeScale = [1.0] * numMovies

        self._movieInfoTable = np.rec.fromrecords(
            zip(self.file["/MovieInfo/ID"],
                self.file["/MovieInfo/Name"],
                frameRate,
                timeScale),
            dtype=[("ID"                  , int),
                   ("Name"                , object),
                   ("FrameRate"           , float),
                   ("TimeScale"           , float)])

        self._movieDict = {}
        for record in self._movieInfoTable:
            assert record.ID not in self._movieDict
            self._movieDict[record.ID] = record
            self._movieDict[record.Name] = record

    def _loadReadGroupInfo(self):
        # This is invoked lazily to allow operation on cmp.h5s with
        # missing chemistry info.
        assert (self._readGroupTable is None) and (self._readGroupDict is None)
        self._readGroupTable = np.rec.fromrecords(
            zip(self._movieInfoTable.ID,
                self._movieInfoTable.Name,
                [self.readType] * len(self._movieInfoTable.ID),
                self.sequencingChemistry,
                self._movieInfoTable.FrameRate),
            dtype=[("ID"                 , np.int32),
                   ("MovieName"          , "O"),
                   ("ReadType"           , "O"),
                   ("SequencingChemistry", "O"),
                   ("FrameRate"          , float)])
        self._readGroupDict = { rg.ID : rg
                                for rg in self._readGroupTable }

    def _loadReferenceInfo(self):
        _referenceGroupTbl = np.rec.fromrecords(
            zip(self.file["/RefGroup/ID"][:],
                self.file["/RefGroup/RefInfoID"][:],
                [path[1:] for path in self.file["/RefGroup/Path"]]),
            dtype=[("ID"       , int),
                   ("RefInfoID", int),
                   ("Name"     , object)])

        _referenceInfoTbl = np.rec.fromrecords(
            zip(self.file["/RefInfo/ID"][:],
                self.file["/RefInfo/FullName"][:],
                self.file["/RefInfo/Length"][:],
                self.file["/RefInfo/MD5"][:]) ,
            dtype=[("RefInfoID", int),
                   ("FullName" , object),
                   ("Length"   , int),
                   ("MD5"      , object)])

        self._referenceInfoTable = \
            rec_join("RefInfoID", _referenceGroupTbl, _referenceInfoTbl, jointype="inner")

        if self.isSorted:
            _offsetTable = self.file["/RefGroup/OffsetTable"].value \
                              .view(dtype=OFFSET_TABLE_DTYPE)       \
                              .view(np.recarray)                    \
                              .flatten()
            self._referenceInfoTable = rec_join("ID",
                                                self._referenceInfoTable,
                                                _offsetTable,
                                                jointype="inner")
        self._referenceDict = {}
        self._readLocatorByKey = {}

        # For cmp.h5 files with large numbers of references, accessing
        # the recarray fields in the inner loop was terribly slow.
        # This makes things faster, though the code is less
        # straightforward.  (One of the tradeoffs we have to make
        # without a compiler to help us...)
        recordID       = self._referenceInfoTable.ID
        recordName     = self._referenceInfoTable.Name
        recordFullName = self._referenceInfoTable.FullName
        recordMD5      = self._referenceInfoTable.MD5

        for i, record in enumerate(self._referenceInfoTable):
            if recordID[i] != -1:
                assert recordID[i] != record.Name
                shortName = splitFastaHeader(record.FullName)[0]
                if (shortName         in self._referenceDict or
                    recordID[i]       in self._referenceDict or
                    recordName[i]     in self._referenceDict or
                    recordFullName[i] in self._referenceDict or
                    recordMD5[i]      in self._referenceDict):
                    raise ValueError, "Duplicate reference contig sequence or identifier"
                else:
                    self._referenceDict[shortName]         = record
                    self._referenceDict[recordID[i]]       = record
                    self._referenceDict[recordName[i]]     = record
                    self._referenceDict[recordFullName[i]] = record
                    self._referenceDict[recordMD5[i]]      = record

                if self.isSorted:
                    readLocator = makeReadLocator(self, recordID[i])
                    self._readLocatorByKey[recordID[i]] = readLocator
                    self._readLocatorByKey[shortName] = readLocator

    def _loadMiscInfo(self):
        if "NumPasses" in self.file["/AlnInfo"]:
            self.numPasses = self.file["/AlnInfo/NumPasses"].value

        if "Barcode" in self.file["/AlnInfo"]:
            # Build forward and backwards id<->label lookup tables
            self._barcodeName = OrderedDict(zip(self.file["/BarcodeInfo/ID"],
                                                self.file["/BarcodeInfo/Name"]))
            self._barcode     = OrderedDict(zip(self.file["/BarcodeInfo/Name"],
                                                self.file["/BarcodeInfo/ID"]))
            # Barcode ID per row
            self._barcodes = self.file["/AlnInfo/Barcode"].value[:,1]

        if "ZScore" in self.file["/AlnInfo"]:
            self.zScore = self.file["/AlnInfo/ZScore"].value

        self._sequencingChemistry = None


    @property
    def sequencingChemistry(self):
        if self._sequencingChemistry is None:
            mi = dict(self.file["/MovieInfo"])
            if (("BindingKit" in mi) and
                ("SequencingKit" in mi) and
                ("SoftwareVersion" in mi)):
                # New way
                self._sequencingChemistry = \
                    [ decodeTriple(bk, sk, sv)
                      for (bk, sk, sv) in zip(
                              mi["BindingKit"],
                              mi["SequencingKit"],
                              mi["SoftwareVersion"]) ]
            elif "SequencingChemistry" in mi:
                # Old way
                self._sequencingChemistry = mi["SequencingChemistry"].value
            else:
                raise ChemistryLookupError, "Chemistry information could not be found in cmp.h5!"
        return self._sequencingChemistry

    @property
    def index(self):
        return self.alignmentIndex

    @property
    def alignmentIndex(self):
        """
        Return the alignment index data structure, which is the
        central data structure in the cmp.h5 file, as a numpy
        recarray.

        The `dtype` of the recarray is::

            dtype([('AlnID', int),
                   ('AlnGroupID', int),
                   ('MovieID', int),
                   ('RefGroupID', int),
                   ('tStart', int),
                   ('tEnd', int),
                   ('RCRefStrand', int),
                   ('HoleNumber', int),
                   ('SetNumber', int),
                   ('StrobeNumber', int),
                   ('MoleculeID', int),
                   ('rStart', int),
                   ('rEnd', int),
                   ('MapQV', int),
                   ('nM', int),
                   ('nMM', int),
                   ('nIns', int),
                   ('nDel', int),
                   ('Offset_begin', int),
                   ('Offset_end', int),
                   ('nBackRead', int),
                   ('nReadOverlap', int)])

        Access to the alignment index is provided to allow users to
        perform vectorized computations over all alignments in the file.

        .. doctest::

            >>> c.alignmentIndex.MapQV[0:10]
            array([254, 254,   0, 254, 254, 254, 254, 254, 254, 254], dtype=uint32)

        Alignment index fields are also exposed as fields of the
        `CmpH5Reader` object, allowing a convenient shorthand.

        .. doctest::

            >>> c.MapQV[0:10]
            array([254, 254,   0, 254, 254, 254, 254, 254, 254, 254], dtype=uint32)

        The alignment index row for a given alignment can also be
        accessed directly as a field of a `CmpH5Alignment` object

        .. doctest::

            >>> c[26].MapQV
            254
        """
        return self._alignmentIndex

    @property
    def movieInfoTable(self):
        """
        .. deprecated:: 0.9.2
           Use :attr:`readGroupTable`, which is compatible with BAM usage

        Return a numpy recarray summarizing source movies for the
        reads in this file.

        The `dtype` of this recarray is::

            dtype([('ID', 'int'),
                   ('Name', 'string'),
                   ('FrameRate', 'float'),
                   ('TimeScale', 'float')])

        `TimeScale` is the factor to multiply time values (IPD,
        PulseWidth) by in order to get times in seconds.  The
        `FrameRate` field should *not* be used directly as it will be
        NaN for pre-1.3 cmp.h5 files.
        """
        return self._movieInfoTable

    @property
    def referenceInfoTable(self):
        """
        .. _referenceInfoTable:

        Return a numpy recarray summarizing the references that were
        aligned against.

        The `dtype` of this recarray is::

            dtype([('RefInfoID', int),
                   ('ID', int),
                   ('Name', string),
                   ('FullName', string),
                   ('Length', int),
                   ('MD5', string),
                   ('StartRow', int),
                   ('EndRow', int) ])

        (the last two columns are omitted for unsorted `cmp.h5` files).
        """
        return self._referenceInfoTable

    @property
    def readType(self):
        """
        Either "standard" or "CCS", indicating the type of reads that
        were aligned to the reference.

        .. doctest::

            >>> c.readType
            'standard'
        """
        return self.file.attrs["ReadType"]

    @property
    def version(self):
        """
        The CmpH5 format version string.

        .. doctest::

            >>> c.version
            '1.2.0.SF'
        """
        return self.file.attrs["Version"]

    def versionAtLeast(self, minimalVersion):
        """
        Compare the file version to `minimalVersion`.

        .. doctest::

            >>> c.versionAtLeast("1.3.0")
            False
        """
        myVersionTuple = map(int, self.version.split(".")[:3])
        minimalVersionTuple = map(int, minimalVersion.split(".")[:3])
        return myVersionTuple >= minimalVersionTuple

    def softwareVersion(self, programName):
        """
        Return the version of program `programName` that processed
        this file.
        """
        filelog = dict(zip(self.file["/FileLog/Program"],
                           self.file["/FileLog/Version"]))
        return filelog.get(programName, None)

    @property
    def isSorted(self):
        return "OffsetTable" in self.file["/RefGroup"]

    @property
    def isBarcoded(self):
        return "Barcode" in self.file["/AlnInfo"]

    @property
    def isEmpty(self):
        return len(self.file["/AlnInfo/AlnIndex"]) == 0

    def _alignmentGroup(self, alnGroupId):
        return self._alignmentGroupById[alnGroupId]

    @property
    def movieNames(self):
        return set([mi.Name for mi in self._movieDict.values()])

    @property
    def ReadGroupID(self):
        return self.MovieID

    @property
    def readGroupTable(self):
        # TODO: add doctest
        if self._readGroupTable is None:
            self._loadReadGroupInfo()
        return self._readGroupTable

    def readGroupInfo(self, rgId):
        """
        Access information about a movie whose reads are represented
        in the file.

        The returned value is a record from the :attr:`readGroupTable`
        """
        # TODO: add doctest
        if self._readGroupDict is None:
            self._loadReadGroupInfo()
        return self._readGroupDict[rgId]


    def _movieInfo(self, movieId):
        return self._movieDict[movieId]

    def movieInfo(self, movieId):
        """
        .. deprecated:: 0.9.2
           Use :attr:`readGroupInfo`, which is compatible with BAM usage

        Access information about a movie whose reads are represented
        in the file.

        The returned value is a record from the :attr:`movieInfoTable`
        """
        return self._movieInfo(movieId)

    def referenceInfo(self, key):
        """
        Access information about a reference that was aligned against.
        Key can be reference ID (integer), name ("ref000001"), full
        name (e.g. "lambda_NEB3011"), truncated full name (full name
        up to the first whitespace, following the samtools convention)
        or MD5 sum hex string (e.g. "a1319ff90e994c8190a4fe6569d0822a").

        The returned value is a record from the :ref:referenceInfoTable .

        .. doctest::

            >>> ri = c.referenceInfo("ref000001")
            >>> ri.FullName
            'lambda_NEB3011'
            >>> ri.MD5
            'a1319ff90e994c8190a4fe6569d0822a'

        """
        return self._referenceDict[key]

    def readsInRange(self, refKey, refStart, refEnd, justIndices=False):
        """
        Get a list of reads overlapping (i.e., intersecting---not
        necessarily spanning) a given reference window.

        If `justIndices` is ``False``, the list returned will contain
        `CmpH5Alignment` objects.

        If `justIndices` is ``True``, the list returned will contain
        row numbers in the alignment index table.  Slicing the
        `CmpH5Reader` object with these row numbers can be used to get
        the corresponding `CmpH5Alignment` objects.

        The contig key can be either the ``RefID``, or the short name
        (FASTA header up to first space).

        .. doctest::

            >>> c.readsInRange(1, 0, 1000) # doctest: +NORMALIZE_WHITESPACE
            [CmpH5 alignment: -    1          0        290,
             CmpH5 alignment: +    1          0        365]

            >>> rowNumbers = c.readsInRange(1, 0, 1000, justIndices=True)
            >>> rowNumbers
            array([0, 1], dtype=uint32)
        """

        if not self.isSorted:
            raise Exception, "CmpH5 is not sorted"
        rowNumbers = self._readLocatorByKey[refKey](refStart, refEnd, justIndices=True)
        if justIndices:
            return rowNumbers
        else:
            return self[rowNumbers]

    def hasBaseFeature(self, featureName):
        """
        Are the datasets for pulse feature `featureName` loaded in
        this file?  Specifically, is it loaded for all movies within
        this cmp.h5?

        .. doctest::

            >>> c.hasBaseFeature("InsertionQV")
            True
            >>> c.hasBaseFeature("MergeQV")
            False

        """
        return all(featureName in alnGroup.keys()
                   for alnGroup in self._alignmentGroupById.values())

    def baseFeaturesAvailable(self):
        """
        What pulse features are available in this cmp.h5 file?

        .. doctest::

            >>> c.baseFeaturesAvailable()
            [u'QualityValue', u'IPD', u'PulseWidth', u'InsertionQV', u'DeletionQV']

        """
        baseFeaturesByMovie = [ alnGroup.keys()
                                 for alnGroup in self._alignmentGroupById.values() ]
        baseFeaturesAvailableAsSet = set.intersection(*map(set, baseFeaturesByMovie))
        baseFeaturesAvailableAsSet.discard("AlnArray")
        return list(baseFeaturesAvailableAsSet)

    @property
    def barcode(self):
        """
        Returns a dict mapping of barcode name to integer barcode.
        Behavior undefined if file is not barcoded.
        """
        return self._barcode

    @property
    def barcodeName(self):
        """
        Returns a dict mapping of barcode integer id to name.
        Behavior undefined if file is not barcoded.
        """
        return self._barcodeName

    @property
    def barcodes(self):
        """
        Returns an array of barcode integer ids, of the same length as the
        alignment array.

        Behavior undefined if file is not barcoded.
        """
        return self._barcodes

    @property
    def qId(self):
        # Forward compatibility with BAM API
        return self.ReadGroupID

    @property
    def holeNumber(self):
        # Forward compatibility with BAM API
        return self.HoleNumber

    @property
    def mapQV(self):
        # Forward compatibility with BAM API
        return self.MapQV

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
        if hasattr(self, "file") and self.file is not None:
            self.file.close()
            self.file = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __dir__(self):
        # Special magic improving IPython completion
        basicDir = dir(self.__class__)
        return basicDir + ALIGNMENT_INDEX_COLUMNS
