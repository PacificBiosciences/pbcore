#
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
#

"""
Data model and I/O support for managing a simple sequence repository.

ReferenceIndex models the repository index structure (index.xml).  It
contains a sequence of ReferenceIndexEntry.

ReferenceEntry models an individual reference entry.  It contains meta
data (ReferenceInfo) and contigs (ReferenceContig).
"""

__all__ = ["ReferenceEntry",
           "ReferenceIndex"]

import os
import glob
import time
import re
import hashlib
from pbcore.io import FastaReader
from xml.etree.cElementTree import *

DEFAULT_VERSION = '1.0.0'


class ReferenceEntry(object):

    "Models an entry in the reference repository."

    def __init__(self, referenceDir=None):
        self._organism = Organism(None)
        self._contigs = []
        self._annotations = []
        self._id = None
        self._indexBy = {"Name": {}, "Id": {}, "Header": {}}
        if not referenceDir:
            self._path = None
            return
        self._path = os.path.abspath(referenceDir)
        if os.path.isdir(referenceDir):
            self._loadMetaData()
            self.is_pseudo_entry = False
        else:
            self._createEntryFromFile()
            self.is_pseudo_entry = True

    def cacheLookups(self):
        """Generates mappings from Name, Id, and Header to the contig"""
        """index for fast lookup using getContig()."""
        for i, contig in enumerate(self._contigs):
            self._indexBy["Name"][contig.name] = i
            self._indexBy["Id"][contig.id] = i
            self._indexBy["Header"][contig.header] = i

    def _findMetaDataFile(self):
        metaDataFile = os.path.join(self._path, 'reference.info.xml')
        # if the canonical file is not found, try to find another xml file
        # that might be the metadata file
        if not os.path.exists(metaDataFile):
            xmlFiles = glob.glob('%s/*xml' % self._path)
            if len(xmlFiles) > 0:
                metaDataFile = xmlFiles[0]
            else:
                metaDataFile = None
        return metaDataFile

    def _loadMetaData(self):
        self._metaDataFile = self._findMetaDataFile()
        if self._metaDataFile is None:
            raise ReferenceXmlException(
                "Can't find meta-data XML file for %s" % self._path)
            return
        tree = ElementTree(file=self._metaDataFile)
        root = tree.getroot()
        if root.tag != 'reference_info':
            raise ReferenceXmlException(
                "Expected <reference_info> element in %s" % self._path)
        self._id = root.attrib['id']
        self._version = DEFAULT_VERSION
        if 'version' in root.attrib:
            self._version = root.attrib['version']

        organism = root.findall('organism')
        if len(organism) > 1:
            raise ReferenceXmlException(
                "Only one organism allowed!")
        for o in organism:
            self._organism = Organism(o)

        self._info = ReferenceInfo(self, root, self._path)
        contigs = root.findall('contigs/contig')
        for contigElement in contigs:
            contig = ReferenceContig(self, contigElement, self._path)
            self._contigs.append(contig)
        annotations = root.findall('annotations/annotation')
        for annotationElement in annotations:
            annotation = ReferenceAnnotation(annotationElement, self._path)
            self._annotations.append(annotation)

    def _createEntryFromFile(self):
        self._id = os.path.splitext(os.path.basename(self._path))[0]
        self._info = ReferenceInfo(self)
        self._info._file = self._path
        self._contigs = []
        for seq in FastaReader(self._path):
            contig = ReferenceContig(self)
            contig._name = seq.getTag()
            contig._id = contig._name
            self._contigs.append(contig)

    @property
    def id(self):
        return self._id

    @property
    def numContigs(self):
        return len(self._contigs)

    @property
    def sequenceFiles(self):
        if self._info._file:
            return [self._info._file]
        else:
            return [c.path for c in self._contigs]

    @property
    def contigs(self):
        "Returns sequence of ReferenceContig"
        return self._contigs

    @property
    def annotations(self):
        "Returns sequence of ReferenceAnnotation"
        return self._annotations

    @property
    def organism(self):
        '''Returns the organism.'''
        return self._organism

    @property
    def info(self):
        return self._info

    @property
    def path(self):
        "Path in the reference repository where this entry is located."
        return self._path

    def getContig(self, id):
        "retrieve a contig by id (first) or header (second) or name (third)"
        # Try fast cached lookup first. Call self.cacheLookups() to enable
        for key in self._indexBy:
            if id in self._indexBy[key]:
                return self.contigs[self._indexBy[key][id]]

        for c in self.contigs:
            if c.id == id:
                return c
        # try search by header
        for c in self.contigs:
            if c.header == id:
                return c
        # try search by name
        for c in self.contigs:
            if c.name == id:
                return c
        return None

    def save(self, outfile):
        """Write a reference.info.xml to the supplied output stream.  Useful
        for development."""
        root = Element("reference_info")
        root.attrib["id"] = self.id
        root.attrib["version"] = "1.0.0"
        root.attrib["last_modified"] = now_in_iso()
        root.append(self._organism.toElement())

        reference = self._info.toElement()
        root.append(reference)
        if self.numContigs > 0:
            contigs = SubElement(root, "contigs")
            for i, c in enumerate(self.contigs):
                e = c.toElement()
                e.attrib["id"] = 'ref%06d' % (i + 1)
                contigs.append(e)
        if len(self._annotations) > 0:
            annotations = SubElement(root, "annotations")
            for a in self.annotations:
                annotations.append(a.toElement())

        print >>outfile, '<?xml version="1.0" encoding="utf-8"?>'
        print >>outfile, prettify(root)


