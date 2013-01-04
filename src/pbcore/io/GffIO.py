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

"""
I/O support for GFF3 files.

The specification for the GFF format is available at
    http://www.sequenceontology.org/gff3.shtml
"""

# Restrict our exports.
__all__ = [ "Gff3Record",
            "GffReader",
            "GffWriter",
            "parseGffLine"  ]

SEQUENCE_SOURCE = 'SMRT'

from ._utils import getFileHandle

class Gff3Record:
    """Models a record in a GFF3 file."""
    def __init__(self, seqName=''):
        self.seqid = seqName
        self.source = '.'
        self.type = '' 
        self.start = 0
        self.end = 0
        self.score = 0.0
        self.strand = '+'
        self.phase = '.'
        self.attributes = []

    def put( self, key, value ):
        self.attributes.append( (key, value) )

    def getAttrVal(self, key):
        """Returns a value for the given attribute key if found, otherwise None"""
        val = [t[1] for t in self.attributes if t[0] == key]
        if len(val) == 1:
            return val[0]
        else:
            return None

    def _getAttributeString( self ):
        return ';'.join( [ '%s=%s' % (k,self._formatField(v)) \
            for (k,v) in self.attributes ] )

    @staticmethod
    def _formatField(field):
        if field == None:
            return "."
        elif type(field) == float:
            return "%.2f" % field
        else:
            return "%s" % field
    
    def __str__(self):
        return "\t".join(map(self._formatField, (self.seqid, self.source, self.type, self.start, 
                                                 self.end, self.score, self.strand, self.phase,
                                                 self._getAttributeString())))

def parseGffLine( line ):
    values = line.split('\t')
    record = Gff3Record()
    try:
        record.seqid = values[0]
        record.source = values[1]
        record.type  = values[2]
        record.start = int(values[3])
        record.end = int(values[4])
        if values[5]=='.':
            # this doesn't really keep with the semantics of GFF
            # (but what kind of format specification allows float and null?)
            record.score = 0.0
        else:
            record.score = float(values[5])
        record.strand = values[6]
        record.phase = values[7]
        record.attributes = []
        for kvPair in values[8].strip().split(';'):
            vals = kvPair.split('=')
            if len(vals)==2:
                record.attributes.append( (vals[0], vals[1]) )
        return record
    except IndexError:
        print >> sys.stderr, 'Unexpected GFF line format: %s' % values


class GffReader:
    def __init__(self, f):
        self.file = getFileHandle(f, "r")
        self.seqMap = {}
        self.headers = []

    def __iter__( self ):
        for line in self.file:
            if line[0]=='#':
                # Keep track of the headers!
                self.headers.append(line)
                splitFields  = line.replace('#', '').split(' ')
                field = splitFields[0]
                value = " ".join( splitFields[1:] )
                if field == 'sequence-header':
                    [internalTag, delim, externalTag] = value.strip().partition(' ')
                    self.seqMap[internalTag] = externalTag
                continue
            record = parseGffLine( line[:-1] )
            if record is None:
                continue
            yield record

    def close( self ):
        self.file.close()

class GffWriter:
    """Simple class for producing a GFF3 file from python code"""
    def __init__( self, f ):
        self._outfile = getFileHandle(f, "w")
        self.writeMetaData( 'gff-version', '3' )

    def writeMetaData( self, key, value ):
        # per the GFF3 spec: meta-data should be written as a
        # space-delimited key-value pair, not tab-delimited
        # (addresses bug 11270)
        print >>self._outfile, '##%s %s' % ( key, value )

    def writeRecord( self, record ):
        assert isinstance(record, Gff3Record)
        print >>self._outfile, str(record)

    def writeLine(self, string):
        print >>self._outfile, string



