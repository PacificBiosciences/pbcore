
from pbcore.io.align.PacBioBamIndex import get_index_size_bytes
from pbcore.io import openDataSet


class TestPacBioBamIndex:

    def test_get_index_size_bytes(self):
        import pbtestdata
        ds = openDataSet(pbtestdata.get_file("subreads-sequel"))
        assert get_index_size_bytes(ds.externalResources[0].pbi) == 580
        ds2 = openDataSet(pbtestdata.get_file("ccs-barcoded"))
        assert get_index_size_bytes(ds2.externalResources[0].pbi) == 68
        ds3 = openDataSet(pbtestdata.get_file("aligned-xml"))
        assert get_index_size_bytes(ds3.externalResources[0].pbi) == 7504
