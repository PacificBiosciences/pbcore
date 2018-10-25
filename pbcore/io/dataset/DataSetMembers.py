# Author: Martin D. Smith


"""DataSetMetadata (also the tag of the Element in the DataSet XML
representation) is somewhat challening to store, access, and (de)serialize
efficiently. Here, we maintain a bulk representation of all of the dataset
metadata (or any other XML data, like ExternalResources) found in the XML file
in the following data structure:

|   An Element is a turned into a dictionary:
|       XmlElement => {'tag': 'ElementTag',
|                      'text': 'ElementText',
|                      'attrib': {'ElementAttributeName': 'AttributeValue',
                                  'AnotherAttrName': 'AnotherAttrValue'},
|                      'children': [XmlElementDict,
                                    XmlElementDictWithSameOrDifferentTag]}

Child elements are represented similarly and stored (recursively) as a list
in 'children'. The top level we store for DataSetMetadata is just a list,
which can be thought of as the list of children of a different element
(say, a DataSet or SubreadSet element, if we stored that):

- DataSetMetadata = [XmlTag, XmlTagWithSameOrDifferentTag]

We keep this for three reasons:

1. We don't want to have to write a lot of logic to go from XML to an \
internal representation and then back to XML.

2. We want to be able to store and at least write metadata that doesn't yet \
exist, even if we can't merge it intelligently.

3. Keeping and manipulating a dictionary is ~10x faster than an \
OrderedAttrDict, and probably faster to use than a full stack of \
objects.

Instead, we keep and modify this list:dictionary structure, wrapping it in
classes as necessary. The classes and methods that wrap this datastructure
serve two pruposes:

- Provide an interface for our code (and making merging clean) e.g.:
    - DataSet("test.xml").metadata.numRecords += 1

- Provide an interface for users of the DataSet API, e.g.:

    - numRecords = DataSet("test.xml").metadata.numRecords
    - bioSamplePointer = (DataSet("test.xml")\
                          .metadata.collections[0]\
                          .wellSample.bioSamplePointers[0])
    - Though users can still access novel metadata types the hard way e.g.:
        - bioSamplePointer = (DataSet("test.xml")\
                              .metadata.collections[0]\
                              ['WellSample']['BioSamplePointers']\
                              ['BioSamplePointer'].record['text'])

Notes:
    - If you want temporary children to be retained for a classes's children,
      pass parent=self to the child's constructor.
        - it helps to add a TAG member...

"""

from __future__ import absolute_import
from __future__ import division

import ast
import uuid
import copy
import logging
import os
import operator as OP
import numpy as np
import re
from urlparse import urlparse
from urllib import unquote
from functools import partial as P
from collections import Counter, defaultdict
from pbcore.io.dataset.utils import getTimeStampedName, hash_combine_zmws
from pbcore.io.dataset.DataSetUtils import getDataSetUuid
from pbcore.io.dataset.DataSetWriter import NAMESPACES
from functools import reduce

log = logging.getLogger(__name__)

def uri2fn(fn):
    return unquote(urlparse(fn).path.strip())

def uri2scheme(fn):
    return urlparse(fn).scheme

def newUuid(record):
    # At some point the uuid may need to be a digest
    #import hashlib
    #newId = str(hashlib.md5(str(record)).hexdigest())

    # Group appropriately
    #newId = '-'.join([newId[:8], newId[8:12], newId[12:16], newId[16:20],
    #                  newId[20:]])
    #return newId

    # Today is not that day
    return str(uuid.uuid4())

def map_val_or_vec(func, target):
    if isinstance(target, (list, tuple, np.ndarray)):
        return map(func, target)
    else:
        return func(target)

def inNd(arrs1, arrs2):
    if isinstance(arrs1, tuple):
        # a tuple of numpy columns to check:
        res = np.ones(len(arrs1[0]), dtype=np.bool_)
        for a1, a2 in zip(arrs1, arrs2):
            res &= np.in1d(a1, a2)
        return res
    else:
        # just two numpy columns:
        return np.in1d(arrs1, arrs2)

OPMAP = {'==': OP.eq,
         '=': OP.eq,
         'eq': OP.eq,
         '!=': OP.ne,
         'ne': OP.ne,
         '>=': OP.ge,
         '&gt;=': OP.ge,
         'gte': OP.ge,
         '<=': OP.le,
         '&lt;=': OP.le,
         'lte': OP.le,
         '>': OP.gt,
         '&gt;': OP.gt,
         'gt': OP.gt,
         '<': OP.lt,
         '&lt;': OP.lt,
         'lt': OP.lt,
         'in': inNd,
         'not_in': lambda x, y: ~inNd(x, y),
         '&': lambda x, y: OP.and_(x, y).view(np.bool_),
         '~': lambda x, y: np.logical_not(OP.and_(x, y).view(np.bool_)),
        }

# These functions should take np.ndarrays that are already a reasonable type
# (e.g. from dset.index.holeNumber, which is already in 32bit int)
# Parsing doesn't happen here, so we're not casting from strings... This is
# probably overkill and lambda x: x is probably always enough.
HASHMAP = {'UnsignedLongCast': lambda x: x.astype(np.uint32),
           'Uint32Cast': lambda x: x.astype(np.uint32),
           'IntegerCast': lambda x: x.astype(np.int_),
           'Int32Cast': lambda x: x.astype(np.int32),
           'NumericCast': lambda x: x,
           'BoostHashCombine': lambda x: hash_combine_zmws(x),
           }

def mapOp(op):
    return OPMAP[op]

def make_mod_hash_acc(accessor, mod, hashname):
    hashfunc = HASHMAP[hashname]
    def accNmod(records):
        return hashfunc(accessor(records)) % mod
    return accNmod

def str2list(value):
    value = value.strip('set')
    value = value.strip('()')
    value = value.strip('[]')
    if ',' in value:
        value = value.split(',')
    else:
        value = value.split()
    value = [v.strip() for v in value]
    value = [v.strip("'") for v in value]
    return value

def setify(value):
    return np.unique(str2list(value))

def fromFile(value):
    with open(value, 'rU') as ifh:
        return np.unique([val.strip() for val in ifh])

def isListString(string):
    """Detect if string is actually a representation a stringified list"""

    listver = str2list(string)
    if len(listver) > 1 or re.search('[\[\(\{].+[\}\)\]]', string):
        return True

def isFile(string):
    if isinstance(string, str) and os.path.exists(string):
        return True
    return False

def qnamer(qid2mov, qId, hn, qs, qe):
    movs = np.empty_like(qId, dtype='S{}'.format(
        max(map(len, qid2mov.values()))))
    for k, v in qid2mov.items():
        movs[qId == k] = v
    return (movs, hn, qs, qe)

def breakqname(qname):
    tbr = []
    chunks = qname.split('/')
    # movie:
    if len(chunks) > 0:
        tbr.append(chunks[0])
    # holenumber:
    if len(chunks) > 1:
        tbr.append(int(chunks[1]))
    # qstart, end
    if len(chunks) > 2:
        span = chunks[2].split('_')
        if len(span) == 2:
            tbr.append(int(span[0]))
            tbr.append(int(span[1]))
    return tbr

def qname2vec(qnames):
    if isinstance(qnames, str):
        qnames = [qnames]
    return zip(*[breakqname(q) for q in qnames])

class PbiFlags(object):
    NO_LOCAL_CONTEXT = 0
    ADAPTER_BEFORE = 1
    ADAPTER_AFTER = 2
    BARCODE_BEFORE = 4
    BARCODE_AFTER = 8
    FORWARD_PASS = 16
    REVERSE_PASS = 32

    @classmethod
    def flagMap(cls, flag):
        if flag.isdigit():
            return int(flag)
        return reduce(OP.or_,
                      (getattr(cls, fl.strip()) for fl in flag.split('|')))

def subgetter(key, container='text', default=None, asType=(lambda x: x),
              attrib=None):
    def get(self):
        return self.getMemberV(key, container=container, default=default,
                               asType=asType, attrib=attrib)
    return property(get)

def subsetter(key, container='text', attrib=None):
    def set(self, value):
        self._runCallbacks()
        self.setMemberV(key, str(value), container=container, attrib=attrib)
    return set

