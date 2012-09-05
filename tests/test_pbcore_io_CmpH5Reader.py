from numpy.testing import assert_array_almost_equal as ARRAY_ALMOST_EQ
from nose.tools import assert_equal as EQ
from nose import SkipTest

import numpy as np
import bisect

from pbcore import data
from pbcore.io import CmpH5Reader
import pbcore.io.rangeQueries as RQ

class TestCmpH5Reader:

    def __init__(self):
        cmpH5Filename = data.getCmpH5()["cmph5"]
        self._inCmpH5 = CmpH5Reader(cmpH5Filename)
        self.hit0 = self._inCmpH5[0]
        self.hit1 = self._inCmpH5[1]

    def test_basicCmpH5Operations(self):
        assert self._inCmpH5.version == "1.2.0.SF"
        assert not self._inCmpH5.isEmpty
        assert self._inCmpH5.isSorted
        EQ(84, len(self._inCmpH5))
        
    def test_strandOrientation(self):
        # Row 0 was a reverse-strand read;
        # row 1 was forward-strand.
        assert self.hit0.isReverseStrand
        assert not self.hit0.isForwardStrand
        assert self.hit1.isForwardStrand
        assert not self.hit1.isReverseStrand
        
    def test_read(self):
        EQ("GGGCG-CGGACCTCCGCGG-",
           self.hit0.read(orientation="genomic")[:20])
        EQ("GGGCGGCGAC-TCAGCCGGC",
           self.hit1.read(orientation="genomic")[:20])

    def test_read_unaligned(self):
        EQ("GGGCGCGGACCTCCGCGGTT",
           self.hit0.read(orientation="genomic", aligned=False)[:20])
        EQ("GGGCGGCGACTCAGCCGGCG",
           self.hit1.read(orientation="genomic", aligned=False)[:20])        
        
    def test_reference(self):
        EQ("GGGCGGC-GACCTC-GCGGG",
           self.hit0.reference(orientation="genomic")[:20])
        EQ("GGGCGGCGACCTC-G-CGG-",
           self.hit1.reference(orientation="genomic")[:20])
        
    def test_reference_unaligned(self):
        EQ("GGGCGGCGACCTCGCGGGTT",
           self.hit0.reference(orientation="genomic", aligned=False)[:20])
        EQ("GGGCGGCGACCTCGCGGGTT",
           self.hit1.reference(orientation="genomic", aligned=False)[:20])
        
    def test_ipd(self):
        ARRAY_ALMOST_EQ([ 0.1466663 ,  0.06666651,  0.0933331 ,  0.0133333 ,
                          0.49333212,      np.nan,  0.0133333 ,  0.0799998],
                        self.hit0.IPD(orientation="genomic")[:8])

        ARRAY_ALMOST_EQ([ 0.06666651,  0.38666573,  0.10666641,  1.37333   ,
                          1.57332945,  4.46665573,  0.47999883,  0.18666621],
                        self.hit1.IPD(orientation="genomic")[:8])

    def test_ipd_unaligned(self):
        ARRAY_ALMOST_EQ([ 0.1466663 ,  0.06666651,  0.0933331 ,  0.0133333 ,
                          0.49333212,  0.0133333 ,  0.0799998 ,  0.11999971],
                        self.hit0.IPD(orientation="genomic", aligned=False)[:8])

        ARRAY_ALMOST_EQ([ 0.06666651,  0.38666573,  0.10666641,  1.37333   ,
                          1.57332945,  4.46665573,  0.47999883,  0.18666621],
                        self.hit1.IPD(orientation="genomic", aligned=False)[:8])

    def test_alignedTargetPositions(self):
        ARRAY_ALMOST_EQ(self.hit0.referencePositions(orientation="genomic")[:20],
                        [ 0,  1,  2,  3,  4,  5,  6,  7,  7,  8,
                          9, 10, 11, 12, 13, 13, 14, 15, 16, 17])

    def test_clipped_alignment(self):
        # Forward strand
        a = self.hit1
        assert zip(a.referencePositions(), a.reference(), a.read())[34:45] == \
            [(29, 'T', 'T'),
             (30, '-', 'A'),
             (30, 'A', 'A'),
             (31, 'T', 'T'),
             (32, 'G', 'G'),
             (33, 'A', 'A'),
             (34, 'A', 'A'),
             (35, '-', 'C'),
             (35, 'A', 'A'),
             (36, 'A', 'A'),
             (37, 'T', 'T')]
        ac1 = a.clippedTo(30, 35)
        EQ(30, ac1.referenceStart)
        EQ(35, ac1.referenceEnd)
        assert zip(ac1.referencePositions(), ac1.reference(), ac1.read()) == \
            [(30, 'A', 'A'),
             (31, 'T', 'T'),
             (32, 'G', 'G'),
             (33, 'A', 'A'),
             (34, 'A', 'A')]
        ac2 = a.clippedTo(29, 36)
        EQ(29, ac2.referenceStart)
        EQ(36, ac2.referenceEnd)
        assert zip(ac2.referencePositions(), ac2.reference(), ac2.read()) == \
            [(29, 'T', 'T'),
             (30, '-', 'A'),
             (30, 'A', 'A'),
             (31, 'T', 'T'),
             (32, 'G', 'G'),
             (33, 'A', 'A'),
             (34, 'A', 'A'),
             (35, '-', 'C'),
             (35, 'A', 'A')]

        # Reverse strand
        a = self.hit0
        assert zip(a.referencePositions(), a.reference(), a.read())[296:307] == \
            [(20, 'A', 'A'),
             (19, 'A', 'A'),
             (19, '-', 'A'),
             (18, 'A', 'A'),
             (17, 'C', '-'),
             (16, 'C', 'C'),
             (15, 'C', 'C'),
             (14, 'G', 'G'),
             (13, 'C', 'C'),
             (13, '-', 'G'),
             (12, 'G', 'G')]
        ac1 = a.clippedTo(13, 19)
        assert zip(ac1.referencePositions(), ac1.reference(), ac1.read()) == \
            [(18, 'A', 'A'),
             (17, 'C', '-'),
             (16, 'C', 'C'),
             (15, 'C', 'C'),
             (14, 'G', 'G'),
             (13, 'C', 'C')]
        ac2 = a.clippedTo(12, 20)
        assert zip(ac2.referencePositions(), ac2.reference(), ac2.read()) == \
            [(19, 'A', 'A'),
             (19, '-', 'A'),
             (18, 'A', 'A'),
             (17, 'C', '-'),
             (16, 'C', 'C'),
             (15, 'C', 'C'),
             (14, 'G', 'G'),
             (13, 'C', 'C'),
             (13, '-', 'G'),
             (12, 'G', 'G')]

    
    def test_reads_in_range_bounds(self):
        ## XXX : At the moment the rangeStart, rangeEnd are
        ## inclusive. This is not-pythonic and should be changed.
        EQ(len(self._inCmpH5.readsInRange(1, 0, 0)), 2)
        EQ(all([ x.tStart == 0 for x in self._inCmpH5.readsInRange(1, 0, 0) ]), True)
        EQ(len(self._inCmpH5.readsInRange(1, 1000, 1050)), 0)
        EQ(len(self._inCmpH5.readsInRange(1, 1000, 1051)), 1)
        EQ(len(self._inCmpH5.readsInRange(1, 0, 1e20)), len(self._inCmpH5))
        
        blockSize = np.random.randint(10, 500)
        for j in range(0, self._inCmpH5.referenceInfo(1).Length, blockSize):
            start = j 
            end   = j + blockSize
            oor   = [ read.tStart > end or read.tEnd < start for read in self._inCmpH5.readsInRange(1, start, end) ]
            assert(not any(oor))
        
        
