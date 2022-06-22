from collections import Counter
import numpy as np
import os
import pytest
import shutil
import tempfile

from numpy.testing import (assert_array_almost_equal as ASIM,
                           assert_array_equal as AEQ)

from pbcore import data
from pbcore.io import BamReader, IndexedBamReader
from pbcore.io.align._BamSupport import UnavailableFeature
from pbcore.sequence import reverseComplement as RC
from pbcore.chemistry import ChemistryLookupError
from pbcore.io.align.BamIO import AlignmentFile


class _BasicAlnFileReaderTests:
    """
    Abstract base class for tests of the basic reader
    functionality---functionality not requiring the bam.pbi index.

    The tests are pretty tailored to the BAM files in
    pbcore.data.
    """

    READER_CONSTRUCTOR = None
    CONSTRUCTOR_ARGS = None

    @classmethod
    def setup_class(cls):
        cls.f = cls.READER_CONSTRUCTOR(*cls.CONSTRUCTOR_ARGS)
        cls.alns = list(cls.f)
        cls.fwdAln = cls.alns[1]
        cls.revAln = cls.alns[105]

    def testBasicOperations(self):
        assert False == self.f.isEmpty
        assert True == self.f.isSorted
        assert 112 == len(self.f)

    def testStrandOrientation(self):
        assert True == self.fwdAln.isForwardStrand
        assert False == self.fwdAln.isReverseStrand
        assert False == self.revAln.isForwardStrand
        assert True == self.revAln.isReverseStrand

    def testReadName(self):
        assert "m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/32328/1_344" == self.fwdAln.readName
        assert "m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/51534/1_200" == self.revAln.readName

    def testAlignedRead(self):
        expectedFwdNative = "GCCGCGAT-GATGAAAACTGATACCGGGGTTGCTGAGTGAATATATCGAACAGTCAGGTT-ACAGGCTGCGGCATTTTGTCCGCGCC-GGCTTCGCTCACTGTTCAGGCCGGAG-CACAGACCGCCGTTGAAATGGGCGGATGCTAATTACTATCTCCCGAAAGAAT-CGC-TACCAGGAAGGGCGATGGGAAACACTGCCCTTTCAGCGGG-CATCATGAATGCGATGGGCAGCGACTACATCCGTGAGGT-AATGTGGTGAAGTCTG-CCGTGTCGGTTATTCCAAAATGCTGCTGGGTG-TTATGCCT-CGTTTATAGAGCATAAGCAGCGCAACA-CCTTATCTGGTTGCC"
        assert expectedFwdNative == self.fwdAln.read(aligned=True)
        assert expectedFwdNative == self.fwdAln.read()
        assert expectedFwdNative == self.fwdAln.read(orientation="genomic")
        expectedRevNative = "TAGCCACCGGATATCACCACAGGTGAGGCCGTGTAAGTTG-AGGTTTTTCTACGTCAGATTCTTTTGGGATTGGGCTTGGGTTTATTTCCTGGTGCGTTTCGTT-GAAGGTATTTGCAGTTTTCGCAGATTATGCCTCCGGTGATACTTCGTCGCTGTCTCGCCACACGTCCTCCTTTTCCTGCGGTAGTGGTAACACCCC"
        assert expectedRevNative == self.revAln.read(aligned=True)
        assert expectedRevNative == self.revAln.read()
        assert RC(expectedRevNative) == self.revAln.read(orientation="genomic")

    def testUnalignedRead(self):
        expectedFwdNative = 'GCCGCGATGATGAAAACTGATACCGGGGTTGCTGAGTGAATATATCGAACAGTCAGGTTACAGGCTGCGGCATTTTGTCCGCGCCGGCTTCGCTCACTGTTCAGGCCGGAGCACAGACCGCCGTTGAAATGGGCGGATGCTAATTACTATCTCCCGAAAGAATCGCTACCAGGAAGGGCGATGGGAAACACTGCCCTTTCAGCGGGCATCATGAATGCGATGGGCAGCGACTACATCCGTGAGGTAATGTGGTGAAGTCTGCCGTGTCGGTTATTCCAAAATGCTGCTGGGTGTTATGCCTCGTTTATAGAGCATAAGCAGCGCAACACCTTATCTGGTTGCC'
        assert expectedFwdNative == self.fwdAln.read(aligned=False)
        assert expectedFwdNative == self.fwdAln.read(
            aligned=False, orientation="genomic")
        expectedRevNative = "TAGCCACCGGATATCACCACAGGTGAGGCCGTGTAAGTTGAGGTTTTTCTACGTCAGATTCTTTTGGGATTGGGCTTGGGTTTATTTCCTGGTGCGTTTCGTTGAAGGTATTTGCAGTTTTCGCAGATTATGCCTCCGGTGATACTTCGTCGCTGTCTCGCCACACGTCCTCCTTTTCCTGCGGTAGTGGTAACACCCC"
        assert expectedRevNative == self.revAln.read(aligned=False)
        assert RC(expectedRevNative) == self.revAln.read(
            aligned=False, orientation="genomic")

    def testAlignedReference(self):
        expectedFwdNative = 'GCCGCGCTGGATG--AACTGATACCGGGGTTGCTGAGTGAATATATCGAACAGTCAGGTTAACAGGCTGCGGCATTTTGTCCGCGCCGGGCTTCGCTCACTGTTCAGGCCGGAGCCACAGACCGCCGTTG-AATGGGCGGATGCTAATTACTATCTCCCGAAAGAATCCGCATACCAGGAAGGGCGCTGGGAAACACTGCCCTTTCAGCGGGCCATCATGAATGCGATGGGCAGCGACTACATCCGTGAGGTGAATGTGGTGAAGTCTGCCCGTGTCGGTTATTCCAAAATGCTGCTGGGTGTTTATGCCTAC-TTTATAGAGCATAAGCAGCGCAACACCCTTATCTGGTTGCC'
        assert expectedFwdNative == self.fwdAln.reference(aligned=True)
        assert expectedFwdNative == self.fwdAln.reference()
        assert expectedFwdNative == self.fwdAln.reference(
            orientation="genomic")
        expectedRevNative = 'TAGCCACCGGATATC-CCACAGGTGA-GCCGTGT-AGTTGAAGG-TTTT-TACGTCAGATTCTTTTGGGATT-GGCTTGGGTTTATTT-CTGGTGCGTTTCGTTGGAAGGTATTTGCAGTTTTCGCAGATTATG--T-CGGTGATACTTCGTCGCTGTCTCGCCACACGTCCTCCTTTTCCTGCGGTAGTGGTAACACCCC'
        assert expectedRevNative == self.revAln.reference(aligned=True)
        assert expectedRevNative == self.revAln.reference()
        assert RC(expectedRevNative) == self.revAln.reference(
            orientation="genomic")

    def testUnalignedReference(self):
        expectedFwdNative = "GCCGCGCTGGATGAACTGATACCGGGGTTGCTGAGTGAATATATCGAACAGTCAGGTTAACAGGCTGCGGCATTTTGTCCGCGCCGGGCTTCGCTCACTGTTCAGGCCGGAGCCACAGACCGCCGTTGAATGGGCGGATGCTAATTACTATCTCCCGAAAGAATCCGCATACCAGGAAGGGCGCTGGGAAACACTGCCCTTTCAGCGGGCCATCATGAATGCGATGGGCAGCGACTACATCCGTGAGGTGAATGTGGTGAAGTCTGCCCGTGTCGGTTATTCCAAAATGCTGCTGGGTGTTTATGCCTACTTTATAGAGCATAAGCAGCGCAACACCCTTATCTGGTTGCC"
        assert expectedFwdNative == self.fwdAln.reference(aligned=False)
        assert expectedFwdNative == self.fwdAln.reference(
            aligned=False, orientation="genomic")
        expectedRevNative = "TAGCCACCGGATATCCCACAGGTGAGCCGTGTAGTTGAAGGTTTTTACGTCAGATTCTTTTGGGATTGGCTTGGGTTTATTTCTGGTGCGTTTCGTTGGAAGGTATTTGCAGTTTTCGCAGATTATGTCGGTGATACTTCGTCGCTGTCTCGCCACACGTCCTCCTTTTCCTGCGGTAGTGGTAACACCCC"
        assert expectedRevNative == self.revAln.reference(aligned=False)
        assert RC(expectedRevNative) == self.revAln.reference(
            aligned=False, orientation="genomic")

    def testDeletionQV(self):
        expectedFwdNative = (
            [17, 17, 17, 17, 17, 17, 17, 17, 255,  4, 17, 17, 17,  8, 17, 17, 17, 17,
             17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
             17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 10,  8, 17,
             17, 17, 17, 17, 17, 17, 255, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
             17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 255, 17, 17,
             17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
             17, 17, 17, 17, 17, 17, 255, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
             17, 17, 17, 17, 17,  6, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
             17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 11, 17, 17, 17, 17,
             17, 17, 17, 17, 17, 255, 17, 17, 17, 255, 17, 17, 17, 17, 17, 17, 17, 17,
             17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
             17, 11, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 255, 17, 17, 17,
             17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
             17, 17, 17, 17,  7, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
             255,  8, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 255,
             17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
             17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 255, 17, 17, 17,
             17, 17, 17, 17, 17, 255, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
             17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 255, 17, 17,
             17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17])

        AEQ(expectedFwdNative, self.fwdAln.DeletionQV(aligned=True))
        AEQ(expectedFwdNative, self.fwdAln.DeletionQV())
        AEQ(expectedFwdNative, self.fwdAln.DeletionQV(orientation="genomic"))

        expectedRevNative = (
            [17, 17, 17, 17, 6, 17, 17, 17, 17, 17, 17, 17, 17, 17,
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
             17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17])

        print(self.revAln.DeletionQV(aligned=True))
        AEQ(expectedRevNative, self.revAln.DeletionQV(aligned=True))
        AEQ(expectedRevNative, self.revAln.DeletionQV())
        AEQ(expectedRevNative[::-1],
            self.revAln.DeletionQV(orientation="genomic"))

    def testTranscript(self):
        assert ('MMMMMMRMDMMMMIIMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM'
                'MMDMMMMMMMMMMMMMMMMMMMMMMMMMMDMMMMMMMMMMMMMMMMMMMMMMMMMMDM'
                'MMMMMMMMMMMMMMIMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMDMMMDMM'
                'MMMMMMMMMMMMRMMMMMMMMMMMMMMMMMMMMMMMMMDMMMMMMMMMMMMMMMMMMM'
                'MMMMMMMMMMMMMMMMMMMMDMMMMMMMMMMMMMMMMDMMMMMMMMMMMMMMMMMMMM'
                'MMMMMMMMMMMMDMMMMMMMMDMIMMMMMMMMMMMMMMMMMMMMMMMMMDMMMMMMMM'
                'MMMMMMM') == self.fwdAln.transcript()

        assert ("MMMMMMMMMMMMMMMIMMMMMMMMMMIMMMMMMMIMMMMMDMMMIMMMMIMMMMMMMM"
                "MMMMMMMMMMMMMMIMMMMMMMMMMMMMMMIMMMMMMMMMMMMMMMDMMMMMMMMMMM"
                "MMMMMMMMMMMMMMMMMMIIMIMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"
                "MMMMMMMMMMMMMMMMMMMMMMMMMMM") == self.revAln.transcript()

    def testClippedAlignments(self):
        # Get a more interesting (more gappy) fwd strand aln
        a = self.fwdAln
        assert [(980, 'C', 'C'),
                (981, 'C', 'C'),
                (982, 'T', 'T'),
                (983, 'A', '-'),
                (984, 'C', 'C'),
                (985, '-', 'G'),
                (985, 'T', 'T'),
                (986, 'T', 'T')] == list(zip(
                    a.referencePositions(),
                    a.reference(),
                    a.read()))[308:316]

        ac1 = a.clippedTo(983, 985)
        assert 983 == ac1.referenceStart
        assert 985 == ac1.referenceEnd
        assert [
            (983, 'A', '-'),
            (984, 'C', 'C')] == list(zip(
                ac1.referencePositions(),
                ac1.reference(),
                ac1.read()))

        ac2 = a.clippedTo(982, 986)
        assert 982 == ac2.referenceStart
        assert 986 == ac2.referenceEnd
        assert [
            (982, 'T', 'T'),
            (983, 'A', '-'),
            (984, 'C', 'C'),
            (985, '-', 'G'),
            (985, 'T', 'T')] == list(zip(
                ac2.referencePositions(),
                ac2.reference(),
                ac2.read()))

        ac3 = a.clippedTo(984, 985)
        assert 984 == ac3.referenceStart
        assert 985 == ac3.referenceEnd
        assert [
            (984, 'C', 'C')] == list(zip(
                ac3.referencePositions(),
                ac3.reference(),
                ac3.read()))

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

    def testReadsInRange(self):
        wLen = 1000
        for wStart in range(0, 50000, wLen):
            wEnd = wStart + wLen
            expectedNames = set([a.readName for a in self.alns
                                 if (a.referenceName == "lambda_NEB3011" and
                                     a.overlapsReferenceRange(wStart, wEnd))])
            assert expectedNames == set(
                [a.readName for a in self.f.readsInRange("lambda_NEB3011", wStart, wEnd)])

    def testReadGroupTable(self):
        rgFwd = self.fwdAln.readGroupInfo
        assert [
            ('ID', '<i4'),
            ('MovieName', 'O'),
            ('ReadType', 'O'),
            ('SequencingChemistry', 'O'),
            ('FrameRate', '<f8'),
            ('SampleName', 'O'),
            ('LibraryName', 'O'),
            ('BaseFeatures', 'O'),
            ('StringID', 'O')] == rgFwd.dtype
        assert isinstance(rgFwd.BaseFeatures, frozenset)
        assert 'S/P4-C2/5.0-8M' == rgFwd.SequencingChemistry
        assert "m140905_042212_sidney_c100564852550000001823085912221377_s1_X0" == rgFwd.MovieName

    def testSequencingChemistry(self):
        assert ['S/P4-C2/5.0-8M'] == self.f.sequencingChemistry
        assert 'S/P4-C2/5.0-8M' == self.fwdAln.sequencingChemistry
        assert 'S/P4-C2/5.0-8M' == self.revAln.sequencingChemistry


