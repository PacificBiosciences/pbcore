"""
Classes representing the elements of the DataSet type

These classes are often instantiated by the parser and passed to the DataSet,
where they are stored, manipulated, filtered, merged, etc.
"""

import hashlib
import copy
import os
import logging
from functools import wraps
from functools import partial
from urlparse import urlparse
from pbcore.io.opener import (openAlignmentFile, openIndexedAlignmentFile,
                              FastaReader, IndexedFastaReader, CmpH5Reader,
                              IndexedBamReader)

from pbcore.io.dataset import DataSetReader
from pbcore.io.dataset.DataSetWriter import toXml
from pbcore.io.dataset.DataSetValidator import validateString
from pbcore.io.dataset.DataSetMembers import (DataSetMetadata,
                                              SubreadSetMetadata,
                                              ReferenceSetMetadata,
                                              ContigSetMetadata,
                                              BarcodeSetMetadata,
                                              ExternalResources, Filters)

log = logging.getLogger(__name__)

def filtered(generator):
    @wraps(generator)
    def wrapper(dset, *args, **kwargs):
        filter_tests = dset.processFilters()
        for read in generator(dset, *args, **kwargs):
            if (dset.noFiltering or
                    any([filt(read) for filt in filter_tests])):
                yield read
    return wrapper


def _toDsId(x):
    return "PacBio.DataSet.{x}".format(x=x)


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


class MetaDataSet(type):
    """This metaclass acts as a factory for DataSet and subtypes,
    intercepting constructor calls and returning a DataSet or subclass
    instance as appropriate (inferred from file contents)."""


    def __call__(cls, *files):
        """Factory function for DataSet and subtypes

        Args:
            files: one or more files to parse

        Returns:
            A dataset (or subtype) object.
        """
        if files:
            # The factory that does the heavy lifting:
            dataset = DataSetReader.parseFiles(files)
            # give the user what they call for, usually
            if cls != DataSet and type(dataset) == DataSet:
                dataset = dataset.copy(asType=cls.__name__)
        else:
            dataset = object.__new__(cls)
            dataset.__init__()
        if not dataset.uuid:
            dataset.newUuid()
        return dataset


