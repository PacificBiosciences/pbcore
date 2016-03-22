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

"""
Streaming I/O support for FASTA files.
"""

__all__ = [ "FastaRecord",
            "FastaReader",
            "FastaWriter",
            "FastaTable",
            "IndexedFastaReader",
            "splitFastaHeader"]

from .base import ReaderBase, WriterBase
from ._utils import splitFileContents
from pbcore import sequence
from pbcore.util.decorators import deprecated

import mmap, numpy as np, re
from collections import namedtuple, OrderedDict, Sequence
from os.path import abspath, expanduser, isfile, getsize


def splitFastaHeader( name ):
    """
    Split a FASTA/FASTQ header into its id and comment components
    """
    nameParts = re.split('\s', name, maxsplit=1)
    id_ = nameParts[0]
    if len(nameParts) > 1:
        comment = nameParts[1].strip()
    else:
        comment = None
    return (id_, comment)

class FastaRecord(object):
    """
    A FastaRecord object models a named sequence in a FASTA file.
    """
    DELIMITER = ">"
    COLUMNS   = 60

    def __init__(self, header, sequence):
        try:
            assert "\n" not in header
            assert "\n" not in sequence
            assert self.DELIMITER not in sequence
            self._header = header
            self._sequence = sequence
            self._id, self._comment = splitFastaHeader(header)
        except AssertionError:
            raise ValueError("Invalid FASTA record data")

    @property
    def header(self):
        """
        The header of the sequence in the FASTA file, equal to the entire
        first line of the FASTA record following the '>' character.

        .. warning::

           You should almost certainly be using "id", not "header".
        """
        return self._header

    @property
    def name(self):
        """
        DEPRECATED: The name of the sequence in the FASTA file, equal to
        the entire FASTA header following the '>' character
        """
        return self._header

    @property
    def id(self):
        """
        The id of the sequence in the FASTA file, equal to the FASTA header
        up to the first whitespace.
        """
        return self._id

    @property
    def comment(self):
        """
        The comment associated with the sequence in the FASTA file, equal to
        the contents of the FASTA header following the first whitespace
        """
        return self._comment

    @property
    def sequence(self):
        """
        The sequence for the record as present in the FASTA file.
        (Newlines are removed but otherwise no sequence normalization
        is performed).
        """
        return self._sequence

    @property
    @deprecated
    def length(self):
        """
        Get the length of the FASTA sequence
        """
        return len(self._sequence)

    @classmethod
    def fromString(cls, s):
        """
        Interprets a string as a FASTA record.  Does not make any
        assumptions about wrapping of the sequence string.
        """
        try:
            lines = s.splitlines()
            assert len(lines) > 1
            assert lines[0][0] == cls.DELIMITER
            header = lines[0][1:]
            sequence = "".join(lines[1:])
            return FastaRecord(header, sequence)
        except AssertionError:
            raise ValueError("String not recognized as a valid FASTA record")

    def reverseComplement(self, preserveHeader=False):
        """
        Return a new FastaRecord with the reverse-complemented DNA sequence.
        Optionally, supply a name
        """
        rcSequence = sequence.reverseComplement(self.sequence)
        if preserveHeader:
            return FastaRecord(self.header, rcSequence)
        else:
            rcName = '{0} [revcomp]'.format(self.header.strip())
            return FastaRecord(rcName, rcSequence)

    def __len__(self):
        return len(self._sequence)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.header   == other.header and
                    self.sequence == other.sequence)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "<FastaRecord: %s>" % self.header

    def __str__(self):
        """
        Output a string representation of this FASTA record, observing
        standard conventions about sequence wrapping.
        """
        return (">%s\n" % self.header) + \
            wrap(self.sequence, self.COLUMNS)


class FastaReader(ReaderBase):
    """
    Streaming reader for FASTA files, useable as a one-shot iterator
    over FastaRecord objects.  Agnostic about line wrapping.

    Example:

    .. doctest::

        >>> from pbcore.io import FastaReader
        >>> from pbcore import data
        >>> filename = data.getTinyFasta()
        >>> r = FastaReader(filename)
        >>> for record in r:
        ...     print record.header, len(record.sequence)
        ref000001|EGFR_Exon_2 183
        ref000002|EGFR_Exon_3 203
        ref000003|EGFR_Exon_4 215
        ref000004|EGFR_Exon_5 157
        >>> r.close()

    """
    DELIMITER = ">"

    def __iter__(self):
        try:
            parts = splitFileContents(self.file, ">")
            assert "" == next(parts)
            for part in parts:
                yield FastaRecord.fromString(">" + part)
        except AssertionError:
            raise ValueError("Invalid FASTA file {f}".format(f=self.filename))


class FastaWriter(WriterBase):
    """
    A FASTA file writer class

    Example:

    .. doctest::

        >>> from pbcore.io import FastaWriter
        >>> with FastaWriter("output.fasta.gz") as writer:
        ...     writer.writeRecord("dog", "GATTACA")
        ...     writer.writeRecord("cat", "CATTACA")

    (Notice that underlying file will be automatically closed after
    exit from the `with` block.)

    .. testcleanup::

        import os; os.unlink("output.fasta.gz")

    """
    def writeRecord(self, *args):
        """
        Write a FASTA record to the file.  If given one argument, it is
        interpreted as a ``FastaRecord``.  Given two arguments, they
        are interpreted as the name and the sequence.
        """
        if len(args) not in (1, 2):
            raise ValueError
        if len(args) == 1:
            record = args[0]
        else:
            header, sequence = args
            record = FastaRecord(header, str(sequence))
        self.file.write(str(record))
        self.file.write("\n")


