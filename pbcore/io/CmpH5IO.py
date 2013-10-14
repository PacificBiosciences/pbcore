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

# Author: David Alexander
__all__ = [ "CmpH5Reader",
            "CmpH5Alignment" ]

import h5py, numpy as np
from bisect import bisect_left, bisect_right
from collections import Counter, OrderedDict
from itertools import groupby
from os.path import abspath, expanduser
from pbcore.io.rangeQueries import makeReadLocator
from pbcore.io._utils import rec_join, arrayFromDataset
from pbcore.io.BasH5IO import BasH5Collection

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


def _makePulseFeatureAccessor(featureName):
    def f(self, aligned=True, orientation="native"):
        return self.pulseFeature(featureName, aligned, orientation)
    return f

class CmpH5Alignment(object):
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
    def zmw(self):
        return self.zmwRead.zmw

    @property
    def zmwRead(self):
        if not self.cmpH5.moviesAttached:
            raise ValueError("Movies not attached!")
        return self.cmpH5.basH5Collection[self.readName]

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
    def alignmentGroup(self):
        return self.cmpH5.alignmentGroup(self.AlnGroupID)

    @property
    def referenceInfo(self):
        return self.cmpH5.referenceInfo(self.RefGroupID)

    @property
    def referenceName(self):
        return self.referenceInfo.FullName

    @property
    def readName(self):
        """
        Return the name of the read that was aligned, in standard
        PacBio format.
        """
        return "%s/%d/%d_%d" % (self.movieInfo.Name,
                                self.HoleNumber,
                                self.rStart,
                                self.rEnd)
    @property
    def movieInfo(self):
        """
        Returns a record (extracted from the cmph5's `movieInfoTable`)
        containing information about the movie that the read was
        extracted from.  This record should be accessed using
        dot-notation, according to the column names documented in
        `movieInfoTable`.

        .. doctest::

            >>> mi = c[0].movieInfo
            >>> mi.Name, mi.ID, mi.TimeScale
            ('m110818_075520_42141_c100129202555500000315043109121112_s2_p0', 1, 1.0)
        """
        return self.cmpH5.movieInfo(self.MovieID)

    @property
    def isForwardStrand(self):
        return self.RCRefStrand == 0

    @property
    def isReverseStrand(self):
        return self.RCRefStrand == 1

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
        return self.rStart

    @property
    def readEnd(self):
        """
        The right bound of the alignment, in read coordinates (from the BAS.H5 file).
        """
        return self.rEnd

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
        return self.alignedLength - self.nDel

    @property
    def alignedLength(self):
        """
        The length of the alignment.
        """
        return self.Offset_end - self.Offset_begin

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

    @property
    def accuracy(self):
        """
        Return the accuracy of this alignment, calculated as
        (#matchs / read length)

        .. doctest::

            >>> c[26].accuracy
            0.87050359712230219
        """
        if self.readLength == 0:
            return 0.
        else:
            return 1. - float(self.nMM + self.nIns + self.nDel)/self.readLength


    @property
    def numPasses(self):
        """
        (CCS only) The number subreads that were used to produce this CCS read.
        """
        return self.cmpH5.numPasses[self.rowNumber]

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

    def alignmentArray(self, orientation="native"):
        """
        Direct access to the raw, encoded aligment array, which is a
        packed representation of the aligned read and reference.
        """
        alnDs = self.alignmentGroup["AlnArray"]
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

    def cigar(self, orientation="native"):
        """
        Return the CIGAR string for the alignment in the given
        orientation.
        """
        cigarTranscript = self.transcript(orientation, "cigar")
        # Run length encoding: (done fairly naively---my attempts at
        # doing this in numpy ended up being *slower*
        collapsed = [(len(list(group)),name)
                      for name, group in groupby(cigarTranscript)]
        cigarString = ''.join([('%s%s') % el for el in collapsed])
        return cigarString

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

    def pulseFeature(self, featureName, aligned=True, orientation="native"):
        """
        Access a pulse feature by name.
        """
        pulseDataset = self.alignmentGroup[featureName]
        pulseArray = arrayFromDataset(pulseDataset, self.Offset_begin, self.Offset_end)
        if self.RCRefStrand and orientation == "genomic":
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
        val += "Read:        " + self.readName           + "\n"
        val += "Reference:   " + self.referenceName      + "\n\n"
        val += "Read length: " + str(self.readLength)    + "\n"
        val += "Concordance: " + "%0.3f" % self.accuracy + "\n"

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
        return ALIGNMENT_INDEX_COLUMNS

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

        # Overlay the new bounds.  The logic for setting rStart, rEnd
        # is tragically complicated, due to the end-exclusive
        # coordinate system.
        self.tStart = refStart
        self.tEnd   = refEnd
        if aln.isForwardStrand:
            self.Offset_begin = aln.Offset_begin + clipStart
            self.Offset_end   = aln.Offset_begin + clipEnd
            self.rStart = readPositions[clipStart]
            self.rEnd   = readPositions[clipEnd - 1] + 1
        else:
            self.Offset_begin = aln.Offset_end - clipEnd
            self.Offset_end   = aln.Offset_end - clipStart
            self.rStart = readPositions[clipEnd - 1]
            self.rEnd   = readPositions[clipStart] + 1
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
    The `CmpH5Reader` class is a lightweight and efficient API for
    accessing PacBio ``cmp.h5`` alignment files.  Alignment records
    can be obtained via random access (via Python indexing/slicing),
    iteration, or range queries (via readsInRange).

    .. testsetup:: *

        from pbcore import data
        from pbcore.io import CmpH5Reader
        filename = data.getCmpH5()['cmph5']
        c = CmpH5Reader(filename)
        a0 = c[0]
        a1 = c[1]

    .. doctest::

        >>> import pbcore.data                # For an example data file
        >>> from pbcore.io import CmpH5Reader
        >>> filename = pbcore.data.getCmpH5()["cmph5"]
        >>> c = CmpH5Reader(filename)
        >>> c[0]
        CmpH5 alignment: -    1          0        290
        >>> c[0:2]  # doctest: +NORMALIZE_WHITESPACE
        [CmpH5 alignment: -    1          0        290,
         CmpH5 alignment: +    1          0        365]
        >>> sum(aln.readLength for aln in c)
        26103

    """
    def __init__(self, filenameOrH5File):
        if isinstance(filenameOrH5File, h5py.File):
            if filenameOrH5File.mode != "r":
                raise ValueError("HDF5 files used by CmpH5Reader must be opened read-only!")
            self.filename = filenameOrH5File.filename
            self.file = filenameOrH5File
        else:
            self.filename = abspath(expanduser(filenameOrH5File))
            self.file = h5py.File(self.filename, "r")
        rawAlignmentIndex = self.file["/AlnInfo/AlnIndex"].value
        self._alignmentIndex = rawAlignmentIndex.view(dtype = ALIGNMENT_INDEX_DTYPE) \
                                                .view(np.recarray)                   \
                                                .flatten()

        # This is the only sneaky part of this whole class.  We do not
        # store the raw h5py group object; rather we cache a dict of {
        # dataset_name -> dataset }.  This way we avoid B-tree
        # scanning in basic data access.
        self._alignmentGroupById = {}
        for (alnGroupId, alnGroupPath) in zip(self.file["/AlnGroup/ID"],
                                              self.file["/AlnGroup/Path"]):
            alnGroup = self.file[alnGroupPath]
            self._alignmentGroupById[alnGroupId] = dict(alnGroup.items())

        numMovies = len(self.file["/MovieInfo/ID"])

        if "FrameRate" in self.file["/MovieInfo"]:
            frameRate = self.file["/MovieInfo/FrameRate"].value
            timeScale = 1.0/frameRate
        else:
            frameRate = [np.nan] * numMovies
            timeScale = [1.0] * numMovies

        if "SequencingChemistry" in self.file["/MovieInfo"]:
            sequencingChemistry = self.file["/MovieInfo/SequencingChemistry"].value
        else:
            sequencingChemistry = ["unknown"] * numMovies


        self._movieInfoTable = np.rec.fromrecords(
            zip(self.file["/MovieInfo/ID"],
                self.file["/MovieInfo/Name"],
                frameRate,
                timeScale,
                sequencingChemistry),
            dtype=[("ID"                  , int),
                   ("Name"                , object),
                   ("FrameRate"           , float),
                   ("TimeScale"           , float),
                   ("SequencingChemistry" , object)])

        self._movieDict = {}
        for record in self._movieInfoTable:
            assert record.ID not in self._movieDict
            self._movieDict[record.ID] = record

        _referenceGroupTbl = np.rec.fromrecords(
            zip(self.file["/RefGroup/ID"],
                self.file["/RefGroup/RefInfoID"],
                [path[1:] for path in self.file["/RefGroup/Path"]]),
            dtype=[("ID"       , int),
                   ("RefInfoID", int),
                   ("Name"     , object)])

        _referenceInfoTbl = np.rec.fromrecords(
            zip(self.file["/RefInfo/ID"],
                self.file["/RefInfo/FullName"],
                self.file["/RefInfo/Length"],
                self.file["/RefInfo/MD5"]) ,
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
        for record in self._referenceInfoTable:
            if record.ID != -1:
                assert record.ID != record.Name
                if (record.ID       in self._referenceDict or
                    record.Name     in self._referenceDict or
                    record.FullName in self._referenceDict or
                    record.MD5      in self._referenceDict):
                    raise ValueError, "Duplicate reference contig sequence or identifier"
                else:
                    self._referenceDict[record.ID]       = record
                    self._referenceDict[record.Name]     = record
                    self._referenceDict[record.FullName] = record
                    self._referenceDict[record.MD5]      = record

        self._readLocatorById = {}
        if self.isSorted:
            for refId in self.file["/RefGroup/ID"]:
                self._readLocatorById[refId] = makeReadLocator(self, refId)

        if "NumPasses" in self.file["/AlnInfo"]:
            self.numPasses = self.file["/AlnInfo/NumPasses"].value

        if "Barcode" in self.file["/AlnInfo"]:
            # Build forward and backwards id<->label lookup tables
            self._barcodeName = OrderedDict(zip(self.file["/BarcodeInfo/ID"],
                                                self.file["/BarcodeInfo/Name"]))
            self._barcode     = OrderedDict(zip(self.file["/BarcodeInfo/Name"],
                                                self.file["/BarcodeInfo/ID"]))
            # Barcode ID per row
            self._barcodes = self.file["/AlnInfo/Barcode"].value[:,0]

        self.basH5Collection = None

    def attach(self, fofnFilename):
        """
        Attach the actual movie data files that were used to create this
        alignment file.

        TODO: enable supplying movie names or fofn names here
        TODO: enable unattach
        TODO: sanity check that the movie names are all there?
        """
        self.basH5Collection = BasH5Collection(fofnFilename)

    @property
    def moviesAttached(self):
        return (self.basH5Collection is not None)

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

    @property
    def primaryVersion(self):
        """
        The version of PacBio Primary Analysis software that produced
        the ``bas.h5`` input file to the aligner.
        """
        return self.file.attrs["PrimaryVersion"]

    def primaryVersionAtLeast(self, minimalVersion):
        """
        Compare ``primaryVersion`` to ``minimalVersion``
        """
        myVersionTuple = map(int, self.primaryVersion.split("."))
        minimalVersionTuple = map(int, minimalVersion.split("."))
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
        return len(self.file["/AlnInfo"]) == 0

    def alignmentGroup(self, alnGroupId):
        return self._alignmentGroupById[alnGroupId]

    @property
    def movieNames(self):
        return set([mi.Name for mi in self._movieDict.values()])

    def movieInfo(self, movieId):
        """
        Access information about a movie whose reads are represented
        in the file.

        The returned value is a record from the :attr:`movieInfoTable`

        .. doctest::

            >>> mi = c.movieInfo(1)
            >>> mi.Name
            'm110818_075520_42141_c100129202555500000315043109121112_s2_p0'
            >>> mi.TimeScale
            1.0

        """
        return self._movieDict[movieId]

    def referenceInfo(self, key):
        """
        Access information about a reference that was aligned against.
        Key can be reference ID (integer), name ("ref000001"), full
        name (e.g. "lambda_NEB3011"), or MD5 sum hex string
        (e.g. "a1319ff90e994c8190a4fe6569d0822a").

        The returned value is a record from the :ref:referenceInfoTable .

        .. doctest::

            >>> ri = c.referenceInfo("ref000001")
            >>> ri.FullName
            'lambda_NEB3011'
            >>> ri.MD5
            'a1319ff90e994c8190a4fe6569d0822a'

        """
        return self._referenceDict[key]

    def readsInRange(self, refId, refStart, refEnd, justIndices=False):
        """
        Get a list of reads overlapping (i.e., intersecting---not
        necessarily spanning) a given reference window.

        If `justIndices` is ``False``, the list returned will contain
        `CmpH5Alignment` objects.

        If `justIndices` is ``True``, the list returned will contain
        row numbers in the alignment index table.  Slicing the
        `CmpH5Reader` object with these row numbers can be used to get
        the corresponding `CmpH5Alignment` objects.

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
        rowNumbers = self._readLocatorById[refId](refStart, refEnd, justIndices=True)
        if justIndices:
            return rowNumbers
        else:
            return self[rowNumbers]

    def hasPulseFeature(self, featureName):
        """
        Are the datasets for pulse feature `featureName` loaded in
        this file?  Specifically, is it loaded for all movies within
        this cmp.h5?

        .. doctest::

            >>> c.hasPulseFeature("InsertionQV")
            True
            >>> c.hasPulseFeature("MergeQV")
            False

        """
        return all(featureName in alnGroup.keys()
                   for alnGroup in self._alignmentGroupById.values())

    def pulseFeaturesAvailable(self):
        """
        What pulse features are available in this cmp.h5 file?

        .. doctest::

            >>> c.pulseFeaturesAvailable()
            [u'QualityValue', u'IPD', u'PulseWidth', u'InsertionQV', u'DeletionQV']

        """
        pulseFeaturesByMovie = [ alnGroup.keys()
                                 for alnGroup in self._alignmentGroupById.values() ]
        pulseFeaturesAvailableAsSet = set.intersection(*map(set, pulseFeaturesByMovie))
        pulseFeaturesAvailableAsSet.discard("AlnArray")
        return list(pulseFeaturesAvailableAsSet)

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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __dir__(self):
        # Special magic improving IPython completion
        return ALIGNMENT_INDEX_COLUMNS
