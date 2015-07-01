from nose.tools import assert_equal, assert_true, assert_false
from pbcore import data
from pbcore.io import FastaReader, FastaWriter, FastaRecord
from StringIO import StringIO

class TestFastaRecord:

    def setup(self):
        self.header = "chr1|blah|blah\tblah blah"
        self.rc_header = "chr1|blah|blah\tblah blah [revcomp]"
        self.id = "chr1|blah|blah"
        self.comment = "blah blah"
        self.sequence = "GATTACA" * 20
        self.rc_sequence = "TGTAATC" * 20
        self.length = 140
        self.expected__str__ = (
            ">chr1|blah|blah\tblah blah\n"
            "GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATT\n"
            "ACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAG\n"
            "ATTACAGATTACAGATTACA")
        self.rc1_expected__str__ = (
            ">chr1|blah|blah\tblah blah [revcomp]\n"
            "TGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTA\n"
            "ATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCT\n"
            "GTAATCTGTAATCTGTAATC")
        self.rc2_expected__str__ = (
            ">chr1|blah|blah\tblah blah\n"
            "TGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTA\n"
            "ATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCT\n"
            "GTAATCTGTAATCTGTAATC")
        self.record = FastaRecord(self.header, self.sequence)
        self.rc1_record = self.record.reverseComplement()
        self.rc2_record = self.record.reverseComplement(True)

    def test__init__(self):
        assert_equal(self.header, self.record.header)
        assert_equal(self.sequence, self.record.sequence)
        assert_equal(self.id, self.record.id)
        assert_equal(self.comment, self.record.comment)

    def test__str__(self):
        assert_equal(self.expected__str__, str(self.record))

    def test_fromString(self):
        recordFromString = FastaRecord.fromString(self.expected__str__)
        assert_equal(self.header, recordFromString.header)
        assert_equal(self.sequence, recordFromString.sequence)

    def test_reverse_complement1(self):
        assert_equal(self.rc1_record.header, self.rc_header)
        assert_equal(self.rc1_record.sequence, self.rc_sequence)
        assert_equal(self.rc1_expected__str__, str(self.rc1_record))

    def test_reverse_complement2(self):
        assert_equal(self.rc2_record.header, self.header)
        assert_equal(self.rc2_record.sequence, self.rc_sequence)
        assert_equal(self.rc2_expected__str__, str(self.rc2_record))

    def test_len(self):
        assert_equal(self.length, len(self.record))
        assert_equal(self.length, len(self.rc1_record))
        assert_equal(self.length, len(self.rc2_record))

    def test_eq(self):
        header = 'r1'
        seq = 'ACGT'
        r1 = FastaRecord(header, seq)
        r2 = FastaRecord(header, seq)
        assert_true(r1 == r2)

    def test_not_equal(self):
        r1 = FastaRecord('r1', 'ACGT')
        r2 = FastaRecord('r2', 'ACGT')
        r3 = FastaRecord('r1', 'ACGT')
        assert_true(r1 != r2)
        assert_false(r1 != r3)


class TestFastaReader:

    def test_readFasta(self):
        f = FastaReader(data.getFasta())
        entries = list(f)
        assert_equal(48, len(entries))
        assert_equal("ref000001|EGFR_Exon_2", entries[0].header)
        assert_equal("TTTCTTCCAGTTTGCCAAGGCACGAGTAACAAGCTCACGCAGTTGGGCACTTT"
                     "TGAAGATCATTTTCTCAGCCTCCAGAGGATGTTCAATAACTGTGAGGTGGTCC"
                     "TTGGGAATTTGGAAATTACCTATGTGCAGAGGAATTATGATCTTTCCTTCTTA"
                     "AAGGTTGGTGACTTTGATTTTCCT",
                     entries[0].sequence)

    def test_dosLineEndingsFasta(self):
        f = FastaReader(data.getDosFormattedFasta())
        entries = list(f)
        for e in entries:
            assert_true("\r" not in e.header)
            assert_equal(16, len(e.sequence))



class TestFastaWriter:

    def setup(self):
        self.fasta1 = StringIO(
            ">chr1|blah|blah\n"                                              \
            "GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATT\n" \
            "ACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAG\n" \
            "ATTACAGATTACAGATTACA\n")
        self.fasta2 = StringIO(self.fasta1.getvalue() + "\n" +               \
            ">chr2|blah|blah\n"                                              \
            "GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATT\n" \
            "ACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAG\n" \
            "ATTACAGATTACAGATTACA\n")

    def test_writeFasta1(self):
        f = StringIO()
        w = FastaWriter(f)
        for record in FastaReader(self.fasta1):
            w.writeRecord(record)
        assert_equal(self.fasta1.getvalue(), f.getvalue())

    def test_writeFasta2(self):
        f = StringIO()
        w = FastaWriter(f)
        for record in FastaReader(self.fasta1):
            w.writeRecord(record.header, record.sequence)
        assert_equal(self.fasta1.getvalue(), f.getvalue())