class _IndexedAlnFileReaderTests(_BasicAlnFileReaderTests):
    """
    Abstract base class for tests of the reader functionality
    requiring an alignment index (or bam.pbi index)
    """

    def testMapQV(self):
        c = Counter(self.f.mapQV)
        assert Counter({254: 112}) == c

    def testHoleNumbers(self):
        c = Counter([a.holeNumber for a in self.f])   # from records
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
        assert expected == c
        assert expected == c2

    def testErrorCounts(self):
        for aln in [self.fwdAln, self.revAln]:
            counts = Counter(aln.transcript())
            assert counts["M"] == aln.nM
            assert counts["R"] == aln.nMM
            assert counts["I"] == aln.nIns
            assert counts["D"] == aln.nDel

    def testReadsByName(self):
        reads2771_1 = self.f.readsByName(
            "m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/2771/*")
        reads2771_2 = self.f.readsByName(
            "m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/2771")
        reads2771_3 = self.f.readsByName(
            "m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/2771/")

        expectedReadNames = ["m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/2771/8741_8874",
                             "m140905_042212_sidney_c100564852550000001823085912221377_s1_X0/2771/8942_9480"]

        assert expectedReadNames == [r.readName for r in reads2771_1]
        assert expectedReadNames == [r.readName for r in reads2771_2]
        assert expectedReadNames == [r.readName for r in reads2771_3]


