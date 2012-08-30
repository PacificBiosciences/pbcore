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

from __init__ import *
from CmpH5Dataset import CmpH5Dataset

__version__="$Revision$ $Change$"

class CmpH5Group(object):
    """This class wraps an instance of an h5py.Group object. It provides
    a subset of the h5py.Group interface components. It handles management
    of 'ID' tables and 'lastRow' functionality along with CmpH5Dataset."""

    def __init__( self, h5Group ):
        """Takes in the h5py.Group object that we are wrapping."""
        self._group = h5Group
        self.name = self._group.name
        self._cache = {}

    def __iter__( self ):
        """Default iterator iterates over the underlying H5Group"""
        return ( obj for obj in self._group )

    def __len__( self ):
        """Default length is the number of elements in my group."""
        return len( self._group )

    def __getitem__( self, key ):
        """Accepts:
        Read Group Name: Returns a AlnGroup object
        """
        return CmpH5Dataset( self._group[ key ] )

    @property
    def attrs( self ):
        """Returns the attrs dict from the underlying Group."""
        return self._group.attrs
    
    def deleteGroup(self, name):
        """Delete group within underlying group, first checking that the group exists"""
        if name in self._group:
            del self._group[name]

    def createGroup( self, name ):
        """Creates the group within our underlying group, and returns the
        CmpH5Group wrapper for the new group."""
        return CmpH5Group( self._group.create_group( name ) )

    def createDataset(self, name, shape, dType, maxShape, chunks, overwrite=False):
        """Generates a dataset in the underlying HDF5 Group. If lastRow, track the last
        filled row of this dataset with an attribute to allow for dynamic dataset growth.
        
        Specify the name of an ID table if you want a second dataset which simply tracks 
        unique IDs for corresponding elements within this dataset."""
        
        if name in self._group:
            if overwrite:
                del self._group[ name ]
            else:
                return self[ name ]
        
        self._group.require_dataset(name, shape, dType, maxshape=maxShape, exact=True, chunks=chunks )
        return self[ name ]

class RefGroup( CmpH5Group ):
    """Simple class to facilitate the high-level __getitem__
    and __iter__ based read interface."""

    def __init__( self, parent, refGroup, id=None ):
        """Add a parent link so we can reference the Cmp object we live under."""
        CmpH5Group.__init__( self, refGroup )
        self.cmpH5 = parent
        self.id = parent["/RefGroup"].getID( Path=self.name ) if id == None else id

    def __getitem__( self, key ):
        """Accepts:
        Read Group Name: Returns a AlnGroup object
        """
        if key in self._cache:
            return self._cache[ key ]

        if key in self and isinstance( self._group[ key ], h5py.Group ):
            self._cache[ key ] = AlnGroup( self, self._group[ key ] )
            return self._cache[ key ]
        
        raise KeyError, "Ref Group unable to locate key: %s" % key

    def __len__( self ):
        """Returns the number of AlnGroups directly
        below this RefGroup"""
        return len( [ rg for rg in self._myPossibleAlnGroups() if rg in self._group ] )

    def __contains__( self, key ):
        """Returns true if the specified key plus this reference
        represents a valid entry in the AlnGroup/Path table."""
        return ( "/".join( [ self.name, key ] ) ) in self.cmpH5["/AlnGroup/Path"]

    def __iter__( self ):
        """Defaults to the read group iterator."""
        return self.alnGroupIterator()

    def _myPossibleAlnGroups( self ):
        """Returns a list of strings of the names of our
        possible read groups from the AlnGroupPath table."""
        rgs = []
        for alnGroupPath in self.cmpH5["/AlnGroup/Path"]:
            ref, rg = alnGroupPath.strip("/").split("/")
            if alnGroupPath.startswith( self.name ):
                rgs.append( rg )
        return rgs
    
    def alnGroupIterator( self ):
        """Iterates over all read groups directly below this reference group."""
        prgs = self._myPossibleAlnGroups()
        for rg in prgs:
            if rg in self._group:
                yield self[ rg ]

    def columnIterator( self, refPosition ):
        """Iterates over entire columns of the alignment"""
        raise Exception( "RefGroup.columnIterator not implemented" )

    @property
    def hasConsensus( self ):
        """Returns True iff there are "Consensus/ConsensusCalls" and 
        "Consensus/ConsensusConfidence" groups under this reference group."""
        return  "Consensus/ConsensusCalls" in self._group and \
                "Consensus/ConsensusConfidence" in self._group

    @property
    def consensus( self ):
        """Returns the Consensus HDF5 group"""
        if not hasattr( self, "_consensus" ):
            if not self.hasConsensus:
                return None
            self._consensus = CmpH5Group( self._group["Consensus"] )
        return self._consensus

    @property
    def consensusCalls( self ):
        """Returns the Consensus/ConsensusCalls dataset."""
        if not hasattr( self, "_consensusCalls" ):
            if not self.hasConsensus:
                return None
            self._consensusCalls = CmpH5Dataset( self._group["Consensus"]["ConsensusCalls"] )
        return self._consensusCalls

    @property
    def consensusConfidence( self ):
        """Returns the Consensus/ConsensusConfidence dataset."""
        if not hasattr( self, "_consensusConfidence" ):
            if not self.hasConsensus:
                return None
            self._consensusConfidence = CmpH5Dataset( self._group["Consensus"]["ConsensusConfidence"] )
        return self._consensusConfidence

    @property
    def refInfoId( self ):
        """Return the refInfoID of this reference group"""
        return self.cmpH5["/RefGroup"].asDict("ID","RefInfoID",cache=True)[ self.id ]

    @property
    def refName( self ):
        """Sequence Id for use in gff file"""
        return self.cmpH5["/RefInfo"].asDict("ID","FullName",cache=True)[ self.refInfoId ]

    def alnHitIterator( self, loadSequence=True, computeAlnPosTranslations=False, auxTables=pulseTables, readFilter=None):
        """Iterates in sequence over all alignment hits to this reference"""
        for alnGroup in self.alnGroupIterator():
            for alnHit in alnGroup.alnHitIterator( loadSequence, computeAlnPosTranslations, auxTables, readFilter ):
                yield alnHit

    @property
    def numAlnHits( self ):
        """Returns the number of alignment hits found in this RefGroup"""
        return sum(x.numAlnHits for x in self.alnGroupIterator())


