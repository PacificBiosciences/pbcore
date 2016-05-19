"""
Classes representing DataSets of various types.
"""

import hashlib
import datetime
import copy
import os, sys
import re
import errno
import uuid
import logging
import itertools
import xml.dom.minidom
import tempfile
import numpy as np
from urlparse import urlparse
from functools import wraps, partial
from collections import defaultdict, Counter
from pbcore.util.Process import backticks
from pbcore.chemistry.chemistry import ChemistryLookupError
from pbcore.io.align.PacBioBamIndex import PBI_FLAGS_BARCODE
from pbcore.io.FastaIO import splitFastaHeader, FastaWriter
from pbcore.io.FastqIO import FastqReader, FastqWriter, qvsFromAscii
from pbcore.io import (BaxH5Reader, FastaReader, IndexedFastaReader,
                       CmpH5Reader, IndexedBamReader, BamReader)
from pbcore.io.align._BamSupport import UnavailableFeature
from pbcore.io.dataset.DataSetReader import (parseStats, populateDataSet,
                                             resolveLocation, xmlRootType,
                                             wrapNewResource, openFofnFile,
                                             parseMetadata)
from pbcore.io.dataset.DataSetWriter import toXml
from pbcore.io.dataset.DataSetValidator import validateString
from pbcore.io.dataset.DataSetMembers import (DataSetMetadata,
                                              SubreadSetMetadata,
                                              ContigSetMetadata,
                                              BarcodeSetMetadata,
                                              ExternalResources,
                                              ExternalResource, Filters)
from pbcore.io.dataset.utils import (consolidateBams, _infixFname, _pbindexBam,
                                     _indexBam, _indexFasta, _fileCopy,
                                     _swapPath, which, consolidateXml)
from pbcore.io.dataset.DataSetErrors import (InvalidDataSetIOError,
                                             ResourceMismatchError)


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

def _getTimeStampedName(mType):
    """Generate a timestamped name using the given metatype 'mType' and the
    current UTC time"""
    mType = mType.lower()
    mType = '_'.join(mType.split('.'))
    time = datetime.datetime.utcnow().strftime("%y%m%d_%H%M%S%f")[:-3]
    return "{m}-{t}".format(m=mType, t=time)

def _toDsId(name):
    """Translate a class name into a MetaType/ID"""
    return "PacBio.DataSet.{x}".format(x=name)

def _dsIdToName(dsId):
    """Translate a MetaType/ID into a class name"""
    if DataSetMetaTypes.isValid(dsId):
        return dsId.split('.')[-1]
    else:
        raise InvalidDataSetIOError("Invalid DataSet MetaType")

def _dsIdToType(dsId):
    """Translate a MetaType/ID into a type"""
    if DataSetMetaTypes.isValid(dsId):
        types = DataSet.castableTypes()
        return types[_dsIdToName(dsId)]
    else:
        raise InvalidDataSetIOError("Invalid DataSet MetaType")

def _dsIdToSuffix(dsId):
    """Translate a MetaType/ID into a file suffix"""
    dsIds = DataSetMetaTypes.ALL
    suffixMap = {dsId: _dsIdToName(dsId) for dsId in dsIds}
    suffixMap[_toDsId("DataSet")] = 'DataSet'
    if DataSetMetaTypes.isValid(dsId):
        suffix = suffixMap[dsId]
        suffix = suffix.lower()
        suffix += '.xml'
        return suffix
    else:
        raise InvalidDataSetIOError("Invalid DataSet MetaType")

def _typeDataSet(dset):
    """Determine the type of a dataset from the xml file without opening it"""
    xml_rt = xmlRootType(dset)
    dsId = _toDsId(xml_rt)
    tbrType = _dsIdToType(dsId)
    return tbrType

def isDataSet(xmlfile):
    """Determine if a file is a DataSet before opening it"""
    try:
        _typeDataSet(xmlfile)
        return True
    except Exception:
        return False

def getDataSetUuid(xmlfile):
    """
    Quickly retrieve the uuid from the root element of a dataset XML file,
    using a streaming parser to avoid loading the entire dataset into memory.
    Returns None if the parsing fails.
    """
    try:
        import xml.etree.cElementTree as ET
        for event, element in ET.iterparse(xmlfile, events=("start",)):
            return element.get("UniqueId")
    except Exception:
        return None


def getDataSetMetaType(xmlfile):
    """
    Quickly retrieve the MetaType from the root element of a dataset XML file,
    using a streaming parser to avoid loading the entire dataset into memory.
    Returns None if the parsing fails.
    """
    try:
        import xml.etree.cElementTree as ET
        for event, element in ET.iterparse(xmlfile, events=("start",)):
            return element.get("MetaType")
    except Exception:
        return None


def openDataSet(*files, **kwargs):
    """Factory function for DataSet types as suggested by the first file"""
    tbrType = _typeDataSet(files[0])
    return tbrType(*files, **kwargs)

def openDataFile(*files, **kwargs):
    """Factory function for DataSet types determined by the first data file"""
    possibleTypes = [AlignmentSet, SubreadSet, ConsensusReadSet,
                     ConsensusAlignmentSet, ReferenceSet, HdfSubreadSet]
    origFiles = files
    fileMap = defaultdict(list)
    for dstype in possibleTypes:
        for ftype in dstype._metaTypeMapping():
            fileMap[ftype].append(dstype)
    ext = _fileType(files[0])
    if ext == 'fofn':
        files = openFofnFile(files[0])
        ext = _fileType(files[0])
    if ext == 'xml':
        dsType = _typeDataSet(files[0])
        return dsType(*origFiles, **kwargs)
    options = fileMap[ext]
    if len(options) == 1:
        return options[0](*origFiles, **kwargs)
    else:
        # peek in the files to figure out the best match
        if ReferenceSet in options:
            log.warn("Fasta files aren't unambiguously reference vs contig, "
                     "opening as ReferenceSet")
            return ReferenceSet(*origFiles, **kwargs)
        elif AlignmentSet in options:
            # it is a bam file
            if files[0].endswith('bam'):
                bam = BamReader(files[0])
            else:
                bam = CmpH5Reader(files[0])
            if bam.isMapped:
                if bam.readType == "CCS":
                    return ConsensusAlignmentSet(*origFiles, **kwargs)
                else:
                    return AlignmentSet(*origFiles, **kwargs)
            else:
                if bam.readType == "CCS":
                    return ConsensusReadSet(*origFiles, **kwargs)
                else:
                    return SubreadSet(*origFiles, **kwargs)

def _stackRecArrays(recArrays):
    """Stack recarrays into a single larger recarray"""
    tbr = np.concatenate(recArrays)
    tbr = tbr.view(np.recarray)
    return tbr

def _uniqueRecords(recArray):
    """Remove duplicate records"""
    unique = set()
    unique_i = []
    for i, rec in enumerate(recArray):
        rect = tuple(rec)
        if rect not in unique:
            unique.add(rect)
            unique_i.append(i)
    return recArray[unique_i]

def _fieldsView(recArray, fields):
    vdtype = np.dtype({fi:recArray.dtype.fields[fi] for fi in fields})
    return np.ndarray(recArray.shape, vdtype, recArray, 0, recArray.strides)

def _renameField(recArray, current, new):
    ind = recArray.dtype.names.index(current)
    names = list(recArray.dtype.names)
    names[ind] = new
    recArray.dtype.names = names

def _flatten(lol, times=1):
    """ This wont do well with mixed nesting"""
    for _ in range(times):
        lol = np.concatenate(lol)
    return lol

def _ranges_in_list(alist):
    """Takes a sorted list, finds the boundaries of runs of each value"""
    unique, indices, counts = np.unique(np.array(alist), return_index=True,
                                        return_counts=True)
    return {u: (i, i + c) for u, i, c in zip(unique, indices, counts)}

def divideKeys(keys, chunks):
    if chunks < 1:
        return []
    if chunks > len(keys):
        chunks = len(keys)
    chunksize = len(keys)/chunks
    key_chunks = [keys[(i * chunksize):((i + 1) * chunksize)] for i in
                  range(chunks-1)]
    key_chunks.append(keys[((chunks - 1) * chunksize):])
    return key_chunks

def splitKeys(keys, chunks):
    if chunks < 1:
        return []
    if chunks > len(keys):
        chunks = len(keys)
    chunksize = len(keys)/chunks
    key_chunks = [(keys[i * chunksize], keys[(i + 1) * chunksize - 1]) for i in
                  range(chunks-1)]
    key_chunks.append((keys[(chunks - 1) * chunksize], keys[-1]))
    return key_chunks

def keysToRanges(keys):
    key_ranges = [[min(k), max(k)] for k in keys]
    return key_ranges

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
    elif ftype == '.index':
        _, prefix = os.path.splitext(remainder)
        if prefix == '.contig':
            ftype = prefix + ftype
    ftype = ftype.strip('.')
    return ftype

def _fileExists(fname):
    """Assert that a file exists with a useful failure mode"""
    if not isinstance(fname, str):
        fname = fname.resourceId
    if not os.path.isfile(fname):
        raise InvalidDataSetIOError("Resource {f} not found".format(f=fname))
    return True

def checkAndResolve(fname, possibleRelStart=None):
    """Try and skip resolveLocation if possible"""
    tbr = fname
    if not fname.startswith(os.path.sep):
        log.debug('Unable to assume path is already absolute')
        tbr = resolveLocation(fname, possibleRelStart)
    return tbr

def _pathChanger(osPathFunc, metaTypeFunc, resource):
    """Apply these two functions to the resource or ResourceId"""
    resId = resource.resourceId
    currentPath = urlparse(resId)
    if currentPath.scheme == 'file' or not currentPath.scheme:
        currentPath = currentPath.path
        currentPath = osPathFunc(currentPath)
        resource.resourceId = currentPath
        metaTypeFunc(resource)

def _copier(dest, resource, subfolder=None):
    """Apply these two functions to the resource or ResourceId"""
    if subfolder is None:
        subfolder = [uuid.uuid4()]
    resId = resource.resourceId
    currentPath = urlparse(resId)
    if currentPath.scheme == 'file' or not currentPath.scheme:
        currentPath = currentPath.path
        try:
            currentPath = _fileCopy(dest, currentPath, uuid=resource.uniqueId)
            subfolder[0] = resource.uniqueId
        except AttributeError:
            if subfolder:
                currentPath = _fileCopy(dest, currentPath, uuid=subfolder[0])
            else:
                raise
        resource.resourceId = currentPath


