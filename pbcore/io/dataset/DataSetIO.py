"""
Classes representing the elements of the DataSet type

These classes are often instantiated by the parser and passed to the DataSet,
where they are stored, manipulated, filtered, merged, etc.
"""

import hashlib
import copy
import os
import errno
import logging
import xml.dom.minidom
import tempfile
from functools import wraps
import numpy as np
from urlparse import urlparse
from pbcore.util.Process import backticks
from pbcore.io.opener import (openAlignmentFile, openIndexedAlignmentFile,
                              FastaReader, IndexedFastaReader, CmpH5Reader,
                              IndexedBamReader)
from pbcore.io.FastaIO import (splitFastaHeader, FastaWriter, FastaRecord,
                               IndexedFastaRecord)
from pbcore.io import PacBioBamIndex, BaxH5Reader
from pbcore.io.align._BamSupport import IncompatibleFile

from pbcore.io.dataset.DataSetReader import (parseStats, populateDataSet,
                                             resolveLocation, wrapNewResource,
                                             xmlRootType)
from pbcore.io.dataset.DataSetWriter import toXml
from pbcore.io.dataset.DataSetValidator import validateString
from pbcore.io.dataset.DataSetMembers import (DataSetMetadata,
                                              SubreadSetMetadata,
                                              ContigSetMetadata,
                                              BarcodeSetMetadata,
                                              ExternalResources, Filters)

log = logging.getLogger(__name__)

def filtered(generator):
    """Wrap a generator with postfiltering"""
    @wraps(generator)
    def wrapper(dset, *args, **kwargs):
        filter_tests = dset.processFilters()
        no_filter = dset.noFiltering
        if no_filter:
            for read in generator(dset, *args, **kwargs):
                yield read
        else:
            for read in generator(dset, *args, **kwargs):
                if any(filt(read) for filt in filter_tests):
                    yield read
    return wrapper


def _toDsId(x):
    return "PacBio.DataSet.{x}".format(x=x)

def _dsIdToName(x):
    if DataSetMetaTypes.isValid(x):
        return x.split('.')[-1]

def _dsIdToType(x):
    if DataSetMetaTypes.isValid(x):
        types = DataSet.castableTypes()
        return types[_dsIdToName(x)]

def _dsIdToSuffix(x):
    dsIds = DataSetMetaTypes.ALL
    suffixMap = {dsId: _dsIdToName(dsId) for dsId in dsIds}
    suffixMap[_toDsId("DataSet")] = 'DataSet'
    if DataSetMetaTypes.isValid(x):
        suffix = suffixMap[x]
        suffix = suffix.lower()
        suffix += '.xml'
        return suffix

def openDataSet(*files, **kwargs):
    # infer from the first:
    first = DataSet(files[0], **kwargs)
    dsId = first.objMetadata.get('MetaType')
    # hdfsubreadset metatypes are subreadset. Fix:
    if files[0].endswith('xml'):
        xml_rt = xmlRootType(files[0])
        if _dsIdToName(dsId) != xml_rt:
            log.warn("XML metatype does not match root tag")
            if xml_rt == 'HdfSubreadSet':
                dsId = _toDsId(xml_rt)
    tbrType = _dsIdToType(dsId)
    if tbrType:
        return tbrType(*files, **kwargs)
    else:
        return DataSet(*files, **kwargs)


class DataSetMetaTypes(object):
    """
    This mirrors the PacBioSecondaryDataModel.xsd definitions and be used
    to reference a specific dataset type.
    """
    SUBREAD = _toDsId("SubreadSet")
    HDF_SUBREAD = _toDsId("HdfSubreadSet")
    ALIGNMENT = _toDsId("AlignmentSet")
    BARCODE = _toDsId("BarcodeSet")
    CCS_ALIGNMENT = _toDsId("ConsensusAlignmentSet")
    CCS = _toDsId("ConsensusReadSet")
    REFERENCE = _toDsId("ReferenceSet")
    CONTIG = _toDsId("ContigSet")

    ALL = (SUBREAD, HDF_SUBREAD, ALIGNMENT,
           BARCODE, CCS, CCS_ALIGNMENT, REFERENCE, CONTIG)

    @classmethod
    def isValid(cls, dsId):
        return dsId in cls.ALL


def _fileType(fname):
    """Get the extension of fname (with h5 type)"""
    remainder, ftype = os.path.splitext(fname)
    if ftype == '.h5':
        _, prefix = os.path.splitext(remainder)
        ftype = prefix + ftype
    ftype = ftype.strip('.')
    return ftype

