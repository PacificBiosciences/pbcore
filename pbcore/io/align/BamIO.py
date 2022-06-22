# Author: David Alexander

__all__ = ["BamReader", "IndexedBamReader"]

from collections import defaultdict
from functools import wraps
import warnings
from os.path import abspath, expanduser, exists

import numpy as np
import pysam
from pysam.libcalignmentfile import AlignmentFile  # pylint: disable=no-name-in-module, import-error, fixme, line-too-long


from pbcore.io import FastaTable
from pbcore.chemistry import decodeTriple
from ..base import ReaderBase
from .PacBioBamIndex import PacBioBamIndex
from .BamAlignment import BamAlignment
from ._BamSupport import (BASE_FEATURE_TAGS,
                          PULSE_FEATURE_TAGS,
                          rgAsInt,
                          UnavailableFeature,
                          Unimplemented,
                          IncompatibleFile,
                          ReferenceMismatch,
                          MultipleReadGroups)
from ._AlignmentMixin import AlignmentReaderMixin, IndexedAlignmentReaderMixin


def requiresBai(method):
    @wraps(method)
    def f(bamReader, *args, **kwargs):
        if not bamReader.peer.has_index():
            raise UnavailableFeature(
                "this feature requires an standard BAM index file (bam.bai)")
        else:
            return method(bamReader, *args, **kwargs)
    return f