class DataSet(object):
    """The record containing the DataSet information, with possible type
    specific subclasses"""

    datasetType = DataSetMetaTypes.ALL

    def __init__(self, *files, **kwargs):
        """DataSet constructor

        Initialize representations of the ExternalResources, MetaData,
        Filters, and LabeledSubsets, parse inputs if possible

        Args:
            :files: one or more filenames or uris to read
            :strict=False: strictly require all index files
            :skipCounts=False: skip updating counts for faster opening

        Doctest:
            >>> import os, tempfile
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import AlignmentSet, SubreadSet
            >>> # Prog like pbalign provides a .bam file:
            >>> # e.g. d = AlignmentSet("aligned.bam")
            >>> # Something like the test files we have:
            >>> inBam = data.getBam()
            >>> d = AlignmentSet(inBam)
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
            >>> d = AlignmentSet(outXml)
            >>> # The UniqueId will be the same
            >>> d.uuid == dOldUuid
            True
            >>> # Inputs can be many and varied
            >>> ds1 = AlignmentSet(data.getXml(8), data.getBam(1))
            >>> ds1.numExternalResources
            2
            >>> ds1 = AlignmentSet(data.getFofn())
            >>> ds1.numExternalResources
            2
            >>> # Constructors should be used directly
            >>> SubreadSet(data.getSubreadSet(),
            ...            skipMissing=True) # doctest:+ELLIPSIS
            <SubreadSet...
            >>> # Even with untyped inputs
            >>> AlignmentSet(data.getBam()) # doctest:+ELLIPSIS
            <AlignmentSet...
            >>> # AlignmentSets can also be manipulated after opening:
            >>> # Add external Resources:
            >>> ds = AlignmentSet()
            >>> _ = ds.externalResources.addResources(["IdontExist.bam"])
            >>> ds.externalResources[-1].resourceId == "IdontExist.bam"
            True
            >>> # Add an index file
            >>> pbiName = "IdontExist.bam.pbi"
            >>> ds.externalResources[-1].addIndices([pbiName])
            >>> ds.externalResources[-1].indices[0].resourceId == pbiName
            True

        """
        files = [str(fn) for fn in files]
        self._strict = kwargs.get('strict', False)
        skipMissing = kwargs.get('skipMissing', False)
        self._skipCounts = kwargs.get('skipCounts', False)
        _induceIndices = kwargs.get('generateIndices', False)

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
        populateDataSet(self, files)

        if not skipMissing:
            self._modResources(_fileExists)

        # DataSet base class shouldn't really be used. It is ok-ish for just
        # basic xml mainpulation. May start warning at some point, but
        # openDataSet uses it, which would warn unnecessarily.
        baseDataSet = False
        if isinstance(self.datasetType, tuple):
            baseDataSet = True

        if self._strict and baseDataSet:
            raise InvalidDataSetIOError("DataSet is an abstract class")

        # Populate required metadata
        if not self.uuid:
            self.newUuid()
        self.objMetadata.setdefault("Tags", "")
        if not baseDataSet:
            dsType = self.objMetadata.setdefault("MetaType", self.datasetType)
        else:
            dsType = self.objMetadata.setdefault("MetaType",
                                                 _toDsId('DataSet'))
        if not "TimeStampedName" in self.objMetadata:
            self.objMetadata["TimeStampedName"] = _getTimeStampedName(
                self.objMetadata["MetaType"])
        self.objMetadata.setdefault("Name",
                                    self.objMetadata["TimeStampedName"])

        # Don't allow for creating datasets from inappropriate sources
        # (XML files with mismatched types)
        if not baseDataSet:
            # use _castableDataSetTypes to contain good casts
            if dsType not in self._castableDataSetTypes:
                raise IOError(errno.EIO,
                              "Cannot create {c} from {f}".format(
                                  c=self.datasetType, f=dsType),
                              files[0])

        # Don't allow for creating datasets from inappropriate file types
        # (external resources of improper types)
        if not baseDataSet:
            for fname in self.toExternalFiles():
                # due to h5 file types, must be unpythonic:
                found = False
                for allowed in self._metaTypeMapping().keys():
                    if fname.endswith(allowed):
                        found = True
                        break
                if not found:
                    allowed = self._metaTypeMapping().keys()
                    extension = fname.split('.')[-1]
                    raise IOError(errno.EIO,
                                  "Cannot create {c} with resource of type "
                                  "'{t}' ({f}), only {a}".format(c=dsType,
                                                           t=extension,
                                                           f=fname,
                                                           a=allowed))

        # State tracking:
        self._cachedFilters = []
        self.noFiltering = False
        self._openReaders = []
        self._referenceInfoTable = None
        self._referenceDict = {}
        self._indexMap = None
        self._referenceInfoTableIsStacked = None
        self._readGroupTableIsRemapped = False
        self._index = None
        # only to be used against incorrect counts from the XML, not for
        # internal accounting:
        self._countsUpdated = False

        # update counts
        if files:
            if not self.totalLength or not self.numRecords:
                self.updateCounts()
            elif self.totalLength <= 0 or self.numRecords <= 0:
                self.updateCounts()
            elif len(files) > 1:
                self.updateCounts()

        # generate indices if requested and needed
        if _induceIndices:
            self.induceIndices()

    def induceIndices(self):
        """Generate indices for ExternalResources.

        Not compatible with DataSet base type"""
        raise NotImplementedError()

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
            :otherDataset: a DataSet to merge with self

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
        """Merge an 'other' dataset with this dataset, same as add operator,
        but can take argumens
        """
        if (other.__class__.__name__ == self.__class__.__name__ or
                other.__class__.__name__ == 'DataSet' or
                self.__class__.__name__ == 'DataSet'):
            # determine whether or not this is the merge that is populating a
            # dataset for the first time
            firstIn = True if len(self.externalResources) == 0 else False

            if copyOnMerge:
                result = self.copy()
            else:
                result = self

            # Block on filters?
            if (not firstIn and
                    not self.filters.testCompatibility(other.filters)):
                log.warning("Filter incompatibility has blocked the merging "
                            "of two datasets")
                return None
            elif firstIn:
                result.addFilters(other.filters, underConstruction=True)

            # reset the filters, just in case
            result._cachedFilters = []

            # block on object metadata?
            result._checkObjMetadata(other.objMetadata)

            # There is probably a cleaner way to do this:
            result.objMetadata.update(other.objMetadata)

            # If this dataset has no subsets representing it, add self as a
            # subdataset to the result
            # TODO: this is a stopgap to prevent spurious subdatasets when
            # creating datasets from dataset xml files...
            if not self.subdatasets and not firstIn:
                result.addDatasets(self.copy())

            # add subdatasets
            if other.subdatasets or not firstIn:
                result.addDatasets(other.copy())

            # add in the metadata (not to be confused with obj metadata)
            if firstIn:
                result.metadata = other.metadata
            else:
                result.addMetadata(other.metadata)

            # skip updating counts because other's metadata should be up to
            # date
            result.addExternalResources(other.externalResources,
                                        updateCount=False)

            # DataSets may only be merged if they have identical filters,
            # So there is nothing new to add.

            return result
        else:
            raise TypeError('DataSets can only be merged with records of the '
                            'same type or of type DataSet')


    def __deepcopy__(self, memo):
        """Deep copy this Dataset by recursively deep copying the members
        (objMetadata, DataSet metadata, externalResources, filters and
        subdatasets)
        """
        tbr = type(self)(skipCounts=True)
        memo[id(self)] = tbr
        tbr.objMetadata = copy.deepcopy(self.objMetadata, memo)
        tbr.metadata = copy.deepcopy(self._metadata, memo)
        tbr.externalResources = copy.deepcopy(self.externalResources, memo)
        tbr.filters = copy.deepcopy(self._filters, memo)
        tbr.subdatasets = copy.deepcopy(self.subdatasets, memo)
        tbr.fileNames = copy.deepcopy(self.fileNames, memo)
        tbr._skipCounts = False
        return tbr

    def __eq__(self, other):
        """Test for DataSet equality. The method specified in the documentation
        calls for md5 hashing the "Core XML" elements and comparing. This is
        the same procedure for generating the Uuid, so the same method may be
        used. However, as simultaneously or regularly updating the Uuid is not
        specified, we opt to not set the newUuid when checking for equality.

        Args:
            :other: The other DataSet to compare to this DataSet.

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
            del reader
        self._openReaders = []

    def __exit__(self, *exec_info):
        self.close()

    def __len__(self):
        """Return the number of records in this DataSet"""
        if self.numRecords <= 0:
            if self._filters:
                if isinstance(self.datasetType, tuple):
                    log.debug("Base class DataSet length cannot be calculated "
                              "when filters are present")
                else:
                    self.updateCounts()
            else:
                try:
                    # a little cheaper:
                    count = 0
                    for reader in self.resourceReaders():
                        count += len(reader)
                    self.numRecords = count
                except UnavailableFeature:
                    # UnavailableFeature: no .bai
                    self.updateCounts()
        elif not self._countsUpdated:
            # isn't that expensive, avoids crashes due to incorrect numRecords:
            self.updateCounts()
        return self.numRecords

    def newUuid(self, setter=True):
        """Generate and enforce the uniqueness of an ID for a new DataSet.
        While user setable fields are stripped out of the Core DataSet object
        used for comparison, the previous UniqueId is not. That means that
        copies will still be unique, despite having the same contents.

        Args:
            :setter=True: Setting to False allows MD5 hashes to be generated
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

    def copyTo(self, dest, relative=False):
        """Doesn't resolve resource name collisions"""
        ofn = None
        dest = os.path.abspath(dest)
        if not os.path.isdir(dest):
            ofn = dest
            dest = os.path.split(dest)[0]
        # unfortunately file indices must have the same name as the file they
        # index, so we carry around some state to store the most recent uuid
        # seen. Good thing we do a depth first traversal!
        state = [self.uuid]
        resFunc = partial(_copier, dest, subfolder=state)
        self._modResources(resFunc)
        if not ofn is None:
            self.write(ofn, relPaths=relative)

    def copy(self, asType=None):
        """Deep copy the representation of this DataSet

        Args:
            :asType: The type of DataSet to return, e.g. 'AlignmentSet'

        Returns:
            A DataSet object that is identical but for UniqueId

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet, SubreadSet
            >>> ds1 = DataSet(data.getXml(12))
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
            >>> ds1 = SubreadSet(data.getXml(no=10), strict=True)
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
            tbr.makePathsAbsolute()
            return tbr
        result = copy.deepcopy(self)
        result.newUuid()
        return result

    def split(self, chunks=0, ignoreSubDatasets=True, contigs=False,
              maxChunks=0, breakContigs=False, targetSize=5000, zmws=False,
              barcodes=False, byRecords=False, updateCounts=True):
        """Deep copy the DataSet into a number of new DataSets containing
        roughly equal chunks of the ExternalResources or subdatasets.

        Examples:

            - split into exactly n datasets where each addresses a different \
              piece of the collection of contigs::

                dset.split(contigs=True, chunks=n)

            - split into at most n datasets where each addresses a different \
              piece of the collection of contigs, but contigs are kept whole::

                dset.split(contigs=True, maxChunks=n)

            - split into at most n datasets where each addresses a different \
              piece of the collection of contigs and the number of chunks is \
              in part based on the number of reads::

                dset.split(contigs=True, maxChunks=n, breakContigs=True)

        Args:
            :chunks: the number of chunks to split the DataSet.
            :ignoreSubDatasets: (True) do not split on subdatasets
            :contigs: split on contigs instead of external resources etc
            :maxChunks: The upper limit on the number of chunks.
            :breakContigs: Whether or not to break contigs when using maxChunks
            :targetSize: The target number of reads per chunk
            :zmws: Split by zmws
            :barcodes: Split by barcodes
            :byRecords: Split contigs by mapped records, rather than ref length
            :updateCounts: Update the count metadata in each chunk

        Returns:
            A list of new DataSet objects (all other information deep copied).

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import AlignmentSet
            >>> # splitting is pretty intuitive:
            >>> ds1 = AlignmentSet(data.getXml(12))
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
            ... dss.split(2, ignoreSubDatasets=False),
            ... key=lambda x: x.totalLength, reverse=True)
            >>> ds1.totalLength == ds1tl
            True
            >>> ds2.totalLength == ds2tl
            True

        """
        # File must have pbi index to be splittable:
        if len(self) == 0:
            return [self.copy()]
        if contigs:
            return self._split_contigs(chunks, maxChunks, breakContigs,
                                       targetSize=targetSize,
                                       byRecords=byRecords,
                                       updateCounts=updateCounts)
        elif zmws:
            if chunks == 0:
                chunks = maxChunks
            return self._split_zmws(chunks, targetSize=targetSize)
        elif barcodes:
            return self._split_barcodes(chunks)

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

    def _split_contigs(self, chunks, maxChunks=0, breakContigs=False,
                       targetSize=5000, byRecords=False, updateCounts=False):
        raise TypeError("Only AlignmentSets may be split by contigs")

    def _split_barcodes(self, chunks):
        raise TypeError("Only ReadSets may be split by contigs")

    def _split_zmws(self, chunks, targetSize=None):
        raise TypeError("Only ReadSets may be split by ZMWs")

    def _split_atoms(self, atoms, num_chunks):
        """Divide up atomic units (e.g. contigs) into chunks (refId, size,
        segments)
        """
        for _ in range(num_chunks - len(atoms)):
            largest = max(atoms, key=lambda x: x[1]/x[2])
            largest[2] += 1
        return atoms

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

    def write(self, outFile, validate=True, modPaths=None,
              relPaths=None, pretty=True):
        """Write to disk as an XML file

        Args:
            :outFile: The filename of the xml file to be created
            :validate: T/F (True) validate the ExternalResource ResourceIds
            :relPaths: T/F (None/no change) make the ExternalResource
                       ResourceIds relative instead of absolute filenames
            :modPaths: DEPRECATED (T/F) allow paths to be modified

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import DataSet
            >>> import tempfile, os
            >>> outdir = tempfile.mkdtemp(suffix="dataset-doctest")
            >>> outfile = os.path.join(outdir, 'tempfile.xml')
            >>> ds1 = DataSet(data.getXml(), skipMissing=True)
            >>> ds1.write(outfile, validate=False)
            >>> ds2 = DataSet(outfile, skipMissing=True)
            >>> ds1 == ds2
            True
        """
        if not modPaths is None:
            log.info("modPaths as a write argument is deprecated. Paths "
                     "aren't modified unless relPaths is explicitly set "
                     "to True or False. Will be removed in future versions.")
            # make sure we keep the same effect for now, in case someone has
            # something odd like modPaths=False, relPaths=True
            if not modPaths:
                relPaths = None

        # fix paths if validate:
        if validate and not relPaths is None:
            if relPaths:
                self.makePathsRelative(os.path.dirname(outFile))
            else:
                self.makePathsAbsolute()
        xml_string = toXml(self)
        if pretty:
            xml_string = xml.dom.minidom.parseString(xml_string).toprettyxml(
                encoding="UTF-8")

        # not useful yet as a list, but nice to keep the options open:
        validation_errors = []
        if validate:
            try:
                validateString(xml_string, relTo=os.path.dirname(outFile))
            except Exception as e:
                validation_errors.append(e)
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

        for e in validation_errors:
            log.error("Invalid file produced: {f}".format(f=fileName))
            raise e

    def loadStats(self, filename):
        """Load pipeline statistics from a <moviename>.sts.xml file. The subset
        of these data that are defined in the DataSet XSD become available
        through via DataSet.metadata.summaryStats.<...> and will be written out
        to the DataSet XML format according to the DataSet XML XSD.

        Args:
            :filename: the filename of a <moviename>.sts.xml file

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
        if isinstance(filename, basestring):
            statsMetadata = parseStats(str(filename))
        else:
            statsMetadata = filename
        if self.metadata.summaryStats:
            newSub = self.copy()
            newSub.metadata.removeChildren('SummaryStats')
            newSub.loadStats(statsMetadata)
            self.addDatasets(self.copy())
            self.addDatasets(newSub)
            self.metadata.summaryStats.merge(statsMetadata)
        else:
            self.metadata.append(statsMetadata)

    def readsByName(self, query):
        reads = _flatten([rr.readsByName(query)
                          for rr in self.resourceReaders()])
        return sorted(reads, key=lambda a: a.readStart)

    def loadMetadata(self, filename):
        """Load pipeline metadata from a <moviename>.run.metadata.xml file.

        Args:
            :filename: the filename of a <moviename>.run.metadata.xml file

        """
        if isinstance(filename, basestring):
            metadata = parseMetadata(str(filename))
        else:
            metadata = filename
        self.addMetadata(metadata)
        self.updateCounts()

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
        filters = self.filters.tests(readType=self._filterType())
        # Having no filters means no opportunity to pass. Fix by filling with
        # always-true (similar to disableFilters())
        if not filters:
            self._cachedFilters = [lambda x: True]
            return self._cachedFilters
        self._cachedFilters = filters
        return filters

    def _filterType(self):
        """A key that maps to a set of filtration keywords specific to this
        DataSet's ExternalResource type"""
        raise NotImplementedError()

    def makePathsAbsolute(self, curStart="."):
        """As part of the validation process, make all ResourceIds absolute
        URIs rather than relative paths. Generally not called by API users.

        Args:
            :curStart: The location from which relative paths should emanate.
        """
        log.debug("Making paths absolute")
        self._changePaths(
            lambda x, s=curStart: checkAndResolve(x, s))

    def makePathsRelative(self, outDir=False):
        """Make things easier for writing test cases: make all
        ResourceIds relative paths rather than absolute paths.
        A less common use case for API consumers.

        Args:
            :outDir: The location from which relative paths should originate

        """
        log.debug("Making paths relative")
        if outDir:
            self._changePaths(lambda x, s=outDir: os.path.relpath(x, s))
        else:
            self._changePaths(os.path.relpath)

    def _modResources(self, func):
        """Execute some function 'func' on each external resource in the
        dataset and each subdataset"""
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
                stack.extend(list(item.externalResources))
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
            :osPathFunc: A function for modifying paths (e.g. os.path.abspath)
            :checkMetaType: Update the metatype of externalResources if needed
        """
        metaTypeFunc = self._updateMetaType if checkMetaType else lambda x: x
        resFunc = partial(_pathChanger, osPathFunc, metaTypeFunc)
        self._modResources(resFunc)

    def _populateMetaTypes(self):
        """Add metatypes to those ExternalResources that currently are
        without"""
        self._modResources(self._updateMetaType)

    def _updateMetaType(self, resource):
        """Infer and set the metatype of 'resource' if it doesn't already have
        one."""
        if not resource.metaType:
            file_type = _fileType(resource.resourceId)
            resource.metaType = self._metaTypeMapping().get(file_type, "")
        if not resource.timeStampedName:
            mtype = resource.metaType
            tsName = _getTimeStampedName(mtype)
            resource.timeStampedName = tsName

    @staticmethod
    def _metaTypeMapping():
        """The available mappings between file extension and MetaType (informed
        by current class)."""
        # no metatypes for generic DataSet
        return {}

    def copyFiles(self, outdir):
        """Copy all of the top level ExternalResources to an output
        directory 'outdir'"""
        backticks('cp {i} {o}'.format(i=' '.join(self.toExternalFiles()),
                                      o=outdir))

    def disableFilters(self):
        """Disable read filtering for this object"""
        self.reFilter()
        self.noFiltering = True
        # a dummy filter:
        self._cachedFilters = [lambda x: True]

    def enableFilters(self):
        """Re-enable read filtering for this object"""
        self.reFilter()
        self.noFiltering = False

    def addFilters(self, newFilters, underConstruction=False):
        """Add new or extend the current list of filters. Public because there
        is already a reasonably compelling reason (the console script entry
        point). Most often used by the __add__ method.

        Args:
            :newFilters: a Filters object or properly formatted Filters record

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import SubreadSet
            >>> from pbcore.io.dataset.DataSetMembers import Filters
            >>> ds1 = SubreadSet()
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
        self.reFilter(light=underConstruction)

    def _checkObjMetadata(self, newMetadata):
        """Check new object metadata (as opposed to dataset metadata) against
        the object metadata currently in this DataSet for compatibility.

        Args:
            :newMetadata: The object metadata of a DataSet being considered for
                          merging
        """
        # If there is no objMetadata, this is a new dataset being populated
        if self.objMetadata:
            # if there isn't a Version in each, that will fail eventually
            if 'Version' in self.objMetadata and 'Version' in newMetadata:
                if newMetadata['Version'] == self.objMetadata['Version']:
                    return True
                # We'll make an exception for now: major version number passes
                elif (newMetadata['Version'].split('.')[0] ==
                      self.objMetadata['Version'].split('.')[0]):
                    log.warn("Future warning: merging datasets that don't "
                             "share a version number will fail.")
                    return True
                raise ValueError("Wrong dataset version for merging {v1} vs "
                                 "{v2}".format(
                                     v1=newMetadata.get('Version'),
                                     v2=self.objMetadata.get('Version')))
            log.warn("Future warning: merging will require Version "
                     "numbers for both DataSets")
        return True


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
            :newMetadata: a dictionary of object metadata from an XML file (or
                          carefully crafted to resemble one), or a wrapper
                          around said dictionary
            :kwargs: new metadata fields to be piled into the current metadata
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
                self.metadata = newMetadata

        for key, value in kwargs.items():
            self.metadata.addMetadata(key, value)

    def updateCounts(self):
        """Update the TotalLength and NumRecords for this DataSet.

        Not compatible with the base DataSet class, which has no ability to
        touch ExternalResources. -1 is used as a sentinel value for failed size
        determination. It should never be written out to XML in regular use.

        """
        self.metadata.totalLength = -1
        self.metadata.numRecords = -1

    def addExternalResources(self, newExtResources, updateCount=True):
        """Add additional ExternalResource objects, ensuring no duplicate
        resourceIds. Most often used by the __add__ method, rather than
        directly.

        Args:
            :newExtResources: A list of new ExternalResource objects, either
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
        if not isinstance(newExtResources, ExternalResources):
            tmp = ExternalResources()
            # have to wrap them here, as wrapNewResource does quite a bit and
            # importing into members would create a circular inport
            tmp.addResources([wrapNewResource(res)
                              if not isinstance(res, ExternalResource) else res
                              for res in newExtResources])
            newExtResources = tmp
        self.externalResources.merge(newExtResources)
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

    def _openFiles(self):
        """Open the top level ExternalResources"""
        raise RuntimeError("Not defined for this type of DataSet")

    def resourceReaders(self):
        """Return a list of open pbcore Reader objects for the
        top level ExternalResources in this DataSet"""
        raise RuntimeError("Not defined for this type of DataSet")

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
            >>> from pbcore.io import AlignmentSet
            >>> ds = AlignmentSet(data.getBam())
            >>> for record in ds.records:
            ...     print 'hn: %i' % record.holeNumber # doctest:+ELLIPSIS
            hn: ...
        """
        for resource in self.resourceReaders():
            for record in resource:
                yield record

    def __iter__(self):
        """Iterate over the records.

        The order of yielded reads is determined by the order of the
        ExternalResources and record order within each file"""
        if self.isIndexed:
            # this uses the index to respect filters
            for i in xrange(len(self)):
                yield self[i]
        else:
            # this uses post-filtering to respect filters
            for record in self.records:
                yield record

    @property
    def subSetNames(self):
        """The subdataset names present in this DataSet"""
        subNames = []
        for sds in self.subdatasets:
            subNames.extend(sds.name)
        return subNames

    def readsInSubDatasets(self, subNames=None):
        """To be used in conjunction with self.subSetNames"""
        if subNames is None:
            subNames = []
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

    # FIXME this is a workaround for the lack of support for ZMW chunking in
    # pbbam, and should probably go away once that is available.
    @property
    def zmwRanges(self):
        """
        Return the end-inclusive range of ZMWs covered by the dataset if this
        was explicitly set by filters via DataSet.split(zmws=True).

        """
        ranges = []
        for filt in self._filters:
            movie, start, end = None, 0, 0
            values = []
            for param in filt:
                if param.name == "movie":
                    movie = param.value
                elif param.name == "zm":
                    ival = int(param.value)
                    if param.operator == '>':
                        ival += 1
                    elif param.operator == '<':
                        ival -= 1
                    values.append(ival)
            ranges.append((movie, min(values), max(values)))
        return ranges

    # FIXME this is a workaround for the lack of support for barcode chunking
    # in pbbam, and should probably go away once that is available.
    @property
    def barcodes(self):
        """Return the list of barcodes explicitly set by filters via
        DataSet.split(barcodes=True).

        """
        barcodes = []
        for filt in self._filters:
            for param in filt:
                if param.name == "bc":
                    barcodes.append(param.value)
        return barcodes

    def toFofn(self, outfn=None, uri=False, relative=False):
        """Return a list of resource filenames (and write to optional outfile)

        Args:
            :outfn: (None) the file to which the resouce filenames are to be
                    written. If None, the only emission is a returned list of
                    file names.
            :uri: (t/F) write the resource filenames as URIs.
            :relative: (t/F) emit paths relative to outfofn or '.' if no
                       outfofn

        Returns:
            A list of filenames or uris

        Writes:
            (Optional) A file containing a list of filenames or uris

        Doctest:
            >>> from pbcore.io import DataSet
            >>> DataSet("bam1.bam", "bam2.bam", strict=False,
            ...         skipMissing=True).toFofn(uri=False)
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
        return self.externalResources.resourceIds

    @property
    def _castableDataSetTypes(self):
        """Tuple of DataSet types to which this DataSet can be cast"""
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
                'ConsensusAlignmentSet': ConsensusAlignmentSet,
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
        self._filters.registerCallback(self._wipeCaches)
        return self._filters

    @filters.setter
    def filters(self, value):
        """Limit setting to ensure cache hygiene and filter compatibility"""
        if value is None:
            self._filters = Filters()
        else:
            value.clearCallbacks()
            self._filters = value
        self.reFilter()

    def reFilter(self, light=True):
        """
        The filters on this dataset have changed, update DataSet state as
        needed
        """
        self._cachedFilters = []
        self._index = None
        self._indexMap = None
        if not light:
            self.metadata.totalLength = -1
            self.metadata.numRecords = -1
            if self.metadata.summaryStats:
                self.metadata.removeChildren('SummaryStats')
            self.updateCounts()

    def _wipeCaches(self):
        self.reFilter(False)

    @property
    def createdAt(self):
        """Return the DataSet CreatedAt timestamp"""
        return self.objMetadata.get('CreatedAt')

    @property
    def numRecords(self):
        """The number of records in this DataSet (from the metadata)"""
        return self._metadata.numRecords

    @numRecords.setter
    def numRecords(self, value):
        """The number of records in this DataSet (from the metadata)"""
        self._metadata.numRecords = value

    @property
    def totalLength(self):
        """The total length of this DataSet"""
        return self._metadata.totalLength

    @totalLength.setter
    def totalLength(self, value):
        """The total length of this DataSet"""
        self._metadata.totalLength = value

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
    def description(self):
        """The description of this DataSet"""
        return self.objMetadata.get('Description', '')

    @description.setter
    def description(self, value):
        """The description of this DataSet"""
        self.objMetadata['Description'] = value

    @property
    def numExternalResources(self):
        """The number of ExternalResources in this DataSet"""
        return len(self.externalResources)

    def _pollResources(self, func):
        """Collect the responses to func on each resource (or those with reads
        mapping to refName)."""
        return [func(resource) for resource in self.resourceReaders()]

    def _unifyResponses(self, responses, keyFunc=lambda x: x,
                        eqFunc=lambda x, y: x == y):
        """Make sure all of the responses from resources are the same."""
        if len(responses) > 1:
            # Check the rest against the first:
            for res in responses[1:]:
                if not eqFunc(keyFunc(responses[0]), keyFunc(res)):
                    raise ResourceMismatchError(responses)
        return responses[0]

    def hasBaseFeature(self, featureName):
        responses = self._pollResources(
            lambda x: x.hasBaseFeature(featureName))
        return self._unifyResponses(responses)

    def baseFeaturesAvailable(self):
        responses = self._pollResources(lambda x: x.baseFeaturesAvailable())
        return self._unifyResponses(responses)

    def hasPulseFeature(self, featureName):
        responses = self._pollResources(
            lambda x: x.hasPulseFeature(featureName))
        return self._unifyResponses(responses)

    def pulseFeaturesAvailable(self):
        responses = self._pollResources(lambda x: x.pulseFeaturesAvailable())
        return self._unifyResponses(responses)

    @property
    def sequencingChemistry(self):
        responses = self._pollResources(lambda x: x.sequencingChemistry)
        return list(_flatten(responses))

    @property
    def isEmpty(self):
        responses = self._pollResources(lambda x: getattr(x, 'isEmpty'))
        return all(responses)

    @property
    def readType(self):
        return self._checkIdentical('readType')

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

    @property
    def index(self):
        if self._index is None:
            log.debug("Populating index")
            self.assertIndexed()
            self._index = self._indexRecords()
            log.debug("Done populating index")
        return self._index

    def _indexRecords(self):
        raise NotImplementedError()

    def isIndexed(self):
        raise NotImplementedError()

    def assertIndexed(self):
        raise NotImplementedError()

    def _assertIndexed(self, acceptableTypes):
        if not self._openReaders:
            self._openFiles()
        for fname, reader in zip(self.toExternalFiles(),
                                 self.resourceReaders()):
            if not isinstance(reader, acceptableTypes):
                raise IOError(errno.EIO, "File not indexed", fname)
        return True

    def __getitem__(self, index):
        """Should respect filters for free, as _indexMap should only be
        populated by filtered reads. Only pbi filters considered, however."""
        if self._indexMap is None:
            _ = self.index
        if isinstance(index, int):
            # support negatives
            if index < 0:
                index = len(self.index) + index
            rrNo, recNo = self._indexMap[index]
            return self.resourceReaders()[rrNo][recNo]
        elif isinstance(index, slice):
            indexTuples = self._indexMap[index]
            return [self.resourceReaders()[ind[0]][ind[1]] for ind in
                    indexTuples]
        elif isinstance(index, list):
            indexTuples = [self._indexMap[ind] for ind in index]
            return [self.resourceReaders()[ind[0]][ind[1]] for ind in
                    indexTuples]
        elif isinstance(index, np.ndarray):
            indexTuples = self._indexMap[index]
            return [self.resourceReaders()[ind[0]][ind[1]] for ind in
                    indexTuples]
        elif isinstance(index, str):
            if 'id' in self.index.dtype.names:
                row = np.nonzero(self.index.id == index)[0][0]
                return self[row]
            else:
                raise NotImplementedError()


class ReadSet(DataSet):
    """Base type for read sets, should probably never be used as a concrete
    class"""

    def __init__(self, *files, **kwargs):
        super(ReadSet, self).__init__(*files, **kwargs)
        self._metadata = SubreadSetMetadata(self._metadata)

    def induceIndices(self):
        for res in self.externalResources:
            fname = res.resourceId
            newInds = []
            if not res.pbi:
                newInds.append(_pbindexBam(fname))
                self.close()
            if not res.bai:
                newInds.append(_indexBam(fname))
                self.close()
            if newInds:
                res.addIndices(newInds)
        self._populateMetaTypes()
        self.updateCounts()

    @property
    def isMapped(self):
        responses = self._pollResources(lambda x: x.isMapped)
        return self._unifyResponses(responses)

    @property
    def isIndexed(self):
        if self.hasPbi:
            return True
        return False

    @property
    def isBarcoded(self):
        """Determine whether all resources are barcoded files"""
        res = self._pollResources(
            lambda x: x.index.pbiFlags & PBI_FLAGS_BARCODE)
        return self._unifyResponses(res)

    def assertBarcoded(self):
        """Test whether all resources are barcoded files"""
        if not self.isBarcoded:
            raise RuntimeError("File not barcoded")

    def _openFiles(self):
        """Open the files (assert they exist, assert they are of the proper
        type before accessing any file)
        """
        if self._openReaders:
            log.debug("Closing old readers...")
            self.close()
        log.debug("Opening ReadSet resources")
        sharedRefs = {}
        infotables = []
        infodicts = []
        for extRes in self.externalResources:
            refFile = extRes.reference
            if refFile:
                if not refFile in sharedRefs:
                    log.debug("Using reference: {r}".format(r=refFile))
                    try:
                        sharedRefs[refFile] = IndexedFastaReader(refFile)
                    except IOError:
                        if not self._strict:
                            log.warn("Problem opening reference with"
                                     "IndexedFastaReader")
                            sharedRefs[refFile] = None
                        else:
                            raise
            location = urlparse(extRes.resourceId).path
            resource = None
            try:
                if extRes.resourceId.endswith('bam'):
                    resource = IndexedBamReader(location)
                    if refFile:
                        resource.referenceFasta = sharedRefs[refFile]
                else:
                    resource = CmpH5Reader(location)
            except (IOError, ValueError):
                if not self._strict and not extRes.pbi:
                    log.warn("pbi file missing for {f}, operating with "
                             "reduced speed and functionality".format(
                                 f=location))
                    resource = BamReader(location)
                    if refFile:
                        resource.referenceFasta = sharedRefs[refFile]
                else:
                    raise
            # Consolidate referenceDicts
            # This gets huge when there are ~90k references. If you have ~28
            # chunks, each with 28 BamReaders, each with 100MB referenceDicts,
            # you end up storing tens of gigs of just these (often identical)
            # dicts
            if not len(infotables):
                infotables.append(resource._referenceInfoTable)
                infodicts.append(resource._referenceDict)
            else:
                for ri, rd in zip(infotables, infodicts):
                    if np.array_equal(resource._referenceInfoTable, ri):
                        del resource._referenceInfoTable
                        del resource._referenceDict
                        resource._referenceInfoTable = ri
                        resource._referenceDict = rd
                        break
                    infotables.append(resource._referenceInfoTable)
                    infodicts.append(resource._referenceDict)
            self._openReaders.append(resource)
            try:
                if resource.isEmpty:
                    log.debug("{f} contains no reads!".format(
                        f=extRes.resourceId))
            except UnavailableFeature: # isEmpty requires bai
                if not list(itertools.islice(resource, 1)):
                    log.debug("{f} contains no reads!".format(
                        f=extRes.resourceId))
        if len(self._openReaders) == 0 and len(self.toExternalFiles()) != 0:
            raise IOError("No files were openable")
        log.debug("Done opening resources")


    def _filterType(self):
        return 'bam'

    @property
    def hasPbi(self):
        """Test whether all resources are opened as IndexedBamReader objects"""
        try:
            res = self._pollResources(lambda x: isinstance(x,
                                                           IndexedBamReader))
            return self._unifyResponses(res)
        except ResourceMismatchError:
            if not self._strict:
                log.warn("Resources inconsistently indexed")
                return False
            else:
                raise

    def _split_barcodes(self, chunks=0):
        """Split a readset into chunks by barcodes.

        Args:
            :chunks: The number of chunks to emit. If chunks < # barcodes,
                     barcodes are grouped by size. If chunks == # barcodes, one
                     barcode is assigned to each dataset regardless of size. If
                     chunks >= # barcodes, only # barcodes chunks are emitted

        """
        # Find all possible barcodes and counts for each
        self.assertIndexed()
        try:
            self.assertBarcoded()
        except RuntimeError:
            log.info("No barcodes found in BAM file, skipping split")
            return [self.copy()]
        barcodes = defaultdict(int)
        for bcTuple in itertools.izip(self.index.bcForward,
                                      self.index.bcReverse):
            if bcTuple != (-1, -1):
                barcodes[bcTuple] += 1

        log.debug("{i} barcodes found".format(i=len(barcodes.keys())))

        atoms = barcodes.items()

        # The number of reads per barcode is used for balancing
        balanceKey = lambda x: x[1]

        # Find the appropriate number of chunks
        if chunks <= 0 or chunks > len(atoms):
            chunks = len(atoms)

        log.debug("Making copies")
        results = [self.copy() for _ in range(chunks)]

        log.debug("Distributing chunks")
        chunks = self._chunkList(atoms, chunks, balanceKey)
        log.debug("Done chunking")
        log.debug("Modifying filters or resources")
        for result, chunk in zip(results, chunks):
            result.filters.removeRequirement('bc')
            result.filters.addRequirement(
                bc=[('=', list(c[0])) for c in chunk])

        # UniqueId was regenerated when the ExternalResource list was
        # whole, therefore we need to regenerate it again here
        log.debug("Generating new UUID")
        for result in results:
            result.reFilter()
            result.newUuid()
            result.updateCounts()

        # Update the basic metadata for the new DataSets from external
        # resources, or at least mark as dirty
        # TODO
        return results

    def _split_zmws(self, chunks, targetSize=None):
        """Holenumbers must be unique within each movie"""

        if chunks == 1:
            return [self.copy()]
        # make sure we can pull out the movie name:
        rgIdMovieNameMap = {rg[0]: rg[1] for rg in self.readGroupTable}

        # find atoms:
        active_holenumbers = self.index
        n_chunks = min(len(active_holenumbers), chunks)

        # if we have a target size and can have two or more chunks:
        if (not targetSize is None and len(active_holenumbers) > 1 and
                chunks > 1):
            n_chunks = min(n_chunks, len(active_holenumbers)/targetSize)
            # we want at least two if we can swing it:
            n_chunks = max(n_chunks, 2)

        # make sure there aren't too few atoms
        if n_chunks != chunks:
            log.info("Adjusted number of chunks to %d" % n_chunks)

        # sort atoms and group into chunks:
        active_holenumbers.sort(order=['qId', 'holeNumber'])
        view = _fieldsView(self.index, ['qId', 'holeNumber'])
        keys = np.unique(view)
        ranges = splitKeys(keys, n_chunks)

        # The above ranges can include hidden, unrepresented movienames that
        # are sandwiched between those in the range. In order to capture those,
        # we need to find the indices of the range bounds, then pull out the
        # chunks.
        hn_chunks = []
        for zmw_range in ranges:
            if zmw_range[0][0] == zmw_range[1][0]:
                hn_chunks.append(active_holenumbers[
                    (active_holenumbers['qId'] == zmw_range[0][0]) &
                    (active_holenumbers['holeNumber'] >= zmw_range[0][1]) &
                    (active_holenumbers['holeNumber'] <= zmw_range[1][1])])
            else:
                start = np.flatnonzero(
                    (active_holenumbers['qId'] == zmw_range[0][0]) &
                    (active_holenumbers['holeNumber'] == zmw_range[0][1]))[0]
                end = np.flatnonzero(
                    (active_holenumbers['qId'] == zmw_range[1][0]) &
                    (active_holenumbers['holeNumber'] == zmw_range[1][1]))[-1]
                hn_chunks.append(active_holenumbers[start:(end + 1)])

        results = []
        log.debug("Making copies")
        tmp_results = [self.copy() for _ in range(n_chunks)]

        # add filters
        for chunk, res in zip(hn_chunks, tmp_results):
            # check if multiple movies:
            if chunk[0]['qId'] == chunk[-1]['qId']:
                movieName = rgIdMovieNameMap[chunk[0]['qId']]
                zmwStart = chunk[0]['holeNumber']
                zmwEnd = chunk[-1]['holeNumber']
                res._filters.clearCallbacks()
                res._filters.addRequirement(
                    movie=[('=', movieName)],
                    zm=[('<', zmwEnd+1)])
                res._filters.addRequirement(
                    zm=[('>', zmwStart-1)])
            else:
                movieNames = []
                zmwStarts = []
                zmwEnds = []
                for mov in np.unique(chunk['qId']):
                    movieNames.append(rgIdMovieNameMap[mov])
                    inds = np.flatnonzero(chunk['qId'] == mov)
                    zmwStarts.append(chunk[inds[0]]['holeNumber'])
                    zmwEnds.append(chunk[inds[-1]]['holeNumber'])
                res._filters.clearCallbacks()
                res._filters.addRequirement(
                    movie=[('=', mn) for mn in movieNames],
                    zm=[('<', ze + 1) for ze in zmwEnds])
                res._filters.mapRequirement(
                    zm=[('>', zs - 1) for zs in zmwStarts])
            res.numRecords = len(chunk)
            res.totalLength = sum(chunk['qEnd'] - chunk['qStart'])
            res.newUuid()
            results.append(res)

        # we changed the sort order above, so this is dirty:
        self._index = None
        self._indexMap = None

        # Update the basic metadata for the new DataSets from external
        # resources, or at least mark as dirty
        # TODO
        return results


    @property
    def readGroupTable(self):
        """Combine the readGroupTables of each external resource"""
        responses = self._pollResources(lambda x: x.readGroupTable)
        if len(responses) > 1:
            # append the read groups, but eliminate duplicates.
            tbr = _uniqueRecords(reduce(np.append, responses))
            # reassign qIds if dupes:
            if len(set(tbr['ID'])) < len(tbr):
                self._readGroupTableIsRemapped = True
                tbr['ID'] = range(len(tbr))
            return tbr
        else:
            return responses[0]

    @property
    def movieIds(self):
        """A dict of movieName: movieId for the joined readGroupTable"""
        return {rg.MovieName: rg.ID for rg in self.readGroupTable}

    def assertIndexed(self):
        self._assertIndexed((IndexedBamReader, CmpH5Reader))

    @property
    def isCmpH5(self):
        """Test whether all resources are cmp.h5 files"""
        res = self._pollResources(lambda x: isinstance(x, CmpH5Reader))
        return self._unifyResponses(res)

    def _fixQIds(self, indices, resourceReader):
        qId_acc = lambda x: x.MovieID
        if not self.isCmpH5:
            qId_acc = lambda x: x.qId

        rr = resourceReader
        try:
            # this would populate the _readGroupTableIsRemapped member, but
            # for whatever reason a lot of cmp.h5's are broken
            _ = self.readGroupTable
        except ChemistryLookupError:
            # this should be an error, but that would mess up Quiver cram
            # tests. If anyone tries to access the readGroupTable in a
            # dataset it will still fail, at least
            log.info("Chemistry information could not be found in "
                     "cmp.h5, cannot fix the readGroupTable or "
                     "MovieID field.")
        if self._readGroupTableIsRemapped:
            log.debug("Must correct index qId's")
            qIdMap = dict(zip(rr.readGroupTable.ID,
                              rr.readGroupTable.MovieName))
            nameMap = self.movieIds
            for qId in qIdMap.keys():
                qId_acc(indices)[qId_acc(indices) == qId] = nameMap[
                    qIdMap[qId]]


    def _indexRecords(self):
        """Returns index recarray summarizing all of the records in all of
        the resources that conform to those filters addressing parameters
        cached in the pbi.

        """
        recArrays = []
        _indexMap = []
        for rrNum, rr in enumerate(self.resourceReaders()):
            indices = rr.index
            if len(indices) == 0:
                continue

            self._fixQIds(indices, rr)

            if not self._filters or self.noFiltering:
                recArrays.append(indices._tbl)
                _indexMap.extend([(rrNum, i) for i in
                                       range(len(indices._tbl))])
            else:
                # Filtration will be necessary:
                nameMap = {}
                if not rr.referenceInfoTable is None:
                    nameMap = {name: n
                               for n, name in enumerate(
                                   rr.referenceInfoTable['Name'])}
                passes = self._filters.filterIndexRecords(indices._tbl,
                                                          nameMap,
                                                          self.movieIds)
                newInds = indices._tbl[passes]
                recArrays.append(newInds)
                _indexMap.extend([(rrNum, i) for i in
                                       np.flatnonzero(passes)])
        self._indexMap = np.array(_indexMap, dtype=[('reader', 'uint64'),
                                                    ('index', 'uint64')])
        if recArrays == []:
            return recArrays
        return _stackRecArrays(recArrays)

    def resourceReaders(self):
        """Open the files in this ReadSet"""
        if not self._openReaders:
            self._openFiles()
        return self._openReaders

    @property
    def _length(self):
        """Used to populate metadata in updateCounts. We're using the pbi here,
        which is necessary and sufficient for both subreadsets and
        alignmentsets, but doesn't work for hdfsubreadsets. Rather than
        duplicate code, we'll implement the hdf specific _length as an
        overriding function where needed.

        ..note:: Both mapped and unmapped bams can be either indexed or
                 unindexed. This makes life more difficult, but we should
                 expect a pbi for both subreadsets and alignmentsets

        """
        count = len(self.index)
        length = 0
        if count:
            length = sum(self.index.qEnd - self.index.qStart)
        return count, length

    def _resourceSizes(self):
        sizes = []
        for rr in self.resourceReaders():
            sizes.append((len(rr.index), sum(rr.index.qEnd - rr.index.qStart)))
        return sizes

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

    def consolidate(self, dataFile, numFiles=1, useTmp=True):
        """Consolidate a larger number of bam files to a smaller number of bam
        files (min 1)

        Args:
            :dataFile: The name of the output file. If numFiles >1 numbers will
                       be added.
            :numFiles: The number of data files to be produced.

        """
        references = [er.reference for er in self.externalResources if
                      er.reference]
        if which('pbmerge'):
            log.debug("Using pbmerge to consolidate")
            dsets = self.split(zmws=True, chunks=numFiles)
            if numFiles > 1:
                fnames = [_infixFname(dataFile, str(i))
                          for i in range(numFiles)]
            else:
                fnames = [dataFile]
            for chunk, fname in zip(dsets, fnames):
                consolidateXml(chunk, fname, useTmp=useTmp)
            log.debug("Replacing resources")
            self.externalResources = ExternalResources()
            self.addExternalResources(fnames)
            self.induceIndices()
        else:
            if numFiles > 1:
                assert (len(self.resourceReaders()) ==
                        len(self.toExternalFiles()))
                resSizes = [[i, size[0], size[1]]
                            for i, size in enumerate(self._resourceSizes())]
                chunks = self._chunkList(resSizes, numFiles, lambda x: x[1])
                resLists = []
                for chunk in chunks:
                    thisResList = []
                    for i in chunk:
                        thisResList.append(self.toExternalFiles()[i[0]])
                    resLists.append(thisResList)
                fnames = [_infixFname(dataFile, str(i))
                          for i in range(numFiles)]
                for resList, fname in zip(resLists, fnames):
                    consolidateBams(resList, fname, filterDset=self,
                                    useTmp=useTmp)
                log.debug("Replacing resources")
                self.externalResources = ExternalResources()
                self.addExternalResources(fnames)
            else:
                consolidateBams(self.toExternalFiles(), dataFile,
                                filterDset=self, useTmp=useTmp)
                # TODO: remove subdatasets?
                log.debug("Replacing resources")
                self.externalResources = ExternalResources()
                self.addExternalResources([dataFile])
        # make sure reference gets passed through:
        if references:
            refCounts = dict(Counter(references))
            if len(refCounts) > 1:
                log.warn("Consolidating AlignmentSets with "
                         "different references, but BamReaders "
                         "can only have one. References will be "
                         "lost")
            else:
                for extres in self.externalResources:
                    extres.reference = refCounts.keys()[0]
        # reset the indexmap especially, as it is out of date:
        self._index = None
        self._indexMap = None
        self._openReaders = []
        self._populateMetaTypes()

    def updateCounts(self):
        if self._skipCounts:
            log.debug("SkipCounts is true, skipping updateCounts()")
            self.metadata.totalLength = -1
            self.metadata.numRecords = -1
            return
        try:
            self.assertIndexed()
            log.debug('Updating counts')
            numRecords, totalLength = self._length
            self.metadata.totalLength = totalLength
            self.metadata.numRecords = numRecords
            self._countsUpdated = True
        except (IOError, UnavailableFeature):
            if not self._strict:
                log.debug("File problem, metadata not populated")
                self.metadata.totalLength = 0
                self.metadata.numRecords = 0
            else:
                raise


class HdfSubreadSet(ReadSet):

    datasetType = DataSetMetaTypes.HDF_SUBREAD

    def __init__(self, *files, **kwargs):
        super(HdfSubreadSet, self).__init__(*files, **kwargs)

        # The metatype for this dataset type is inconsistent, plaster over it
        # here:
        self.objMetadata["MetaType"] = "PacBio.DataSet.HdfSubreadSet"
        self.objMetadata["TimeStampedName"] = _getTimeStampedName(
            self.objMetadata["MetaType"])

    def induceIndices(self):
        log.debug("Bax files already indexed")

    @property
    def isIndexed(self):
        return False

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
        if len(self._openReaders) == 0 and len(self.toExternalFiles()) != 0:
            raise IOError("No files were openable or reads found")
        log.debug("Done opening resources")

    @property
    def _length(self):
        """Used to populate metadata in updateCounts"""
        length = 0
        count = 0
        for rec in self.records:
            count += 1
            hqReg = rec.hqRegion
            length += hqReg[1] - hqReg[0]
        return count, length

    def updateCounts(self):
        """Overriding here so we don't have to assertIndexed"""
        if self._skipCounts:
            log.debug("SkipCounts is true, skipping updateCounts()")
            self.metadata.totalLength = -1
            self.metadata.numRecords = -1
            return
        try:
            log.debug('Updating counts')
            numRecords, totalLength = self._length
            self.metadata.totalLength = totalLength
            self.metadata.numRecords = numRecords
            self._countsUpdated = True
        except (IOError, UnavailableFeature):
            if not self._strict:
                log.debug("File problem, metadata not populated")
                self.metadata.totalLength = 0
                self.metadata.numRecords = 0
            else:
                raise

    def consolidate(self, dataFile, numFiles=1):
        raise NotImplementedError()

    @staticmethod
    def _metaTypeMapping():
        return {'bax.h5':'PacBio.SubreadFile.BaxFile',
                'bas.h5':'PacBio.SubreadFile.BasFile', }


