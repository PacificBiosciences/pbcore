from numpy.testing import (assert_array_almost_equal as ASIM,
                           assert_array_equal        as AEQ)
from nose.tools import (nottest,
                        assert_raises,
                        assert_equal as EQ)
from nose import SkipTest

import numpy as np
import bisect
import h5py
from collections import Counter

from pbcore import data
from pbcore.io import CmpH5Reader, BamReader, IndexedBamReader
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
        self.fwdAln = self.alns[70]
        self.revAln = self.alns[71]

    def testBasicOperations(self):
        EQ(False, self.f.isEmpty)
        EQ(True,  self.f.isSorted)
        EQ(115,   len(self.f))

    def testStrandOrientation(self):
        EQ(True,  self.fwdAln.isForwardStrand)
        EQ(False, self.fwdAln.isReverseStrand)
        EQ(False, self.revAln.isForwardStrand)
        EQ(True,  self.revAln.isReverseStrand)

    def testReadName(self):
        EQ("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/7957/9681_9727",
           self.fwdAln.readName)
        EQ("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/7957/9561_9619",
           self.revAln.readName)

    def testAlignedRead(self):
        expectedFwdNative = "TACGGTCATCATCTGACACTACAGACTCTGGCATCGCTGTGAAGAC"
        EQ(expectedFwdNative, self.fwdAln.read(aligned=True))
        EQ(expectedFwdNative, self.fwdAln.read())
        EQ(expectedFwdNative, self.fwdAln.read(orientation="genomic"))
        expectedRevNative = "CTTGTGAAAATGCTGAATTCT-GCGTCG-CTTCACCAGCGATGCCA-AGTCTGTAGTGTCA"
        EQ(expectedRevNative, self.revAln.read(aligned=True))
        EQ(expectedRevNative, self.revAln.read())
        EQ(RC(expectedRevNative), self.revAln.read(orientation="genomic"))

    def testUnalignedRead(self):
        expectedFwdNative = "TACGGTCATCATCTGACACTACAGACTCTGGCATCGCTGTGAAGAC"
        EQ(expectedFwdNative, self.fwdAln.read(aligned=False))
        EQ(expectedFwdNative, self.fwdAln.read(aligned=False, orientation="genomic"))
        expectedRevNative = "CTTGTGAAAATGCTGAATTCTGCGTCGCTTCACCAGCGATGCCAAGTCTGTAGTGTCA"
        EQ(expectedRevNative, self.revAln.read(aligned=False))
        EQ(RC(expectedRevNative), self.revAln.read(aligned=False, orientation="genomic"))

    def testAlignedReference(self):
        expectedFwdNative = "TACGGTCATCATCTGACACTACAGACTCTGGCATCGCTGTGAAGAC"
        EQ(expectedFwdNative, self.fwdAln.reference(aligned=True))
        EQ(expectedFwdNative, self.fwdAln.reference())
        EQ(expectedFwdNative, self.fwdAln.reference(orientation="genomic"))
        expectedRevNative = "CTTGTGAAAATGCTGAATT-TCGCGTCGTCTTCA-CAGCGATGCCAGAGTCTGTAGTGTCA"
        EQ(expectedRevNative, self.revAln.reference(aligned=True))
        EQ(expectedRevNative, self.revAln.reference())
        EQ(RC(expectedRevNative), self.revAln.reference(orientation="genomic"))

    def testUnalignedReference(self):
        expectedFwdNative = "TACGGTCATCATCTGACACTACAGACTCTGGCATCGCTGTGAAGAC"
        EQ(expectedFwdNative, self.fwdAln.reference(aligned=False))
        EQ(expectedFwdNative, self.fwdAln.reference(aligned=False, orientation="genomic"))
        expectedRevNative = "CTTGTGAAAATGCTGAATTTCGCGTCGTCTTCACAGCGATGCCAGAGTCTGTAGTGTCA"
        EQ(expectedRevNative, self.revAln.reference(aligned=False))
        EQ(RC(expectedRevNative), self.revAln.reference(aligned=False, orientation="genomic"))

    def testDeletionQV(self):
        expectedFwdNative = [ 17,  17,   7,  17,  17,   6,  17,  17,  17,  17,  17,  17,  17,
                              17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,  17,
                              17,  17,  17,  17,  17,  17,   7,  17,  17,  17,  17,  17,  17,
                              17,  17,  17,  17,  17,  17,  17 ]
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


    # def testInsertionQV(self):
    #     pass

    # def testSubstitutionQV(self):
    #     pass

    # def testIPD(self):
    #     pass

    def testDeletionTag(self):
        expectedFwdNative = [78, 78, 84, 78, 78, 67, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78,
                             78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 65, 78,
                             78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78]
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
        b = self.alns[3]
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
           zip(d.referencePositions(), d.reference(), d.read())[129:140])
        dc1 = d.clippedTo(16196, 16198)

        # where's the test code?

    def testBaxAttaching(self):
        # Before attaching, should get sane exceptions
        with assert_raises(ValueError):
           self.fwdAln.zmw

        with assert_raises(ValueError):
           self.fwdAln.zmwRead

        # Now attach
        self.f.attach(self.BAX_FILE)
        EQ('m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/7957/9681_9727',
           self.fwdAln.readName)
        EQ('m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/7957'
           , self.fwdAln.zmwName)
        EQ('<Zmw: m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/7957>',
           repr(self.fwdAln.zmw))
        EQ('<ZmwRead: m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/7957/9681_9727>',
           repr(self.fwdAln.zmwRead))

        # Check read contents, for every aln.
        for aln in self.alns:
            EQ(aln.read(aligned=False, orientation="native"), aln.zmwRead.basecalls())


    def testClippingsVsBaxData(self):
        self.f.attach(self.BAX_FILE)
        for aln in [self.alns[52], self.alns[8]]:
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
        EQ(Counter({254: 115}), c)

    def testHoleNumbers(self):
        c  = Counter([a.holeNumber for a in self.f])   # from records
        c2 = Counter(self.f.holeNumber)                # from index
        expected = Counter({37134: 14, 6251: 10, 32861: 8, 14743: 4, 35858: 3,
                            39571: 3, 13473: 3, 32560: 3, 46835: 3, 47698: 3, 16996: 3,
                            30983: 2, 38025: 2, 36363: 2, 7957: 2, 49050: 2, 23454: 2,
                            49194: 2, 24494: 2, 20211: 2, 50621: 2, 12736: 2, 19915: 2,
                            6469: 2, 31174: 2, 32328: 2, 42827: 2, 7247: 2, 50257: 2,
                            2771: 2, 1650: 2, 45203: 2, 24962: 1, 32901: 1, 36628: 1,
                            26262: 1, 15641: 1, 19360: 1, 42165: 1, 44356: 1, 51534: 1,
                            29843: 1, 38754: 1, 52206: 1, 49521: 1, 7670: 1, 54396: 1,
                            19837: 1})
        EQ(expected, c)
        EQ(expected, c2)

    def testAlignedIdentity(self):
        pass

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
        EQ("3.0b3",     self.f.version)

    # def testNoLegacyBamTags(self):
    #     # junk from older PacBio BAM spec versions doesn't belong
    #     tagNames = [x[0] for x in self.fwdAln.peer.tags]
    #     EQ(set(["RG",
    #             "qs", "qe", "zm", "np", "rq",
    #             "dq", "dt", "iq", "mq", "sq"]),
    #        set(tagNames))


class TestIndexedBam(_IndexedAlnFileReaderTests):
    READER_CONSTRUCTOR = IndexedBamReader
    CONSTRUCTOR_ARGS   = (data.getBamAndCmpH5()[0], data.getLambdaFasta())