class DataSet(object):
    """The record containing the DataSet information, with possible type
    specific subclasses"""

    __metaclass__ = MetaDataSet
    datasetType = DataSetMetaTypes.ALL

    def __init__(self, *files):
        """DataSet constructor

        Initialize representations of the ExternalResources, MetaData,
        Filters, and LabeledSubsets, parse inputs if possible

        Args:
            (HANDLED BY METACLASS __call__) *files: one or more filenames or
                                                    uris to read

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
            >>> ds1 = DataSet(data.getXml(no=0), data.getXml(no=1),
            ...               data.getBam())
            >>> ds1.numExternalResources
            5
            >>> ds1 = DataSet(data.getFofn())
            >>> ds1.numExternalResources
            5
            >>> # DataSet types are autodetected:
            >>> DataSet(data.getSubreadSet()) # doctest:+ELLIPSIS
            <SubreadSet...
            >>> # But can also be used directly
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
        self.fileNames = []

        # State tracking:
        self._cachedFilters = []
        self.noFiltering = False
        self._openReaders = []

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
            >>> from pbcore.io import DataSet
            >>> from pbcore.io.dataset.DataSetWriter import toXml
            >>> import timeit
            >>> print "Secs per: %f" % (timeit.timeit("ds3 = ds1 + ds2",
            ...               setup=("from pbcore.io import DataSet;"
            ...                      "import pbcore.data.datasets as data; "
            ...                      "ds1 = DataSet(data.getXml(no=8)); "
            ...                      "ds2 = DataSet(data.getXml(no=9))"),
            ...               number=100)/100.0) # doctest:+ELLIPSIS
            Secs per: ...
            >>> # xmls with different resourceIds: success
            >>> ds1 = DataSet(data.getXml(no=8))
            >>> ds2 = DataSet(data.getXml(no=9))
            >>> ds3 = ds1 + ds2
            >>> expected = ds1.numExternalResources + ds2.numExternalResources
            >>> ds3.numExternalResources == expected
            True
            >>> # xmls with different resourceIds but conflicting filters:
            >>> # failure to merge
            >>> ds2 = DataSet(data.getXml(no=10))
            >>> ds3 = ds1 + ds2
            >>> ds3
            >>> # xmls with same resourceIds: ignores new inputs
            >>> ds1 = DataSet(data.getXml(no=8))
            >>> ds2 = DataSet(data.getXml(no=8))
            >>> ds3 = ds1 + ds2
            >>> expected = ds1.numExternalResources
            >>> ds3.numExternalResources == expected
            True
        """
        if (otherDataset.__class__.__name__ == self.__class__.__name__ or
                otherDataset.__class__.__name__ == 'DataSet'):
            if not self.filters.testCompatibility(otherDataset.filters):
                log.warning("Filter incompatibility has blocked the addition "
                            "of two datasets")
                return None
            self._cachedFilters = []
            self._checkObjMetadata(otherDataset.objMetadata)
            result = self.copy()
            result.addMetadata(otherDataset.metadata)
            result.addExternalResources(otherDataset.externalResources)
            # DataSets may only be merged if they have identical filters,
            # So there is nothing new to add.
            result.addDatasets(otherDataset.copy())
            # If this dataset has no subsets representing it, add self as a
            # subdataset to the result
            if not self.subdatasets:
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
                log.info("Reader not opened properly, therefore not closed "
                         "properly.")
        self._openReaders = []

    def __exit__(self, *exec_info):
        self.close()

    def __len__(self):
        count = 0
        if self.filters:
            for _ in self.records:
                count += 1
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
            >>> import timeit
            >>> print "Secs per: %f" % (timeit.timeit("_ = ds1.newUuid()",
            ...               setup=("from pbcore.io import DataSet;"
            ...                      "import pbcore.data.datasets as data; "
            ...                      "ds1 = DataSet(data.getXml(no=8))"),
            ...               number=100)/100.0) # doctest:+ELLIPSIS
            Secs per: ...
            >>> from pbcore.io import DataSet
            >>> ds = DataSet()
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

        Returns:
            A DataSet object that is identical but for UniqueId

        Doctest:
            >>> import timeit
            >>> print "Secs per: %f" % (timeit.timeit("_ = ds1.copy()",
            ...               setup=("from pbcore.io import DataSet;"
            ...                      "import pbcore.data.datasets as data; "
            ...                      "ds1 = DataSet(data.getXml(no=8))"),
            ...               number=100)/100.0) # doctest:+ELLIPSIS
            Secs per: ...
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
            >>> ds1 = DataSet(data.getXml(no=8))
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
                tbr = self._castableTypes[asType]()
            except KeyError:
                raise TypeError("Cannot cast from {s} to "
                                "{t}".format(s=type(self).__name__, t=asType))
            tbr.__dict__.update(copy.deepcopy(self.__dict__))
            # update the metatypes: (TODO: abstract out 'iterate over all
            # resources and modify the element that contains them')
            tbr.makePathsAbsolute()
            return tbr
        result = copy.deepcopy(self)
        result.newUuid()
        return result

    def split(self, chunks=0, ignoreSubDatasets=False, contigs=False):
        """Deep copy the DataSet into a number of new DataSets containing
        roughly equal chunks of the ExternalResources or subdatasets.

        Args:
            chunks: the number of chunks to split the DataSet. When chunks=0,
                    create one DataSet per subdataset, or failing that
                    ExternalResource
            ignoreSubDatasets: F/T (False) do not split on datasets, only split
                               on ExternalResources
        Returns:
            A list of new DataSet objects (all other information deep
            copied).

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet
            >>> import timeit
            >>> print "Secs per: %f" % (timeit.timeit("dss = ds1.split()",
            ...               setup=("from pbcore.io import DataSet;"
            ...                      "import pbcore.data.datasets as data; "
            ...                      "ds1 = DataSet(data.getXml(no=8)); "),
            ...               number=100)/100.0) # doctest:+ELLIPSIS
            Secs per: ...
            >>> # splitting is pretty intuitive:
            >>> ds1 = DataSet(data.getXml())
            >>> # but divides up extRes's, so have more than one:
            >>> ds1.numExternalResources > 1
            True
            >>> # the default is one DataSet per ExtRes:
            >>> dss = ds1.split()
            >>> len(dss) == ds1.numExternalResources
            True
            >>> # but you can specify a number of DataSets to produce:
            >>> dss = ds1.split(chunks=1)
            >>> len(dss) == 1
            True
            >>> dss = ds1.split(chunks=2)
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
            >>> ds1 = DataSet(data.getXml(8))
            >>> ds1.totalLength
            500000
            >>> ds1tl = ds1.totalLength
            >>> ds2 = DataSet(data.getXml(9))
            >>> ds2.totalLength
            500000
            >>> ds2tl = ds2.totalLength
            >>> # merge:
            >>> dss = ds1 + ds2
            >>> dss.totalLength == (ds1tl + ds2tl)
            True
            >>> # unmerge:
            >>> ds1, ds2 = dss.split(2)
            >>> ds1.totalLength == ds1tl
            True
            >>> ds2.totalLength == ds2tl
            True
        """
        if contigs:
            return self._split_contigs(chunks)

        # Lets only split on datasets if actual splitting will occur,
        # And if all subdatasets have the required balancing key (totalLength)
        if (len(self.subdatasets) > 1
                and not ignoreSubDatasets):
            return self._split_subdatasets(chunks)

        atoms = self.externalResources
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

    def _split_contigs(self, chunks):
        # removed the non-trivial case so that it is still filtered to just
        # contigs with associated records

        # The format is rID, start, end, for a reference window
        refNames = self.refNames
        log.debug("{i} references found".format(i=len(refNames)))
        log.debug("Finding contigs")
        if len(refNames) < 100:
            atoms = [(rn, None, None) for rn in refNames if
                     next(self.readsInReference(rn), None)]
        else:
            log.debug("Skipping records for each reference check")
            atoms = [(rn, None, None) for rn in self.refNames]

        # The window length is used for balancing
        # TODO switch it to countRecords
        balanceKey = lambda x: x[2] - x[1]
        if not chunks:
            chunks = len(atoms)
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
        log.debug("Distributing chunkg")
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

    def write(self, outFile, validate=True, relPaths=False):
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
            >>> # The original file (and the copy) should have no
            >>> # DataSetMetadata
            >>> assert not ds1.metadata
            >>> assert not ds2.metadata
            >>> ds1 == ds2
            True
        """
        # prep for writing, fill some fields that aren't filled elsewhere:
        self.objMetadata.setdefault(
            "MetaType", "PacBio.DataSet." + self.__class__.__name__)
        self.objMetadata.setdefault("Name", "")
        self.objMetadata.setdefault("Tags", "")
        # fix paths if validate:
        if validate:
            if relPaths:
                self.makePathsRelative(os.path.dirname(outFile))
            else:
                self.makePathsAbsolute()
        xml = toXml(self)
        if validate:
            validateString(xml, relTo=outFile)
        fileName = urlparse(outFile).path.strip()
        with open(fileName, 'w') as outFile:
            outFile.writelines(xml)

    def loadStats(self, filename):
        """Load pipeline statistics from a <moviename>.sts.xml file. The subset
        of these data that are defined in the DataSet XSD become available
        through via DataSet.metadata.summaryStats.<...> and will be written out
        to the DataSet XML format according to the DataSet XML XSD.

        Args:
            filename: the filename of a <moviename>.sts.xml file

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet
            >>> ds1 = DataSet(data.getXml(8))
            >>> ds1.loadStats(data.getStats())
            >>> ds2 = DataSet(data.getXml(9))
            >>> ds2.loadStats(data.getStats())
            >>> ds3 = ds1 + ds2
            >>> ds1.metadata.summaryStats.prodDist.bins
            [1576, 901, 399, 0]
            >>> ds2.metadata.summaryStats.prodDist.bins
            [1576, 901, 399, 0]
            >>> ds3.metadata.summaryStats.prodDist.bins
            [3152, 1802, 798, 0]
        """
        statsMetadata = DataSetReader.parseStats(filename)
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

    def _resolveLocation(self, fname, possibleRelStart):
        if os.path.exists(fname):
            return os.path.abspath(fname)
        if os.path.exists(possibleRelStart):
            if os.path.exists(os.path.join(possibleRelStart, fname)):
                return os.path.abspath(os.path.join(possibleRelStart, fname))
        log.error("Including unresolved file: {f}".format(f=fname))
        return fname

    def makePathsAbsolute(self, curStart="."):
        """As part of the validation process, make all ResourceIds absolute
        URIs rather than relative paths. Generally not called by API users.

        Args:
            curStart: The location from which relative paths should emanate.
        """
        self._changePaths(
            lambda x, s=curStart: self._resolveLocation(x, s))

    def makePathsRelative(self, outDir=False):
        """Make things easier for writing test cases: make all
        ResourceIds relative paths rather than absolute paths.
        A less common use case for API consumers."""
        if outDir:
            self._changePaths(lambda x, s=outDir: os.path.relpath(x, s))
        else:
            self._changePaths(os.path.relpath)

    def _changePaths(self, osPathFunc, checkMetaType=True):
        """Change all resourceId paths in this DataSet according to the
        osPathFunc provided.

        Args:
            osPathFunc: A function for modifying paths (e.g. os.path.abspath)
        """
        # check all ExternalResources
        stack = list(self.externalResources)
        while stack:
            item = stack.pop()
            resId = item.resourceId
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

    def _updateMetaType(self, resource):
        file_type = self._fileType(resource.resourceId)
        resource.metaType = self._metaTypeMapping().get(file_type, "")

    def _metaTypeMapping(self):
        # no metatypes for generic DataSet
        return {}

    def _fileType(self, fname):
        ftype = fname.split('.')[-1]
        if ftype == 'h5':
            ftype = fname.split('.')[-2]
        return ftype

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

        TODO: How should this update conflicting filters?

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
            >>> ds2 = DataSet(data.getXml(8))
            >>> print ds2.filters
            ( rq > 0.75 ) OR ( qname == 100/0/0_100 )
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
        if newMetadata.get('Version') > self.objMetadata.get('Version'):
            raise ValueError("Wrong dataset version for merging {v1} vs "
                             "{v2}".format(v1=newMetadata.get('Version'),
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
            >>> import timeit
            >>> print "Secs per: %f" % (timeit.timeit(
            ...     "ds1 = DataSet(data.getXml(no=8))",
            ...     setup=("from pbcore.io import DataSet;"
            ...            "import pbcore.data.datasets as data"),
            ...     number=100)/100.0) # doctest:+ELLIPSIS
            Secs per: ...
            >>> print "Secs per: %f" % (timeit.timeit(
            ...     "ds1.addMetadata(None, ReadLength='Looong')",
            ...     setup=("from pbcore.io import DataSet;"
            ...            "import pbcore.data.datasets as data; "
            ...            "ds1 = DataSet(data.getXml(no=8)); "),
            ...     number=100)/100.0) # doctest:+ELLIPSIS
            Secs per: ...
            >>> from pbcore.io import DataSet
            >>> ds = DataSet()
            >>> # it is possible to add new metadata:
            >>> ds.addMetadata(None, Name='LongReadsRock')
            >>> print ds._metadata.getV(container='attrib', tag='Name')
            LongReadsRock
            >>> # but most will be loaded and modified:
            >>> import pbcore.data.datasets as data
            >>> ds2 = DataSet(data.getXml(no=8))
            >>> ds2._metadata.totalLength
            500000
            >>> ds2._metadata.totalLength = 100000
            >>> ds2._metadata.totalLength
            100000
            >>> ds2._metadata.totalLength += 100000
            >>> ds2._metadata.totalLength
            200000
            >>> ds3 = DataSet(data.getXml(no=8))
            >>> ds3.loadStats(data.getStats())
            >>> ds4 = DataSet(data.getXml(no=9))
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

    def addExternalResources(self, newExtResources):
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
            >>> ds.addExternalResources([er1])
            >>> len(ds.externalResources)
            1
            >>> # different resourceId: succeeds
            >>> ds.addExternalResources([er2])
            >>> len(ds.externalResources)
            2
            >>> # same resourceId: fails
            >>> ds.addExternalResources([er3])
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
            # merge duplicates instead of adding them
            if newExtRes.resourceId in resourceIds:
                first = resourceIds.index(newExtRes.resourceId)
                self.externalResources[first].merge(newExtRes)

            # add non-duplicates, update the list of current resourceIds
            else:
                self.externalResources.append(newExtRes)
                resourceIds.append(newExtRes.resourceId)

    def addDatasets(self, otherDataSet):
        """Add 'subsets' to a DataSet object using other DataSets (some fields
        may be missing).

        The following method of enabling merge-based split prevents nesting of
        datasets more than one deep. Most often used by the __add__ method,
        rather than directly.
        """
        if otherDataSet.subdatasets:
            self.subdatasets.extend(otherDataSet.subdatasets)
        else:
            self.subdatasets.append(otherDataSet)

    def _openFiles(self, refFile=None):
        """Open the files (assert they exist, assert they are of the proper
        type before accessing any file)
        """
        log.debug("Opening resources")
        for extRes in self.externalResources:
            location = urlparse(extRes.resourceId).path
            try:
                resource = openIndexedAlignmentFile(
                    location,
                    referenceFastaFname=refFile)
            except (IOError, ValueError):
                log.info("pbi file missing, operating with "
                         "reduced speed and functionality")
                resource = openAlignmentFile(location,
                                             referenceFastaFname=refFile)
            self._openReaders.append(resource)
        log.debug("Done opening resources")


    def resourceReaders(self, refName=False):
        """A generator of Indexed*Reader objects for the ExternalResources
        in this DataSet.

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
        if not self._openReaders:
            self._openFiles()
        if refName:
            return [resource for resource in self._openReaders
                    if refName in resource.referenceInfoTable['FullName'] or
                    refName in resource.referenceInfoTable['ID']]
        else:
            return self._openReaders

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
        nameIDs = self.refInfo('ID')
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
        return [name for name, _ in self.refInfo('Name')]

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
        return [name for name, _ in self.refInfo('FullName')]

    def refInfo(self, key):
        """The reference names present in the referenceInfoTable of the
        ExtResources.

        Args:
            key: a key for the referenceInfoTable of each resource
        Returns:
            A dictionary of refrence name: key_result pairs"""
        # sample
        names = []
        infos = []
        for resource in self.resourceReaders():
            names.extend(resource.referenceInfoTable['FullName'])
            infos.extend(resource.referenceInfoTable[key])
        # remove dupes
        sampled = zip(names, infos)
        sampled = list(set(sampled))
        # filter
        if not self.noFiltering:
            sampled = [(name, info) for name, info in sampled
                       if self._filters.testParam('rname', name)]
        return sampled

    @filtered
    def readsInReference(self, refName, justIndices=False):
        """A generator of (usually) BamAlignment objects for the
        reads in one or more Bam files pointed to by the ExternalResources in
        this DataSet that are mapped to the specified reference genome.

        Args:
            refName: the name of the reference that we are sampling

        Yields:
            BamAlignment objects

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet
            >>> ds = DataSet(data.getBam())
            >>> for read in ds.readsInReference(ds.refNames[0]):
            ...     print 'hn: %i' % read.holeNumber # doctest:+ELLIPSIS
            hn: ...
        """

        # I would love to use readsInRange(refName, None, None), but
        # IndexedBamReader breaks this (works for regular BamReader).

        # So I have to do a little hacking...
        refLen = 0
        for resource in self.resourceReaders():
            if (refName in resource.referenceInfoTable['Name'] or
                    refName in resource.referenceInfoTable['ID'] or
                    refName in resource.referenceInfoTable['FullName']):
                refLen = resource.referenceInfo(refName).Length
        if refLen:
            # TODO if the bam file is indexed readsInRange returns a list.
            # Calling this on the alignment results in every read in a list all
            # at once. We can block it into smaller calls...
            for read in self.readsInRange(refName, 0, refLen, justIndices):
                yield read

    @filtered
    def readsInRange(self, refName, start, end, justIndices=False):
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
            >>> for read in ds.readsInRange(ds.refNames[0], 100, 150):
            ...     print 'hn: %i' % read.holeNumber # doctest:+ELLIPSIS
            hn: ...
        """
        # merge sort before yield
        if self.numExternalResources > 1:
            if justIndices:
                try:
                    read_its = [iter(rr.readsInRange(refName, start, end,
                                                     justIndices))
                                for rr in self.resourceReaders()]
                except Exception:
                    log.warn("This would be faster with a .pbi file")
                    read_its = [iter(rr.readsInRange(refName, start, end))
                                for rr in self.resourceReaders()]
            else:
                read_its = [iter(rr.readsInRange(refName, start, end))
                            for rr in self.resourceReaders()]
            # buffer one element from each generator
            currents = [next(its, None) for its in read_its]
            # remove empty iterators
            read_its = [it for it, cur in zip(read_its, currents) if cur]
            currents = [cur for cur in currents if cur]
            while len(read_its) != 0:
                # pick the first one to yield
                first_i, first = min(enumerate(currents),
                                     key=lambda x: x[1].tStart)
                # update the buffer
                try:
                    currents[first_i] = next(read_its[first_i])
                except StopIteration:
                    del read_its[first_i]
                    del currents[first_i]
                yield first
        else:
            # the above will work in either case, but this might be ever so
            # slightly faster
            for resource in self.resourceReaders():
                for read in resource.readsInRange(refName, start, end):
                    yield read

    def toFofn(self, outfn=None, uri=False, relative=False):
        """Return a list of resource filenames (and write to optional outfile)

        Args:
            outfn: (None) the file to which the resouce filenames are to be
                   written. If None, the only emission is a returned list of
                   file names.
            uri: T/F (False) write the resource filenames as URIs.

        Returns:
            A list of filenames or uris

        Writes:
            (Optional) A file containing a list of filenames or uris

        Doctest:
            >>> from pbcore.io import DataSet
            >>> DataSet("bam1.bam", "bam2.bam").toFofn(uri=False)
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
        files = self.externalResources.resourceIds
        tbr = []
        for fname in files:
            tbr.append(self._resolveLocation(fname, '.'))
        return tbr

    @property
    def _castableTypes(self):
        """The types to which this DataSet type may be cast. This is a property
        instead of a member variable as we can enforce casting limits here (and
        modify if needed by overriding them in subclasses).

        Returns:
            A dictionary of MetaType->Class mappings, e.g. 'DataSet': DataSet
        """
        if type(self).__name__ != 'DataSet':
            return {'DataSet': DataSet,
                    type(self).__name__: type(self)}
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
        self._cachedFilters = []
        return self._filters

    @filters.setter
    def filters(self, value):
        """Limit setting to ensure cache hygiene and filter compatibility"""
        self._cachedFilters = []
        self._filters = value

    @property
    def numRecords(self):
        """The number of records in this DataSet (from the metadata)"""
        return self._metadata.numRecords

    def countRecords(self, rname=None, window=None):
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
        return [func(resource) for resource in self.resourceReaders(refName)]

    def _unifyResponses(self, responses, keyFunc=lambda x: x):
        if len(responses) > 1:
            # Check the rest against the first:
            for res in responses[1:]:
                if keyFunc(responses[0]) != keyFunc(res):
                    raise ResourceMismatchError(responses)
        return responses[0]

    @property
    def isCmpH5(self):
        res = self._pollResources(lambda x: isinstance(x, CmpH5Reader))
        return self._unifyResponses(res)

    @property
    def hasPbi(self):
        res = self._pollResources(lambda x: isinstance(x, IndexedBamReader))
        return self._unifyResponses(res)

    def referenceInfo(self, refName):
        responses = self._pollResources(
            lambda x, rn=refName: x.referenceInfo(rn), refName)
        return self._unifyResponses(responses, keyFunc=lambda x: x.MD5)

    def hasPulseFeature(self, featureName):
        responses = self._pollResources(
            lambda x: x.hasPulseFeature(featureName))
        return self._unifyResponses(responses)

    def pulseFeaturesAvailable(self):
        responses = self._pollResources(lambda x: x.pulseFeaturesAvailable())
        return self._unifyResponses(responses)

    def __getattr__(self, key):
        identicalList = ['sequencingChemistry', 'isSorted', 'isEmpty',
                         'readType', 'tStart', 'tEnd']
        if key in identicalList:
            responses = self._pollResources(lambda x: getattr(x, key))
            return self._unifyResponses(responses)
        else:
            raise AttributeError("{c} has no attribute {a}".format(
                c=self.__class__.__name__, a=key))

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
            chunkSizes[0][0] += balanceKey(item)
        return chunks

