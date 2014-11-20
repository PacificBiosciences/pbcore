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

# Author: David Alexander

"""
Streaming I/O support for FASTA files.
"""

__all__ = [ "FastaRecord",
            "FastaReader",
            "FastaWriter",
            "FastaTable",
            "splitFastaHeader"]

from .base import ReaderBase, WriterBase
from ._utils import splitFileContents
from pbcore.util import sequences

import md5, mmap, numpy as np, re
from collections import namedtuple, OrderedDict, Sequence
from os.path import abspath, expanduser, isfile


def splitFastaHeader( name ):
    """
    Split a FASTA/FASTQ header into its id and metadata components
    """
    nameParts = re.split('\s', name, maxsplit=1)
    id_ = nameParts[0]
    if len(nameParts) > 1:
        metadata = nameParts[1].strip()
    else:
        metadata = None
    return (id_, metadata)

class FastaRecord(object):
    """
    A FastaRecord object models a named sequence in a FASTA file.
    """
    DELIMITER = ">"
    COLUMNS   = 60

    def __init__(self, name, sequence):
        try:
            assert "\n" not in name
            assert "\n" not in sequence
            assert self.DELIMITER not in sequence
            self._name = name
            self._sequence = sequence
            self._md5 = md5.md5(self.sequence).hexdigest()
            self._id, self._metadata = splitFastaHeader(name)
        except AssertionError:
            raise ValueError("Invalid FASTA record data")

    @property
    def name(self):
        """
        The name of the sequence in the FASTA file, equal to the entire
        FASTA header following the '>' character
        """
        return self._name

    @property
    def id(self):
        """
        The id of the sequence in the FASTA file, equal to the FASTA header
        up to the first whitespace.
        """
        return self._id

    @property
    def metadata(self):
        """
        The metadata associated with the sequence in the FASTA file, equal to
        the contents of the FASTA header following the first whitespace
        """
        return self._metadata

    @property
    def sequence(self):
        """
        The sequence for the record as present in the FASTA file.
        (Newlines are removed but otherwise no sequence normalization
        is performed).
        """
        return self._sequence

    @property
    def length(self):
        """
        Get the length of the FASTA sequence
        """
        return len(self._sequence)

    @property
    def md5(self):
        """
        The MD5 checksum (hex digest) of `sequence`
        """
        return self._md5

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
            name = lines[0][1:]
            sequence = "".join(lines[1:])
            return FastaRecord(name, sequence)
        except AssertionError:
            raise ValueError("String not recognized as a valid FASTA record")

    def reverseComplement(self, preserveHeader=False):
        """
        Return a new FastaRecord with the reverse-complemented DNA sequence.
        Optionally, supply a name
        """
        rcSequence = sequences.reverseComplement(self.sequence)
        if preserveHeader:
            return FastaRecord(self.name, rcSequence)
        else:
            rcName = '{0} [revcomp]'.format(self.name.strip())
            return FastaRecord(rcName, rcSequence)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.name     == other.name and
                    self.sequence == other.sequence)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        """
        Output a string representation of this FASTA record, observing
        standard conventions about sequence wrapping.
        """
        return (">%s\n" % self.name) + \
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
        ...     print record.name, len(record.sequence), record.md5
        ref000001|EGFR_Exon_2 183 e3912e9ceacd6538ede8c1b2adda7423
        ref000002|EGFR_Exon_3 203 4bf218da37175a91869033024ac8f9e9
        ref000003|EGFR_Exon_4 215 245bc7a046aad0788c22b071ed210f4d
        ref000004|EGFR_Exon_5 157 c368b8191164a9d6ab76fd328e2803ca
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
            raise ValueError("Invalid FASTA file")


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
            assert isinstance(record, FastaRecord)
        else:
            name, sequence = args
            record = FastaRecord(name, sequence)
        self.file.write(str(record))
        self.file.write("\n")


##
## Utility functions for FastaReader
##
def wrap(s, columns):
    return "\n".join(s[start:start+columns]
                     for start in xrange(0, len(s), columns))



# ------------------------------------------------------------------------------
# FastaTable: random access Fasta class
#

