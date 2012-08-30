from nose.tools import assert_equal
from pbcore.io import cmph5
from pbcore.io.cmph5.CmpH5 import CmpH5, SFCmpH5, CmpH5Error
from pbcore.io.cmph5.CmpH5Factory import CmpH5FileCloseError
import tempfile
import os


class TestCmpH5Factory:
    def test_create(self):
        try:
            tmpf = tempfile.mkstemp(suffix=".cmp.h5", dir="/tmp")
            f = cmph5.factory.create( tmpf[1], 'w', cmpType=SFCmpH5, readType="standard" )
            cmph5.factory.close(f) # remove the file from the factory dictionary
            del f #this totally deferences the file
        except:
            assert False
        else:
            assert True
        finally:
            os.remove(tmpf[1])

    def test_close(self):
        """TestCmpH5.test_close"""
        try:
            tmpf = tempfile.mkstemp(suffix=".cmp.h5", dir="/tmp")
            f = cmph5.factory.create( tmpf[1], 'w', cmpType=SFCmpH5, readType="standard" )
            cmph5.factory.close(f) # remove the file from the factory dictionary
            del f #this totally deferences the file
            f1 = cmph5.factory.create( tmpf[1], 'r', cmpType=SFCmpH5, readType="standard" )
            f2 = cmph5.factory.create( tmpf[1], 'r', cmpType=SFCmpH5, readType="standard" )
            assert f1 == f2
            cmph5.factory.close(f1) 
            cmph5.factory.close(f2) 
        except CmpH5Error:
            assert True
        else:
            raise
            assert False
        finally:
            os.remove(tmpf[1])