class SubreadSet(ReadSet):
    """DataSet type specific to Subreads

    DocTest:

        >>> from pbcore.io import SubreadSet
        >>> from pbcore.io.dataset.DataSetMembers import ExternalResources
        >>> import pbcore.data.datasets as data
        >>> ds1 = SubreadSet(data.getXml(no=5), skipMissing=True)
        >>> ds2 = SubreadSet(data.getXml(no=5), skipMissing=True)
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
        >>> ds4 = SubreadSet(data.getSubreadSet(), skipMissing=True)
        >>> ds4 # doctest:+ELLIPSIS
        <SubreadSet...
        >>> ds4._metadata # doctest:+ELLIPSIS
        <SubreadSetMetadata...
        >>> len(ds4.metadata.collections)
        1
    """

    datasetType = DataSetMetaTypes.SUBREAD

    def __init__(self, *files, **kwargs):
        super(SubreadSet, self).__init__(*files, **kwargs)

    @staticmethod
    def _metaTypeMapping():
        # This doesn't work for scraps.bam, whenever that is implemented
        return {'bam':'PacBio.SubreadFile.SubreadBamFile',
                'bai':'PacBio.Index.BamIndex',
                'pbi':'PacBio.Index.PacBioIndex',
                }


class AlignmentSet(ReadSet):
    """DataSet type specific to Alignments. No type specific Metadata exists,
    so the base class version is OK (this just ensures type representation on
    output and expandability"""

    datasetType = DataSetMetaTypes.ALIGNMENT

    def __init__(self, *files, **kwargs):
        """ An AlignmentSet

        Args:
            :files: handled by super
            :referenceFastaFname=None: the reference fasta filename for this \
                                       alignment.
            :strict=False: see base class
            :skipCounts=False: see base class
        """
        super(AlignmentSet, self).__init__(*files, **kwargs)
        fname = kwargs.get('referenceFastaFname', None)
        if fname:
            self.addReference(fname)
        self.__referenceIdMap = None

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
            >>> from pbcore.io import AlignmentSet
            >>> ds = AlignmentSet(data.getBam())
            >>> for record in ds.records:
            ...     print 'hn: %i' % record.holeNumber # doctest:+ELLIPSIS
            hn: ...
        """
        if self.isIndexed:
            for i in range(len(self.index)):
                yield self[i]
        else:
            for resource in self.resourceReaders():
                for record in resource:
                    yield record

    def consolidate(self, *args, **kwargs):
        if self.isCmpH5:
            raise NotImplementedError()
        else:
            return super(AlignmentSet, self).consolidate(*args, **kwargs)

    def induceIndices(self):
        if self.isCmpH5:
            log.debug("Cmp.h5 files already indexed")
        else:
            return super(AlignmentSet, self).induceIndices()

    @property
    def isIndexed(self):
        if self.isCmpH5:
            return True
        else:
            return super(AlignmentSet, self).isIndexed

    def addReference(self, fname):
        if isinstance(fname, ReferenceSet):
            reference = fname.externalResources.resourceIds
        else:
            reference = ReferenceSet(fname).externalResources.resourceIds
        if len(reference) > 1:
            if len(reference) != self.numExternalResources:
                raise ResourceMismatchError(
                    "More than one reference found, but not enough for one "
                    "per resource")
            for res, ref in zip(self.externalResources, reference):
                res.reference = ref
        else:
            for res in self.externalResources:
                res.reference = reference[0]
            self._openFiles()

    def _fixTIds(self, indices, rr, correctIds=True):
        tId_acc = lambda x: x.RefGroupID
        rName = lambda x: x['FullName']
        if not self.isCmpH5:
            tId_acc = lambda x: x.tId
            rName = lambda x: x['Name']
        if correctIds and self._stackedReferenceInfoTable:
            log.debug("Must correct index tId's")
            tIdMap = dict(zip(rr.referenceInfoTable['ID'],
                              rName(rr.referenceInfoTable)))
            nameMap = self.refIds
            for tId in tIdMap.keys():
                tId_acc(indices)[tId_acc(indices) == tId] = nameMap[
                    tIdMap[tId]]

    def _indexRecords(self, correctIds=True):
        """Returns index records summarizing all of the records in all of
        the resources that conform to those filters addressing parameters
        cached in the pbi.

        """
        recArrays = []
        log.debug("Processing resource indices")
        _indexMap = []
        for rrNum, rr in enumerate(self.resourceReaders()):
            indices = rr.index
            # pbi files lack e.g. mapping cols when bam emtpy, ignore
            if len(indices) == 0:
                continue
            # TODO(mdsmith)(2016-01-19) rename the fields instead of branching:
            #if self.isCmpH5:
            #    _renameField(indices, 'MovieID', 'qId')
            #    _renameField(indices, 'RefGroupID', 'tId')
            if not self.isCmpH5:
                indices = indices._tbl

            # Correct tId field
            self._fixTIds(indices, rr, correctIds)

            # Correct qId field
            self._fixQIds(indices, rr)

            # filter
            if not self._filters or self.noFiltering:
                recArrays.append(indices)
                _indexMap.extend([(rrNum, i) for i in
                                  range(len(indices))])
            else:
                passes = self._filters.filterIndexRecords(indices, self.refIds,
                                                          self.movieIds)
                newInds = indices[passes]
                recArrays.append(newInds)
                _indexMap.extend([(rrNum, i) for i in
                                  np.flatnonzero(passes)])
        self._indexMap = np.array(_indexMap, dtype=[('reader', 'uint64'),
                                                    ('index', 'uint64')])
        if recArrays == []:
            return recArrays
        tbr = _stackRecArrays(recArrays)

        # sort if cmp.h5 so we can rectify RowStart/End, maybe someday bam
        if self.isCmpH5:
            sort_order = np.argsort(tbr, order=('RefGroupID', 'tStart',
                                                'tEnd',))
            tbr = tbr[sort_order]
            self._indexMap = self._indexMap[sort_order]
            ranges = _ranges_in_list(tbr.RefGroupID)
            for ref in self.referenceInfoTable:
                bounds = ranges.get(ref.ID)
                if bounds:
                    ref.StartRow = bounds[0]
                    # we want the ranges to be inclusive:
                    ref.EndRow = bounds[1] - 1
                # and fix the naming scheme while we're at it
                ref.Name = self._cleanCmpName(ref.FullName)
        return tbr

    def resourceReaders(self, refName=False):
        """A generator of Indexed*Reader objects for the ExternalResources
        in this DataSet.

        Args:
            :refName: Only yield open resources if they have refName in their
                      referenceInfoTable

        Yields:
            An open indexed alignment file

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import AlignmentSet
            >>> ds = AlignmentSet(data.getBam())
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
    def refNames(self):
        """A list of reference names (id)."""
        return np.sort(self.referenceInfoTable["Name"])

    def _indexReadsInReference(self, refName):
        # This can probably be deprecated for all but the official reads in
        # range (and maybe reads in reference)
        refName = self.guaranteeName(refName)

        desiredTid = self.refIds[refName]
        tIds = self.tId
        passes = tIds == desiredTid
        return self.index[passes]

    def _resourceSizes(self):
        sizes = []
        for rr in self.resourceReaders():
            sizes.append((len(rr.index), sum(rr.index.aEnd - rr.index.aStart)))
        return sizes

    @property
    def refWindows(self):
        """Going to be tricky unless the filters are really focused on
        windowing the reference. Much nesting or duplication and the correct
        results are really not guaranteed"""
        log.debug("Fetching reference windows...")
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
                            winend = param.value
                        if param.name == 'tend':
                            winstart = param.value
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
        log.debug("Done fetching reference windows")
        return sorted(windowTuples)

    def countRecords(self, rname=None, winStart=None, winEnd=None):
        """Count the number of records mapped to 'rname' that overlap with
        'window'"""
        if rname and winStart != None and winEnd != None:
            return len(self._indexReadsInRange(rname, winStart, winEnd))
        elif rname:
            return len(self._indexReadsInReference(rname))
        else:
            return len(self.index)

    def readsInReference(self, refName):
        """A generator of (usually) BamAlignment objects for the
        reads in one or more Bam files pointed to by the ExternalResources in
        this DataSet that are mapped to the specified reference genome.

        Args:
            :refName: the name of the reference that we are sampling.

        Yields:
            BamAlignment objects

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import AlignmentSet
            >>> ds = AlignmentSet(data.getBam())
            >>> for read in ds.readsInReference(ds.refNames[15]):
            ...     print 'hn: %i' % read.holeNumber # doctest:+ELLIPSIS
            hn: ...

        """

        try:
            refName = self.guaranteeName(refName)
            refLen = self.refLengths[refName]
        except (KeyError, AttributeError):
            raise StopIteration
        for read in self.readsInRange(refName, 0, refLen):
            yield read

    def intervalContour(self, rname, tStart=0, tEnd=None):
        """Take a set of index records and build a pileup of intervals, or
        "contour" describing coverage over the contig

        ..note:: Naively incrementing values in an array is too slow and takes
        too much memory. Sorting tuples by starts and ends and iterating
        through them and the reference (O(nlogn + nlogn + n + n + m)) takes too
        much memory and time. Iterating over the reference, using numpy
        conditional indexing at each base on tStart and tEnd columns uses no
        memory, but is too slow (O(nm), but in numpy (C, hopefully)). Building
        a delta list via sorted tStarts and tEnds one at a time saves memory
        and is ~5x faster than the second method above (O(nlogn + nlogn + m)).

        """
        log.debug("Generating coverage summary")
        index = self._indexReadsInReference(rname)
        if tEnd is None:
            tEnd = self.refLengths[rname]
        coverage = [0] * (tEnd - tStart)
        starts = sorted(index.tStart)
        for i in starts:
            # ends are exclusive
            if i >= tEnd:
                continue
            if i >= tStart:
                coverage[i - tStart] += 1
            else:
                coverage[0] += 1
        del starts
        ends = sorted(index.tEnd)
        for i in ends:
            # ends are exclusive
            if i <= tStart:
                continue
            # ends are exclusive
            if i < tEnd:
                coverage[i - tStart] -= 1
        del ends
        curCov = 0
        for i, delta in enumerate(coverage):
            curCov += delta
            coverage[i] = curCov
        return coverage

    def splitContour(self, contour, splits):
        """Take a contour and a number of splits, return the location of each
        coverage mediated split with the first at 0"""
        log.debug("Splitting coverage summary")
        totalCoverage = sum(contour)
        splitSize = totalCoverage/splits
        tbr = [0]
        for _ in range(splits - 1):
            size = 0
            # Start where the last one ended, so we append the current endpoint
            tbr.append(tbr[-1])
            while (size < splitSize and
                   tbr[-1] < (len(contour) - 1)):
                # iterate the endpoint
                tbr[-1] += 1
                # track the size
                size += contour[tbr[-1]]
        assert len(tbr) == splits
        return tbr

    def _shiftAtoms(self, atoms):
        shiftedAtoms = []
        rnames = defaultdict(list)
        for atom in atoms:
            rnames[atom[0]].append(atom)
        for rname, rAtoms in rnames.iteritems():
            if len(rAtoms) > 1:
                contour = self.intervalContour(rname)
                splits = self.splitContour(contour, len(rAtoms))
                ends = splits[1:] + [self.refLengths[rname]]
                for start, end in zip(splits, ends):
                    newAtom = (rname, start, end)
                    shiftedAtoms.append(newAtom)
            else:
                shiftedAtoms.append(rAtoms[0])
        return shiftedAtoms

    def _split_contigs(self, chunks, maxChunks=0, breakContigs=False,
                       targetSize=5000, byRecords=False, updateCounts=True):
        """Split a dataset into reference windows based on contigs.

        Args:
            :chunks: The number of chunks to emit. If chunks < # contigs,
                     contigs are grouped by size. If chunks == contigs, one
                     contig is assigned to each dataset regardless of size. If
                     chunks >= contigs, contigs are split into roughly equal
                     chunks (<= 1.0 contig per file).

        """
        # removed the non-trivial case so that it is still filtered to just
        # contigs with associated records

        # The format is rID, start, end, for a reference window
        log.debug("Fetching reference names and lengths")
        # pull both at once so you only have to mess with the
        # referenceInfoTable once.
        refLens = self.refLengths
        refNames = refLens.keys()
        log.debug("{i} references found".format(i=len(refNames)))

        log.debug("Finding contigs")
        if byRecords:
            log.debug("Counting records...")
            atoms = [(rn, 0, 0, count)
                     for rn, count in zip(refNames, map(self.countRecords,
                                                        refNames))
                     if count != 0]
            balanceKey = lambda x: self.countRecords(*x)
        else:
            # if there are that many references, on average they will probably
            # be distributed pretty evenly. Checking the counts will also be
            # super expensive
            if len(refNames) < 100:
                atoms = [(rn, 0, refLens[rn]) for rn in refNames if
                         self.countRecords(rn) != 0]
            else:
                atoms = [(rn, 0, refLens[rn]) for rn in refNames]
            balanceKey = lambda x: x[2] - x[1]
        log.debug("{i} contigs found".format(i=len(atoms)))

        # By providing maxChunks and not chunks, this combination will set
        # chunks down to < len(atoms) < maxChunks
        if not chunks:
            log.debug("Chunks not set, splitting to len(atoms): {i}"
                      .format(i=len(atoms)))
            chunks = len(atoms)
        if maxChunks and chunks > maxChunks:
            log.debug("maxChunks trumps chunks")
            chunks = maxChunks

        # Decide whether to intelligently limit chunk count:
        if maxChunks and breakContigs:
            # The bounds:
            minNum = 2
            maxNum = maxChunks
            # Adjust
            log.debug("Target numRecords per chunk: {i}".format(i=targetSize))
            dataSize = self.numRecords
            log.debug("numRecords in dataset: {i}".format(i=dataSize))
            chunks = int(dataSize/targetSize)
            # Respect bounds:
            chunks = minNum if chunks < minNum else chunks
            chunks = maxNum if chunks > maxNum else chunks
            log.debug("Resulting number of chunks: {i}".format(i=chunks))

        # refwindow format: rId, start, end
        if chunks > len(atoms):
            # splitting atom format is slightly different (but more compatible
            # going forward with countRecords): (rId, size, segments)

            # Lets do a rough split, counting reads once and assuming uniform
            # coverage (reads span, therefore can't split by specific reads)
            if byRecords:
                atoms = [[rn, size, 1] for rn, _, _, size in atoms]
            else:
                atoms = [[rn, refLens[rn], 1] for rn, _, _ in atoms]
            log.debug("Splitting atoms")
            atoms = self._split_atoms(atoms, chunks)

            # convert back to window format:
            segments = []
            for atom in atoms:
                segment_size = atom[1]/atom[2]
                if byRecords:
                    segment_size = refLens[atom[0]]/atom[2]
                sub_segments = [(atom[0], segment_size * i, segment_size *
                                 (i + 1)) for i in range(atom[2])]
                # if you can't divide it evenly you may have some messiness
                # with the last window. Fix it:
                tmp = sub_segments.pop()
                tmp = (tmp[0], tmp[1], refLens[tmp[0]])
                sub_segments.append(tmp)
                segments.extend(sub_segments)
            atoms = segments
        elif breakContigs and not byRecords:
            log.debug("Checking for oversized chunks")
            # we may have chunks <= len(atoms). We wouldn't usually split up
            # contigs, but some might be huge, resulting in some tasks running
            # very long
            # We are only doing this for refLength splits for now, as those are
            # cheap (and quiver is linear in length not coverage)
            dataSize = sum(refLens.values())
            # target size per chunk:
            target = dataSize/chunks
            log.debug("Target chunk length: {t}".format(t=target))
            newAtoms = []
            for i, atom in enumerate(atoms):
                testAtom = atom
                while testAtom[2] - testAtom[1] > target:
                    newAtom1 = (testAtom[0], testAtom[1], testAtom[1] + target)
                    newAtom2 = (testAtom[0], testAtom[1] + target, testAtom[2])
                    newAtoms.append(newAtom1)
                    testAtom = newAtom2
                newAtoms.append(testAtom)
                atoms = newAtoms

        log.debug("Done defining {n} chunks".format(n=chunks))
        # duplicate
        log.debug("Making copies")
        results = [self.copy() for _ in range(chunks)]

        if byRecords:
            log.debug("Respacing chunks by records")
            atoms = self._shiftAtoms(atoms)
        # indicates byRecords with no sub atom splits: (the fourth spot is
        # countrecords in that window)
        if len(atoms[0]) == 4:
            balanceKey = lambda x: x[3]
        log.debug("Distributing chunks")
        # if we didn't have to split atoms and are doing it byRecords, the
        # original counts are still valid:
        #
        # Otherwise we'll now have to count records again to recombine atoms
        chunks = self._chunkList(atoms, chunks, balanceKey)

        log.debug("Done chunking")
        log.debug("Modifying filters or resources")
        for result, chunk in zip(results, chunks):
            # we don't want to updateCounts or anything right now, so we'll
            # block that functionality:
            result._filters.clearCallbacks()
            if atoms[0][2]:
                result._filters.addRequirement(
                    rname=[('=', c[0]) for c in chunk],
                    tStart=[('<', c[2]) for c in chunk],
                    tEnd=[('>', c[1]) for c in chunk])
            else:
                result._filters.addRequirement(
                    rname=[('=', c[0]) for c in chunk])

        # UniqueId was regenerated when the ExternalResource list was
        # whole, therefore we need to regenerate it again here
        log.debug("Generating new UUID")
        # At this point the ID's should be corrected, so the namemap should be
        # here:
        for result in results:
            result.newUuid()
            # If there are so many filters that it will be really expensive, we
            # will use an approximation for the number of records and bases.
            # This is probably not too far off, if there are that many chunks
            # to distribute. We'll still round to indicate that it is an
            # abstraction.
            if len(result._filters) > 100:
                meanNum = self.numRecords/len(chunks)
                result.numRecords = long(round(meanNum,
                                               (-1 * len(str(meanNum))) + 3))
                meanLen = self.totalLength/len(chunks)
                result.totalLength = long(round(meanLen,
                                                (-1 * len(str(meanLen))) + 3))
            elif updateCounts:
                result._openReaders = self._openReaders
                passes = result._filters.filterIndexRecords(self.index,
                                                            self.refIds,
                                                            self.movieIds)
                result._index = self.index[passes]
                result.updateCounts()
                del result._index
                del passes
                result._index = None

        # Update the basic metadata for the new DataSets from external
        # resources, or at least mark as dirty
        # TODO
        return results

    def _indexReadsInRange(self, refName, start, end, justIndices=False):
        """Return the index (pbi) records within a range.

        ..note:: Not sorted by genomic location!

        """
        desiredTid = self.refIds[refName]
        if self.isCmpH5:
            passes = ((self.index.RefGroupID == desiredTid) &
                      (self.index.tStart < end) &
                      (self.index.tEnd > start))
        else:
            passes = ((self.index.tId == desiredTid) &
                      (self.index.tStart < end) &
                      (self.index.tEnd > start))
        if justIndices:
            return np.nonzero(passes)[0]
            #return passes
        return self.index[passes]

    def _pbiReadsInRange(self, refName, start, end, longest=False,
                         sampleSize=0):
        """Return the reads in range for a file, but use the index in this
        object to get the order of the (reader, read) index tuples, instead of
        using the pbi rangeQuery for each file and merging the actual reads.
        This also opens up the ability to sort the reads by length in the
        window, and yield in that order (much much faster for quiver)

        Args:
            :refName: The reference name to sample
            :start: The start of the target window
            :end: The end of the target window
            :longest: (False) yield the longest reads first

        Yields:
            reads in the range, potentially longest first

        """
        if not refName in self.refNames:
            raise StopIteration
        # get pass indices
        passes = self._indexReadsInRange(refName, start, end, justIndices=True)
        mapPasses = self._indexMap[passes]
        if longest:
            def lengthInWindow(hits):
                ends = hits.tEnd
                post = ends > end
                ends[post] = end
                starts = hits.tStart
                pre = starts < start
                starts[pre] = start
                return ends - starts
            lens = lengthInWindow(self.index[passes])
            # reverse the keys here, so the descending sort is stable
            lens = (end - start) - lens
            if sampleSize != 0:
                if len(lens) != 0:
                    min_len = min(lens)
                    count_min = Counter(lens)[min_len]
                else:
                    count_min = 0
                if count_min > sampleSize:
                    sort_order = lens.argsort()
                else:
                    sort_order = lens.argsort(kind='mergesort')
            else:
                sort_order = lens.argsort(kind='mergesort')
            mapPasses = mapPasses[sort_order]
        elif len(self.toExternalFiles()) > 1:
            # sort the pooled passes and indices using a stable algorithm
            sort_order = self.index[passes].tStart.argsort(kind='mergesort')
            # pull out indexMap using those passes
            mapPasses = mapPasses[sort_order]
        return self._getRecords(mapPasses)

    def _getRecords(self, indexList, buffsize=1):
        """Get the records corresponding to indexList

        Args:
            :indexList: A list of (reader, read) index tuples
            :buffsize: The number of reads to buffer (coalesced file reads)

        Yields:
            reads from all files

       """
        # yield in order of sorted indexMap
        if buffsize == 1:
            for indexTuple in indexList:
                yield self.resourceReaders()[indexTuple[0]].atRowNumber(
                    indexTuple[1])
        else:
            def debuf():
                # This will store the progress through the buffer for each
                # reader
                reqCacheI = [0] * len(self.resourceReaders())
                # fill the record cache
                for rrNum, rr in enumerate(self.resourceReaders()):
                    for req in reqCache[rrNum]:
                        recCache[rrNum].append(rr.atRowNumber(req))
                # empty cache
                for i in range(cacheFill):
                    rrNum = fromCache[i]
                    curI = reqCacheI[rrNum]
                    reqCacheI[rrNum] += 1
                    yield recCache[rrNum][curI]

            def cleanBuffs():
                # This will buffer the records being pulled from each reader
                recCache = [[] for _ in self.resourceReaders()]
                # This will buffer the indicies being pulled from each reader
                reqCache = [[] for _ in self.resourceReaders()]
                # This will store the order in which reads are consumed, which
                # here can be specified by the reader number (read index order
                # is cached in the reqCache buffer)
                fromCache = [None] * buffsize
                return recCache, reqCache, fromCache, 0

            # The algorithm:
            recCache, reqCache, fromCache, cacheFill = cleanBuffs()
            for indexTuple in indexList:
                # segregate the requests by reader into ordered lists of read
                # indices
                reqCache[indexTuple[0]].append(indexTuple[1])
                # keep track of the order in which readers should be sampled,
                # which will maintain the overall read order
                fromCache[cacheFill] = indexTuple[0]
                cacheFill += 1
                if cacheFill >= buffsize:
                    for rec in debuf():
                        yield rec
                    recCache, reqCache, fromCache, cacheFill = cleanBuffs()
            if cacheFill > 0:
                for rec in debuf():
                    yield rec

    def guaranteeName(self, nameOrId):
        refName = nameOrId
        if isinstance(refName, np.int64):
            refName = str(refName)
        if refName.isdigit():
            if (not refName in self.refNames and
                    not refName in self.fullRefNames):
                # we need the real refName, which may be hidden behind a
                # mapping to resolve duplicate refIds between resources...
                refName = self._idToRname(int(refName))
        return refName

    def readsInRange(self, refName, start, end, buffsize=50, usePbi=True,
                     longest=False, sampleSize=0, justIndices=False):
        """A generator of (usually) BamAlignment objects for the reads in one
        or more Bam files pointed to by the ExternalResources in this DataSet
        that have at least one coordinate within the specified range in the
        reference genome.

        Rather than developing some convoluted approach for dealing with
        auto-inferring the desired references, this method and self.refNames
        should allow users to compose the desired query.

        Args:
            :refName: the name of the reference that we are sampling
            :start: the start of the range (inclusive, index relative to \
                    reference)
            :end: the end of the range (inclusive, index relative to reference)

        Yields:
            BamAlignment objects

        Doctest:
            >>> import pbcore.data.datasets as data
            >>> from pbcore.io import AlignmentSet
            >>> ds = AlignmentSet(data.getBam())
            >>> for read in ds.readsInRange(ds.refNames[15], 100, 150):
            ...     print 'hn: %i' % read.holeNumber # doctest:+ELLIPSIS
            hn: ...

        """
        refName = self.guaranteeName(refName)

        # correct the cmp.h5 reference names before reads go out the door
        if self.isCmpH5:
            for res in self.resourceReaders():
                for row in res.referenceInfoTable:
                    row.FullName = self._cleanCmpName(row.FullName)

        if justIndices:
            return self._indexReadsInRange(refName, start, end,
                                           justIndices=True)
        else:
            return (read for read in self._readsInRange(refName, start, end,
                                                        buffsize, usePbi,
                                                        longest, sampleSize))

    @filtered
    def _readsInRange(self, refName, start, end, buffsize=50, usePbi=True,
                      longest=False, sampleSize=0):

        if self.hasPbi and usePbi:
            for rec in self._pbiReadsInRange(refName, start, end,
                                             longest=longest,
                                             sampleSize=sampleSize):
                yield rec
            raise StopIteration

        # merge sort before yield
        if self.numExternalResources > 1:
            if buffsize > 1:
                # create read/reader caches
                read_its = [iter(rr.readsInRange(refName, start, end))
                            for rr in self.resourceReaders()]
                deep_buf = [[next(it, None) for _ in range(buffsize)]
                            for it in read_its]

                # remove empty iterators
                read_its = [it for it, cur in zip(read_its, deep_buf)
                            if cur[0]]
                deep_buf = [buf for buf in deep_buf if buf[0]]

                # populate starting values/scratch caches
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

    @property
    def tId(self):
        if self.isCmpH5:
            return self.index.RefGroupID
        return self.index.tId

    @property
    def mapQV(self):
        if self.isCmpH5:
            return self.index.MapQV
        return self.index.mapQV

    @property
    def isSorted(self):
        return self._checkIdentical('isSorted')

    @property
    def tStart(self):
        return self._checkIdentical('tStart')

    @property
    def tEnd(self):
        return self._checkIdentical('tEnd')

    @property
    def _length(self):
        """Used to populate metadata in updateCounts. We're using the pbi here,
        which is necessary and sufficient for both subreadsets and
        alignmentsets, but doesn't work for hdfsubreadsets. Rather than
        duplicate code, we'll implement the hdf specific _length as an
        overriding function where needed.

        ..note:: Both mapped and unmapped bams can be either indexed or
                 unindexed. This makes life more difficult, but we should
                 expect a pbi for both subreadsets and alignmentsets

        """
        count = len(self.index)
        length = 0
        if count:
            if self.isCmpH5:
                length = sum(self.index.rEnd - self.index.rStart)
            else:
                try:
                    length = sum(self.index.aEnd - self.index.aStart)
                except AttributeError:
                    # If the bam is empty or the file is not actually aligned,
                    # this field wont be populated
                    if self.isMapped:
                        log.debug(".pbi mapping columns missing from mapped "
                                  "bam, bam may be empty")
                    else:
                        log.warn("File not actually mapped!")
                    length = 0
        return count, length

    @property
    def _referenceFile(self):
        responses = [res.reference for res in self.externalResources]
        return self._unifyResponses(responses)

    @property
    def recordsByReference(self):
        """The records in this AlignmentSet, sorted by tStart."""
        # we only care about aligned sequences here, so we can make this a
        # chain of readsInReferences to add pre-filtering by rname, instead of
        # going through every record and performing downstream filtering.
        # This will make certain operations, like len(), potentially faster
        for rname in self.refNames:
            for read in self.readsInReference(rname):
                yield read

    def referenceInfo(self, refName):
        """Select a row from the DataSet.referenceInfoTable using the reference
        name as a unique key (or ID, if you really have to)"""

        # Convert it to a name if you have to:
        if not isinstance(refName, str):
            refName = str(refName)
        if refName.isdigit():
            if not refName in self.refNames:
                refName = self._idToRname(int(refName))

        tbr = self.referenceInfoTable[
            self.referenceInfoTable['Name'] == refName]
        if len(tbr) > 1:
            log.info("Duplicate reference names detected")
        elif len(tbr) == 1:
            return tbr[0]
        else:
            log.debug("No reference found by that Name or ID")

    @property
    def referenceInfoTable(self):
        """The merged reference info tables from the external resources.
        Record.ID is remapped to a unique integer key (though using record.Name
        is preferred). Record.Names are remapped for cmp.h5 files to be
        consistent with bam files.

        ..note:: Reference names are assumed to be unique

        """
        if self._referenceInfoTable is None:
            self._referenceInfoTableIsStacked = False
            responses = []

            # allow for merge here:
            for res in self._pollResources(lambda x: x.referenceInfoTable):
                if not res is None:
                    if self.isCmpH5:
                        for rec in res:
                            rec.StartRow = 0
                            rec.EndRow = 0
                    responses.append(res)
            table = []
            if len(responses) > 1:
                # perhaps this can be removed someday so that cmpH5 references
                # are 0-indexed even if only one exists
                try:
                    # this works even for cmp's, because we overwrite the
                    # highly variable fields above
                    table = self._unifyResponses(
                        responses,
                        eqFunc=np.array_equal)
                except ResourceMismatchError:
                    table = np.concatenate(responses)
                    table = np.unique(table)
                    for i, rec in enumerate(table):
                        rec.ID = i
                        rec.RefInfoID = i
                    self._referenceInfoTableIsStacked = True
            elif len(responses) == 1:
                table = responses[0]
            else:
                raise InvalidDataSetIOError("No reference tables found, "
                                            "are these input files aligned?")
            if self.isCmpH5:
                for rec in table:
                    rec.Name = self._cleanCmpName(rec.FullName)
            log.debug("Filtering reference entries")
            if not self.noFiltering and self._filters:
                passes = self._filters.testField('rname', table['Name'])
                table = table[passes]
            self._referenceInfoTable = table
            #TODO: Turn on when needed (expensive)
            #self._referenceDict.update(zip(self.refIds.values(),
            #                               self._referenceInfoTable))
        return self._referenceInfoTable

    @property
    def _stackedReferenceInfoTable(self):
        if self._referenceInfoTableIsStacked is None:
            _ = self.referenceInfoTable
        return self._referenceInfoTableIsStacked

    @property
    def _referenceIdMap(self):
        """Map the dataset shifted refIds to the [resource, refId] they came
        from.

        """
        if self.__referenceIdMap is None:
            self.__referenceIdMap = {ref.ID: ref.Name
                                     for ref in self.referenceInfoTable}
        return self.__referenceIdMap

    def _cleanCmpName(self, name):
        return splitFastaHeader(name)[0]

    @property
    def refLengths(self):
        """A dict of refName: refLength"""
        return {name: length for name, length in self.refInfo('Length')}

    @property
    def refIds(self):
        """A dict of refName: refId for the joined referenceInfoTable"""
        return {name: rId for name, rId in self.refInfo('ID')}

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
        """Return a column in the referenceInfoTable, tupled with the reference
        name. TODO(mdsmith)(2016-01-27): pick a better name for this method...

        """
        return zip(self.referenceInfoTable['Name'],
                   self.referenceInfoTable[key])

    def _idToRname(self, rId):
        """Map the DataSet.referenceInfoTable.ID to the superior unique
        reference identifier: referenceInfoTable.Name

        Args:
            :rId: The DataSet.referenceInfoTable.ID of interest

        Returns:
            The referenceInfoTable.Name corresponding to rId

        """
        return self._referenceIdMap[rId]

    @staticmethod
    def _metaTypeMapping():
        # This doesn't work for scraps.bam, whenever that is implemented
        return {'bam':'PacBio.AlignmentFile.AlignmentBamFile',
                'bai':'PacBio.Index.BamIndex',
                'pbi':'PacBio.Index.PacBioIndex',
                'cmp.h5':'PacBio.AlignmentFile.AlignmentCmpH5File',
               }