FaiRecord = namedtuple("FaiRecord", ("name", "length", "offset", "lineWidth", "stride"))

def faiFilename(fastaFilename):
    return fastaFilename + ".fai"

def loadFastaIndex(faidxFilename, fastaView):

    if not isfile(faidxFilename): # os.path.isfile
        raise IOError("Companion FASTA index (.fai) file not found or "
                      "malformatted! Use 'samtools faidx' to generate FASTA "
                      "index.")

    tbl = OrderedDict()
    #
    # `samtools faidx` mangles FASTA contig names containing a
    # space, for example, so we have to look up the true name in
    # the FASTA file itself, ignoring the name in the fai.
    #
    offsetEnd = 0
    for line in open(faidxFilename):
        length, offset, lineWidth, blen = map(int, line.split()[-4:])
        newlineWidth = blen - lineWidth                                # 2 for DOS, 1 for UNIX
        header    = fastaView[offsetEnd:offset]
        assert (header[0] == ">" and header[-1] == "\n")
        name      = header[1:-newlineWidth]
        q, r = divmod(length, lineWidth)
        numNewlines = q + (r > 0)
        offsetEnd = offset + length + numNewlines*newlineWidth
        record = FaiRecord(name, length, offset, lineWidth, blen)
        tbl[name] = record
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

class FastaTableRecord(object):
    def __init__(self, view, faiRecord):
        self.view = view
        self.faiRecord = faiRecord

    @property
    def name(self):
        return self.faiRecord.name

    @property
    def id(self):
        return splitFastaHeader(self.name)[0]

    @property
    def metadata(self):
        return splitFastaHeader(self.name)[1]

    @property
    def sequence(self):
        return MmappedFastaSequence(self.view, self.faiRecord)

    @property
    def length(self):
        return self.faiRecord.length

    def __repr__(self):
        return "<FastaTableRecord: %s>" % self.name

    def __eq__(self, other):
        return (isinstance(other, FastaTableRecord) and
                self.name == other.name and
                self.sequence == other.sequence)

class FastaTable(ReaderBase, Sequence):
    """
    Random-access FASTA file reader.

    Requires that the lines of the FASTA file be fixed-length and that
    there is a FASTA index file (generated by `samtools faidx`) with
    name `fastaFilename.fai` in the same directory.

    .. doctest::

        >>> from pbcore.io import FastaTable
        >>> from pbcore import data
        >>> filename = data.getFasta()
        >>> t = FastaTable(filename)
        >>> print t[:4]
        [<FastaTableRecord: ref000001|EGFR_Exon_2>,
        <FastaTableRecord: ref000002|EGFR_Exon_3>,
        <FastaTableRecord: ref000003|EGFR_Exon_4>,
        <FastaTableRecord: ref000004|EGFR_Exon_5>]
        >>> t.close()

    """
    def __init__(self, filename):
        self.filename = abspath(expanduser(filename))
        self.file = open(self.filename, "r")
        self.view = mmap.mmap(self.file.fileno(), 0,
                              prot=mmap.PROT_READ)
        self.faiFilename = faiFilename(self.filename)
        self.fai = loadFastaIndex(self.faiFilename, self.view)
        self.contigById = self._loadContigById()

    def _loadContigById(self):
        # Initialize the dictionary with the full sequence name
        contigById = dict(self.fai)
        # Add the same records back under just the Id as well
        for name in contigById.keys():
            id_ = splitFastaHeader(name)[0]
            if id_ not in contigById:
                contigById[id_] = contigById[name]
        # Finally add their index number
        contigById.update(zip(xrange(len(self.fai)),
                              self.fai.itervalues()))
        return contigById

    def __getitem__(self, key):
        if key < 0:
            key = len(self) + key

        if isinstance(key, slice):
            indices = xrange(*key.indices(len(self.fai)))
            return [ FastaTableRecord(self.view, self.contigById[i])
                     for i in indices ]
        elif key in self.contigById:
            return FastaTableRecord(self.view, self.contigById[key])
        else:
            raise IndexError, "Contig not in FastaTable"

    def __iter__(self):
        return (self[key] for key in self.fai)

    def __len__(self):
        return len(self.fai)
