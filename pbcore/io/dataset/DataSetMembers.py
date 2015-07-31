"""DataSetMetadata (also the tag of the Element in the DataSet XML
representation) is somewhat challening to store, access, and (de)serialize
efficiently. Here, we maintain a bulk representation of all of the dataset
metadata (or any other XML data, like ExternalResources) found in the XML file
in the following data structure:

    An Element is a turned into a dictionary:
        XmlElement => {'tag': 'ElementTag',
                       'text': 'ElementText',
                       'attrib': {'ElementAttributeName': 'AttributeValue',
                                  'AnotherAttrName': 'AnotherAttrValue'},
                       'children': [XmlElementDict,
                                    XmlElementDictWithSameOrDifferentTag]}

    Child elements are represented similarly and stored (recursively) as a list
    in 'children'. The top level we store for DataSetMetadata is just a list,
    which can be thought of as the list of children of a different element
    (say, a DataSet or SubreadSet element, if we stored that):
        DataSetMetadata = [XmlTag, XmlTagWithSameOrDifferentTag]

We keep this for two reasons:
    1. We don't want to have to write a lot of logic to go from XML to an
       internal representation and then back to XML.
    2. We want to be able to store and at least write metadata that doesn't yet
       exist, even if we can't merge it intelligently.
    3. Keeping and manipulating a dictionary is ~10x faster than an
       OrderedAttrDict, and probably faster to use than a full stack of
       objects.

Instead, we keep and modify this list:dictionary structure, wrapping it in
classes as necessary. The classes and methods that wrap this datastructure
serve two pruposes:
    1. Provide an interface for our code (and making merging clean) e.g.:
        - DataSet("test.xml").metadata.numRecords += 1
    2. Provide an interface for users of the DataSet API, e.g.:
        - numRecords = DataSet("test.xml").metadata.numRecords
        - bioSamplePointer = (DataSet("test.xml")
                                .metadata.collections[0]
                                .wellSample.bioSamplePointers[0])
        a. Though users can still access novel metadata types the hard way
           e.g.:
            - bioSamplePointer = (DataSet("test.xml")
                                    .metadata.collections[0]
                                    ['WellSample']['BioSamplePointers']
                                    ['BioSamplePointer'].record['text'])
            note: Assuming __getitem__ is implemented for the 'children' list
"""

import copy
import operator as OP
import re
import numpy as np
import logging
from functools import partial as P

log = logging.getLogger(__name__)

class RecordWrapper(object):
    """The base functionality of a metadata element.

    Many of the methods here are intended for use with children of
    RecordWrapper (e.g. append, extend). Methods in child classes often provide
    similar functionality for more raw inputs (e.g. resourceIds as strings)"""


    def __init__(self, record=None):
        """Here, record is any element in the Metadata Element tree and a
        dictionary with four members: 'tag', 'attrib', 'text', and 'children'.

        Do not deepcopy, we rely on side effects for all persistent
        modifications.
        """
        if record:
            try:
                self.record = record.record
            except AttributeError:
                self.record = record
        else:
            self.record = _emptyMember()
        assert 'tag' in self.record.keys()

    def __len__(self):
        """Return the number of children in this node"""
        return len(self.record['children'])

    def __nonzero__(self):
        if self.record['tag'] != '':
            return True
        if self.record['text'] != '':
            return True
        if self.record['attrib'] != {}:
            return True
        if self.record['children'] != []:
            return True
        return False

    def __deepcopy__(self, memo):
        tbr = type(self)()
        memo[id(self)] = tbr
        tbr.record = copy.deepcopy(self.record, memo)
        return tbr

    def __getitem__(self, tag):
        """Try to get the a specific child (only useful in simple cases where
        children will not be wrapped in a special wrapper object, returns the
        first instance of 'tag')"""
        if isinstance(tag, str):
            return RecordWrapper(self.getV('children', tag))
        elif isinstance(tag, int):
            return RecordWrapper(self.record['children'][tag])

    def __iter__(self):
        """Get each child iteratively (only useful in simple cases where
        children will not be wrapped in a special wrapper object)"""
        for child in self.record['children']:
            yield RecordWrapper(child)
            #yield child['text']

    def __repr__(self):
        """Return a pretty string represenation of this object:

            "<type tag text attribs children>"
        """
        c_tags = [c.record['tag'] for c in self]
        repr_d = dict(k=self.__class__.__name__, t=self.record['tag'],
                      x=self.record['text'], a=self.record['attrib'],
                      c=c_tags)
        rep = '<{k} tag:{t} text:{x} attribs:{a} children:{c}>'.format(
            **repr_d)
        return rep

    def pop(self, index):
        return self.record['children'].pop(index)

    def merge(self, other):
        pass

    def getMemberV(self, tag, container='text'):
        """Generic accessor for the contents of the children of this element,
        without having to interface with them directly"""
        try:
            return self.record['children'][self.index(str(tag))][
                str(container)]
        except KeyError:
            return None

    def setMemberV(self, tag, value, container='text'):
        """Generic accessor for the contents of the children of this element,
        without having to interface with them directly"""
        try:
            self.record['children'][self.index(str(tag))][str(container)] = (
                str(value))
        except ValueError:
            if container == 'text':
                newMember = _emptyMember(tag=tag, text=value)
                self.append(newMember)
            else:
                raise
        return self

    def getV(self, container='text', tag=None):
        """Generic accessor for the contents of this element's 'attrib' or
        'text' fields"""
        try:
            if container == 'children':
                return self.record['children'][self.index(str(tag))]
            if tag:
                return self.record[str(container)][tag]
            else:
                return self.record[str(container)]
        except (KeyError, ValueError):
            return None

    def setV(self, value, container='text', tag=None):
        """Generic accessor for the contents of this element's 'attrib' or
        'text' fields"""
        if tag:
            self.record[str(container)][tag] = value
        else:
            self.record[str(container)] = value
        return self

    def extend(self, newMembers):
        """Extend the actual list of child elements"""
        newMembers = [nM.record if isinstance(nM, RecordWrapper) else nM
                      for nM in newMembers]
        self.record['children'].extend(newMembers)

    def append(self, newMember):
        """Append to the actual list of child elements"""
        if isinstance(newMember, RecordWrapper):
            self.record['children'].append(newMember.record)
        else:
            self.record['children'].append(newMember)

    def index(self, tag):
        """Return the index in 'children' list of item with 'tag' member"""
        return self.tags.index(tag)

    @property
    def tags(self):
        """Return the list of tags for children in this element"""
        return [child['tag'] for child in self.record['children']]

    @property
    def metaname(self):
        """Cleaner accessor for this node's tag"""
        return self.record['tag']

    @metaname.setter
    def metaname(self, value):
        """Cleaner accessor for this node's tag"""
        self.record['tag'] = value

    @property
    def metavalue(self):
        """Cleaner accessor for this node's text"""
        return self.record['text']

    @metavalue.setter
    def metavalue(self, value):
        """Cleaner accessor for this node's text"""
        self.record['text'] = value

    @property
    def metadata(self):
        """Cleaner accessor for this node's attributes. Returns mutable,
        doesn't need setter"""
        return self.record['attrib']

    def addMetadata(self, key, value):
        """Add a key, value pair to this metadata object (attributes)"""
        self.metadata[key] = value

    @property
    def submetadata(self):
        """Cleaner accessor for wrapped versions of this node's children."""
        return [RecordWrapper(child) for child in self.record['children']]

    @property
    def subrecords(self):
        """Cleaner accessor for this node's children. Returns mutable, doesn't
        need setter"""
        return self.record['children']

    def findChildren(self, tag):
        for child in self.submetadata:
            if child.metaname == tag:
                yield child

    def removeChildren(self, tag):
        keepers = []
        for child in self.record['children']:
            if child['tag'] != tag:
                keepers.append(child)
        self.record['children'] = keepers

    def pruneChildrenTo(self, whitelist):
        newChildren = []
        oldChildren = self.record['children']
        for child in oldChildren:
            if child['tag'] in whitelist:
                newChildren.append(child)
        self.record['children'] = newChildren

    # Some common attributes (to reduce code duplication):

    @property
    def name(self):
        return self.getV('attrib', 'Name')

    @name.setter
    def name(self, value):
        self.setV(value, 'attrib', 'Name')

    @property
    def value(self):
        return self.getV('attrib', 'Value')

    @value.setter
    def value(self, value):
        self.setV(value, 'attrib', 'Value')

    @property
    def version(self):
        return self.getV('attrib', 'Version')

    @property
    def description(self):
        return self.getV('attrib', 'Description')

    @description.setter
    def description(self, value):
        return self.setV(value, 'attrib', 'Description')

