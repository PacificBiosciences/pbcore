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

__all__ = [ "BamReader", "IndexedBamReader" ]

from pysam import Samfile
from pbcore.io import FastaTable
from pbcore.chemistry import decodeTriple, ChemistryLookupError

import numpy as np
from itertools import groupby
from functools import wraps
from os.path import abspath, expanduser, exists

from .PacBioBamIndex import PacBioBamIndex
from .BamAlignment import *
from ._BamSupport import *
from ._AlignmentMixin import AlignmentReaderMixin, IndexedAlignmentReaderMixin


def requiresBai(method):
    @wraps(method)
    def f(bamReader, *args, **kwargs):
        if not bamReader.peer._hasIndex():
            raise UnavailableFeature, "this feature requires an standard BAM index file (bam.bai)"
        else:
            return method(bamAln, *args, **kwargs)
    return f


class _BamReaderBase(object):
    """
    The BamReader class provides a high-level interface to PacBio BAM
    files.  If a PacBio BAM index (bam.pbi file) is present and the
    user instantiates the BamReader using the reference FASTA as the
    second argument, the BamReader will provide an interface
    compatible with CmpH5Reader.
    """
    def _loadReferenceInfo(self):
        refRecords = self.peer.header["SQ"]
        refNames   = [r["SN"] for r in refRecords]
        refLengths = [r["LN"] for r in refRecords]
        refMD5s    = [r["M5"] for r in refRecords]
        refIds = map(self.peer.gettid, refNames)
        nRefs = len(refRecords)

        if nRefs > 0:
            self._referenceInfoTable = np.rec.fromrecords(zip(
                refIds,
                refIds,
                refNames,
                refNames,
                refLengths,
                refMD5s,
                np.zeros(nRefs, dtype=np.uint32),
                np.zeros(nRefs, dtype=np.uint32)),
                dtype=[('ID', '<i8'), ('RefInfoID', '<i8'),
                       ('Name', 'O'), ('FullName', 'O'),
                       ('Length', '<i8'), ('MD5', 'O'),
                       ('StartRow', '<u4'), ('EndRow', '<u4')])
            self._referenceDict = {}
            self._referenceDict.update(zip(refIds, self._referenceInfoTable))
            self._referenceDict.update(zip(refNames, self._referenceInfoTable))
        else:
            self._referenceInfoTable = None
            self._referenceDict = None

    def _loadReadGroupInfo(self):
        rgs = self.peer.header["RG"]
        readGroupTable_ = []
        pulseFeaturesInAll_ = frozenset(PULSE_FEATURE_TAGS.keys())
        for rg in rgs:
            # Regarding RG ID: BLASR currently outputs a hex digest of
            # 10 nibbles, instead of the 8 which would fit into a
            # 32-bit word.  So we truncate here for the purposes of
            # cross-referencing within this API and the PacBioBamIndex
            # API.  We do check for a collision below.
            rgID = int(rg["ID"][:8], 16)
            rgName = rg["PU"]
            ds = dict([pair.split("=") for pair in rg["DS"].split(";") if pair != ""])
            triple = ds["BINDINGKIT"], ds["SEQUENCINGKIT"], ds["BASECALLERVERSION"]
            rgChem = decodeTriple(*triple)
            rgReadType = ds["READTYPE"]
            readGroupTable_.append((rgID, rgName, rgReadType, rgChem))
            pulseFeaturesInAll_ = pulseFeaturesInAll_.intersection(ds.keys())

        self._readGroupTable = np.rec.fromrecords(
            readGroupTable_,
            dtype=[("ID"                 , np.uint32),
                   ("MovieName"          , "O"),
                   ("ReadType"           , "O"),
                   ("SequencingChemistry", "O")])
        assert len(set(self._readGroupTable.ID)) == len(self._readGroupTable), \
            "First 8 chars of read group IDs must be unique!"

        self._readGroupDict = { rg.ID : rg
                                for rg in self._readGroupTable }

        self._pulseFeaturesAvailable = pulseFeaturesInAll_


    def _loadProgramInfo(self):
        pgRecords = [ (pg["ID"], pg.get("VN", None), pg.get("CL", None))
                      for pg in self.peer.header.get("PG", []) ]

        if len(pgRecords) > 0:
            self._programTable = np.rec.fromrecords(
                pgRecords,
                dtype=[("ID"     ,     "O"),
                       ("Version",     "O"),
                       ("CommandLine", "O")])
        else:
            self._programTable = None

    def _loadReferenceFasta(self, referenceFastaFname):
        ft = FastaTable(referenceFastaFname)
        # Verify that this FASTA is in agreement with the BAM's
        # reference table---BAM should be a subset.
        fastaIdsAndLens = set((c.id, c.length) for c in ft)
        bamIdsAndLens   = set((c.Name, c.Length) for c in self.referenceInfoTable)
        if not bamIdsAndLens.issubset(fastaIdsAndLens):
            raise ReferenceMismatch, "FASTA file must contain superset of reference contigs in BAM"
        self.referenceFasta = ft

    def _checkFileCompatibility(self):
        # Verify that this is a "pacbio" BAM file of version at least
        # 3.0b3
        try:
            checkedVersion = self.version
        except:
            raise IncompatibleFile(
                "This BAM file is incompatible with this API " +
                "(only PacBio BAM files version >= 3.0b3 are supported)")

    def __init__(self, fname, referenceFastaFname=None):
        self.filename = fname = abspath(expanduser(fname))
        self.peer = Samfile(fname, "rb", check_sq=False)
        self._checkFileCompatibility()
        # Check for sortedness, index.
        # There doesn't seem to be a "public" way to do this right
        # now, but that's fine because we're going to have to rewrite
        # it all anyway once the pysam rewrite lands.
        if not self.peer._hasIndex:
            raise IOError, "Specified bam file lacks a bam index---required for this API"

        self._loadReferenceInfo()
        self._loadReadGroupInfo()
        self._loadProgramInfo()

        self.referenceFasta = None
        if referenceFastaFname is not None:
            if self.isUnmapped:
                raise ValueError, "Unmapped BAM file--reference FASTA should not be given as argument to BamReader"
            self._loadReferenceFasta(referenceFastaFname)

    @property
    def isIndexLoaded(self):
        return self.index is not None

    @property
    def isReferenceLoaded(self):
        return self.referenceFasta is not None

    @property
    def isUnmapped(self):
        return not(self.isMapped)

    @property
    def isMapped(self):
        return len(self.peer.header["SQ"]) > 0

    @property
    def alignmentIndex(self):
        raise UnavailableFeature("BAM has no alignment index")

    @property
    def movieNames(self):
        return set([mi.MovieName for mi in self.readGroupTable])

    @property
    def readGroupTable(self):
        return self._readGroupTable

    def readGroupInfo(self, readGroupId):
        return self._readGroupDict[readGroupId]

    @property
    def sequencingChemistry(self):
        """
        List of the sequencing chemistries by movie.  Order is
        unspecified.
        """
        return list(self.readGroupTable.SequencingChemistry)

    @property
    def referenceInfoTable(self):
        return self._referenceInfoTable

    #TODO: standard?  how about subread instead?  why capitalize ccs?
    # can we standardize this?  is cDNA an additional possibility
    @property
    def readType(self):
        """
        Either "standard", "CCS", "mixed", or "unknown", to represent the
        type of PacBio reads aligned in this BAM file.
        """
        readTypes = self.readGroupTable.ReadType
        if all(readTypes == "SUBREAD"):
            return "standard"
        elif all(readTypes == "CCS"):
            return "CCS"
        elif all((readTypes == "CCS") | (readTypes == "SUBREAD")):
            return "mixed"
        else:
            return "unknown"

    @property
    def version(self):
        return self.peer.header["HD"]["pb"]

    #TODO: Marcus needs to put something in the spec for this
    def versionAtLeast(self, minimalVersion):
        raise Unimplemented()

    def softwareVersion(self, programName):
        raise Unimplemented()

    @property
    def isSorted(self):
        return self.peer.header["HD"]["SO"] == "coordinate"

    @property
    def isBarcoded(self):
        raise Unimplemented()

    @property
    def isEmpty(self):
        return (len(self) == 0)

    def referenceInfo(self, key):
        return self._referenceDict[key]

    def atOffset(self, offset):
        self.peer.seek(offset)
        return BamAlignment(self, next(self.peer))

    def hasPulseFeature(self, featureName):
        return featureName in self._pulseFeaturesAvailable

    def pulseFeaturesAvailable(self):
        return self._pulseFeaturesAvailable

    @property
    def barcode(self):
        raise Unimplemented()

    @property
    def barcodeName(self):
        raise Unimplemented()

    @property
    def barcodes(self):
        raise Unimplemented()

    def __repr__(self):
        return "<%s for %s>" % (type(self).__name__, self.filename)

    @requiresBai
    def __len__(self):
        return self.peer.mapped + self.peer.unmapped

    def close(self):
        if hasattr(self, "file") and self.file is not None:
            self.file.close()
            self.file = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


