
"""
A corner case: reference sequence contains IUPAC ambiguous nucleotide
characters, which we allow.  This test ensures that we can extract the
transcript from a BAM alignment file, specifically when the reverse complement
is needed.
"""

import pbcore.io
import pysam
import tempfile
import unittest
import shutil
import os

sam_str_ = """\
@HD	VN:1.5\tSO:coordinate\tpb:3.0.1
@SQ\tSN:genome\tLN:28\tM5:734d5f3b2859595f4bd87a2fe6b7389b
@RG\tID:1\tPL:PACBIO\tDS:READTYPE=SUBREAD;DeletionQV=dq;DeletionTag=dt;InsertionQV=iq;MergeQV=mq;SubstitutionQV=sq;Ipd=ip;BASECALLERVERSION=2.0.1.0.123678;FRAMERATEHZ=75.000000;BINDINGKIT=foo;SEQUENCINGKIT=bar\tPU:movie1
@PG\tID:bax2bam-0.0.2\tPN:bax2bam\tVN:0.0.2\tDS:bax2bam
movie1/54130/0_10\t16\tgenome\t12\t30\t10=\t*\t0\t-28\tTCTCAGGAGA\t*\tRG:Z:1\tdq:Z:2222'$22'2\tdt:Z:NNNNAGNNGN\tip:B:C,255,2,0,10,22,34,0,2,3,0,16\tiq:Z:(+#1'$#*1&\tmq:Z:&1~51*5&~2\tnp:i:1\tqe:i:10\tqs:i:0\trq:f:0.854\tsn:B:f,-1,-1,-1,-1\tsq:Z:<32<4<<<<3\tzm:i:54130\tAS:i:-3020\tNM:i:134\tcx:i:2"""

fasta_str = """\
>genome
AAAATGASGAGATCARAATGASGAGATC"""
fai_str = """genome  28      8       28      29"""

class TestCase (unittest.TestCase):
    def setUp (self):
        f = open("tst_pbcore.sam", "w")
        f.write(sam_str_)
        f.close()
        # convert to bam using pysam
        sam_in = pysam.AlignmentFile("tst_pbcore.sam", "r")
        bam_out = pysam.AlignmentFile("tst_pbcore.bam", "wb",
            template=sam_in)
        for s in sam_in:
            bam_out.write(s)
        bam_out.close()
        open("tst_pbcore.fa", "w").write(fasta_str)
        open("tst_pbcore.fa.fai", "w").write(fai_str)

    def tearDown (self):
        os.remove("tst_pbcore.sam")
        os.remove("tst_pbcore.bam")
        os.remove("tst_pbcore.fa")
        os.remove("tst_pbcore.fa.fai")

    def test_reverse_complement (self):
        bam_file = pbcore.io.BamReader("tst_pbcore.bam",
            referenceFastaFname="tst_pbcore.fa")
        for aln in bam_file:
            seq = aln.transcript()

if __name__ == "__main__":
    tmp_dir = tempfile.mkdtemp()
    cwd = os.getcwd()
    os.chdir(tmp_dir)
    try:
        unittest.main()
    finally:
        os.chdir(cwd)
        shutil.rmtree(tmp_dir)