def filter_read(accessor, operator, value, read):
    return operator(accessor(read), value)


class Filters(RecordWrapper):

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__
        self._callbacks = []

    def registerCallback(self, func):
        if func not in self._callbacks:
            self._callbacks.append(func)

    def _runCallbacks(self):
        for func in self._callbacks:
            func()

    def __getitem__(self, index):
        return Filter(self.record['children'][index])

    def __iter__(self):
        for child in self.record['children']:
            yield Filter(child)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        if len(self) == 0:
            return True
        return all([sFilt == oFilt for sFilt, oFilt in zip(
            sorted(list(self)),
            sorted(list(other)))])

    def __nonzero__(self):
        for filt in self:
            for req in filt:
                if req.name:
                    return True
        return False

    def __str__(self):
        buff = []
        for filt in self:
            temp = ['(']
            for req in filt:
                temp.append(' '.join([req.name, req.operator, req.value]))
                temp.append('AND')
            if temp:
                temp.pop()
                temp.append(')')
                buff.extend(temp)
                buff.append('OR')
        if buff:
            if buff[-1] == 'OR':
                buff.pop()

        return ' '.join(buff)

    def testCompatibility(self, other):
        if self == other:
            return True
        else:
            return False

    def merge(self, other):
        # Just add it to the or list
        self.extend(Filters(other).submetadata)

    def testParam(self, param, value, testType=str, oper='='):
        options = [True] * len(list(self))
        if not options:
            return True
        for i, filt in enumerate(self):
            for req in filt:
                if req.name == param:
                    if not self.opMap(oper)(testType(req.value),
                                            testType(value)):
                        options[i] = False
        return any(options)

    def opMap(self, op):
        ops = {'>=': OP.le,
               '&gt;=': OP.le,
               '<=': OP.ge,
               '&lt;=': OP.ge,
               '==': OP.eq,
               '!=': OP.ne,
               '=': OP.eq,
               '>': OP.gt,
               '&gt;': OP.gt,
               '<': OP.lt,
               '&lt;': OP.lt,
              }
        return ops[op]

    @property
    def _bamAccMap(self):
        # tStart/tEnd is a hack for overlapping ranges. you're not testing
        # whether the tStart/tEnd is within a range, you're testing if it
        # overlaps with the tStart/tEnd in the filter (overlaps with a
        # reference window)
        return {'rname': (lambda x: x.referenceName),
                'length': (lambda x: int(x.readLength)),
                'qname': (lambda x: x.qNameA),
                'zm': (lambda x: int(x.HoleNumber)),
                'bc': (lambda x: x.barcode),
                'qs': (lambda x: int(x.qStart)),
                'rq': (lambda x: int(x.MapQV)),
                'pos': (lambda x: int(x.tStart)),
                'accuracy': (lambda x: int(x.identity)),
                'readstart': (lambda x: int(x.aStart)),
                'tstart': (lambda x: int(x.tEnd)), # see above
                'tend': (lambda x: int(x.tStart)), # see above
               }

    def _pbiAccMap(self, tIdMap):
        # tStart/tEnd is a hack for overlapping ranges. you're not testing
        # whether the tStart/tEnd is within a range, you're testing if it
        # overlaps with the tStart/tEnd in the filter (overlaps with a
        # reference window)
        return {'rname': (lambda x, m=tIdMap: m[x.tId]),
                'length': (lambda x: int(x.aEnd)-int(x.aStart)),
                'qname': (lambda x: x.qId),
                'zm': (lambda x: int(x.holeNumber)),
                'pos': (lambda x: int(x.tStart)),
                'readstart': (lambda x: int(x.aStart)),
                'tstart': (lambda x: int(x.tEnd)), # see above
                'tend': (lambda x: int(x.tStart)), # see above
               }

    @property
    def _bamTypeMap(self):
        return {'rname': str,
                'length': int,
                'qname': str,
                'zm': int,
                'bc': str,
                'qs': int,
                'rq': float,
                'pos': int,
                'tstart': int,
                'tend': int,
                'accuracy': int,
                'readstart': int,
               }

    def tests(self, readType="bam", tIdMap=None):
        # Allows us to not process all of the filters each time. This is marked
        # as dirty (= []) by addFilters etc. Filtration can be turned off by
        # setting this to [lambda x: True], which can be reversed by marking
        # the cache dirty see disableFilters/enableFilters
        if readType.lower() == "bam":
            accMap = self._bamAccMap
            typeMap = self._bamTypeMap
        elif readType.lower() == "fasta":
            accMap = {'id': (lambda x: x.id),
                      'length': (lambda x: int(x.length)),
                     }
            typeMap = {'id': str,
                       'length': int,
                      }
        elif readType.lower() == "pbi":
            accMap = self._pbiAccMap(tIdMap)
            typeMap = self._bamTypeMap
        else:
            raise TypeError("Read type not properly specified")
        tests = []
        for filt in self:
            reqTests = []
            for req in filt:
                param = req.name
                value = typeMap[param](req.value)
                operator = self.opMap(req.operator)
                reqTests.append(P(filter_read, accMap[param], operator, value))
            tests.append(
                lambda x, reqTests=reqTests: all([f(x) for f in reqTests]))
        return tests

    def filterIndexRecords(self, indexRecords, nameMap):
        filterResultList = []
        typeMap = self._bamTypeMap
        accMap = self._pbiAccMap({})
        accMap['rname'] = lambda x: x.tId
        for filt in self:
            thisFilterResultList = []
            for req in filt:
                param = req.name
                value = typeMap[param](req.value)
                value = nameMap[value]
                operator = self.opMap(req.operator)
                reqResultsForRecords = operator(accMap[param](indexRecords),
                                                value)
                thisFilterResultList.append(reqResultsForRecords)
            thisFilterResultList = np.logical_and.reduce(thisFilterResultList)
            filterResultList.append(thisFilterResultList)
        filterResultList = np.logical_or.reduce(filterResultList)
        return filterResultList

    def addRequirement(self, **kwargs):
        """Use this to add requirements. Members of the list will be considered
        options for fulfilling this requirement, all other filters will be
        duplicated for each option. Use multiple calls to add multiple
        requirements to the existing filters. Use removeRequirement first to
        not add conflicting filters.

        Args:
            name: The name of the requirement, e.g. 'rq'
            options: A list of (operator, value) tuples, e.g. ('>', '0.85')
        """
        # if there are already filters, you must copy the filters for each new
        # option and add one set of requirements to each option:
        if self.submetadata:
            origFilts = copy.deepcopy(list(self))
            self.record['children'] = []
            newFilts = [copy.deepcopy(origFilts) for _ in kwargs.values()[0]]
            for name, options in kwargs.items():
                for i, (oper, val) in enumerate(options):
                    for filt in newFilts[i]:
                        filt.addRequirement(name, oper, val)
            for filtList in newFilts:
                self.extend(filtList)
        else:
            newFilts = [Filter() for _ in kwargs.values()[0]]
            for name, options in kwargs.items():
                for i, (oper, val) in enumerate(options):
                    newFilts[i].addRequirement(name, oper, val)
            self.extend(newFilts)
        self._runCallbacks()

    def removeRequirement(self, req):
        log.debug("Removing requirement {r}".format(r=req))
        for i, filt in enumerate(self):
            empty = filt.removeRequirement(req)
            if empty:
                self.pop(i)
        self._runCallbacks()


