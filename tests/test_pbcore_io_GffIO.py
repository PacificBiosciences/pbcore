from nose.tools import assert_equal, assert_raises
from StringIO import StringIO
from pbcore.io import GffWriter, Gff3Record, GffReader
from pbcore import data

class TestGff3Record:

    def setup(self):
        self.record = Gff3Record("chr1", 10, 11, "insertion",
                                 attributes=[("cat", "1"), ("dog", "2")])

    def test_str(self):
        assert_equal("chr1\t.\tinsertion\t10\t11\t.\t.\t.\tcat=1;dog=2",
                     str(self.record))

    def test_modification(self):
        record = self.record.copy()
        record.dog = 3
        record.cat = 4
        record.mouse = 5
        record.start = 100
        record.end = 110
        assert_equal("chr1\t.\tinsertion\t100\t110\t.\t.\t.\tcat=4;dog=3;mouse=5",
                     str(record))

    def test_fromString(self):
        newRecord = Gff3Record.fromString(str(self.record))
        assert_equal(str(self.record),  str(newRecord))

    def test_get(self):
        """
        Verify field access behavior
        """
        record = self.record
        record.dog = 3
        record.cat = 4
        record.mouse = 5
        record.start = 100
        record.end = 110

        assert_equal(3, record.dog)
        assert_equal(100, record.start)
        with assert_raises(AttributeError):
            record.god

        assert_equal(3, record.get("dog"))
        assert_equal(None, record.get("god"))
        assert_equal(100, record.get("start", 100))




class TestGffReader:
    def setup(self):
        self.rawFile = open(data.getGff3())
        self.reader = GffReader(data.getGff3())

    def test_headers(self):
        assert_equal(["##gff-version 3",
                      "##pacbio-variant-version 2.1",
                      "##date Sat Mar 22 12:16:13 2014",
                      "##feature-ontology http://song.cvs.sourceforge.net/*checkout*/song/ontology/sofa.obo?revision=1.12",
                      "##source GenomicConsensus 0.8.0",
                      "##source-commandline /Users/dalexander/.virtualenvs/VE/bin/variantCaller.py --algorithm=plurality -q20 -x5 pbcore/data/aligned_reads_1.cmp.h5 -r /Users/dalexander/Data/lambdaNEB.fa -o /tmp/v.gff",
                      "##source-alignment-file /Users/dalexander/Dropbox/Sources/git/pbcore/pbcore/data/aligned_reads_1.cmp.h5",
                      "##source-reference-file /Users/dalexander/Data/lambdaNEB.fa",
                      "##sequence-region lambda_NEB3011 1 48502"],
                     self.reader.headers)

    def test__iter__(self):
        records = list(self.reader)
        rawLines = self.rawFile.readlines()[9:]
        for record, rawLine in zip(records, rawLines):
            # No newlines or whitespace allowed in records
            assert_equal(str(record).strip(), str(record))
            # Make sure record matches line
            assert_equal(rawLine.strip(), str(record))


class TestGffWriter:
    def setup(self):
        self.outfile = StringIO()
        self.record1 = Gff3Record("chr1", 10, 11, "insertion",
                                  attributes=[("cat", "1"), ("dog", "2")])
        self.record2 = Gff3Record("chr1", 200, 201, "substitution",
                                  attributes=[("mouse", "1"), ("moose", "2")])
        self.gffWriter = GffWriter(self.outfile)

    def test_writeHeader(self):
        self.gffWriter.writeHeader("##foo bar")
        assert_equal("##gff-version 3\n##foo bar\n",
                     self.outfile.getvalue())

    def test_writeRecord(self):
        self.gffWriter.writeRecord(self.record1)
        self.gffWriter.writeRecord(self.record2)
        expected = ("##gff-version 3\n" +
                    "chr1\t.\tinsertion\t10\t11\t.\t.\t.\tcat=1;dog=2\n" +
                    "chr1\t.\tsubstitution\t200\t201\t.\t.\t.\tmouse=1;moose=2\n")
        assert_equal(expected, self.outfile.getvalue())
