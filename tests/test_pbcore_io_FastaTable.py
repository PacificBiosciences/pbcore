from nose.tools import assert_equal, assert_raises
from pbcore import data
from pbcore.io import FastaTable, ReferenceTable
from StringIO import StringIO


class TestFastaTable:

    def test_readFluidigmFasta(self):
        expectedFirstNames = ['ref000001|EGFR_Exon_2',
                              'ref000002|EGFR_Exon_3',
                              'ref000003|EGFR_Exon_4']
        expectedFirstMD5s = ['e3912e9ceacd6538ede8c1b2adda7423',
                             '4bf218da37175a91869033024ac8f9e9',
                             '245bc7a046aad0788c22b071ed210f4d']
        ft = FastaTable(data.getFasta())
        assert_equal(48, len(ft))
        assert_equal(expectedFirstNames,
                     [ft[i].name for i in range(3)])
        assert_equal(expectedFirstMD5s,
                     [ft[i].md5 for i in range(3)])
        assert_equal(expectedFirstMD5s,
                     [ft.byMD5(md5).md5 for md5 in expectedFirstMD5s])
        assert_equal(expectedFirstNames,
                     [ft.byMD5(md5).name for md5 in expectedFirstMD5s])
        with assert_raises(KeyError):
            ft.byMD5(1)

class CmpH5Stub(object):
    def __init__(self, mapping):
        self.mapping = mapping

    def localReferenceIdMapping(self):
        return self.mapping

fluidigmAmpliconsSubsetCmpH5Stub = CmpH5Stub(
    {'04e53a5218ca88728241ba4af7db74bf': 28,
     '104194486deec30f906ea075bd06b74f': 24,
     '10bec442624e48fb3e44adb015daf01d': 44,
     '10d7c32b2e1be3cab4322fde54de350b': 11,
     '115bf6a40c3b5864277369b53e992b78': 26,
     '1848a590eb8aaee682c8f9d3243b763c': 31,
     '2054f599134b787d54c6d819945d0836': 19,
     '245bc7a046aad0788c22b071ed210f4d': 32,
     '2a87564a62f4cf212075af06882a588f': 9,
     '2da355d82ee932be5ca7e323dea03993': 20 })


class TestReferenceTable:

    def test_readFluidigmFasta(self):
        rt = ReferenceTable(data.getFasta(), fluidigmAmpliconsSubsetCmpH5Stub)
        assert_equal(10, len(rt))
        assert_equal("10d7c32b2e1be3cab4322fde54de350b", rt.byLocalId(11).md5)
        assert_equal("2da355d82ee932be5ca7e323dea03993", rt.byLocalId(20).md5)
        with assert_raises(KeyError):
            rt.byLocalId(1)