class ConsensusReadSet(ReadSet):
    """DataSet type specific to CCSreads. No type specific Metadata exists, so
    the base class version is OK (this just ensures type representation on
    output and expandability

    Doctest:
        >>> import pbcore.data.datasets as data
        >>> from pbcore.io import ConsensusReadSet
        >>> ds2 = ConsensusReadSet(data.getXml(2), strict=False,
        ...                        skipMissing=True)
        >>> ds2 # doctest:+ELLIPSIS
        <ConsensusReadSet...
        >>> ds2._metadata # doctest:+ELLIPSIS
        <SubreadSetMetadata...
    """

    datasetType = DataSetMetaTypes.CCS

    @staticmethod
    def _metaTypeMapping():
        # This doesn't work for scraps.bam, whenever that is implemented
        return {'bam':'PacBio.ConsensusReadFile.ConsensusReadBamFile',
                'bai':'PacBio.Index.BamIndex',
                'pbi':'PacBio.Index.PacBioIndex',
                }


class ConsensusAlignmentSet(AlignmentSet):
    """
    Dataset type for aligned CCS reads.  Essentially identical to AlignmentSet
    aside from the contents of the underlying BAM files.
    """
    datasetType = DataSetMetaTypes.CCS_ALIGNMENT

    @staticmethod
    def _metaTypeMapping():
        # This doesn't work for scraps.bam, whenever that is implemented
        return {'bam':'PacBio.ConsensusReadFile.ConsensusReadBamFile',
                'bai':'PacBio.Index.BamIndex',
                'pbi':'PacBio.Index.PacBioIndex',
                }


