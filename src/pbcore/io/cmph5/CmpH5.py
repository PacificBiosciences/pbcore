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


import numpy
import re
import unittest
from glob import glob
from CmpH5Group import RefGroup, AlnGroup, CmpH5Group
from CmpH5AlnHit import CmpH5AlnHit, SFCmpH5AlnHit, PBCmpH5AlnHit, SFCmpH5RCCSAlnHit
from CmpH5Dataset import CmpH5Dataset
from CmpH5InfoTable import InfoTableContainer
from time import asctime
from __init__  import *

__version__="$Revision$ $Change$"

def movie2Set( m ):
    return "_".join(str(m).split("_")[2:5])

class CmpH5( CmpH5Group, InfoTableContainer ):
    """Wraps an h5py.File object, providing a high level interface
    to the underlying groups and datasets."""

    def __init__(self, filename, mode='r', readType = "standard", withAuxDS = False):
        """Initialize the wrapped h5py object. Since the h5py.File object is also the
        root group, initializes our _group attribute to point to it as well.
        Sets up some defaults, and creates the top level tables if they do not yet exist."""

        self.filename = filename
        self.mode = mode
        self.withAuxDS = withAuxDS

        try:
            self.h5File = h5py.File(filename, mode)
        except IOError:
            raise IOError, "Unable to open file %s with the specified mode (%s). Check permissions and existence." % ( filename, mode )

        CmpH5Group.__init__( self, self.h5File ) 
        if mode == "w":
            self._setVersion( )
        
        InfoTableContainer.__init__( self, self.h5File, self.mode, self.version, self.withAuxDS )
        if mode == 'w':
            self.createAll()
            self.attrs["ReadType"] = readType
        self.refreshAll( )

        self._colName2Index = dict(zip(self.indexCols,range(len(self.indexCols))))
        
        # The following must be defined in subclasses.
        self._cmpAlnHit = None


    def log( self, program, version, timestamp, commandLine, log ):
        """Adds an entry to the FileLog in this cmp.h5"""
        self["/FileLog"].append( Program=program,
                                 Version=version,
                                 Timestamp=timestamp,
                                 CommandLine=commandLine,
                                 Log=log )

    def _setVersion( self ):
        raise CmpH5Error, "Should be implemented in a subclass"

    def flushDatasets( self ):
        if self._items != None:
            self.closeAll()
        if hasattr(self, "_cache") and  self._cache != None:
            for obj in self._cache.values( ):
                if isinstance( obj, CmpH5Dataset ):
                    obj.close( )

    def close( self ):
        """ 
        This close method is only used when the object is initialize directly
        from subclass of the CmpH5. If a CmpH5 object is created by the "CmpH5Factor"
        it should be managed by the factory 
        """
        self.flushDatasets()

        if hasattr(self, "h5File"):
            if self.h5File:
                self.h5File.close()
            del self.h5File #remove the reference, let's h5py to handle the rest

    def __del__( self ):
        self.close( )

    def __getattr__(self, name):
        if name == "h5File":
            raise CmpH5Error, "cmph5 file is closed"
        else:
            raise AttributeError

    def addRefGroup( self, refInfoID, path=None ):
        """Creates a group for the given reference, then adds it to
        the RefGroup table. Does nothing if the ref group already exists.
        Returns the RefGroup. Uses path only if it exists."""
        
        if refInfoID not in self["/RefGroup"].asRecArray( )["RefInfoID"]:
            refGroupPath = self._nextRefGroupPath if path == None else path
            refGroupId = self["/RefGroup"].append(  Path = refGroupPath,
                                                    RefInfoID = refInfoID )
            return RefGroup( self, self._group.create_group( refGroupPath ), id=refGroupId )
        else:
            refGroupPath = self["/RefGroup"].asDict("RefInfoID","Path", cache=True)[ refInfoID ]
        return self[ refGroupPath ]

    def addAlnGroup( self, refGroupPath, alnGroupName ): 
        """Creates an aln group under the specified reference group.
        Adds this to the AlnGroupPath table.
        Does nothing if the alnGroup already exists."""
       
        alnGroupPath =  refGroupPath + "/" + alnGroupName
        if alnGroupPath not in self["/AlnGroup"].asRecArray( )["Path"]:
            alnGroupId = self["/AlnGroup"].append( Path = alnGroupPath )
            alnGroup = AlnGroup( self[ refGroupPath ], self._group[ refGroupPath ].create_group( alnGroupName ), id=alnGroupId )
            alnGroup.attrs.create("MasterDataset","AlnArray", dtype=h5vlen, shape=None );
            return alnGroup
        return self[ alnGroupPath ]
    
    def addReference( self, referenceFullName, length, md5 ):
        """The full reference name goes in /RefInfo. Returns the created RefInfoID.
        If refGroupPath is specified, creates an empty refGroup at the corresponding path"""
        if referenceFullName in self['/RefInfo'].asRecArray( )['FullName']:
            return self["/RefInfo"].asDict("FullName","ID",cache=True)[ referenceFullName ]
        return self['/RefInfo'].append( FullName = referenceFullName,
                                        Length = length, MD5 = md5 )

    def addMovie( self, movieName ):
        """Adds the specified movie name to the MovieName and MovieID tables."""
        if movieName in self["/MovieInfo"].asRecArray( )["Name"]:
            return self["/MovieInfo"].asDict("Name","ID",cache=True)[ movieName ]
        return self["/MovieInfo"].append( Name = movieName )

    def isSorted( self ):
        """Returns true iff there exists an attribute called 'index' (from the spec)."""
        return "Index" in self.attrs

    @property
    def _nextRefGroupPath( self ):
        """Returns the integer value of the higest auto generated 
        reference sequence group name. Actively searches to find it."""
        matches = [ re.search( REF_GROUP_PATH_REGEX, refGroupPath ) for refGroupPath in self["/RefGroup"].asRecArray( )["Path"] ]
        indices = [ int(match.group(1)) for match in matches if match ] + [ 0 ] # 0 here means we return minimum value of 1.
        return REF_GROUP_PATH_TEMPLATE % (max(indices)+1)
        
    def refGroupFromFullName( self, referenceFullName ):
        """Given a reference full name, returns the corresponding RefGroup."""
        try:
            refInfoID   = self['/RefInfo'].asDict('FullName', 'ID')[ referenceFullName ]
            rgPath      = self['/RefGroup'].asDict('RefInfoID', 'Path')[ refInfoID ]
            return self[ rgPath ]
        except IndexError:
            raise KeyError, "Call to refGroupFromFullName failed: No ref group with that name exists (%s)." % referenceFullName

    def addConsensus( self, referenceFullName, sequence, qualities, algorithmSource="Unknown Algorithm"):
        """Adds a consensus sequence (uc string) and associated 
           qualities (list of ints) and other info to the reference specified."""

        if len(sequence) != len(qualities):
            raise CmpH5Error, "Unequal length sequence and qualities: %i != %i" % (sequence, qualities)
        
        refSeqGroup = self.refGroupFromFullName( referenceFullName )

        consensusGroup = refSeqGroup.createGroup("Consensus")
        consensusGroup.attrs.create( "Algorithm Source", data=algorithmSource )
        consensusGroup.attrs.create( "Sequence Sample Ploidy", data="Haploid" )
        consensusGroup.attrs.create( "Date Generated", data=asctime() )
        consensusGroup.attrs.create( "lastCoveredPos", data=len(sequence) )
        
        # hopefully with new cmp.h5 this will not blow up memory after extend below. 
        shape = (0,)
        calls = consensusGroup.createDataset("ConsensusCalls", shape, h5py.h5t.NATIVE_UINT8, (None,), (256,))
        newCalls = [ base2hexMap[base] if base2hexMap.has_key(base) else -1 for base in list(sequence) ]
        calls.extend( newCalls )
        quality = consensusGroup.createDataset("ConsensusConfidence", shape, h5py.h5t.IEEE_F32LE, (None,), (256,))
        quality.extend( qualities )

    def writeAlignments( self, alignmentHitList, refSeqName, alnGroupName, movieName, refGroupPath=None, writeQV = False ):
        """Writes a list of AlignmentHit objects to this cmpH5 file.
        Requires a reference name (NOT reference group name) and an aln
        group name to store them under. Also requires a movie name
        to associate with these alignments. NOTE: The specified alnGroup 
        must not exist."""

        refInfoID   = self['/RefInfo'].asDict("FullName","ID",cache=True)[ refSeqName ]
        refGroup    = self.addRefGroup( refInfoID, path=refGroupPath )
        if refGroup.name + "/" + alnGroupName in self["/AlnGroup"].asRecArray( )["Path"]:
            raise CmpH5Error, "Error: writeAlignments must be called exactly once per aln group."
        alnGroup    = self.addAlnGroup( refGroup.name, alnGroupName )
        movieID     = self.addMovie( movieName )
        
        # Line below generates { 'm234234_234234_s1' : lowest matching MovieID }
        idBySet     = dict( [ ( movie2Set(name), id ) for id, name in self['/MovieInfo'].asRecArray(['ID','Name']) ][::-1] )

        if len(alignmentHitList)==0:
            return
        
        refGroupID      = refGroup.id
        alnGroupID      = alnGroup.id
        alnID           = len( self["/AlnInfo/AlnIndex"] ) + 1
        offset_begin    = 0 #len( alnGroup["AlnArray"] )
        
        alnIndexRows    = numpy.empty( shape=( len(alignmentHitList), len(self.indexCols) ), dtype=self.alnIdxDType )
        alnData         = []
        qvData          = []
        
        for i, hit in enumerate( alignmentHitList ):
            
            if isinstance( hit, CmpH5AlnHit ):
                cmpHit = hit
            else:
                cmpHit = self._cmpAlnHit( hit )
            
            indexData = cmpHit.alignmentIndexData
            offset_end = offset_begin + cmpHit.alignedLength

            indexData["Offset_begin"]   = offset_begin
            indexData["Offset_end"]     = offset_end
            indexData["AlnID"]          = alnID+i
            indexData["RefGroupID"]     = refGroupID
            indexData["AlnGroupID"]     = alnGroupID
            indexData["MovieID"]        = movieID
            #indexData["MoleculeID"]     = movieID * MAX_HOLE_NUMBER + indexData["HoleNumber"]
            indexData["MoleculeID"]     = idBySet[ movie2Set( movieName ) ] * MAX_HOLE_NUMBER + indexData["HoleNumber"]

            alnIndexRows[i] = numpy.array( [ int(indexData[col]) for col in cmpHit.indexCols ], dtype=self.alnIdxDType) # Using cmpHit.indexCols gets the ordering

            alnData += cmpHit.alignmentArray + [0] # zero padded at the end of each of the alignment array
            if writeQV == True:
                qvData += cmpHit.QualityValue + [0]
            offset_begin = offset_end + 1 # zero padded at the end of each of the alignment array

        self["/AlnInfo/AlnIndex"].extend( alnIndexRows )
        alnGroup.createDataset("AlnArray", (len(alnData),), h5py.h5t.NATIVE_UINT8, (None,), (16384,) )
        alnGroup["AlnArray"].fill( numpy.array(alnData, dtype=numpy.uint8), 0 )

        if writeQV == True:
            alnGroup.createDataset("QualityValue", (len(alnData),), h5py.h5t.NATIVE_UINT8, (None,), (16384,) )
            alnGroup["QualityValue"].fill( numpy.array(qvData, dtype=numpy.uint8), 0 )

        self["/AlnInfo"].dirty = True
        
    def resetMoleculeIDs( self ):
        """After writing, we update *all* molecule IDs for now.
        TODO: Replace this with an intelligent hash-based system."""
        if len(self["/AlnInfo"]) == 0: return
        mIDByRow = numpy.empty( shape=(len(self["/AlnInfo"]),), dtype='u4' )
        mKeys = self.asRecArray( ["/MovieInfo/Name","HoleNumber"] )
        mIDs = { }
        for i,(name,hole) in enumerate( mKeys ):
            molecule = ( movie2Set(name), hole )
            mIDs.setdefault( molecule, i )
            mIDByRow[i] = mIDs[ molecule ]
        self._group["/AlnInfo/AlnIndex"][:,self.indexCols.index("MoleculeID")] = mIDByRow
            
    def copyFrom( self, srcCmpH5 ):
        """Copies all metadata (no alignments) from the specified cmpH5 object"""
        for path in [ "/MovieInfo", "/RefInfo" ]:
            del self._group[ path ]
            srcCmpH5._group.copy( path, self._group )
        for k,v in srcCmpH5.attrs.iteritems():
            self._group.attrs[k] = v
        self.refreshAll( )
        
    def __getitem__( self, key ):
        """Provides a high level read interface. Accepts many keys:
        - Read Group or Ref Group Path: returns the corresponding Read/Ref Group
        - Underlying Dataset Path: returns the underlying Dataset, wrapped in a CmpH5Dataset object.
        - Underlying Top Level Group: returns a CmpInfoTable object representing the data within the group
        """
        if not hasattr(self, "h5File"):
            raise CmpH5Error, "cmpH5 file object is already closed"

        if key in self._items: # CmpInfoTable
            return self._items[ key ]

        if key in self._cache:
            return self._cache[ key ]
        
        if key in self._group:

            if isinstance( self._group[ key ], h5py.Dataset ):
                self._cache[ key ] = CmpH5Dataset( self._group[ key ] )
                return self._cache[ key ]

            if "/AlnGroup/Path" in self._group and key in self['/AlnGroup'].asRecArray( )["Path"]:
                refGroupName, alnGroupName = key.split("/")[-2:]
                return self[ "/"+refGroupName ][ alnGroupName ]

            if "/RefGroup/Path" in self._group and key in self['/RefGroup'].asRecArray( )["Path"]:
                self._cache[ key ] = RefGroup( self, self._group[ key ] )
                return self._cache[ key ]

        raise KeyError, "CmpH5 unable to interpret/locate key: %s" % key

    def __contains__( self, key ):
        """Returns true iff __getitem__(key) should work."""
        try:
            self[ key ]
            return True
        except KeyError:
            return False

    def __iter__( self ):
        """Returns the default iterator, which iterates over reference groups."""
        return self.refGroupIterator()

    def refGroupIterator( self ):
        """Returns a generator over all reference groups"""
        for refGroupPath in self["/RefGroup/Path"]:
            yield self[ refGroupPath ] 

    def refInfoIterator( self ):
        """Returns a generator over reference annotations"""
        for row in self["/RefInfo"].asRecArray( ):
            yield ReferenceAnnotation( row )

    def alnHitIterator( self, loadSequence=True, computeAlnPosTranslations=False, auxTables=pulseTables, readFilter=None ):
        """Iterates over every alignmentHit in this file"""
        for refGroup in self.refGroupIterator():
            for alnHit in refGroup.alnHitIterator( loadSequence, computeAlnPosTranslations, auxTables, readFilter):
                yield alnHit

    def refGroupById( self, id ):
        """Given the integer ID for a ref group in the
        RefSeqName table, returns that RefGroup"""
        refGroupPath = self["/RefGroup"].asDict("ID","Path")[ id ]
        return self[ refGroupPath ]

    def alnGroupById( self, id ):
        """Given the integer ID for a read group in the 
        AlnGroupPathIDs table, returns that AlnGroup."""
        alnGroupPath = self["/AlnGroup"].asDict("ID","Path")[ id ]
        return self[ alnGroupPath ]

    def getAlnHitsFromReadId( self, readId, **kwargs ):
        """Given a readId, returns an iterator over alignmentHit objects
        that match it. Subread Ids are also accepted. ``**kwargs`` accepted
        are those from alnHitIterator( )"""
        movie, hole, subread = None, None, None
        idElts = readId.split("/")
        if len(idElts) == 3:
            movie, hole, subread = idElts
        elif len(idElts) == 2:
            movie, hole = idElts
        else:
            raise KeyError, "Unable to parse read Id: %s" % readId

        aiTable = self.asRecArray(["/MovieInfo/Name","HoleNumber","rStart","rEnd","AlnGroupID"])
        mySlice = (aiTable["/MovieInfo/Name"] == movie) & (aiTable["HoleNumber"] == int(hole))
        if subread != None:
            rs, re = [ int(v) for v in subread.split("_") ]
            mySlice = (aiTable["rStart"] == rs) & (aiTable["rEnd"] == re) & mySlice

        for rowNumber in numpy.where( mySlice )[0]:
            myRG = aiTable["AlnGroupID"][ rowNumber ]
            myRG = self.alnGroupById( myRG )
            yield myRG._alnHitFromRowNum( rowNumber, **kwargs )

    @property
    def numAlnHits( self ):
        """Read only, indicates the number of alignment hits contained in this cmp.h5 file."""
        return len(self["/AlnInfo"])

    @property
    def numReads( self ):
        """Read only, indicates the number of unique reads(ZMWs) in this cmp.h5 file."""
        return self._numUniqueAlnIdxRows( [ "MoleculeID" ] )
    
    @property
    def numSubreads( self ):
        """Read only, indicates the number of unique subreads in this cmp.h5 file."""
        return self._numUniqueAlnIdxRows( [ "MoleculeID", "rStart", "rEnd" ] )
    
    def _numUniqueAlnIdxRows( self, keys ):
        """Return the number of rows in the alignment index which are unique over the given set of keys."""
        return len( numpy.unique( self["/AlnInfo"].asRecArray( keys ) ) )

    @property
    def version( self ):
        """Returns the version string for this cmpH5 file if it exists, else an empty string."""
        if "Version" in self._group.attrs:
            return self._group.attrs["Version"]
        return None
        
    def asRecArray( self, columns=INDEX_COLS ):
        """Given an optional list of columns, returns the data from this cmp.h5 as a numpy recarray.
        Defaults to the columns from the AlnIndex dataset."""
        colPaths = [ "/AlnInfo/%s" % col if "/" not in col else col for col in columns ]
        tcPairs = [ ( t, c ) for a,t,c in [ col.split("/") for col in colPaths ] ]
        columnsByTable = { }
        for tableName, colName in tcPairs:
            columnsByTable.setdefault( tableName, set() )
            columnsByTable[ tableName ].add( colName )
            while tableName != "AlnInfo": # Make sure we have the necessary ID columns as well
                columnsByTable[ tableName ].add( "ID" )
                tableName, colName = idMap[ tableName ]
                columnsByTable.setdefault( tableName, set() )
                columnsByTable[ tableName ].add( colName )
                
        tables = dict( [ ( tableName, self[ asPath(tableName) ].asRecArray( columns=list(columnsByTable[ tableName ]) )) 
                                                                    for tableName in columnsByTable ] )
        # Generates a mapping of ( tableName, colName ) : dataType for all tables
        col2dt = dict( sum( [ zip( [ (tableName,colName) for colName in table.dtype.fields.keys( ) ], \
                                   [ type for type,size in table.dtype.fields.values( ) ] ) \
                                            for tableName,table in tables.items() ], [] ) )
        dataTypes = zip( columns, [ col2dt[t,c] for t,c in tcPairs ] )
        ret = numpy.recarray( shape=(self.numAlnHits,), dtype=dataTypes )
        
        for ( column, ( tableName, colName ) ) in zip( columns, tcPairs ):
            ret[ column ] = self._getPerAlignment( tableName, colName, tables, col2dt )
                        
        return ret
                
    def _getPerAlignment( self, tableName, colName, tables, col2dt ):
        """Given a set of top level RecArrays, translates the given table/column into 
        AlnIndex coordinates, returning an array with one row per alignment."""
        if tableName == "AlnInfo":
            return tables["AlnInfo"][ colName ]
        nextTable, nextID = idMap[ tableName ]
        ids = self._getPerAlignment( nextTable, nextID, tables, col2dt )
        translation = numpy.empty( shape=(max(tables[tableName]["ID"])+1,), dtype=col2dt[ tableName, colName ] )
        # translation.fill( numpy.nan )
        for row in tables[ tableName ]:
            translation[ row["ID"] ] = row[ colName ]
        return translation[ ids ]
    
    def isEmpty( self ):
        """Returns true iff this is an empty cmp.h5"""
        return len(self["/AlnInfo"]) == 0
        

