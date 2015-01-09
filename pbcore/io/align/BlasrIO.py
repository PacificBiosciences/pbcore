#################################################################################
# Copyright (c) 2011-2015, Pacific Biosciences of California, Inc.
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

# Author: David Alexander

from pbcore.io.base import ReaderBase

__all__ = [ "M4Record",
            "M4Reader",
            "M5Record",
            "M5Reader" ]

class MalformattedRecord(Exception): pass

class M4Record(object):
    """
    Record for alignment summary record output from BLASR -m 4 option
    """
    @classmethod
    def fromString(cls, s):
        obj = cls()
        try:
            columns = s.strip().split()
            obj.qName             = columns[0]
            obj.tName             = columns[1]
            obj.score             = int(columns[2])
            obj.percentSimilarity = float(columns[3])
            obj.qStrand           = int(columns[4])
            obj.qStart            = int(columns[5])
            obj.qEnd              = int(columns[6])
            obj.qLength           = int(columns[7])
            obj.tStrand           = int(columns[8])
            obj.tStart            = int(columns[9])
            obj.tEnd              = int(columns[10])
            obj.tLength           = int(columns[11])
            obj.mapQV             = int(columns[12])
            return obj
        except:
            raise MalformattedRecord(s)

class M4Reader(ReaderBase):
    """
    Reader for -m 4 formatted alignment summary information from BLASR
    """
    def __iter__(self):
        for line in self.file:
            yield M4Record.fromString(line)



class M5Record(object):
    """
    Record for alignment summary record output from BLASR -m 5 option
    """
    @classmethod
    def fromString(cls, s):
        obj = cls()
        try:
            columns = s.strip().split()
            obj.qName        = columns[0]
            obj.qLength      = int(columns[1])
            obj.qStart       = int(columns[2])
            obj.qEnd         = int(columns[3])
            obj.qStrand      = columns[4]
            obj.tName        = columns[5]
            obj.tLength      = int(columns[6])
            obj.tStart       = int(columns[7])
            obj.tEnd         = int(columns[8])
            obj.tStrand      = columns[9]
            obj.score        = float(columns[10])
            obj.numMatch     = int(columns[11])
            obj.numMismatch  = int(columns[12])
            obj.numIns       = int(columns[13])
            obj.numDel       = int(columns[14])
            obj.mapQV        = int(columns[15])
            obj.qAlignedSeq  = columns[16]
            obj.matchPattern = columns[17]
            obj.tAlignedSeq  = columns[18]
            return obj
        except:
            raise MalformattedRecord(s)

class M5Reader(ReaderBase):
    """
    Reader for -m 5 formatted alignment summary information from BLASR
    """
    def __iter__(self):
        for line in self.file:
            yield M5Record.fromString(line)
