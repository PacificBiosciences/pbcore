from pbcore import data
from pbcore.io import FastaReader, FastaWriter, IndexedFastaReader


class TestIndexedFastaReader(object):

    FASTAPATH = data.getFasta()

    def testIteration(self):
        ft = IndexedFastaReader(self.FASTAPATH)
        fr = FastaReader(self.FASTAPATH)
        ftContigs = list(ft)
        frContigs = list(fr)
        assert len(frContigs) == len(ftContigs)
        assert 48 == len(ftContigs)
        for ftC, frC in zip(ftContigs, frContigs):
            assert frC.header == ftC.header
            assert frC.sequence == ftC.sequence[:]

        # Unlike FastaReader, IndexedFastaReader iteration is repeatable.
        assert 48 == len(list(ft))

    def testAccessByName(self):
        ft = IndexedFastaReader(self.FASTAPATH)
        r000021 = ft["ref000021|EGFR_Exon_22\tMetadataTest"]
        assert "ref000021|EGFR_Exon_22\tMetadataTest" == r000021.header
        assert "ref000021|EGFR_Exon_22" == r000021.id
        assert "MetadataTest" == r000021.comment
        assert ("CACTGCCTCATCTCTCACCATCCCAAGGTGCCTATCAAGTGGATGGCATTGGAATCAATT"
                "TTACACAGAATCTATACCCACCAGAGTGATGTCTGGAGCTACGGTGAGTCATAATCCTGA"
                "TGCTAATGAGTTTGTACTGAGGCCAAGCTGG") == r000021.sequence[:]

    def testAccessById(self):
        ft = IndexedFastaReader(self.FASTAPATH)
        r000021 = ft["ref000021|EGFR_Exon_22"]
        assert "ref000021|EGFR_Exon_22\tMetadataTest" == r000021.header
        assert "ref000021|EGFR_Exon_22" == r000021.id
        assert "MetadataTest" == r000021.comment
        assert ("CACTGCCTCATCTCTCACCATCCCAAGGTGCCTATCAAGTGGATGGCATTGGAATCAATT"
                "TTACACAGAATCTATACCCACCAGAGTGATGTCTGGAGCTACGGTGAGTCATAATCCTGA"
                "TGCTAATGAGTTTGTACTGAGGCCAAGCTGG") == r000021.sequence[:]

    def testAccessByPosition(self):
        ft = IndexedFastaReader(self.FASTAPATH)
        r000001 = ft[0]
        assert "<IndexedFastaRecord: ref000001|EGFR_Exon_2>" == repr(r000001)
        firstTwo = ft[:2]
        assert [ft[0], ft[1]] == firstTwo
        lastTwo = ft[-2:]
        assert [ft[-2], ft[-1]] == lastTwo

    def testSlice(self):
        ft = IndexedFastaReader(self.FASTAPATH)
        r000021 = ft["ref000021|EGFR_Exon_22"]
        sequence = r000021.sequence
        assert "CACTGCCTCA" == sequence[0:10]
        assert "GCCAAGCTGG" == sequence[-10:]
        assert "G" == sequence[-1]
        assert "T" == sequence[-3]
        assert "C" == sequence[0]
        assert "A" == sequence[1]

    def test_dosLineEndingsFasta(self):
        fr = FastaReader(data.getDosFormattedFasta())
        frEntries = list(fr)

        ft = IndexedFastaReader(data.getDosFormattedFasta())
        ftEntries = list(ft)

        assert len(frEntries) == len(ftEntries)
        for (frE, ftE) in zip(frEntries, ftEntries):
            assert frE.header == ftE.header
            assert frE.sequence == ftE.sequence[:]

    def test_readWeirdFastaIndex(self):
        f = IndexedFastaReader(data.getWeird())
        entries = list(f)
        assert 1 == len(entries)
        assert "chr1" == entries[0].header
        assert "acgtacgtacgtact" == entries[0].sequence[:]