class TestBasicBam(_BasicAlnFileReaderTests):

    READER_CONSTRUCTOR = BamReader
    CONSTRUCTOR_ARGS = (data.getAlignedBam(), data.getLambdaFasta())

    def testSpecVersion(self):
        assert "3.0.1" == self.f.version

    def testReadScore(self):
        assert 0.904 == pytest.approx(self.fwdAln.readScore)

    def test_sample_name_default(self):
        assert "UnnamedSample" == self.f.readGroupTable[0].SampleName

    def test_library_name_default(self):
        assert "UnnamedLibrary" == self.f.readGroupTable[0].LibraryName


class TestIndexedBam(_IndexedAlnFileReaderTests):

    READER_CONSTRUCTOR = IndexedBamReader
    CONSTRUCTOR_ARGS = (data.getAlignedBam(), data.getLambdaFasta())

    def test_empty_bam(self):
        fn = data.getEmptyBam()
        bam = IndexedBamReader(fn)
        assert len(bam) == 0

    def test_alignment_identity(self):
        """
        Check that the values of the 'identity' property are consistent
        between IndexedBamReader (numpy array) and BamAlignment (float)
        """
        fn = data.getAlignedBam()
        with IndexedBamReader(fn) as bam_in:
            i1 = bam_in.identity
            i2 = np.array([rec.identity for rec in bam_in])
            assert (i2 == i1).all()

    def test_alignment_identity_unindexed(self):
        """
        Check that the value of the 'identity' property is the same whether
        or not the .pbi index was used to calculate it.
        """
        fn1 = data.getAlignedBam()
        fn2 = tempfile.NamedTemporaryFile(suffix=".bam").name
        shutil.copyfile(fn1, fn2)
        with IndexedBamReader(fn1) as bam_pbi:
            with BamReader(fn2) as bam_noindex:
                i1 = np.array([rec.identity for rec in bam_pbi])
                i2 = np.array([rec.identity for rec in bam_noindex])
                assert (i2 == i1).all()


