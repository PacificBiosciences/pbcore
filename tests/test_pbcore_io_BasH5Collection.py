from nose.tools import assert_equal, assert_true, assert_false
from numpy.testing import assert_array_equal
from StringIO import StringIO

from pbcore.io import BasH5Collection
from pbcore import data

def lookupSomeReadsByName(bc):
    pass

def test():
    for fofn in data.getFofns():
        bc = BasH5Collection(fofn)

        for zmw in bc:
            zmwAgain = bc[zmw.zmwName]
            assert_equal(zmw.zmwName, zmwAgain.zmwName)



def test_read_iterators():
    for fofn in data.getFofns():
        bc = BasH5Collection(fofn)

        # TODO Add some meaningful tests here
        list(bc.subreads())
        list(bc.reads())
        list(bc.ccsReads())