class ResourceMismatchError(Exception):

    def __init__(self, responses):
        super(ResourceMismatchError, self).__init__()
        self.responses = responses

    def __str__(self):
        return "Resources responded differently: " + ', '.join(self.responses)

class ReadSet(DataSet):
    """Base type for read sets, should probably never be used as a concrete
    class"""

    def __init__(self, *files):
        super(ReadSet, self).__init__()
        self._metadata = SubreadSetMetadata()

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

class HdfSubreadSet(ReadSet):

    datasetType = DataSetMetaTypes.HDF_SUBREAD


class SubreadSet(ReadSet):
    """DataSet type specific to Subreads

    DocTest:

        >>> from pbcore.io import DataSet, SubreadSet
        >>> import pbcore.data.datasets as data
        >>> ds1 = DataSet(data.getXml(no=8))
        >>> ds2 = DataSet(data.getXml(no=9))
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

    def _metaTypeMapping(self):
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
        >>> from pbcore.io import DataSet, ConsensusReadSet
        >>> ds1 = DataSet(data.getXml(5))
        >>> ds1 # doctest:+ELLIPSIS
        <ConsensusReadSet...
        >>> ds1._metadata # doctest:+ELLIPSIS
        <SubreadSetMetadata...
        >>> ds2 = ConsensusReadSet(data.getXml(5))
        >>> ds2 # doctest:+ELLIPSIS
        <ConsensusReadSet...
        >>> ds2._metadata # doctest:+ELLIPSIS
        <SubreadSetMetadata...
    """

    datasetType = DataSetMetaTypes.CCS

