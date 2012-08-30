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
from __init__ import *

from pbcore.model.AlignmentHit import AlignmentHit

__version__="$Revision$ $Change$"


class CmpH5AlnHit( AlignmentHit ):
    """Base class for the extended AlignmentHit, customized for
    the cmp.h5 format."""

    def __init__( self, sourceAlnHit=None ):
        """Can be constructed from another alignment hit 
        (copies __dict__ over), or denovo."""

        if sourceAlnHit:
            self.__dict__ = sourceAlnHit.__dict__.copy()
        else:
            AlignmentHit.__init__( self )

        self._colToValue = None
        self.hasPulseInfo = False

    def __str__( self ):
        """Replaces the standard Agar string representation"""
        ret = "Q:\t%s\n" % "\t".join( map( str, [ self.query_strand, self.query_start, self.query_end, self.query_id ] ) ) 
        ret += "T:\t%s\n" % "\t".join( map( str, [ self.target_strand, self.target_start, self.target_end, self.target_id ] ) )  
        ret += "Aln:\t%s\n" % "\t".join( map( str, [ self.score, self.alignedLength ] ) )
        return ret

    def loadPulseInfo( self, alnIdxRow, pulseDatasets ):
        """Loads pulse stats into this alignment hit. Sets the .hasPulseInfo flag
        to indicate their presence. PulseDatasets should be a dictionary mapping 
        PulseMetric:CmpDataset."""
        self.pulseInfo = {}
        for ( name, dataset ) in pulseDatasets.items():
            self.pulseInfo[ name ] = dataset[alnIdxRow["Offset_begin"]:alnIdxRow["Offset_end"]]
        self.hasPulseInfo = True

    def __contains__( self, key ):
        if self.hasPulseInfo:
            return key in self.pulseInfo
        return False

    def __getitem__( self, key ):
        """Indexes into the pulse metrics if they exist."""
        if self.hasPulseInfo and key in self.pulseInfo:
            return self.pulseInfo[ key ]

        raise KeyError, "Unable to locate key '%s' in CmpAlnHit. Maybe pulse info is not loaded?" % ( key )

    def loadFromCmpH5Dataset( self, rowNum, alnArrayDataset, cmpH5, loadSequence=True, computeAlnPosTranslations=False ):
        """Loads all relevant data from the AlignmentIndex dataset row
        and the relevant rows in the alnArrayDataset."""

        alnInfoRow = cmpH5["/AlnInfo"].asRecArray( )[ rowNum ]

        offsetBegin, offsetEnd = alnInfoRow["Offset_begin"], alnInfoRow["Offset_end"]
        self.alignedLength = offsetEnd - offsetBegin

        self.alignmentId    = alnInfoRow["AlnID"]
        self.target_start   = alnInfoRow["tStart"]
        self.target_end     = alnInfoRow["tEnd"]
        self.query_start    = alnInfoRow["rStart"]
        self.query_end      = alnInfoRow["rEnd"]
        self.nMismatch      = alnInfoRow["nMM"]
        self.nIns           = alnInfoRow["nIns"]
        self.nDel           = alnInfoRow["nDel"]
        self.nMatch         = alnInfoRow["nM"]
        self.mapQV          = alnInfoRow["MapQV"]
        self.moleculeId     = alnInfoRow["MoleculeID"]
        self.target_strand  = "+" if alnInfoRow["RCRefStrand"] == 0 else "-"
        self.query_strand   = "+"

        self.query_id = self._buildQueryName( alnInfoRow, cmpH5 ) 
        self.target_id = "UnknownReference" # This should be updated by the ReadGroup.
    
        self.hasMatchInfo = True

        aln_dset_slice = None

        if loadSequence:
            aln_dset_slice = alnArrayDataset[offsetBegin:offsetEnd]
            self.alignedQuery = fastQueryMap[ aln_dset_slice ].tostring()
            self.alignedTarget = fastTargetMap[ aln_dset_slice ].tostring()
            self.hasAlignment = True
        
        if computeAlnPosTranslations:
            if aln_dset_slice is None:
                aln_dset_slice = alnArrayDataset[offsetBegin:offsetEnd]
            GAP = base2hexMap["-"]
            self._aln2query = self.query_start - 1 + numpy.cumsum(((aln_dset_slice >> 4) & 15) != GAP)
            if self.target_strand == '+':
                self._aln2target = self.target_start - 1 + numpy.cumsum((aln_dset_slice & 15) != GAP)
            else:
                self._aln2target = self.target_start - 1 + numpy.cumsum((aln_dset_slice & 15)[::-1] != GAP)[::-1]

            self._query2aln = numpy.empty(self.query_end-self.query_start, dtype=int)
            self._target2aln = numpy.empty(self.target_end-self.target_start, dtype=int)

            # TODO: gap1, gap2 should always be 1 (0 occurs when alignment starts with a gap)
            q2a = numpy.flatnonzero(numpy.diff(self._aln2query))
            gap1 = self.query_end-self.query_start - len(q2a)
                 
            self._query2aln[0] = 0
            self._query2aln[gap1:] = q2a + 1
            
            if self.target_strand == '+':
                t2a = numpy.flatnonzero(numpy.diff(self._aln2target))
            else:
                t2a = numpy.flatnonzero(numpy.diff(self._aln2target[::-1]))
            
            gap2 = self.target_end-self.target_start - len(t2a)

            self._target2aln[0] = 0
            self._target2aln[gap2:] = t2a + 1
            
            if self.target_strand == '-':
                self._target2aln = len(self._aln2target) - 1 - self._target2aln
            

    def _buildQueryName( self, alnData ):
        """This method should be implemented by the subclass with instrument/version specific information."""
        raise Exception, "This method should be implemented in a subclass"

    def _alnDataFromQueryId( self, queryId ):
        """This method should be implemented by the subclass with instrument/version specific information."""
        raise Exception, "This method should be implemented in a subclass"

    @property
    def alignmentIndexData( self ):
        """Generates a mapping of column name to integer to be written to an 
        alignmentIndex row describing this hit."""
                                        
        if self._colToValue != None:
            return self._colToValue

        colToValue = { }
        colToValue["tStart"]        = min( self.target_start, self.target_end )
        colToValue["tEnd"]          = max( self.target_start, self.target_end )
        colToValue["RCRefStrand"]   = 0 if self.query_strand == self.target_strand else 1
        colToValue["rStart"]        = min( self.query_start, self.query_end )
        colToValue["rEnd"]          = max( self.query_start, self.query_end )
        colToValue["nM"]            = self.nMatch
        colToValue["nMM"]           = self.nMismatch
        colToValue["nIns"]          = self.nIns
        colToValue["nDel"]          = self.nDel
        colToValue["MapQV"]         = self.mapQV
       
        colToValue.update( self._alnDataFromQueryId( self.query_id ) )

        self._colToValue = colToValue
        return colToValue

    @property
    def alignmentArray( self ):
        """Constructs the integer array describing the alignment, suitable
        for appending into the AlignmentArray table."""
        query = self.alignedQuery if self.query_strand == "+" else revCompSeq( self.alignedQuery )
        target = self.alignedTarget if self.query_strand == "+" else revCompSeq( self.alignedTarget )

        return [ ( ( base2hexMap[query[x]] << 4) | base2hexMap[target[x]] )
                               for x in xrange(len(query)) ]
    