class TestCCSBam:

    @classmethod
    def setup_class(cls):
        cls.f = BamReader(data.getCCSBAM())

    @pytest.mark.skip(reason="broken")
    def testBasicOperations(self):
        assert False == self.f.isEmpty
        assert False == self.f.isSorted
        assert 18 == len(self.f)

    def testQStartEndUnavailable(self):
        for aln in self.f:
            with pytest.raises(UnavailableFeature):
                aln.qStart
            with pytest.raises(UnavailableFeature):
                aln.qEnd


@pytest.mark.internal_data
class TestTranscriptBam:

    BAM_FILE = "/pbi/dept/secondary/siv/testdata/isoseqs/TranscriptSet/unpolished.bam"

    @classmethod
    def setup_class(cls):
        cls.f = IndexedBamReader(cls.BAM_FILE)

    def test_transcript_set_support(self):
        assert len(self.f) == 12218


class TestEmptyBam:

    def test_empty_bam_reads_in_range(self):
        with IndexedBamReader(data.getEmptyAlignedBam()) as bam:
            reads = bam.readsInRange("lambda_NEB3011", 0, 50000,
                                     justIndices=True)
            assert len(reads) == 0


class TestMultipleReadGroups:
    """
    Verify that BAM files with multiple read groups are handled sensibly - see
    bug 26548.
    """

    SAM_IN = """\
@HD\tVN:1.5\tSO:coordinate\tpb:3.0.7
@SQ\tSN:ecoliK12_pbi_March2013_2955000_to_2980000\tLN:25000\tM5:734d5f3b2859595f4bd87a2fe6b7389b
@RG\tID:19d45c63\tPL:PACBIO\tDS:READTYPE=SUBREAD;Ipd:CodecV1=ip;PulseWidth:CodecV1=pw;BINDINGKIT=101-789-500;SEQUENCINGKIT=101-789-300;BASECALLERVERSION=5.0.0;FRAMERATEHZ=100.000000\tPU:movie1\tPM:SEQUELII\tSM:test_sample1
@RG\tID:69995355\tPL:PACBIO\tDS:READTYPE=SUBREAD;Ipd:CodecV1=ip;PulseWidth:CodecV1=pw;BINDINGKIT=101-789-500;SEQUENCINGKIT=101-789-300;BASECALLERVERSION=5.0.0;FRAMERATEHZ=100.000000\tPU:m64012_181222_192540\tPM:SEQUELII\tSM:test_sample2
movie1/54130/0_10\t2\tecoliK12_pbi_March2013_2955000_to_2980000\t2\t10\t10=\t*\t0\t0\tAATGAGGAGA\t*\tRG:Z:19d45c63\tdq:Z:2222'$22'2\tdt:Z:NNNNAGNNGN\tip:B:C,255,2,0,10,22,34,0,2,3,0,16\tiq:Z:(+#1'$#*1&\tmq:Z:&1~51*5&~2\tnp:i:1\tqe:i:10\tqs:i:0\trq:f:0.854\tsn:B:f,2,2,2,2\tsq:Z:<32<4<<<<3\tzm:i:54130\tAS:i:-3020\tNM:i:134\tcx:i:2
m64012_181222_192540/1/10_20\t2\tecoliK12_pbi_March2013_2955000_to_2980000\t12\t10\t10=\t*\t0\t0\tAATGAGGAGA\t*\tRG:Z:69995355\tdq:Z:2222'$22'2\tdt:Z:NNNNAGNNGN\tip:B:C,255,2,0,10,22,34,0,2,3,0,16\tiq:Z:(+#1'$#*1&\tmq:Z:&1~51*5&~2\tnp:i:1\tqe:i:20\tqs:i:10\trq:f:0.854\tsn:B:f,2,2,2,2\tsq:Z:<32<4<<<<3\tzm:i:54130\tAS:i:-3020\tNM:i:134\tcx:i:2"""

    @classmethod
    def setup_class(cls):
        f1 = tempfile.NamedTemporaryFile(suffix=".sam").name
        f2 = tempfile.NamedTemporaryFile(suffix=".bam").name
        with open(f1, "w") as f:
            f.write(cls.SAM_IN)
        with AlignmentFile(f1) as sam_in:
            with AlignmentFile(f2, 'wb', template=sam_in) as bam_out:
                for aln in sam_in:
                    bam_out.write(aln)
        cls.bam_file = f2

    def test_retrieve_read_group_properties(self):
        movie_names = []
        with BamReader(self.bam_file) as bam_in:
            for aln in bam_in:
                assert aln.sequencingChemistry == 'S/P4-C2/5.0-8M'
            movie_names.extend([rg.MovieName for rg in bam_in.readGroupTable])
        assert movie_names == ['movie1', 'm64012_181222_192540']

    def test_sample_names(self):
        with BamReader(self.bam_file) as bam:
            samples = {rg.MovieName: rg.SampleName for rg in bam.readGroupTable}
            assert samples == {
                "movie1": "test_sample1",
                "m64012_181222_192540": "test_sample2"}


