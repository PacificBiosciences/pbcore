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
I/O support for GFF3 files.

The specification for the GFF format is available at
    http://www.sequenceontology.org/gff3.shtml
"""

__all__ = [ "Gff3Record",
            "GffReader",
            "GffWriter" ]

from .base import ReaderBase, WriterBase
from collections import OrderedDict, defaultdict
from copy import copy as shallow_copy
import tempfile
import os.path


class Gff3Record(object):
    """
    Class for GFF record, providing uniform access to standard
    GFF fields and attributes.

    .. doctest::

        >>> from pbcore.io import Gff3Record
        >>> record = Gff3Record("chr1", 10, 11, "insertion",
        ...                     attributes=[("foo", "1"), ("bar", "2")])
        >>> record.start
        10
        >>> record.foo
        '1'
        >>> record.baz = 3
        >>> del record.baz

    Attribute access using record.fieldName notation raises ``ValueError``
    if an attribute named fieldName doesn't exist.  Use::

        >>> record.get(fieldName)

    to fetch a field or attribute with None default or::

        >>> record.get(fieldName, defaultValue)

    to fetch the field or attribute with a custom default.
    """
    _GFF_COLUMNS = [ "seqid", "source", "type",
                     "start", "end", "score",
                     "strand", "phase", "attributes" ]

    def __init__(self, seqid, start, end, type,
                 score=".", strand=".", phase=".",
                 source=".", attributes=()):
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
        columns = s.rstrip().rstrip(";").split("\t")
        try:
            assert len(columns) == len(cls._GFF_COLUMNS)
            attributes = map(tupleFromGffAttribute, columns[-1].split(";"))
            (_seqid, _source, _type, _start,
             _end, _score, _strand, _phase)  = columns[:-1]
            return Gff3Record(_seqid, int(_start), int(_end), _type,
                              _score, _strand, _phase, _source, attributes)
        except (AssertionError, ValueError):
            raise ValueError("Could not interpret string as a Gff3Record: %s" % s)


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
    # interface.  Exception if attribute
    # not found.
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

    #
    # Access without exceptions.
    #
    def get(self, name, default=None):
        return getattr(self, name, default)

    def put(self, name, value):
        setattr(self, name, value)

    def __cmp__(self, other):
        return cmp((self.seqid, self.start), (other.seqid, other.start))

class GffReader(ReaderBase):
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
        super(GffReader, self).__init__(f)
        self.headers, self.firstLine = self._readHeaders()

    def __iter__(self):
        if self.firstLine:
            yield Gff3Record.fromString(self.firstLine)
            self.firstLine = None
        for line in self.file:
            yield Gff3Record.fromString(line)


class GffWriter(WriterBase):
    """
    A GFF file writer class
    """
    def __init__(self, f):
        super(GffWriter, self).__init__(f)
        self.writeHeader("##gff-version 3")

    def writeHeader(self, headerLine):
        if not headerLine.startswith("##"):
            raise ValueError("GFF headers must start with ##")
        self.file.write("{0}\n".format(headerLine.rstrip()))

    def writeRecord(self, record):
        assert isinstance(record, Gff3Record)
        self.file.write("{0}\n".format(str(record)))

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
    iv = integerValue(s)
    if iv is not None: return iv
    fv = floatValue(s)
    if fv is not None: return fv
    return s

def tupleFromGffAttribute(s):
    k, v = s.split("=")
    return k, grok(v)


def sort_gff(file_name, output_file_name=None):
    """
    Sort a single GFF file by genomic location (seqid, start).
    """
    if output_file_name is None:
        output_file_name = os.path.splitext(file_name)[0] + "_sorted.gff"
    with GffReader(file_name) as f:
        records = [ rec for rec in f ]
        records.sort()
        with open(output_file_name, "w") as out:
            gff_out = GffWriter(out)
            map(gff_out.writeHeader, f.headers)
            for rec in records:
                gff_out.writeRecord(rec)
    return output_file_name


def merge_gffs (gff_files, output_file):
    """
    Merge a sequence of GFF files, preserving unique headers (except for the
    source commandline, which will usually vary).
    """
    headers, header_keys = _merge_gff_headers(gff_files)
    n_rec = 0
    with GffWriter(output_file) as writer:
        for key in header_keys:
            for value in headers[key]:
                writer.writeHeader("##%s %s" % (key, value))
        for gff_file in gff_files:
            with GffReader(gff_file) as reader:
                for rec in reader:
                    writer.writeRecord(rec)
                    n_rec += 1
    return n_rec


def _merge_gff_headers(gff_files):
    ignore_fields = set(["source-commandline", "gff-version", "date"])
    def _get_headers(f):
        with GffReader(f) as reader:
            for h in reader.headers:
                fields = h[2:].strip().split(" ")
                if not fields[0] in ignore_fields:
                    yield fields[0], " ".join(fields[1:])
    header_keys = []
    for k, v in _get_headers(gff_files[0]):
        if not k in header_keys:
            header_keys.append(k)
    headers = defaultdict(list)
    for gff_file in gff_files:
        for key, value in _get_headers(gff_file):
            if not value in headers[key]:
                headers[key].append(value)
    return headers, header_keys


def _merge_gffs_sorted(gff1, gff2, out_file):
    import logging
    logging.warn("Merging %s and %s" % (gff1, gff2))
    with GffWriter(out_file) as out:
        n_rec = 0
        headers, header_keys = _merge_gff_headers([gff1, gff2])
        with GffReader(gff1) as f1:
            for key in header_keys:
                for value in headers[key]:
                    out.writeHeader("##%s %s" % (key, value))
            with GffReader(gff2) as f2:
                rec1 = [ rec for rec in f1 ]
                rec2 = [ rec for rec in f2 ]
                i = j = 0
                while i < len(rec1) and j < len(rec2):
                    if (rec1[i] > rec2[j]):
                        out.writeRecord(rec2[j])
                        j += 1
                    else:
                        out.writeRecord(rec1[i])
                        i += 1
                for rec in rec1[i:]:
                    out.writeRecord(rec)
                    i += 1
                for rec in rec2[j:]:
                    out.writeRecord(rec)
                    j += 2
        return i + j


def merge_gffs_sorted(gff_files, output_file_name):
    """
    Utility function to combine a set of N (>= 2) GFF files, with records
    ordered by genomic location.  (Assuming each input file is already sorted.)
    """
    if len(gff_files) == 1: return gff_files[0]
    while len(gff_files) > 2:
        tmpout = tempfile.NamedTemporaryFile(suffix=".gff").name
        _merge_gffs_sorted(gff_files[0], gff_files[1], tmpout)
        gff_files = [tmpout] + gff_files[2:]
    with open(output_file_name, "w") as f:
        _merge_gffs_sorted(gff_files[0], gff_files[1], f)
    return output_file_name