class Filter(RecordWrapper):

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

    def __getitem__(self, index):
        return self.plist[index]

    def __iter__(self):
        for param in self.plist:
            yield param

    def __eq__(self, other):
        return (sorted([str(p) for p in self]) ==
                sorted([str(p) for p in other]))

    def __lt__(self, other):
        return sorted([p.name for p in self]) < sorted([p.name for p in other])

    def pop(self, index):
        self.record['children'][0]['children'].pop(index)

    def addRequirement(self, name, operator, value):
        param = Parameter()
        param.name = name
        param.operator = operator
        param.value = value
        self.plist.append(param)

    def removeRequirement(self, req):
        for i, param in enumerate(self):
            if param.name == req:
                self.pop(i)
        if len(self.plist):
            return False
        else:
            return True

    @property
    def plist(self):
        if self.record['children']:
            return Parameters(self.record['children'][0])
        else:
            temp = Parameters()
            self.append(temp)
            return temp

    def merge(self, other):
        pass


class Parameters(RecordWrapper):

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

    def __getitem__(self, index):
        return Parameter(self.record['children'][index])

    def __iter__(self):
        for child in self.record['children']:
            yield Parameter(child)

    def merge(self, other):
        pass


class Parameter(RecordWrapper):

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

    def __str__(self):
        return ''.join(["(", self.name, " ", self.operator, " ", self.value,
                        ")"])

    @property
    def name(self):
        return self.metadata['Name'].lower()

    @name.setter
    def name(self, value):
        self.metadata['Name'] = value.lower()

    @property
    def operator(self):
        return self.metadata['Operator']

    @operator.setter
    def operator(self, value):
        self.metadata['Operator'] = value

    @property
    def value(self):
        return self.metadata['Value']

    @value.setter
    def value(self, value):
        self.metadata['Value'] = str(value)


