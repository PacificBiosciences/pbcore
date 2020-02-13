import os.path
import tempfile
from textwrap import dedent

from pbcore.io import Vcf4Record
from pbcore.io.VcfIO import merge_vcfs_sorted


def rm_out(fname):
    if os.path.exists(fname):
        os.remove(fname)


class TestVcfSorting:

    VCF_META = dedent("""\
            ##fileformat=VCFv4.3
            ##fileDate=20170328
            ##source=GenomicConsensusV2.2.0
            ##reference=ecoliK12_pbi_March2013.fasta
            ##contig=<ID=ecoliK12_pbi_March2013,length=4642522>
            #CHROM POS ID REF ALT QUAL FILTER INFO""")
    VCF_RECS = [
        Vcf4Record.fromString(
            "ecoliK12_pbi_March2013\t84\t.\tTG\tT\t48\tPASS\tDP=53"),
        Vcf4Record.fromString(
            "ecoliK12_pbi_March2013\t218\t.\tGA\tG\t47\tPASS\tDP=58"),
        Vcf4Record.fromString("ecoliK12_pbi_March2013\t1536\t.\tG\tGC\t47\tPASS\tDP=91")]

    @classmethod
    def setup_class(cls):
        cls.files = []
        for i in range(2):
            file_name = "tmp_pbcore_%d.vcf" % i
            with open(file_name, "w") as f:
                print(cls.VCF_META, file=f)
                recs = cls.VCF_RECS[2:] if i == 0 else cls.VCF_RECS[:2]
                for r in recs:
                    print(str(r), file=f)
            cls.files.append(file_name)

    @classmethod
    def teardown_class(cls):
        for file_name in cls.files:
            if os.path.exists(file_name):
                os.remove(file_name)

    def test_merge_vcfs_sorted(self):
        vcf_out = "tmp_pbcore_merged_sorted.vcf"
        merge_vcfs_sorted(self.files, vcf_out)
        meta = []
        recs = []
        with open(vcf_out) as f:
            for l in f:
                l = l.strip()
                if not l:
                    continue
                elif l[0] == "#":
                    meta.append(l)
                else:
                    recs.append(Vcf4Record.fromString(l))
        assert self.VCF_META.strip().split('\n') == meta
        assert self.VCF_RECS == recs
        rm_out(vcf_out)
