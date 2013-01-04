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

__all__ = [ "BedRecord",
            "BedWriter" ]

from ._utils import getFileHandle

class BedRecord:
    """Models a record in a BED file format"""
    def __init__(self, chrom='', chromStart = 0, chromEnd = 0, name = '', score = -1.00, strand = '+'):
        self.chrom = chrom
        self.chromStart = chromStart
        self.chromEnd = chromEnd
        self.name = name
        self.score = score
        self.strand = strand
           
    def __str__(self):
        return '%s\t%d\t%d\t%s\t%.3f\t%s' % \
            (self.chrom, self.chromStart, self.chromEnd, self.name, \
              self.score, self.strand)
              
class BedWriter:
    """Outputs BED annotation track file"""
    def __init__(self, f):
        self.file = getFileHandle(f, "w")

    def writeHeader(self, name, description, useScore):
        print >> self.file, 'track name=%s description="%s" useScore=%d' \
            % (name, description, useScore)

    def writeRecord(self, record):
        print >> self.file, str(record)

