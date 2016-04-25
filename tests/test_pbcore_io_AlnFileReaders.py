from numpy.testing import (assert_array_almost_equal as ASIM,
                           assert_array_equal        as AEQ)
from nose.tools import (nottest,
                        assert_raises,
                        assert_equal as EQ,
                        assert_almost_equal as EQISH)
from nose import SkipTest

import tempfile
import shutil
import pysam
import numpy as np
import bisect
import h5py
from collections import Counter

from pbcore import data
from pbcore.io import CmpH5Reader, BamReader, IndexedBamReader
from pbcore.io.align._BamSupport import UnavailableFeature
from pbcore.sequence import reverseComplement as RC
from pbcore.chemistry import ChemistryLookupError


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
        self.fwdAln = self.alns[1]
        self.revAln = self.alns[105]

    def testBasicOperations(self):
        EQ(False, self.f.isEmpty)
        EQ(True,  self.f.isSorted)
        EQ(112,   len(self.f))

    def testStrandOrientation(self):
        EQ(True,  self.fwdAln.isForwardStrand)
        EQ(False, self.fwdAln.isReverseStrand)
        EQ(False, self.revAln.isForwardStrand)
        EQ(True,  self.revAln.isReverseStrand)

    def testReadName(self):
        EQ("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/32328/1_344",
           self.fwdAln.readName)
        EQ("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/51534/1_200",
           self.revAln.readName)

    def testAlignedRead(self):
        expectedFwdNative = "GCCGCGAT-GATGAAAACTGATACCGGGGTTGCTGAGTGAATATATCGAACAGTCAGGTT-ACAGGCTGCGGCATTTTGTCCGCGCC-GGCTTCGCTCACTGTTCAGGCCGGAG-CACAGACCGCCGTTGAAATGGGCGGATGCTAATTACTATCTCCCGAAAGAAT-CGC-TACCAGGAAGGGCGATGGGAAACACTGCCCTTTCAGCGGG-CATCATGAATGCGATGGGCAGCGACTACATCCGTGAGGT-AATGTGGTGAAGTCTG-CCGTGTCGGTTATTCCAAAATGCTGCTGGGTG-TTATGCCT-CGTTTATAGAGCATAAGCAGCGCAACA-CCTTATCTGGTTGCC"
        EQ(expectedFwdNative, self.fwdAln.read(aligned=True))
        EQ(expectedFwdNative, self.fwdAln.read())
        EQ(expectedFwdNative, self.fwdAln.read(orientation="genomic"))
        expectedRevNative = "TAGCCACCGGATATCACCACAGGTGAGGCCGTGTAAGTTG-AGGTTTTTCTACGTCAGATTCTTTTGGGATTGGGCTTGGGTTTATTTCCTGGTGCGTTTCGTT-GAAGGTATTTGCAGTTTTCGCAGATTATGCCTCCGGTGATACTTCGTCGCTGTCTCGCCACACGTCCTCCTTTTCCTGCGGTAGTGGTAACACCCC"
        EQ(expectedRevNative, self.revAln.read(aligned=True))
        EQ(expectedRevNative, self.revAln.read())
        EQ(RC(expectedRevNative), self.revAln.read(orientation="genomic"))

    def testUnalignedRead(self):
        expectedFwdNative = 'GCCGCGATGATGAAAACTGATACCGGGGTTGCTGAGTGAATATATCGAACAGTCAGGTTACAGGCTGCGGCATTTTGTCCGCGCCGGCTTCGCTCACTGTTCAGGCCGGAGCACAGACCGCCGTTGAAATGGGCGGATGCTAATTACTATCTCCCGAAAGAATCGCTACCAGGAAGGGCGATGGGAAACACTGCCCTTTCAGCGGGCATCATGAATGCGATGGGCAGCGACTACATCCGTGAGGTAATGTGGTGAAGTCTGCCGTGTCGGTTATTCCAAAATGCTGCTGGGTGTTATGCCTCGTTTATAGAGCATAAGCAGCGCAACACCTTATCTGGTTGCC'
        EQ(expectedFwdNative, self.fwdAln.read(aligned=False))
        EQ(expectedFwdNative, self.fwdAln.read(aligned=False, orientation="genomic"))
        expectedRevNative = "TAGCCACCGGATATCACCACAGGTGAGGCCGTGTAAGTTGAGGTTTTTCTACGTCAGATTCTTTTGGGATTGGGCTTGGGTTTATTTCCTGGTGCGTTTCGTTGAAGGTATTTGCAGTTTTCGCAGATTATGCCTCCGGTGATACTTCGTCGCTGTCTCGCCACACGTCCTCCTTTTCCTGCGGTAGTGGTAACACCCC"
        EQ(expectedRevNative, self.revAln.read(aligned=False))
        EQ(RC(expectedRevNative), self.revAln.read(aligned=False, orientation="genomic"))

    def testAlignedReference(self):
        expectedFwdNative = 'GCCGCGCTGGATG--AACTGATACCGGGGTTGCTGAGTGAATATATCGAACAGTCAGGTTAACAGGCTGCGGCATTTTGTCCGCGCCGGGCTTCGCTCACTGTTCAGGCCGGAGCCACAGACCGCCGTTG-AATGGGCGGATGCTAATTACTATCTCCCGAAAGAATCCGCATACCAGGAAGGGCGCTGGGAAACACTGCCCTTTCAGCGGGCCATCATGAATGCGATGGGCAGCGACTACATCCGTGAGGTGAATGTGGTGAAGTCTGCCCGTGTCGGTTATTCCAAAATGCTGCTGGGTGTTTATGCCTAC-TTTATAGAGCATAAGCAGCGCAACACCCTTATCTGGTTGCC'
        EQ(expectedFwdNative, self.fwdAln.reference(aligned=True))
        EQ(expectedFwdNative, self.fwdAln.reference())
        EQ(expectedFwdNative, self.fwdAln.reference(orientation="genomic"))
        expectedRevNative = 'TAGCCACCGGATATC-CCACAGGTGA-GCCGTGT-AGTTGAAGG-TTTT-TACGTCAGATTCTTTTGGGATT-GGCTTGGGTTTATTT-CTGGTGCGTTTCGTTGGAAGGTATTTGCAGTTTTCGCAGATTATG--T-CGGTGATACTTCGTCGCTGTCTCGCCACACGTCCTCCTTTTCCTGCGGTAGTGGTAACACCCC'
        EQ(expectedRevNative, self.revAln.reference(aligned=True))
        EQ(expectedRevNative, self.revAln.reference())
        EQ(RC(expectedRevNative), self.revAln.reference(orientation="genomic"))

    def testUnalignedReference(self):
        expectedFwdNative = "GCCGCGCTGGATGAACTGATACCGGGGTTGCTGAGTGAATATATCGAACAGTCAGGTTAACAGGCTGCGGCATTTTGTCCGCGCCGGGCTTCGCTCACTGTTCAGGCCGGAGCCACAGACCGCCGTTGAATGGGCGGATGCTAATTACTATCTCCCGAAAGAATCCGCATACCAGGAAGGGCGCTGGGAAACACTGCCCTTTCAGCGGGCCATCATGAATGCGATGGGCAGCGACTACATCCGTGAGGTGAATGTGGTGAAGTCTGCCCGTGTCGGTTATTCCAAAATGCTGCTGGGTGTTTATGCCTACTTTATAGAGCATAAGCAGCGCAACACCCTTATCTGGTTGCC"
        EQ(expectedFwdNative, self.fwdAln.reference(aligned=False))
        EQ(expectedFwdNative, self.fwdAln.reference(aligned=False, orientation="genomic"))
        expectedRevNative = "TAGCCACCGGATATCCCACAGGTGAGCCGTGTAGTTGAAGGTTTTTACGTCAGATTCTTTTGGGATTGGCTTGGGTTTATTTCTGGTGCGTTTCGTTGGAAGGTATTTGCAGTTTTCGCAGATTATGTCGGTGATACTTCGTCGCTGTCTCGCCACACGTCCTCCTTTTCCTGCGGTAGTGGTAACACCCC"
        EQ(expectedRevNative, self.revAln.reference(aligned=False))
        EQ(RC(expectedRevNative), self.revAln.reference(aligned=False, orientation="genomic"))

    def testDeletionQV(self):
        expectedFwdNative = (
            [ 17, 17, 17, 17, 17, 17, 17, 17,255,  4, 17, 17, 17,  8, 17, 17, 17, 17,
              17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
              17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 10,  8, 17,
              17, 17, 17, 17, 17, 17,255, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
              17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,255, 17, 17,
              17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
              17, 17, 17, 17, 17, 17,255, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
              17, 17, 17, 17, 17,  6, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
              17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 11, 17, 17, 17, 17,
              17, 17, 17, 17, 17,255, 17, 17, 17,255, 17, 17, 17, 17, 17, 17, 17, 17,
              17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
              17, 11, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,255, 17, 17, 17,
              17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
              17, 17, 17, 17,  7, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
              255,  8, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,255,
              17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
              17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,255, 17, 17, 17,
              17, 17, 17, 17, 17,255, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
              17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,255, 17, 17,
              17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17] )

        AEQ(expectedFwdNative, self.fwdAln.DeletionQV(aligned=True))
        AEQ(expectedFwdNative, self.fwdAln.DeletionQV())
        AEQ(expectedFwdNative, self.fwdAln.DeletionQV(orientation="genomic"))

        expectedRevNative = (
            [ 17, 17, 17, 17, 6, 17, 17, 17, 17, 17, 17, 17, 17, 17,
            17, 17, 17, 17, 17, 6, 17, 17, 17, 17, 17, 17, 6, 17, 17,
            17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 255, 10, 17,
            17, 17, 17, 17, 8, 9, 17, 17, 17, 17, 17, 17, 17, 17, 17,
            17, 17, 17, 17, 17, 10, 17, 17, 17, 17, 17, 17, 17, 17,
            17, 17, 17, 17, 17, 17, 17, 17, 8, 17, 17, 17, 17, 17, 17,
            17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
            17, 7, 17, 255, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
            17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
            17, 17, 9, 17, 17, 5, 17, 17, 17, 17, 17, 17, 17, 17, 17,
            17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
            17, 17, 17, 7, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
            17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
            17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17 ] )

        print self.revAln.DeletionQV(aligned=True)
        AEQ(expectedRevNative, self.revAln.DeletionQV(aligned=True))
        AEQ(expectedRevNative, self.revAln.DeletionQV())
        AEQ(expectedRevNative[::-1], self.revAln.DeletionQV(orientation="genomic"))


        #     # def testInsertionQV(self):
        #     #     pass

        #     # def testSubstitutionQV(self):
        #     #     pass

        #     # def testIPD(self):
        #     #     pass



        #     def testDeletionTag(self):
        #         expectedFwdNative = [78, 78, 84, 78, 78, 67, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78,
        #                              78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 65, 78,
        #                              78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78]
        #         AEQ(expectedFwdNative, self.fwdAln.DeletionTag(aligned=True))
        #         AEQ(expectedFwdNative, self.fwdAln.DeletionTag())
        #         AEQ(expectedFwdNative, self.fwdAln.DeletionTag(orientation="genomic"))

        #         expectedRevNative = [78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78,
        #                              78, 78, 78, 78, 45, 67, 78, 78, 78, 78, 78, 45, 84, 78, 78, 78, 78,
        #                              78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 45, 78, 78, 78, 78,
        #                              78, 78, 78, 78, 78, 78, 78, 78, 78, 78]
        #         AEQ(expectedRevNative, self.revAln.DeletionTag(aligned=True))
        #         AEQ(expectedRevNative, self.revAln.DeletionTag())

        #         # TODO: what is the correct behavior here?
        #         #AEQ(expectedRevNative[::-1], self.revAln.DeletionTag(orientation="genomic"))

    def testTranscript(self):
        EQ('MMMMMMRMDMMMMIIMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMDMMMMMMMMMMMMMMMMMMMMMMMMMMDMMMMMMMMMMMMMMMMMMMMMMMMMMDMMMMMMMMMMMMMMMIMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMDMMMDMMMMMMMMMMMMMMRMMMMMMMMMMMMMMMMMMMMMMMMMDMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMDMMMMMMMMMMMMMMMMDMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMDMMMMMMMMDMIMMMMMMMMMMMMMMMMMMMMMMMMMDMMMMMMMMMMMMMMM',
           self.fwdAln.transcript())

        EQ("MMMMMMMMMMMMMMMIMMMMMMMMMMIMMMMMMMIMMMMMDMMMIMMMMIMMMMMMMMMMMMMMMMMMMMMMIMMMMMMMMMMMMMMMIMMMMMMMMMMMMMMMDMMMMMMMMMMMMMMMMMMMMMMMMMMMMMIIMIMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
           self.revAln.transcript())

    def testClippedAlignments(self):
        # Get a more interesting (more gappy) fwd strand aln
        a = self.fwdAln
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

        #         # Get a more interesting (more gappy) rev strand aln
        #         b = self.alns[3]
        #         EQ([(2216, 'G', 'G'),
        #             (2215, 'G', 'G'),
        #             (2214, '-', 'C'),
        #             (2214, 'C', 'C'),
        #             (2213, 'A', 'A'),
        #             (2212, 'T', 'T'),
        #             (2211, 'G', 'G'),
        #             (2210, 'C', 'C'),
        #             (2209, 'T', 'T'),
        #             (2208, 'G', '-'),
        #             (2207, 'G', 'G'),
        #             (2206, 'C', 'C')],
        #            zip(b.referencePositions(), b.reference(), b.read())[188:200])

        #         bc1 = b.clippedTo(2208, 2214)
        #         EQ([(2213, 'A', 'A'),
        #             (2212, 'T', 'T'),
        #             (2211, 'G', 'G'),
        #             (2210, 'C', 'C'),
        #             (2209, 'T', 'T'),
        #             (2208, 'G', '-')],
        #            zip(bc1.referencePositions(), bc1.reference(), bc1.read()))

        #         bc2 = b.clippedTo(2207, 2215)
        #         EQ([(2214, 'C', 'C'),
        #             (2213, 'A', 'A'),
        #             (2212, 'T', 'T'),
        #             (2211, 'G', 'G'),
        #             (2210, 'C', 'C'),
        #             (2209, 'T', 'T'),
        #             (2208, 'G', '-'),
        #             (2207, 'G', 'G')],
        #            zip(bc2.referencePositions(), bc2.reference(), bc2.read()))

        #         bc3 = b.clippedTo(2209, 2214)
        #         EQ([(2213, 'A', 'A'),
        #             (2212, 'T', 'T'),
        #             (2211, 'G', 'G'),
        #             (2210, 'C', 'C'),
        #             (2209, 'T', 'T')],
        #            zip(bc3.referencePositions(), bc3.reference(), bc3.read()))


        #         # Test clipping in a large deletion
        #         d = self.alns[52]
        #         EQ([(16191, 'C', 'C'),
        #             (16192, 'A', 'A'),
        #             (16193, 'G', 'G'),
        #             (16194, 'C', 'C'),
        #             (16195, 'A', 'A'),
        #             (16196, 'G', '-'),
        #             (16197, 'G', '-'),
        #             (16198, 'T', '-'),
        #             (16199, 'G', 'G'),
        #             (16200, 'A', 'A'),
        #             (16201, 'G', 'G')],
        #            zip(d.referencePositions(), d.reference(), d.read())[129:140])
        #         dc1 = d.clippedTo(16196, 16198)

        #         # where's the test code?

    def testBaxAttaching(self):
        # Before attaching, should get sane exceptions
        with assert_raises(ValueError):
           self.fwdAln.zmw

        with assert_raises(ValueError):
           self.fwdAln.zmwRead

        # Now attach
        self.f.attach(self.BAX_FILE)
        EQ("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/32328/1_344",
           self.fwdAln.readName)
        EQ("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/32328",
           self.fwdAln.zmwName)
        EQ("<Zmw: m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/32328>",
           repr(self.fwdAln.zmw))
        EQ("<ZmwRead: m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/32328/1_344>",
           repr(self.fwdAln.zmwRead))

        # Check read contents, for every aln.
        for aln in self.alns:
            EQ(aln.read(aligned=False, orientation="native"), aln.zmwRead.basecalls())

    def testClippingsVsBaxData(self):
        self.f.attach(self.BAX_FILE)
        for aln in [self.fwdAln, self.revAln]:
            for cS in xrange(aln.tStart, aln.tEnd + 1):
                for cE in xrange(cS + 1, min(aln.tEnd, cS + 10)):
                    ca = aln.clippedTo(cS, cE)
                    EQ(ca.zmwRead.basecalls(),
                       ca.read(aligned=False, orientation="native"))

    def testReadsInRange(self):
        wLen = 1000
        for wStart in xrange(0, 50000, wLen):
            wEnd = wStart + wLen
            expectedNames = set([ a.readName for a in self.alns
                                  if (a.referenceName == "lambda_NEB3011" and
                                      a.overlapsReferenceRange(wStart, wEnd)) ])
            EQ(expectedNames,
               set([ a.readName for a in self.f.readsInRange("lambda_NEB3011", wStart, wEnd) ]))

    def testReadGroupTable(self):
        rgFwd = self.fwdAln.readGroupInfo
        EQ([('ID', '<i4'), ('MovieName', 'O'), ('ReadType', 'O'), ('SequencingChemistry', 'O'), ('FrameRate', '<f8')], rgFwd.dtype)
        EQ("P6-C4", rgFwd.SequencingChemistry)
        EQ("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0", rgFwd.MovieName)
        #EQ("bar", rgFwd.ReadType)

    def testSequencingChemistry(self):
        EQ(["P6-C4"], self.f.sequencingChemistry)
        EQ("P6-C4", self.fwdAln.sequencingChemistry)
        EQ("P6-C4", self.revAln.sequencingChemistry)



