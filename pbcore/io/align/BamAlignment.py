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

from functools import wraps
from bisect import bisect_right, bisect_left

from pbcore.sequence import reverseComplement
from ._BamSupport import *
from ._AlignmentMixin import AlignmentRecordMixin

import os

__all__ = [ "BamAlignment" ]

def _unrollCigar(cigar, exciseSoftClips=False):
    """
    Run-length decode the cigar (input is BAM packed CIGAR, not a cigar string)

    Removes hard clip ops from the output.  Remove all?
    """
    cigarArray = np.array(cigar, dtype=int)
    hasHardClipAtLeft = cigarArray[0,0] == BAM_CHARD_CLIP
    hasHardClipAtRight = cigarArray[-1,0] == BAM_CHARD_CLIP
    ncigar = len(cigarArray)
    x = np.s_[int(hasHardClipAtLeft) : ncigar - int(hasHardClipAtRight)]
    ops = np.repeat(cigarArray[x,0], cigarArray[x,1])
    if exciseSoftClips:
        return ops[ops != BAM_CSOFT_CLIP]
    else:
        return ops

def _makeBaseFeatureAccessor(featureName):
    def f(self, aligned=True, orientation="native"):
        return self.baseFeature(featureName, aligned, orientation)
    return f

def requiresReference(method):
    @wraps(method)
    def f(bamAln, *args, **kwargs):
        if not bamAln.bam.isReferenceLoaded:
            raise UnavailableFeature, "this feature requires loaded reference sequence"
        else:
            return method(bamAln, *args, **kwargs)
    return f

def requiresPbi(method):
    @wraps(method)
    def f(bamAln, *args, **kwargs):
        if not bamAln.hasPbi:
            raise UnavailableFeature, "this feature requires a PacBio BAM index"
        else:
            return method(bamAln, *args, **kwargs)
    return f

def requiresMapping(method):
    @wraps(method)
    def f(bamAln, *args, **kwargs):
        if bamAln.isUnmapped:
            raise UnavailableFeature, "this feature requires a *mapped* BAM record"
        else:
            return method(bamAln, *args, **kwargs)
    return f


