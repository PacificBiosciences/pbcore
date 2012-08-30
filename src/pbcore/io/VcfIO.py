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

# Restrict exports
__all__ = [ "VcfRecord",
            "VcfWriter" ]

from ._utils import getFileHandle

class VcfRecord:
    """Models a record in a VCF3.3 file."""
    def __init__(self):
        self.chrom = ''
        self.pos = 1
        self.id = '.'
        self.ref = ''
        self.alt = ''
        self.qual = -1.00
        self.filter = '0'
        self.info = {}
     
    def put(self, key, value):
        self.info[key] = value
   
    @staticmethod
    def getHeader():
        return 'CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO'
             
    def _getInfoString(self):
        return ';'.join(['%s=%s' % (k,v) \
            for k,v in self.info.iteritems()])

    def __str__(self):
        return '%s\t%d\t%s\t%s\t%s\t%.2f\t%s\t%s' % \
            (self.chrom, self.pos, self.id, self.ref, \
              self.alt, self.qual, self.filter, self._getInfoString())
              
class VcfWriter:
    """Outputs VCF (1000 Genomes Variant Call Format) 3.3 files"""
    def __init__(self, f):
        self.f = getFileHandle(f, "w")
        self.writeMetaData('fileformat', 'VCFv3.3')

    def writeHeader(self):
        print >> self._outfile, '#%s' % VcfRecord.getHeader()
        
    def writeMetaData(self, key, value):
        print >> self._outfile, '##%s=%s' % (key, value)

    def writeRecord( self, record ):
        print >> self._outfile, str(record)

