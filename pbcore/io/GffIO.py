# Author: David Alexander

"""
I/O support for GFF3 files.

The specification for the GFF format is available at
    http://www.sequenceontology.org/gff3.shtml
"""

from __future__ import absolute_import, division, print_function

__all__ = [ "Gff3Record",
            "GffReader",
            "GffWriter" ]

from builtins import map, super
from .base import ReaderBase, WriterBase
from collections import OrderedDict, defaultdict, namedtuple
from copy import copy as shallow_copy
from future.utils import iteritems
from functools import total_ordering
import logging
import tempfile
import os.path


@total_ordering
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
            attributes = list(map(tupleFromGffAttribute, columns[-1].split(";")))
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
             for (k, v) in iteritems(self.attributes)))
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

    def __eq__(self, other):
        return ((self.seqid, self.start) == (other.seqid, other.start))

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.seqid, self.start) < (other.seqid, other.start))


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
        super().__init__(f)
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
        super().__init__(f)
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
            for h in f.headers:
                gff_out.writeHeader(h)
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


GffHead = namedtuple("GffHead", ("file_name", "record", "headers"))

def merge_gffs_sorted(gff_files, output_file_name):
    """
    Utility function to combine a set of N (>= 2) GFF files, with records
    ordered by genomic location.  This assumes that each input file is already
    sorted, and forms a contiguous set of records.
    """
    # collect the very first record of each GFF and use that to sort the files
    first_records = []
    empty_files = []
    for file_name in gff_files:
        with GffReader(file_name) as f:
            for rec in f:
                first_records.append(GffHead(file_name, rec, f.headers))
                break
            else:
                empty_files.append(file_name)
    first_records.sort(key=lambda rec: rec.record)
    gff_files = [f.file_name for f in first_records]
    gff_files.extend(empty_files)
    headers, header_keys = _merge_gff_headers(gff_files)
    nrec = 0
    with GffWriter(output_file_name) as out:
        for key in header_keys:
            for value in headers[key]:
                out.writeHeader("##%s %s" % (key, value))
        for file_name in gff_files:
            logging.info("Merging {f}".format(f=file_name))
            with GffReader(file_name) as gff:
                for rec in gff:
                    out.writeRecord(rec)
                    nrec += 1
    return nrec