class DataSet(object):
    """The record containing the DataSet information, with possible type
    specific subclasses"""

    datasetType = DataSetMetaTypes.ALL

    def __init__(self, *files, **kwargs):
        """DataSet constructor

        Initialize representations of the ExternalResources, MetaData,
        Filters, and LabeledSubsets, parse inputs if possible

        Args:
            *files: one or more filenames or uris to read
            strict=False: strictly require all index files
            skipCounts=False: skip updating counts for faster opening

        Doctest:
            >>> import os, tempfile
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet, SubreadSet
            >>> # Prog like pbalign provides a .bam file:
            >>> # e.g. d = DataSet("aligned.bam")
            >>> # Something like the test files we have:
            >>> inBam = data.getBam()
            >>> inBam.endswith('.bam')
            True
            >>> d = DataSet(inBam)
            >>> # A UniqueId is generated, despite being a BAM input
            >>> bool(d.uuid)
            True
            >>> dOldUuid = d.uuid
            >>> # They can write this BAM to an XML:
            >>> # e.g. d.write("alignmentset.xml")
            >>> outdir = tempfile.mkdtemp(suffix="dataset-doctest")
            >>> outXml = os.path.join(outdir, 'tempfile.xml')
            >>> d.write(outXml)
            >>> # And then recover the same XML:
            >>> d = DataSet(outXml)
            >>> # The UniqueId will be the same
            >>> d.uuid == dOldUuid
            True
            >>> # Inputs can be many and varied
            >>> ds1 = DataSet(data.getXml(8), data.getBam(1))
            >>> ds1.numExternalResources
            2
            >>> ds1 = DataSet(data.getFofn())
            >>> ds1.numExternalResources
            2
            >>> # Constructors should be used directly
            >>> SubreadSet(data.getSubreadSet()) # doctest:+ELLIPSIS
            <SubreadSet...
            >>> # Even with untyped inputs
            >>> DataSet(data.getBam()) # doctest:+ELLIPSIS
            <DataSet...
            >>> SubreadSet(data.getBam()) # doctest:+ELLIPSIS
            <SubreadSet...
            >>> # You can also cast up and down, but casting between siblings
            >>> # is limited (abuse at your own risk)
            >>> DataSet(data.getBam()).copy(asType='SubreadSet')
            ... # doctest:+ELLIPSIS
            <SubreadSet...
            >>> SubreadSet(data.getBam()).copy(asType='DataSet')
            ... # doctest:+ELLIPSIS
            <DataSet...
            >>> # DataSets can also be manipulated after opening:
            >>> # Add external Resources:
            >>> ds = DataSet()
            >>> _ = ds.externalResources.addResources(["IdontExist.bam"])
            >>> ds.externalResources[-1].resourceId == "IdontExist.bam"
            True
            >>> # Add an index file
            >>> pbiName = "IdontExist.bam.pbi"
            >>> ds.externalResources[-1].addIndices([pbiName])
            >>> ds.externalResources[-1].indices[0].resourceId == pbiName
            True

        """
        self._strict = kwargs.get('strict', False)
        self._skipCounts = kwargs.get('skipCounts', False)

        # The metadata concerning the DataSet or subtype itself (e.g.
        # name, version, UniqueId)
        self.objMetadata = {}

        # The metadata contained in the DataSet or subtype (e.g.
        # NumRecords, BioSamples, Collections, etc.
        self._metadata = DataSetMetadata()

        self.externalResources = ExternalResources()
        self._filters = Filters()

        # list of DataSet objects representing subsets
        self.subdatasets = []

        # Why not keep this around... (filled by file reader)
        self.fileNames = files

        # parse files
        log.debug('Containers specified')
        populateDataSet(self, files)
        log.debug('Done populating')
        # update uuid
        if not self.uuid:
            self.newUuid()

        self.objMetadata.setdefault("Name", "")
        self.objMetadata.setdefault("Tags", "")
        dsType = self.objMetadata.setdefault(
            "MetaType", "PacBio.DataSet." + self.__class__.__name__)
        if self._strict:
            if dsType != _toDsId('DataSet'):
                if dsType not in self._castableDataSetTypes:
                    raise IOError(errno.EIO,
                                  "Cannot create {c} from {f}".format(
                                      c=self.datasetType, f=dsType),
                                  files[0])

        # State tracking:
        self._cachedFilters = []
        self.noFiltering = False
        self._openReaders = []

        # update counts
        if files:
            if not self.totalLength or not self.numRecords:
                self.updateCounts()
            elif self.totalLength <= 0 or self.numRecords <= 0:
                self.updateCounts()

    def __repr__(self):
        """Represent the dataset with an informative string:

        Returns:
            "<type uuid filenames>"
        """
        repr_d = dict(k=self.__class__.__name__, u=self.uuid, f=self.fileNames)
        return '<{k} uuid:{u} source files:{f}>'.format(**repr_d)

    def __add__(self, otherDataset):
        """Merge the representations of two DataSets without modifying
        the original datasets. (Fails if filters are incompatible).

        Args:
            otherDataset: a DataSet to merge with self

        Returns:
            A new DataSet with members containing the union of the input
            DataSets' members and subdatasets representing the input DataSets

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import AlignmentSet
            >>> from pbcore.io.dataset.DataSetWriter import toXml
            >>> # xmls with different resourceIds: success
            >>> ds1 = AlignmentSet(data.getXml(no=8))
            >>> ds2 = AlignmentSet(data.getXml(no=11))
            >>> ds3 = ds1 + ds2
            >>> expected = ds1.numExternalResources + ds2.numExternalResources
            >>> ds3.numExternalResources == expected
            True
            >>> # xmls with different resourceIds but conflicting filters:
            >>> # failure to merge
            >>> ds2.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
            >>> ds3 = ds1 + ds2
            >>> ds3
            >>> # xmls with same resourceIds: ignores new inputs
            >>> ds1 = AlignmentSet(data.getXml(no=8))
            >>> ds2 = AlignmentSet(data.getXml(no=8))
            >>> ds3 = ds1 + ds2
            >>> expected = ds1.numExternalResources
            >>> ds3.numExternalResources == expected
            True
        """
        return self.merge(otherDataset)

    def merge(self, other, copyOnMerge=True):
        if (other.__class__.__name__ == self.__class__.__name__ or
                other.__class__.__name__ == 'DataSet' or
                self.__class__.__name__ == 'DataSet'):
            firstIn = False
            if not self.toExternalFiles():
                firstIn = True
            if (not firstIn and
                    not self.filters.testCompatibility(other.filters)):
                log.warning("Filter incompatibility has blocked the addition "
                            "of two datasets")
                return None
            else:
                self.addFilters(other.filters)
            self._cachedFilters = []
            self._checkObjMetadata(other.objMetadata)
            # There is probably a cleaner way to do this:
            self.objMetadata.update(other.objMetadata)
            if copyOnMerge:
                result = self.copy()
            else:
                result = self
            result.addMetadata(other.metadata)
            # skip updating counts because other's metadata should be up to
            # date
            result.addExternalResources(other.externalResources,
                                        updateCount=False)
            # DataSets may only be merged if they have identical filters,
            # So there is nothing new to add.
            if other.subdatasets or not firstIn:
                if copyOnMerge:
                    result.addDatasets(other.copy())
                else:
                    result.addDatasets(other)
            # If this dataset has no subsets representing it, add self as a
            # subdataset to the result
            # TODO: this is a stopgap to prevent spurious subdatasets when
            # creating datasets from dataset xml files...
            if not self.subdatasets and not firstIn:
                result.addDatasets(self.copy())
            return result
        else:
            raise TypeError('DataSets can only be merged with records of the '
                            'same type or of type DataSet')


    def __deepcopy__(self, memo):
        """Deep copy this Dataset by recursively deep copying the members
        (objMetadata, DataSet metadata, externalResources, filters and
        subdatasets)
        """
        tbr = type(self)()
        memo[id(self)] = tbr
        tbr.objMetadata = copy.deepcopy(self.objMetadata, memo)
        tbr.metadata = copy.deepcopy(self._metadata, memo)
        tbr.externalResources = copy.deepcopy(self.externalResources, memo)
        tbr.filters = copy.deepcopy(self._filters, memo)
        tbr.subdatasets = copy.deepcopy(self.subdatasets, memo)
        tbr.fileNames = copy.deepcopy(self.fileNames, memo)
        return tbr

    def __eq__(self, other):
        """Test for DataSet equality. The method specified in the documentation
        calls for md5 hashing the "Core XML" elements and comparing. This is
        the same procedure for generating the Uuid, so the same method may be
        used. However, as simultaneously or regularly updating the Uuid is not
        specified, we opt to not set the newUuid when checking for equality.

        Args:
            other: The other DataSet to compare to this DataSet.

        Returns:
            T/F the Core XML elements of this and the other DataSet hash to the
            same value
        """
        sXml = self.newUuid(setter=False)
        oXml = other.newUuid(setter=False)
        return sXml == oXml

    def __enter__(self):
        return self

    def close(self):
        """Close all of the opened resource readers"""
        for reader in self._openReaders:
            try:
                reader.close()
            except AttributeError:
                if not self._strict:
                    log.info("Reader not opened properly, therefore not "
                             "closed properly.")
                else:
                    raise
        self._openReaders = []

    def __exit__(self, *exec_info):
        self.close()

    def __len__(self):
        count = 0
        if self._filters:
            log.warn("Base class DataSet length cannot be calculate when "
                     "filters present")
            return -1
        else:
            for reader in self.resourceReaders():
                count += len(reader)
        return count

    def newUuid(self, setter=True):
        """Generate and enforce the uniqueness of an ID for a new DataSet.
        While user setable fields are stripped out of the Core DataSet object
        used for comparison, the previous UniqueId is not. That means that
        copies will still be unique, despite having the same contents.

        Args:
            setter=True: Setting to False allows MD5 hashes to be generated
                         (e.g. for comparison with other objects) without
                         modifying the object's UniqueId
        Returns:
            The new Id, a properly formatted md5 hash of the Core DataSet

        Doctest:
            >>> from pbcore.io import AlignmentSet
            >>> ds = AlignmentSet()
            >>> old = ds.uuid
            >>> _ = ds.newUuid()
            >>> old != ds.uuid
            True
        """
        coreXML = toXml(self, core=True)
        newId = str(hashlib.md5(coreXML).hexdigest())

        # Group appropriately
        newId = '-'.join([newId[:8], newId[8:12], newId[12:16], newId[16:20],
                          newId[20:]])

        if setter:
            self.objMetadata['UniqueId'] = newId
        return newId

    def copy(self, asType=None):
        """Deep copy the representation of this DataSet

        Args:
            asType: The type of DataSet to return, e.g. 'AlignmentSet'

        Returns:
            A DataSet object that is identical but for UniqueId

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet, SubreadSet
            >>> ds1 = DataSet(data.getXml())
            >>> # Deep copying datasets is easy:
            >>> ds2 = ds1.copy()
            >>> # But the resulting uuid's should be different.
            >>> ds1 == ds2
            False
            >>> ds1.uuid == ds2.uuid
            False
            >>> ds1 is ds2
            False
            >>> # Most members are identical
            >>> ds1.name == ds2.name
            True
            >>> ds1.externalResources == ds2.externalResources
            True
            >>> ds1.filters == ds2.filters
            True
            >>> ds1.subdatasets == ds2.subdatasets
            True
            >>> len(ds1.subdatasets) == 2
            True
            >>> len(ds2.subdatasets) == 2
            True
            >>> # Except for the one that stores the uuid:
            >>> ds1.objMetadata == ds2.objMetadata
            False
            >>> # And of course identical != the same object:
            >>> assert not reduce(lambda x, y: x or y,
            ...                   [ds1d is ds2d for ds1d in
            ...                    ds1.subdatasets for ds2d in
            ...                    ds2.subdatasets])
            >>> # But types are maintained:
            >>> # TODO: turn strict back on once sim sets are indexable
            >>> ds1 = SubreadSet(data.getXml(no=10), strict=False)
            >>> ds1.metadata # doctest:+ELLIPSIS
            <SubreadSetMetadata...
            >>> ds2 = ds1.copy()
            >>> ds2.metadata # doctest:+ELLIPSIS
            <SubreadSetMetadata...
            >>> # Lets try casting
            >>> ds1 = DataSet(data.getBam())
            >>> ds1 # doctest:+ELLIPSIS
            <DataSet...
            >>> ds1 = ds1.copy(asType='SubreadSet')
            >>> ds1 # doctest:+ELLIPSIS
            <SubreadSet...
            >>> # Lets do some illicit casting
            >>> ds1 = ds1.copy(asType='ReferenceSet')
            Traceback (most recent call last):
            TypeError: Cannot cast from SubreadSet to ReferenceSet
            >>> # Lets try not having to cast
            >>> ds1 = SubreadSet(data.getBam())
            >>> ds1 # doctest:+ELLIPSIS
            <SubreadSet...
        """
        if asType:
            try:
                tbr = self.__class__.castableTypes()[asType]()
            except KeyError:
                raise TypeError("Cannot cast from {s} to "
                                "{t}".format(s=type(self).__name__,
                                             t=asType))
            tbr.merge(self)
            # update the metatypes: (TODO: abstract out 'iterate over all
            # resources and modify the element that contains them')
            tbr.makePathsAbsolute()
            return tbr
        result = copy.deepcopy(self)
        result.newUuid()
        return result

    def split(self, chunks=0, ignoreSubDatasets=False, contigs=False,
              maxChunks=0):
        """Deep copy the DataSet into a number of new DataSets containing
        roughly equal chunks of the ExternalResources or subdatasets.

        Args:
            chunks: the number of chunks to split the DataSet. When chunks=0,
                    create one DataSet per subdataset, or failing that
                    ExternalResource
            ignoreSubDatasets: F/T (False) do not split on datasets, only split
                               on ExternalResources
            contigs: (False) split on contigs instead of external resources or
                     subdatasets
        Returns:
            A list of new DataSet objects (all other information deep copied).

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import AlignmentSet
            >>> # splitting is pretty intuitive:
            >>> ds1 = AlignmentSet(data.getXml())
            >>> # but divides up extRes's, so have more than one:
            >>> ds1.numExternalResources > 1
            True
            >>> # the default is one AlignmentSet per ExtRes:
            >>> dss = ds1.split()
            >>> len(dss) == ds1.numExternalResources
            True
            >>> # but you can specify a number of AlignmentSets to produce:
            >>> dss = ds1.split(chunks=1)
            >>> len(dss) == 1
            True
            >>> dss = ds1.split(chunks=2, ignoreSubDatasets=True)
            >>> len(dss) == 2
            True
            >>> # The resulting objects are similar:
            >>> dss[0].uuid == dss[1].uuid
            False
            >>> dss[0].name == dss[1].name
            True
            >>> # Previously merged datasets are 'unmerged' upon split, unless
            >>> # otherwise specified.
            >>> # Lets try merging and splitting on subdatasets:
            >>> ds1 = AlignmentSet(data.getXml(8))
            >>> ds1.totalLength
            123588
            >>> ds1tl = ds1.totalLength
            >>> ds2 = AlignmentSet(data.getXml(11))
            >>> ds2.totalLength
            117086
            >>> ds2tl = ds2.totalLength
            >>> # merge:
            >>> dss = ds1 + ds2
            >>> dss.totalLength == (ds1tl + ds2tl)
            True
            >>> # unmerge:
            >>> ds1, ds2 = sorted(
            ... dss.split(2), key=lambda x: x.totalLength, reverse=True)
            >>> ds1.totalLength == ds1tl
            True
            >>> ds2.totalLength == ds2tl
            True
        """
        if contigs:
            return self._split_contigs(chunks, maxChunks)

        # Lets only split on datasets if actual splitting will occur,
        # And if all subdatasets have the required balancing key (totalLength)
        if (len(self.subdatasets) > 1
                and not ignoreSubDatasets):
            return self._split_subdatasets(chunks)

        atoms = self.externalResources.resources
        balanceKey = len

        # If chunks not specified, split to one DataSet per
        # ExternalResource, but no fewer than one ExternalResource per
        # Dataset
        if not chunks or chunks > len(atoms):
            chunks = len(atoms)

        # Nothing to split!
        if chunks == 1:
            tbr = [self.copy()]
            return tbr

        # duplicate
        results = [self.copy() for _ in range(chunks)]

        # replace default (complete) ExternalResource lists
        log.debug("Starting chunking")
        chunks = self._chunkList(atoms, chunks, balanceKey)
        log.debug("Done chunking")
        log.debug("Modifying filters or resources")
        for result, chunk in zip(results, chunks):
            result.externalResources.resources = copy.deepcopy(chunk)

        # UniqueId was regenerated when the ExternalResource list was
        # whole, therefore we need to regenerate it again here
        log.debug("Generating new UUID")
        for result in results:
            result.newUuid()

        # Update the basic metadata for the new DataSets from external
        # resources, or at least mark as dirty
        # TODO
        return results

    def _split_atoms(self, atoms, num_chunks):
        """Divide up atomic units (e.g. contigs) into chunks (refId, size,
        segments)
        """
        for _ in range(num_chunks - len(atoms)):
            largest = max(atoms, key=lambda x: x[1]/x[2])
            largest[2] += 1
        return atoms

    def _split_contigs(self, chunks, maxChunks=0):
        """Split a dataset into reference windows based on contigs.

        Args:
            chunks: The number of chunks to emit. If chunks < # contigs,
                    contigs are grouped by size. If chunks == contigs, one
                    contig is assigned to each dataset regardless of size. If
                    chunks >= contigs, contigs are split into roughly equal
                    chunks (<= 1.0 contig per file).

        """
        # removed the non-trivial case so that it is still filtered to just
        # contigs with associated records

        # The format is rID, start, end, for a reference window
        refNames = self.refNames
        log.debug("{i} references found".format(i=len(refNames)))
        log.debug("Finding contigs")
        if len(refNames) < 100:
            atoms = [(rn, None, None) for rn in refNames if
                     next(self._indexReadsInReference(rn), None)]
        else:
            log.debug("Skipping records for each reference check")
            atoms = [(rn, None, None) for rn in self.refNames]

        # The window length is used for balancing
        # TODO switch it to countRecords
        balanceKey = lambda x: x[2] - x[1]
        if not chunks:
            chunks = len(atoms)
        if maxChunks and chunks > maxChunks:
            chunks = maxChunks
        log.debug("Fetching reference lengths")
        refLens = self.refLengths
        # refwindow format: rId, start, end
        atoms = [(rn, 0, refLens[rn]) for rn, _, _ in atoms]
        if chunks > len(atoms):
            # splitting atom format is slightly different (but more compatible
            # going forward with countRecords): (rId, size, segments)
            atoms = [[rn, refLens[rn], 1] for rn, _, _ in atoms]
            log.debug("Splitting atoms")
            atoms = self._split_atoms(atoms, chunks)
            segments = []
            for atom in atoms:
                segment_size = atom[1]/atom[2]
                sub_segments = [(atom[0], segment_size * i, segment_size *
                                 (i + 1)) for i in range(atom[2])]
                # if you can't divide it evenly you may have some messiness
                # with the last window. Fix it:
                tmp = sub_segments.pop()
                tmp = (tmp[0], tmp[1], refLens[tmp[0]])
                sub_segments.append(tmp)
                segments.extend(sub_segments)
            atoms = segments
        log.debug("Done defining chunks")

        # duplicate
        log.debug("Making copies")
        results = [self.copy() for _ in range(chunks)]

        # replace default (complete) ExternalResource lists
        log.debug("Distributing chunks")
        chunks = self._chunkList(atoms, chunks, balanceKey)
        log.debug("Done chunking")
        log.debug("Modifying filters or resources")
        for result, chunk in zip(results, chunks):
            if not atoms[0][2] is None:
                result.filters.addRequirement(
                    rname=[('=', c[0]) for c in chunk],
                    tStart=[('>', c[1]) for c in chunk],
                    tEnd=[('<', c[2]) for c in chunk])
            else:
                result.filters.addRequirement(
                    rname=[('=', c[0]) for c in chunk])

        # UniqueId was regenerated when the ExternalResource list was
        # whole, therefore we need to regenerate it again here
        log.debug("Generating new UUID")
        for result in results:
            result.newUuid()

        # Update the basic metadata for the new DataSets from external
        # resources, or at least mark as dirty
        # TODO
        return results

    def _split_subdatasets(self, chunks):
        """Split on subdatasets

        Args:
            chunks: Split in to <= chunks pieces. If chunks > subdatasets,
                    fewer chunks will be produced.

        """
        if not chunks or chunks > len(self.subdatasets):
            chunks = len(self.subdatasets)

        if (chunks == len(self.subdatasets)
                and all([sds.externalResources.resourceIds
                         for sds in self.subdatasets])):
            return self.subdatasets

        # Chunk subdatasets into sets of subdatasets of roughly equal
        # lengths
        chunks = self._chunkList(
            self.subdatasets, chunks,
            balanceKey=lambda x: x.metadata.numRecords)

        # Merge the lists of datasets into single datasets to return
        results = []
        for subDatasets in chunks:
            newCopy = self.copy()
            newCopy.subdatasets = subDatasets
            newCopy.newUuid()
            results.append(newCopy)
        return results

    def write(self, outFile, validate=True, relPaths=False, pretty=True):
        """Write to disk as an XML file

        Args:
            outFile: The filename of the xml file to be created
            validate: T/F (True) validate the ExternalResource ResourceIds
            relPaths: T/F (False) make the ExternalResource ResourceIds
                      relative instead of absolute filenames

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet
            >>> import tempfile, os
            >>> outdir = tempfile.mkdtemp(suffix="dataset-doctest")
            >>> outfile = os.path.join(outdir, 'tempfile.xml')
            >>> ds1 = DataSet(data.getXml())
            >>> ds1.write(outfile, validate=False)
            >>> ds2 = DataSet(outfile)
            >>> ds1 == ds2
            True
        """
        # fix paths if validate:
        if validate:
            if relPaths:
                self.makePathsRelative(os.path.dirname(outFile))
            else:
                self.makePathsAbsolute()
        xml_string = toXml(self)
        if pretty:
            xml_string = xml.dom.minidom.parseString(xml_string).toprettyxml()
        if validate:
            validateString(xml_string, relTo=outFile)
        fileName = urlparse(outFile).path.strip()
        if self._strict and not isinstance(self.datasetType, tuple):
            if not fileName.endswith(_dsIdToSuffix(self.datasetType)):
                raise IOError(errno.EIO,
                              "Given filename does not meet standards, "
                              "should end with {s}".format(
                                  s=_dsIdToSuffix(self.datasetType)),
                              fileName)
        with open(fileName, 'w') as outFile:
            outFile.writelines(xml_string)

    def loadStats(self, filename):
        """Load pipeline statistics from a <moviename>.sts.xml file. The subset
        of these data that are defined in the DataSet XSD become available
        through via DataSet.metadata.summaryStats.<...> and will be written out
        to the DataSet XML format according to the DataSet XML XSD.

        Args:
            filename: the filename of a <moviename>.sts.xml file

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import AlignmentSet
            >>> ds1 = AlignmentSet(data.getXml(8))
            >>> ds1.loadStats(data.getStats())
            >>> ds2 = AlignmentSet(data.getXml(11))
            >>> ds2.loadStats(data.getStats())
            >>> ds3 = ds1 + ds2
            >>> ds1.metadata.summaryStats.prodDist.bins
            [1576, 901, 399, 0]
            >>> ds2.metadata.summaryStats.prodDist.bins
            [1576, 901, 399, 0]
            >>> ds3.metadata.summaryStats.prodDist.bins
            [3152, 1802, 798, 0]

        """
        statsMetadata = parseStats(filename)
        if self.metadata.summaryStats:
            self.metadata.summaryStats.merge(statsMetadata)
        else:
            self.metadata.append(statsMetadata)

    def processFilters(self):
        """Generate a list of functions to apply to a read, all of which return
        T/F. Each function is an OR filter, so any() true passes the read.
        These functions are the AND filters, and will likely check all() of
        other functions. These filtration functions are cached so that they are
        not regenerated from the base filters for every read"""
        # Allows us to not process all of the filters each time. This is marked
        # as dirty (= []) by addFilters etc. Filtration can be turned off by
        # setting this to [lambda x: True], which can be reversed by marking
        # the cache dirty. See disableFilters/enableFilters
        if self._cachedFilters:
            return self._cachedFilters
        filters = self.filters.tests()
        # Having no filters means no opportunity to pass. Fix by filling with
        # always-true (similar to disableFilters())
        if not filters:
            self._cachedFilters = [lambda x: True]
            return self._cachedFilters
        self._cachedFilters = filters
        return filters

    def makePathsAbsolute(self, curStart="."):
        """As part of the validation process, make all ResourceIds absolute
        URIs rather than relative paths. Generally not called by API users.

        Args:
            curStart: The location from which relative paths should emanate.
        """
        self._changePaths(
            lambda x, s=curStart: resolveLocation(x, s))

    def makePathsRelative(self, outDir=False):
        """Make things easier for writing test cases: make all
        ResourceIds relative paths rather than absolute paths.
        A less common use case for API consumers.

        Args:
            outDir: The location from which relative paths should originate

        """
        if outDir:
            self._changePaths(lambda x, s=outDir: os.path.relpath(x, s))
        else:
            self._changePaths(os.path.relpath)

    def _modResources(self, func):
        # check all ExternalResources
        stack = list(self.externalResources)
        while stack:
            item = stack.pop()
            resId = item.resourceId
            if not resId:
                continue
            func(item)
            try:
                stack.extend(list(item.indices))
            except AttributeError:
                # Some things just don't have indices
                pass

        # check all SubDatasets
        for dataset in self.subdatasets:
            dataset._modResources(func)

    def _changePaths(self, osPathFunc, checkMetaType=True):
        """Change all resourceId paths in this DataSet according to the
        osPathFunc provided.

        Args:
            osPathFunc: A function for modifying paths (e.g. os.path.abspath)
            checkMetaType: Update the metatype of externalResources if needed
        """
        # check all ExternalResources
        stack = list(self.externalResources)
        while stack:
            item = stack.pop()
            resId = item.resourceId
            if not resId:
                continue
            currentPath = urlparse(resId)
            if currentPath.scheme == 'file' or not currentPath.scheme:
                currentPath = currentPath.path
                currentPath = osPathFunc(currentPath)
                item.resourceId = currentPath
                if checkMetaType:
                    self._updateMetaType(item)
            try:
                stack.extend(list(item.indices))
            except AttributeError:
                # Some things just don't have indices
                pass

        # check all DataSetMetadata

        # check all SubDatasets
        for dataset in self.subdatasets:
            dataset._changePaths(osPathFunc)

    def _populateMetaTypes(self):
        self._modResources(self._updateMetaType)

    def _updateMetaType(self, resource):
        """Infer and set the metatype of 'resource' if it doesn't already have
        one."""
        if not resource.metaType:
            file_type = _fileType(resource.resourceId)
            resource.metaType = self._metaTypeMapping().get(file_type, "")

    @staticmethod
    def _metaTypeMapping():
        """The available mappings between file extension and MetaType (informed
        by current class)."""
        # no metatypes for generic DataSet
        return {}

    def copyFiles(self, outdir):
        backticks('cp {i} {o}'.format(i=' '.join(self.toExternalFiles()),
                                      o=outdir))

    def disableFilters(self):
        """Disable read filtering for this object"""
        self.noFiltering = True
        self._cachedFilters = [lambda x: True]

    def enableFilters(self):
        """Re-enable read filtering for this object"""
        self.noFiltering = False
        self._cachedFilters = []

    def addFilters(self, newFilters):
        """Add new or extend the current list of filters. Public because there
        is already a reasonably compelling reason (the console script entry
        point). Most often used by the __add__ method.

        Args:
            newFilters: a Filters object or properly formatted Filters record

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet
            >>> from pbcore.io.dataset.DataSetMembers import Filters
            >>> ds1 = DataSet()
            >>> filt = Filters()
            >>> filt.addRequirement(rq=[('>', '0.85')])
            >>> ds1.addFilters(filt)
            >>> print ds1.filters
            ( rq > 0.85 )
            >>> # Or load with a DataSet
            >>> ds2 = DataSet(data.getXml(16))
            >>> print ds2.filters
            ... # doctest:+ELLIPSIS
            ( rname = E.faecalis...
        """
        self.filters.merge(copy.deepcopy(newFilters))
        self._cachedFilters = []

    def _checkObjMetadata(self, newMetadata):
        """Check new object metadata (as opposed to dataset metadata) against
        the object metadata currently in this DataSet for compatibility.

        Args:
            newMetadata: The object metadata of a DataSet being considered for
                         merging
        """
        if self.objMetadata.get('Version'):
            if newMetadata.get('Version') > self.objMetadata.get('Version'):
                raise ValueError("Wrong dataset version for merging {v1} vs "
                                 "{v2}".format(
                                        v1=newMetadata.get('Version'),
                                        v2=self.objMetadata.get('Version')))


    def addMetadata(self, newMetadata, **kwargs):
        """Add dataset metadata.

        Currently we ignore duplicates while merging (though perhaps other
        transformations are more appropriate) and plan to remove/merge
        conflicting metadata with identical attribute names.

        All metadata elements should be strings, deepcopy shouldn't be
        necessary.

        This method is most often used by the __add__ method, rather than
        directly.

        Args:
            newMetadata: a dictionary of object metadata from an XML file (or
                         carefully crafted to resemble one), or a wrapper
                         around said dictionary
            kwargs: new metadata fields to be piled into the current metadata
                    (as an attribute)

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet
            >>> ds = DataSet()
            >>> # it is possible to add new metadata:
            >>> ds.addMetadata(None, Name='LongReadsRock')
            >>> print ds._metadata.getV(container='attrib', tag='Name')
            LongReadsRock
            >>> # but most will be loaded and modified:
            >>> ds2 = DataSet(data.getXml(no=8))
            >>> ds2._metadata.totalLength
            123588
            >>> ds2._metadata.totalLength = 100000
            >>> ds2._metadata.totalLength
            100000
            >>> ds2._metadata.totalLength += 100000
            >>> ds2._metadata.totalLength
            200000
            >>> ds3 = DataSet(data.getXml(no=8))
            >>> ds3.loadStats(data.getStats())
            >>> ds4 = DataSet(data.getXml(no=11))
            >>> ds4.loadStats(data.getStats())
            >>> ds5 = ds3 + ds4
        """
        if newMetadata:
            # if this record is not wrapped, wrap for easier merging
            if not isinstance(newMetadata, DataSetMetadata):
                newMetadata = DataSetMetadata(newMetadata)
            # merge
            if self.metadata:
                self.metadata.merge(newMetadata)
            # or initialize
            else:
                self._metadata = newMetadata

        for key, value in kwargs.items():
            self.metadata.addMetadata(key, value)

    def updateCounts(self):
        self.metadata.totalLength = -1
        self.metadata.numRecords = -1

    def assertIndexed(self):
        if not self._openReaders:
            try:
                tmp = self._strict
                self._openFiles()
            except Exception:
                self._strict = tmp
                raise
            finally:
                self._strict = tmp
        else:
            for fname, reader in zip(self.toExternalFiles(),
                                     self.resourceReaders()):
                if (not isinstance(reader, IndexedBamReader) and
                        not isinstance(reader, CmpH5Reader)):
                    raise IOError(errno.EIO,
                                  "File not indexed: {f}".format(f=fname),
                                  fname)


    def addExternalResources(self, newExtResources, updateCount=True):
        """Add additional ExternalResource objects, ensuring no duplicate
        resourceIds. Most often used by the __add__ method, rather than
        directly.

        Args:
            newExtResources: A list of new ExternalResource objects, either
                             created de novo from a raw bam input, parsed from
                             an xml input, or already contained in a separate
                             DataSet object and being merged.
        Doctest:
            >>> from pbcore.io.dataset.DataSetMembers import ExternalResource
            >>> from pbcore.io import DataSet
            >>> ds = DataSet()
            >>> # it is possible to add ExtRes's as ExternalResource objects:
            >>> er1 = ExternalResource()
            >>> er1.resourceId = "test1.bam"
            >>> er2 = ExternalResource()
            >>> er2.resourceId = "test2.bam"
            >>> er3 = ExternalResource()
            >>> er3.resourceId = "test1.bam"
            >>> ds.addExternalResources([er1], updateCount=False)
            >>> len(ds.externalResources)
            1
            >>> # different resourceId: succeeds
            >>> ds.addExternalResources([er2], updateCount=False)
            >>> len(ds.externalResources)
            2
            >>> # same resourceId: fails
            >>> ds.addExternalResources([er3], updateCount=False)
            >>> len(ds.externalResources)
            2
            >>> # but it is probably better to add them a little deeper:
            >>> ds.externalResources.addResources(
            ...     ["test3.bam"])[0].addIndices(["test3.bam.bai"])
        """
        # Build list of current resourceIds
        resourceIds = [extRes.resourceId for extRes in
                       self.externalResources]

        for newExtRes in newExtResources:
            if isinstance(newExtRes, str):
                newExtRes = wrapNewResource(newExtRes)

            # merge duplicates instead of adding them
            if newExtRes.resourceId in resourceIds:
                first = resourceIds.index(newExtRes.resourceId)
                self.externalResources[first].merge(newExtRes)

            # add non-duplicates, update the list of current resourceIds
            else:
                self.externalResources.append(newExtRes)
                resourceIds.append(newExtRes.resourceId)
        if updateCount:
            self._openFiles()
            self.updateCounts()

    def addDatasets(self, otherDataSet):
        """Add subsets to a DataSet object using other DataSets.

        The following method of enabling merge-based split prevents nesting of
        datasets more than one deep. Nested relationships are flattened.

        .. note::

            Most often used by the __add__ method, rather than directly.

        """
        if otherDataSet.subdatasets:
            self.subdatasets.extend(otherDataSet.subdatasets)
        else:
            self.subdatasets.append(otherDataSet)

    def _openFiles(self, refFile=None):
        """Open the files (assert they exist, assert they are of the proper
        type before accessing any file)
        """
        if self._openReaders:
            log.debug("Closing old readers...")
            self.close()
        log.debug("Opening resources")
        for extRes in self.externalResources:
            location = urlparse(extRes.resourceId).path
            try:
                resource = openIndexedAlignmentFile(
                    location,
                    referenceFastaFname=refFile)
            except (IOError, ValueError):
                if not self._strict:
                    log.info("pbi file missing for {f}, operating with "
                             "reduced speed and functionality".format(
                                 f=location))
                    resource = openAlignmentFile(location,
                                                 referenceFastaFname=refFile)
                else:
                    raise
            if not resource:
                raise IOError(errno.EIO,
                              "{f} fails to open".format(f=location),
                              location)
            self._openReaders.append(resource)
        log.debug("Done opening resources")


    def resourceReaders(self, refName=False):
        """A generator of Indexed*Reader objects for the ExternalResources
        in this DataSet.

        Args:
            refName: Only yield open resources if they have refName in their
                     referenceInfoTable

        Yields:
            An open indexed alignment file

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet
            >>> ds = DataSet(data.getBam())
            >>> for seqFile in ds.resourceReaders():
            ...     for record in seqFile:
            ...         print 'hn: %i' % record.holeNumber # doctest:+ELLIPSIS
            hn: ...

        """
        if refName:
            if (not refName in self.refNames and
                    not refName in self.fullRefNames):
                _ = int(refName)
                refName = self._idToRname(refName)

        if not self._openReaders:
            self._openFiles()
        if refName:
            return [resource for resource in self._openReaders
                    if refName in resource.referenceInfoTable['FullName'] or
                    refName in resource.referenceInfoTable['Name']]
        else:
            return self._openReaders

    @property
    def indexRecords(self):
        """Yields chunks of recarray summarizing all of the records in all of
        the resources that conform to those filters addressing parameters
        cached in the pbi.
        """
        self.assertIndexed()
        for rr in self.resourceReaders():
            indices = rr.index
            if not self._filters or self.noFiltering:
                yield indices
                continue

            tIdMap = {n: name
                      for n, name in enumerate(rr.referenceInfoTable['Name'])}
            filts = self._filters.tests(readType='pbi', tIdMap=tIdMap)
            mask = np.zeros(len(indices), dtype=bool)
            # remove reads per filter
            for i, read in enumerate(indices):
                if any([filt(read) for filt in filts]):
                    mask[i] = True
            yield np.extract(mask, indices)

    @property
    @filtered
    def records(self):
        """A generator of (usually) BamAlignment objects for the
        records in one or more Bam files pointed to by the
        ExternalResources in this DataSet.

        Yields:
            A BamAlignment object

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet
            >>> ds = DataSet(data.getBam())
            >>> for record in ds.records:
            ...     print 'hn: %i' % record.holeNumber # doctest:+ELLIPSIS
            hn: ...
        """
        for resource in self.resourceReaders():
            for record in resource:
                yield record

    @filtered
    def __iter__(self):
        """ Iterate over the records. (sorted for AlignmentSet objects)"""
        for record in self.records:
            yield record

    @property
    def subSetNames(self):
        """The subdataset names present in this DataSet"""
        subNames = []
        for sds in self.subdatasets:
            subNames.extend(sds.name)
        return subNames

    @filtered
    def readsInSubDatasets(self, subNames=[]):
        """To be used in conjunction with self.subSetNames"""
        if self.subdatasets:
            for sds in self.subdatasets:
                if subNames and sds.name not in subNames:
                    continue
                # subdatasets often don't have the same resourcess
                if not sds.externalResources.resourceIds:
                    sds.externalResources = self.externalResources
                # this should enforce the subdataset filters:
                for read in sds.records:
                    yield read
        else:
            for read in self.records:
                yield read

    @property
    def refWindows(self):
        """Going to be tricky unless the filters are really focused on
        windowing the reference. Much nesting or duplication and the correct
        results are really not guaranteed"""
        windowTuples = []
        nameIDs = self.refInfo('Name')
        refLens = None
        for name, refID in nameIDs:
            for filt in self._filters:
                thisOne = False
                for param in filt:
                    if param.name == 'rname':
                        if param.value == name:
                            thisOne = True
                if thisOne:
                    winstart = 0
                    winend = -1
                    for param in filt:
                        if param.name == 'tstart':
                            winstart = param.value
                        if param.name == 'tend':
                            winend = param.value
                    # If the filter is just for rname, fill the window
                    # boundaries (pricey but worth the guaranteed behavior)
                    if winend == -1:
                        if not refLens:
                            refLens = self.refLengths
                        winend = refLens[name]
                    windowTuples.append((refID, int(winstart), int(winend)))
        # no tuples found: return full length of each reference
        if not windowTuples:
            for name, refId in nameIDs:
                if not refLens:
                    refLens = self.refLengths
                refLen = refLens[name]
                windowTuples.append((refId, 0, refLen))
        return windowTuples

    @property
    def refNames(self):
        """A list of reference names (id)."""
        if self.isCmpH5:
            return [self._cleanCmpName(name) for _, name in
                    self.refInfo('FullName')]
        return sorted([name for _, name in self.refInfo('Name')])

    def _cleanCmpName(self, name):
        return splitFastaHeader(name)[0]

    @property
    def refLengths(self):
        """A dict of refName: refLength"""
        return {name: length for name, length in self.refInfo('Length')}

    def refLength(self, rname):
        """The length of reference 'rname'. This is expensive, so if you're
        going to do many lookups cache self.refLengths locally and use that."""
        lut = self.refLengths
        return lut[rname]

    @property
    def fullRefNames(self):
        """A list of reference full names (full header)."""
        return [name for _, name in self.refInfo('FullName')]

    def refInfo(self, key):
        """The reference names present in the referenceInfoTable of the
        ExtResources.

        Args:
            key: a key for the referenceInfoTable of each resource
        Returns:
            A dictionary of refrence name: key_result pairs"""
        # sample
        names = self.referenceInfoTable['Name']
        infos = self.referenceInfoTable[key]
        # remove dupes
        sampled = zip(names, infos)
        sampled = list(set(sampled))
        # filter
        if not self.noFiltering:
            sampled = [(name, info) for name, info in sampled
                       if self._filters.testParam('rname', name)]
        return sampled

    def _indexReadsInReference(self, refName):
        if isinstance(refName, np.int64):
            refName = str(refName)
        if refName.isdigit():
            if (not refName in self.refNames
                    and not refName in self.fullRefNames):
                try:
                    refName = self._idToRname(int(refName))
                except AttributeError:
                    raise StopIteration

        # I would love to use readsInRange(refName, None, None), but
        # IndexedBamReader breaks this (works for regular BamReader).
        # So I have to do a little hacking...
        refLen = 0
        for resource in self.resourceReaders():
            if (refName in resource.referenceInfoTable['Name'] or
                    refName in resource.referenceInfoTable['FullName']):
                refLen = resource.referenceInfo(refName).Length
                break
        if refLen:
            for read in self._indexReadsInRange(refName, 0, refLen):
                yield read

    @filtered
    def readsInReference(self, refName):
        """A generator of (usually) BamAlignment objects for the
        reads in one or more Bam files pointed to by the ExternalResources in
        this DataSet that are mapped to the specified reference genome.

        Args:
            refName: the name of the reference that we are sampling.

        Yields:
            BamAlignment objects

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet
            >>> ds = DataSet(data.getBam())
            >>> for read in ds.readsInReference(ds.refNames[15]):
            ...     print 'hn: %i' % read.holeNumber # doctest:+ELLIPSIS
            hn: ...
        """

        if isinstance(refName, np.int64):
            refName = str(refName)
        if refName.isdigit():
            if (not refName in self.refNames
                    and not refName in self.fullRefNames):
                try:
                    refName = self._idToRname(int(refName))
                except AttributeError:
                    raise StopIteration

        # I would love to use readsInRange(refName, None, None), but
        # IndexedBamReader breaks this (works for regular BamReader).
        # So I have to do a little hacking...
        refLen = 0
        for resource in self.resourceReaders():
            if (refName in resource.referenceInfoTable['Name'] or
                    refName in resource.referenceInfoTable['FullName']):
                refLen = resource.referenceInfo(refName).Length
                break
        if refLen:
            for read in self.readsInRange(refName, 0, refLen):
                yield read


    def _indexReadsInRange(self, refName, start, end):
        if isinstance(refName, np.int64):
            refName = str(refName)
        if refName.isdigit():
            if (not refName in self.refNames and
                    not refName in self.fullRefNames):
                # we need the real refName, which may be hidden behind a
                # mapping to resolve duplicate refIds between resources...
                refName = self._idToRname(int(refName))
        for reader in self.resourceReaders():
            tIdMap = {n: name
                      for n, name in enumerate(
                          reader.referenceInfoTable['Name'])}
            filts = self._filters.tests(readType='pbi', tIdMap=tIdMap)
            index = reader.index
            winId = reader.referenceInfo(refName).ID
            for rec_i in index.rangeQuery(winId, start, end):
                read = index[rec_i]
                if filts:
                    if any([filt(read) for filt in filts]):
                        yield read
                else:
                    yield read

    @filtered
    def readsInRange(self, refName, start, end, buffsize=50):
        """A generator of (usually) BamAlignment objects for the reads in one
        or more Bam files pointed to by the ExternalResources in this DataSet
        that have at least one coordinate within the specified range in the
        reference genome.

        Rather than developing some convoluted approach for dealing with
        auto-inferring the desired references, this method and self.refNames
        should allow users to compose the desired query.

        Args:
            refName: the name of the reference that we are sampling
            start: the start of the range (inclusive, index relative to
                   reference)
            end: the end of the range (inclusive, index relative to reference)

        Yields:
            BamAlignment objects

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet
            >>> ds = DataSet(data.getBam())
            >>> for read in ds.readsInRange(ds.refNames[15], 100, 150):
            ...     print 'hn: %i' % read.holeNumber # doctest:+ELLIPSIS
            hn: ...
        """
        if isinstance(refName, np.int64):
            refName = str(refName)
        if refName.isdigit():
            if (not refName in self.refNames and
                    not refName in self.fullRefNames):
                # we need the real refName, which may be hidden behind a
                # mapping to resolve duplicate refIds between resources...
                refName = self._idToRname(int(refName))

        # merge sort before yield
        if self.numExternalResources > 1:
            if buffsize > 1:
                read_its = [iter(rr.readsInRange(refName, start, end))
                            for rr in self.resourceReaders()]
                # scale to per reader buffsize:
                # remove empty iterators
                deep_buf = [[next(it, None) for _ in range(buffsize)]
                            for it in read_its]
                read_its = [it for it, cur in zip(read_its, deep_buf)
                            if cur[0]]
                deep_buf = [buf for buf in deep_buf if buf[0]]
                buf_indices = [0 for _ in read_its]
                tStarts = [cur[0].tStart for cur in deep_buf]
                while len(read_its) != 0:
                    # pick the first one to yield
                    # this should be a bit faster than taking the min of an
                    # enumeration of currents with a key function accessing a
                    # field...
                    first = min(tStarts)
                    first_i = tStarts.index(first)
                    buf_index = buf_indices[first_i]
                    assert all([buf[buf_i] for buf, buf_i
                                in zip(deep_buf, buf_indices)])
                    first = deep_buf[first_i][buf_index]
                    # update the buffers
                    buf_index += 1
                    buf_indices[first_i] += 1
                    if buf_index == buffsize:
                        buf_index = 0
                        buf_indices[first_i] = 0
                        deep_buf[first_i] = [next(read_its[first_i], None)
                                             for _ in range(buffsize)]
                    if not deep_buf[first_i][buf_index]:
                        del read_its[first_i]
                        del tStarts[first_i]
                        del deep_buf[first_i]
                        del buf_indices[first_i]
                    else:
                        tStarts[first_i] = deep_buf[first_i][buf_index].tStart
                    assert first
                    yield first
            else:
                read_its = [iter(rr.readsInRange(refName, start, end))
                            for rr in self.resourceReaders()]
                # buffer one element from each generator
                currents = [next(its, None) for its in read_its]
                # remove empty iterators
                read_its = [it for it, cur in zip(read_its, currents) if cur]
                currents = [cur for cur in currents if cur]
                tStarts = [cur.tStart for cur in currents]
                while len(read_its) != 0:
                    # pick the first one to yield
                    # this should be a bit faster than taking the min of an
                    # enumeration of currents with a key function accessing a
                    # field...
                    first = min(tStarts)
                    first_i = tStarts.index(first)
                    first = currents[first_i]
                    # update the buffers
                    try:
                        currents[first_i] = next(read_its[first_i])
                        tStarts[first_i] = currents[first_i].tStart
                    except StopIteration:
                        del read_its[first_i]
                        del currents[first_i]
                        del tStarts[first_i]
                    yield first
        else:
            # the above will work in either case, but this might be ever so
            # slightly faster
            for resource in self.resourceReaders():
                for read in resource.readsInRange(refName, start, end):
                    yield read

    def _idToRname(self, rId):
        """Map the DataSet.referenceInfoTable.ID to the superior unique
        reference identifier: referenceInfoTable.Name

        Args:
            rId: The DataSet.referenceInfoTable.ID of interest

        Returns:
            The referenceInfoTable.Name corresponding to rId
        """
        resNo, rId = self._referenceIdMap[rId]
        if self.isCmpH5:
            rId -= 1
        if self.isCmpH5:
            # This is what CmpIO recognizes as the 'shortname'
            refName = self.resourceReaders()[
                resNo].referenceInfoTable[rId]['FullName']
        else:
            refName = self.resourceReaders()[
                resNo].referenceInfoTable[rId]['Name']
        return refName

    def toFofn(self, outfn=None, uri=False, relative=False):
        """Return a list of resource filenames (and write to optional outfile)

        Args:
            outfn: (None) the file to which the resouce filenames are to be
                   written. If None, the only emission is a returned list of
                   file names.
            uri: (t/F) write the resource filenames as URIs.
            relative: (t/F) emit paths relative to outfofn or '.' if no
                      outfofn

        Returns:
            A list of filenames or uris

        Writes:
            (Optional) A file containing a list of filenames or uris

        Doctest:
            >>> from pbcore.io import DataSet
            >>> DataSet("bam1.bam", "bam2.bam", strict=False).toFofn(uri=False)
            ['bam1.bam', 'bam2.bam']
        """
        lines = [er.resourceId for er in self.externalResources]
        if not uri:
            lines = [urlparse(line).path for line in lines]
        if relative is True:
            # make it relative to the fofn location
            if outfn:
                lines = [os.path.relpath(line, os.path.dirname(outfn))
                         for line in lines]
            # or current location
            else:
                lines = [os.path.relpath(line) for line in lines]
        if outfn:
            with open(outfn, 'w') as outFile:
                outFile.writelines(line + '\n' for line in lines)
        return lines

    def toExternalFiles(self):
        """Returns a list of top level external resources (no indices)."""
        files = self.externalResources.resourceIds
        tbr = []
        for fname in files:
            tbr.append(resolveLocation(fname, '.'))
        return tbr

    @property
    def _castableDataSetTypes(self):
        if isinstance(self.datasetType, tuple):
            return self.datasetType
        else:
            return (_toDsId('DataSet'), self.datasetType)

    @classmethod
    def castableTypes(cls):
        """The types to which this DataSet type may be cast. This is a property
        instead of a member variable as we can enforce casting limits here (and
        modify if needed by overriding them in subclasses).

        Returns:
            A dictionary of MetaType->Class mappings, e.g. 'DataSet': DataSet
        """
        if cls.__name__ != 'DataSet':
            return {'DataSet': DataSet,
                    cls.__name__: cls}
        return {'DataSet': DataSet,
                'SubreadSet': SubreadSet,
                'HdfSubreadSet': HdfSubreadSet,
                'AlignmentSet': AlignmentSet,
                'ContigSet': ContigSet,
                'ConsensusReadSet': ConsensusReadSet,
                'ReferenceSet': ReferenceSet,
                'BarcodeSet': BarcodeSet}
    @property
    def metadata(self):
        """Return the DataSet metadata as a DataSetMetadata object. Attributes
        should be populated intuitively, but see DataSetMetadata documentation
        for more detail."""
        return self._metadata

    @metadata.setter
    def metadata(self, newDict):
        """Set the metadata for this object. This is reasonably dangerous, as
        the argument must be a properly formated data structure, as specified
        in the DataSetMetadata documentation. This setter is primarily used
        by other DataSet objects, rather than users or API consumers."""
        if isinstance(newDict, DataSetMetadata):
            self._metadata = newDict
        else:
            self._metadata = self._metadata.__class__(newDict)

    @property
    def filters(self):
        """Limit setting to ensure cache hygiene and filter compatibility"""
        self._filters.registerCallback(lambda x=self: x.reFilter())
        return self._filters

    @filters.setter
    def filters(self, value):
        """Limit setting to ensure cache hygiene and filter compatibility"""
        self._filters = value

    def reFilter(self):
        """
        The filters on this dataset have changed, update DataSet state as
        needed
        """
        self._cachedFilters = []
        #self.updateCounts()
        self.metadata.totalLength = -1
        self.metadata.numRecords = -1
        if self.metadata.summaryStats:
            self.metadata.removeChildren('SummaryStats')

    @property
    def numRecords(self):
        """The number of records in this DataSet (from the metadata)"""
        return self._metadata.numRecords

    def countRecords(self, rname=None, window=None):
        """Count the number of records mapped to 'rname' that overlap with
        'window'
        """
        def count(iterable):
            count = 0
            for _ in iterable:
                count += 1
            return count

        if window:
            return count(self.readsInRange(rname, *window))
        if rname:
            return count(self.readsInReference(rname))
        else:
            count(self.records)

    @property
    def totalLength(self):
        """The total length of this DataSet"""
        return self._metadata.totalLength

    @property
    def uuid(self):
        """The UniqueId of this DataSet"""
        return self.objMetadata.get('UniqueId')

    @property
    def name(self):
        """The name of this DataSet"""
        return self.objMetadata.get('Name', '')

    @name.setter
    def name(self, value):
        """The name of this DataSet"""
        self.objMetadata['Name'] = value

    @property
    def numExternalResources(self):
        """The number of ExternalResources in this DataSet"""
        return len(self.externalResources)

    def _pollResources(self, func, refName=None):
        """Collect the responses to func on each resource (or those with reads
        mapping to refName)."""
        return [func(resource) for resource in self.resourceReaders(refName)]

    def _unifyResponses(self, responses, keyFunc=lambda x: x):
        """Make sure all of the responses from resources are the same."""
        if len(responses) > 1:
            # Check the rest against the first:
            for res in responses[1:]:
                if keyFunc(responses[0]) != keyFunc(res):
                    raise ResourceMismatchError(responses)
        return responses[0]

    @property
    def isCmpH5(self):
        """Test whether all resources are cmp.h5 files"""
        res = self._pollResources(lambda x: isinstance(x, CmpH5Reader))
        return self._unifyResponses(res)

    @property
    def hasPbi(self):
        """Test whether all resources are opened as IndexedBamReader objects"""
        try:
            res = self._pollResources(lambda x: isinstance(x,
                                                           IndexedBamReader))
            return self._unifyResponses(res)
        except ResourceMismatchError:
            if not self._strict:
                log.error("Resources inconsistently indexed")
                return False
            else:
                raise

    def referenceInfo(self, refName):
        """Select a row from the DataSet.referenceInfoTable using the reference
        name as a unique key"""
        if not self.isCmpH5:
            for row in self.referenceInfoTable:
                if row.Name == refName:
                    return row
        else:
            for row in self.referenceInfoTable:
                if row.FullName.startswith(refName):
                    return row

    @property
    def referenceInfoTable(self):
        """The merged reference info tables from the external resources.
        Record.ID is remapped to a unique integer key (though using record.Name
        is preferred). Record.Names are remapped for cmp.h5 files to be
        consistent with bam files.
        """
        # This isn't really possible for cmp.h5 files (rowStart, rowEnd, for
        # instance). Use the resource readers directly instead.
        responses = self._pollResources(lambda x: x.referenceInfoTable)
        if len(responses) > 1:
            assert not self.isCmpH5 # see above
            tbr = reduce(np.append, responses)
            tbr = np.unique(tbr)
            for i, rec in enumerate(tbr):
                rec.ID = i
            return tbr
        else:
            table = responses[0]
            if self.isCmpH5:
                for rec in table:
                    rec.Name = self._cleanCmpName(rec.FullName)
            return table

    @property
    def _referenceIdMap(self):
        """Map the dataset shifted refIds to the [resource, refId] they came
        from.
        """
        # This isn't really possible for cmp.h5 files (rowStart, rowEnd, for
        # instance). Use the resource readers directly instead.
        responses = self._pollResources(lambda x: x.referenceInfoTable)
        if len(responses) > 1:
            assert not self.isCmpH5 # see above
            tbr = reduce(np.append, responses)
            tbrMeta = []
            for i, res in enumerate(responses):
                for j in res['ID']:
                    tbrMeta.append([i, j])
            _, indices = np.unique(tbr, return_index=True)
            tbrMeta = list(tbrMeta[i] for i in indices)
            return {i: meta for i, meta in enumerate(tbrMeta)}
        else:
            return {i: [0, i] for i in responses[0]['ID']}

    @property
    def readGroupTable(self):
        """Combine the readGroupTables of each external resource"""
        responses = self._pollResources(lambda x: x.readGroupTable)
        if len(responses) > 1:
            tbr = reduce(np.append, responses)
            return tbr
        else:
            return responses[0]

    def hasPulseFeature(self, featureName):
        responses = self._pollResources(
            lambda x: x.hasPulseFeature(featureName))
        return self._unifyResponses(responses)

    def pulseFeaturesAvailable(self):
        responses = self._pollResources(lambda x: x.pulseFeaturesAvailable())
        return self._unifyResponses(responses)

    @property
    def sequencingChemistry(self):
        return self._checkIdentical('sequencingChemistry')

    @property
    def isSorted(self):
        return self._checkIdentical('isSorted')

    @property
    def isEmpty(self):
        return self._checkIdentical('isEmpty')

    @property
    def readType(self):
        return self._checkIdentical('readType')

    @property
    def tStart(self):
        return self._checkIdentical('tStart')

    @property
    def tEnd(self):
        return self._checkIdentical('tEnd')

    def _checkIdentical(self, key):
        responses = self._pollResources(lambda x: getattr(x, key))
        return self._unifyResponses(responses)

    def _chunkList(self, inlist, chunknum, balanceKey=len):
        """Divide <inlist> members into <chunknum> chunks roughly evenly using
        a round-robin binning system, return list of lists.

        This is a method so that balanceKey functions can access self."""
        chunks = [[] for _ in range(chunknum)]
        # a lightweight accounting of how big (entry 0) each sublist (numbered
        # by entry 1) is getting
        chunkSizes = [[0, i] for i in range(chunknum)]
        for i, item in enumerate(sorted(inlist, key=balanceKey, reverse=True)):
            # Refresh measure of bin fullness
            chunkSizes.sort()
            # Add one to the emptiest bin
            chunks[chunkSizes[0][1]].append(item)
            mass = balanceKey(item)
            if mass == 0:
                mass += 1
            chunkSizes[0][0] += mass
        return chunks

