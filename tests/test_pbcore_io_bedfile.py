import unittest
import tempfile

from pbcore.io import parse_bed


class TestBedReader(unittest.TestCase):

    def test_parse_bed(self):
        BED = """\
chrX\t67545316\t67545385\tID=AR;MOTIFS=GCA;STRUC=(GCA)n
chr12\t6936716\t6936773\tID=ATN1;MOTIFS=CAG;STRUC=(CAG)n
chr6\t16327633\t16327723\tID=ATXN1;MOTIFS=TGC;STRUC=(TGC)n"""
        bed_file = tempfile.NamedTemporaryFile(suffix=".bed").name
        with open(bed_file, "wt") as bed_out:
            bed_out.write(BED)
        records = parse_bed(bed_file)
        assert len(records) == 3
        assert records[0].chr_start == 67545316 and records[0].chr_end == 67545385
