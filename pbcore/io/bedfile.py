"""
Reader for BED files used to define genomic regions of interest
"""
from collections import namedtuple
import logging
import re

import numpy as np

from .base import getFileHandle


log = logging.getLogger(__name__)


class BedRecord(namedtuple("BedRecord", ["chrom", "chr_start", "chr_end", "name"])):

    @staticmethod
    def from_line(s):
        fields = s.split()
        chr_start = int(re.sub(",", "", fields[1]))
        chr_end = int(re.sub(",", "", fields[2]))
        name = None
        if len(fields) > 3:
            name = fields[3]
        if chr_end <= chr_start:
            raise ValueError("chr_end <= chr_start: {e} <= {s}".format(
                             e=chr_end, s=chr_start))
        return BedRecord(fields[0], chr_start, chr_end, name)

    def __len__(self):
        return self.chr_end - self.chr_start

    @property
    def coordinates(self):
        return "{}:{:,}-{:,}".format(*(self[0:3]))

    def __repr__(self):
        if self.name is None:
            return self.coordinates
        else:
            return "{}:{:,}-{:,} ({})".format(*self)

    def __str__(self):
        end = len(self)
        if self.name is None:
            end = end - 1
        return "\t".join([str(x) for x in self[0:end]])

    @property
    def pandas_record(self):
        return (np.str(self.chrom), np.int64(self.chr_start), np.int64(self.chr_end), np.str(self.name if self.name else ""))


def parse_bed(bed_file):
    records = []
    with getFileHandle(bed_file, mode="rt") as bed_in:
        for line in bed_in:
            try:
                rec = BedRecord.from_line(line.strip())
            except ValueError as e:
                log.warning(e)
                log.warning("Can't parse as BED record: %s", line)
            else:
                records.append(rec)
    return records
