from nose.tools import assert_equal

import numpy
from pbcore.io import cmph5
from pbcore import data

NUMERIC = ( int, numpy.uint32 )

class TestRevCompSeq:
    def test_rev_comp_seq(self):
        """TestRevComSeq.test_rev_comp_seq: Tests the reverse complement function we use in this package"""
        assert_equal("ACGTTGCA", cmph5.revCompSeq("TGCAACGT"))
        assert_equal("", cmph5.revCompSeq(""))
        assert_equal("AAAANNNN", cmph5.revCompSeq("NNNNTTTT"))

class TestBasename:
    def test_basename(self):
        """TestBasename.test_basename: Tests the basename utility function used to translate H5 paths to datasets/groups"""
        assert_equal( "Dataset", cmph5.basename("/Group/Group/Dataset"))
        assert_equal( "Dataset", cmph5.basename("Group/Dataset")) 

class TestAsPath:
    def test_as_path(self):
        """TestAsPath.test_as_path: Tests the utility function which converts a series of strings to an H5 path."""
        assert_equal( "/Group/Group/Dataset", cmph5.asPath("Group","Group","Dataset") )
        assert_equal( "/", cmph5.asPath("") )