def subaccs(key, container='text', default=None, asType=(lambda x: x),
            attrib=None):
    get = subgetter(key, container=container, default=default, asType=asType,
                    attrib=attrib)
    get = get.setter(subsetter(key, container=container, attrib=attrib))
    return get

def getter(key, container='attrib', asType=(lambda x: x), parent=False):
    def get(self):
        if parent:
            return asType(self.getV(container, key), parent=self)
        else:
            return asType(self.getV(container, key))
    return property(get)

def setter(key, container='attrib'):
    def set(self, value):
        self._runCallbacks()
        self.setV(str(value), container, key)
    return set

def accs(key, container='attrib', asType=(lambda x: x), parent=False):
    get = getter(key, container, asType, parent=parent)
    get = get.setter(setter(key, container))
    return get

def runonce(func):
    def runner():
        if not runner.hasrun:
            try:
                return func()
            finally:
                runner.hasrun = True
    runner.hasrun = False
    return runner

def updateTag(ele, tag):
    if ele.metaname == '':
        ele.metaname = tag

def updateNamespace(ele, ns):
    if ele.namespace == '':
        ele.namespace = ns


class RecordWrapper(object):
    """The base functionality of a metadata element.

    Many of the methods here are intended for use with children of
    RecordWrapper (e.g. append, extend). Methods in child classes often provide
    similar functionality for more raw inputs (e.g. resourceIds as strings)"""

    # only things that should be kept with their parents (indices) should be
    # True
    KEEP_WITH_PARENT = False
    NS = ''

    def __init__(self, record=None, parent=None):
        """Here, record is any element in the Metadata Element tree and a
        dictionary with five members: 'tag', 'attrib', 'text', 'children', and
        'namespace'

        Do not deepcopy, we rely on side effects for all persistent
        modifications.
        """
        self._callbacks = []
        if record:
            try:
                self.record = record.record
            except AttributeError:
                self.record = record
        else:
            self.record = _emptyMember()
            # register a callback to set the XML element 'tag' to the
            # class's TAG member if it has one, with the class name as a
            # fallback
            self.registerCallback(runonce(
                P(updateTag, self,
                  getattr(self, 'TAG', self.__class__.__name__))))
            if not parent is None:
                # register a callback to append this object to the parent, so
                # that it will be added to the XML file
                self.registerCallback(runonce(P(parent.append, self.record)))
        assert 'tag' in self.record.keys()

        # we could do the same with namespace, but it isn't used in nonzero, so
        # we can just update it:
        if not self.record.get('namespace', ''):
            self.record['namespace'] = NAMESPACES[self.NS]


    def registerCallback(self, func):
        if func not in self._callbacks:
            self._callbacks.append(func)

    def clearCallbacks(self):
        self._callbacks = []

    def _runCallbacks(self):
        for func in self._callbacks:
            func()

    def __len__(self):
        """Return the number of children in this node"""
        return len(self.record['children'])

    def __bool__(self):
        if self.record['tag'] != '':
            return True
        if self.record['text'] != '':
            return True
        if self.record['attrib'] != {}:
            return True
        if self.record['children'] != []:
            return True
        return False

    def __nonzero__(self):
        # py2 compatibility
        # https://docs.djangoproject.com/en/1.11/topics/python3/
        return type(self).__bool__(self)

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

    def __repr__(self):
        """Return a pretty string represenation of this object:

            "<type tag text attribs children>"
        """
        c_tags = [c.record['tag'] for c in self]
        repr_d = dict(k=self.__class__.__name__, t=self.record['tag'],
                      n=self.record['namespace'],
                      x=self.record['text'], a=self.record['attrib'],
                      c=c_tags)
        rep = '<{k} tag:{{{n}}}{t} text:{x} attribs:{a} children:{c}>'.format(
            **repr_d)
        return rep

    def __eq__(self, other):
        """Does not take child order into account!!!!"""
        if (sorted([c.record['tag'] for c in self]) !=
                sorted([c.record['tag'] for c in other])):
            return False
        if self.__class__.__name__ != other.__class__.__name__:
            return False
        for attrib in ['metaname', 'namespace', 'metavalue', 'metadata']:
            if getattr(self, attrib) != getattr(other, attrib):
                return False
        return True

    def pop(self, index):
        return self.record['children'].pop(index)

    def merge(self, other):
        pass

    def getMemberV(self, tag, container='text', default=None, asType=str,
                   attrib=None):
        """Generic accessor for the contents of the children of this element,
        without having to interface with them directly"""
        try:
            tbr = asType(self.record['children'][self.index(str(tag))][
                str(container)])
            if container == 'attrib':
                return tbr[attrib]
            return tbr
        except (KeyError, ValueError):
            return default

    def setMemberV(self, tag, value, container='text', attrib=None):
        """Generic accessor for the contents of the children of this element,
        without having to interface with them directly"""
        try:
            if container == 'attrib':
                self.record['children'][self.index(str(tag))][str(container)][attrib] = (
                    str(value))
            else:
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
            newMember._runCallbacks()
            self.record['children'].append(newMember.record)
        else:
            self.record['children'].append(newMember)
        self._runCallbacks()

    def index(self, tag):
        """Return the index in 'children' list of item with 'tag' member"""
        return self.tags.index(tag)

    @property
    def tags(self):
        """Return the list of tags for children in this element"""
        return [child['tag'] for child in self.record['children']]

    @property
    def namespace(self):
        return self.record['namespace']

    @namespace.setter
    def namespace(self, value):
        self.record['namespace'] = value

    @property
    def attrib(self):
        return self.record['attrib']

    @property
    def metaname(self):
        """Cleaner accessor for this node's tag"""
        return self.record['tag']

    @metaname.setter
    def metaname(self, value):
        """Cleaner accessor for this node's tag"""
        self.record['tag'] = value

    @property
    def text(self):
        return self.metavalue

    @text.setter
    def text(self, value):
        self.metavalue = value

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
        removed = []
        for child in self.record['children']:
            if child['tag'] != tag:
                keepers.append(child)
            else:
                removed.append(child)
        self.record['children'] = keepers
        return removed

    def pruneChildrenTo(self, whitelist):
        newChildren = []
        oldChildren = self.record['children']
        for child in oldChildren:
            if child['tag'] in whitelist:
                newChildren.append(child)
        self.record['children'] = newChildren

    # Some common attributes (to reduce code duplication):

    name = accs('Name')
    value = accs('Value')
    version = accs('Version')
    description = accs('Description')
    uniqueId = accs('UniqueId')
    createdAt = accs('CreatedAt')

def filter_read(accessor, operator, value, read):
    return operator(accessor(read), value)

def n_subreads(index):
    _, inverse, counts = np.unique(index.holeNumber, return_inverse=True,
                                   return_counts=True)
    return counts[inverse]