class InvalidDataSetIOError(Exception):
    """The base class for all DataSetIO related custom exceptions (hopefully)
    """

class ResourceMismatchError(InvalidDataSetIOError):

    def __init__(self, responses):
        super(ResourceMismatchError, self).__init__()
        self.responses = responses

    def __str__(self):
        return "Resources responded differently: " + ', '.join(
            map(str, self.responses))


class ReadSet(DataSet):
    """Base type for read sets, should probably never be used as a concrete
    class"""

    def __init__(self, *files, **kwargs):
        self._referenceFile = None
        super(ReadSet, self).__init__(*files, **kwargs)
        self._metadata = SubreadSetMetadata(self._metadata)

    def _openFiles(self):
        """Open the files (assert they exist, assert they are of the proper
        type before accessing any file)
        """
        if self._openReaders:
            log.debug("Closing old readers...")
            self.close()
        log.debug("Opening SubreadSet resources")
        if self._referenceFile:
            log.debug("Using reference: {r}".format(r=self._referenceFile))
        for extRes in self.externalResources:
            location = urlparse(extRes.resourceId).path
            try:
                resource = openIndexedAlignmentFile(
                    location,
                    referenceFastaFname=self._referenceFile)
            except (IOError, ValueError):
                if not self._strict:
                    log.info("pbi file missing for {f}, operating with "
                             "reduced speed and functionality".format(
                                 f=location))
                    resource = openAlignmentFile(
                        location, referenceFastaFname=self._referenceFile)
                else:
                    raise
            if not resource:
                raise IOError(errno.EIO,
                              "{f} fails to open".format(f=location),
                              location)
            self._openReaders.append(resource)
        log.debug("Done opening resources")

    def addMetadata(self, newMetadata, **kwargs):
        """Add metadata specific to this subtype, while leaning on the
        superclass method for generic metadata. Also enforce metadata type
        correctness."""
        # Validate, clean and prep input data
        if newMetadata:
            if isinstance(newMetadata, dict):
                newMetadata = SubreadSetMetadata(newMetadata)
            elif isinstance(newMetadata, SubreadSetMetadata) or (
                    type(newMetadata).__name__ == 'DataSetMetadata'):
                newMetadata = SubreadSetMetadata(newMetadata.record)
            else:
                raise TypeError("Cannot extend SubreadSetMetadata with "
                                "{t}".format(t=type(newMetadata).__name__))

        # Pull generic values, kwargs, general treatment in super
        super(ReadSet, self).addMetadata(newMetadata, **kwargs)

    @property
    def _length(self):
        """Used to populate metadata in updateCounts"""
        length = -1
        count = -1
        return count, length

    def __len__(self):
        count = 0
        if self._filters:
            count = self._length[0]
        else:
            for reader in self.resourceReaders():
                count += len(reader)
        return count

