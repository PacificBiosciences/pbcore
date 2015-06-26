
# FIXME This is not compatible with running nosetests on everything at once!

# Test for hack to support lossless pulse feature encoding (e.g. Ipd).
# XXX this should be kept in some form, but the hope is that changes in pysam
# will make the environment variable hack unnecessary in the future.

import subprocess
import unittest
from unittest.case import SkipTest
import os
os.environ["PBCORE_BAM_LOSSLESS_KINETICS"] = "1"

import pysam

import pbcore.io.align.BamAlignment
pbcore.io.align.BamAlignment.PBCORE_BAM_LOSSLESS_KINETICS = "1"

class TestCase (unittest.TestCase):
    sam_str_ = """\
@HD\tVN:1.5\tSO:coordinate\tpb:3.0b5
@SQ\tSN:ecoliK12_pbi_March2013_2955000_to_2980000\tLN:25000\tM5:734d5f3b2859595f4bd87a2fe6b7389b
@RG\tID:3f58e5b8\tPL:PACBIO\tDS:READTYPE=SUBREAD;DeletionQV=dq;DeletionTag=dt;InsertionQV=iq;MergeQV=mq;SubstitutionQV=sq;Ipd=ip;BASECALLERVERSION=2.0.1.0.123678;FRAMERATEHZ=75.000000;BINDINGKIT=foo;SEQUENCINGKIT=bar\tPU:movie1
@PG\tID:bax2bam-0.0.2\tPN:bax2bam\tVN:0.0.2\tDS:bax2bam\tCL:bax2bam in.bax.h5 out.bam
movie1/54130/0_10\t2\tecoliK12_pbi_March2013_2955000_to_2980000\t2\t10\t10M\t*\t0\t0\tAATGAGGAGA\t*\tRG:Z:3f58e5b8\tdq:Z:2222'$22'2\tdt:Z:NNNNAGNNGN\tip:B:S,275,2,0,10,22,349,0,2,3,16\tiq:Z:(+#1'$#*1&\tmq:Z:&1~51*5&~2\tnp:i:1\tqe:i:10\tqs:i:0\trq:i:854\tsn:B:f,2.0,2.0,2.0,2.0\tsq:Z:<32<4<<<<3\tzm:i:54130\tAS:i:-3020\tNM:i:134\tcx:i:2
movie1/54130/10_20\t2\tecoliK12_pbi_March2013_2955000_to_2980000\t12\t10\t10M\t*\t0\t0\tAATGAGGAGA\t*\tRG:Z:3f58e5b8\tdq:Z:2222'$22'2\tdt:Z:NNNNAGNNGN\tip:B:S,285,2,0,10,22,340,0,2,3,16\tiq:Z:(+#1'$#*1&\tmq:Z:&1~51*5&~2\tnp:i:1\tqe:i:20\tqs:i:10\trq:i:854\tsn:B:f,2.0,2.0,2.0,2.0\tsq:Z:<32<4<<<<3\tzm:i:54130\tAS:i:-3020\tNM:i:134\tcx:i:2"""

    def setUp (self):
        sam_file = "tmp_pbcore_io_subreads.sam"
        with open(sam_file, "w") as f:
            f.write(self.sam_str_)
        sam_in = pysam.AlignmentFile(sam_file, "r")
        bam_out = pysam.AlignmentFile(sam_file[:-3]+"bam", "wb",
            template=sam_in)
        for s in sam_in:
            bam_out.write(s)
        bam_out.close()

    def tearDown (self):
        os.remove("tmp_pbcore_io_subreads.sam")
        os.remove("tmp_pbcore_io_subreads.bam")

    @SkipTest
    def test_1 (self):
        file_name = "tmp_pbcore_io_subreads.bam"
        os.environ
        with pbcore.io.BamReader(file_name) as f:
            expected = [
                [275,2,0,10,22,349,0,2,3,16],
                [285,2,0,10,22,340,0,2,3,16],
            ]
            k = 0
            for a in f:
                ipd = list(a.IPD()) # we don't want the numpy array
                self.assertEqual(ipd, expected[k])
                k += 1

if __name__ == "__main__":
    unittest.main()
