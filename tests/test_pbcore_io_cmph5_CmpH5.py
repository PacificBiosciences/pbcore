from nose.tools import assert_equal
from pbcore.io import cmph5
from pbcore.io.cmph5.CmpH5 import CmpH5, SFCmpH5, CmpH5Error
from pbcore import data
import numpy
import tempfile
import os

NUMERIC = ( int, numpy.uint32 )

class TestCmpH5:

    def setUp( self ):
        """Loads cmp.h5s from the package test data"""
        self.cmpH5s = dict([ ( mapping['cmph5'], cmph5.factory.create( mapping['cmph5'], 'r' ) ) for mapping in data.getCmpH5s( ) ])
                
    def tearDown( self ):
        """Simply closes the opened cmp.h5 files"""
        for cmpH5 in self.cmpH5s.values( ):
            cmph5.factory.close(cmpH5)
            # cmpH5.close( )
            # del cmpH5

    def test___contains__(self):
        """TestCmpH5.test__contains__"""
        for cmpH5 in self.cmpH5s.values( ):
            assert cmpH5.__contains__("/RefInfo")

    def test___del__(self):
        """TestCmpH5.test__del__"""
        try:
            tmpfn = tempfile.mkstemp(suffix="cmp.h5", dir="/tmp")[1]
            tmpfn = unicode(os.path.abspath(os.path.expanduser(tmpfn)))
            f = SFCmpH5( tmpfn, 'w', readType="standard" )
            del f
            os.remove(tmpfn)
        except:
            assert False
        else:
            assert True

    def test___getitem__(self):
        """TestCmpH5.test__getitem__"""
        for cmpH5 in self.cmpH5s.values( ):
            for k in cmpH5._items:
                assert cmpH5[k] == cmpH5._items[k]

    def test___iter__(self):
        for cmpH5 in self.cmpH5s.values( ):
            for x in cmpH5:
                assert isinstance(x, cmph5.CmpH5Group.RefGroup)

    def test_alnHitIterator(self):
        """TestCmpH5.test_alnHitIterator: Iterates over the alignment hits in the cmp.h5 files"""
        for cmpH5 in self.cmpH5s.values( ):
            for hit in cmpH5.alnHitIterator( ):
                assert isinstance( hit.alignedQuery, str )
                assert isinstance( hit.query_start, NUMERIC )

    def test_asRecArray(self):
        """TestCmpH5.test_asRecArray: Returns a large amount of per-alignment information using the 'asRecArray' interface"""
        for cmpH5 in self.cmpH5s.values( ):
            for name, hole, rStart, tStart, template in cmpH5.asRecArray( \
                           ["/MovieInfo/Name", "HoleNumber", "rStart", "tStart", "/RefInfo/FullName"]):
                assert isinstance( name, str )
                assert isinstance( hole, NUMERIC )
                assert isinstance( rStart, NUMERIC )
                assert isinstance( tStart, NUMERIC )
                assert isinstance( template, str )

    def test_numAlnHits(self):
        """TestCmpH5.test_numAlnHits: Tests the .numAlnHits property by asserting equality with the .numSubreads property"""
        for cmpH5 in self.cmpH5s.values( ):
            assert cmpH5.numAlnHits == cmpH5.numSubreads

    def test_numReads(self):
        """TestCmpH5.test_numReads: Tests the quick utility function that grabs the total # of aligned reads from a cmp.h5"""
        for path, cmpH5 in self.cmpH5s.iteritems( ):
            assert isinstance( cmpH5.numReads, NUMERIC )

    def test_numSubreads(self):
        """TestCmpH5.test_numSubreads: Tests the .numAlnHits property by asserting equality with the .numSubreads property"""
        for cmpH5 in self.cmpH5s.values( ):
            assert cmpH5.numAlnHits == cmpH5.numSubreads

    def test_refGroupIterator(self):
        """TestCmpH5.test_refGroupIterator: Tests iteration over reference groups"""
        for cmpH5 in self.cmpH5s.values( ):
            for refGroup in cmpH5.refGroupIterator( ):
                assert isinstance( refGroup, cmph5.CmpH5Group.RefGroup )

    def test_refInfoIterator(self):
        """TestCmpH5.test_refInfoIterator: Tests iteration over reference annotation objects"""
        for cmpH5 in self.cmpH5s.values( ):
            for refInfo in cmpH5.refInfoIterator( ):
                assert isinstance( refInfo, cmph5.CmpH5.ReferenceAnnotation )
                assert isinstance( refInfo.fullName, str )
                assert isinstance( refInfo.length, NUMERIC )

class TestSFCmpH5:

    def test___init__(self):
        tmpf = tempfile.mkstemp(suffix=".cmp.h5", dir="/tmp")
        try:
            cmp_h5 = SFCmpH5(tmpf[1], 'w', readType="standard")
        except:
            assert False
        else:
            assert True
        finally:
            del cmp_h5
            os.remove(tmpf[1])

    # These tests elicit segfaults on OS X---may be due to undefined
    # behavior in h5py.  Since the CmpH5 APIS are now essentially
    # deprecated in favor of CmpH5Reader, I am commenting them out.
    #   - dalexander, 6/22/12
            
    # def test_addAlnGroup(self):
    #     tmpf = tempfile.mkstemp(suffix=".cmp.h5", dir="/tmp")
    #     cmp_h5 = SFCmpH5(tmpf[1], 'w', readType="standard")
    #     refInfoId = cmp_h5.addReference("x", 100, "0")
    #     cmp_h5.addRefGroup(refInfoId, "/ref00001")
    #     cmp_h5.addAlnGroup("/ref00001", "testGroup")
    #     assert "/ref00001/testGroup" in cmp_h5.h5File
    #     del cmp_h5
    #     os.remove(tmpf[1])

    # def test_addRefGroup(self):
    #     tmpf = tempfile.mkstemp(suffix=".cmp.h5", dir="/tmp")
    #     cmp_h5 = SFCmpH5(tmpf[1], 'w', readType="standard")
    #     cmp_h5.addReference("x", 100, "0")
    #     cmp_h5.addRefGroup(0, "/ref00001")
    #     del cmp_h5
    #     os.remove(tmpf[1])

    # def test_addReference(self):
    #     tmpf = tempfile.mkstemp(suffix=".cmp.h5", dir="/tmp")
    #     cmp_h5 = SFCmpH5(tmpf[1], 'w', readType="standard")
    #     cmp_h5.addReference("x", 100, "0")
    #     del cmp_h5
    #     os.remove(tmpf[1])

    # def test_addMovie(self):
    #     tmpf = tempfile.mkstemp(suffix=".cmp.h5", dir="/tmp")
    #     cmp_h5 = SFCmpH5(tmpf[1], 'w', readType="standard")
    #     cmp_h5.addMovie("movie")
    #     assert "movie" in cmp_h5["/MovieInfo"].asRecArray( )["Name"]
    #     del cmp_h5
    #     os.remove(tmpf[1])
        