class SFCmpH5AlnHit( CmpH5AlnHit ):
    """Contains the Springfield-specfic AlignmentHit extensions"""

    def __init__( self, sourceAlnHit=None ):
        """Can build on an AlignmentHit, nothing,
        or an AlignmentIndex row and an AlignmentArray
        Dataset."""
    
        CmpH5AlnHit.__init__( self, sourceAlnHit )
        self.indexCols = INDEX_COLS 
        if not sourceAlnHit:
            self.target_id = "UnknownReference"

    def _buildQueryName( self, alnData, cmpH5 ):
        """Constructs the query name (query_id) of this alignmentHit from
        a dictionary of alignmentData"""
        movieName = cmpH5["/MovieInfo"].asDict("ID","Name",cache=True)[ int(alnData["MovieID"]) ]
        return "%s/%d/%d_%d" % ( movieName, alnData["HoleNumber"], alnData["rStart"], alnData["rEnd"] ) 
        
    def _alnDataFromQueryId( self, queryId ):
        """Given a query Id, returns a dictionary mapping names of alignmentIndex Columns
        to their appropriate values."""

        ( movieDateStamp, movieTimeStamp, machine,
        zmwSet, partOfStrobe, zmwHoleNumber, subreadId ) = self._parseReadId( queryId )

        colToValue = { }
        
        colToValue["HoleNumber"]    = zmwHoleNumber
        colToValue["MoleculeID"]    = 0
        colToValue["SetNumber"]     = zmwSet
        colToValue["StrobeNumber"]  = partOfStrobe
        colToValue["nBackRead"]     = 0
        colToValue["nReadOverlap"]  = 0

        return colToValue

    def _parseReadId( self, readId ):
        """Parses the relevant information out of an Springfield-formatted read ID."""

        # set defaults
        movieDateStamp = "m000000";
        movieTimeStamp = "000000"; 
        machine = "DUM";
        zmwSet = "0";
        partOfStrobe = "0";
        subreadId = 0;
        zmwHoleNumber = 0;
    
        try:
            # parse the various flavors of ids
            readId = readId.split("|")[0] # remove any annotations
            elts = readId.split("/")
            if len(elts) == 2:
                movieName, zmwHoleNumber = elts
            else:
                movieName = elts[0]
                zmwHoleNumber = elts[1]
                ignoreSubreadId = elts[2]

            zmwHoleNumber = int(zmwHoleNumber)
            subreadId = int(subreadId)

            try:
                elts = movieName.split("_")
                if len(elts) >= 6:
                    movieDateStamp, movieTimeStamp, machine, chipId, zmwSet, partOfStrobe = elts[0:6]
                elif len(elts) == 5:
                    movieDateStamp, movieTimeStamp, machine, zmwSet, partOfStrobe = elts
                else:
                    raise ValueError
                zmwSet = int(zmwSet[1:])  #ignore the prefix
                partOfStrobe = int(partOfStrobe[1:])
            except ValueError:
                raise CmpH5Error, "Found movie that does not appear to be valid (%s) " % movieName

        except ValueError:
            raise CmpH5Error, "Unable to parse SF readId: %s" % readId

        return movieDateStamp, movieTimeStamp, machine, zmwSet, partOfStrobe, zmwHoleNumber, subreadId

