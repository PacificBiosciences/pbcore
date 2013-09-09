from pbcore.io.base import ReaderBase
from collections import namedtuple, OrderedDict, Sequence
import mmap, numpy as np
from os.path import abspath, expanduser

__all__ = [ "FastaTable" ]

FaiRecord = namedtuple("FaiRecord", ("name", "length", "offset", "lineWidth", "stride"))

def faiFilename(fastaFilename):
    return fastaFilename + ".fai"

def loadFastaIndex(filename):
    tbl = OrderedDict()
    try:
        for line in open(filename):
            name, length_, offset_, lineWidth_, blen_ = line.split()
            record = FaiRecord(name, int(length_), int(offset_),
                               int(lineWidth_), int(blen_))
            tbl[name] = record
        return tbl
    except:
        raise IOError,                                                        \
            "Companion FASTA index (.fai) file not found or malformatted! " + \
            "Use 'samtools faidx' to generate FASTA index."

def fileOffset(faiRecord, pos):
    """
    Find the in-file position (in bytes) corresponding to the position
    in the named contig, using the FASTA index.
    """
    q, r = divmod(pos, faiRecord.lineWidth)
    offset = faiRecord.offset + q*faiRecord.stride + r
    return offset

class MmappedFastaContig(Sequence):
    """
    A string-like view of a contig sequence that is backed by a file
    using mmap.
    """
    def __init__(self, view, faiRecord):
        self.view = view
        self.faiRecord = faiRecord

    def __getitem__(self, spec):
        if isinstance(spec, slice):
            start, stop, stride = spec.indices(len(self))
            if stride != 1:
                raise ValueError, "Unsupported stride"
        elif spec < 0:
            start = self.faiRecord.length + spec
            stop = start + 1
            stride = 1
        else:
            start = spec
            stop = start + 1
            stride = 1
        if not (0 <= start <= stop <= self.faiRecord.length):
            raise IndexError, "Out of bounds"
        startOffset = fileOffset(self.faiRecord, start)
        endOffset   = fileOffset(self.faiRecord, stop)
        snip = self.view[startOffset:endOffset].replace("\n", "")
        return snip

    def __len__(self):
        return self.faiRecord.length


class FastaTableRecord(object):
    def __init__(self, view, faiRecord):
        self.view = view
        self.faiRecord = faiRecord

    @property
    def name(self):
        return self.faiRecord.name

    @property
    def sequence(self):
        return MmappedFastaContig(self.view,
                                  self.faiRecord)


class FastaTable(ReaderBase):
    def __init__(self, filename):
        self.filename = abspath(expanduser(filename))
        self.file = open(self.filename, "r")
        self.faiFilename = faiFilename(self.filename)
        self.fai = loadFastaIndex(self.faiFilename)
        self.contigById = dict(self.fai)
        self.contigById.update(zip(xrange(len(self.fai)),
                                   self.fai.itervalues()))
        self.view = mmap.mmap(self.file.fileno(), 0,
                              prot=mmap.PROT_READ)

    def __getitem__(self, name):
        if name in self.contigById:
            return FastaTableRecord(self.view, self.contigById[name])
        else:
            raise IndexError, "Contig not in FastaTable"

    def __iter__(self):
        return (self[key] for key in self.fai)
