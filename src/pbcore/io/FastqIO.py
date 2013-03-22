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
I/O support for FASTQ files (Sanger style).

We support FASTQ files in the four-line convention (unwrapped).
Wrapped FASTQ files are generally considered a bad idea as the @, +
delimiters can also appear in the quality string.

See:
  http://en.wikipedia.org/wiki/FASTQ_format
"""


__all__ = [ "FastqRecord",
            "FastqReader",
            "FastqWriter",
            "qvsFromAscii",
            "asciiFromQvs" ]

from pbcore.io._utils import getFileHandle, splitFileContents
from cStringIO import StringIO
import numpy as np, re


class FastqRecord(object):
    """
    A FastqRecord object models a named sequence and its quality
    values in a FASTQ file.  We adopt the Sanger conventions, that
    """
    DELIMITER1 = "@"
    DELIMITER2 = "+"

    def __init__(self, name, sequence, quality=None, qualityString=None):
        try:
            assert "\n" not in name
            assert "\n" not in sequence
            self.name = name
            self.sequence = sequence

            # Only one of quality, qualityString should be provided
            assert (quality == None) != (qualityString == None)
            if quality != None:
                self.quality = quality
            else:
                self.quality = qvsFromAscii(qualityString)
            assert len(self.sequence) == len(self.quality)
        except AssertionError:
            raise ValueError("Invalid FASTQ record data")

    @property
    def qualityString(self):
        return asciiFromQvs(self.quality)

    @classmethod
    def fromString(cls, s):
        """
        Interprets a string as a FASTQ record. Only supports four-line
        format, as wrapped FASTQs can't easily be safely parsed.
        """
        try:
            lines = s.rstrip().split("\n")
            assert len(lines) == 4
            assert lines[0][0] == cls.DELIMITER1
            assert lines[2][0] == cls.DELIMITER2
            assert len(lines[1]) == len(lines[3])
            name = lines[0][1:]
            sequence = lines[1]
            quality = qvsFromAscii(lines[3])
            return FastqRecord(name, sequence, quality)
        except AssertionError:
            raise ValueError("String not recognized as a valid FASTQ record")

    def __eq__(self, other):
        return (self.name     == other.name and
                self.sequence == other.sequence and
                np.array_equiv(self.quality, other.quality))

    def __str__(self):
        """
        Output a string representation of this FASTQ record, in
        standard four-line format.
        """
        return "\n".join([self.DELIMITER1 + self.name,
                          self.sequence,
                          self.DELIMITER2,
                          self.qualityString])

class FastqReader(object):
    """
    Reader for FASTQ files, useable as a one-shot iterator over
    FastqRecord objects.  FASTQ files must follow the four-line
    convention.
    """
    def __init__(self, f):
        self.file = getFileHandle(f, "r")

    def __iter__(self):
        while True:
            lines = [next(self.file) for i in xrange(4)]
            yield FastqRecord(lines[0][1:-1],
                              lines[1][:-1],
                              qualityString=lines[3][:-1])

    def close(self):
        self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


class FastqWriter(object):
    """
    A FASTQ file writer class
    """
    def __init__(self, f):
        self.file = getFileHandle(f, "w")

    def writeRecord(self, *args):
        """
        Write a FASTQ record to the file.
        If given one argument, it is interpreted as a FastaRecord.
        Given two arguments, they are interpreted as the name, sequence, and quality.
        """
        if len(args) not in (1, 3):
            raise ValueError
        if len(args) == 1:
            record = args[0]
            assert isinstance(record, FastqRecord)
        else:
            name, sequence, quality = args
            record = FastqRecord(name, sequence, quality)
        self.file.write(str(record))
        self.file.write("\n")

    def close(self):
        self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


##
## Utility
##
def qvsFromAscii(s):
    return (np.fromstring(s, dtype=np.uint8) - 33)

def asciiFromQvs(a):
    return (np.clip(a, 0, 93).astype(np.uint8) + 33).tostring()