class Filters(RecordWrapper):
    NS = 'pbds'

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

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
            sorted(list(self), key=lambda x: x.metaname),
            sorted(list(other), key=lambda x: x.metaname))])

    def __bool__(self):
        for filt in self:
            for req in filt:
                if req.name:
                    return True
        return False

    def __nonzero__(self):
        # py2 compatibility
        # https://docs.djangoproject.com/en/1.11/topics/python3/
        return type(self).__bool__(self)

    def __str__(self):
        buff = []
        for filt in self:
            temp = ['(']
            for req in filt:
                # strip off the parens
                temp.append(str(req)[1:-1])
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
        # (mdsmith 28092017) I feel like we should be running callbacks here,
        # but we've been doing fine without and it adds to the opening cost

    def testParam(self, param, value, testType=str, oper='='):
        options = [True] * len(list(self))
        if not options:
            return True
        for i, filt in enumerate(self):
            for req in filt:
                if req.name == param:
                    if not mapOp(oper)(testType(value),
                                            testType(req.value)):
                        options[i] = False
        return any(options)

    def testField(self, param, values, testType=str, oper='='):
        passes = np.zeros(len(values), dtype=np.bool_)
        tested = False
        for i, filt in enumerate(self):
            for req in filt:
                if req.name == param:
                    tested = True
                    passes |= mapOp(oper)(values,
                                          testType(req.value))
        if not tested:
            return np.ones(len(values), dtype=np.bool_)
        return passes

    @property
    def _bamAccMap(self):
        return {'rname': (lambda x: x.referenceName),
                'length': (lambda x: int(x.readLength)),
                'qname': (lambda x: x.qName),
                'movie': (lambda x: x.movieName),
                'zm': (lambda x: int(x.HoleNumber)),
                # not implemented yet:
                #'bc': (lambda x: x.barcode),
                # pbi mediated alt:
                'bc': (lambda x: (x.bam.pbi[x.rowNumber]['bcForward'],
                                  x.bam.pbi[x.rowNumber]['bcReverse'])),
                'qs': (lambda x: int(x.qStart)),
                'rq': (lambda x: int(x.MapQV)),
                'mapqv': (lambda x: int(x.MapQV)),
                'pos': (lambda x: int(x.tStart)),
                'accuracy': (lambda x: float(x.identity)),
                'readstart': (lambda x: int(x.aStart)),
                'tstart': (lambda x: int(x.tStart)),
                'tend': (lambda x: int(x.tEnd)),
                'n_subreads': (lambda x: len(np.flatnonzero(
                                            x.reader.holeNumber ==
                                            x.HoleNumber))),
               }

    def _pbiAccMap(self):
        return {'length': (lambda x: int(x.aEnd)-int(x.aStart)),
                'qname': (lambda m, x: qnamer(m, x.qId, x.holeNumber, x.qStart,
                                              x.qEnd)),
                'qid': (lambda x: x.qId),
                'zm': (lambda x: int(x.holeNumber)),
                'pos': (lambda x: int(x.tStart)),
                'readstart': (lambda x: int(x.aStart)),
                'tstart': (lambda x: int(x.tStart)),
                'tend': (lambda x: int(x.tEnd)),
               }

    def _pbiMappedVecAccMap(self):
        plus = {'rname': (lambda x: x.tId),
                'alignedlength': (lambda x: x.aEnd - x.aStart),
                'length': (lambda x: x.aEnd - x.aStart),
                'pos': (lambda x: x.tStart),
                'as': (lambda x: x.aStart),
                'ae': (lambda x: x.aEnd),
                'astart': (lambda x: x.aStart),
                'aend': (lambda x: x.aEnd),
                'readstart': (lambda x: x.aStart),
                'tstart': (lambda x: x.tStart),
                'tend': (lambda x: x.tEnd),
                'mapqv': (lambda x: x.mapQV),
                'accuracy': (
                    lambda x: (np.ones(len(x.nMM), dtype='f4') -
                               (x.nMM + x.nIns + x.nDel).astype(np.float)/
                               (x.nM + x.nMM + x.nIns)))
               }
        base = self._pbiVecAccMap()
        base.update(plus)
        return base

    def _pbiVecAccMap(self):
        return {'length': (lambda x: x.qEnd - x.qStart),
                'qstart': (lambda x: x.qStart),
                'qend': (lambda x: x.qEnd),
                'qname': (lambda m, x: qnamer(m, x.qId, x.holeNumber, x.qStart,
                                              x.qEnd)),
                'qid': (lambda x: x.qId),
                'movie': (lambda x: x.qId),
                'zm': (lambda x: x.holeNumber),
                'rq': (lambda x: x.readQual),
                'bcf': (lambda x: x.bcForward),
                'bcr': (lambda x: x.bcReverse),
                'bcq': (lambda x: x.bcQual),
                'bq': (lambda x: x.bcQual),
                'bc': (lambda x: x['bcForward', 'bcReverse']),
                'cx': (lambda x: x.contextFlag),
                'n_subreads': n_subreads,
               }

    @property
    def _bamTypeMap(self):
        return {'rname': str,
                'length': int,
                'qstart': int,
                'qend': int,
                'qname': str,
                'qid': int,
                'movie': str,
                'zm': int,
                'bc': str,
                'bcr': int,
                'bcf': int,
                'bcq': int,
                'bq': int,
                'qs': int,
                'rq': np.float,
                'pos': int,
                'tstart': int,
                'tend': int,
                'accuracy': np.float,
                'readstart': int,
                'cx': PbiFlags.flagMap,
                'n_subreads': int,
                'mapqv': int,
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
                      'length': (lambda x: int(len(x))),
                     }
            typeMap = {'id': str,
                       'length': int,
                      }
        elif readType.lower() == "pbi":
            accMap = self._pbiAccMap()
            typeMap = self._bamTypeMap
        else:
            raise TypeError("Read type not properly specified")
        tests = []
        for filt in self:
            reqTests = []
            for req in filt:
                param = req.name
                value = typeMap[param](req.value)
                operator = mapOp(req.operator)
                reqTests.append(P(filter_read, accMap[param], operator, value))
            tests.append(lambda x, rt=reqTests: all([f(x) for f in rt]))
        return tests

    def filterIndexRecords(self, indexRecords, nameMap, movieMap,
                           readType='bam'):
        if readType == 'bam':
            typeMap = self._bamTypeMap
            accMap = self._pbiVecAccMap()
            # check for mappings:
            if 'tStart' in indexRecords.dtype.names:
                accMap = self._pbiMappedVecAccMap()
                if 'RefGroupID' in indexRecords.dtype.names:
                    accMap['rname'] = (lambda x: x.RefGroupID)
            accMap['qname'] = P(accMap['qname'],
                                {v:k for k, v in movieMap.items()})
            # check for hdf resources:
            if 'MovieID' in indexRecords.dtype.names:
                # TODO(mdsmith)(2016-01-29) remove these once the fields are
                # renamed:
                accMap['movie'] = (lambda x: x.MovieID)
                accMap['qname'] = (lambda x: x.MovieID)
                accMap['zm'] = (lambda x: x.HoleNumber)
                accMap['length'] = (lambda x: x.rEnd - x.rStart)
        elif readType == 'fasta':
            accMap = {'id': (lambda x: x.id),
                      'length': (lambda x: x.length.astype(int)),
                     }
            typeMap = {'id': str,
                       'length': int,
                      }

        filterLastResult = np.zeros(len(indexRecords), dtype=np.bool_)
        for filt in self:
            lastResult = np.ones(len(indexRecords), dtype=np.bool_)
            for req in filt:
                param = req.name
                if param == 'qname_file':
                    param = 'qname'
                if param in accMap.keys():
                    # Treat "value" as a string of a list of potential values
                    # if operator is 'in', or 'in' masquerading as '=='.
                    # Have to be careful with bc and other values that are
                    # natively lists, but still single values
                    opstr = req.operator
                    value = req.value
                    if ((isListString(value) or isFile(value)) and
                            not param in ('cx', 'bc')) or param == 'qname':
                        if mapOp(opstr) == OP.eq:
                            opstr = 'in'
                        elif mapOp(opstr) == OP.ne:
                            opstr = 'not_in'

                    if opstr in ('in', 'not_in'):
                        if isFile(value):
                            value = fromFile(value)
                        elif isListString(value):
                            value = setify(value)
                    value = map_val_or_vec(typeMap[param], value)

                    if param == 'rname':
                        value = map_val_or_vec(nameMap.get, value)
                    elif param == 'movie':
                        value = map_val_or_vec(movieMap.get, value)
                    elif param == 'qname':
                        value = qname2vec(value)

                    if param == 'bc':
                        # convert string to list:
                        values = ast.literal_eval(value)
                        assert isinstance(values, list), (
                            'Barcode filter value must be of form [<bcf>, <bcr>]')
                        assert len(values) == 2, (
                            'Barcode filter value must be of form [<bcf>, <bcr>]')
                        param = 'bcf'
                        value = int(values[0])
                        operator = mapOp(opstr)
                        reqResultsForRecords = operator(
                            accMap[param](indexRecords), value)
                        param = 'bcr'
                        value = int(values[1])
                        operator = mapOp(opstr)
                        reqResultsForRecords &= operator(
                            accMap[param](indexRecords), value)
                    else:
                        operator = mapOp(opstr)
                        accessor = accMap[param]
                        if req.modulo is not None:
                            accessor = make_mod_hash_acc(accessor, req.modulo,
                                                          req.hashfunc)
                        reqResultsForRecords = operator(
                            accessor(indexRecords), value)
                    lastResult &= reqResultsForRecords
                    del reqResultsForRecords
                else:
                    log.warn("Filter not recognized: {f}".format(f=param))
            filterLastResult |= lastResult
            del lastResult
        return filterLastResult

    def fromString(self, filterString):
        # TODO(mdsmith)(2016-02-09) finish this
        filtDict = {}
        self._runCallbacks()

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
        if not kwargs:
            return
        # if there are already filters, you must copy the filters for each new
        # option and add one set of requirements to each option:
        if self.submetadata:
            origFilts = copy.deepcopy(list(self))
            self.record['children'] = []
            newFilts = [copy.deepcopy(origFilts) for _ in kwargs.values()[0]]
            for name, options in kwargs.items():
                for i, option in enumerate(options):
                    for filt in newFilts[i]:
                        val = option[1]
                        if isinstance(val, np.ndarray):
                            val = list(val)
                        filt.addRequirement(name, *option)
            for filtList in newFilts:
                self.extend(filtList)
        else:
            newFilts = [Filter() for _ in kwargs.values()[0]]
            for name, options in kwargs.items():
                for i, option in enumerate(options):
                    val = option[1]
                    if isinstance(val, np.ndarray):
                        val = list(val)
                    newFilts[i].addRequirement(name, *option)
            self.extend(newFilts)
        #log.debug("Current filters: {s}".format(s=str(self)))
        self._runCallbacks()

    def addFilter(self, **kwargs):
        """Use this to add filters. Members of the list will be considered
        requirements for fulfilling this option. Use multiple calls to add
        multiple filters.

        Args:
            name: The name of the requirement, e.g. 'rq'
            options: A list of (operator, value) tuples, e.g. ('>', '0.85')
        """
        if not kwargs:
            return
        newFilt = Filter()
        for name, options in kwargs.items():
            for option in options:
                newFilt.addRequirement(name, *option)
        self.append(newFilt)
        log.debug("Current filters: {s}".format(s=str(self)))
        self._runCallbacks()

    def addFilterList(self, filters):
        """
        filters is a list of options, with a list of reqs for each option. Each
        req is a tuple (name, oper, val)
        """
        if not filters:
            return
        for filt in filters:
            newFilt = Filter()
            for option in filt:
                newFilt.addRequirement(*option)
            self.append(newFilt)
        log.debug("Current filters: {s}".format(s=str(self)))
        self._runCallbacks()

    def broadcastFilters(self, filts):
        """
        Filt is a list of Filter objects or lists of reqs.
        Take all existing filters, duplicate and combine with each new filter
        """
        if not len(filts):
            # nothing to do
            return
        existing = [Filter()]
        if len(self):
            existing = copy.deepcopy(list(self))
        existing = [copy.deepcopy(existing) for _ in filts]

        new = []
        for filt, efilts in zip(filts, existing):
            if isinstance(filt, Filter):
                filt = [(p.name, p.operator, p.value) for p in filt]
            for efilt in efilts:
                for option in filt:
                    efilt.addRequirement(*option)
                new.append(efilt)

        while len(self):
            self.pop(0)
        for filt in new:
            self.append(filt)
        log.debug("Current filters: {s}".format(s=str(self)))
        self._runCallbacks()

    def removeFilter(self, index):
        self.pop(index)
        log.debug("Current filters: {s}".format(s=str(self)))
        self._runCallbacks()

    def mapRequirement(self, **kwargs):
        """Add requirements to each of the existing requirements, mapped one
        to one"""
        # Check that all lists of values are the same length:
        values = kwargs.values()
        if len(values) > 1:
            for v in values[1:]:
                assert len(v) == len(values[0])

        # Check that this length is equal to the current number of filters:
        assert len(kwargs.values()[0]) == len(list(self))

        for req, opvals in kwargs.items():
            for filt, opval in zip(self, opvals):
                filt.addRequirement(req, *opval)
        self._runCallbacks()

    def removeRequirement(self, req):
        log.debug("Removing requirement {r}".format(r=req))
        to_remove = []
        for i, filt in enumerate(self):
            empty = filt.removeRequirement(req)
            if empty:
                to_remove.append(i)
        for i in sorted(to_remove, reverse=True):
            self.pop(i)
        self._runCallbacks()