class HdfSubreadSet(ReadSet):

    datasetType = DataSetMetaTypes.HDF_SUBREAD

    def __init__(self, *files, **kwargs):
        log.debug("Opening HdfSubreadSet")
        kwargs['skipCounts'] = True
        super(HdfSubreadSet, self).__init__(*files, **kwargs)

    def _openFiles(self):
        """Open the files (assert they exist, assert they are of the proper
        type before accessing any file)
        """
        if self._openReaders:
            log.debug("Closing old readers...")
            self.close()
        log.debug("Opening resources")
        for extRes in self.externalResources:
            location = urlparse(extRes.resourceId).path
            resource = BaxH5Reader(location)
            self._openReaders.append(resource)
        log.debug("Done opening resources")

    @staticmethod
    def _metaTypeMapping():
        return {'bax.h5':'PacBio.SubreadFile.SubreadBaxFile', }


class SubreadSet(ReadSet):
    """DataSet type specific to Subreads

    DocTest:

        >>> from pbcore.io import SubreadSet
        >>> from pbcore.io.dataset.DataSetMembers import ExternalResources
        >>> import pbcore.data.datasets as data
        >>> ds1 = SubreadSet(data.getXml(no=5))
        >>> ds2 = SubreadSet(data.getXml(no=5))
        >>> # So they don't conflict:
        >>> ds2.externalResources = ExternalResources()
        >>> ds1 # doctest:+ELLIPSIS
        <SubreadSet...
        >>> ds1._metadata # doctest:+ELLIPSIS
        <SubreadSetMetadata...
        >>> ds1._metadata # doctest:+ELLIPSIS
        <SubreadSetMetadata...
        >>> ds1.metadata # doctest:+ELLIPSIS
        <SubreadSetMetadata...
        >>> len(ds1.metadata.collections)
        1
        >>> len(ds2.metadata.collections)
        1
        >>> ds3 = ds1 + ds2
        >>> len(ds3.metadata.collections)
        2
        >>> ds4 = SubreadSet(data.getSubreadSet())
        >>> ds4 # doctest:+ELLIPSIS
        <SubreadSet...
        >>> ds4._metadata # doctest:+ELLIPSIS
        <SubreadSetMetadata...
        >>> len(ds4.metadata.collections)
        1
    """

    datasetType = DataSetMetaTypes.SUBREAD

    def __init__(self, *files, **kwargs):
        log.debug("Opening SubreadSet")
        super(SubreadSet, self).__init__(*files, **kwargs)

    @property
    def _length(self):
        """Used to populate metadata in updateCounts"""
        length = 0
        count = 0
        endkey = 'qEnd'
        startkey = 'qStart'
        for rec in self.indexRecords:
            count += len(rec)
            if isinstance(rec, np.ndarray):
                length += sum(rec[endkey] - rec[startkey])
            elif isinstance(rec, PacBioBamIndex):
                length += sum(rec.aEnd - rec.aStart)
        return count, length

    @staticmethod
    def _metaTypeMapping():
        # This doesn't work for scraps.bam, whenever that is implemented
        return {'bam':'PacBio.SubreadFile.SubreadBamFile',
                'bai':'PacBio.Index.BamIndex',
                'pbi':'PacBio.Index.PacBioIndex',
                }


