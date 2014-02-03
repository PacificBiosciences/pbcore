from numpy.testing import (assert_array_almost_equal as ARRAY_ALMOST_EQ,
                           assert_array_equal        as ARRAY_EQ)
from nose.tools import assert_equal as EQ
from nose import SkipTest

import numpy as np
import bisect
import h5py

from pbcore import data
from pbcore.io import CmpH5Reader
import pbcore.io.rangeQueries as RQ

class TestCmpH5Reader:

    def __init__(self):
        cmpH5Filename = data.getCmpH5()
        self._inCmpH5 = CmpH5Reader(cmpH5Filename)
        self.hit0 = self._inCmpH5[0]
        self.hit1 = self._inCmpH5[1]

    def test_openFromH5File(self):
        cmpH5Filename = data.getCmpH5()
        c = CmpH5Reader(h5py.File(cmpH5Filename, "r"))
        EQ("1.2.0.SF", c.version)

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

    def test_referencePositions(self):
        # Native orientation on a fwd strand read
        EQ([('G', 7466),
            ('A', 7467),
            ('A', 7468),
            ('G', 7469),
            ('-', 7470),
            ('C', 7470),
            ('T', 7471),
            ('-', 7472),
            ('G', 7472),
            ('C', 7473)],
           zip(self._inCmpH5[26].reference()[25:35],
               self._inCmpH5[26].referencePositions()[25:35]))

        # Genomic orientation on a fwd strand read
        EQ([('G', 7466),
            ('A', 7467),
            ('A', 7468),
            ('G', 7469),
            ('-', 7470),
            ('C', 7470),
            ('T', 7471),
            ('-', 7472),
            ('G', 7472),
            ('C', 7473)],
           zip(self._inCmpH5[26].reference(orientation="genomic")[25:35],
               self._inCmpH5[26].referencePositions(orientation="genomic")[25:35]))

        # Test native orientation on a rev. strand read
        EQ([('T', 8),
            ('C', 7),
            ('-', 6),
            ('G', 6),
            ('C', 5),
            ('C', 4),
            ('G', 3),
            ('C', 2),
            ('C', 1),
            ('C', 0)],
           zip(self._inCmpH5[0].reference()[-10:],
               self._inCmpH5[0].referencePositions()[-10:]))

        # Test genomic orientation on a rev. strand read
        EQ([('G', 0),
            ('G', 1),
            ('G', 2),
            ('C', 3),
            ('G', 4),
            ('G', 5),
            ('C', 6),
            ('-', 7),
            ('G', 7),
            ('A', 8)],
           zip(self._inCmpH5[0].reference(orientation="genomic")[:10],
               self._inCmpH5[0].referencePositions(orientation="genomic")[:10]))

    def test_readPositions(self):
        # Native orientation on a fwd strand read
        EQ([('A', 44),
            ('A', 45),
            ('C', 46),
            ('T', 47),
            ('G', 48),
            ('G', 49),
            ('T', 50),
            ('-', 51),
            ('-', 51),
            ('C', 51)],
           zip(self._inCmpH5[26].read()[:10],
               self._inCmpH5[26].readPositions()[:10]))

        # Genomic orientation on a fwd strand read
        EQ([('A', 44),
            ('A', 45),
            ('C', 46),
            ('T', 47),
            ('G', 48),
            ('G', 49),
            ('T', 50),
            ('-', 51),
            ('-', 51),
            ('C', 51)],
           zip(self._inCmpH5[26].read(orientation="genomic")[:10],
               self._inCmpH5[26].readPositions(orientation="genomic")[:10]))

        # Test native orientation on a rev. strand read
        EQ([('T', 295),
            ('C', 296),
            ('C', 297),
            ('G', 298),
            ('-', 299),
            ('C', 299),
            ('G', 300),
            ('C', 301),
            ('C', 302),
            ('C', 303)],
           zip(self.hit0.read()[-10:],
               self.hit0.readPositions()[-10:]))

        # Test genomic orientation on a rev. strand read
        EQ([('G', 303),
            ('G', 302),
            ('G', 301),
            ('C', 300),
            ('G', 299),
            ('-', 298),
            ('C', 298),
            ('G', 297),
            ('G', 296),
            ('A', 295)],
           zip(self.hit0.read(orientation="genomic")[:10],
               self.hit0.readPositions(orientation="genomic")[:10]))


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
             (18, '-', 'A'),
             (18, 'A', 'A'),
             (17, 'C', '-'),
             (16, 'C', 'C'),
             (15, 'C', 'C'),
             (14, 'G', 'G'),
             (13, 'C', 'C'),
             (12, '-', 'G'),
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
             (18, '-', 'A'),
             (18, 'A', 'A'),
             (17, 'C', '-'),
             (16, 'C', 'C'),
             (15, 'C', 'C'),
             (14, 'G', 'G'),
             (13, 'C', 'C'),
             (12, '-', 'G'),
             (12, 'G', 'G')]


    def test_reads_in_range_bounds(self):
        EQ(len(self._inCmpH5.readsInRange(1, 0, 1)), 2)
        EQ(all([ x.tStart == 0 for x in self._inCmpH5.readsInRange(1, 0, 1) ]), True)
        EQ(len(self._inCmpH5.readsInRange(1, 1000, 1051)), 0)
        EQ(len(self._inCmpH5.readsInRange(1, 1000, 1052)), 1)
        EQ(len(self._inCmpH5.readsInRange(1, 0, 1e20)), len(self._inCmpH5))

    def test_cigar(self):
        EQ("6M2D12M1I10M1D21M1I2M2I7M1I2M1I10M1I4M1I11M1D1I4M1I1M1I36M1I4M2I1M" +
           "1D2M1I9M1I15M1I9M1I4M9D9M1I2M1D16M1I20M1D4M1D8M3I12M1I2M2I7M1I4M1I" +
           "1M1D4M1I6M1I1M1D5M",
           self._inCmpH5[0].cigar())

        EQ("5M1D1M1I6M1I4M1D1M1I4M1I7M2I2M1I12M3I8M1D4M1D20M1I16M1D2M1I9M9D4M1" +
           "I9M1I15M1I9M1I2M1D1M2I4M1I36M1I1M1I4M1I1D11M1I4M1I10M1I2M1I7M2I2M1" +
           "I21M1D10M1I12M2D6M",
           self._inCmpH5[0].cigar(orientation="genomic"))
