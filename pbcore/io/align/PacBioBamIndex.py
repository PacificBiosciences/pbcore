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

import h5py
import numpy as np
from os.path import abspath, expanduser
from functools import wraps
from collections import namedtuple

class PacBioBamIndex(object):
    """
    The PacBio BAM index is a companion file allowing modest
    *semantic* queries on PacBio BAM files without iterating over the
    entire file.  By convention, the PacBio BAM index has extension
    "bam.pbi".

    The bam.pbi index is an HDF5 file containing two data frames
    (groups containing arrays (frame columns) of common length):

      - A table with a row per BAM record, columns reflecting
        precomputed statistics per record

      - A table with a row per reference contig (tid) in the BAM,
        indicating the range of rows pertaining to the
    """
    def _loadColumns(self, f):
        g = f["PacBioBamIndex/Columns"]
        columnNamesAndColumns = sorted([ (k, v[:]) for (k, v) in g.iteritems() ])
        columnNames, columns = zip(*columnNamesAndColumns)
        return np.rec.fromarrays(columns, names=columnNames)

    def _loadVersion(self, f):
        return f["PacBioBamIndex"].attrs["Version"]

    def _loadOffsets(self, f):
        pass

    def __init__(self, pbiFilename):
        pbiFilename = abspath(expanduser(pbiFilename))
        with h5py.File(pbiFilename, "r") as f:
            try:
                self._version = self._loadVersion(f)
                self._columns = self._loadColumns(f)
                self._offsets = self._loadOffsets(f)
            except Exception as e:
                raise IOError, "Malformed bam.pbi file: " + str(e)


    @property
    def version(self):
        return self._version

    @property
    def columnNames(self):
        return list(self._columns.dtype.names)

    def __getattr__(self, columnName):
        if columnName in self.columnNames:
            return self._columns[columnName]
        else:
            raise AttributeError, "pbi has no column named '%s'" % columnName

    def __getitem__(self, rowNumber):
        return self._columns[rowNumber]

    def __dir__(self):
        # Special magic for IPython tab completion
        return self.columnNames

    def __len__(self):
        return len(self._columns)

    def __iter__(self):
        for i in xrange(len(self)):
            yield self[i]

    def rangeQuery(self, winId, winStart, winEnd):
        #
        # A read overlaps the window if winId == tid and
        #
        #  (tStart < winEnd) && (tEnd > winStart)     (1)
        #
        # We are presently doing this naively right now, just
        # computing the predicate over all rows. If/when we determine
        # this is too slow, we can accelerate using the nBackread
        # approach we use int he cmph5, doing binary search to
        # identify a candidate range and then culling the range.
        #
        ix = np.flatnonzero((self.tId    == winId)  &
                            (self.tStart  < winEnd) &
                            (self.tEnd    > winStart))
        return ix