class ConsensusReadSet(ReadSet):
    """DataSet type specific to CCSreads. No type specific Metadata exists, so
    the base class version is OK (this just ensures type representation on
    output and expandability

    Doctest:
        >>> import pbcore.data.datasets as data
        >>> from pbcore.io import ConsensusReadSet
        >>> ds2 = ConsensusReadSet(data.getXml(2), strict=False)
        >>> ds2 # doctest:+ELLIPSIS
        <ConsensusReadSet...
        >>> ds2._metadata # doctest:+ELLIPSIS
        <SubreadSetMetadata...
    """

    datasetType = DataSetMetaTypes.CCS

class AlignmentSet(ReadSet):
    """DataSet type specific to Alignments. No type specific Metadata exists,
    so the base class version is OK (this just ensures type representation on
    output and expandability"""

    datasetType = DataSetMetaTypes.ALIGNMENT

    def __init__(self, *files, **kwargs):
        """ An AlignmentSet

        Args:
            *files: handled by super
            referenceFastaFname=None: the reference fasta filename for this
                                      alignment.
            strict=False: see base class
            skipCounts=False: see base class
        """
        log.debug("Opening AlignmentSet with {f}".format(f=files))
        super(AlignmentSet, self).__init__(*files, **kwargs)
        fname = kwargs.get('referenceFastaFname', None)
        if fname:
            self.addReference(fname)

    def addReference(self, fname):
        if isinstance(fname, ReferenceSet):
            reference = fname.externalResources.resourceIds
        else:
            reference = ReferenceSet(fname).externalResources.resourceIds
        if len(reference) > 1:
            log.warn("Multiple references found, cannot open with reads")
        else:
            self._referenceFile = reference[0]
            self._openFiles()

    def updateCounts(self):
        if self._skipCounts:
            self.metadata.totalLength = -1
            self.metadata.numRecords = -1
            return
        try:
            self.assertIndexed()
            log.debug('Updating counts')
            numRecords, totalLength = self._length
            self.metadata.totalLength = totalLength
            self.metadata.numRecords = numRecords
        # I would prefer to just catch IOError and UnavailableFeature
        except Exception as e:
            if not self._strict:
                log.debug("File problem ({e}), metadata not "
                          "populated".format(e=str(e)))
                self.metadata.totalLength = -1
                self.metadata.numRecords = -1
            else:
                raise

    @property
    def _length(self):
        """Used to populate metadata in updateCounts"""
        length = 0
        count = 0
        endkey = 'aEnd'
        startkey = 'aStart'
        if self.isCmpH5:
            endkey = 'rEnd'
            startkey = 'rStart'
        for rec in self.indexRecords:
            count += len(rec)
            if isinstance(rec, np.ndarray):
                length += sum(rec[endkey] - rec[startkey])
            elif isinstance(rec, PacBioBamIndex):
                length += sum(rec.aEnd - rec.aStart)
        return count, length

    def __len__(self):
        count = 0
        if self._filters:
            count = self._length[0]
        else:
            for reader in self.resourceReaders():
                count += len(reader)
        return count


    @property
    def recordsByReference(self):
        """ The records in this AlignmentSet, sorted by tStart. """
        # we only care about aligned sequences here, so we can make this a
        # chain of readsInReferences to add pre-filtering by rname, instead of
        # going through every record and performing downstream filtering.
        # This will make certain operations, like len(), potentially faster
        for rname in self.refNames:
            for read in self.readsInReference(rname):
                yield read

    @staticmethod
    def _metaTypeMapping():
        # This doesn't work for scraps.bam, whenever that is implemented
        return {'bam':'PacBio.SubreadFile.SubreadBamFile',
                'bai':'PacBio.Index.BamIndex',
                'pbi':'PacBio.Index.PacBioIndex',
               }


