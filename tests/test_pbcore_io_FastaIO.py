from nose.tools import assert_equal, assert_true, assert_false
from pbcore import data
from pbcore.io import FastaReader, FastaWriter, FastaRecord
from StringIO import StringIO

class TestFastaRecord:

    def setup(self):
        self.name = "chr1|blah|blah\tblah blah"
        self.rc_name = "chr1|blah|blah\tblah blah [revcomp]"
        self.id = "chr1|blah|blah"
        self.metadata = "blah blah"
        self.sequence = "GATTACA" * 20
        self.rc_sequence = "TGTAATC" * 20
        self.expected__str__ =                                               \
            ">chr1|blah|blah\tblah blah\n"                                   \
            "GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATT\n" \
            "ACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAG\n" \
            "ATTACAGATTACAGATTACA"
        self.rc1_expected__str__ =                                           \
            ">chr1|blah|blah\tblah blah [revcomp]\n"                         \
            "TGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTA\n" \
            "ATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCT\n" \
            "GTAATCTGTAATCTGTAATC"
        self.rc2_expected__str__ =                                           \
            ">chr1|blah|blah\tblah blah\n"                                   \
            "TGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTA\n" \
            "ATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCT\n" \
            "GTAATCTGTAATCTGTAATC"
        self.record = FastaRecord(self.name, self.sequence)
        self.rc1_record = self.record.reverseComplement()
        self.rc2_record = self.record.reverseComplement(True)

    def test__init__(self):
        assert_equal(self.name, self.record.name)
        assert_equal(self.sequence, self.record.sequence)
        assert_equal(self.id, self.record.id)
        assert_equal(self.metadata, self.record.metadata)

    def test__str__(self):
        assert_equal(self.expected__str__, str(self.record))

    def test_fromString(self):
        recordFromString = FastaRecord.fromString(self.expected__str__)
        assert_equal(self.name, recordFromString.name)
        assert_equal(self.sequence, recordFromString.sequence)

    def test_md5(self):
        assert_equal("67fc75ce599ed0ca1fc8ed2dcbccc95d",
                     self.record.md5)

    def test_reverse_complement1(self):
        assert_equal(self.rc1_record.name, self.rc_name)
        assert_equal(self.rc1_record.sequence, self.rc_sequence)
        assert_equal(self.rc1_expected__str__, str(self.rc1_record))

    def test_reverse_complement2(self):
        assert_equal(self.rc2_record.name, self.name)
        assert_equal(self.rc2_record.sequence, self.rc_sequence)
        assert_equal(self.rc2_expected__str__, str(self.rc2_record))

    def test_eq(self):
        name = 'r1'
        seq = 'ACGT'
        r1 = FastaRecord(name, seq)
        r2 = FastaRecord(name, seq)
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
        assert_equal("ref000001|EGFR_Exon_2", entries[0].name)
        assert_equal("TTTCTTCCAGTTTGCCAAGGCACGAGTAACAAGCTCACGCAGTTGGGCACTTT"
                     "TGAAGATCATTTTCTCAGCCTCCAGAGGATGTTCAATAACTGTGAGGTGGTCC"
                     "TTGGGAATTTGGAAATTACCTATGTGCAGAGGAATTATGATCTTTCCTTCTTA"
                     "AAGGTTGGTGACTTTGATTTTCCT",
                     entries[0].sequence)
        assert_equal("e3912e9ceacd6538ede8c1b2adda7423",
                     entries[0].md5)

    def test_dosLineEndingsFasta(self):
        f = FastaReader(data.getDosFormattedFasta())
        entries = list(f)
        for e in entries:
            assert_true("\r" not in e.name)
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
            w.writeRecord(record.name, record.sequence)
        assert_equal(self.fasta1.getvalue(), f.getvalue())