class TestMissingHeaderM5:
    """
    Verify that BAM files no M5 for SQ can still be processed
    """

    SAM_IN = """\
@HD\tVN:1.5\tSO:coordinate\tpb:3.0.7
@SQ\tSN:ecoliK12_pbi_March2013_2955000_to_2980000\tLN:25000
@RG\tID:19d45c63\tPL:PACBIO\tDS:READTYPE=SUBREAD;Ipd:CodecV1=ip;PulseWidth:CodecV1=pw;BINDINGKIT=101-789-500;SEQUENCINGKIT=101-789-300;BASECALLERVERSION=5.0.0;FRAMERATEHZ=100.000000\tPU:movie1\tPM:SEQUELII
@RG\tID:69995355\tPL:PACBIO\tDS:READTYPE=SUBREAD;Ipd:CodecV1=ip;PulseWidth:CodecV1=pw;BINDINGKIT=101-789-500;SEQUENCINGKIT=101-789-300;BASECALLERVERSION=5.0.0;FRAMERATEHZ=100.000000\tPU:m64012_181222_192540\tPM:SEQUELII
movie1/54130/0_10\t2\tecoliK12_pbi_March2013_2955000_to_2980000\t2\t10\t10=\t*\t0\t0\tAATGAGGAGA\t*\tRG:Z:19d45c63\tdq:Z:2222'$22'2\tdt:Z:NNNNAGNNGN\tip:B:C,255,2,0,10,22,34,0,2,3,0,16\tiq:Z:(+#1'$#*1&\tmq:Z:&1~51*5&~2\tnp:i:1\tqe:i:10\tqs:i:0\trq:f:0.854\tsn:B:f,2,2,2,2\tsq:Z:<32<4<<<<3\tzm:i:54130\tAS:i:-3020\tNM:i:134\tcx:i:2
m64012_181222_192540/1/10_20\t2\tecoliK12_pbi_March2013_2955000_to_2980000\t12\t10\t10=\t*\t0\t0\tAATGAGGAGA\t*\tRG:Z:69995355\tdq:Z:2222'$22'2\tdt:Z:NNNNAGNNGN\tip:B:C,255,2,0,10,22,34,0,2,3,0,16\tiq:Z:(+#1'$#*1&\tmq:Z:&1~51*5&~2\tnp:i:1\tqe:i:20\tqs:i:10\trq:f:0.854\tsn:B:f,2,2,2,2\tsq:Z:<32<4<<<<3\tzm:i:54130\tAS:i:-3020\tNM:i:134\tcx:i:2"""

    def test_retrieve_read_group_properties(self):
        f1 = tempfile.NamedTemporaryFile(suffix=".sam").name
        f2 = tempfile.NamedTemporaryFile(suffix=".bam").name
        with open(f1, "w") as f:
            f.write(self.SAM_IN)
        with AlignmentFile(f1) as sam_in:
            with AlignmentFile(f2, 'wb', template=sam_in) as bam_out:
                for aln in sam_in:
                    bam_out.write(aln)
        movie_names = []
        with BamReader(f2) as bam_in:
            for aln in bam_in:
                assert aln.sequencingChemistry == 'S/P4-C2/5.0-8M'
                movie_names.append(aln.movieName)
        assert movie_names == ['movie1', 'm64012_181222_192540']


