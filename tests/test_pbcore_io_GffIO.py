
from StringIO import StringIO
import unittest
import os.path

from nose.tools import assert_equal, assert_raises

from pbcore.io import GffWriter, Gff3Record, GffReader
from pbcore.io.GffIO import merge_gffs, merge_gffs_sorted, sort_gff
from pbcore import data

def rm_out(fname):
    if os.path.exists(fname):
        os.remove(fname)

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


class TestGffSorting(unittest.TestCase):
    gff_data = ["""\
##gff-version 3
##source ipdSummary
##source-commandline ipdSummary etc.
##sequence-region lambda_NEB3011 1 48502
chr1\tkinModCall\tmodified_base\t32580\t32580\t32\t-\t.\tcoverage=94;context=AATGGCATCGTTCCGGTGGTGGGCGTTGATGGCTGGTCCCG;IPDRatio=1.75
chr1\tkinModCall\tmodified_base\t32766\t32766\t42\t-\t.\tcoverage=170;context=GCTGGGAAGCTGGCTGAACGTGTCGGCATGGATTCTGTCGA;IPDRatio=1.70
chr1\tkinModCall\tmodified_base\t32773\t32773\t54\t-\t.\tcoverage=154;context=AACGCTGGCTGGGAAGCTGGCTGAACGTGTCGGCATGGATT;IPDRatio=2.65""", """\
##gff-version 3
##source ipdSummary
##source-commandline ipdSummary etc.
##sequence-region lambda_NEB3011 1 48502
chr2\tkinModCall\tmodified_base\t1200\t1200\t47\t-\t.\tcoverage=109;context=ACTTTTCACGGTAGTTTTTTGCCGCTTTACCGCCCAGGCAC;IPDRatio=1.89
chr2\tkinModCall\tmodified_base\t1786\t1786\t36\t-\t.\tcoverage=153;context=TCCCACGTCTCACCGAGCGTGGTGTTTACGAAGGTTTTACG;IPDRatio=1.67
chr2\tkinModCall\tmodified_base\t1953\t1953\t39\t+\t.\tcoverage=148;context=AATGCGCGTATGGGGATGGGGGCCGGGTGAGGAAAGCTGGC;IPDRatio=1.86""", """\
chr1\tkinModCall\tmodified_base\t16204\t16204\t31\t-\t.\tcoverage=119;context=CCCGCGCAGATGATAATTACGGCTCACCTGCTGGCTGCCGA;IPDRatio=1.80
chr1\tkinModCall\tmodified_base\t16302\t16302\t33\t+\t.\tcoverage=108;context=TGGGACGGAACGTTTAAACCGGCATACAGCAACAACATGGC;IPDRatio=1.81
chr1\tkinModCall\tmodified_base\t16348\t16348\t42\t-\t.\tcoverage=115;context=CCCCATGCCGTAGCGCGGATGGGTCAGCATATCCCACAGAC;IPDRatio=1.82""",]
    sorted_start = [
        ('chr1', 16204), ('chr1', 16302), ('chr1', 16348),
        ('chr1', 32580), ('chr1', 32766), ('chr1', 32773),
        ('chr2', 1200), ('chr2', 1786), ('chr2', 1953),
    ]

    @classmethod
    def setUpClass(cls):
        cls.files = []
        cls.combined = "tmp_pbcore_all.gff"
        with open(cls.combined, "w") as f_all:
            for i in range(3):
                file_name = "tmp_pbcore_%d.gff" % i
                with open(file_name, "w") as f:
                    f.write(cls.gff_data[i])
                cls.files.append(file_name)
                for line in cls.gff_data[i].splitlines():
                    if line.startswith("#"):
                        if i == 0:
                            f_all.write(line+"\n")
                    else:
                        f_all.write(line+"\n")

    @classmethod
    def tearDownClass(cls):
        for file_name in cls.files:
            if os.path.exists(file_name):
                os.remove(file_name)
        if os.path.exists(cls.combined):
            os.remove(cls.combined)

    def test_merge_gffs(self):
        gff_out = "tmp_pbcore_merge.gff"
        merge_gffs(self.files, gff_out)
        n_rec = 0
        for fn in self.files:
            with GffReader(fn) as f:
                n_rec += len([ rec for rec in f ])
        with GffReader(gff_out) as f:
            self.assertEqual(f.headers, [
                "##gff-version 3",
                "##source ipdSummary",
                "##sequence-region lambda_NEB3011 1 48502",
            ])
            n_rec_merged = len([ rec for rec in f ])
            self.assertEqual(n_rec, n_rec_merged)
        rm_out(gff_out)

    def test_merge_gffs_sorted(self):
        gff_out = "tmp_pbcore_merged_sorted.gff"
        merge_gffs_sorted(self.files, gff_out)
        with GffReader(gff_out) as f:
            start = [ (rec.seqid, rec.start) for rec in f ]
            self.assertEqual(start, self.sorted_start)
        rm_out(gff_out)

    def test_sort_gff(self):
        gff_out = sort_gff(self.combined)
        with GffReader(gff_out) as f:
            start = [ (rec.seqid, rec.start) for rec in f ]
            self.assertEqual(start, self.sorted_start)
        rm_out(gff_out)
