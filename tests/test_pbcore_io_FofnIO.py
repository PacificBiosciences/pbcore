from nose.tools import assert_equal, assert_true, assert_false
from numpy.testing import assert_array_equal
from StringIO import StringIO
from os.path import isabs

from pbcore import data
from pbcore.io import readFofn

def test_simple():
    fofn = StringIO("/a/b\n/c/d")
    lst = list(readFofn(fofn))
    assert_array_equal(["/a/b", "/c/d"], lst)

def test_empty_lines():
    fofn = StringIO("/a/b\n \n/c/d\n ")
    lst = list(readFofn(fofn))
    assert_array_equal(["/a/b", "/c/d"], lst)

def test_absolutifying():
    for fofnPath in data.getFofns():
        for filePath in readFofn(fofnPath):
            assert_true(isabs(filePath))