class Filter(RecordWrapper):
    NS = 'pbds'

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

    def addRequirement(self, name, operator, value, modulo=None):
        param = Property()
        param.name = name
        param.operator = operator
        param.value = value
        if modulo:
            param.modulo = modulo
            param.hashfunc = 'Uint32Cast'
        self.plist.append(param)

    def removeRequirement(self, req):
        to_remove = []
        for i, param in enumerate(self):
            if param.name == req:
                to_remove.append(i)
        for i in sorted(to_remove, reverse=True):
            self.pop(i)
        if len(self.plist):
            return False
        else:
            return True

    @property
    def plist(self):
        if self.record['children']:
            return Properties(self.record['children'][0])
        else:
            temp = Properties()
            self.append(temp)
            return temp

    def merge(self, other):
        pass

class Properties(RecordWrapper):
    NS = 'pbbase'

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

    def __getitem__(self, index):
        return Property(self.record['children'][index])

    def __iter__(self):
        for child in self.record['children']:
            yield Property(child)

    def merge(self, other):
        pass


class Property(RecordWrapper):
    NS = 'pbbase'

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

    def __str__(self):
        modstr = ''
        if self.modulo is not None:
            modstr = ' % {}'.format(self.modulo)
        namestr = self.name
        if self.hashfunc is not None:
            namestr = '{}({})'.format(self.hashfunc, self.name)
        return ''.join(["(", namestr, modstr, " ", self.operator, " ", self.value,
                        ")"])

    @property
    def modulo(self):
        #optional:
        if 'Modulo' not in self.metadata:
            return None
        value = self.metadata['Modulo']
        # I kind of want to support both types of modulo, but I want to use int
        # if possible...
        dtype = int
        if '.' in value or 'e' in value:
            dtype = float
        return dtype(value)

    @modulo.setter
    def modulo(self, value):
        self.metadata['Modulo'] = str(value)

    @property
    def hashfunc(self):
        #optional:
        if 'Hash' not in self.metadata:
            return None
        return self.metadata['Hash']

    @hashfunc.setter
    def hashfunc(self, value):
        self.metadata['Hash'] = value

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
        if isinstance(value, np.ndarray):
            if len(value.shape) > 1:
                raise RuntimeError(
                    "Cannot use multidimensional arrays as "
                    "filter values")
        if isinstance(value, (set, list, tuple, np.ndarray)):
            strval = '[{}]'.format(', '.join(map(str, value)))
        else:
            strval = str(value)
        self.metadata['Value'] = strval


class ExternalResources(RecordWrapper):
    NS = 'pbbase'

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

        # state tracking. Not good, but needs it:
        self._resourceIds = []

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

    def merge(self, other):
        # make sure we don't add dupes
        curIds = self.resourceIds

        # check to make sure ResourceIds in other are unique
        otherIds = Counter([res.resourceId for res in other])
        dupes = [c for c in otherIds if otherIds[c] > 1]
        if dupes:
            raise RuntimeError("Duplicate ResourceIds found: "
                               "{f}".format(f=', '.join(dupes)))

        for newRes in other:
            # merge instead
            if newRes.resourceId in curIds:
                indexof = curIds.index(newRes.resourceId)
                self[indexof].merge(newRes)
            else:
                self.append(newRes)
                curIds.append(newRes.resourceId)
        # we may be missing some metadata
        if not self.namespace:
            self.namespace = other.namespace
            self.attrib.update(other.attrib)


    def addResources(self, resourceIds):
        """Add a new external reference with the given uris. If you're looking
        to add ExternalResource objects, append() or extend() them instead.

        Args:
            resourceIds: a list of uris as strings
        """
        if not isinstance(resourceIds, list):
            resourceIds = [resourceIds]
        templist = []
        self._resourceIds = []
        for res in resourceIds:
            toAdd = res
            if not isinstance(res, ExternalResource):
                temp = ExternalResource()
                temp.resourceId = res
                toAdd = temp
            self.append(toAdd)
            templist.append(toAdd)
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
        self._resourceIds = []
        self.record['children'] = []
        for res in resources:
            self.append(res)

    @property
    def resourceIds(self):
        if not self._resourceIds:
            self._resourceIds = [res.resourceId for res in self]
        return self._resourceIds