class _IndexedAlnFileReaderTests(_BasicAlnFileReaderTests):
    """
    Abstract base class for tests of the reader functionality
    requiring an alignment index (or bam.pbi index)
    """

    def testMapQV(self):
        c = Counter(self.f.mapQV)
        EQ(Counter({254: 112}), c)

    def testHoleNumbers(self):
        c  = Counter([a.holeNumber for a in self.f])   # from records
        c2 = Counter(self.f.holeNumber)                # from index
        expected = Counter({37134: 14, 6251: 10, 32861: 8, 14743: 4,
                            35858: 3, 39571: 3, 13473: 3, 32560: 3, 46835: 3, 47698: 3,
                            16996: 3, 30983: 2, 38025: 2, 36363: 2, 23454: 2, 49194: 2,
                            24494: 2, 20211: 2, 50621: 2, 12736: 2, 19915: 2, 6469: 2,
                            31174: 2, 32328: 2, 42827: 2, 7247: 2, 50257: 2, 2771: 2,
                            1650: 2, 24962: 1, 32901: 1, 36628: 1, 7957: 1, 26262: 1,
                            15641: 1, 49050: 1, 19360: 1, 42165: 1, 44356: 1, 51534: 1,
                            29843: 1, 38754: 1, 52206: 1, 49521: 1, 45203: 1, 7670: 1,
                            54396: 1, 19837: 1})
        EQ(expected, c)
        EQ(expected, c2)

    def testErrorCounts(self):
        for aln in [self.fwdAln, self.revAln]:
            counts = Counter(aln.transcript())
            EQ(counts["M"], aln.nM)
            EQ(counts["R"], aln.nMM)
            EQ(counts["I"], aln.nIns)
            EQ(counts["D"], aln.nDel)


    #     def testAlignedIdentity(self):
    #         pass

    def testReadsByName(self):
        reads2771_1 = self.f.readsByName("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/2771/*")
        reads2771_2 = self.f.readsByName("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/2771")
        reads2771_3 = self.f.readsByName("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/2771/")

        expectedReadNames = ["m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/2771/8741_8874",
                             "m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/2771/8942_9480"]

        EQ(expectedReadNames, [r.readName for r in reads2771_1])
        EQ(expectedReadNames, [r.readName for r in reads2771_2])
        EQ(expectedReadNames, [r.readName for r in reads2771_3])