class AlignmentSet(DataSet):
    """DataSet type specific to Alignments. No type specific Metadata exists,
    so the base class version is OK (this just ensures type representation on
    output and expandability"""

    datasetType = DataSetMetaTypes.ALIGNMENT

    def addReference(self, fname):
        reference = ReferenceSet(fname).externalResources.resourceIds
        if len(reference) > 1:
            log.warn("Multiple references found, cannot open with reads")
        else:
            self._openFiles(refFile=reference[0])

    @property
    def records(self):
        """ The records in this AlignmentSet, sorted by tStart. """
        # we only care about aligned sequences here, so we can make this a
        # chain of readsInReferences to add pre-filtering by rname, instead of
        # going through every record and performing downstream filtering.
        # This will make certain operations, like len(), potentially faster
        for rname in self.refNames:
            for read in self.readsInReference(rname):
                yield read

    def _metaTypeMapping(self):
        # This doesn't work for scraps.bam, whenever that is implemented
        return {'bam':'PacBio.SubreadFile.SubreadBamFile',
                'bai':'PacBio.Index.BamIndex',
                'pbi':'PacBio.Index.PacBioIndex',
               }


class ReferenceSet(DataSet):
    """DataSet type specific to References"""

    datasetType = DataSetMetaTypes.REFERENCE

    def __init__(self, *files):
        super(ReferenceSet, self).__init__()
        self._metadata = ReferenceSetMetadata()
        self._indexedOnly = False

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

    def addMetadata(self, newMetadata, **kwargs):
        """Add metadata specific to this subtype, while leaning on the
        superclass method for generic metadata. Also enforce metadata type
        correctness."""
        # Validate, clean and prep input data
        if newMetadata:
            if isinstance(newMetadata, dict):
                newMetadata = ReferenceSetMetadata(newMetadata)
            elif isinstance(newMetadata, ReferenceSetMetadata) or (
                    type(newMetadata).__name__ == 'DataSetMetadata'):
                newMetadata = ReferenceSetMetadata(newMetadata.record)
            else:
                raise TypeError("Cannot extend ReferenceSetMetadata with "
                                "{t}".format(t=type(newMetadata).__name__))

        # Pull generic values, kwargs, general treatment in super
        super(ReferenceSet, self).addMetadata(newMetadata, **kwargs)

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
                if not self._indexedOnly:
                    log.warn('Companion reference index (.fai) missing. '
                             'Use "samtools faidx <refname>" to generate one.')
                    resource = FastaReader(location)
                else:
                    raise
            self._openReaders.append(resource)
        log.debug("Done opening resources")

    def assertIndexed(self):
        self._indexedOnly = True
        self._openFiles()
        return True

    def resourceReaders(self):
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
        self._openFiles()
        for resource in self._openReaders:
            yield resource
        self.close()

    @property
    def refNames(self):
        """The reference names assigned to the External Resources, or contigs,
        if no name assigned."""
        refNames = []
        for contig in self.contigs:
            if (self.noFiltering
                    or self._filters.testParam('id', contig.id, str)):
                refNames.append(contig.id)
        return list(set(refNames))

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
        for contig in self.contigs:
            if contig.id == contig_id or contig.name == contig_id:
                return contig

    def _metaTypeMapping(self):
        return {'fasta':'PacBio.ReferenceFile.ReferenceFastaFile',
                'fai':'PacBio.Index.SamIndex',
                'sa':'PacBio.Index.SaWriterIndex',
               }


class ContigSet(DataSet):
    """DataSet type specific to Contigs"""

    datasetType = DataSetMetaTypes.CONTIG

    def __init__(self, *files):
        super(ContigSet, self).__init__()
        self._metadata = ContigSetMetadata()

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

class BarcodeSet(DataSet):
    """DataSet type specific to Barcodes"""

    datasetType = DataSetMetaTypes.BARCODE

    def __init__(self, *files):
        super(BarcodeSet, self).__init__()
        self._metadata = BarcodeSetMetadata()

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