class ExternalResource(RecordWrapper):
    NS = 'pbbase'

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__
        self.attrib.setdefault('UniqueId', newUuid(self.record))
        self.attrib.setdefault('TimeStampedName', '')

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

    metaType = accs('MetaType')
    timeStampedName = accs('TimeStampedName')
    tags = accs('Tags')

    @property
    def resourceId(self):
        return uri2fn(self.getV('attrib', 'ResourceId'))

    @resourceId.setter
    def resourceId(self, value):
        self.setV(value, 'attrib', 'ResourceId')
        dsuuid = getDataSetUuid(value)
        if dsuuid:
            self.uniqueId = dsuuid

    @property
    def bam(self):
        return self.resourceId

    @property
    def pbi(self):
        indices = self.indices
        for index in indices:
            if index.metaType == 'PacBio.Index.PacBioIndex':
                return index.resourceId

    @pbi.setter
    def pbi(self, value):
        self._setIndResByMetaType('PacBio.Index.PacBioIndex', value)

    @property
    def bai(self):
        indices = self.indices
        for index in indices:
            if index.metaType == 'PacBio.Index.BamIndex':
                return index.resourceId

    @property
    def gmap(self):
        """Unusual: returns the gmap external resource instead of the resId"""
        return self._getSubExtResByMetaType('PacBio.GmapDB.GmapDBPath')

    @gmap.setter
    def gmap(self, value):
        """Sets the resourceId"""
        self._setSubResByMetaType('PacBio.GmapDB.GmapDBPath', value)

    @property
    def sts(self):
        return self._getSubResByMetaType('PacBio.SubreadFile.ChipStatsFile')

    @sts.setter
    def sts(self, value):
        self._setSubResByMetaType('PacBio.SubreadFile.ChipStatsFile', value)

    @property
    def scraps(self):
        if self.metaType == 'PacBio.SubreadFile.SubreadBamFile':
            return self._getSubResByMetaType(
                'PacBio.SubreadFile.ScrapsBamFile')
        elif self.metaType == 'PacBio.SubreadFile.ZmwBamFile':
            return self._getSubResByMetaType(
                'PacBio.SubreadFile.ZmwScrapsBamFile')
        elif self.metaType == 'PacBio.SubreadFile.Control.SubreadBamFile':
            return self._getSubResByMetaType(
                'PacBio.SubreadFile.Control.ScrapsBamFile')

    @scraps.setter
    def scraps(self, value):
        # metaType isn't populated right off the bat. We'll provide an option
        # to check against the filename for now, but this should change in
        # DataSetReader eventually
        if (self.metaType == 'PacBio.SubreadFile.Control.SubreadBamFile' or
                self.resourceId.endswith('control.subreads.bam')):
            self._setSubResByMetaType(
                'PacBio.SubreadFile.Control.ScrapsBamFile', value)
        elif (self.metaType == 'PacBio.SubreadFile.SubreadBamFile' or
              self.resourceId.endswith('subreads.bam')):
            self._setSubResByMetaType(
                'PacBio.SubreadFile.ScrapsBamFile', value)
        elif (self.metaType == 'PacBio.SubreadFile.ZmwBamFile' or
              self.resourceId.endswith('zmws.bam')):
            self._setSubResByMetaType(
                'PacBio.SubreadFile.ZmwScrapsBamFile', value)

    @property
    def control(self):
        return self._getSubResByMetaType(
            'PacBio.SubreadFile.Control.SubreadBamFile')

    @control.setter
    def control(self, value):
        self._setSubResByMetaType('PacBio.SubreadFile.Control.SubreadBamFile', value)

    @property
    def barcodes(self):
        return self._getSubResByMetaType("PacBio.DataSet.BarcodeSet")

    @barcodes.setter
    def barcodes(self, value):
        self._setSubResByMetaType("PacBio.DataSet.BarcodeSet", value)

    @property
    def reference(self):
        return self._getSubResByMetaType(
            'PacBio.ReferenceFile.ReferenceFastaFile')

    @reference.setter
    def reference(self, value):
        self._setSubResByMetaType('PacBio.ReferenceFile.ReferenceFastaFile',
                                  value)

    @property
    def adapters(self):
        return self._getSubResByMetaType(
            'PacBio.SubreadFile.AdapterFastaFile')

    @adapters.setter
    def adapters(self, value):
        self._setSubResByMetaType('PacBio.SubreadFile.AdapterFastaFile',
                                  value)

    def _deleteIndByMetaType(self, mType):
        rm = []
        for i, res in enumerate(self.indices):
            if res.metaType == mType:
                rm.append(i)
        for i in sorted(rm, reverse=True):
            self.indices.pop(i)

    def _getIndByMetaType(self, mType):
        resources = self.indices
        for res in resources:
            if res.metaType == mType:
                return res

    def _getIndResByMetaType(self, mType):
        res = self._getIndByMetaType(mType)
        if not res is None:
            return res.resourceId

    def _setIndResByMetaType(self, mType, value):
        if not isinstance(value, FileIndex):
            tmp = FileIndex()
            tmp.resourceId = value
        else:
            tmp = value
        extant = self._getIndByMetaType(mType)
        if extant:
            if value is None:
                self._deleteIndByMetaType(mType)
            else:
                extant.resourceId = value
        else:
            tmp.metaType = mType
            tmp.timeStampedName = getTimeStampedName(mType)
            resources = self.indices
            # externalresources objects have a tag by default, which means their
            # truthiness is true. Perhaps a truthiness change is in order
            # TODO: (mdsmith 20160728) this can be updated now that the
            # retention and tag system has been refactored
            if len(resources) == 0:
                resources = FileIndices()
                resources.append(tmp)
                self.append(resources)
            else:
                resources.append(tmp)

    def _deleteExtResByMetaType(self, mType):
        rm = []
        for i, res in enumerate(self.externalResources):
            if res.metaType == mType:
                rm.append(i)
        for i in sorted(rm, reverse=True):
            self.externalResources.pop(i)

    def _getSubExtResByMetaType(self, mType):
        resources = self.externalResources
        for res in resources:
            if res.metaType == mType:
                return res

    def _getSubResByMetaType(self, mType):
        res = self._getSubExtResByMetaType(mType)
        if not res is None:
            return res.resourceId

    def _setSubResByMetaType(self, mType, value):
        if not isinstance(value, ExternalResource):
            tmp = ExternalResource()
            tmp.resourceId = value
        else:
            tmp = value
        extant = self._getSubExtResByMetaType(mType)
        if extant:
            if value is None:
                self._deleteExtResByMetaType(mType)
            else:
                extant.resourceId = value
        else:
            tmp.metaType = mType
            tmp.timeStampedName = getTimeStampedName(mType)
            resources = self.externalResources
            # externalresources objects have a tag by default, which means their
            # truthiness is true. Perhaps a truthiness change is in order
            # TODO: (mdsmith 20160728) this can be updated now that the
            # retention and tag system has been refactored
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
            fileIndices = FileIndices(fileIndices[0])
        else:
            fileIndices = FileIndices()
            self.append(fileIndices)
        for index in list(indices):
            temp = FileIndex()
            temp.resourceId = index
            fileIndices.append(temp)

class FileIndices(RecordWrapper):
    NS = 'pbbase'

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

    def __getitem__(self, index):
        return FileIndex(self.record['children'][index])

    def __iter__(self):
        for child in self.record['children']:
            yield FileIndex(child)


class FileIndex(RecordWrapper):
    NS = 'pbbase'

    KEEP_WITH_PARENT = True

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__
        self.attrib.setdefault('UniqueId', newUuid(self.record))
        self.attrib.setdefault('TimeStampedName', '')

    resourceId = accs('ResourceId')
    metaType = accs('MetaType')
    timeStampedName = accs('TimeStampedName')