class ContigSet(DataSet):
    """DataSet type specific to Contigs"""

    datasetType = DataSetMetaTypes.CONTIG

    def __init__(self, *files, **kwargs):
        log.debug("Opening ContigSet")
        super(ContigSet, self).__init__(*files, **kwargs)
        self._metadata = ContigSetMetadata(self._metadata)
        self._updateMetadata()

    def consolidate(self, outfn=None):
        """Consolidation should be implemented for window text in names and
        for filters in ContigSets"""

        # In general "name" here refers to the contig.id only, which is why we
        # also have to keep track of comments.
        log.debug("Beginning consolidation")
        # Get the possible keys
        names = self.contigNames
        winless_names = [self._removeWindow(name) for name in names]

        # Put them into buckets
        matches = {}
        for con in self.contigs:
            conId = con.id
            window = self._parseWindow(conId)
            if not window is None:
                conId = self._removeWindow(conId)
            if conId not in matches:
                matches[conId] = [con]
            else:
                matches[conId].append(con)
        for name, match_list in matches.items():
            matches[name] = np.array(match_list)

        writeTemp = False
        # consolidate multiple files into one
        if len(self.toExternalFiles()) > 1:
            writeTemp = True
        writeMatches = {}
        writeComments = {}
        for name, match_list in matches.items():
            if len(match_list) > 1:
                log.debug("Multiple matches found for {i}".format(i=name))
                # look for the quiver window indication scheme from quiver:
                windows = np.array([self._parseWindow(match.id)
                                    for match in match_list])
                for win in windows:
                    if win is None:
                        log.debug("Windows not found for all items with a "
                                  "matching id, consolidation aborted")
                        return
                # order windows
                order = np.argsort([window[0] for window in windows])
                match_list = match_list[order]
                windows = windows[order]
                # TODO: check to make sure windows/lengths are compatible,
                # complete

                # collapse matches
                new_name = self._removeWindow(name)
                new_seq = ''.join([match.sequence for match in match_list])

                # set to write
                writeTemp = True
                writeMatches[new_name] = new_seq
                writeComments[new_name] = match_list[0].comment
            else:
                log.debug("One match found for {i}".format(i=name))
                writeMatches[name] = match_list[0].sequence
                writeComments[name] = match_list[0].comment
        if writeTemp:
            log.debug("Writing a new file is necessary")
            if not outfn:
                log.debug("Writing to a temp directory as no path given")
                outdir = tempfile.mkdtemp(suffix="consolidated-contigset")
                outfn = os.path.join(outdir,
                                     'consolidated.contigset.xml')
            with FastaWriter(outfn) as outfile:
                log.debug("Writing new resource {o}".format(o=outfn))
                for name, seq in writeMatches.items():
                    if writeComments[name]:
                        name = ' '.join([name, writeComments[name]])
                    outfile.writeRecord(name, seq)
            # replace resources
            log.debug("Replacing resources")
            self.externalResources = ExternalResources()
            self.addExternalResources([outfn])
            # replace contig info
            log.debug("Replacing metadata")
            self._metadata.contigs = []
            self._populateContigMetadata()

    def _popSuffix(self, name):
        observedSuffixes = ['|quiver']
        for suff in observedSuffixes:
            if name.endswith(suff):
                log.debug("Suffix found: {s}".format(s=suff))
                return name.replace(suff, ''), suff
        return name, ''

    def _removeWindow(self, name):
        if isinstance(self._parseWindow(name), np.ndarray):
            name, suff = self._popSuffix(name)
            return '_'.join(name.split('_')[:-2]) + suff
        return name

    def _parseWindow(self, name):
        name, _ = self._popSuffix(name)
        possibilities = name.split('_')[-2:]
        for pos in possibilities:
            if not pos.isdigit():
                return None
        return np.array(map(int, possibilities))

    def _updateMetadata(self):
        # update contig specific metadata:
        if not self._metadata.organism:
            self._metadata.organism = ''
        if not self._metadata.ploidy:
            self._metadata.ploidy = ''
        if not self._metadata.contigs:
            self._metadata.contigs = []
            self._populateContigMetadata()

    def _populateContigMetadata(self):
        for contig in self.contigs:
            self._metadata.addContig(contig)

    def updateCounts(self):
        if self._skipCounts:
            self.metadata.totalLength = -1
            self.metadata.numRecords = -1
            return
        try:
            log.debug('Updating counts')
            self.metadata.totalLength = 0
            self.metadata.numRecords = 0
            for res in self.resourceReaders():
                self.metadata.numRecords += len(res)
                for index in res.fai:
                    self.metadata.totalLength += index.length
        except Exception:
            if not self._strict:
                self.metadata.totalLength = -1
                self.metadata.numRecords = -1
            else:
                raise

    def addMetadata(self, newMetadata, **kwargs):
        """Add metadata specific to this subtype, while leaning on the
        superclass method for generic metadata. Also enforce metadata type
        correctness."""
        # Validate, clean and prep input data
        if newMetadata:
            if isinstance(newMetadata, dict):
                newMetadata = ContigSetMetadata(newMetadata)
            elif isinstance(newMetadata, ContigSetMetadata) or (
                    type(newMetadata).__name__ == 'DataSetMetadata'):
                newMetadata = ContigSetMetadata(newMetadata.record)
            else:
                raise TypeError("Cannot extend ContigSetMetadata with "
                                "{t}".format(t=type(newMetadata).__name__))

        # Pull generic values, kwargs, general treatment in super
        super(ContigSet, self).addMetadata(newMetadata, **kwargs)

        # Pull subtype specific values where important
        if newMetadata:
            if newMetadata.contigs:
                self._metadata.contigs.extend(newMetadata.contigs)

    def _openFiles(self):
        """Open the files (assert they exist, assert they are of the proper
        type before accessing any file)
        """
        if self._openReaders:
            log.debug("Closing old readers...")
            self.close()
        log.debug("Opening resources")
        for extRes in self.externalResources:
            location = urlparse(extRes.resourceId).path
            try:
                resource = IndexedFastaReader(location)
            except IOError:
                if not self._strict:
                    log.debug('Companion reference index (.fai) missing. '
                              'Use "samtools faidx <refname>" to generate '
                              'one.')
                    resource = FastaReader(location)
                else:
                    raise
            self._openReaders.append(resource)
        log.debug("Done opening resources")

    def resourceReaders(self, refName=None):
        """A generator of fastaReader objects for the ExternalResources in this
        ReferenceSet.

        Yields:
            An open fasta file
        Doctest:
            >>> # Either way:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet
            >>> ds = DataSet(data.getBam())
            >>> for seqFile in ds.resourceReaders():
            ...     for row in seqFile:
            ...         print 'hn: %i' % row.holeNumber # doctest:+ELLIPSIS
            hn: ...
        """
        if refName:
            log.error("Specifying a contig name not yet implemented")
        self._openFiles()
        return self._openReaders

    @property
    @filtered
    def contigs(self):
        """A generator of contigs from the fastaReader objects for the
        ExternalResources in this ReferenceSet.

        Yields:
            A fasta file entry

        Doctest:
            >>> # Either way:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet
            >>> ds = DataSet(data.getBam())
            >>> for seqFile in ds.resourceReaders():
            ...     for row in seqFile:
            ...         print 'hn: %i' % row.holeNumber # doctest:+ELLIPSIS
            hn: ...
        """
        for resource in self.resourceReaders():
            for contig in resource:
                yield contig

    def get_contig(self, contig_id):
        """Get a contig by ID"""
        # TODO: have this use getitem for indexed fasta readers:
        for contig in self.contigs:
            if contig.id == contig_id or contig.name == contig_id:
                return contig

    def assertIndexed(self):
        self._strict = True
        self._openFiles()
        return True

    @property
    def isIndexed(self):
        try:
            res = self._pollResources(
                lambda x: isinstance(x, IndexedFastaReader))
            return self._unifyResponses(res)
        except ResourceMismatchError:
            if not self._strict:
                log.error("Not all resource are equally indexed.")
                return False
            else:
                raise

    @property
    def contigNames(self):
        """The names assigned to the External Resources, or contigs if no name
        assigned."""
        names = []
        for contig in self.contigs:
            if (self.noFiltering
                    or self._filters.testParam('id', contig.id, str)):
                names.append(contig.id)
        return sorted(list(set(names)))

    @staticmethod
    def _metaTypeMapping():
        return {'fasta':'PacBio.ContigFile.ContigFastaFile',
                'fai':'PacBio.Index.SamIndex',
                'sa':'PacBio.Index.SaWriterIndex',
               }


