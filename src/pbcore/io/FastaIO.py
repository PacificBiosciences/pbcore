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
I/O support for FASTA files.
"""

__all__ = [ "FastaRecord",
            "FastaReader",
            "FastaWriter" ]

from pbcore.io._utils import getFileHandle, splitFileContents

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
            self.name = name
            self.sequence = sequence
        except AssertionError:
            raise ValueError("Invalid FASTA record data")

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


class FastaReader(object):
    """
    Reader for FASTA files, usable as a one-shot iterator over
    FastaRecord objects.  Agnostic about line wrapping.
    """
    DELIMITER = ">"

    def __init__(self, f):
        self.file = getFileHandle(f, "r")

    def __iter__(self):
        try:
            parts = splitFileContents(self.file, ">")
            assert "" == next(parts)
            for part in parts:
                yield FastaRecord.fromString(">" + part)
        except AssertionError:
            raise ValueError("Invalid FASTA file")


class FastaWriter(object):
    """
    A FASTA file writer class
    """
    def __init__(self, f):
        self.file = getFileHandle(f, "w")

    def writeRecord(self, record):
        assert isinstance(record, FastaRecord)
        self.file.write(str(record))
        self.file.write("\n")

    def close(self):
        self.file.close()


##
## Utility functions
##
def wrap(s, columns):
    return "\n".join(s[start:start+columns]
                     for start in xrange(0, len(s), columns))