class DataSetMetadata(RecordWrapper):
    """The root of the DataSetMetadata element tree, used as base for subtype
    specific DataSet or for generic "DataSet" records."""
    TAG = 'DataSetMetadata'
    NS = 'pbds'

    def __init__(self, record=None):
        """Here, record is the root element of the Metadata Element tree"""
        super(DataSetMetadata, self).__init__(record)
        self.record['tag'] = self.TAG

    def merge(self, other):
        self.numRecords += other.numRecords
        self.totalLength += other.totalLength
        if other.summaryStats:
            if self.summaryStats:
                self.summaryStats.merge(other.summaryStats)
            else:
                self.append(other.summaryStats)
        if not self.namespace:
            self.namespace = other.namespace
            self.attrib.update(other.attrib)

    @property
    def numRecords(self):
        """Return the number of records in a DataSet using helper functions
        defined in the base class"""
        return self.getMemberV('NumRecords', default=0, asType=int)

    @numRecords.setter
    def numRecords(self, value):
        """Set the number of records, primarily when merging two DataSets"""
        self.setMemberV('NumRecords', str(value))

    @property
    def totalLength(self):
        """Return the TotalLength property of this dataset.
        TODO: update the value from the actual external reference on
        ValueError"""
        return self.getMemberV('TotalLength', default=0, asType=int)

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

    @summaryStats.setter
    def summaryStats(self, value):
        self.removeChildren('SummaryStats')
        if value:
            self.append(value)

    @property
    def provenance(self):
        try:
            return Provenance(self.getV('children', 'Provenance'))
        except ValueError:
            return None

    @provenance.setter
    def provenance(self, value):
        self.removeChildren('Provenance')
        if value:
            self.append(value)

    def addParentDataSet(self, uniqueId, metaType, timeStampedName="",
                         createdBy="AnalysisJob"):
        """
        Add a ParentDataSet record in the Provenance section.  Currently only
        used for SubreadSets.
        """
        new = Provenance()
        new.createdBy = createdBy
        new.addParentDataSet(uniqueId, metaType, timeStampedName)
        self.provenance = new
        self._runCallbacks()


class SubreadSetMetadata(DataSetMetadata):
    """The DataSetMetadata subtype specific to SubreadSets. Deals explicitly
    with the merging of Collections metadata hierarchies."""

    TAG = 'DataSetMetadata'

    def __init__(self, record=None):
        # This doesn't really need to happen unless there are contextual
        # differences in the meanings of subtypes (e.g. Collections mean
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
        if other.collections and not self.collections:
            self.append(other.collections)
        else:
            self.collections.merge(other.collections)

    @property
    def collections(self):
        """Return a list of wrappers around Collections elements of the
        Metadata Record"""
        return CollectionsMetadata(self.getV(tag='Collections',
                                             container='children'),
                                   parent=self)

    @collections.setter
    def collections(self, value):
        self.removeChildren('Collections')
        if value:
            self.append(value)

    def getMovieSampleNames(self):
        """
        Map the BioSample names in metadata Collection to "context" ID, i.e.
        movie names.  Used for deconvoluting multi-sample
        inputs.  This function will raise a KeyError if a movie name is not
        unique, or a ValueError if there is not a 1-to-1 mapping of sample to
        to movie.
        """
        movie_to_sample = {}
        for collection in self.collections:
            bio_samples = [b.name for b in collection.wellSample.bioSamples]
            movie_name = collection.context
            n_bio_samples = len(bio_samples)
            if n_bio_samples == 1:
                if movie_to_sample.get(movie_name, None) == bio_samples[0]:
                    raise KeyError("Collection context {c} occurs more than once".format(c=movie_name))
                movie_to_sample[movie_name] = bio_samples[0]
            elif n_bio_samples == 0:
                raise ValueError("No BioSample records for collection {c}".format(c=movie_name))
            else:
                raise ValueError("Collection {c} has multiple BioSample records".format(c=movie_name))
        return movie_to_sample


class ContigSetMetadata(DataSetMetadata):
    """The DataSetMetadata subtype specific to ContigSets."""

    TAG = 'DataSetMetadata'

    def __init__(self, record=None):
        if record:
            if (not isinstance(record, dict) and
                    not isinstance(record, ContigSetMetadata) and
                    type(record).__name__ != 'DataSetMetadata'):
                raise TypeError("Cannot create ContigSetMetadata from "
                                "{t}".format(t=type(record).__name__))
        super(ContigSetMetadata, self).__init__(record)

    organism = subaccs('Organism')
    ploidy = subaccs('Ploidy')


class BarcodeSetMetadata(DataSetMetadata):
    """The DataSetMetadata subtype specific to BarcodeSets."""

    TAG = 'DataSetMetadata'

    def __init__(self, record=None):
        if record:
            if (not isinstance(record, dict) and
                    not isinstance(record, BarcodeSetMetadata) and
                    type(record).__name__ != 'DataSetMetadata'):
                raise TypeError("Cannot create BarcodeSetMetadata from "
                                "{t}".format(t=type(record).__name__))
        super(BarcodeSetMetadata, self).__init__(record)

    barcodeConstruction = subaccs('BarcodeConstruction')


class CollectionsMetadata(RecordWrapper):
    """The Element should just have children: a list of
    CollectionMetadataTags"""
    TAG = 'Collections'
    NS = 'pbmeta'

    def __getitem__(self, index):
        return CollectionMetadata(self.record['children'][index])

    def __iter__(self):
        for child in self.record['children']:
            yield CollectionMetadata(child)

    def merge(self, other, forceUnique=False):
        if forceUnique:
            collectionIds = {child.uniqueId for child in self}
            for child in other:
                if not child.uniqueId in collectionIds:
                    self.append(child)
                    collectionIds.add(child.uniqueId)
        else:
            self.extend([child for child in other])


class AutomationParameter(RecordWrapper):
    NS = 'pbbase'

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

    value = accs('SimpleValue')


class AutomationParameters(RecordWrapper):
    NS = 'pbbase'

    def __init__(self, record=None):
        super(self.__class__, self).__init__(record)
        self.record['tag'] = self.__class__.__name__

    automationParameter = accs('AutomationParameter', container='children',
                               asType=AutomationParameter)

    def addParameter(self, key, value):
        temp = AutomationParameter()
        if key:
            temp.name = key
        if value:
            temp.value = value
        self.append(temp)

    def __getitem__(self, tag):
        """Override to use tag as Name instead of strictly tag"""
        if isinstance(tag, str):
            for child in self:
                child = AutomationParameter(child)
                if child.name == tag:
                    return child
            return RecordWrapper(self.getV('children', tag))
        elif isinstance(tag, int):
            return RecordWrapper(self.record['children'][tag])

    @property
    def parameterNames(self):
        return [c.name for c in self]


class Automation(RecordWrapper):
    NS = 'pbmeta'

    automationParameters = accs('AutomationParameters', container='children',
                                asType=AutomationParameters)


class ParentTool(RecordWrapper):
    NS = 'pbds'


class ParentDataSet(RecordWrapper):
    NS = 'pbds'

    metaType = accs("MetaType")
    timeStampedName = accs('TimeStampedName')


class Provenance(RecordWrapper):
    """The metadata concerning this dataset's provenance"""
    NS = 'pbds'

    createdBy = accs('CreatedBy')
    parentTool = accs('ParentTool', container='children', asType=ParentTool)
    parentDataSet = accs("ParentDataSet", container="children", asType=ParentDataSet)

    def addParentDataSet(self, uniqueId, metaType, timeStampedName):
        new = ParentDataSet()
        new.uniqueId = uniqueId
        new.metaType = metaType
        new.timeStampedName = timeStampedName
        self.append(new)
        self._runCallbacks()
        return new


