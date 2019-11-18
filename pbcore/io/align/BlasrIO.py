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
