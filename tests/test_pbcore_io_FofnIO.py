from __future__ import absolute_import, division, print_function

from io import StringIO
import os

from pbcore import data
from pbcore.io import readFofn

def test_simple():
    fofn = StringIO("/a/b\n/c/d")
    lst = list(readFofn(fofn))
    assert ["/a/b", "/c/d"] == lst

def test_empty_lines():
    fofn = StringIO(u"/a/b\n \n/c/d\n ")
    lst = list(readFofn(fofn))
    assert ["/a/b", "/c/d"] == lst

def test_absolutifying():
    for fofnPath in data.getFofns():
        for filePath in readFofn(fofnPath):
            assert os.path.isabs(filePath)