class ExternalResources(RecordWrapper):

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

    def __eq__(self, other):
        for extRef in self:
            found = False
            for oExtRef in other:
                if extRef == oExtRef:
                    found = True
            if not found:
                return False
        return True

    def sort(self):
        """In theory we could sort the ExternalResource objects, but that
        would require opening them"""

    def __getitem__(self, index):
        return ExternalResource(self.record['children'][index])

    def __iter__(self):
        for child in self.record['children']:
            yield ExternalResource(child)

    def addResources(self, resourceIds):
        """Add a new external reference with the given uris. If you're looking
        to add ExternalResource objects, append() or extend() them instead.

        Args:
            resourceIds: a list of uris as strings
        """
        templist = []
        for ref in resourceIds:
            temp = ExternalResource()
            temp.resourceId = ref
            self.append(temp)
            templist.append(temp)
        return templist

    @property
    def resources(self):
        return [ExternalResource(extRef) for extRef in self]

    @resources.setter
    def resources(self, resources):
        """This is primarily used with split, where a list of ExternalResource
        Objects is divided up and passed to a new ExternalResources object
        through this method. We can't set the list directly, as the contents
        aren't in record form, but append will fix that for us automatically. A
        bit messy, but fairly concise.
        """
        self.record['children'] = []
        for res in resources:
            self.append(res)

    @property
    def resourceIds(self):
        return [res.resourceId for res in self]


class ExternalResource(RecordWrapper):

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

    def __eq__(self, other):
        if self.resourceId == other.resourceId:
            return True
        return False

    def merge(self, other):
        if self.metaType:
            if self.metaType != other.metaType:
                raise IOError("Two ExternalResources have same ResourceId "
                              "and different types")
        if self.tags:
            self.tags = ', '.join([self.tags, other.tags])

    @property
    def metaType(self):
        return self.getV('attrib', 'MetaType')

    @metaType.setter
    def metaType(self, value):
        return self.setV(value, 'attrib', 'MetaType')

    @property
    def resourceId(self):
        return self.getV('attrib', 'ResourceId')

    @resourceId.setter
    def resourceId(self, value):
        self.setV(value, 'attrib', 'ResourceId')

    @property
    def tags(self):
        return self.getV('attrib', 'Tags')

    @tags.setter
    def tags(self, value):
        self.setV(value, 'attrib', 'Tags')

    @property
    def bam(self):
        return self.resourceId

    @property
    def pbi(self):
        indices = self.indices
        for index in indices:
            if index.metaType == 'PacBio.Index.PacBioIndex':
                return index.resourceId

    @property
    def bai(self):
        indices = self.indices
        for index in indices:
            if index.metaType == 'PacBio.Index.BamIndex':
                return index.resourceId

    @property
    def scraps(self):
        return self._getSubResByMetaType('PacBio.SubreadFile.ScrapsBamFile')

    @scraps.setter
    def scraps(self, value):
        self._setSubResByMetaType('PacBio.SubreadFile.ScrapsBamFile', value)

    @property
    def reference(self):
        return self._getSubResByMetaType(
            'PacBio.ReferenceFile.ReferenceFastaFile')

    @reference.setter
    def reference(self, value):
        self._setSubResByMetaType('PacBio.ReferenceFile.ReferenceFastaFile',
                                  value)

    def _getSubResByMetaType(self, mType):
        resources = self.externalResources
        for res in resources:
            if res.metaType == mType:
                return res.resourceId

    def _setSubResByMetaType(self, mType, value):
        tmp = ExternalResource()
        tmp.resourceId = value
        tmp.metaType = mType
        resources = self.externalResources
        # externalresources objects have a tag by default, which means their
        # truthiness is true. Perhaps a truthiness change is in order
        if len(resources) == 0:
            resources = ExternalResources()
            resources.append(tmp)
            self.append(resources)
        else:
            resources.append(tmp)

    @property
    def externalResources(self):
        current = list(self.findChildren('ExternalResources'))
        if current:
            return ExternalResources(current[0])
        else:
            return ExternalResources()

    @property
    def indices(self):
        current = list(self.findChildren('FileIndices'))
        if current:
            return FileIndices(current[0])
        else:
            return FileIndices()

    @indices.setter
    def indices(self, indexList):
        self.removeChildren('FileIndices')
        tempList = FileIndices()
        for ind in indexList:
            temp = FileIndex()
            temp.resourceId = ind
            tempList.append(temp)
        self.append(tempList)

    def addIndices(self, indices):
        fileIndices = list(self.findChildren('FileIndices'))
        if fileIndices:
            fileIndices = FileIndices(fileIndices)
        else:
            fileIndices = FileIndices()
        for index in indices:
            temp = FileIndex()
            temp.resourceId = index
            fileIndices.append(temp)
        self.append(fileIndices)

class FileIndices(RecordWrapper):

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

    def __getitem__(self, index):
        return FileIndex(self.record['children'][index])

    def __iter__(self):
        for child in self.record['children']:
            yield FileIndex(child)