class ReferenceSet(ContigSet):
    """DataSet type specific to References"""

    datasetType = DataSetMetaTypes.REFERENCE

    def __init__(self, *files, **kwargs):
        log.debug("Opening ReferenceSet")
        super(ReferenceSet, self).__init__(*files, **kwargs)

    def processFilters(self):
        # Allows us to not process all of the filters each time. This is marked
        # as dirty (= []) by addFilters etc. Filtration can be turned off by
        # setting this to [lambda x: True], which can be reversed by marking
        # the cache dirty. See disableFilters/enableFilters
        if self._cachedFilters:
            return self._cachedFilters
        filters = self.filters.tests(readType="fasta")
        # Having no filters means no opportunity to pass. Fix by filling with
        # always-true (e.g. disableFilters())
        if not filters:
            self._cachedFilters = [lambda x: True]
            return self._cachedFilters
        self._cachedFilters = filters
        return filters

    @property
    def refNames(self):
        """The reference names assigned to the External Resources, or contigs
        if no name assigned."""
        return self.contigNames


    @staticmethod
    def _metaTypeMapping():
        return {'fasta':'PacBio.ReferenceFile.ReferenceFastaFile',
                'fai':'PacBio.Index.SamIndex',
                'sa':'PacBio.Index.SaWriterIndex',
               }


class BarcodeSet(DataSet):
    """DataSet type specific to Barcodes"""

    datasetType = DataSetMetaTypes.BARCODE

    def __init__(self, *files, **kwargs):
        log.debug("Opening BarcodeSet")
        super(BarcodeSet, self).__init__(*files, **kwargs)
        self._metadata = BarcodeSetMetadata(self._metadata)

    def addMetadata(self, newMetadata, **kwargs):
        """Add metadata specific to this subtype, while leaning on the
        superclass method for generic metadata. Also enforce metadata type
        correctness."""
        # Validate, clean and prep input data
        if newMetadata:
            if isinstance(newMetadata, dict):
                newMetadata = BarcodeSetMetadata(newMetadata)
            elif isinstance(newMetadata, BarcodeSetMetadata) or (
                    type(newMetadata).__name__ == 'DataSetMetadata'):
                newMetadata = BarcodeSetMetadata(newMetadata.record)
            else:
                raise TypeError("Cannot extend BarcodeSetMetadata with "
                                "{t}".format(t=type(newMetadata).__name__))

        # Pull generic values, kwargs, general treatment in super
        super(BarcodeSet, self).addMetadata(newMetadata, **kwargs)

        # Pull subtype specific values where important
        # -> No type specific merging necessary, for now