class ReferenceXmlException(Exception):

    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return repr(self._msg)


def get_text_from_child(root, childName, required=False):
    element = root.find(childName)
    if element is not None:
        text = element.text
        if text is not None:
            return text.strip()
        else:
            return ''
    else:
        if required:
            raise ReferenceXmlException("Couldn't find required element <%s> under <%s>" % (childName, root.tag))
        return None


def get_attribute_from_child(root, childName, attrName):
    element = root.find(childName)
    if element is not None:
        if attrName in element.attrib:
            return element.attrib[attrName]
        else:
            return None
    else:
        return None


def add_subelement(parent, tag, text, add_if_missing=False):
    if not text and not add_if_missing:
        return
    e2 = SubElement(parent, tag)
    e2.text = str(text)


def now_in_iso():
    return time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime())


def resolve_path(path, referenceDir=None):
    if path is None:
        return None
    _path = None
    if not path.startswith('/'):
        if not referenceDir:
            raise Exception("Can't resolve relative path %s with no referenceDir" % path)
        p1 = os.path.join(referenceDir, os.path.join('..', path))
        if os.path.exists(p1):
            _path = os.path.abspath(p1)
        else:
            p1 = os.path.join(referenceDir, path)
            _path = os.path.abspath(p1)
    else:
        _path = os.path.abspath(path)
    return _path

#
# tip from http://renesd.blogspot.com/2007/05/pretty-print-xml-with-python.html
#
# except it puts unsightly spaces in pure text nodes
# so I'm turning it off for now
# ( best suggestion out there is use lxml ... yuck )
#


def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    #rough_string = tostring(elem, 'utf-8')
    #reparsed = minidom.parseString(rough_string)
    # return reparsed.toprettyxml(indent="  ")
    return tostring(elem, 'utf-8')


class ReferenceInfo(object):

    def __init__(self, parent, referenceInfoElement=None, referenceDir=None):
        self._parent = parent
        self._description = ''
        self._nContigs = 0
        self._file = ''
        self._maxContigLength = 0
        # index files are keyed by type
        self._index_files = {}
        if referenceInfoElement:
            self._parseElement(referenceInfoElement, referenceDir)

    def _parseElement(self, root, referenceDir=None):
        srcElement = root.find('reference')
        if srcElement is None:
            raise ReferenceXmlException(
                "Can't find <reference> element while parsing %s" %
                self._parent._metaDataFile)
        self._description = get_text_from_child(srcElement, 'description', required=True)
        #self._organism = get_text_from_child( srcElement, 'organism' )
        self._nContigs = int(get_text_from_child(srcElement, 'num_contigs', required=True))
        self._file = get_text_from_child(srcElement, 'file')
        self._file = resolve_path(self._file, referenceDir)
        sMaxContigLength = get_text_from_child(srcElement, 'max_contig_length')
        if sMaxContigLength:
            self._maxContigLength = int(sMaxContigLength)
        else:
            # unlikely that python code would be using this element anyways
            self._maxContigLength = 0

        for index_file in srcElement.findall('index_file'):
            type = index_file.attrib['type']
            path = resolve_path(index_file.text.strip(), referenceDir)
            if not path:
                raise ReferenceXmlException(
                    "Can't find resolve file path for index_file type=%s; path=%s" %
                    (type, index_file.text))
            self._index_files[type] = path

    @property
    def description(self):
        return self._description

    @property
    def file(self):
        return self._file

    @property
    def nContigs(self):
        return self._nContigs

    @property
    def maxContigLength(self):
        return self._maxContigLength

    def indexFile(self, type):
        "return index file corresponding to requested type"
        return self._index_files.get(type)

    def hasIndexFile(self, type):
        "returns true if an index file of specified type exists"
        return type in self._index_files

    def toElement(self):
        e = Element('reference')
        add_subelement(e, 'description', self.description)
        add_subelement(e, 'num_contigs', self.nContigs)
        if self.file:
            add_subelement(e, 'file', self.file)
        if self.maxContigLength > 0:
            add_subelement(e, 'max_contig_length', self.maxContigLength)
        return e