class _BamReaderBase(ReaderBase):
    """
    The BamReader class provides a high-level interface to PacBio BAM
    files.  If a PacBio BAM index (bam.pbi file) is present and the
    user instantiates the BamReader using the reference FASTA as the
    second argument, the BamReader will provide an interface
    compatible with the now removed CmpH5Reader.
    """

    def _loadReferenceInfo(self):
        refRecords = self.peer.header["SQ"]
        refNames = [r["SN"] for r in refRecords]
        refLengths = [r["LN"] for r in refRecords]
        refIds = list(map(self.peer.get_tid, refNames))
        nRefs = len(refRecords)

        if nRefs > 0:
            self._referenceInfoTable = np.rec.fromrecords(list(zip(
                refIds,
                refIds,
                refNames,
                refNames,
                refLengths,
                np.zeros(nRefs, dtype=np.uint32),
                np.zeros(nRefs, dtype=np.uint32))),
                dtype=[('ID', '<i8'), ('RefInfoID', '<i8'),
                       ('Name', 'O'), ('FullName', 'O'),
                       ('Length', '<i8'),
                       ('StartRow', '<u4'), ('EndRow', '<u4')])
            self._referenceDict = {}
            self._referenceDict.update(
                list(zip(refIds, self._referenceInfoTable)))
            self._referenceDict.update(
                list(zip(refNames, self._referenceInfoTable)))
        else:
            self._referenceInfoTable = None
            self._referenceDict = None

    def _loadReadGroupInfo(self):
        rgs = self.peer.header["RG"]
        readGroupTable_ = []

        # RGID -> ("abstract feature name" -> actual feature name)
        self._baseFeatureNameMappings = {}
        self._pulseFeatureNameMappings = {}

        for rg in rgs:
            rgID = rgAsInt(rg["ID"])
            rgName = rg["PU"]
            ds = dict([pair.split("=")
                       for pair in rg["DS"].split(";") if pair != ""])
            # spec: we only consider first two components of basecaller version
            # in "chem" lookup
            rgReadType = ds["READTYPE"]
            rgChem = "unknown"
            rgFrameRate = 0.0
            rgSample = rg.get("SM", "UnnamedSample")
            rgLibrary = rg.get("LB", "UnnamedLibrary")
            if rgReadType != "TRANSCRIPT":
                if set(("BASECALLERVERSION", "SEQUENCINGKIT", "BINDINGKIT")) <= set(ds):
                    pass
                else:
                    raise IOError(
                        "This does not appear to be a valid PacBio BAM file. Only datasets from RS II and Sequel instruments are supported by this program.")
                rgFrameRate = ds["FRAMERATEHZ"]
                basecallerVersion = ".".join(
                    ds["BASECALLERVERSION"].split(".")[0:2])
                triple = ds["BINDINGKIT"], ds["SEQUENCINGKIT"], basecallerVersion
                rgChem = decodeTriple(*triple)

            # Look for the features manifest entries within the DS tag,
            # and build an "indirection layer", i.e. to get from
            # "Ipd"  to "Ipd:Frames"
            # (This is a bit messy.  Can we separate the manifest from
            # the rest of the DS content?)
            baseFeatureNameMapping = {key.split(":")[0]: key
                                      for key in ds
                                      if key in BASE_FEATURE_TAGS}
            pulseFeatureNameMapping = {key.split(":")[0]: key
                                       for key in ds
                                       if key in PULSE_FEATURE_TAGS}
            self._baseFeatureNameMappings[rgID] = baseFeatureNameMapping
            self._pulseFeatureNameMappings[rgID] = pulseFeatureNameMapping

            readGroupTable_.append(
                (rgID, rgName, rgReadType, rgChem, rgFrameRate, rgSample,
                 rgLibrary, frozenset(baseFeatureNameMapping), rg["ID"]))

        self._readGroupTable = np.rec.fromrecords(
            readGroupTable_,
            dtype=[("ID", np.int32),
                   ("MovieName", "O"),
                   ("ReadType", "O"),
                   ("SequencingChemistry", "O"),
                   ("FrameRate",           float),
                   ("SampleName",          "O"),
                   ("LibraryName",         "O"),
                   ("BaseFeatures",        "O"),
                   ("StringID", "O")])
        if len(set(self._readGroupTable.ID)) != len(self._readGroupTable):
            warnings.warn("Non-unique read group integer IDs found - some features may be restricted", RuntimeWarning)

        # In our modern barcoded BAM files the read groups take the form
        # '0123456/0--0', '0123456/1--1', etc., but the barcode pairs are not
        # included in the conversion to integer ID.  this means we need to
        # track the full ID string separately
        self._readGroupUniqueDict = {rg.StringID:rg for rg in self._readGroupTable}
        self._readGroupDict = defaultdict(list)
        for rg in self._readGroupTable:
            self._readGroupDict[rg.ID].append(rg)

        # The base/pulse features "available" to clients of this file are the intersection
        # of features available from each read group.
        self._baseFeaturesAvailable = set.intersection(
            *[set(mapping) for mapping in self._baseFeatureNameMappings.values()])
        self._pulseFeaturesAvailable = set.intersection(
            *[set(mapping) for mapping in self._pulseFeatureNameMappings.values()])

    def _loadProgramInfo(self):
        pgRecords = [(pg["ID"], pg.get("VN", None), pg.get("CL", None))
                     for pg in self.peer.header.get("PG", [])]

        if len(pgRecords) > 0:
            self._programTable = np.rec.fromrecords(
                pgRecords,
                dtype=[("ID",     "O"),
                       ("Version",     "O"),
                       ("CommandLine", "O")])
        else:
            self._programTable = None

    def _loadReferenceFasta(self, referenceFastaFname):
        ft = FastaTable(referenceFastaFname)
        # Verify that this FASTA is in agreement with the BAM's
        # reference table---BAM should be a subset.
        fastaIdsAndLens = set((c.id, len(c)) for c in ft)
        bamIdsAndLens = set((c.Name, c.Length)
                            for c in self.referenceInfoTable)
        if not bamIdsAndLens.issubset(fastaIdsAndLens):
            raise ReferenceMismatch(
                "FASTA file must contain superset of reference contigs in BAM")
        self.referenceFasta = ft

    def _checkFileCompatibility(self):
        # Verify that this is a "pacbio" BAM file of version at least
        # 3.0.1
        badVersionException = IncompatibleFile(
            "This BAM file is incompatible with this API " +
            "(only PacBio BAM files version >= 3.0.1 are supported)")
        checkedVersion = self.version
        if "b" in checkedVersion:
            raise badVersionException
        else:
            major, minor, patch = checkedVersion.split('.')
            if not (int(major), int(minor), int(patch)) >= (3, 0, 1):
                raise badVersionException

    def __init__(self, fname, referenceFastaFname=None):
        self.filename = fname = abspath(expanduser(fname))
        # XXX https://github.com/pysam-developers/pysam/issues/939
        pysam.set_verbosity(0)  # pylint: disable=no-member
        self.peer = AlignmentFile(fname, "rb", check_sq=False)
        self._checkFileCompatibility()

        self._loadReferenceInfo()
        self._loadReadGroupInfo()
        self._loadProgramInfo()

        self.referenceFasta = None
        if referenceFastaFname is not None:
            if self.isUnmapped:
                raise ValueError(
                    "Unmapped BAM file--reference FASTA should not be given as argument to BamReader")
            self._loadReferenceFasta(referenceFastaFname)

    @property
    def isIndexLoaded(self):
        return self.index is not None  # pylint: disable=no-member

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
    def index(self):
        raise UnavailableFeature("BAM has no index")

    @property
    def identity(self):
        raise UnavailableFeature("Identity calculation requires index")

    @property
    def movieNames(self):
        return set([mi.MovieName for mi in self.readGroupTable])

    @property
    def readGroupTable(self):
        return self._readGroupTable

    def readGroupInfo(self, readGroupId):
        if isinstance(readGroupId, str):
            return self._readGroupUniqueDict[readGroupId]
        else:
            rgs = self._readGroupDict[readGroupId]
            if len(rgs) == 1:
                return rgs[0]
            elif len(rgs) > 1:
                raise MultipleReadGroups("There are multiple read groups with ID {}: {}".format(readGroupId, ", ".join([rg.StringID for rg in rgs])))
            else:
                return KeyError("No read group with ID {}".format(readGroupId))

    def readGroupInfos(self, readGroupId):
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

    # TODO: standard?  how about subread instead?  why capitalize ccs?
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
        elif all(readTypes == "TRANSCRIPT"):
            return "TRANSCRIPT"
        elif all((readTypes == "CCS") | (readTypes == "SUBREAD")):
            return "mixed"
        else:
            return "unknown"

    @property
    def version(self):
        try:
            return self.peer.header["HD"]["pb"]
        except KeyError:
            raise IOError(
                "This does not appear to be a valid PacBio BAM file. Only datasets from RS II and Sequel instruments are supported by this program.")

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

    def hasBaseFeature(self, featureName):
        return featureName in self._baseFeaturesAvailable

    def baseFeaturesAvailable(self):
        return self._baseFeaturesAvailable

    def hasPulseFeature(self, featureName):
        return featureName in self._pulseFeaturesAvailable

    def pulseFeaturesAvailable(self):
        return self._pulseFeaturesAvailable

    def hasPulseFeatures(self):
        """
        Is this BAM file a product of running analysis with the
        PacBio-internal analysis mode enabled?
        """
        return self.hasPulseFeature("PulseCall")

    @property
    def barcode(self):
        raise Unimplemented()

    @property
    def barcodeName(self):
        raise Unimplemented()

    @property
    def barcodes(self):
        raise Unimplemented()

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
        super().__init__(fname, referenceFastaFname)

    @property
    def index(self):
        return None

    def __iter__(self):
        self.peer.reset()
        for a in self.peer:
            yield BamAlignment(self, a)

    def readsInRange(self, winId, winStart, winEnd, justIndices=False):
        # PYSAM BUG: fetch doesn't work if arg 1 is tid and not rname
        if not isinstance(winId, str):
            winId = self.peer.get_reference_name(winId)
        if justIndices == True:
            raise UnavailableFeature("BAM is not random-access")
        else:
            return (BamAlignment(self, it)
                    for it in self.peer.fetch(winId, winStart, winEnd, multiple_iterators=False))

    def __getitem__(self, rowNumbers):
        raise UnavailableFeature(
            "Use IndexedBamReader to get row-number based slicing.")


