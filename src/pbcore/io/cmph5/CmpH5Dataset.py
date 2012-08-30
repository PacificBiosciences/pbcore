#################################################################################$$
# Copyright (c) 2011,2012, Pacific Biosciences of California, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright notice, this 
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice, 
#   this list of conditions and the following disclaimer in the documentation 
#   and/or other materials provided with the distribution.
# * Neither the name of Pacific Biosciences nor the names of its contributors 
#   may be used to endorse or promote products derived from this software 
#   without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY PACIFIC BIOSCIENCES AND ITS CONTRIBUTORS 
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED 
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR ITS 
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#################################################################################$$


import numpy as np
from __init__ import h5vlen, INTEGER_TYPES, CmpH5Error

__version__="$Revision$ $Change$"

class CmpH5Dataset(object):
    """This class wraps an instance of an h5py.Dataset object. It provides
    a subset of the h5py.Dataset interface components. It handles management
    of 'ID' tables and 'lastRow' functionality along with CmpGroup."""
    
    def __init__( self, h5Dataset ):
        """Takes in the h5py.Dataset we want to wrap.
        Uses the globally defined idTableMapping and minGrowthRates
        to determine values for this particular dataset."""
        self._dataset = h5Dataset
        self._isStrDataset = h5Dataset.dtype == np.object 
        self._cache = self._dataset
        self._nRows = self._dataset.shape[0]
        self._growBy = None
        
    def __del__( self ):
        try:
            self.close( )
        except TypeError:
            pass # Means the underlying dataset was already closed
        
    def close( self ):
        self._shrink( )
        
    def _shrink( self ):
        if self._nRows != None and self._dataset.shape[0] != self._nRows:
            self.resize( self._nRows )

    @property
    def name( self ):
        """Map the name attribute to the underlying dataset."""
        return self._dataset.name

    @property
    def shape( self ):
        """Map the shape attribute to the underlying dataset."""
        return self._dataset.shape

    @property
    def attrs( self ):
        """Map our attrs attribute to the underlying dataset."""
        return self._dataset.attrs

    @property
    def asNumPy( self ):
        """Returns the contents of this dataset as a numpy array."""
        d = self._dataset.value.copy( )
        if self._isStrDataset:
            d.dtype = h5vlen
        return d

    def asDictIter( self, keys ):
        """Allows the user to iterate over this table as a series of dictionaries,
        mapping the supplied keys to the elements of each row. Convenient, and slow."""
        for row in self:
            yield dict(zip( keys, row ))

    def asRecArray( self, keys ):
        """Returns the dataset in the form of a recarray with the given keys."""
        columns = [ ( k, self._dataset.dtype ) for k in keys ]
        return np.rec.fromrecords( self._dataset.value, dtype=columns )
  
    def __setitem__( self, key, value ):
        """Delegates to the underlying h5py dataset."""
        self._dataset.__setitem__( key, value )

    def __getitem__( self, key ):
        """Integers index into the corresponding row number. NOT THE ID."""
        if self._isStrDataset:
            return str(self._cache[ key ])
        return self._cache[ key ]

    def __contains__( self, key ):
        """Functions as does __contains__ on a list. If the key exists within the
        values of this dataset, returns true."""
        if self._isStrDataset:
            return any( str(row) == key for row in self )
        return any( row == key for row in self )

    def __iter__( self ):
        """Iterates over the underlying dataset."""
        size = len(self)
        for (i,row) in enumerate( self._cache ):
            if i < size:
                if self._isStrDataset:
                    yield str(row)
                else:
                    yield row

    def __len__( self ):
        """Returns the number of filled rows in the dataset."""
        return self._nRows

    def append(self, data):
        """Convenience function, forwards the request to extend."""
        self.extend( [ data ] )
        
    @property
    def capacity( self ):
        return self._dataset.shape[0]

    def extend( self, rows ):
        """Adds the specified rows of data to the end of the dataset."""
        rowsToAdd = len(rows)
        if self.capacity < self._nRows + rowsToAdd:
            self._grow( rowsToAdd )
        self._dataset[self._nRows:self._nRows+rowsToAdd] = rows
        self._nRows += rowsToAdd
        
    def fill( self, rows, offset ):
        """Adds the specified rows to the dataset, starting from offset.
        Assumes that the dataset is already large enough to contain the data."""
        self._dataset[offset:offset+len(rows)] = rows
        
    def _grow( self, minRows ):
        """Adds at least minRows to the dataset using resize. Adds
        exponentially more each time it is called."""
        if self._growBy == None:
            self._growBy = minRows
        else:
            self._growBy = max( minRows, self._growBy * 2 )
        self.resize( self.capacity + self._growBy )
        
    def resize( self, nRows ):
        """Resized the underlying dataset to the target # of rows."""
        shape = list( self._dataset.shape )
        shape[0] = nRows
        self._dataset.resize( tuple( shape ) )

    def cache( self ):
        """Tells this dataset to load the underlying table into memory 
        for fast access. Make sure and call clearCache() when you're done."""
        self._cache = self.asNumPy

    def clearCache( self ):
        """Clears the memory cached copy of the underlying dataset."""
        self._cache = self._dataset

