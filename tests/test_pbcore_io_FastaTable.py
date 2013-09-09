from nose.tools import assert_equal, assert_true, assert_false
from pbcore import data
from pbcore.io import FastaReader, FastaWriter, FastaTable


class TestFastaTable:

    def setup(self):
        self.fastaPath = data.getFasta()

    def testIteration(self):
        ft = FastaTable(self.fastaPath)
        fr = FastaReader(self.fastaPath)
        ftContigs = list(ft)
        frContigs = list(fr)
        assert_equal(len(frContigs), len(ftContigs))
        assert_equal(48, len(ftContigs))
        for ftC, frC in zip(ftContigs, frContigs):
            assert_equal(frC.name, ftC.name)
            assert_equal(frC.sequence, ftC.sequence[:])

        # Unlike FastaReader, FastaTable iteration is repeatable.
        assert_equal(48, len(list(ft)))

    def testAccessByName(self):
        ft = FastaTable(self.fastaPath)
        r0000021 = ft["ref000021|EGFR_Exon_22"]
        assert_equal("ref000021|EGFR_Exon_22", r0000021.name)
        assert_equal("CACTGCCTCATCTCTCACCATCCCAAGGTGCCTATCAAGTGGATGGCATTGGAATCAATT" + \
                     "TTACACAGAATCTATACCCACCAGAGTGATGTCTGGAGCTACGGTGAGTCATAATCCTGA" + \
                     "TGCTAATGAGTTTGTACTGAGGCCAAGCTGG",
                     r0000021.sequence[:])

    def testAccessByPosition(self):
        ft = FastaTable(self.fastaPath)
        r000001 = ft[0]
        assert_equal("<FastaTableRecord: ref000001|EGFR_Exon_2>", repr(r000001))
        firstTwo = ft[:2]
        assert_equal([ft[0], ft[1]], firstTwo)
        lastTwo = ft[-2:]
        assert_equal([ft[-2], ft[-1]], lastTwo)

    def testSlice(self):
        ft = FastaTable(self.fastaPath)
        r0000021 = ft["ref000021|EGFR_Exon_22"]
        sequence = r0000021.sequence
        assert_equal("CACTGCCTCA",
                     sequence[0:10])
        assert_equal("GCCAAGCTGG",
                     sequence[-10:])
        assert_equal("G", sequence[-1])
        assert_equal("T", sequence[-3])
        assert_equal("C", sequence[0])
        assert_equal("A", sequence[1])
