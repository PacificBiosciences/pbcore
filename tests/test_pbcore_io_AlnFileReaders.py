from numpy.testing import (assert_array_almost_equal as ASIM,
                           assert_array_equal        as AEQ)
from nose.tools import nottest, assert_equal as EQ
from nose import SkipTest

import numpy as np
import bisect
import h5py

from pbcore import data
from pbcore.io import CmpH5Reader, BamReader
from pbcore.util.sequences import reverseComplement as RC

class _BasicAlnFileReaderTests(object):
    """
    Abstract base class for tests of the basic reader
    functionality---functionality not requiring the bam.pbi index.

    The tests are pretty tailored to the BAM/cmp.h5 files in
    pbcore.data.
    """
    READER_CONSTRUCTOR = None
    CONSTRUCTOR_ARGS   = None

    def __init__(self):
        self.f = self.READER_CONSTRUCTOR(*self.CONSTRUCTOR_ARGS)
        self.alns = list(self.f)
        self.fwdAln = self.alns[70]
        self.revAln = self.alns[71]

    def testBasicOperations(self):
        #EQ("1.3.1", self.f.version)
        EQ(False, self.f.isEmpty)
        EQ(True,  self.f.isSorted)
        EQ(115,   len(self.f))

    def testStrandOrientation(self):
        EQ(True,  self.fwdAln.isForwardStrand)
        EQ(False, self.fwdAln.isReverseStrand)
        EQ(False, self.revAln.isForwardStrand)
        EQ(True,  self.revAln.isReverseStrand)

    def testReadName(self):
        EQ("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/7957/9681_9734",
           self.fwdAln.readName)
        EQ("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/7957/9561_9619",
           self.revAln.readName)

    def testAlignedRead(self):
        expectedFwdNative = "TACGGTCATCATCTGACACTACAGACTCTGGCATCGCTGTGAAGAC-ACGCGAA"
        EQ(expectedFwdNative, self.fwdAln.read(aligned=True))
        EQ(expectedFwdNative, self.fwdAln.read())
        EQ(expectedFwdNative, self.fwdAln.read(orientation="genomic"))
        expectedRevNative = "CTTGTGAAAATGCTGAATTCT-GCGTCG-CTTCACCAGCGATGCCA-AGTCTGTAGTGTCA"
        EQ(expectedRevNative, self.revAln.read(aligned=True))
        EQ(expectedRevNative, self.revAln.read())
        EQ(RC(expectedRevNative), self.revAln.read(orientation="genomic"))

    def testUnalignedRead(self):
        expectedFwdNative = "TACGGTCATCATCTGACACTACAGACTCTGGCATCGCTGTGAAGACACGCGAA"
        EQ(expectedFwdNative, self.fwdAln.read(aligned=False))
        EQ(expectedFwdNative, self.fwdAln.read(aligned=False, orientation="genomic"))
        expectedRevNative = "CTTGTGAAAATGCTGAATTCTGCGTCGCTTCACCAGCGATGCCAAGTCTGTAGTGTCA"
        EQ(expectedRevNative, self.revAln.read(aligned=False))
        EQ(RC(expectedRevNative), self.revAln.read(aligned=False, orientation="genomic"))

    def testAlignedReference(self):
        expectedFwdNative = "TACGGTCATCATCTGACACTACAGACTCTGGCATCGCTGTGAAGACGACGCGAA"
        EQ(expectedFwdNative, self.fwdAln.reference(aligned=True))
        EQ(expectedFwdNative, self.fwdAln.reference())
        EQ(expectedFwdNative, self.fwdAln.reference(orientation="genomic"))
        expectedRevNative = "CTTGTGAAAATGCTGAATT-TCGCGTCGTCTTCA-CAGCGATGCCAGAGTCTGTAGTGTCA"
        EQ(expectedRevNative, self.revAln.reference(aligned=True))
        EQ(expectedRevNative, self.revAln.reference())
        EQ(RC(expectedRevNative), self.revAln.reference(orientation="genomic"))

    def testUnalignedReference(self):
        expectedFwdNative = "TACGGTCATCATCTGACACTACAGACTCTGGCATCGCTGTGAAGACGACGCGAA"
        EQ(expectedFwdNative, self.fwdAln.reference(aligned=False))
        EQ(expectedFwdNative, self.fwdAln.reference(aligned=False, orientation="genomic"))
        expectedRevNative = "CTTGTGAAAATGCTGAATTTCGCGTCGTCTTCACAGCGATGCCAGAGTCTGTAGTGTCA"
        EQ(expectedRevNative, self.revAln.reference(aligned=False))
        EQ(RC(expectedRevNative), self.revAln.reference(aligned=False, orientation="genomic"))

    def testDeletionQV(self):
        expectedFwdNative = [ 17,  17,   7,  17,  17,   6,  17,  17,  17,  17,  17,  17,  17,
                              17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,
                              17,  17,  17,  17,  17,  17,   7,  17,  17,  17,  17,  17,  17,
                              17,  17,  17,  17,  17,  17,  17, 255,  17,  17,  17,  17,  17,
                              17,  17 ]
        AEQ(expectedFwdNative, self.fwdAln.DeletionQV(aligned=True))
        AEQ(expectedFwdNative, self.fwdAln.DeletionQV())
        AEQ(expectedFwdNative, self.fwdAln.DeletionQV(orientation="genomic"))

        expectedRevNative = [ 17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,
                              17,  17,  17,  17,  17,  17,  17,  17, 255,   7,  17,  17,  17,
                              17,  17, 255,   6,  17,  17,  17,  17,  17,  17,  17,  17,  17,
                              17,  17,  17,  17,  17,  17,  17, 255,  17,  17,  17,  17,  17,
                              17,  17,  17,  17,  17,  17,  17,  17,  17 ]
        AEQ(expectedRevNative, self.revAln.DeletionQV(aligned=True))
        AEQ(expectedRevNative, self.revAln.DeletionQV())
        AEQ(expectedRevNative[::-1], self.revAln.DeletionQV(orientation="genomic"))


    def testDeletionTag(self):
        expectedFwdNative = [78, 78, 84, 78, 78, 67, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78,
                             78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 65, 78,
                             78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 45, 78, 78, 78, 78,
                             78, 78, 78]
        AEQ(expectedFwdNative, self.fwdAln.DeletionTag(aligned=True))
        AEQ(expectedFwdNative, self.fwdAln.DeletionTag())
        AEQ(expectedFwdNative, self.fwdAln.DeletionTag(orientation="genomic"))

        expectedRevNative = [78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78,
                             78, 78, 78, 78, 45, 67, 78, 78, 78, 78, 78, 45, 84, 78, 78, 78, 78,
                             78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 45, 78, 78, 78, 78,
                             78, 78, 78, 78, 78, 78, 78, 78, 78, 78]
        AEQ(expectedRevNative, self.revAln.DeletionTag(aligned=True))
        AEQ(expectedRevNative, self.revAln.DeletionTag())

        # TODO: what is the correct behavior here?
        #AEQ(expectedRevNative[::-1], self.revAln.DeletionTag(orientation="genomic"))

    def testReferencePositions(self):
        expectedFwdNative = [29751, 29752, 29753, 29754, 29755, 29756, 29757, 29758, 29759,
                             29760, 29761, 29762, 29763, 29764, 29765, 29766, 29767, 29768,
                             29769, 29770, 29771, 29772, 29773, 29774, 29775, 29776, 29777,
                             29778, 29779, 29780, 29781, 29782, 29783, 29784, 29785, 29786,
                             29787, 29788, 29789, 29790, 29791, 29792, 29793, 29794, 29795,
                             29796, 29797, 29798, 29799, 29800, 29801, 29802, 29803, 29804]
        AEQ(expectedFwdNative, self.fwdAln.referencePositions())
        AEQ(expectedFwdNative, self.fwdAln.referencePositions(orientation="genomic"))
        # test for native orientation...

        expectedRevNative = [29822, 29821, 29820, 29819, 29818, 29817, 29816, 29815, 29814,
                             29813, 29812, 29811, 29810, 29809, 29808, 29807, 29806, 29805,
                             29804, 29803, 29803, 29802, 29801, 29800, 29799, 29798, 29797,
                             29796, 29795, 29794, 29793, 29792, 29791, 29790, 29789, 29789,
                             29788, 29787, 29786, 29785, 29784, 29783, 29782, 29781, 29780,
                             29779, 29778, 29777, 29776, 29775, 29774, 29773, 29772, 29771,
                             29770, 29769, 29768, 29767, 29766, 29765, 29764]
        AEQ(expectedRevNative, self.revAln.referencePositions())
        # this is not true...
        #AEQ(expectedRevNative[::-1], self.revAln.referencePositions(orientation="genomic"))

    # def testReadPositions(self):
    #     EQ("" , self.fwdAln.readName)
    #     EQ("" , self.revAln.readName)

    # def testClippedAlignments(self):
    #     EQ("" , self.fwdAln.readName)
    #     EQ("" , self.revAln.readName)

    # def testClippedAlignmentExhaustive(self):
    #     EQ("" , self.fwdAln.readName)
    #     EQ("" , self.revAln.readName)


    # def testReadsInRange(self):
    #     EQ("" , self.fwdAln.readName)
    #     EQ("" , self.revAln.readName)


    # def testReadsInRangeExhaustive(self):
    #     EQ("" , self.fwdAln.readName)
    #     EQ("" , self.revAln.readName)


    # #
    # # move out:
    # #
    # def testFeatureManifest(self):
    #     EQ("" , self.fwdAln.readName)
    #     EQ("" , self.revAln.readName)


class _IndexedAlnFileReaderTests(_BasicAlnFileReaderTests):
    """
    Abstract base class for tests of the reader functionality
    requiring the bam.pbi index
    """
    pass

class TestCmpH5(_IndexedAlnFileReaderTests):
    READER_CONSTRUCTOR = CmpH5Reader
    CONSTRUCTOR_ARGS   = (data.getBamAndCmpH5()[1],)


class TestBasicBam(_BasicAlnFileReaderTests):
     READER_CONSTRUCTOR = BamReader
     CONSTRUCTOR_ARGS   = (data.getBamAndCmpH5()[0], data.getLambdaFasta())

# class TestIndexedBam(_BasicAlnFileReaderTests):
#     READER_CONSTRUCTOR = IndexedBamReader
#     ALN_FILE           = data.getBamAndCmpH5()[0]