class ReferenceAnnotation(object):
    "Simple struct bundling attribute fields of a RefGroup"
    def __init__( self, refInfoRow ):
        self.fullName = refInfoRow['FullName']
        self.md5digest = refInfoRow['MD5']
        self.length = refInfoRow['Length']
        self.ID = refInfoRow['ID']
       

###########################################################
#
# Springfield specific code block
#
###########################################################
class SFCmpH5( CmpH5 ):
    """This class contains code specific to the Springfield .cmp.h5 file.
       Some common methods to the AstroCmpH5 should be refactor into the base class"""
    
    def __init__(self, filename, mode='r', readType = "standard", withAuxDS = False):
        """Calls the parent init, then sets a few springfield-specific values."""

        self.indexCols = INDEX_COLS
        self.alnIdxDType = INDEX_DTYPE
        CmpH5.__init__( self, filename, mode, readType, withAuxDS )
        self._cmpAlnHit = SFCmpH5AlnHit
    
    def _setVersion( self ):
        self._group.attrs['Version'] = V1_3_1_SF

class SFRCCSCmpH5( SFCmpH5 ):
    """This class contains code specific to store RCCS results from the Springfield platform."""
    def __init__( self, filename, mode = 'r', readType = "RCCS" ):
        """Uses the standard SFCmpH5 init, then takes care of extra init."""
        
        SFCmpH5.__init__( self, filename, mode, readType, withAuxDS=True )
        self._cmpAlnHit = SFCmpH5RCCSAlnHit

    def writeAlignments( self, alnHitList, refSeqName, alnGroupName, movieName, refGroupPath=None ):
        """Write CirculareCoverage information to cmp.h5"""
        self["/AlnInfo/CircularCoverage"].extend( numpy.array([ float(alnHit.CircularCoverage) for alnHit in alnHitList ], dtype=numpy.float32) )
        SFCmpH5.writeAlignments( self, alnHitList, refSeqName, alnGroupName, movieName, refGroupPath=refGroupPath, writeQV = True )

    def _setVersion( self ):
        self._group.attrs['Version'] = V1_2_0

