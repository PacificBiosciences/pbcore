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


"""Classes and routines for simple FASTA parsing."""

__all__ = [ "FastaReader",
            "FastqReader",
            "FastaEntry",
            "FastqEntry",
            "splitFasta",
            "writeFastaEntry" ]

import os
from pbcore.model.Range import Range
from ._utils import getFileHandle

class FastaReader:
    """
    Parser for FASTA input from a filename or file-like object
    """
    DEFAULT_DELIMITER = '>'
    
    def __init__(self, f):
        self.file = getFileHandle(f, "r")
        self.delimiter = self.DEFAULT_DELIMITER

    def setDelimiter(self, delimiter):
        self.delimiter = delimiter

    def __iter__(self):
        name = ''
        seqBuffer = []
        for line in self.file:
            if len(line)<1: continue
            if line[0]=='#' and self.delimiter!='#': continue
            line = line.rstrip()
            if len(line)==0: continue
            if line[0]==self.delimiter:
                if len(seqBuffer)>0:
                    yield FastaEntry( name, "".join(seqBuffer) )
                seqBuffer = []
                if len(line)==1:
                    name = ''
                else:
                    name = line[1:]
            else:
                seqBuffer.append( line )
        if len(seqBuffer)>0:
            yield FastaEntry( name, "".join(seqBuffer) )
    
class FastaEntry:
    """
    Storage class for modeling a named sequence stored in a FASTA file.
    Supports 'extended-FASTA' notation for key-value annotations.
    """
    def __init__(self, name, sequence):
        self.sequence = sequence
        self.raw_name = name
        self.__processAnnotations(name)

    def getAnnotation(self,key):
        if key in self._annotations:
            return self._annotations[key]
        return None

    def getTag(self):
        if len(self._annotations)==0:
            return self.name
        tag = '%s|%s' % ( self.name, \
            '|'.join(['%s=%s'%(k,v) for k,v in self._annotations.iteritems()] ) )
        return tag

    def __processAnnotations(self, tag):
        """
        Processes extended syntax for entry names of the form
         >readName|key1=value1|key2=value2|...
        """
        self._annotations = {}
        if tag.find('|')<0:
            self.name = tag
            return
        pairs = tag.split( '|' )
        self.name = pairs[0]
        for pair in pairs[1:]:
            if '=' not in pair:
                self.name = '%s|%s' % ( self.name, pair )
                continue
            values = pair.split('=')
            if len(values)==2:
                self._annotations[ values[0] ] = values[1]
        # revert to traditional model if this tag doesn't have kv pairs
        if len(self._annotations)==0:
            self.name = tag

    def __str__( self ):
        buffer = []
        buffer.append( ">" + self.getTag() )
        buffer.append( _prettyprint(self.sequence) )
        return os.linesep.join(buffer)
    
    def subseq(self, seqRange, name=None):
        if not name:
            name = "%s_%i_%i" % (self.name, seqRange.getStart(), seqRange.getEnd())
        return FastaEntry(name, self.sequence[seqRange.getStart():seqRange.getEnd()] )


class FastqReader:
    """
    Parser for FASTQ input from a filename or file-like object
    """
    def __init__(self, f):
        self.file = getFileHandle(f, "r")
        
    def __iter__( self ):
        qualFlag = False
        seqBuffer = []
        qualBuffer = []
        name = ""
        for line in self.file:
            line = line.rstrip()
            if len(line)==0: continue
            if line[0]=="@" and len(seqBuffer) == len(qualBuffer):
                if len(seqBuffer)>0:
                    yield FastqEntry( name, "".join(seqBuffer), "".join(qualBuffer) )
                qualFlag = False
                seqBuffer = []
                qualBuffer = []
                if len(line)==1:
                    name = ''
                else:
                    name = line[1:]
            elif (line[0] == "+" and len(qualBuffer) == 0 and not qualFlag):
                qualFlag = True
            else:
                if (qualFlag):
                    qualBuffer.append( line )
                else:
                    seqBuffer.append( line )
        if len(seqBuffer)>0:
            yield FastqEntry( name, "".join(seqBuffer), "".join(qualBuffer) )


class FastqEntry:
    def __init__( self, name, sequence, quality ):
        self.name = name
        self.sequence = sequence
        self.quality = quality

    def __str__( self ):
        buffer = []
        buffer.append( "@" + self.name )
        buffer.append( self.sequence )
        buffer.append( "+" + self.name )
        buffer.append( self.quality )
        return os.linesep.join(buffer)
    
    def subseq(self, seqRange, name=None):
        if not name: 
            name = "%s_%i_%i" % (self.name, seqRange.start, seqRange.end)
        return FastqEntry(name, self.sequence[seqRange.start : seqRange.end], self.quality[seqRange.start : seqRange.end])


def _prettyprint( sequence, width=70 ):
    return os.linesep.join( \
        [ sequence[i:i+width] for i in xrange(0,len(sequence),width) ] )

def writeFastaEntry( file, entry, width=70 ):
    file.write( '>%s%s%s%s' % ( entry.getTag(), os.linesep, \
                               _prettyprint(entry.sequence,width=width), \
                               os.linesep ) )

def splitFasta(fasta, nSplits):
    """
    Splits fasta into nSplits files and return their absolute paths
    """
    reader = FastaReader(fasta)
    n = int(nSplits)

    basePath = os.path.basename( fasta )
    fileNames = [ "%i.%s" % (i, basePath) for i in range(n) ]
    fhs = map(lambda x: open(x,"w"), fileNames)
    for idx, entry in enumerate(reader):
        fileIdx = idx % n
        print >>fhs[fileIdx], str( entry )
    del reader
    for fh in fhs: fh.close()
    splits = map(lambda x: os.path.abspath(x), fileNames)
    return splits

