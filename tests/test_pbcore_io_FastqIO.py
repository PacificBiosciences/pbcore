from numpy.testing import assert_array_equal
from io import StringIO

from pbcore import data
from pbcore.io.FastqIO import *


# Test QV <-> string conversion routines
class TestQvConversion:

    ASCII = (r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`"""
             r"""abcdefghijklmnopqrstuvwxyz{|}~""")

    QVS = range(0, 94)

    def testAsciiFromQvs(self):
        assert self.ASCII == asciiFromQvs(self.QVS)

    def testQvsFromAscii(self):
        assert_array_equal(self.QVS, qvsFromAscii(self.ASCII))


class TestFastqRecord:

    HEADER = "chr1|blah|blah\tblah blah"
    RC_HEADER = "chr1|blah|blah\tblah blah [revcomp]"
    ID = "chr1|blah|blah"
    COMMENT = "blah blah"
    SEQUENCE = "GATTACA" * 20
    RC_SEQUENCE = "TGTAATC" * 20
    LENGTH = 140
    QUALITY  = [10,11,12,13,14,15,16] * 20
    RC_QUALITY = [16,15,14,13,12,11,10] * 20
    QUALITYSTRING = "+,-./01" * 20
    RC_QUALITYSTRING = "10/.-,+" * 20
    EXPECTED__STR__ = (
        "@chr1|blah|blah\tblah blah\n"
        "GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATT"
        "ACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAG"
        "ATTACAGATTACAGATTACA\n"
        "+\n"
        "+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-."
        "/01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+"
        ",-./01+,-./01+,-./01")
    RC1_EXPECTED__STR__ = (
        "@chr1|blah|blah\tblah blah [revcomp]\n"
        "TGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTA"
        "ATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCT"
        "GTAATCTGTAATCTGTAATC\n"
        "+\n"
        "10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/."
        "-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+1"
        "0/.-,+10/.-,+10/.-,+")
    RC2_EXPECTED__STR__ = (
        "@chr1|blah|blah\tblah blah\n"
        "TGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTA"
        "ATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCT"
        "GTAATCTGTAATCTGTAATC\n"
        "+\n"
        "10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/."
        "-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+1"
        "0/.-,+10/.-,+10/.-,+")

    @classmethod
    def setup_class(cls):
        cls.record = FastqRecord(cls.HEADER, cls.SEQUENCE, cls.QUALITY)
        cls.record2 = FastqRecord(cls.HEADER, cls.SEQUENCE, qualityString=cls.QUALITYSTRING)
        cls.rc1_record = cls.record.reverseComplement()
        cls.rc2_record = cls.record.reverseComplement(True)

    def test__init__(self):
        assert self.HEADER == self.record.header
        assert self.SEQUENCE == self.record.sequence
        assert self.ID == self.record.id
        assert self.COMMENT == self.record.comment
        assert_array_equal(self.QUALITY, self.record.quality)
        assert self.record == self.record2

    def test__str__(self):
        assert self.EXPECTED__STR__ == str(self.record)

    def test_fromString(self):
        recordFromString = FastqRecord.fromString(self.EXPECTED__STR__)
        assert self.HEADER == recordFromString.header
        assert self.SEQUENCE == recordFromString.sequence
        assert_array_equal(self.QUALITY, recordFromString.quality)

    def test_reverse_complement1(self):
        assert self.rc1_record.header == self.RC_HEADER
        assert self.rc1_record.sequence == self.RC_SEQUENCE
        assert self.rc1_record.quality == self.RC_QUALITY
        assert self.rc1_record.qualityString == self.RC_QUALITYSTRING
        assert str(self.rc1_record) == self.RC1_EXPECTED__STR__

    def test_reverse_complement2(self):
        assert self.rc2_record.header == self.record.header
        assert self.rc2_record.sequence == self.RC_SEQUENCE
        assert self.rc2_record.quality == self.RC_QUALITY
        assert self.rc2_record.qualityString == self.RC_QUALITYSTRING
        assert str(self.rc2_record) == self.RC2_EXPECTED__STR__

    def test_len(self):
        assert self.LENGTH == len(self.record)
        assert self.LENGTH == len(self.rc1_record)
        assert self.LENGTH == len(self.rc2_record)

    def test_eq(self):
        header = 'r1'
        seq = 'ACGT'
        qvs = list(range(10, 10 + len(seq)))
        r1 = FastqRecord(header, seq, qvs)
        r2 = FastqRecord(header, seq, qvs)
        assert r1 == r2
        assert not r1 != r2

    def test_not_equal(self):
        header = 'r1'
        seq = 'ACGT'
        qvs = list(range(10, 10 + len(seq)))
        r1 = FastqRecord(header, seq, qvs)
        r2 = FastqRecord('r2', seq, qvs)
        assert r1 != r2


class TestFastqReader:

    FASTQ1 = StringIO(
        "@seq1\n"
        "GATTACA\n"
        "+\n"
        "789:;<=\n")
    FASTQ2 = StringIO(
        FASTQ1.getvalue() +
        "@seq2\n"
        "CATTAGA\n"
        "+\n"
        "@@@@@@@\n")

    def test_readFastq1(self):
        r1 = FastqReader(self.FASTQ1)
        l = list(rec for rec in r1)
        assert [FastqRecord("seq1", "GATTACA", range(22, 29))] == l

    def test_readFastq2(self):
        r2 = FastqReader(self.FASTQ2)
        l = list(rec for rec in r2)
        assert [FastqRecord("seq1", "GATTACA", range(22, 29)),
                FastqRecord("seq2", "CATTAGA", [31]*7) ] == l


class TestFastqWriter:

    def setup_method(self):
        self.fastq1 = StringIO(
            "@seq1\n"
            "GATTACA\n"
            "+\n"
            "789:;<=\n")
        self.fastq2 = StringIO(
            self.fastq1.getvalue() +
            "@seq2\n"
            "CATTAGA\n"
            "+\n"
            "@@@@@@@\n")

    def test_writeFastq1(self):
        f = StringIO()
        w = FastqWriter(f)
        for record in FastqReader(self.fastq1):
            w.writeRecord(record)
        assert self.fastq1.getvalue() == f.getvalue()

    def test_writeFastq2(self):
        f = StringIO()
        w = FastqWriter(f)
        for record in FastqReader(self.fastq2):
            w.writeRecord(record)
        assert self.fastq2.getvalue() == f.getvalue()

    def test_writeFastq3(self):
        f = StringIO()
        w = FastqWriter(f)
        for record in FastqReader(self.fastq2):
            w.writeRecord(record.header, record.sequence, record.quality)
        assert self.fastq2.getvalue() == f.getvalue()
