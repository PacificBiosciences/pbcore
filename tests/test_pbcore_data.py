from nose.tools import assert_equal
from pbcore import data

class TestGetCmpH5s(object):
    def test_get_cmp_h5s(self):
        for item in data.getCmpH5s():
            assert 'cmph5' in item
            assert 'bash5s' in item

class TestGetCmpH5(object):
    def test_get_cmp_h5(self):
        assert data.getCmpH5().endswith(".cmp.h5")
