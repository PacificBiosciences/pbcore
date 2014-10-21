from nose.tools import assert_equal, assert_true, assert_false
from numpy.testing import assert_array_equal
from pbcore import data
from StringIO import StringIO

from pbcore.io.FastqIO import *


# Test QV <-> string conversion routines
class TestQvConversion:
    def setup(self):
        self.ascii = \
            "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`" + \
            "abcdefghijklmnopqrstuvwxyz{|}~"
        self.qvs = range(0, 94)

    def testAsciiFromQvs(self):
        assert_equal(self.ascii, asciiFromQvs(self.qvs))

    def testQvsFromAscii(self):
        assert_array_equal(self.qvs, qvsFromAscii(self.ascii))


class TestFastqRecord:

    def setup(self):
        self.name = "chr1|blah|blah"
        self.rc_name = "chr1|blah|blah [revcomp]"
        self.sequence = "GATTACA" * 20
        self.rc_sequence = "TGTAATC" * 20
        self.quality  = [10,11,12,13,14,15,16] * 20
        self.rc_quality = [16,15,14,13,12,11,10] * 20
        self.qualityString = "+,-./01" * 20
        self.rc_qualityString = "10/.-,+" * 20
        self.expected__str__ =                                              \
            "@chr1|blah|blah\n"                                             \
            "GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATT"  \
            "ACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAG"  \
            "ATTACAGATTACAGATTACA\n"                                        \
            "+\n"                                                           \
            "+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-."  \
            "/01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+"  \
            ",-./01+,-./01+,-./01"
        self.rc1_expected__str__ =                                           \
            "@chr1|blah|blah [revcomp]\n"                                             \
            "TGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTA"  \
            "ATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCT"  \
            "GTAATCTGTAATCTGTAATC\n"                                        \
            "+\n"                                                           \
            "10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/."  \
            "-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+1"  \
            "0/.-,+10/.-,+10/.-,+"
        self.rc2_expected__str__ =                                           \
            "@chr1|blah|blah\n"                                             \
            "TGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTA"  \
            "ATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCTGTAATCT"  \
            "GTAATCTGTAATCTGTAATC\n"                                        \
            "+\n"                                                           \
            "10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/."  \
            "-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+10/.-,+1"  \
            "0/.-,+10/.-,+10/.-,+"
        self.record = FastqRecord(self.name, self.sequence, self.quality)
        self.record2 = FastqRecord(self.name, self.sequence,
                                   qualityString=self.qualityString)
        self.rc1_record = self.record.reverseComplement()
        self.rc2_record = self.record.reverseComplement(True)

    def test__init__(self):
        assert_equal(self.name, self.record.name)
        assert_equal(self.sequence, self.record.sequence)
        assert_array_equal(self.quality, self.record.quality)
        assert_equal(self.record, self.record2)

    def test__str__(self):
        assert_equal(self.expected__str__, str(self.record))

    def test_fromString(self):
        recordFromString = FastqRecord.fromString(self.expected__str__)
        assert_equal(self.name, recordFromString.name)
        assert_equal(self.sequence, recordFromString.sequence)
        assert_array_equal(self.quality, recordFromString.quality)

    def test_reverse_complement(self):
        assert_equal(self.rc1_record.name, self.rc_name)
        assert_equal(self.rc1_record.sequence, self.rc_sequence)
        assert_equal(self.rc1_record.quality, self.rc_quality)
        assert_equal(self.rc1_record.qualityString, self.rc_qualityString)
        assert_equal(str(self.rc1_record), self.rc1_expected__str__)

    def test_reverse_complement(self):
        assert_equal(self.rc2_record.name, self.record.name)
        assert_equal(self.rc2_record.sequence, self.rc_sequence)
        assert_equal(self.rc2_record.quality, self.rc_quality)
        assert_equal(self.rc2_record.qualityString, self.rc_qualityString)
        assert_equal(str(self.rc2_record), self.rc2_expected__str__)

    def test_eq(self):
        name = 'r1'
        seq = 'ACGT'
        qvs = list(xrange(10, 10 + len(seq)))
        r1 = FastqRecord(name, seq, qvs)
        r2 = FastqRecord(name, seq, qvs)
        assert_true(r1 == r2)
        assert_false(r1 != r2)

    def test_not_equal(self):
        name = 'r1'
        seq = 'ACGT'
        qvs = list(xrange(10, 10 + len(seq)))
        r1 = FastqRecord(name, seq, qvs)
        r2 = FastqRecord('r2', seq, qvs)
        assert_true(r1 != r2)


class TestFastqReader:

    def setup(self):
        self.fastq1 = StringIO("@seq1\n"   +
                               "GATTACA\n" +
                               "+\n"       +
                               "789:;<=\n")
        self.fastq2 = StringIO(self.fastq1.getvalue() +
                               "@seq2\n"   +
                               "CATTAGA\n" +
                               "+\n"       +
                               "@@@@@@@\n")

    def test_readFastq1(self):
        r1 = FastqReader(self.fastq1)
        l = list(r1)
        assert_equal([FastqRecord("seq1", "GATTACA", range(22, 29))], l)

    def test_readFastq2(self):
        r2 = FastqReader(self.fastq2)
        l = list(r2)
        assert_equal([FastqRecord("seq1", "GATTACA", range(22, 29)),
                      FastqRecord("seq2", "CATTAGA", [31]*7) ],
                     l)


class TestFastqWriter:

    def setup(self):
        self.fastq1 = StringIO("@seq1\n"   +
                               "GATTACA\n" +
                               "+\n"       +
                               "789:;<=\n")
        self.fastq2 = StringIO(self.fastq1.getvalue() +
                               "@seq2\n"   +
                               "CATTAGA\n" +
                               "+\n"       +
                               "@@@@@@@\n")

    def test_writeFastq1(self):
        f = StringIO()
        w = FastqWriter(f)
        for record in FastqReader(self.fastq1):
            w.writeRecord(record)
        assert_equal(self.fastq1.getvalue(), f.getvalue())

    def test_writeFastq2(self):
        f = StringIO()
        w = FastqWriter(f)
        for record in FastqReader(self.fastq2):
            w.writeRecord(record)
        assert_equal(self.fastq2.getvalue(), f.getvalue())

    def test_writeFastq3(self):
        f = StringIO()
        w = FastqWriter(f)
        for record in FastqReader(self.fastq2):
            w.writeRecord(record.name, record.sequence, record.quality)
        assert_equal(self.fastq2.getvalue(), f.getvalue())
