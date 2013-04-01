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
            "FastaWriter" ]

from .base import ReaderBase, WriterBase
from ._utils import splitFileContents
import md5

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
    def sequence(self):
        """
        The sequence for the record as present in the FASTA file.
        (Newlines are removed but otherwise no sequence normalization
        is performed).
        """
        return self._sequence

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
            lines = s.split("\n")
            assert len(lines) > 1
            assert lines[0][0] == cls.DELIMITER
            name = lines[0][1:]
            sequence = "".join(lines[1:])
            return FastaRecord(name, sequence)
        except AssertionError:
            raise ValueError("String not recognized as a valid FASTA record")

    def __eq__(self, other):
        return (self.name     == other.name and
                self.sequence == other.sequence)

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

        >>> fr = FastaReader("input.fasta.gz")
        >>> for record in fr:
        ...     print record.name, len(record.sequence), record.md5
        >>> fr.close()

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
## Utility functions
##
def wrap(s, columns):
    return "\n".join(s[start:start+columns]
                     for start in xrange(0, len(s), columns))