class BamReader(_BamReaderBase, AlignmentReaderMixin):
    """
    Reader for a BAM with a bam.bai (SAMtools) index, but not a
    bam.pbi (PacBio) index.  Supports basic BAM operations.
    """
    def __init__(self, fname, referenceFastaFname=None):
        super(BamReader, self).__init__(fname, referenceFastaFname)

    def __iter__(self):
        self.peer.reset()
        for a in self.peer:
            yield BamAlignment(self, a)

    # TODO: cmp.h5 readsInRange only accepts int key, not string.
    # that's just lame, fix it.
    def readsInRange(self, winId, winStart, winEnd, justIndices=False):
        # PYSAM BUG: fetch doesn't work if arg 1 is tid and not rname
        if not isinstance(winId, str):
            winId = self.peer.getrname(winId)
        if justIndices == True:
            raise UnavailableFeature("BAM is not random-access")
        else:
            return ( BamAlignment(self, it)
                     for it in self.peer.fetch(winId, winStart, winEnd, multiple_iterators=False) )

    def __getitem__(self, rowNumbers):
        raise UnavailableFeature("Use IndexedBamReader to get row-number based slicing.")



class IndexedBamReader(_BamReaderBase, IndexedAlignmentReaderMixin):
    """
    A `IndexedBamReader` is a BAM reader class that uses the
    ``bam.pbi`` (PacBio BAM index) file to enable random access by
    "row number" and to provide access to precomputed semantic
    information about the BAM records
    """
    def __init__(self, fname, referenceFastaFname=None):
        super(IndexedBamReader, self).__init__(fname, referenceFastaFname)
        self.pbi = None
        pbiFname = self.filename + ".pbi"
        if exists(pbiFname):
            self.pbi = PacBioBamIndex(pbiFname)
        else:
            raise IOError, "IndexedBamReader requires bam.pbi index file"
        assert len(self.pbi) == self.peer.mapped, "Corrupt or mismatched pbi index file"

    def atRowNumber(self, rn):
        offset = self.pbi.virtualFileOffset[rn]
        self.peer.seek(offset)
        return BamAlignment(self, next(self.peer), rn)

    def readsInRange(self, winId, winStart, winEnd, justIndices=False):
        if isinstance(winId, str):
            winId = self.referenceInfo(winId).ID
        ix = self.pbi.rangeQuery(winId, winStart, winEnd)
        if justIndices:
            return ix
        else:
            return self[ix]

    def __iter__(self):
        for rn in xrange(len(self.pbi)):
            yield self.atRowNumber(rn)

    def __len__(self):
        return len(self.pbi)

    def __getitem__(self, rowNumbers):
        if (isinstance(rowNumbers, int) or
            issubclass(type(rowNumbers), np.integer)):
            return self.atRowNumber(rowNumbers)
        elif isinstance(rowNumbers, slice):
            return [ self.atRowNumber(r)
                     for r in xrange(*rowNumbers.indices(len(self)))]
        elif isinstance(rowNumbers, list) or isinstance(rowNumbers, np.ndarray):
            if len(rowNumbers) == 0:
                return []
            else:
                entryType = type(rowNumbers[0])
                if entryType == int or issubclass(entryType, np.integer):
                    return [ self.atRowNumber(r) for r in rowNumbers ]
                elif entryType == bool or issubclass(entryType, np.bool_):
                    return [ self.atRowNumber(r) for r in np.flatnonzero(rowNumbers) ]
                    raise TypeError, "Invalid type for IndexedBamReader slicing"

    def __getattr__(self, key):
        if key in self.pbi.columnNames:
            return self.pbi[key]
        else:
            raise AttributeError, "no such column in pbi index"

    def __dir__(self):
        return self.pbi.columnNames
