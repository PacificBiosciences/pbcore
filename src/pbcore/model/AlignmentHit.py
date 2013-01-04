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

__doc__="""Base class for representing a single pairwise alignment"""
import os, sys
import numpy

class AlignmentHit:

    def __len__( self ):
        return self.query_end - self.query_start
    
    def __init__( self ):
        self.query_length, self.query_id, self.query_start, \
            self.query_end, self.query_strand = 0, None, 0, 0, None
        self.target_length, self.target_id, self.target_start, \
            self.target_end,self.target_strand = 0, None, 0, 0, None
        self.score = 0
        self.zScore= None 
        self.mapQV = 255
        self._clearMatchInfo()

    def _clearMatchInfo( self ):
        
        self.hasMatchInfo = False
        self.alignedLength = 0
        self.nMatch = 0
        self.nMismatch = 0
        self.nIns = 0
        self.nDel = 0
        
        self.hasAlignments = False
        self.alignedQuery = ""
        self.alignedTarget = ""
        self._aln2query, self._aln2target, self._query2aln, self._target2aln = None, None, None, None

    def setMatchInfo(self, nMatch, nMismatch, nIns, nDel, alignedLength, \
                     alignedQuery=None, alignedTarget=None):
        """ Call for a fully functional hit (e.g. for use in Z-score calc in compare sequences"""
        self.nMatch         = nMatch
        self.nMismatch      = nMismatch
        self.nIns           = nIns
        self.nDel           = nDel
        self.alignedLength  = alignedLength
        self.hasMatchInfo   = True
 
        if (alignedQuery and alignedTarget):
            self.alignedQuery  = alignedQuery
            self.alignedTarget = alignedTarget
            self.hasAlignment  = True
    
    def getNumAllErrors( self ):
        " Subclasses override. "
        return 0

    def parseAgar( self, line ):
        """ Parses the "agar" format for alignments
        from exonerate.
        See exonerate(1) man page for description of format. 
        Returns a string containing the portion of the line after
        column 12 (the extended columns)."""
        try:
            values  = line.split()
            if values[0]!='agar:':
                 raise AlignmentParseException( "Line doesn't "\
                     "look to be in agar format" + os.linesep + \
                     line + os.linesep + 'No agar: prefix' )
            self.query_length = int(values[1])
            self.target_length = int(values[2])
            self.query_id = values[3]
            self.query_start = int(values[4])
            self.query_end = int(values[5])
            self.query_strand = values[6]
            self.target_id = values[7]
            self.target_start = int(values[8])
            self.target_end = int(values[9])
            self.target_strand = values[10]
            self.score = int(values[11])
            if len(values)>12:
                return " ".join(values[12:])
            else:
                return ''
        except Exception, e:
            raise AlignmentParseException( "Line doesn't "\
                  "look to be in agar format" + os.linesep + \
                  line + os.linesep + str(e) )
    def __str__( self ):
        return 'agar: %d %d %s %d %d %s %s %d %d %s %d' % \
            ( self.query_length, self.target_length, \
              self.query_id, self.query_start, self.query_end, \
              self.query_strand, self.target_id, self.target_start, \
              self.target_end, self.target_strand, self.score )


    def constructBuffer(self):
         buffer = []

         buffer.append("qi:%10s" % self.query_id)
         buffer.append("qs:%6s" % self.query_start)
         buffer.append("qe:%6s" % self.query_end)
         buffer.append("ql:%7s" % self.query_length)
         buffer.append("qs:%s" % self.query_strand)

         buffer.append("ti:%10s" % self.target_id)
         buffer.append("ts:%7s" % self.target_start)
         buffer.append("te:%7s" % self.target_end)
         buffer.append("tl:%7s" % self.target_length)
         buffer.append("ts:%s" % self.target_strand)

         buffer.append("s:%i" % self.score) 
         return buffer

    def readableLine( self ):
        buffer = self.constructBuffer()     
        return " ".join(buffer)
 
    def readable( self ):
        buffer = self.constructBuffer()     
        return "\n".join(buffer)

    def validateHit(self):
        """Checks that a hit conforms to the HDF5 convention:
            - 0-based half-open interval coordinates
            - start < end for query and target
            - coordinates are unaligned (i.e. ungapped)
            """

        if not (self.alignedLength == len(self.alignedQuery)):
            print >>sys.stderr, "alignedLength: %i != len(alignedQuery): %i" % (self.alignedLength, len(self.alignedQuery) )
            return False
        
        if not (self.alignedLength == len(self.alignedTarget)):
            print >>sys.stderr, "alignedLength: %i != len(alignedTarget): %i" % (self.alignedLength, len(self.alignedTarget) )
            return False

        if not (self.query_start < self.query_end): 
            print >>sys.stderr, "query_start: %i !< query_end: %i" % (self.query_start, self.query_end)
            return False
            
        if not (self.target_start < self.target_end):
            print >>sys.stderr, "target_start: %i !< target_end: %i" % (self.target_start, self.target_end)
            return False
            
        if not (len(self.alignedQuery) - self.alignedQuery.count("-") == self.query_end - self.query_start):
            print >>sys.stderr, "len(alignedQuery): %i - count(-): %i = %i != %i = query_end: %i - query_start: %i"                 \
                % (len(self.alignedQuery), self.alignedQuery.count("-"), len(self.alignedQuery) - self.alignedQuery.count("-"),     \
                        self.query_end - self.query_start, self.query_end, self.query_start)
            return False

        if not (len(self.alignedTarget) - self.alignedTarget.count("-") == self.target_end - self.target_start):
            print >>sys.stderr, "len(alignedTarget): %i - count(-): %i = %i != %i = target_end: %i - target_start: %i"              \
                % (len(self.alignedTarget), self.alignedTarget.count("-"), len(self.alignedTarget) - self.alignedTarget.count("-"), \
                        self.target_end - self.target_start, self.target_end, self.target_start)
            return False

        return True
    
    def fullyAligned(self, tolerance=30, minFraction=0.90):
        return (self.query_start < tolerance and 
                self.query_length - self.query_end < tolerance and
                minFraction * self.query_length < (self.query_end - self.query_start) )

    def hasFullOverlap(self, tolerance=30):
        assert(self.target_strand == "+")

        # query contained
        if self.query_start < tolerance and (self.query_length   - self.query_end  < tolerance): return True
        
        # target contained
        if self.target_start < tolerance and (self.target_length - self.target_end < tolerance): return True

        if self.query_strand == "+":
            # --->
            #   --->
            if (self.query_length - self.query_end < tolerance) and (self.target_start < tolerance): return True
            #   --->
            # --->
            if (self.target_length - self.target_end < tolerance) and (self.query_start < tolerance): return True
        else:
            # --->
            #   <---
            if (self.query_length - self.query_end < tolerance) and (self.target_length - self.target_end < tolerance): return True
            #   --->
            # <---
            if (self.query_start < tolerance) and (self.target_start < tolerance): return True

        return False

    # TODO obo error in coords here?
    def queryExtendsTargetLeft(self, minExtend=0):
        assert(self.target_strand == "+")
        if (self.query_strand == "+"):
            if (self.target_start + minExtend < self.query_start): return True
        else:
            if (self.target_length - self.target_end + minExtend < self.query_start): return True
        return False

    def queryExtendsTargetRight(self, minExtend=0):
        assert(self.target_strand == "+")
        if (self.query_strand == "+"):
            if (self.target_length - self.target_end + minExtend < self.query_length - self.query_end): return True
        else:
            if (self.target_start + minExtend < self.query_length - self.query_end): return True
        return False

    def queryContained(self, minExtend=0):
        assert(self.target_strand == "+")
        if self.queryExtendsTargetLeft(minExtend=minExtend) or self.queryExtendsTargetRight(minExtend=minExtend): return False
        return True

    @property
    def identity(self):
        hitLength= (self.query_end - self.query_start + self.target_end - self.target_start)/2.0
        return (hitLength + self.score/2.0) / hitLength
                   
    def switchTargetQuery(self):
        self.query_id, self.query_start, self.query_end, self.query_strand, self.query_length,      \
        self.target_id, self.target_start, self.target_end, self.target_strand, self.target_length, \
        self.alignedQuery, self.alignedTarget =                                                     \
        self.target_id, self.target_start, self.target_end, self.target_strand, self.target_length, \
        self.query_id, self.query_start, self.query_end, self.query_strand, self.query_length,  \
        self.alignedTarget, self.alignedQuery
    
    def stripGaps(self):
        """Trim off starting and ending gaps from the target and query sequences"""
        if self.alignedTarget.startswith("-"):
            # find the last "-" in the target beginning
            for idx, ch in enumerate(self.alignedTarget):
                if ch != "-": break
    
            # fix query, adjusting coords
            self.query_start   += (idx - self.alignedQuery[0:idx].count("-"))
            self.alignedQuery  =  self.alignedQuery[idx:]
            self.alignedLength =  len(self.alignedQuery)
    
            # fix target, adjusting coords if necessary
            self.alignedTarget =  self.alignedTarget[idx:]
            if self.target_strand == "-":
                self.target_end -= 1
    
        # and trim the ending gaps "-"
        if self.alignedTarget.endswith("-"):
            # find the initial "-" in the target tail
            for idx in range(-1,-len(self.alignedTarget),-1):
                ch = self.alignedTarget[idx]
                if ch != "-": break
            idx += 1 # to make it point to the initial "-"
    
            self.query_end -= (- idx - self.alignedQuery[idx:].count("-"))
            self.alignedQuery  =  self.alignedQuery[:idx]
            self.alignedLength = len(self.alignedQuery)
            self.alignedTarget = self.alignedTarget[:idx]
            if self.target_strand == "+":
                self.target_end -= 1

    @property
    def queryToAlnPos(self):
        if self._query2aln is None:
            self._computeAlnPosTranslations()
        return self._query2aln

    @property
    def targetToAlnPos(self):
        if self._target2aln is None:
            self._computeAlnPosTranslations()
        return self._target2aln

    @property
    def alnToQueryPos(self):
        if self._aln2query is None:
            self._computeAlnPosTranslations()
        return self._aln2query

    @property
    def alnToTargetPos(self):
        if self._aln2target is None:
            self._computeAlnPosTranslations()
        return self._aln2target

    def _computeAlnPosTranslations(self):
        self._aln2query = numpy.empty(self.alignedLength, dtype=int)
        self._aln2target = numpy.empty(self.alignedLength, dtype=int)
        self._query2aln = numpy.empty(self.query_end-self.query_start, dtype=int)
        self._target2aln = numpy.empty(self.target_end-self.target_start, dtype=int)

        query_pos = self.query_start-1 if self.query_strand is '+' else self.query_end
        target_pos = self.target_start-1 if self.target_strand is '+' else self.target_end

        query_increment = 1 if self.query_strand is '+' else -1
        target_increment = 1 if self.target_strand is '+' else -1
        
        for aln_pos in range(self.alignedLength):
            if self.alignedQuery[aln_pos] != '-':
                query_pos += query_increment
                self._query2aln[query_pos-self.query_start] = aln_pos
            if self.alignedTarget[aln_pos] != '-':
                target_pos += target_increment
                self._target2aln[target_pos-self.target_start] = aln_pos
            
            self._aln2query[aln_pos] = query_pos
            self._aln2target[aln_pos] = target_pos

    def _isReadOverhanging (self, overhangLength=50, overhangUpstream=0, overhangDownstream=0, leftOnly=False, rightOnly=False):
        """Checks if a read is overhanging at the end of a contig"""
        target_start, target_end = self.target_start, self.target_end
        target_length, target_strand = self.target_length, self.target_strand
        query_start, query_end = self.query_start, self.query_end
        query_length, query_strand = self.query_length, self.query_strand
        # Check Negative Strand Alignments
        if (query_strand == "-" or target_strand == "-"):
            if ((target_length - target_end) <= (query_start-overhangUpstream) and     
                 query_start >= overhangLength):
                if (not rightOnly):
                    return True
            if (target_start <= (query_length-query_end-overhangDownstream) and 
                 (query_length-query_end) >= overhangLength):
                if (not leftOnly):
                    return True
        # Check Positive Strand Alignments
        else:
            if ((target_length - target_end) <= (query_length-query_end-overhangDownstream) and     
                 (query_length-query_end) >= overhangLength):
                if (not rightOnly):
                    return True
            if (target_start <= query_start-overhangUpstream and query_start >= overhangLength):
                if (not leftOnly):
                    return True
        return False

class AlignmentParseException( Exception ):
    def __init__( self, msg ):
        self.msg = msg

    def __str__( self ):
        return self.msg