####################################################################
#
# Internal Springfield CmpH5
#
class PBCmpH5( SFCmpH5 ):
    """This class represents the in house version of a cmp.h5 file,
    which contains extra information (Z-Scores, Exp/RunIDs, etc.)"""
    def __init__( self, filename, mode = 'r', readType = "standard" ):
        """Uses the standard SFCmpH5 init, then takes care of extra init."""
        
        SFCmpH5.__init__( self, filename, mode, readType )
        self._cmpAlnHit = PBCmpH5AlnHit

    def _setVersion( self ):
        self._group.attrs['Version'] = V1_2_0_PB

    def addMovie( self, movieName, exp=None, run=None ):
        """Adds the specified movie name to the MovieName and MovieID tables."""
        if movieName not in self["/MovieInfo"].asRecArray( )["Name"]:
            if exp == None or run == None:
                raise CmpH5Error, "You must specify valid Exp+Run when adding a movie to a PBCmpH5."
            return self["/MovieInfo"].append( Name = movieName,
                                              Exp = exp,
                                              Run = run)
        return self["/MovieInfo"].asDict("Name","ID",cache=True)[ movieName ]
        
    def writeAlignments( self, alnHitList, refSeqName, alnGroupName, movieName, exp, run, refGroupPath=None ):
        """Overloaded to add ZScore writing, experiments, and runs"""
        self.addMovie( movieName, exp=int(exp), run=int(run) )
        self["/AlnInfo/ZScore"].extend( numpy.array([ float(alnHit.zScore) for alnHit in alnHitList ], dtype=numpy.float32) )
        SFCmpH5.writeAlignments( self, alnHitList, refSeqName, alnGroupName, movieName, refGroupPath=refGroupPath )

    @property
    def reportsFolder( self ):
        """Records the primary analysis reports folder under which
        the pls/bas.h5 file for these data were stored."""
        return self.attrs[ "ReportsFolder" ]

    @property
    def primaryPipeline( self ):
        """Records the version number of the primary analysis pipeline
        which was used to generate the raw pls/bas.h5 file for these data."""
        return self.attrs[ "PrimaryPipeline" ]

  
