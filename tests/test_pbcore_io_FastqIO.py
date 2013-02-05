from nose.tools import assert_equal
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
        self.sequence = "GATTACA" * 20
        self.quality  = [10,11,12,13,14,15,16] * 20
        self.qualityString = "+,-./01" * 20
        self.expected__str__ =                                              \
            "@chr1|blah|blah\n"                                             \
            "GATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATT"  \
            "ACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAGATTACAG"  \
            "ATTACAGATTACAGATTACA\n"                                        \
            "+\n"                                                           \
            "+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-."  \
            "/01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+,-./01+"  \
            ",-./01+,-./01+,-./01"
        self.record = FastqRecord(self.name, self.sequence, self.quality)
        self.record2 = FastqRecord(self.name, self.sequence,
                                   qualityString=self.qualityString)


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