class FileIndex(RecordWrapper):

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

    @property
    def resourceId(self):
        return self.getV('attrib', 'ResourceId')

    @resourceId.setter
    def resourceId(self, value):
        self.setV(value, 'attrib', 'ResourceId')

    @property
    def metaType(self):
        return self.getV('attrib', 'MetaType')

    @metaType.setter
    def metaType(self, value):
        return self.setV(value, 'attrib', 'MetaType')


class DataSetMetadata(RecordWrapper):
    """The root of the DataSetMetadata element tree, used as base for subtype
    specific DataSet or for generic "DataSet" records."""


    def __init__(self, record=None):
        """Here, record is the root element of the Metadata Element tree"""
        super(DataSetMetadata, self).__init__(record)

    def merge(self, other):
        self.numRecords += other.numRecords
        self.totalLength += other.totalLength
        if other.summaryStats:
            if self.summaryStats:
                self.summaryStats.merge(other.summaryStats)
            else:
                self.append(other.summaryStats)

    @property
    def numRecords(self):
        """Return the number of records in a DataSet using helper functions
        defined in the base class"""
        try:
            return int(self.getMemberV('NumRecords'))
        except ValueError:
            return 0

    @numRecords.setter
    def numRecords(self, value):
        """Set the number of records, primarily when merging two DataSets"""
        self.setMemberV('NumRecords', str(value))

    @property
    def totalLength(self):
        """Return the TotalLength property of this dataset.
        TODO: update the value from the actual external reference on
        ValueError"""
        try:
            return int(self.getMemberV('TotalLength'))
        except ValueError:
            return 0

    @totalLength.setter
    def totalLength(self, value):
        """The total length of the dataset may merge differently for different
        datatypes. This will commonly be overridden by subclasses"""
        self.setMemberV('TotalLength', str(value))

    @property
    def summaryStats(self):
        try:
            return StatsMetadata(self.getV('children', 'SummaryStats'))
        except ValueError:
            return None

    @property
    def provenance(self):
        try:
            return Provenance(self.getV('children', 'Provenance'))
        except ValueError:
            return None


class SubreadSetMetadata(DataSetMetadata):
    """The DataSetMetadata subtype specific to SubreadSets. Deals explicitly
    with the merging of Collections and BioSamples metadata hierarchies."""

    def __init__(self, record=None):
        # This doesn't really need to happen unless there are contextual
        # differences in the meanings of subtypes (e.g. BioSamples mean
        # something different in SubreadSetMetadata vs ReferenceSetMetadata)
        if record:
            if (not isinstance(record, dict) and
                    not isinstance(record, SubreadSetMetadata) and
                    type(record).__name__ != 'DataSetMetadata'):
                raise TypeError("Cannot create SubreadSetMetadata from "
                                "{t}".format(t=type(record).__name__))
        super(SubreadSetMetadata, self).__init__(record)

    def merge(self, other):
        super(self.__class__, self).merge(other)
        self.collections.merge(other.collections)
        self.bioSamples.merge(other.bioSamples)

    @property
    def collections(self):
        """Return a list of wrappers around Collections elements of the
        Metadata Record"""
        return CollectionsMetadata(self.getV(tag='Collections',
                                             container='children'))

    @property
    def bioSamples(self):
        """Return a list of wrappers around BioSamples elements of the Metadata
        Record"""
        return BioSamplesMetadata(self.getV(tag='BioSamples',
                                            container='children'))


class ContigSetMetadata(DataSetMetadata):
    """The DataSetMetadata subtype specific to ContigSets."""


    def __init__(self, record=None):
        if record:
            if (not isinstance(record, dict) and
                    not isinstance(record, ContigSetMetadata) and
                    type(record).__name__ != 'DataSetMetadata'):
                raise TypeError("Cannot create ContigSetMetadata from "
                                "{t}".format(t=type(record).__name__))
        super(ContigSetMetadata, self).__init__(record)

    def merge(self, other):
        super(self.__class__, self).merge(other)
        self.contigs.merge(other.contigs)

    @property
    def organism(self):
        try:
            return self.getMemberV('Organism')
        except ValueError:
            return None

    @organism.setter
    def organism(self, value):
        self.setMemberV('Organism', value)

    @property
    def ploidy(self):
        try:
            return self.getMemberV('Ploidy')
        except ValueError:
            return None

    @ploidy.setter
    def ploidy(self, value):
        self.setMemberV('Ploidy', value)

    @property
    def contigs(self):
        # to this so that the absence of contigs is adequately conveyed.
        if not list(self.findChildren('Contigs')):
            return None
        return ContigsMetadata(self.getV('children', 'Contigs'))

    @contigs.setter
    def contigs(self, value):
        if not value:
            self.removeChildren('Contigs')
            self.append(ContigsMetadata())

    def addContig(self, newContig):
        if not self.contigs:
            self.contigs = []
        tmp = ContigMetadata()
        tmp.name = newContig.id if newContig.id else ''
        tmp.description = newContig.comment if newContig.comment else ''
        tmp.digest = 'DEPRECATED'
        tmp.length = len(newContig)
        self.contigs.append(tmp)


class BarcodeSetMetadata(DataSetMetadata):
    """The DataSetMetadata subtype specific to BarcodeSets."""


    def __init__(self, record=None):
        if record:
            if (not isinstance(record, dict) and
                    not isinstance(record, BarcodeSetMetadata) and
                    type(record).__name__ != 'DataSetMetadata'):
                raise TypeError("Cannot create BarcodeSetMetadata from "
                                "{t}".format(t=type(record).__name__))
        super(BarcodeSetMetadata, self).__init__(record)

    @property
    def barcodeConstruction(self):
        return self.getMemberV('BarcodeConstruction')