class BamAlignment(AlignmentRecordMixin):
    def __init__(self, bamReader, pysamAlignedRead, rowNumber=None):
        #TODO: make these __slot__
        self.peer        = pysamAlignedRead
        self.bam         = bamReader
        self.rowNumber   = rowNumber
        self.tStart      = self.peer.pos
        self.tEnd        = self.peer.aend
        # Our terminology doesn't agree with pysam's terminology for
        # "query", "read".  This makes this code confusing.
        if self.peer.is_reverse:
            clipLeft  = self.peer.rlen - self.peer.qend
            clipRight = self.peer.qstart
        else:
            clipLeft  = self.peer.qstart
            clipRight = self.peer.rlen - self.peer.qend
        # handle virtual qStart/qEnd for CCS READTYPE
        if self.isCCS:
            qs, qe = 0, self.qLen
        else:
            qs, qe = self.qStart, self.qEnd
        # alignment start/end (aStart/aEnd)
        self.aStart = qs + clipLeft
        self.aEnd   = qe - clipRight
        # Cache of unrolled cigar, in genomic orientation
        self._unrolledCigar = None

    @property
    def reader(self):
        return self.bam

    @property
    def hasPbi(self):
        return self.rowNumber is not None

    @property
    def qId(self):
        return self.readGroupInfo.ID

    @property
    def qName(self):
        return self.peer.qname

    @property
    def qStart(self):
        if self.isCCS:
            raise UnavailableFeature("No qStart for CCS READTYPE")
        return self.peer.opt("qs")

    @property
    def qEnd(self):
        if self.isCCS:
            raise UnavailableFeature("No qEnd for CCS READTYPE")
        return self.peer.opt("qe")

    @property
    def qLen(self):
        return self.peer.query_length

    @property
    def tId(self):
        return self.peer.tid

    @property
    def isCCS(self):
        return self.readType == "CCS"

    @property
    def isMapped(self):
        return not self.isUnmapped

    @property
    def isUnmapped(self):
        return self.peer.is_unmapped

    @property
    def isReverseStrand(self):
        return self.peer.is_reverse

    @property
    def isForwardStrand(self):
        return not self.peer.is_reverse

    @property
    def HoleNumber(self):
        return self.peer.opt("zm")

    @property
    def MapQV(self):
        return self.peer.mapq

    @requiresMapping
    def clippedTo(self, refStart, refEnd):
        """
        Return a new `BamAlignment` that refers to a subalignment of
        this alignment, as induced by clipping to reference
        coordinates `refStart` to `refEnd`.

        .. warning::
            This function takes time linear in the length of the alignment.
        """
        assert type(self) is BamAlignment
        if (refStart >= refEnd or
            refStart >= self.tEnd or
            refEnd   <= self.tStart):
            raise IndexError, "Clipping query does not overlap alignment"

        # The clipping region must intersect the alignment, though it
        # does not have to be contained wholly within it.
        refStart = max(self.referenceStart, refStart)
        refEnd   = min(self.referenceEnd,   refEnd)
        refPositions = self.referencePositions(orientation="genomic")
        readPositions = self.readPositions(orientation="genomic")
        uc = self.unrolledCigar(orientation="genomic")

        # Clipping positions within the alignment array
        clipStart = bisect_right(refPositions, refStart) - 1
        clipEnd   = bisect_left(refPositions, refEnd)

        tStart = refStart
        tEnd   = refEnd
        cUc = uc[clipStart:clipEnd]
        readLength = np.count_nonzero(cUc != BAM_CDEL)
        if self.isForwardStrand:
            aStart = readPositions[clipStart]
            aEnd = aStart + readLength
        else:
            aEnd   = readPositions[clipStart] + 1
            aStart = aEnd - readLength
        return ClippedBamAlignment(self, tStart, tEnd, aStart, aEnd, cUc)

    @property
    @requiresMapping
    def referenceInfo(self):
        return self.bam.referenceInfo(self.referenceId)

    @property
    @requiresMapping
    def referenceName(self):
        return self.referenceInfo.FullName

    @property
    def movieName(self):
        return self.readGroupInfo.MovieName

    @property
    def readGroupInfo(self):
        return self.bam.readGroupInfo(rgAsInt(self.peer.opt("RG")))

    @property
    def readScore(self):
        """
        Return the "read score", a de novo prediction (not using any
        alignment) of the accuracy (between 0 and 1) of this read.

        .. note::

            This capability was not available in `cmp.h5` files, so
            use of this property can result in code that won't work on
            legacy data.
        """
        return self.peer.opt("rq")

    @property
    def readType(self):
        return self.readGroupInfo.ReadType

    @property
    def scrapType(self):
        if self.readType != "SCRAP":
            raise ValueError, "scrapType not meaningful for non-scrap reads"
        else:
            return self.peer.opt("sc")

    @property
    def sequencingChemistry(self):
        return self.readGroupInfo.SequencingChemistry

    @property
    def hqRegionSnr(self):
        """
        Return the per-channel SNR averaged over the HQ region.

        .. note::

            This capability was not available in `cmp.h5` files, so
            use of this property can result in code that won't work on
            legacy data.
        """
        return self.peer.opt("sn")

    @property
    def referenceId(self):
        return self.tId

    @property
    def queryStart(self):
        return self.qStart

    @property
    def queryEnd(self):
        return self.qEnd

    #TODO: provide this in cmp.h5 but throw "unsupported"
    @property
    def queryName(self):
        return self.peer.qname

    @property
    @requiresMapping
    def identity(self):
        if self.hasPbi:
            # Fast (has pbi)
            if self.readLength == 0:
                return 0.
            else:
                return 1. - float(self.nMM + self.nIns + self.nDel)/self.readLength
        else:
            # Slow (no pbi);
            if self.readLength == 0:
                return 0.
            else:
                x = self.transcript()
                nMM  = x.count("R")
                nIns = x.count("I")
                nDel = x.count("D")
                return 1. - float(nMM + nIns + nDel)/self.readLength

    @property
    def mapQV(self):
        return self.peer.mapq

    @property
    def numPasses(self):
        return self.peer.opt("np")

    @property
    def zScore(self):
        raise UnavailableFeature("No ZScore in BAM")

    @property
    def barcode(self):
        raise Unimplemented()

    @property
    def barcodeName(self):
        raise Unimplemented()

    def transcript(self, orientation="native", style="gusfield"):
        """
        A text representation of the alignment moves (see Gusfield).
        This can be useful in pretty-printing an alignment.
        """
        uc = self.unrolledCigar(orientation)
        #                                    MIDNSHP=X
        _exoneratePlusTrans = np.fromstring("Z  ZZZZ|*", dtype=np.int8)
        _exonerateTrans     = np.fromstring("Z  ZZZZ| ", dtype=np.int8)
        _cigarTrans         = np.fromstring("ZIDZZZZMM", dtype=np.int8)
        _gusfieldTrans      = np.fromstring("ZIDZZZZMR", dtype=np.int8)

        if   style == "exonerate+": return _exoneratePlusTrans [uc].tostring()
        elif style == "exonerate":  return _exonerateTrans     [uc].tostring()
        elif style == "cigar":      return _cigarTrans         [uc].tostring()
        else:                       return _gusfieldTrans      [uc].tostring()


    @requiresReference
    def reference(self, aligned=True, orientation="native"):
        if not (orientation == "native" or orientation == "genomic"):
            raise ValueError, "Bad `orientation` value"
        tSeq = self.bam.referenceFasta[self.referenceName].sequence[self.tStart:self.tEnd]
        shouldRC = orientation == "native" and self.isReverseStrand
        tSeqOriented = reverseComplement(tSeq) if shouldRC else tSeq
        if aligned:
            x = np.fromstring(tSeqOriented, dtype=np.int8)
            y = self._gapifyRef(x, orientation)
            return y.tostring()
        else:
            return tSeqOriented

    @requiresMapping
    def unrolledCigar(self, orientation="native"):
        """
        Run-length decode the CIGAR encoding, and orient.  Clipping ops are removed.
        """
        if self.isUnmapped: return None

        if self._unrolledCigar is None:
            self._unrolledCigar = _unrollCigar(self.peer.cigar, exciseSoftClips=True)
            if BAM_CMATCH in self._unrolledCigar:
                raise IncompatibleFile("CIGAR op 'M' illegal in PacBio BAM files")

        if (orientation == "native" and self.isReverseStrand):
            return self._unrolledCigar[::-1]
        else:
            return self._unrolledCigar

    @requiresMapping
    def referencePositions(self, aligned=True, orientation="native"):
        """
        Returns an array of reference positions.

        If aligned is True, the array has the same length as the
        alignment and referencePositions[i] = reference position of
        the i'th column in the oriented alignment.

        If aligned is False, the array has the same length as the read
        and referencePositions[i] = reference position of the i'th
        base in the oriented read.
        """
        assert (aligned in (True, False) and
                orientation in ("native", "genomic"))

        ucOriented = self.unrolledCigar(orientation)
        refNonGapMask = (ucOriented != BAM_CINS)

        if self.isReverseStrand and orientation == "native":
            pos = self.tEnd - 1 - np.hstack([0, np.cumsum(refNonGapMask[:-1])])
        else:
            pos = self.tStart + np.hstack([0, np.cumsum(refNonGapMask[:-1])])

        if aligned:
            return pos
        else:
            return pos[ucOriented != BAM_CDEL]

    def readPositions(self, aligned=True, orientation="native"):
        """
        Returns an array of read positions.

        If aligned is True, the array has the same length as the
        alignment and readPositions[i] = read position of the i'th
        column in the oriented alignment.

        If aligned is False, the array has the same length as the
        mapped reference segment and readPositions[i] = read position
        of the i'th base in the oriented reference segment.
        """
        assert (aligned in (True, False) and
                orientation in ("native", "genomic"))

        ucOriented = self.unrolledCigar(orientation)
        readNonGapMask = (ucOriented != BAM_CDEL)

        if self.isReverseStrand and orientation == "genomic":
            pos = self.aEnd - 1 - np.hstack([0, np.cumsum(readNonGapMask[:-1])])
        else:
            pos = self.aStart + np.hstack([0, np.cumsum(readNonGapMask[:-1])])

        if aligned:
            return pos
        else:
            return pos[ucOriented != BAM_CINS]


    def baseFeature(self, featureName, aligned=True, orientation="native"):
        """
        Retrieve the base feature as indicated.
        - `aligned`    : whether gaps should be inserted to reflect the alignment
        - `orientation`: "native" or "genomic"

        Note that this function assumes the the feature is stored in
        native orientation in the file, so it is not appropriate to
        use this method to fetch the read or the qual, which are
        oriented genomically in the file.
        """
        if not (orientation == "native" or orientation == "genomic"):
            raise ValueError, "Bad `orientation` value"
        if self.isUnmapped and (orientation != "native" or aligned == True):
            raise UnavailableFeature, \
                "Cannot get genome oriented/aligned features from unmapped BAM record"

        # 0. Get the "concrete" feature name.  (Example: Ipd could be
        # Ipd:Frames or Ipd:CodecV1)
        concreteFeatureName = self.bam._baseFeatureNameMappings[self.qId][featureName]

        # 1. Extract in native orientation
        tag, kind_, dtype_ = BASE_FEATURE_TAGS[concreteFeatureName]
        data_ = self.peer.opt(tag)

        if isinstance(data_, str):
            data = np.fromstring(data_, dtype=dtype_)
        else:
            # This is about 300x slower than the fromstring above.
            # Unless pysam exposes  buffer or numpy interface,
            # is is going to be very slow.
            data = np.fromiter(data_, dtype=dtype_)
        del data_
        assert len(data) == self.peer.rlen

        # 2. Decode
        if kind_ == "qv":
            data -= 33
        elif kind_ == "codecV1":
            data = codeToFrames(data)

        # 3. Clip
        # [s, e) delimits the range, within the query, that is in the aligned read.
        # This will be determined by the soft clips actually in the file as well as those
        # imposed by the clipping API here.
        if self.isCCS:
            s = self.aStart
            e = self.aEnd
        else:
            s = self.aStart - self.qStart
            e = self.aEnd   - self.qStart
        assert s >= 0 and e <= len(data)
        clipped = data[s:e]

        # 4. Orient
        shouldReverse = self.isReverseStrand and orientation == "genomic"
        if kind_ == "base":
            ungapped = reverseComplementAscii(clipped) if shouldReverse else clipped
        else:
            ungapped = clipped[::-1] if shouldReverse else clipped

        # 5. Gapify if requested
        if aligned == False:
            return ungapped
        else:
            return self._gapifyRead(ungapped, orientation)

    def _gapifyRead(self, data, orientation):
        return self._gapify(data, orientation, BAM_CDEL)

    def _gapifyRef(self, data, orientation):
        return self._gapify(data, orientation, BAM_CINS)

    def _gapify(self, data, orientation, gapOp):
        if self.isUnmapped: return data

        # Precondition: data must already be *in* the specified orientation
        if data.dtype == np.int8:
            gapCode = ord("-")
        else:
            gapCode = data.dtype.type(-1)
        uc = self.unrolledCigar(orientation=orientation)
        alnData = np.repeat(np.array(gapCode, dtype=data.dtype), len(uc))
        gapMask = (uc == gapOp)
        alnData[~gapMask] = data
        return alnData

    IPD            = _makeBaseFeatureAccessor("Ipd")
    PulseWidth     = _makeBaseFeatureAccessor("PulseWidth")
    #QualityValue   = _makeBaseFeatureAccessor("QualityValue")
    InsertionQV    = _makeBaseFeatureAccessor("InsertionQV")
    DeletionQV     = _makeBaseFeatureAccessor("DeletionQV")
    DeletionTag    = _makeBaseFeatureAccessor("DeletionTag")
    MergeQV        = _makeBaseFeatureAccessor("MergeQV")
    SubstitutionQV = _makeBaseFeatureAccessor("SubstitutionQV")

    def read(self, aligned=True, orientation="native"):
        if not (orientation == "native" or orientation == "genomic"):
            raise ValueError, "Bad `orientation` value"
        if self.isUnmapped and (orientation != "native" or aligned == True):
            raise UnavailableFeature, \
                "Cannot get genome oriented/aligned features from unmapped BAM record"
        data = np.fromstring(self.peer.seq, dtype=np.int8)
        if self.isCCS:
            s = self.aStart
            e = self.aEnd
        else:
            s = self.aStart - self.qStart
            e = self.aEnd   - self.qStart
        l = self.qLen
        # clip
        assert l == len(data) and s >= 0 and e <= l
        if self.isForwardStrand: clipped = data[s:e]
        else:                    clipped = data[(l-e):(l-s)]
        # orient
        shouldReverse = self.isReverseStrand and orientation == "native"
        ungapped = reverseComplementAscii(clipped) if shouldReverse else clipped
        # gapify
        if aligned: r = self._gapifyRead(ungapped, orientation)
        else:       r = ungapped
        return r.tostring()

    def __repr__(self):
        if self.isUnmapped:
            return "Unmapped BAM record: " + self.queryName
        else:
            return "BAM alignment: %s @ %s  %3d  %9d  %9d" \
            % (self.queryName, ("+" if self.isForwardStrand else "-"),
               self.referenceId, self.tStart, self.tEnd)

    def __str__(self):
        if self.bam.isReferenceLoaded:
            COLUMNS = 80
            val = ""
            val += repr(self) + "\n\n"
            val += "Read:        " + self.readName           + "\n"
            val += "Reference:   " + self.referenceName      + "\n\n"
            val += "Read length: " + str(self.readLength)    + "\n"
            val += "Identity:    " + "%0.3f" % self.identity + "\n"

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
        else:
            return repr(self)

    def __cmp__(self, other):
        return cmp((self.referenceId, self.tStart, self.tEnd),
                   (other.referenceId, other.tStart, other.tEnd))

    @requiresPbi
    def __getattr__(self, key):
        if key in self.bam.pbi.columnNames:
            return self.bam.pbi[self.rowNumber][key]
        else:
            raise AttributeError("no such column '%s' in pbi index" % key)

    def __dir__(self):
        basicDir = dir(self.__class__)
        if self.hasPbi:
            return basicDir + self.bam.pbi.columnNames
        else:
            return basicDir

class ClippedBamAlignment(BamAlignment):
    def __init__(self, aln, tStart, tEnd, aStart, aEnd, unrolledCigar):
        # Self-consistency checks
        assert aln.isMapped
        assert tStart <= tEnd
        assert aStart <= aEnd
        assert np.count_nonzero(unrolledCigar != BAM_CDEL) == (aEnd - aStart)

        # Assigment
        self.peer           = aln.peer
        self.bam            = aln.bam
        self.rowNumber      = aln.rowNumber
        self.tStart         = tStart
        self.tEnd           = tEnd
        self.aStart         = aStart
        self.aEnd           = aEnd
        self._unrolledCigar = unrolledCigar  # genomic orientation

    def unrolledCigar(self, orientation="native"):
        if orientation=="native" and self.isReverseStrand:
            return self._unrolledCigar[::-1]
        else:
            return self._unrolledCigar