class ReferenceContig(object):

    def __init__(self, parent, contigElement=None, referenceDir=None):
        self._parent = parent
        if not contigElement:
            self._id = ''
            self._name = ''
            self._length = 0
            self._path = ''
            self._source = None
            self._digest = None
            self._header = None
        else:
            self._id = contigElement.attrib['id']
            self._name = contigElement.attrib['displayName']
            self._length = int(contigElement.attrib['length'])
            self._path = get_text_from_child(contigElement, 'file', required=False)
            # resolve path
            self._path = resolve_path(self._path, referenceDir)
            self._source = get_text_from_child(contigElement, 'file_source')
            self._digest = get_text_from_child(contigElement, 'digest')
            self._header = get_text_from_child(contigElement, 'header')

    @property
    def id(self):
        return self._id

    @property
    def idNumber(self):
        return int(re.match('ref([0-9]+)', self.id).groups()[0])

    @property
    def length(self):
        return self._length

    @property
    def name(self):
        return self._name

    @property
    def header(self):
        return self._header

    @property
    def path(self):
        if not self._path:
            return self._parent._info._file
        return self._path

    @property
    def source(self):
        return self._source

    @property
    def digest(self):
        return self._digest

    def __str__(self):
        "for testing"
        return 'Contig { name=%s; length=%d; relativePath=%s; source=%s }' % \
            (self.name, self.length, self.path, self.source)

    @property
    def sequence(self):
        """
        Read the sequence for this contig and return it.
        """
        path = self.path
        reader = FastaReader(path)

        for entry in reader:
            # only support reference repositories where the fasta 'raw_name' (ie the normal fasta header) exactly matches the reference repo header
            if entry.name == self.header:
                # Read this sequence, close the reader and return
                sequence = entry.sequence
                del reader
                return sequence

        # throw an exception if we can't find our sequence
        raise Exception("Couldn't find sequence for contig %s in %s" % (self.header, path))

    def calcDigest(self, path=None):
        if not path:
            path = self.path
        md = hashlib.md5()
        reader = FastaReader(path)
        sequence = None
        for entry in reader:
            if entry.raw_name == self.header:
                sequence = entry.sequence
                break
        if not sequence:
            raise Exception("Couldn't find sequence for contig %s in %s" % (self.header, path))
        md.update(sequence)
        self._digest = md.hexdigest()

    def toElement(self):
        """Returns ElemenTree.Element representation of this contig.
        Requires reading the underlying sequence for the checksum."""
        e = Element("contig")
        e.attrib["name"] = self.name
        e.attrib["length"] = str(self.length)
        if self.digest or self.header:
            digest = SubElement(e, "digest")
            if not self.digest:
                self.calcDigest()
                digest.text = self.digest
            else:
                digest.text = self.digest
        if self.header:
            header = SubElement(e, "header")
            header.text = self.header
        return e


class ReferenceAnnotation(object):

    """Represents <annotation> element in reference entry."""

    def __init__(self, annotationElement, referenceDir):
        self._name = annotationElement.attrib['name']
        self._type = annotationElement.attrib['type']
        self._file = resolve_path(
            get_text_from_child(annotationElement, 'file'), referenceDir)
        self._format = get_attribute_from_child(annotationElement, 'file', 'format')

    def __str__(self):
        "for testing"
        return 'ReferenceAnnotation { name=%s; type=%s; file=%s; format=%s }' % \
            (self._name, self._type, self._file, self._format)

    def toElement(self):
        e = Element("annotation")
        e.attrib["name"] = self._name
        e.attrib["type"] = self._type
        file = SubElement(e, "file")
        if self._format:
            file.attrib["format"] = self._format
        file.text = self._file
        return e


