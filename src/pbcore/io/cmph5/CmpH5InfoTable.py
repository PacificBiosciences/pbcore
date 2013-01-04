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

from __init__ import *

import sys
import h5py
import numpy as np

class registeredInfoTableClass(type):
    _tables = {} 
    def __new__(cls, name, bases, dct):
        tableClass = type.__new__(cls, name, bases, dct)
        if hasattr(tableClass, "_h5group") and tableClass._h5group != "":
            for ver in tableClass._version:
                cls._tables[ ver, tableClass._h5group ] = tableClass
        return tableClass

    @classmethod
    def getTableObjs(cls, cmph5, targetVerison):
        rtn = {}
        for (version, h5group) in cls._tables:
            if version == targetVerison:
                tableClass = cls._tables[ (version, h5group) ]
                rtn[h5group] = tableClass(cmph5)
        return rtn

class InfoTable(object):
    __metaclass__ = registeredInfoTableClass
    _h5group = ""
    _h5datasets = ("ID",)   
    _h5auxDatasets = ()
    _masterDataset = "ID"
    _h5attrs = { "MasterDataset": ( _masterDataset, h5vlen, None ) }
    _chunkRows = 256

    def __init__(self, cmph5):
        self._cmph5 = cmph5
        self._group = self._cmph5[self.__class__._h5group] if self.__class__._h5group in self._cmph5 else None
        self._idToRow = {}
        self._recarray = None
        self._dictViews = {}
        self.dirty = True
        self._nRow = None
        self._growBy = None
        if "ReadType" in cmph5.attrs and cmph5.attrs["ReadType"] == "RCCS":
            self._withAuxDS = True
        else:
            self._withAuxDS = False
        
    def close( self ):
        self._shrinkDatasets( )
        
    def _shrinkDatasets( self ):
        """Resize our datasets to match the data."""
        if self._nRow == None: # No writes
            return
        for dsName in [ ds[0] for ds in self._getDSList( ) ]:
            ds = self._group[ dsName ]
            if len(ds.shape) == 1:
                if ds.shape[0] != self._nRow:
                    ds.resize(( self._nRow, ))
            else:
                r,c = ds.shape
                if r != self._nRow:
                    ds.resize(( self._nRow, c ))
     
    def _getDSList(self):
        datasets = list(self.__class__._h5datasets)
        if self._withAuxDS == True:
            datasets.extend( [ds for ds in self.__class__._h5auxDatasets] )
        return datasets
    
    def refresh(self):
        # We re-init self._group in case the underlying group has changed.
        self._group = self._cmph5[self.__class__._h5group] if self.__class__._h5group in self._cmph5 else None
        self._dictViews = {}
        self._recarray = self._buildRecArray( )
        self.dirty = False

    def __len__( self ):
        return self._group[ self._masterDataset ].shape[0]
        #return len(self.asRecArray( ))  #does not work in my test, create infinit recursvie loop, JC 2/8/11

    @property
    def attrs( self ):
        return self._group.attrs

    def asRecArray( self, columns=None ):
        if self.dirty:
            self.refresh( )
        if columns == None:
            return self._recarray
        else:
            return self._recarray[ columns ]
        
    def _handleVLenStr( self, dsName, dsType, group ):
        """If the dataset type is vlenstr, returns a fixed length
        string type whos length matches the longest element of the dataset"""
        if dsType != h5vlen or len( group[ dsName ] ) == 0:
            return (dsName, dsType)
        return (dsName, "|S%d" % np.max( [ 1 ] + map( len, group[ dsName ].value )))

    def _buildRecArray( self ):
        dsList = self._getDSList( )

        data = np.recarray( shape=( len(self), ),
                         dtype=[ self._handleVLenStr(n, t, self._group) for n,t,c in dsList ])
        if len(self) > 0:
            for name, type, count in dsList:
                if count == 1:
                    data[ name ] = self._group[ name ].value
        return data
    
    def asDict( self, key, values, cache=False ):
        """Returns a dictionary mapping the given key
        to the specified values (all columns of this table)
        If cache=True, the resulting dict is cached for fast repeat use"""
        recarray = self.asRecArray( )
        if cache: 
            if ( key, values ) not in self._dictViews:
                self._dictViews[ ( key, values ) ] = dict( zip( recarray[ key ], recarray[ values ] ) )
            return self._dictViews[ ( key, values ) ]
        return dict( zip( recarray[ key ], recarray[ values ] ) )

    def create(self, withAuxDS=False):
        self._cmph5["/"].require_group(self.__class__._h5group)
        self._group = self._cmph5[self.__class__._h5group]
        self._withAuxDS = withAuxDS
        datasets = self._getDSList()

        for dsn, dType, nCol in datasets:
            if nCol == 1:
                self._group.require_dataset( dsn, (0,), dType, exact=True, maxshape=(None,), chunks = (self._chunkRows,) )  
            else:
                self._group.require_dataset( dsn, (0,nCol,), dType, exact=True, maxshape=(None,nCol), chunks =(self._chunkRows,nCol) )  

        for attr in self.__class__._h5attrs:    
            dVal, dType, shape = self.__class__._h5attrs[attr]
            self._group.attrs.create(attr, dVal, shape=shape, dtype=dType)
    
    def getID( self, **kwargs ):
        """Takes keyword arguments mapping columns to values. Returns
        the single ID that satisfies all constraints. An exception is
        raised if zero or more than one ID satisfy the condition."""
        recarray = self.asRecArray( )
        idxSets = [ set( np.where( recarray[ key ] == kwargs[ key ] )[0] ) for key in kwargs ]
        idx = reduce( lambda x,y: x & y, idxSets )
        if len(idx) != 1:
            raise CmpH5Error, "Unable to locate unique ID for constraints %s in %s:\n%s" \
                                            % ( str(kwargs), str(self.__class__), str(idx))
        return recarray[ idx.pop() ]["ID"]

    def getUnusedIDs( self, n ):
        """For now returns N ids beyond the max current ID. Change to fill in?"""
        recarray = self.asRecArray( )
        startID = max( recarray["ID"] ) + 1 if len( recarray["ID"] > 0 ) else 1
        return range( startID, startID+n )

    def append(self, **kwargs):
        """See Extend, but specify single values for kwargs. Ex. append( MovieID=1, RefGroupID=2, ... )"""
        for k in kwargs:
            kwargs[ k ] = [ kwargs[ k ] ]
        return self.extend( **kwargs )[ 0 ]

    def extend( self, **kwargs ):
        """Takes in kwargs, ex. extend( MovieID=[1,2,3,4], RefGroupID=[2,3,4,5], ... )"""
        data = kwargs
        if len(data) == 0:
            return None

        nToAdd = [ len(v) for v in data.values() ]
        if not all( [ n == nToAdd[0] for n in nToAdd ] ):
            raise ValueError, "Lengths of all kwargs to extend/append must be equal"
        nToAdd = nToAdd[0]
        dsNames = [ds[0] for ds in self._getDSList( )]
 
        if "ID" in dsNames and "ID" not in data:
            data["ID"] = self.getUnusedIDs( nToAdd )

        for dsn in dsNames:
            if dsn not in data:
                raise KeyError, "Unable to locate append key (%s) in CmpInfoTable" % dsn
             
        if not self.dirty: # Update the cached version to avoid a full refresh
            nRow = len( self._recarray )
            self._recarray.resize( ( nRow + nToAdd, ) )
            for dsn in dsNames:
                self._recarray[ dsn ][ nRow:nRow+nToAdd ] = data[ dsn ]
            self._dictViews = {} # These are no longer valid

        if self._nRow == None: # Should be filled.
            self._nRow = len(self)
        for dsn in [ ds[0] for ds in self._getDSList( ) ]:
            ds = self._group[dsn]
            self._resizeToFit( ds, nToAdd )
            if len(ds.shape) == 1:
                ds[self._nRow:(self._nRow + nToAdd)] = data[dsn]
            else:    
                ds[self._nRow:(self._nRow + nToAdd),:] = data[dsn]

        self._nRow += nToAdd
        self._group.attrs.modify("nRow", self._nRow)

        return data["ID"] if "ID" in data else [ None ]
    
    def _resizeToFit( self, ds, nToAdd ):
        currSize = ds.shape[0]
        if self._nRow + nToAdd > currSize:
            if self._growBy == None:
                self._growBy = nToAdd
            else:
                self._growBy = max( nToAdd, self._growBy * 2 ) # Double the resize each time we need it.
            if len(ds.shape) == 1:
                ds.resize( (currSize+self._growBy, ) )
            else:
                nRow, nCol = ds.shape
                ds.resize( (currSize+self._growBy, nCol ) )