class TestUpdatedChemistryMapping:
    """
    Verify we load the mapping from the updated chemistry mapping.xml
    from SMRT_CHEMISTRY_BUNDLE_DIR
    """

    def test_load_updated_mapping(self):
        import os
        from os.path import dirname
        from pbcore.chemistry.chemistry import _loadBarcodeMappings
        os.environ["SMRT_CHEMISTRY_BUNDLE_DIR"] = dirname(data.getMappingXml())
        mappings = _loadBarcodeMappings()
        assert mappings.get(("1", "2", "3.4"), None) == "FOUND"
        del os.environ["SMRT_CHEMISTRY_BUNDLE_DIR"]
        mappings = _loadBarcodeMappings()
        assert mappings.get(("1", "2", "3.4"), None) is None


class TestBarcodedBam:

    @pytest.mark.internal_data
    def test_read_lima_demultiplexed_bam(self):
        fn = "/pbi/dept/secondary/siv/testdata/pbcore-unittest/data/demultiplex.lbc1--lbc1.bam"
        bam = IndexedBamReader(fn)
        assert str(bam[0]) == "Unmapped BAM record: m54008_160219_003234/74056024/1184_3910"

    @pytest.mark.internal_data
    def test_mapped_bam_cigar_cref_skip(self):
        fn = "/pbi/dept/secondary/siv/testdata/pbcore-unittest/data/ITG-2283-cref-skip.subreads.bam"
        bam = BamReader(fn)
        for rec in bam:
            assert rec.read(aligned=True) is not None

    @pytest.mark.internal_data
    def test_mapped_bam_multiple_barcodes(self):
        fn = "/pbi/dept/secondary/siv/testdata/pbcore-unittest/data/multi_bc_bam/mapped.bam"
        bam = IndexedBamReader(fn)
        assert len(bam.readGroupTable) == 4
        for rec in bam:
            assert rec.readType == "CCS"
            rg = rec.readGroupInfo
            assert rg.StringID == rec.peer.get_tag("RG")
            break