class TestCmpH5(_IndexedAlnFileReaderTests):
    READER_CONSTRUCTOR = CmpH5Reader
    CONSTRUCTOR_ARGS   = (data.getBamAndCmpH5()[1],)

    #
    # Test behaviors specific to CmpH5Reader, which should be few.
    #
    def testLazyChemistryResolution(self):
        """
        The CmpH5Reader allows reading of files that have missing
        chemistry information---an exception will be thrown only upon
        attempts to access the information.  We need to retain this
        behavior for compatibility.  """
        oldCmpH5 = data.getCmpH5()

        C = CmpH5Reader(oldCmpH5) # no exception here

        with assert_raises(ChemistryLookupError):
            C.sequencingChemistry

        with assert_raises(ChemistryLookupError):
            C[0].sequencingChemistry


class TestBasicBam(_BasicAlnFileReaderTests):
    READER_CONSTRUCTOR = BamReader
    CONSTRUCTOR_ARGS   = (data.getBamAndCmpH5()[0], data.getLambdaFasta())

    def testSpecVersion(self):
        EQ("3.0.1",     self.f.version)

    def testReadScore(self):
        EQISH(0.904, self.fwdAln.readScore, 3)


class TestIndexedBam(_IndexedAlnFileReaderTests):
    READER_CONSTRUCTOR = IndexedBamReader
    CONSTRUCTOR_ARGS   = (data.getBamAndCmpH5()[0], data.getLambdaFasta())

    def test_empty_bam(self):
        fn = data.getEmptyBam()
        bam = IndexedBamReader(fn)
        EQ(len(bam), 0)

    def test_alignment_identity(self):
        """
        Check that the values of the 'identity' property are consistent
        between IndexedBamReader (numpy array) and BamAlignment (float)
        """
        fn = data.getBamAndCmpH5()[0]
        with IndexedBamReader(fn) as bam_in:
            i1 = bam_in.identity
            i2 = np.array([ rec.identity for rec in bam_in ])
            EQ((i2 == i1).all(), True)

    def test_alignment_identity_unindexed(self):
        """
        Check that the value of the 'identity' property is the same whether
        or not the .pbi index was used to calculate it.
        """
        fn1 = data.getBamAndCmpH5()[0]
        fn2 = tempfile.NamedTemporaryFile(suffix=".bam").name
        shutil.copyfile(fn1, fn2)
        with IndexedBamReader(fn1) as bam_pbi:
            with BamReader(fn2) as bam_noindex:
                i1 = np.array([ rec.identity for rec in bam_pbi ])
                i2 = np.array([ rec.identity for rec in bam_noindex ])
                EQ((i2 == i1).all(), True)


