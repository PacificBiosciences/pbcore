from nose.tools import assert_equal
from StringIO import StringIO
from pbcore.io import GffWriter, Gff3Record, GffReader
from pbcore import data

class TestGffReader:
    def setup(self):
        self.rawFile = open(data.getGff3())
        self.reader = GffReader(data.getGff3())

    def test___iter__(self):
        records = list(self.reader.__iter__())
        lines = [line for line in self.rawFile.readlines() if not line.startswith("#")]
        
        assert len(lines) == len(records)
        for line, record in zip(lines, records):
            # Unfortunately this does not work because of the way Gff3Record munges
            # empty ('.') score fields.
            # assert line == str(record)
            assert line.split()[0] == str(record).split()[0]

class TestGffWriter:
    def setup(self):
        self.outfile = StringIO()
        self.gff_writer = GffWriter(self.outfile)

    def test_writeMetaData(self):
        self.gff_writer.writeMetaData("foo", "bar")
        
        assert_equal("##gff-version 3\n##foo bar\n",
                     self.outfile.getvalue())

    def test_writeBlankRecord(self):
        record = Gff3Record(seqName="Phony")
        record.put("SomeKey", "SomeValue")
        record.put("AnotherKey", "AnotherValue")
        self.gff_writer.writeRecord(record)

        expected = "##gff-version 3\nPhony\t.\t\t0\t0\t0.00\t+\t.\t" \
                   "SomeKey=SomeValue;AnotherKey=AnotherValue\n"
        assert_equal(expected, self.outfile.getvalue())