class AlnGroup( CmpH5Group ):
    """Simple class to facilitate the high-level __getitem__
    and __iter__ based read interface."""

    def __init__( self, parentRefGroup, alnGroup, id=None ):
        """Add a parent parameter so we can access the refGroup we
        live under."""
        CmpH5Group.__init__( self, alnGroup )
        self.refGroup = parentRefGroup
        self.id = parentRefGroup.cmpH5["/AlnGroup"].getID( Path=self.name ) if id == None else id
        self._cmpH5 = self.refGroup.cmpH5

    def __getitem__( self, key ):
        """Accepts:
        - Read Name: returns the AlignmentHit associated with the specified read
        - Underlying Table Name: returns a CmpH5Dataset object containing the specified table.
        """
        if key in self._cache:
            return self._cache[ key ]

        if key in self._group and isinstance( self._group[ key ], h5py.Dataset ):
            self._cache[ key ] = CmpH5Dataset( self._group[ key ] )
            return self._cache[ key ] 

        raise KeyError, "Read Group unable to locate key: %s" % key

    def __contains__( self, key ):
        """Returns True iff the key is a valid readName for one
        of the alignments. Returns false for integer keys."""
        return key in self._group and isinstance( self._group[ key ], h5py.Dataset )
    
    def __iter__( self ):
        """Defaults to the alignment hit iterator."""
        return self.alnHitIterator()

    def _alnHitFromRowNum( self, rowNumber, loadSequence=True, computeAlnPosTranslations=False, auxTables=pulseTables ):
        """Convenience function for creating an alignment hit object
        from one row of the global alignmentIndex table. You should always use 
        this to create alignment hits within this class."""
        hit = self._cmpH5._cmpAlnHit()
        hit.loadFromCmpH5Dataset( rowNumber, self["AlnArray"], self._cmpH5, loadSequence, computeAlnPosTranslations )
        if len(auxTables) > 0:
            pulseInfo = dict( [ ( table, self[ table ] ) for table in self._group if table in auxTables ] )
            hit.loadPulseInfo( self._cmpH5["/AlnInfo"].asRecArray()[ rowNumber ], pulseInfo )
        refInfoID = self._cmpH5["/RefGroup"].asDict("ID","RefInfoID",cache=True)[ self.refGroup.id ]
        hit.target_id = self._cmpH5["/RefInfo"].asDict("ID","FullName",cache=True)[ refInfoID ]
        return hit

    def alnHitIterator( self, loadSequence=True, computeAlnPosTranslations=False, auxTables=pulseTables, readFilter=None ):
        """Iterates over all Alignment Hits in this read group."""
        
        try:
            cacheTables = [ table for table in self._group if table in auxTables ]
            cacheTables += [ "AlnArray" ] if loadSequence else []
            for table in cacheTables:
                self[ table ].cache()
    
            for rowNum in self._myAlignmentIndexRows(readFilter):
                yield self._alnHitFromRowNum( rowNum, loadSequence, computeAlnPosTranslations, auxTables )
        
        # Be sure to uncache the dataset we have loaded, even if we don't
        # fully consume the iterator        
        finally:
            for table in cacheTables:
                self[ table ].clearCache()

    def _myAlignmentIndexRows( self, readFilter=None):
        """Returns a numpy array of indexes into the global AlignmentIndex
        table representing all of the rows corresponding to this readgroup.
        readFilter is a function that maps the AlnInfo recArray to booleans,
        indicating which alignments to iterate through.
        """
        ai = self.refGroup.cmpH5["/AlnInfo"].asRecArray( )
        
        readSelection = ai["AlnGroupID"] == self.id                
        
        if readFilter:
            readSelection = np.logical_and(readSelection, readFilter(ai))          
                
        return np.where( readSelection )[0]

    def columnIterator( self ):
        """Iterates over entire columns of the alignment, where each
        column is composed of only reads within this readgroup."""
        raise Exception( "AlnGroup.columnIterator not implemented" )

    def __len__( self ):
        """Returns the number of alignment hits found in this AlnGroup"""
        return self.numAlnHits

    @property
    def numAlnHits( self ):
        """Returns the number of alignment hits found in this AlnGroup"""
        return len(self._myAlignmentIndexRows())

    @property
    def pulseTables( self ):
        """Returns a list of the pulse metrics available within this 
        read group."""
        return [ pt for pt in pulseTables if pt in self._group ]