class TestCCSBam(object):
    def __init__(self):
        self.f = BamReader(data.getCCSBAM())

    @SkipTest
    def testBasicOperations(self):
        EQ(False, self.f.isEmpty)
        EQ(False, self.f.isSorted)
        EQ(18,    len(self.f))

    def testQStartEndUnavailable(self):
        for aln in self.f:
            with assert_raises(UnavailableFeature):
                aln.qStart
            with assert_raises(UnavailableFeature):
                aln.qEnd


class TestMultipleReadGroups(object):
    """
    Verify that BAM files with multiple read groups are handled sensibly - see
    bug 26548.
    """
    SAM_IN = """\
@HD\tVN:1.5\tSO:coordinate\tpb:3.0.1
@SQ\tSN:ecoliK12_pbi_March2013_2955000_to_2980000\tLN:25000\tM5:734d5f3b2859595f4bd87a2fe6b7389b
@RG\tID:3f58e5b8\tPL:PACBIO\tDS:READTYPE=SUBREAD;DeletionQV=dq;DeletionTag=dt;InsertionQV=iq;MergeQV=mq;SubstitutionQV=sq;Ipd:CodecV1=ip;BASECALLERVERSION=2.1;FRAMERATEHZ=75.000000;BINDINGKIT=100356300;SEQUENCINGKIT=100356200\tPU:movie1
@RG\tID:b5482b33\tPL:PACBIO\tDS:READTYPE=SUBREAD;DeletionQV=dq;DeletionTag=dt;InsertionQV=iq;MergeQV=mq;SubstitutionQV=sq;Ipd:CodecV1=ip;BINDINGKIT=100356300;SEQUENCINGKIT=100356200;BASECALLERVERSION=2.1;FRAMERATEHZ=75.000000\tPU:m140906_231018_42161_c100676332550000001823129611271486_s1_p0
movie1/54130/0_10\t2\tecoliK12_pbi_March2013_2955000_to_2980000\t2\t10\t10=\t*\t0\t0\tAATGAGGAGA\t*\tRG:Z:3f58e5b8\tdq:Z:2222'$22'2\tdt:Z:NNNNAGNNGN\tip:B:C,255,2,0,10,22,34,0,2,3,0,16\tiq:Z:(+#1'$#*1&\tmq:Z:&1~51*5&~2\tnp:i:1\tqe:i:10\tqs:i:0\trq:f:0.854\tsn:B:f,2,2,2,2\tsq:Z:<32<4<<<<3\tzm:i:54130\tAS:i:-3020\tNM:i:134\tcx:i:2
m140906_231018_42161_c100676332550000001823129611271486_s1_p0/1/10_20\t2\tecoliK12_pbi_March2013_2955000_to_2980000\t12\t10\t10=\t*\t0\t0\tAATGAGGAGA\t*\tRG:Z:b5482b33\tdq:Z:2222'$22'2\tdt:Z:NNNNAGNNGN\tip:B:C,255,2,0,10,22,34,0,2,3,0,16\tiq:Z:(+#1'$#*1&\tmq:Z:&1~51*5&~2\tnp:i:1\tqe:i:20\tqs:i:10\trq:f:0.854\tsn:B:f,2,2,2,2\tsq:Z:<32<4<<<<3\tzm:i:54130\tAS:i:-3020\tNM:i:134\tcx:i:2"""

    def test_retrieve_read_group_properties(self):
        f1 = tempfile.NamedTemporaryFile(suffix=".sam").name
        f2 = tempfile.NamedTemporaryFile(suffix=".bam").name
        with open(f1, "w") as f:
            f.write(self.SAM_IN)
        with pysam.AlignmentFile(f1) as sam_in:
            with pysam.AlignmentFile(f2, 'wb', template=sam_in) as bam_out:
                for aln in sam_in:
                    bam_out.write(aln)
        movie_names = []
        with BamReader(f2) as bam_in:
            for aln in bam_in:
                EQ(aln.sequencingChemistry, "P6-C4")
                movie_names.append(aln.movieName)
        EQ(movie_names, ['movie1', 'm140906_231018_42161_c100676332550000001823129611271486_s1_p0'])
