from numpy.testing import assert_array_equal as ARRAY_EQ
from nose.tools import assert_equal as EQ, assert_raises
import numpy as np

from pbcore import data
from pbcore.io import CmpH5Reader, BasH5Reader

class TestBasH5Reader:

    def __init__(self):
        self.cmpH5 = CmpH5Reader(data.getCmpH5()["cmph5"])
        basFiles = data.getCmpH5()["bash5s"]
        self.bas1, self.bas2 = map(BasH5Reader, basFiles)

    def test_BasH5Reader_basicTest(self):
        EQ("m110818_075520_42141_c100129202555500000315043109121112_s1_p0",
           self.bas1.movieName)
        ARRAY_EQ([7, 8, 9, 1000, 1006, 1007, 2001,
                  2003, 2007, 2008, 3004, 3006, 3008,
                  4004, 4005, 4006, 4007, 4009],
                 self.bas1.sequencingZmws)
        for zmw in self.bas1:
            assert len(zmw.subreads()) > 0

    def test_BasH5Reader_basecallsVsCmpH5(self):
        aln = self.cmpH5[2]

        EQ("m110818_075520_42141_c100129202555500000315043109121112_s1_p0/2001/3580_3922",
           aln.readName)

        zmwRead = self.bas1[2001].read(3580, 3922)
        EQ("m110818_075520_42141_c100129202555500000315043109121112_s1_p0/2001/3580_3922",
           zmwRead.readName)

        EQ(aln.read(aligned=False), zmwRead.basecalls())
        ARRAY_EQ(aln.InsertionQV(aligned=False),
                 zmwRead.InsertionQV())
        ARRAY_EQ(aln.DeletionQV(aligned=False),
                 zmwRead.DeletionQV())
        ARRAY_EQ(aln.QualityValue(aligned=False),
                 zmwRead.QualityValue())

    def test_BasH5Reader_regionTableAccessors(self):
        # Test the region table accessors
        ARRAY_EQ((334,), self.bas1.regionTable.shape)

        zmw = self.bas1[7]
        ARRAY_EQ(
            np.array([[   7,    1,    0,  299,   -1],
                      [   7,    1,  343,  991,   -1],
                      [   7,    1, 1032, 1840,   -1],
                      [   7,    0,  299,  343,  681],
                      [   7,    0,  991, 1032,  804],
                      [   7,    2,    0, 1578,    0]], dtype=np.int32),
            zmw.regionTable.view(dtype=(np.int32, 5)))

        EQ((0, 1578),
           zmw.hqRegion())
        EQ([(299, 343), (991, 1032)],
           zmw.adapterRegions())
        EQ([(0, 299), (343, 991), (1032, 1578)],
           zmw.insertRegions())

    def test_BasH5Reader_invalidRangeUsage(self):
        # Make sure that attempts to access an invalid data range from
        # a ZMW (i.e., outside the HQ region) throw an exception.

        zmw = self.bas1[8]
        EQ((3381, 5495), zmw.hqRegion())

        # This is OK.
        zmw.read(4000, 5000)

        # These raise an exception.
        with assert_raises(IndexError):
            zmw.read(0, 10)
        with assert_raises(IndexError):
            zmw.read(5400, 5500)
        with assert_raises(IndexError):
            zmw.read(5000, 4000)

    def test_BasH5Reader_ccs(self):
        EQ(self.bas1[4006].ccsRead().basecalls(),
           ''.join(['GGCGCACGGAGGAGCAAGCGTGACAGTCCCACGTCATGCCCGCCGACG',
                    'ATATCGAGCTCGCGCTCACCGCCAGGGTGTGAAGTGAATTCACGGTGC',
                    'CGCCGAAAGCTGGGCCGGCTTTCGTTCCTTCGCCGGTCAGGAGAAGGC',
                    'GGACCCCGTCGTGGGCCATTCCGAGCCTGGAGACAGCGGTCGAAAAAG',
                    'CCTTCGCCAAGCCGGTGGCCAAATGGTCGGCCAGCGAGAATCCGTGC']))
    
        
        