class GenericAlnInfoTable(InfoTable):
    _version = (V1_2_0, V1_2_0_SF, V1_3_1, V1_3_1_SF )
    _h5group = "/AlnInfo"
    _h5datasets = ( ("AlnIndex", uint32t, 22), )
    _masterDataset = "AlnIndex"
    _h5auxDatasets = ( ("CircularCoverage", uint8t, 1), )
    _h5attrs = { "MasterDataset": ( _masterDataset, h5vlen, None ) }
    _chunkRows = 4096

    def _buildRecArray( self ):
        dsList = self._getDSList( )
        dtype = [ self._handleVLenStr(n, t, self._group) for n,t,c in dsList if n != "AlnIndex" ]
        dtype += [ (n,INDEX_DTYPE) for n in INDEX_COLS ]
        dtype += [ ("ID","u4") ]

        data = np.recarray( shape=( len(self), ), dtype=dtype )
        if len(self) > 0:
            for name, type, count in dsList:
                if name != "AlnIndex":
                    try:
                        data[ name ] = self._group[ name ].value
                    except Exception, e:
                        print >>sys.stderr, '!! in _buildRecArray:'
                        print >>sys.stderr, '!! Caught exception (%s)' % str(e)
                        print >>sys.stderr, '!! name=%s' % name
                        print >>sys.stderr, '!! type=%s' % str(type)
                        print >>sys.stderr, '!! count=%s' % str(count)
            for i,name in enumerate( INDEX_COLS ):
                data[ name ] = self._group["AlnIndex"][:,i]
            data["ID"]  = data["AlnID"]
        return data