####################################################################
#
# Springfield RCCS CmpH5
#
class SFCmpH5RCCSAlnHit( SFCmpH5AlnHit ):
    def __init__( self, sourceAlnHit=None ):
        """Can build on an AlignmentHit, nothing,
        or an AlignmentIndex row and an AlignmentArray
        Dataset."""
    
        SFCmpH5AlnHit.__init__( self, sourceAlnHit )
        self.QualityValue = None
        self.CCC = 0

    def loadFromCmpH5Dataset( self, rowNum, alnArrayDataset, cmpH5, loadSequence, computeAlnPosTranslations ):
        SFCmpH5AlnHit.loadFromCmpH5Dataset( self, rowNum, alnArrayDataset, cmpH5, loadSequence, computeAlnPosTranslations )
        alnInfoRow = cmpH5["/AlnInfo"].asRecArray( )[ rowNum ]
        self.CircularCoverage = int( alnInfoRow["CircularCoverage"] )


####################################################################
#
# Internal Springfield CmpH5
#
class PBCmpH5AlnHit( SFCmpH5AlnHit ):
    """Overloaded for added in house functionality"""

    def loadFromCmpH5Dataset( self, rowNum, alnArrayDataset, cmpH5, loadSequence, computeAlnPosTranslations ):
        """Overloaded to handle ZScore"""
        SFCmpH5AlnHit.loadFromCmpH5Dataset( self, rowNum, alnArrayDataset, cmpH5, loadSequence, computeAlnPosTranslations )
        alnInfoRow      = cmpH5["/AlnInfo"].asRecArray( )[ rowNum ]
        self.zScore     = float( alnInfoRow["ZScore"] )
        myMovieId       = int( alnInfoRow["MovieID"] )
        self.experiment, self.run = map( str, cmpH5["/MovieInfo"].asDict("ID",["Exp","Run"])[ myMovieId ] )

        


