from pbcore import data
from pbcore.io import FastaReader, FastaWriter, FastaRecord
from io import StringIO

class TestFastaRecord(object):

    HEADER = "chr1|blah|blah\tblah blah"
    RC_HEADER = "chr1|blah|blah\tblah blah [revcomp]"
    ID = "chr1|blah|blah"
    COMMENT = "blah blah"
    SEQUENCE = "GATTACA" * 20
    RC_SEQUENCE = "TGTAATC" * 20
    LENGTH = 140
    EXPECTED__STR__ = (
        ">chr1|blah|blah\tblah blah\n"
        "GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATT\n"
        "ACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAG\n"
        "ATTACAGATTACAGATTACA")
    RC1_EXPECTED__STR__ = (
        ">chr1|blah|blah\tblah blah [revcomp]\n"
        "TGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTA\n"
        "ATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCT\n"
        "GTAATCTGTAATCTGTAATC")
    RC2_EXPECTED__STR__ = (
        ">chr1|blah|blah\tblah blah\n"
        "TGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTA\n"
        "ATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCT\n"
        "GTAATCTGTAATCTGTAATC")

    @classmethod
    def setup_class(cls):
        cls.record = FastaRecord(cls.HEADER, cls.SEQUENCE)
        cls.rc1_record = cls.record.reverseComplement()
        cls.rc2_record = cls.record.reverseComplement(True)

    def test__init__(self):
        assert self.HEADER == self.record.header
        assert self.SEQUENCE == self.record.sequence
        assert self.ID == self.record.id
        assert self.COMMENT == self.record.comment

    def test__str__(self):
        assert self.EXPECTED__STR__ == str(self.record)

    def test_fromString(self):
        recordFromString = FastaRecord.fromString(self.EXPECTED__STR__)
        assert self.HEADER == recordFromString.header
        assert self.SEQUENCE == recordFromString.sequence

    def test_reverse_complement1(self):
        assert self.rc1_record.header == self.RC_HEADER
        assert self.rc1_record.sequence == self.RC_SEQUENCE
        assert self.RC1_EXPECTED__STR__ == str(self.rc1_record)

    def test_reverse_complement2(self):
        assert self.rc2_record.header == self.HEADER
        assert self.rc2_record.sequence == self.RC_SEQUENCE
        assert self.RC2_EXPECTED__STR__ == str(self.rc2_record)

    def test_len(self):
        assert self.LENGTH == len(self.record)
        assert self.LENGTH == len(self.rc1_record)
        assert self.LENGTH == len(self.rc2_record)

    def test_eq(self):
        header = 'r1'
        seq = 'ACGT'
        r1 = FastaRecord(header, seq)
        r2 = FastaRecord(header, seq)
        assert r1 == r2

    def test_not_equal(self):
        r1 = FastaRecord('r1', 'ACGT')
        r2 = FastaRecord('r2', 'ACGT')
        r3 = FastaRecord('r1', 'ACGT')
        assert r1 != r2
        assert not r1 != r3


class TestFastaReader(object):

    def test_readFasta(self):
        f = FastaReader(data.getFasta())
        entries = list(f)
        assert 48 == len(entries)
        assert "ref000001|EGFR_Exon_2" == entries[0].header
        assert ("TTTCTTCCAGTTTGCCAAGGCACGAGTAACAAGCTCACGCAGTTGGGCACTTT"
                "TGAAGATCATTTTCTCAGCCTCCAGAGGATGTTCAATAACTGTGAGGTGGTCC"
                "TTGGGAATTTGGAAATTACCTATGTGCAGAGGAATTATGATCTTTCCTTCTTA"
                "AAGGTTGGTGACTTTGATTTTCCT") == entries[0].sequence

    def test_dosLineEndingsFasta(self):
        f = FastaReader(data.getDosFormattedFasta())
        entries = list(f)
        for e in entries:
            assert "\r" not in e.header
            assert 16 == len(e.sequence)


class TestFastaWriter(object):

    def setup_method(self):
        self.fasta1 = StringIO(
            ">chr1|blah|blah\n"
            "GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATT\n"
            "ACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAG\n"
            "ATTACAGATTACAGATTACA\n")
        self.fasta2 = StringIO(self.fasta1.getvalue() +
            ">chr2|blah|blah\n"
            "GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATT\n"
            "ACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAG\n"
            "ATTACAGATTACAGATTACA\n")

    def test_writeFasta1(self):
        f = StringIO()
        w = FastaWriter(f)
        for record in FastaReader(self.fasta1):
            w.writeRecord(record)
        assert self.fasta1.getvalue() == f.getvalue()

    def test_writeFasta2(self):
        f = StringIO()
        w = FastaWriter(f)
        for record in FastaReader(self.fasta2):
            w.writeRecord(record.header, record.sequence)
        assert self.fasta2.getvalue() == f.getvalue()
