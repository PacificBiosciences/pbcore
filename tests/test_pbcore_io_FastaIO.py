from nose.tools import assert_equal
from pbcore import data
from pbcore.io import FastaReader


class TestFastaReader:

    def test_readFasta(self):
        f = FastaReader(data.getFasta())
        entries = list(f)
        assert_equal(48, len(entries))
        assert_equal("ref000001|EGFR_Exon_2", entries[0].name)
        assert_equal("TTTCTTCCAGTTTGCCAAGGCACGAGTAACAAGCTCACGCAGTTGGGCACTTT"
                     "TGAAGATCATTTTCTCAGCCTCCAGAGGATGTTCAATAACTGTGAGGTGGTCC"
                     "TTGGGAATTTGGAAATTACCTATGTGCAGAGGAATTATGATCTTTCCTTCTTA"
                     "AAGGTTGGTGACTTTGATTTTCCT",
                     entries[0].sequence)