class Organism(object):

    """Represents organism element."""

    def __init__(self, element):
        if element is not None:
            self._name = get_text_from_child(element, 'name')
            self._ploidy = get_text_from_child(element, 'ploidy')
        else:
            self._name = None
            self._ploidy = None

    def __str__(self):
        "String representation"
        return 'Organism { name=%s; ploidy=%s; }' % \
            (self._name, self._ploidy)

    def toElement(self):
        e = Element("organism")
        add_subelement(e, 'name', self._name)
        add_subelement(e, 'ploidy', self._ploidy)
        return e

    @property
    def name(self):
        return self._name

    @property
    def ploidy(self):
        return self._ploidy


class ReferenceIndex(object):

    """Basic support for reading, writing the index structure of
    the reference repository."""

    def __init__(self, path=None):
        self._entries = []
        self._properties = {}
        if path:
            self._path = path
            self._load(path)
        else:
            self._path = None

    def _load(self, path):
        tree = ElementTree(file=path)
        root = tree.getroot()
        if root.tag != 'reference_index':
            raise ReferenceXmlException("%s doesn't look like a reference repository index file (no <reference_index>)" % path)
        properties = root.find('properties')
        if properties is not None:
            self._properties = dict([(p.tag, p.text.strip()) for p in properties])
        for entry in root.findall('reference'):
            self._entries.append(ReferenceIndexEntry(entry))

    def __getitem__(self, key):
        if key in self._properties:
            return self._properties[key]
        for entry in self._entries:
            if entry.id == key:
                return entry
        return None

    def __contains__(self, key):
        return self[key] is not None

    def __iter__(self):
        return iter(self._entries)

    def append(self, entry):
        self._entries.append(entry)

    def toXml(self):
        root = Element('reference_index')
        props = SubElement(root, 'properties')
        for k, v in self._properties.iteritems():
            add_subelement(props, k, v)
        for entry in self:
            root.append(entry.toElement())
        return prettify(root)

    def save(self, outfile=None):
        should_close = False
        if not outfile:
            outfile = open(self._path, 'w')
            should_close = True
        self._properties.setdefault('title', 'Seymour References Repository')
        self._properties.setdefault('system', 'Seymour 1.0')
        self._properties['last_modified'] = now_in_iso()
        print >>outfile, '<?xml version="1.0" encoding="utf-8"?>'
        print >>outfile, self.toXml()
        if should_close:
            outfile.close()


class ReferenceIndexEntry(object):

    def __init__(self, element=None):
        if element:
            self._loadFromElement(element)
        else:
            self._name = ''
            self._version = ''
            self._id = ''
            self._fasta = ''
            self._metadata = ''
            self._last_modified = now_in_iso()
            self._state = ''
            self._type = ''

    def _loadFromElement(self, element):
        self._id = get_text_from_child(element, 'id', required=True)
        self._name = get_text_from_child(element, 'name', required=True)
        self._version = get_text_from_child(element, 'version', required=True)
        self._fasta = get_text_from_child(element, 'fasta', required=True)
        self._metadata = get_text_from_child(element, 'metadata', required=True)
        self._last_modified = get_text_from_child(element, 'last_modified', required=True)
        self._state = get_text_from_child(element, 'state')
        self._type = get_text_from_child(element, 'type')

    def toElement(self):
        e = Element("reference")
        add_subelement(e, 'name', self._name)
        add_subelement(e, 'version', self._version)
        add_subelement(e, 'id', self._id)
        add_subelement(e, 'fasta', self._fasta)
        add_subelement(e, 'metadata', self._metadata)
        add_subelement(e, 'last_modified', self._last_modified)
        add_subelement(e, 'state', self._state)
        add_subelement(e, 'type', self._type)
        return e

    @property
    def name(self):
        return self._name

    @property
    def version(self):
        return self._version

    @property
    def id(self):
        return self._id

    @property
    def fasta(self):
        return self._fasta

    @property
    def metadata(self):
        return self._metadata

    @property
    def last_modified(self):
        return self._last_modified

    @property
    def state(self):
        return self._state

    @property
    def type(self):
        return self._type