class ContigsMetadata(RecordWrapper):

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = 'Contigs'

    def __getitem__(self, index):
        return ContigMetadata(self.record['children'][index])

    def __iter__(self):
        for child in self.record['children']:
            yield ContigMetadata(child)

    def merge(self, other):
        self.extend([child for child in other])


class ContigMetadata(RecordWrapper):

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = 'Contig'

    @property
    def digest(self):
        return self.getV('attrib', 'Digest')

    @digest.setter
    def digest(self, value):
        return self.setV(value, 'attrib', 'Digest')

    @property
    def length(self):
        return int(self.getV('attrib', 'Length'))

    @length.setter
    def length(self, value):
        return self.setV(str(value), 'attrib', 'Length')


class CollectionsMetadata(RecordWrapper):
    """The Element should just have children: a list of
    CollectionMetadataTags"""


    def __getitem__(self, index):
        return CollectionMetadata(self.record['children'][index])

    def __iter__(self):
        for child in self.record['children']:
            yield CollectionMetadata(child)

    def merge(self, other):
        self.extend([child for child in other])


class CollectionMetadata(RecordWrapper):
    """The metadata for a single collection. It contains Context,
    InstrumentName etc. as attribs, InstCtrlVer etc. for children"""


    @property
    def context(self):
        return self.getV('attrib', 'Context')

    @property
    def instrumentName(self):
        return self.getV('attrib', 'InstrumentName')

    @property
    def instrumentId(self):
        return self.getV('attrib', 'InstrumentId')

    @property
    def instCtrlVer(self):
        return self.getMemberV('InstCtrlVer')

    @property
    def sigProcVer(self):
        return self.getMemberV('SigProcVer')

    @property
    def automation(self):
        return Automation(self.getMemberV('Automation'))

    @property
    def collectionNumber(self):
        return self.getMemberV('collectionNumber')

    @property
    def cellIndex(self):
        return self.getMemberV('cellIndex')

    @property
    def cellPac(self):
        return self.getMemberV('cellPac', 'attrib')

    @property
    def runDetails(self):
        return RunDetailsMetadata(self.getV('children', 'RunDetails'))

    @property
    def wellSample(self):
        return WellSampleMetadata(self.getV('children', 'WellSample'))

    @property
    def primary(self):
        return PrimaryMetadata(self.getV('children', 'Primary'))

class Automation(RecordWrapper):

    @property
    def automationParameters(self):
        return AutomationParameters(self.getV('children',
                                              'AutomationParameters'))

class AutomationParameters(RecordWrapper):

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

    @property
    def automationParameter(self):
        return AutomationParameter(self.getV('children',
                                             'AutomationParameter'))

    def addParameter(self, key, value):
        temp = AutomationParameter()
        if key:
            temp.name = key
        if value:
            temp.value = value
        self.append(temp)

class AutomationParameter(RecordWrapper):

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

class Provenance(RecordWrapper):
    """The metadata concerning this dataset's provenance"""

    @property
    def createdBy(self):
        return self.getV(container='attrib', tag='CreatedBy')

    @property
    def parentTool(self):
        return ParentTool(self.getV('children', 'ParentTool'))

class ParentTool(RecordWrapper):
    pass

class StatsMetadata(RecordWrapper):
    """The metadata from the machine sts.xml"""

    def merge(self, other):
        self.shortInsertFraction = (self.shortInsertFraction *
                                    self.prodDist.bins[1] +
                                    other.shortInsertFraction *
                                    other.prodDist.bins[1])/(
                                        self.prodDist.bins[1]
                                        + other.prodDist.bins[1])
        self.adapterDimerFraction = (self.adapterDimerFraction *
                                     self.prodDist.bins[1] +
                                     other.adapterDimerFraction *
                                     other.prodDist.bins[1])/(
                                         self.prodDist.bins[1]
                                         + other.prodDist.bins[1])
        self.numSequencingZmws += other.numSequencingZmws
        toHandle = [
            (self.prodDist, other.prodDist),
            (self.readTypeDist, other.readTypeDist),
            (self.readLenDist, other.readLenDist),
            (self.readQualDist, other.readQualDist),
            (self.medianInsertDist, other.medianInsertDist),
            (self.insertReadQualDist, other.insertReadQualDist),
            (self.insertReadLenDist, other.insertReadLenDist),
            (self.controlReadQualDist, other.controlReadQualDist),
            (self.controlReadLenDist, other.controlReadLenDist),
            ]
        for selfDist, otherDist in toHandle:
            try:
                selfDist.merge(otherDist)
            except BinMismatchError:
                self.append(otherDist)
            except ValueError:
                if otherDist:
                    self.append(otherDist)

    @property
    def prodDist(self):
        return DiscreteDistribution(self.getV('children', 'ProdDist'))

    @property
    def readTypeDist(self):
        return DiscreteDistribution(self.getV('children', 'ReadTypeDist'))

    @property
    def readLenDist(self):
        return ContinuousDistribution(self.getV('children', 'ReadLenDist'))

    @property
    def readLenDists(self):
        return [ContinuousDistribution(child) for child in
                self.findChildren('ReadLenDist')]

    @property
    def readQualDist(self):
        return ContinuousDistribution(self.getV('children', 'ReadQualDist'))

    @property
    def readQualDists(self):
        return [ContinuousDistribution(child) for child in
                self.findChildren('ReadQualDist')]

    @property
    def insertReadQualDist(self):
        return ContinuousDistribution(self.getV('children',
                                                'InsertReadQualDist'))

    @property
    def insertReadLenDist(self):
        return ContinuousDistribution(self.getV('children',
                                                'InsertReadLenDist'))
    @property
    def controlReadQualDist(self):
        return ContinuousDistribution(self.getV('children',
                                                'ControlReadQualDist'))

    @property
    def controlReadLenDist(self):
        return ContinuousDistribution(self.getV('children',
                                                'ControlReadLenDist'))

    @property
    def medianInsertDist(self):
        return ContinuousDistribution(self.getV('children',
                                                'MedianInsertDist'))
    @property
    def medianInsertDists(self):
        return [ContinuousDistribution(child)
                for child in self.findChildren('MedianInsertDist')]

    @property
    def adapterDimerFraction(self):
        return float(self.getMemberV('AdapterDimerFraction'))

    @adapterDimerFraction.setter
    def adapterDimerFraction(self, value):
        self.setMemberV('AdapterDimerFraction', float(value))

    @property
    def numSequencingZmws(self):
        return float(self.getMemberV('NumSequencingZmws'))

    @numSequencingZmws.setter
    def numSequencingZmws(self, value):
        self.setMemberV('NumSequencingZmws', float(value))

    @property
    def shortInsertFraction(self):
        return float(self.getMemberV('ShortInsertFraction'))

    @shortInsertFraction.setter
    def shortInsertFraction(self, value):
        self.setMemberV('ShortInsertFraction', float(value))


