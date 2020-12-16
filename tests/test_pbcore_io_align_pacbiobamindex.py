
from pbcore.io.align.PacBioBamIndex import get_index_size_bytes
from pbcore.io import openDataSet, PacBioBamIndex
import pbcore.data


class TestPacBioBamIndex:

    def test_get_index_size_bytes(self):
        import pbtestdata
        ds = openDataSet(pbtestdata.get_file("subreads-sequel"))
        assert get_index_size_bytes(ds.externalResources[0].pbi) == 580
        ds2 = openDataSet(pbtestdata.get_file("ccs-barcoded"))
        assert get_index_size_bytes(ds2.externalResources[0].pbi) == 68
        ds3 = openDataSet(pbtestdata.get_file("aligned-xml"))
        assert get_index_size_bytes(ds3.externalResources[0].pbi) == 7504

    def test_read_mapped_subreads_pbi(self):
        bam_file = pbcore.data.getAlignedBam()
        pbi_file = bam_file + ".pbi"
        pbi = PacBioBamIndex(pbi_file)
        assert pbi.hasMappingEventInfo
        pbi_file_v3 = bam_file + ".pbi.v3"
        pbi3 = PacBioBamIndex(pbi_file_v3)
        assert not pbi3.hasMappingEventInfo
        assert (pbi3.nMM == pbi.nMM).all()
        assert (pbi3.qStart == pbi.qStart).all()
        assert (pbi3.identity == pbi.identity).all()
