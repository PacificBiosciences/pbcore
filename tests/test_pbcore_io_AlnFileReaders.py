from numpy.testing import (assert_array_almost_equal as ASIM,
                           assert_array_equal        as AEQ)
from nose.tools import (nottest,
                        assert_raises,
                        assert_equal as EQ)
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
    BAX_FILE           = data.getBaxForBam()

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

    def testClippedAlignments(self):
        # Get a more interesting (more gappy) fwd strand aln
        a = self.alns[2]
        EQ([(980, 'C', 'C'),
            (981, 'C', 'C'),
            (982, 'T', 'T'),
            (983, 'A', '-'),
            (984, 'C', 'C'),
            (985, '-', 'G'),
            (985, 'T', 'T'),
            (986, 'T', 'T') ],
           zip(a.referencePositions(), a.reference(), a.read())[308:316])

        ac1 = a.clippedTo(983, 985)
        EQ(983, ac1.referenceStart)
        EQ(985, ac1.referenceEnd)
        EQ([(983, 'A', '-'),
            (984, 'C', 'C')],
           zip(ac1.referencePositions(), ac1.reference(), ac1.read()))

        ac2 = a.clippedTo(982, 986)
        EQ(982, ac2.referenceStart)
        EQ(986, ac2.referenceEnd)
        EQ([(982, 'T', 'T'),
            (983, 'A', '-'),
            (984, 'C', 'C'),
            (985, '-', 'G'),
            (985, 'T', 'T')],
           zip(ac2.referencePositions(), ac2.reference(), ac2.read()))

        ac3 = a.clippedTo(984, 985)
        EQ(984, ac3.referenceStart)
        EQ(985, ac3.referenceEnd)
        EQ([(984, 'C', 'C')],
           zip(ac3.referencePositions(), ac3.reference(), ac3.read()))

        # Get a more interesting (more gappy) rev strand aln
        b = self.alns[4]
        EQ([(2216, 'G', 'G'),
            (2215, 'G', 'G'),
            (2214, '-', 'C'),
            (2214, 'C', 'C'),
            (2213, 'A', 'A'),
            (2212, 'T', 'T'),
            (2211, 'G', 'G'),
            (2210, 'C', 'C'),
            (2209, 'T', 'T'),
            (2208, 'G', '-'),
            (2207, 'G', 'G'),
            (2206, 'C', 'C')],
           zip(b.referencePositions(), b.reference(), b.read())[188:200])

        bc1 = b.clippedTo(2208, 2214)
        EQ([(2213, 'A', 'A'),
            (2212, 'T', 'T'),
            (2211, 'G', 'G'),
            (2210, 'C', 'C'),
            (2209, 'T', 'T'),
            (2208, 'G', '-')],
           zip(bc1.referencePositions(), bc1.reference(), bc1.read()))

        bc2 = b.clippedTo(2207, 2215)
        EQ([(2214, 'C', 'C'),
            (2213, 'A', 'A'),
            (2212, 'T', 'T'),
            (2211, 'G', 'G'),
            (2210, 'C', 'C'),
            (2209, 'T', 'T'),
            (2208, 'G', '-'),
            (2207, 'G', 'G')],
           zip(bc2.referencePositions(), bc2.reference(), bc2.read()))

        bc3 = b.clippedTo(2209, 2214)
        EQ([(2213, 'A', 'A'),
            (2212, 'T', 'T'),
            (2211, 'G', 'G'),
            (2210, 'C', 'C'),
            (2209, 'T', 'T')],
           zip(bc3.referencePositions(), bc3.reference(), bc3.read()))


        # Test clipping in a large deletion
        d = self.alns[52]
        EQ([(16191, 'C', 'C'),
            (16192, 'A', 'A'),
            (16193, 'G', 'G'),
            (16194, 'C', 'C'),
            (16195, 'A', 'A'),
            (16196, 'G', '-'),
            (16197, 'G', '-'),
            (16198, 'T', '-'),
            (16199, 'G', 'G'),
            (16200, 'A', 'A'),
            (16201, 'G', 'G')],
           zip(d.referencePositions(), d.reference(), d.read())[130:141])
        dc1 = d.clippedTo(16196, 16198)


    def testBaxAttaching(self):
        # Before attaching, should get sane exceptions
        with assert_raises(ValueError):
           self.fwdAln.zmw

        with assert_raises(ValueError):
           self.fwdAln.zmwRead

        # Now attach
        self.f.attach(self.BAX_FILE)
        EQ('m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/7957/9681_9734',
           self.fwdAln.readName)
        EQ('m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/7957'
           , self.fwdAln.zmwName)
        EQ('<Zmw: m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/7957>',
           repr(self.fwdAln.zmw))
        EQ('<ZmwRead: m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/7957/9681_9734>',
           repr(self.fwdAln.zmwRead))

        # Check read contents, for every aln.
        for aln in self.alns:
            EQ(aln.read(aligned=False, orientation="native"), aln.zmwRead.basecalls())


    def testClippingsVsBaxData(self):
        self.f.attach(self.BAX_FILE)


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