def _staggeredZip(binWidth, start1, start2, bins1, bins2):
    tupleList = [(start1, bins1), (start2, bins2)]
    tupleList.sort(key=lambda x: x[0])
    tuple1, tuple2 = tupleList
    start1, bins1 = tuple1
    start2, bins2 = tuple2
    index = start1
    while bins1 and bins2:
        # pull from the first if it starts first
        if index != start2:
            index += binWidth
            yield bins1.pop(0)
        else:
            yield bins1.pop(0) + bins2.pop(0)
    # fill with zeros if the second hasn't started yet (they don't overlap)
    while index != start2:
        index += binWidth
        yield 0
    # then run out whichever still has items
    for scrap in bins1 or bins2:
        yield scrap

class ContinuousDistribution(RecordWrapper):

    def merge(self, other):
        if self.binWidth != other.binWidth:
            raise BinWidthMismatchError(self.binWidth, other.binWidth)
        if (self.minBinValue % self.binWidth
                != other.minBinValue % other.binWidth):
            raise BinBoundaryMismatchError(self.minBinValue, other.minBinValue)
        self.bins = list(_staggeredZip(self.binWidth, self.minBinValue,
                                       other.minBinValue, self.bins,
                                       other.bins))
        self.minBinValue = min(self.minBinValue, other.minBinValue)

    @property
    def numBins(self):
        return int(self.getMemberV('NumBins'))

    @property
    def sampleSize(self):
        return int(self.getMemberV('SampleSize'))

    @property
    def sampleMean(self):
        return float(self.getMemberV('SampleMean'))

    @property
    def sampleMed(self):
        return float(self.getMemberV('SampleMed'))

    @property
    def sampleStd(self):
        return float(self.getMemberV('SampleStd'))

    @property
    def sample95thPct(self):
        return float(self.getMemberV('Sample95thPct'))

    @property
    def binWidth(self):
        return float(self.getMemberV('BinWidth'))

    @binWidth.setter
    def binWidth(self, value):
        self.setMemberV('BinWidth', str(value))

    @property
    def minOutlierValue(self):
        return float(self.getMemberV('MinOutlierValue'))

    @property
    def maxOutlierValue(self):
        return float(self.getMemberV('MaxOutlierValue'))

    @property
    def minBinValue(self):
        return float(self.getMemberV('MinBinValue'))

    @minBinValue.setter
    def minBinValue(self, value):
        self.setMemberV('MinBinValue', str(value))

    @property
    def maxBinValue(self):
        return float(self.getMemberV('MaxBinValue'))

    @property
    def description(self):
        return self.getMemberV('MetricDescription')

    @property
    def bins(self):
        binCounts = RecordWrapper(self.getV('children', 'BinCounts'))
        counts = binCounts.findChildren('BinCount')
        counts = [int(count.metavalue) for count in counts]
        return counts

    @bins.setter
    def bins(self, newBins):
        """Replace the bins."""
        binCounts = RecordWrapper(self.getV('children', 'BinCounts'))
        binCounts.removeChildren('BinCount')
        binCounts.extend([_emptyMember(tag='BinCount', text=str(mem))
                          for mem in newBins])

    @property
    def labels(self):
        """Label the bins with the min value of each bin"""
        # numBins appears to be wrong in the sts.xml files. Otherwise, it would
        # work well here:
        return [self.minBinValue + i * self.binWidth for i in
                range(len(self.bins))]

class BinMismatchError(Exception):
    pass

class BinWidthMismatchError(BinMismatchError):

    def __init__(self, width1, width2):
        self.width1 = width1
        self.width2 = width2

    def __str__(self):
        return "Bin width mismatch: {w1} != {w2}".format(w1=self.width1,
                                                         w2=self.width2)

class BinNumberMismatchError(BinMismatchError):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return "Bin number mismatch: {w1} != {w2}".format(w1=self.num1,
                                                          w2=self.num2)

class BinBoundaryMismatchError(BinMismatchError):

    def __init__(self, min1, min2):
        self.min1 = min1
        self.min2 = min2

    def __str__(self):
        return "Bin boundary offset mismatch, minVals: {w1} != {w2}".format(
            w1=self.min1, w2=self.min2)

