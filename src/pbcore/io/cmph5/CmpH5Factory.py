#################################################################################
# Copyright (c) 2011-2013, Pacific Biosciences of California, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Pacific Biosciences nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE.  THIS SOFTWARE IS PROVIDED BY PACIFIC BIOSCIENCES AND ITS
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR
# ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#################################################################################

import os
import h5py

class CmpH5FileCloseError( Exception ):
    pass

##################################################################
#
# This factory is the safest/best way to generate a CmpH5 object.
#
class Singleton(type):
    """Standard Singleton pattern"""
    def __init__( cls, name, bases, dict ):
        super( Singleton, cls ).__init__( name, bases, dict )
        cls.instance = None
    def __call__( cls, *args, **kwargs ):
        if cls.instance == None:
            cls.instance = super( Singleton, cls ).__call__( *args, **kwargs )
        return cls.instance

class CmpH5Factory( object ):
    """This class generates CmpH5 objects (Astro, SF, etc.) from filename/paths."""
    __metaclass__ = Singleton

    def __init__( self ):
        self._opened = {}

    def close( self, cmpH5 ):
        if cmpH5.h5File.filename not in self._opened:
            raise CmpH5FileCloseError, "File %s is not opened by CmpH5Factory, or it has been closed." % cmpH5.h5File.filename
        if hasattr(cmpH5, "h5File"): #the file is in an "open" state. We should make this more explicit in the furture
            fn = cmpH5.h5File.filename
            del self._opened[fn]
            cmpH5.close()
        

    def create( self, cmpH5Path, mode='r', cmpType=None, readType='standard' ):
        """Given the path to a valid .cmp.h5 file, returns a CmpH5 object. 
        If the mode is read or append, the type of CmpH5 to create is determined from
        the version string in the file. If the mode is write, then the optional
        'type' parameter to this function is used.
        This is the best way to create CmpH5 objects."""
        cmpH5AbsPath = unicode(os.path.abspath(os.path.expanduser(cmpH5Path)))
        
        if mode in "ra":
            cmpH5 = h5py.File( cmpH5AbsPath, 'r' )
            version = str(cmpH5.attrs["Version"]) if "Version" in cmpH5.attrs else None
            readType = str(cmpH5.attrs["ReadType"]) if "ReadType" in cmpH5.attrs else None
            from CmpH5 import SFCmpH5
            from CmpH5 import PBCmpH5
            from CmpH5 import SFRCCSCmpH5
            from __init__ import V1_2_0_SF, V1_2_0_PB, V1_2_0, V1_3_1, V1_3_1_PB, V1_3_1_SF
            v2c = { V1_2_0_SF: SFCmpH5,
                    V1_2_0_PB: PBCmpH5,
                    V1_2_0   : SFCmpH5,
                    V1_3_1   : SFCmpH5,
                    V1_3_1_SF : SFCmpH5,
                    V1_3_1_PB : PBCmpH5 }

            if readType == "RCCS" and version == V1_2_0:
                cmpType = SFRCCSCmpH5
            else:
                cmpType = SFCmpH5 if version == None else v2c[ version.strip() ]
            cmpH5.close()
        
        if cmpType == None:
            raise IOError, "A CmpH5 Type must be specified when creating a new cmp.h5 file. (%s)" % cmpH5AbsPath

        if not cmpH5AbsPath in self._opened:
            self._opened[cmpH5AbsPath] = cmpType(cmpH5AbsPath, mode=mode, readType=readType)
            
        return self._opened[cmpH5AbsPath]

factory = CmpH5Factory( )