class StatsMetadata(RecordWrapper):
    """The metadata from the machine sts.xml"""

    # merged dists:
    MERGED_DISTS = ["ProdDist", "ReadTypeDist", "ReadLenDist", "ReadQualDist",
                    "MedianInsertDist", "InsertReadQualDist",
                    "InsertReadLenDist", "ControlReadQualDist",
                    "ControlReadLenDist"]

    # continuous channel dists:
    CHANNEL_DISTS = ['BaselineLevelDist', 'BaselineStdDist', 'SnrDist',
                     'HqRegionSnrDist', 'HqBasPkMidDist',
                     'BaselineLevelSequencingDist',
                     'TotalBaseFractionPerChannel', 'DmeAngleEstDist']

    # continuous misc. dists:
    OTHER_DISTS = ['PausinessDist', 'PulseRateDist', 'PulseWidthDist',
                   'BaseRateDist', 'BaseWidthDist', 'BaseIpdDist',
                   'LocalBaseRateDist', 'NumUnfilteredBasecallsDist',
                   'HqBaseFractionDist', 'NumUnfilteredBasecallsDist']

    UNMERGED_DISTS = CHANNEL_DISTS + OTHER_DISTS

    def getDist(self, key, unwrap=True):
        tbr = list(self.findChildren(key))
        if len(tbr) == 0:
            return None

        dtype = ContinuousDistribution
        if tbr[0].getV('children', 'BinLabels') is not None:
            dtype = DiscreteDistribution

        if unwrap and key in self.MERGED_DISTS:
            if len(tbr) > 1:
                log.warn("Merging a distribution failed!")
            return dtype(tbr[0])
        elif 'Channel' in tbr[0].attrib:
            chans = defaultdict(list)
            for chan in tbr:
                chans[chan.attrib['Channel']].append(
                    dtype(chan))
            return chans
        else:
            return map(dtype, tbr)

    def availableDists(self):
        return [c.metaname for c in self]

    def __getitem__(self, key):
        return self.getDist(key)

    @property
    def channelDists(self):
        """This can be modified to use the new accessors above instead of the
        brittle list of channel dists above"""
        tbr = {}
        for dist in self.CHANNEL_DISTS:
            chans = defaultdict(list)
            for chan in self.findChildren(dist):
                chans[chan.attrib['Channel']].append(
                    ContinuousDistribution(chan))
            tbr[dist] = chans
        return tbr

    @property
    def otherDists(self):
        """This can be modified to use the new accessors above instead of the
        brittle list of dists above"""
        tbr = defaultdict(list)
        for disttype in self.OTHER_DISTS:
            for dist in self.findChildren(disttype):
                tbr[disttype].append(ContinuousDistribution(dist))
        return tbr

    def merge(self, other):
        """This can be modified to use the new accessors above instead of the
        brittle list of dists above"""
        if (other.shortInsertFraction and other.prodDist and
                self.shortInsertFraction and self.prodDist):
            self.shortInsertFraction = (self.shortInsertFraction *
                                        self.prodDist.bins[1] +
                                        other.shortInsertFraction *
                                        other.prodDist.bins[1])/(
                                            self.prodDist.bins[1]
                                            + other.prodDist.bins[1])
        if (other.adapterDimerFraction and other.prodDist and
                self.shortInsertFraction and self.prodDist):
            self.adapterDimerFraction = (self.adapterDimerFraction *
                                         self.prodDist.bins[1] +
                                         other.adapterDimerFraction *
                                         other.prodDist.bins[1])/(
                                             self.prodDist.bins[1]
                                             + other.prodDist.bins[1])
        if other.shortInsertFraction and not self.shortInsertFraction:
            self.shortInsertFraction = other.shortInsertFraction
        if other.adapterDimerFraction and not self.adapterDimerFraction:
            self.adapterDimerFraction = other.adapterDimerFraction
        if other.prodDist and not self.prodDist:
            self.append(other.prodDist)
        self.numSequencingZmws += other.numSequencingZmws

        for dist in self.MERGED_DISTS:
            selfDist = getattr(self, dist[0].lower() + dist[1:])
            otherDist = getattr(other, dist[0].lower() + dist[1:])
            if not selfDist:
                if otherDist:
                    self.append(otherDist)
            else:
                try:
                    selfDist.merge(otherDist)
                except ZeroBinWidthError as e:
                    removed = self.removeChildren(dist)
                    self.append(otherDist)
                except BinMismatchError:
                    self.append(otherDist)

        for dist in self.UNMERGED_DISTS:
            otherDists = other.findChildren(dist)
            for otherDist in otherDists:
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
    def insertReadLenDists(self):
        return [ContinuousDistribution(child) for child in
                self.findChildren('InsertReadLenDist')]

    @property
    def insertReadLenDist(self):
        return ContinuousDistribution(self.getV('children',
                                                'InsertReadLenDist'))
    @property
    def insertReadQualDists(self):
        return [ContinuousDistribution(child) for child in
                self.findChildren('InsertReadQualDist')]

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
        return self.getMemberV('AdapterDimerFraction', asType=float)

    @adapterDimerFraction.setter
    def adapterDimerFraction(self, value):
        self.setMemberV('AdapterDimerFraction', float(value))

    @property
    def numSequencingZmws(self):
        return self.getMemberV('NumSequencingZmws', asType=float)

    @numSequencingZmws.setter
    def numSequencingZmws(self, value):
        self.setMemberV('NumSequencingZmws', float(value))

    @property
    def shortInsertFraction(self):
        return self.getMemberV('ShortInsertFraction', asType=float)

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

def histogram_percentile(counts, labels, percentile):
    thresh = np.true_divide(percentile * sum(counts), 100.0)
    passed = 0
    for c, l in zip(counts, labels):
        passed += c
        if passed >= thresh:
            return l
    return labels[-1]

class ContinuousDistribution(RecordWrapper):

    def merge(self, other):
        if other.binWidth == 0:
            return
        if self.binWidth == 0:
            raise ZeroBinWidthError(self.binWidth, other.binWidth)
        if self.binWidth != other.binWidth:
            raise BinWidthMismatchError(self.binWidth, other.binWidth)
        if (self.minBinValue % self.binWidth
                != other.minBinValue % other.binWidth):
            raise BinBoundaryMismatchError(self.minBinValue, other.minBinValue)
        self.bins = list(_staggeredZip(self.binWidth, self.minBinValue,
                                       other.minBinValue, self.bins,
                                       other.bins))
        self.minBinValue = min(self.minBinValue, other.minBinValue)
        self.maxBinValue = max(self.maxBinValue, other.maxBinValue)
        self.minOutlierValue = min(self.minOutlierValue, other.minOutlierValue)
        self.maxOutlierValue = max(self.maxOutlierValue, other.maxOutlierValue)

        def _true_divide(num, denom):
            if denom == 0:
                return 0
            else:
                return np.true_divide(num, denom)

        # Std merging is somewhat complicated:
        selfweight = _true_divide(self.sampleSize,
                                  (self.sampleSize + other.sampleSize))
        otherweight = _true_divide(other.sampleSize,
                                   (self.sampleSize + other.sampleSize))
        selfsum = self.sampleMean * self.sampleSize
        othersum = other.sampleMean * other.sampleSize
        selfval = otherval = 0
        if self.sampleSize > 0:
            selfval = ((self.sampleStd ** 2) * (self.sampleSize - 1) +
                       ((selfsum) ** 2) / self.sampleSize)
        if other.sampleSize > 0:
            otherval = ((other.sampleStd ** 2) * (other.sampleSize - 1) +
                        ((othersum) ** 2) / other.sampleSize)
        sums = selfsum + othersum
        vals = selfval + otherval
        tots = self.sampleSize + other.sampleSize
        if tots > 1:
            self.sampleStd = np.sqrt((vals - (sums ** 2) / tots) / (tots - 1))
        else:
            self.sampleStd = 0

        # The others are pretty simple:
        self.sampleMean = ((self.sampleMean * selfweight) +
                           (other.sampleMean * otherweight))
        self.sampleSize = self.sampleSize + other.sampleSize

        # These two are approximations:
        if np.sum(self.bins):
            self.sampleMed = histogram_percentile(
                self.bins,
                (np.array(self.labels) + self.binWidth / 2.0),
                50)
            self.sample95thPct = histogram_percentile(
                self.bins,
                (np.array(self.labels) + self.binWidth / 2.0),
                95)
        else:
            self.sampleMed = 0
            self.sample95thPct = 0

    numBins = subaccs('NumBins', asType=int)
    sampleSize = subaccs('SampleSize', asType=int)
    sampleMean = subaccs('SampleMean', asType=float)
    sampleMed = subaccs('SampleMed', asType=float)
    sampleMedian = subaccs('SampleMed', asType=float)
    sampleMode = subaccs('SampleMode', asType=float)
    sampleStd = subaccs('SampleStd', asType=float)
    sample95thPct = subaccs('Sample95thPct', asType=float)
    binWidth = subaccs('BinWidth', asType=float)
    minOutlierValue = subaccs('MinOutlierValue', asType=float)
    maxOutlierValue = subaccs('MaxOutlierValue', asType=float)
    minBinValue = subaccs('MinBinValue', asType=float)
    maxBinValue = subaccs('MaxBinValue', asType=float)


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

