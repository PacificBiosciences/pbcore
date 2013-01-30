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
I/O support for GFF3 files.

The specification for the GFF format is available at
    http://www.sequenceontology.org/gff3.shtml
"""

__all__ = [ "Gff3Record",
            "GffReader",
            "GffWriter" ]

from pbcore.io._utils import getFileHandle
from collections import OrderedDict
from copy import copy as shallow_copy

class Gff3Record(object):
    """
    Class for GFF record, providing uniform access to standard
    GFF fields and attributes.

      >> record = Gff3Record("chr1", 10, 11, "insertion",
                            attributes=[("cat", "1"), ("dog", "2")])
      >> record.start
      10
      >> record.dog
      2
      >> record.mouse = 3
      >> del record.mouse

    Attribute access using record.fieldName notation raises ValueError
    if an attribute named fieldName doesn't exist.  Use

      >> record.attributes.get(fieldName, defaultValue)

    to search for attribute with a default.

    """
    _GFF_COLUMNS = [ "seqid", "source", "type",
                     "start", "end", "score",
                     "strand", "phase", "attributes" ]

    def __init__(self, seqid, start, end, type,
                 score=".", strand=".", phase=".",
                 source=".", attributes=[]):
        self.seqid  = seqid
        self.source = source
        self.type   = type
        self.start  = start
        self.end    = end
        self.score  = score
        self.strand = strand
        self.phase  = phase
        self.attributes = OrderedDict(attributes)

    def copy(self):
        """
        Return a shallow copy
        """
        return shallow_copy(self)

    @classmethod
    def fromString(cls, s):
        """
        Parse a string as a GFF record.
        Trailing whitespace is ignored.
        """
        columns = s.rstrip().split("\t")
        try:
            assert len(columns) == len(cls._GFF_COLUMNS)
            attributes = map(tupleFromGffAttribute, columns[-1].split(";"))
            (_seqid, _source, _type, _start,
             _end, _score, _strand, _phase)  = columns[:-1]
            return Gff3Record(_seqid, int(_start), int(_end), _type,
                              _score, _strand, _phase, _source, attributes)
        except (AssertionError, ValueError):
            raise ValueError("Could not interpret string as a Gff3Record")

    @staticmethod
    def _formatField(field):
        if type(field) == float:
            return "%.2f" % field
        else:
            return "%s" % field

    def __str__(self):
        formattedAttributes = ";".join(
            ("%s=%s" % (k, self._formatField(v))
             for (k, v) in self.attributes.iteritems()))
        formattedFixedColumns = "\t".join(
            self._formatField(getattr(self, k))
            for k in self._GFF_COLUMNS[:-1])
        return "%s\t%s" % (formattedFixedColumns,
                           formattedAttributes)

    #
    # Access to the attributes list using
    # dot notation, providing a uniform
    # interface.
    #
    def __getattr__(self, name):
        if name in self.attributes:
            return self.attributes[name]
        else:
            raise AttributeError

    def __setattr__(self, name, value):
        if name in self._GFF_COLUMNS:
            object.__setattr__(self, name, value)
        else:
            self.attributes[name] = value

    def __delattr__(self, name):
        del self.attributes[name]


class GffReader(object):
    """
    A GFF file reader class
    """
    def _readHeaders(self):
        headers = []
        firstLine = None
        for line in self.file:
            if line.startswith("##"):
                headers.append(line.rstrip())
            else:
                firstLine = line
                break
        return headers, firstLine

    def __init__(self, f):
        self.file = getFileHandle(f, "r")
        self.headers, self.firstLine = self._readHeaders()

    def __iter__(self):
        if self.firstLine:
            yield Gff3Record.fromString(self.firstLine)
            self.firstLine = None
        for line in self.file:
            yield Gff3Record.fromString(line)

    def close(self):
        self.file.close()


class GffWriter(object):
    """
    A GFF file writer class
    """
    def __init__(self, f):
        self.file = getFileHandle(f, "w")
        self.writeHeader("##gff-version 3")

    def writeHeader(self, headerLine):
        if not headerLine.startswith("##"):
            raise ValueError("GFF headers must start with ##")
        self.file.write("{0}\n".format(headerLine.rstrip()))

    def writeRecord(self, record):
        assert isinstance(record, Gff3Record)
        self.file.write("{0}\n".format(str(record)))

    def close(self):
        self.file.close()

#
# Utility functions
#

def floatValue(s):
    try:
        return float(s)
    except:
        return None

def integerValue(s):
    try:
        return int(s)
    except:
        return None

def grok(s):
    return integerValue(s) or floatValue(s) or s

def tupleFromGffAttribute(s):
    k, v = s.split("=")
    return k, grok(v)
