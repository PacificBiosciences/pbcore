#################################################################################
# Copyright (c) 2017, Pacific Biosciences of California, Inc.
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

# Author: Lance Hepler

from __future__ import print_function

"""
I/O support for VCF4 files.

The specification for the VCF4 format is available at:
    https://samtools.github.io/hts-specs
"""

from collections import OrderedDict
from functools import total_ordering

__all__ = ["Vcf4Record"]


def _int_float_or_string(s):
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    return str(s)


def _fmt(x):
    if isinstance(x, float):
        return "{0:.3g}".format(x)
    return x


def _empty_then(xs):
    if not xs:
        return
    yield ""
    for x in xs:
        yield x


@total_ordering
class Vcf4Record(object):
    """
    Class for VCF record, providing uniform access to standard
    VCF fields and attributes.

    .. doctest::

        >>> from pbcore.io import Vcf4Record
        >>> rec1 = Vcf4Record("ecoliK12_pbi_March2013", \
                              84, ".", "TG", "T", 48, "PASS", [("DP", 53)])
        >>> str(rec1)
        'ecoliK12_pbi_March2013\\t84\\t.\\tTG\\tT\\t48\\tPASS\\tDP=53'
        >>> rec2 = Vcf4Record.fromString(str(rec1))
        >>> rec1 == rec2
        True
        >>> rec1.pos
        84
        >>> rec1.filter
        'PASS'

    """

    __slots__ = ("chrom", "pos", "id", "ref", "alt", "qual", "filter", "info", "fields")

    def __init__(self, chrom, pos, id, ref, alt, qual, filt, info, *fields):
        self.chrom = chrom
        self.pos = pos
        self.id = id
        self.ref = ref
        self.alt = alt
        self.qual = qual
        self.filter = filt
        self.info = OrderedDict(info)
        self.fields = fields

    @staticmethod
    def fromString(s):
        try:
            fields = s.strip().split('\t')
            fields[1] = int(fields[1])
            fields[5] = _int_float_or_string(fields[5])
            fields[7] = OrderedDict((k.strip(), _int_float_or_string(v.strip()))
                                    for k, v in (x.strip().split('=')
                                                for x in fields[7].split(';')))
            return Vcf4Record(*fields)
        except TypeError:
            raise ValueError("Could not interpret string as a Vcf4Record: '{0}'".format(s))

    def __lt__(self, other):
        return (self.chrom, self.pos) < (other.chrom, other.pos)

    def __eq__(self, other):
        return (self.chrom == other.chrom and self.pos == other.pos and self.id == other.id and \
                self.ref == other.ref and self.alt == other.alt and self.qual == other.qual and \
                self.filter == other.filter and self.info == other.info and \
                self.fields == other.fields)

    def __str__(self):
        return "{chrom}\t{pos}\t{id}\t{ref}\t{alt}\t{qual}\t{filter}\t{info}{fields}".format(
                chrom=self.chrom, pos=self.pos, id=self.id,
                ref=self.ref, alt=self.alt, qual=_fmt(self.qual),
                filter=self.filter,
                info=";".join("{0}={1}".format(k, _fmt(v)) for k, v in self.info.iteritems()),
                fields="\t".join(_empty_then(self.fields)))


def merge_vcfs_sorted(vcf_files, output_file_name):
    """
    Utility function to combine N (>=1) VCF files, with records
    sorted by contig then contig position. This assumes each file is already
    sorted, and forms a contiguous set of records.
    """
    # get the headers and the first record of each file, so we can compare
    meta = OrderedDict([])
    hdr = OrderedDict([])
    fst_recs = []
    for f in vcf_files:
        with open(f) as h:
            for line in h:
                line = line.strip()
                if not line:
                    continue
                elif line[:2] == "##":
                    meta[line] = ()
                elif line[:6] == "#CHROM":
                    hdr.update((h, ()) for h in line.lstrip("#").split("\t"))
                else:
                    fst_recs.append((Vcf4Record.fromString(line), f))
                    break
    sorted_files = sorted(fst_recs, key=lambda x: x[0])
    nrec = 0
    with open(output_file_name, "w") as oh:
        for m, _ in meta.iteritems():
            print(m, file=oh)
        print("#{0}".format("\t".join(h for h, _ in hdr.iteritems())), file=oh)
        for _, f in sorted_files:
            with open(f) as h:
                for line in h:
                    line = line.strip()
                    if not line or line[0] == "#":
                        continue
                    else:
                        print(line, file=oh)
                        nrec += 1
    return nrec