class ZeroBinWidthError(Exception):

    def __init__(self, width1, width2):
        self.width1 = width1
        self.width2 = width2

    def __str__(self):
        return "Zero bin width: {w1}, {w2}".format(w1=self.width1,
                                                   w2=self.width2)

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
        return self.getMemberV('NumBins', asType=int)

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

    TAG = 'RunDetails'
    NS = 'pbmeta'

    timeStampedName = subgetter('TimeStampedName')
    name = subaccs('Name')


class BioSamplesMetadata(RecordWrapper):
    """The metadata for the list of BioSamples

        Doctest:
            >>> from __future__ import print_function
            >>> from pbcore.io import SubreadSet
            >>> import pbcore.data.datasets as data
            >>> ds = SubreadSet(data.getSubreadSet(), skipMissing=True)
            >>> ds.metadata.collections[0].wellSample.bioSamples[0].name
            'consectetur purus'
            >>> for bs in ds.metadata.collections[0].wellSample.bioSamples:
            ...     print(bs.name)
            consectetur purus
            >>> em = {'tag':'BioSample', 'text':'', 'children':[],
            ...       'attrib':{'Name':'great biosample'}}
            >>> ds.metadata.collections[0].wellSample.bioSamples.append(em)
            >>> ds.metadata.collections[0].wellSample.bioSamples[1].name
            'great biosample'
        """

    TAG = 'BioSamples'
    NS = 'pbsample'

    def __getitem__(self, index):
        """Get a biosample"""
        return BioSampleMetadata(self.record['children'][index])

    def __iter__(self):
        """Iterate over biosamples"""
        for child in self.record['children']:
            yield BioSampleMetadata(child)

    def addSample(self, name):
        new = BioSampleMetadata()
        new.name = name
        self.append(new)
        self._runCallbacks()


class DNABarcode(RecordWrapper):
    TAG = 'DNABarcode'
    NS = 'pbsample'


class DNABarcodes(RecordWrapper):
    TAG = 'DNABarcodes'
    NS = 'pbsample'

    def __getitem__(self, index):
        """Get a DNABarcode"""
        return DNABarcode(self.record['children'][index])

    def __iter__(self):
        """Iterate over DNABarcode"""
        for child in self.record['children']:
            yield DNABarcode(child)

    def addBarcode(self, name):
        new = DNABarcode()
        new.name = name
        self.append(new)
        self._runCallbacks()


class BioSampleMetadata(RecordWrapper):
    """The metadata for a single BioSample"""
    TAG = 'BioSample'
    NS = 'pbsample'

    DNABarcodes = accs('DNABarcodes', 'children', DNABarcodes, parent=True)


class WellSampleMetadata(RecordWrapper):
    TAG = 'WellSample'
    NS = 'pbmeta'

    wellName = subaccs('WellName')
    concentration = subaccs('Concentration')
    sampleReuseEnabled = subgetter('SampleReuseEnabled')
    stageHotstartEnabled = subgetter('StageHotstartEnabled')
    sizeSelectionEnabled = subgetter('SizeSelectionEnabled')
    useCount = subaccs('UseCount')
    comments = subaccs('Comments')
    bioSamples = accs('BioSamples', 'children', BioSamplesMetadata,
                      parent=True)

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)


class CopyFilesMetadata(RecordWrapper):
    """The CopyFile members don't seem complex enough to justify
    class representation, instead rely on base class methods"""
    TAG = 'CopyFiles'


class OutputOptions(RecordWrapper):
    NS = 'pbmeta'

    resultsFolder = subaccs('ResultsFolder')
    collectionPathUri = subaccs('CollectionPathUri')
    copyFiles = accs('CopyFiles', container='children',
                     asType=CopyFilesMetadata)


class SecondaryMetadata(RecordWrapper):
    TAG = 'Secondary'
    cellCountInJob = subaccs('CellCountInJob')


class PrimaryMetadata(RecordWrapper):
    """

    Doctest:
        >>> import os, tempfile
        >>> from pbcore.io import SubreadSet
        >>> import pbcore.data.datasets as data
        >>> ds1 = SubreadSet(data.getXml(5), skipMissing=True)
        >>> ds1.metadata.collections[0].primary.outputOptions.resultsFolder
        'Analysis_Results'
        >>> ds1.metadata.collections[0].primary.outputOptions.resultsFolder = (
        ...     'BetterAnalysis_Results')
        >>> ds1.metadata.collections[0].primary.outputOptions.resultsFolder
        'BetterAnalysis_Results'
        >>> outdir = tempfile.mkdtemp(suffix="dataset-doctest")
        >>> outXml = 'xml:' + os.path.join(outdir, 'tempfile.xml')
        >>> ds1.write(outXml, validate=False)
        >>> ds2 = SubreadSet(outXml, skipMissing=True)
        >>> ds2.metadata.collections[0].primary.outputOptions.resultsFolder
        'BetterAnalysis_Results'
    """

    TAG = 'Primary'
    NS = 'pbmeta'

    automationName = subaccs('AutomationName')
    configFileName = subaccs('ConfigFileName')
    sequencingCondition = subaccs('SequencingCondition')
    outputOptions = accs('OutputOptions', container='children',
                         asType=OutputOptions)

class Kit(RecordWrapper):
    partNumber = accs('PartNumber')
    lotNumber = accs('LotNumber')
    barcode = accs('Barcode')
    expirationDate = accs('ExpirationDate')

class CellPac(Kit):
    NS = 'pbmeta'

class TemplatePrepKit(Kit):
    """TemplatePrepKit metadata"""

    rightAdaptorSequence = subaccs('RightAdaptorSequence')
    leftAdaptorSequence = subaccs('LeftAdaptorSequence')

class BindingKit(Kit):
    pass

class SequencingKitPlate(Kit):
    pass


class ConsensusReadSetRef(RecordWrapper):
    uuid = accs("UniqueId")


class CollectionMetadata(RecordWrapper):
    """The metadata for a single collection. It contains Context,
    InstrumentName etc. as attribs, InstCtrlVer etc. for children"""

    TAG = 'CollectionMetadata'
    NS = 'pbmeta'

    context = accs('Context')
    instrumentName = accs('InstrumentName')
    instrumentId = accs('InstrumentId')
    instCtrlVer = subaccs('InstCtrlVer')
    sigProcVer = subaccs('SigProcVer')
    collectionNumber = subaccs('CollectionNumber')
    cellIndex = subaccs('CellIndex')
    cellPac = accs('CellPac', 'children', CellPac)
    templatePrepKit = accs('TemplatePrepKit', 'children', TemplatePrepKit)
    bindingKit = accs('BindingKit', 'children', BindingKit)
    sequencingKitPlate = accs('SequencingKitPlate', 'children',
                              SequencingKitPlate)
    automation = accs('Automation', 'children', Automation)
    primary = accs('Primary', 'children', PrimaryMetadata)
    secondary = accs('Secondary', 'children', SecondaryMetadata)
    consensusReadSetRef = accs("ConsensusReadSetRef", 'children', ConsensusReadSetRef)

    @property
    def runDetails(self):
        return RunDetailsMetadata(self.getV('children', 'RunDetails'),
                                  parent=self)

    @property
    def wellSample(self):
        return WellSampleMetadata(self.getV('children', 'WellSample'),
                                  parent=self)


def _emptyMember(tag=None, text=None, attrib=None, children=None,
                 namespace=None):
    """Return an empty stock Element representation"""
    if tag is None:
        tag = ''
    if namespace is None:
        namespace = ''
    if text is None:
        text = ''
    if attrib is None:
        attrib = {}
    if children is None:
        children = []
    return {'tag': tag, 'text': text, 'attrib': attrib, 'children': children,
            'namespace': namespace}