class ContigSet(DataSet):
    """DataSet type specific to Contigs"""

    datasetType = DataSetMetaTypes.CONTIG

    def __init__(self, *files, **kwargs):
        self._fastq = False
        super(ContigSet, self).__init__(*files, **kwargs)
        # weaken by permitting failure to allow BarcodeSet to have own
        # Metadata type
        try:
            self._metadata = ContigSetMetadata(self._metadata)
            self._updateMetadata()
        except TypeError:
            pass

    def split(self, nchunks):
        log.debug("Getting and dividing contig id's")
        keys = self.index.id
        chunks = divideKeys(keys, nchunks)
        log.debug("Creating copies of the dataset")
        results = [self.copy() for _ in range(nchunks)]
        log.debug("Applying filters and updating counts")
        for chunk, res in zip(chunks, results):
            res._filters.addRequirement(id=[('=', n) for n in chunk])
            res.newUuid()
            log.debug("Updating new res counts:")
            res.updateCounts()
        return results

    def consolidate(self, outfn=None, numFiles=1, useTmp=False):
        """Consolidation should be implemented for window text in names and
        for filters in ContigSets"""

        if numFiles != 1:
            raise NotImplementedError(
                "Only one output file implemented so far.")

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
        if self._filters and not self.noFiltering:
            writeTemp = True
        writeMatches = {}
        writeComments = {}
        writeQualities = {}
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
                new_seq = ''.join([match.sequence[:] for match in match_list])
                if self._fastq:
                    new_qual = ''.join([match.qualityString for match in
                                        match_list])
                    writeQualities[new_name] = new_qual

                # set to write
                writeTemp = True
                writeMatches[new_name] = new_seq
                writeComments[new_name] = match_list[0].comment
            else:
                log.debug("One match found for {i}".format(i=name))
                writeMatches[name] = match_list[0].sequence[:]
                writeComments[name] = match_list[0].comment
                if self._fastq:
                    writeQualities[name] = match_list[0].qualityString
        if writeTemp:
            log.debug("Writing a new file is necessary")
            if not outfn:
                log.debug("Writing to a temp directory as no path given")
                outdir = tempfile.mkdtemp(suffix="consolidated-contigset")
                if self._fastq:
                    outfn = os.path.join(outdir,
                                         'consolidated_contigs.fastq')
                else:
                    outfn = os.path.join(outdir,
                                         'consolidated_contigs.fasta')
            with self._writer(outfn) as outfile:
                log.debug("Writing new resource {o}".format(o=outfn))
                for name, seq in writeMatches.items():
                    name_key = name
                    if writeComments[name]:
                        name = ' '.join([name, writeComments[name]])
                    if self._fastq:
                        outfile.writeRecord(
                            name, seq, qvsFromAscii(writeQualities[name_key]))
                    else:
                        outfile.writeRecord(name, seq)
            if not self._fastq:
                _indexFasta(outfn)
            # replace resources
            log.debug("Replacing resources")
            self.externalResources = ExternalResources()
            self.addExternalResources([outfn])
            self._index = None
            self._indexMap = None
            self._openReaders = []
            self._populateMetaTypes()
            self.updateCounts()

            # replace contig info
            if not self._fastq:
                log.debug("Replacing metadata")
                self._metadata.contigs = []
                self._populateContigMetadata()
        self._populateMetaTypes()

    @property
    def _writer(self):
        if self._fastq:
            return FastqWriter
        return FastaWriter

    def _popSuffix(self, name):
        """Chunking and quivering adds suffixes to contig names, after the
        normal ID and window. This complicates our dewindowing and
        consolidation, so we'll remove them for now"""
        observedSuffixes = ['|quiver', '|plurality', '|arrow', '|poa']
        for suff in observedSuffixes:
            if name.endswith(suff):
                log.debug("Suffix found: {s}".format(s=suff))
                return name.replace(suff, ''), suff
        return name, ''

    def _removeWindow(self, name):
        """Chunking and quivering appends a window to the contig ID, which
        allows us to consolidate the contig chunks but also gets in the way of
        contig identification by ID. Remove it temporarily"""
        if isinstance(self._parseWindow(name), np.ndarray):
            name, suff = self._popSuffix(name)
            return '_'.join(name.split('_')[:-2]) + suff
        return name

    def induceIndices(self):
        if not self.isIndexed:
            for extRes in self.externalResources:
                extRes.addIndices([_indexFasta(extRes.resourceId)])
            self.close()
        self._populateMetaTypes()
        self.updateCounts()

    def _parseWindow(self, name):
        """Chunking and quivering appends a window to the contig ID, which
        allows us to consolidate the contig chunks."""
        name, _ = self._popSuffix(name)
        if re.search("_\d+_\d+$", name) is None:
            return None
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
        log.debug("Adding contig metadata...")
        numrec = 0
        totlen = 0
        for contig in self.contigs:
            self._metadata.addContig(contig)
            numrec += 1
            totlen += len(contig)
        if not self._countsUpdated:
            log.debug("Counts updated: numrec={n} totlen={l}".format(n=numrec,
                                                                     l=totlen))
            self.numRecords = numrec
            self.totalLength = totlen
            self._countsUpdated = True

    def updateCounts(self):
        if self._skipCounts:
            if not self.metadata.totalLength:
                self.metadata.totalLength = -1
            if not self.metadata.numRecords:
                self.metadata.numRecords = -1
            return
        if not self.isIndexed:
            if (not self.totalLength and not self.numRecords and not
                    self._countsUpdated):
                log.info("Cannot updateCounts without an index file")
                self.metadata.totalLength = 0
                self.metadata.numRecords = 0
            return
        try:
            log.debug('Updating counts')
            self.metadata.totalLength = sum(self.index.length)
            self.metadata.numRecords = len(self.index)
            self._countsUpdated = True
        except (IOError, UnavailableFeature, TypeError):
            # IOError for missing files
            # UnavailableFeature for files without companion files
            # TypeError for FastaReader, which doesn't have a len()
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
                self.metadata.contigs.extend(newMetadata.contigs)

    @property
    def metadata(self):
        if not isinstance(self._metadata, ContigSetMetadata):
           self._metadata = ContigSetMetadata(self._metadata)
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        if not isinstance(value, ContigSetMetadata):
            value = ContigSetMetadata(value)
        self._metadata = value

    def _openFiles(self):
        """Open the files (assert they exist, assert they are of the proper
        type before accessing any file)
        """
        if self._openReaders:
            log.debug("Closing old {t} readers".format(
                t=self.__class__.__name__))
            self.close()
        log.debug("Opening {t} resources".format(
            t=self.__class__.__name__))
        for extRes in self.externalResources:
            resource = self._openFile(urlparse(extRes.resourceId).path)
            if resource is not None:
                self._openReaders.append(resource)
        if len(self._openReaders) == 0 and len(self.toExternalFiles()) != 0:
            raise IOError("No files were openable")
        log.debug("Done opening {t} resources".format(
            t=self.__class__.__name__))

    def _openFile(self, location):
        resource = None
        if location.endswith("fastq"):
            self._fastq = True
            resource = FastqReader(location)
        else:
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
            except ValueError:
                log.debug("Fasta file is empty")
                # this seems to work for an emtpy fasta, interesting:
                resource = FastaReader(location)
                # we know this file is empty
                self._skipCounts = True
                self.metadata.totalLength = 0
                self.metadata.numRecords = 0
        return resource

    def resourceReaders(self, refName=None):
        """A generator of fastaReader objects for the ExternalResources in this
        ReferenceSet.

        Yields:
            An open fasta file

        """
        if refName:
            log.error("Specifying a contig name not yet implemented")
        if not self._openReaders:
            self._openFiles()
        else:
            for reader in self._openReaders:
                if isinstance(reader, (FastaReader, FastqReader)):
                    reader.file = open(reader.filename, "r")
        return self._openReaders

    @property
    @filtered
    def contigs(self):
        """A generator of contigs from the fastaReader objects for the
        ExternalResources in this ReferenceSet.

        Yields:
            A fasta file entry

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
        try:
            self._assertIndexed(IndexedFastaReader)
        except IOError:
            raise IOError("Companion FASTA index (.fai) file not found or "
                          "malformatted! Use 'samtools faidx' to generate "
                          "FASTA index.")
        return True

    @property
    def isIndexed(self):
        try:
            res = self._pollResources(
                lambda x: isinstance(x, IndexedFastaReader))
            return self._unifyResponses(res)
        except ResourceMismatchError:
            if not self._strict:
                log.info("Not all resource are equally indexed.")
                return False
            else:
                raise
        except IndexError:
            if not self._strict:
                log.info("No resource readers!")
                return False
            else:
                raise InvalidDataSetIOError("No openable resources!")

    @property
    def contigNames(self):
        """The names assigned to the External Resources, or contigs if no name
        assigned."""
        # TODO{mdsmith}{3/10/2016} Make this faster by using (optionally) the
        # index file
        names = []
        for contig in self.contigs:
            if self.noFiltering:
                names.append(contig.id)
            elif self._filters.testParam('id', contig.id, str):
                names.append(contig.id)
        return sorted(list(set(names)))

    @staticmethod
    def _metaTypeMapping():
        return {'fasta':'PacBio.ContigFile.ContigFastaFile',
                'fastq':'PacBio.ContigFile.ContigFastqFile',
                'fa':'PacBio.ContigFile.ContigFastaFile',
                'fas':'PacBio.ContigFile.ContigFastaFile',
                'fai':'PacBio.Index.SamIndex',
                'contig.index':'PacBio.Index.FastaContigIndex',
                'index':'PacBio.Index.Indexer',
                'sa':'PacBio.Index.SaWriterIndex',
               }

    def _indexRecords(self):
        """Returns index records summarizing all of the records in all of
        the resources that conform to those filters addressing parameters
        cached in the pbi.

        """
        recArrays = []
        _indexMap = []
        for rrNum, rr in enumerate(self.resourceReaders()):
            indices = rr.fai
            if len(indices) == 0:
                continue
            # have to manually specify the dtype to make it work like a pbi
            indices = np.rec.fromrecords(
                indices,
                dtype=[('id', 'O'), ('comment', 'O'), ('header', 'O'),
                       ('length', '<i8'), ('offset', '<i8'),
                       ('lineWidth', '<i8'), ('stride', '<i8')])

            if not self._filters or self.noFiltering:
                recArrays.append(indices)
                _indexMap.extend([(rrNum, i) for i in
                                  range(len(indices))])
            else:
                # Filtration will be necessary:
                # dummy map, the id is the name in fasta space
                nameMap = {name: name for name in indices.id}

                passes = self._filters.filterIndexRecords(indices, nameMap, {},
                                                          readType='fasta')
                newInds = indices[passes]
                recArrays.append(newInds)
                _indexMap.extend([(rrNum, i) for i in
                                  np.flatnonzero(passes)])
        self._indexMap = np.array(_indexMap, dtype=[('reader', 'uint64'),
                                                    ('index', 'uint64')])
        if len(recArrays) == 0:
            recArrays = [np.array(
                [],
                dtype=[('id', 'O'), ('comment', 'O'), ('header', 'O'),
                       ('length', '<i8'), ('offset', '<i8'),
                       ('lineWidth', '<i8'), ('stride', '<i8')])]
        return _stackRecArrays(recArrays)

    def _filterType(self):
        return 'fasta'


class ReferenceSet(ContigSet):
    """DataSet type specific to References"""

    datasetType = DataSetMetaTypes.REFERENCE

    def __init__(self, *files, **kwargs):
        super(ReferenceSet, self).__init__(*files, **kwargs)

    @property
    def refNames(self):
        """The reference names assigned to the External Resources, or contigs
        if no name assigned."""
        return self.contigNames

    @staticmethod
    def _metaTypeMapping():
        return {'fasta':'PacBio.ContigFile.ContigFastaFile',
                'fa':'PacBio.ContigFile.ContigFastaFile',
                'fas':'PacBio.ContigFile.ContigFastaFile',
                'fai':'PacBio.Index.SamIndex',
                'contig.index':'PacBio.Index.FastaContigIndex',
                'index':'PacBio.Index.Indexer',
                'sa':'PacBio.Index.SaWriterIndex',
               }


class BarcodeSet(ContigSet):
    """DataSet type specific to Barcodes"""

    datasetType = DataSetMetaTypes.BARCODE

    def __init__(self, *files, **kwargs):
        super(BarcodeSet, self).__init__(*files, **kwargs)
        self._metadata = BarcodeSetMetadata(self._metadata.record)
        self._updateMetadata()

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

    @property
    def metadata(self):
        if not isinstance(self._metadata, BarcodeSetMetadata):
           self._metadata = BarcodeSetMetadata(self._metadata)
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        if not isinstance(value, BarcodeSetMetadata):
            value = BarcodeSetMetadata(value)
        self._metadata = value

    def _updateMetadata(self):
        # update barcode specific metadata:
        if not self._metadata.barcodeConstruction:
            self._metadata.barcodeConstruction = ''


    @staticmethod
    def _metaTypeMapping():
        return {'fasta':'PacBio.BarcodeFile.BarcodeFastaFile',
                'fai':'PacBio.Index.SamIndex',
                'sa':'PacBio.Index.SaWriterIndex',
               }