class IndexedBamReader(_BamReaderBase, IndexedAlignmentReaderMixin):
    """
    A `IndexedBamReader` is a BAM reader class that uses the
    ``bam.pbi`` (PacBio BAM index) file to enable random access by
    "row number" and to provide access to precomputed semantic
    information about the BAM records
    """

    def __init__(self, fname, referenceFastaFname=None, sharedIndex=None):
        super().__init__(fname, referenceFastaFname)
        if sharedIndex is None:
            self.pbi = None
            pbiFname = self.filename + ".pbi"
            if exists(pbiFname):
                self.pbi = PacBioBamIndex(pbiFname)
            else:
                raise IOError("IndexedBamReader requires bam.pbi index file " +
                              "to read {f}".format(f=fname))
        else:
            self.pbi = sharedIndex

    @property
    def index(self):
        return self.pbi

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
        self.peer.reset()
        for (rowNumber, peerRecord) in enumerate(self.peer):
            yield BamAlignment(self, peerRecord, rowNumber)

    def __len__(self):
        return len(self.pbi)

    def __getitem__(self, rowNumbers):
        if (isinstance(rowNumbers, int) or
                issubclass(type(rowNumbers), np.integer)):
            return self.atRowNumber(rowNumbers)
        elif isinstance(rowNumbers, slice):
            return (self.atRowNumber(r)
                    for r in range(*rowNumbers.indices(len(self))))
        elif isinstance(rowNumbers, list) or isinstance(rowNumbers, np.ndarray):
            if len(rowNumbers) == 0:
                return []
            else:
                entryType = type(rowNumbers[0])
                if entryType == int or issubclass(entryType, np.integer):
                    return (self.atRowNumber(r) for r in rowNumbers)
                elif entryType == bool or issubclass(entryType, np.bool_):
                    return (self.atRowNumber(r) for r in np.flatnonzero(rowNumbers))
        raise TypeError("Invalid type for IndexedBamReader slicing")

    def __getattr__(self, key):
        if key in self.pbi.columnNames:
            return getattr(self.pbi, key)
        else:
            raise AttributeError("no such column in pbi index")

    def __dir__(self):
        basicDir = dir(self.__class__)
        return basicDir + self.pbi.columnNames

    @property
    def identity(self):
        """
        Fractional alignment sequence identities as numpy array.
        """
        if len(self.pbi) == 0:
            return np.array([])
        if not "nMM" in self.pbi.columnNames:
            raise AttributeError("Identities require mapped BAM.")
        return self.pbi.identity