class DiscreteDistribution(RecordWrapper):

    def merge(self, other):
        if self.numBins != other.numBins:
            raise BinNumberMismatchError(self.numBins, other.numBins)
        if set(self.labels) != set(other.labels):
            raise BinMismatchError
        sBins = zip(self.labels, self.bins)
        oBins = dict(zip(other.labels, other.bins))
        self.bins = [value + oBins[key] for key, value in sBins]

    @property
    def numBins(self):
        return int(self.getMemberV('NumBins'))

    @property
    def bins(self):
        binCounts = RecordWrapper(self.getV('children', 'BinCounts'))
        return [int(child.metavalue)
                for child in binCounts.findChildren('BinCount')]

    @bins.setter
    def bins(self, newBins):
        """Replace the bin values. This assumes the label order is
        maintained"""
        binCounts = RecordWrapper(self.getV('children', 'BinCounts'))
        for child, value in zip(binCounts.findChildren('BinCount'), newBins):
            child.metavalue = str(value)

    @property
    def labels(self):
        binLabels = RecordWrapper(self.getV('children', 'BinLabels'))
        return [child.metavalue
                for child in binLabels.findChildren('BinLabel')]

    @property
    def description(self):
        return self.getMemberV('MetricDescription')


class RunDetailsMetadata(RecordWrapper):


    @property
    def runId(self):
        return self.getMemberV('runId')

    @property
    def name(self):
        return self.getMemberV('Name')


class WellSampleMetadata(RecordWrapper):


    @property
    def uniqueId(self):
        return self.getV('attrib', 'UniqueId')

    @property
    def plateId(self):
        return self.getMemberV('PlateId')

    @property
    def wellName(self):
        return self.getMemberV('WellName')

    @property
    def concentration(self):
        return self.getMemberV('Concentration')

    @property
    def sampleReuseEnabled(self):
        return self.getMemberV('SampleReuseEnabled')

    @property
    def stageHotstartEnabled(self):
        return self.getMemberV('StageHotstartEnabled')

    @property
    def sizeSelectionEnabled(self):
        return self.getMemberV('SizeSelectionEnabled')

    @property
    def useCount(self):
        return self.getMemberV('UseCount')

    @property
    def comments(self):
        return self.getMemberV('Comments')

    @property
    def bioSamplePointers(self):
        return BioSamplePointersMetadata(
            self.getV('children', 'BioSamplePointers'))


class BioSamplePointersMetadata(RecordWrapper):
    """The BioSamplePointer members don't seem complex enough to justify
    class representation, instead rely on base class methods to provide
    iterators and accessors"""
    pass


class PrimaryMetadata(RecordWrapper):
    """

    Doctest:
        >>> import os, tempfile
        >>> from pbcore.io import SubreadSet
        >>> import pbcore.data.datasets as data
        >>> ds1 = SubreadSet(data.getXml(5))
        >>> ds1.metadata.collections[0].primary.resultsFolder
        'Analysis_Results'
        >>> ds1.metadata.collections[0].primary.resultsFolder = (
        ...     'BetterAnalysis_Results')
        >>> ds1.metadata.collections[0].primary.resultsFolder
        'BetterAnalysis_Results'
        >>> outdir = tempfile.mkdtemp(suffix="dataset-doctest")
        >>> outXml = 'xml:' + os.path.join(outdir, 'tempfile.xml')
        >>> ds1.write(outXml, validate=False)
        >>> ds2 = SubreadSet(outXml)
        >>> ds2.metadata.collections[0].primary.resultsFolder
        'BetterAnalysis_Results'
    """

    @property
    def automationName(self):
        return self.getMemberV('AutomationName')

    @property
    def configFileName(self):
        return self.getMemberV('ConfigFileName')

    @property
    def sequencingCondition(self):
        return self.getMemberV('SequencingCondition')

    @property
    def resultsFolder(self):
        return self.getMemberV('ResultsFolder')

    @resultsFolder.setter
    def resultsFolder(self, value):
        self.setMemberV('ResultsFolder', value)

    @property
    def collectionPathUri(self):
        return self.getMemberV('CollectionPathUri')

    @property
    def copyFiles(self):
        return CopyFilesMetadata(self.getV('children', 'CopyFiles'))


class CopyFilesMetadata(RecordWrapper):
    """The CopyFile members don't seem complex enough to justify
    class representation, instead rely on base class methods"""
    pass


class BioSamplesMetadata(RecordWrapper):
    """The metadata for the list of BioSamples

        Doctest:
            >>> from pbcore.io import SubreadSet
            >>> import pbcore.data.datasets as data
            >>> ds = SubreadSet(data.getSubreadSet())
            >>> ds.metadata.bioSamples[0].name
            'consectetur purus'
            >>> for bs in ds.metadata.bioSamples:
            ...     print bs.name
            consectetur purus
            >>> em = {'tag':'BioSample', 'text':'', 'children':[],
            ...       'attrib':{'Name':'great biosample'}}
            >>> ds.metadata.bioSamples.extend([em])
            >>> ds.metadata.bioSamples[1].name
            'great biosample'
        """


    def __getitem__(self, index):
        """Get a biosample"""
        return BioSampleMetadata(self.record['children'][index])

    def __iter__(self):
        """Iterate over biosamples"""
        for child in self.record['children']:
            yield BioSampleMetadata(child)

    def merge(self, other):
        self.extend([child for child in other])


class BioSampleMetadata(RecordWrapper):
    """The metadata for a single BioSample"""


    @property
    def uniqueId(self):
        return self.getV('attrib', 'UniqueId')

    @property
    def createdAt(self):
        return self.getV('attrib', 'CreatedAt')


def _emptyMember(tag=None, text=None, attrib=None, children=None):
    """Return an empty stock Element representation"""
    if not tag:
        tag = ''
    if not text:
        text = ''
    if not attrib:
        attrib = {}
    if not children:
        children = []
    return {'tag': tag, 'text': text, 'attrib': attrib, 'children': children}
