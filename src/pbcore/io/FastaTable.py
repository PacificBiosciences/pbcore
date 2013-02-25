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

# Random-access container for FASTA contigs (as FastaRecords)

from pbcore.io import FastaReader, FastaRecord

__all__ = [ "FastaTable",
            "ReferenceTable" ]

class FastaTable(object):
    """
    A random access API for accessing FastaRecords by
      - MD5;
      - order loaded from file
    """
    def __init__(self, fastaFile):
        self._records = list(FastaReader(fastaFile))
        self._recordsByMD5 = { r.md5 : r for r in self._records }

    def __getitem__(self, pos):
        """
        FastaRecord, by order loaded from the file.  Not advised for
        use in production code.
        """
        return self._records[pos]

    def __len__(self):
        return len(self._records)

    def __iter__(self):
        return iter(self._records)

    def byMD5(self, md5):
        """
        FastaRecord, by sequence MD5.  Exception if not found.
        """
        return self._recordsByMD5[md5]


class ReferenceContigRecord(FastaRecord):
    """
    An extension of FastaRecord that has the notion of a local
    identifier.
    """
    def __init__(self, fastaRecord, localId):
        self._name     = fastaRecord.name
        self._sequence = fastaRecord.sequence
        self._md5      = fastaRecord.md5
        self._localId  = localId

    @property
    def localId(self):
        return self._localId

class ReferenceTable(FastaTable):
    """
    An extension of FastaTable that also has a notion of local
    identifier mappings.  For instance, the local identifier could be
    the RefId within a cmp.h5.  The only requirement is that the local
    identifiers define a one-to-one (but not necessarily onto!)
    mapping to the reference contigs.  The view of the FASTA file is
    restricted to those contigs which have a local identifier.
    """
    def __init__(self, fastaFile, localIdMappingProvider):
        """
        Instantiate a ReferenceTable.

        localIdMappingProvider is an object with a method
        `localReferenceIdMapping` returning a dict of MD5 -> localId
        """
        mapping = localIdMappingProvider.localReferenceIdMapping()
        self._records = []
        for fastaRecord in FastaReader(fastaFile):
            localId = mapping.get(fastaRecord.md5)
            if localId:
                self._records.append(ReferenceContigRecord(fastaRecord, localId))
        self._recordsByMD5 = { r.md5 : r for r in self._records }
        self._recordsByLocalId = { r.localId : r for r in self._records }

    def byLocalId(self, localId):
        """
        Lookup reference contig---returns ReferenceContigRecord
        object.  Exception if not found.
        """
        return self._recordsByLocalId[localId]

    def localIdToName(self, localId):
        """
        Convenience name lookup routine.  Exception if not found
        """
        return self.byLocalId(localId).name
