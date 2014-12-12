#################################################################################
# Copyright (c) 2011-2014, Pacific Biosciences of California, Inc.
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
from os.path import abspath, expanduser, exists

from .PacBioBamIndex import PacBioBamIndex
from .BamAlignment import *
from ._BamSupport import *
from ._AlignmentMixin import AlignmentReaderMixin

class _BamReaderBase(AlignmentReaderMixin):
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
            triple = ds["BINDINGKIT"], ds["SEQUENCINGKIT"], ds["SOFTWAREVERSION"]
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
        # TODO: guarantee that these fields are nonoptional in our bams --- check with Marcus
        # TODO: are we interesting in the PP info?
        self._programTable = np.rec.fromrecords(
            [ (pg["ID"], pg.get("VN", None), pg.get("CL", None))
              for pg in self.peer.header["PG"] ],
            dtype=[("ID"     ,     "O"),
                   ("Version",     "O"),
                   ("CommandLine", "O")])

    def _loadReferenceFasta(self, referenceFastaFname):
        ft = FastaTable(referenceFastaFname)
        # Verify that this FASTA is in agreement with the BAM's
        # reference table---BAM should be a subset.
        fastaIdsAndLens = set((c.id, c.length) for c in ft)
        bamIdsAndLens   = set((c.Name, c.Length) for c in self.referenceInfoTable)
        if not bamIdsAndLens.issubset(fastaIdsAndLens):
            raise ReferenceMismatch, "FASTA file must contain superset of reference contigs in BAM"
        self.referenceFasta = ft

    def __init__(self, fname, referenceFastaFname=None):
        self.filename = fname = abspath(expanduser(fname))
        self.peer = Samfile(fname, "rb")
        # Check for sortedness, index.
        # There doesn't seem to be a "public" way to do this right
        # now, but that's fine because we're going to have to rewrite
        # it all anyway once the pysam rewrite lands.
        if not self.peer._hasIndex:
            raise ValueError, "Specified bam file lacks a bam index---required for this API"

        self._loadReferenceInfo()
        self._loadReadGroupInfo()
        self._loadProgramInfo()

        self.referenceFasta = None
        if referenceFastaFname is not None:
            self._loadReferenceFasta(referenceFastaFname)

    @property
    def isIndexLoaded(self):
        return self.index is not None

    @property
    def isReferenceLoaded(self):
        return self.referenceFasta is not None

    @property
    def alignmentIndex(self):
        raise UnavailableFeature("BAM has no alignment index")

    #TODO: change concept to readGroupTable in cmp.h5
    @property
    def movieInfoTable(self):
        raise Unimplemented()

    # TODO: change to read group accessor, this is semantically wrong now
    def movieInfo(self, movieId):
        raise Unimplemented()

    @property
    def movieNames(self):
        return set([mi.MovieName for mi in self.readGroupTable])

    @property
    def readGroupTable(self):
        return self._readGroupTable

    def readGroup(self, readGroupId):
        return self._readGroupDict[readGroupId]

    @property
    def sequencingChemistry(self):
        """
        List of the sequencing chemistries by movie.  Order is
        unspecified.
        """
        return list(self.readGroupTable.SequencingChemistry)

    #TODO: elide "Info" innames?
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

    #TODO: Marcus needs to put something in the spec for this
    @property
    def version(self):
        raise Unimplemented()

    #TODO: Marcus needs to put something in the spec for this
    def versionAtLeast(self, minimalVersion):
        raise Unimplemented()

    def softwareVersion(self, programName):
        raise Unimplemented()

    @property
    def isSorted(self):
        return True

    @property
    def isBarcoded(self):
        raise Unimplemented()

    @property
    def isEmpty(self):
        return (len(self) == 0)

    # TODO: make this private in cmp.h5 reader
    def alignmentGroup(self, alnGroupId):
        raise UnavailableFeature("BAM has no HDF5 groups")

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


    def __len__(self):
        return self.peer.mapped

    def close(self):
        if hasattr(self, "file") and self.file is not None:
            self.file.close()
            self.file = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


class BamReader(_BamReaderBase):
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
        raise UnavailableFeature("Use PacBioBamReader to get row-number based slicing.")



class IndexedBamReader(_BamReaderBase):
    """
    A `IndexedBamReader` is a BAM reader class that uses the bam.pbi
    (PacBio BAM index) format to enable random access by "row number"
    and to provide access to precomputed semantic information about
    the BAM records
    """
    def __init__(self, fname, referenceFastaFname=None):
        super(IndexedBamReader, self).__init__(fname, referenceFastaFname)
        self.pbi = None
        pbiFname = self.filename + ".pbi"
        if exists(pbiFname):
            self.pbi = PacBioBamIndex(pbiFname)
        else:
            raise ValueError, "IndexedBamReader requires bam.pbi index file"
        assert len(self.pbi) == self.peer.mapped, "Corrupt or mismatched pbi index file"

    def atRowNumber(self, rn):
        offset = self.pbi.virtualFileOffset[rn]
        self.peer.seek(offset)
        return BamAlignment(self, next(self.peer), rn)

    def readsInRange(self, winId, winStart, winEnd, justIndices=False):
        ix = self.pbi.rangeQuery(winId, winStart, winEnd)
        if justIndices:
            return ix
        else:
            return self[ix]

    def readsByName(self, query):
        """
        Identifies reads by name query.  The name query is interpreted as follows:

         - "movieName/holeNumber[/[*]]"      => gets all records from a chosen movie, ZMW
         - "movieName/holeNumber/rStart_rEnd => gets all records *overlapping* read range query in movie, ZMW
         - "movieName/holeNumber/ccs"        => gets CCS records from chose movie, ZMW (zero or one)

        Records are returned in a list in ascending order of rStart
        """
        def rgIDs(movieName):
            return self.readGroupTable.ID[self.readGroupTable.MovieName == movieName]

        def rangeOverlap(w1, w2):
            s1, e1 = w1
            s2, e2 = w2
            return (e1 > s2) and (e2 > s1)

        def rQueryMatch(readName, rQuery):
            if rQuery == "*" or rQuery == "":
                return True
            elif rQuery == "ccs":
                return readName.endswith("ccs")
            elif readName.endswith("ccs"):
                return False
            else:
                q = map(int, rQuery.split("_"))
                r = map(int, readName.split("/")[-1].split("_"))
                return rangeOverlap(q, r)

        fields = query.split("/")
        movieName = fields[0]
        holeNumber = int(fields[1])
        if len(fields) > 2: rQuery = fields[2]
        else:               rQuery = "*"

        rgs = rgIDs(movieName)
        rns = np.flatnonzero(np.in1d(self.ReadGroupID, rgs) &
                             (self.HoleNumber == holeNumber))
        alns = [ a for a in self[rns]
                 if rQueryMatch(a.readName, rQuery) ]
        return sorted(alns, key=lambda a: a.readStart)


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