class PBAlnInfoTable(GenericAlnInfoTable):
    _version = (V1_2_0_PB, V1_3_1_PB)
    _h5group = "/AlnInfo"
    _h5datasets = ( ("AlnIndex", uint32t, 22),
                    ("ZScore", float32t, 1 ) )

class GenericMovieInfoTable(InfoTable):
    _version = (V1_2_0, V1_2_0_SF, V1_3_1, V1_3_1_SF)
    _h5group = "/MovieInfo"
    _h5datasets = ( ("ID", uint32t, 1), 
                    ("Name", h5vlen, 1) ) 

class PBMovieInfoTable(InfoTable):
    _version = (V1_2_0_PB, V1_3_1_PB)
    _h5group = "/MovieInfo"
    _h5datasets = ( ("ID", uint32t, 1),
                    ("Name", h5vlen, 1),
                    ("Exp", uint32t, 1),
                    ("Run", uint32t, 1))

class GenericRefInfoTable(InfoTable):
    _version = SUPPORTED_VERSIONS
    _h5group = "/RefInfo"
    _h5datasets = ( ("ID", uint32t, 1),
                    ("FullName", h5vlen, 1), 
                    ("Length", uint32t, 1),
                    ("MD5", h5vlen, 1) )

class GenericAlnGroupTable(InfoTable):
    _version = SUPPORTED_VERSIONS
    _h5group = "/AlnGroup"
    _h5datasets = ( ("ID", uint32t, 1),
                    ("Path", h5vlen, 1) )

class GenericRefGroupTable(InfoTable):
    _version = SUPPORTED_VERSIONS
    _h5group = "/RefGroup"
    _h5datasets = ( ("ID", uint32t, 1), 
                    ( "Path", h5vlen, 1),
                    ( "RefInfoID", uint32t, 1))

class GenericFileLogTable(InfoTable):
    _version = SUPPORTED_VERSIONS
    _h5group = "/FileLog"
    _h5datasets = ( ("ID", uint32t, 1),
                    ("Program", h5vlen, 1),
                    ("Version", h5vlen, 1),
                    ("Timestamp", h5vlen, 1),
                    ("CommandLine", h5vlen, 1),
                    ("Log", h5vlen, 1))

class InfoTableContainer(object):
    def __init__(self, cmph5, mode, version = None, withAuxDS = False ):
        self._cmph5 = cmph5

        self._items = {}
        if version == None:
            cmph5VER = self._cmph5["/"].attrs["Version"]
        else:
            cmph5VER = version

        assert cmph5VER in SUPPORTED_VERSIONS, "cmp.h5 version not supported"
        self._withAuxDS = withAuxDS
        
        self._items = registeredInfoTableClass.getTableObjs(self._cmph5, cmph5VER)

    def refreshAll(self):
        for gn in self._items:
            self._items[gn].refresh( )

    def createAll(self):
        for gn in self._items:
            self._items[gn].create( withAuxDS = self._withAuxDS )
            
    def closeAll(self):
        for gn in self._items:
            self._items[gn].close( )

    def __getitem__(self, key):
        return self._items[key]

    def __iter__(self):
        for key in self._items:
            yield key