##
## Utility functions for FastaReader
##
def wrap(s, columns):
    return "\n".join(s[start:start+columns]
                     for start in xrange(0, len(s), columns))



# ------------------------------------------------------------------------------
# IndexedFastaReader: random access Fasta class
#

FaiRecord = namedtuple("FaiRecord", ("id", "comment", "header", "length", "offset", "lineWidth", "stride"))

def faiFilename(fastaFilename):
    return fastaFilename + ".fai"

def loadFastaIndex(faidxFilename, fastaView):

    if not isfile(faidxFilename): # os.path.isfile
        raise IOError("Companion FASTA index (.fai) file not found or "
                      "malformatted! Use 'samtools faidx' to generate FASTA "
                      "index.")

    tbl = []
    # NB: We have to look back in the FASTA to find the full header;
    # only "id" makes it into the fai.
    offsetEnd = 0
    for line in open(faidxFilename):
        length, offset, lineWidth, blen = map(int, line.split()[-4:])
        newlineWidth = blen - lineWidth                                # 2 for DOS, 1 for UNIX
        header_    = fastaView[offsetEnd:offset]
        assert (header_[0] == ">" and header_[-1] == "\n")
        header     = header_[1:-newlineWidth]
        id, comment = splitFastaHeader(header)
        q, r = divmod(length, lineWidth)
        numNewlines = q + (r > 0)
        offsetEnd = offset + length + numNewlines*newlineWidth
        record = FaiRecord(id, comment, header, length, offset, lineWidth, blen)
        tbl.append(record)
    return tbl

def fileOffset(faiRecord, pos):
    """
    Find the in-file position (in bytes) corresponding to the position
    in the named contig, using the FASTA index.
    """
    q, r = divmod(pos, faiRecord.lineWidth)
    offset = faiRecord.offset + q*faiRecord.stride + r
    return offset

class MmappedFastaSequence(Sequence):
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
        snip = self.view[startOffset:endOffset].translate(None, "\r\n")
        return snip

    def __len__(self):
        return self.faiRecord.length

    def __eq__(self, other):
        return (isinstance(other, MmappedFastaSequence) and
                self[:] == other[:])

    def __str__(self):
        return str(self[:])


class IndexedFastaRecord(object):

    COLUMNS   = 60

    def __init__(self, view, faiRecord):
        self.view = view
        self.faiRecord = faiRecord

    @property
    def name(self):
        return self.header

    @property
    def header(self):
        return self.faiRecord.header

    @property
    def id(self):
        return self.faiRecord.id

    @property
    def comment(self):
        return self.faiRecord.comment

    @property
    def sequence(self):
        return MmappedFastaSequence(self.view, self.faiRecord)

    @property
    @deprecated
    def length(self):
        return self.faiRecord.length

    def __len__(self):
        return self.faiRecord.length

    def __repr__(self):
        return "<IndexedFastaRecord: %s>" % self.header

    def __eq__(self, other):
        return (isinstance(other, IndexedFastaRecord) and
                self.header == other.header and
                self.sequence == other.sequence)

    def __str__(self):
        """
        Output a string representation of this FASTA record, observing
        standard conventions about sequence wrapping.
        """
        return (">%s\n" % self.header) + \
            wrap(self.sequence, self.COLUMNS)

class IndexedFastaReader(ReaderBase, Sequence):
    """
    Random-access FASTA file reader.

    Requires that the lines of the FASTA file be fixed-length and that
    there is a FASTA index file (generated by `samtools faidx`) with
    name `fastaFilename.fai` in the same directory.

    .. doctest::

        >>> from pbcore.io import FastaTable
        >>> from pbcore import data
        >>> filename = data.getFasta()
        >>> t = IndexedFastaReader(filename)
        >>> print t[:4] # doctest: +NORMALIZE_WHITESPACE
        [<IndexedFastaRecord: ref000001|EGFR_Exon_2>,
         <IndexedFastaRecord: ref000002|EGFR_Exon_3>,
         <IndexedFastaRecord: ref000003|EGFR_Exon_4>,
         <IndexedFastaRecord: ref000004|EGFR_Exon_5>]
        >>> t.close()

    """
    def __init__(self, filename):
        self.filename = abspath(expanduser(filename))
        self.file = open(self.filename, "r")
        self.faiFilename = faiFilename(self.filename)
        if getsize(self.filename) > 0:
            self.view = mmap.mmap(self.file.fileno(), 0,
                                  prot=mmap.PROT_READ)
            self.fai = loadFastaIndex(self.faiFilename, self.view)
        else:
            self.view = None
            self.fai = []
        self.contigLookup = self._loadContigLookup()

    def _loadContigLookup(self):
        contigLookup = dict()
        for (pos, faiRecord) in enumerate(self.fai):
            contigLookup[pos]              = faiRecord
            contigLookup[faiRecord.id]     = faiRecord
            contigLookup[faiRecord.header] = faiRecord
        return contigLookup

    def __getitem__(self, key):
        if key < 0:
            key = len(self) + key

        if isinstance(key, slice):
            indices = xrange(*key.indices(len(self)))
            return [ IndexedFastaRecord(self.view, self.contigLookup[i])
                     for i in indices ]
        elif key in self.contigLookup:
            return IndexedFastaRecord(self.view, self.contigLookup[key])
        else:
            raise IndexError, "Contig not in FastaTable"

    def __iter__(self):
        return (self[i] for i in xrange(len(self)))

    def __len__(self):
        return len(self.fai)

# old name for IndexedFastaReader was FastaTable
FastaTable = IndexedFastaReader
