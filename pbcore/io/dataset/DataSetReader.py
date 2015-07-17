""" Input and output functions for DataSet XML files"""

import os.path
import functools
import xml.etree.ElementTree as ET
import logging
from urlparse import urlparse
from pbcore.io.dataset.DataSetMembers import (ExternalResource,
                                              ExternalResources,
                                              DataSetMetadata,
                                              Filters, AutomationParameters,
                                              StatsMetadata)
from pbcore.io.dataset.DataSetWriter import _eleFromDictList

XMLNS = "http://pacificbiosciences.com/PacBioDataModel.xsd"

log = logging.getLogger(__name__)

def populateDataSet(dset, filenames):
    for filename in filenames:
        _addFile(dset, filename)

def _addFile(dset, filename):
    handledTypes = {'xml': _addXmlFile,
                    'bam': _addGenericFile,
                    'fofn': _addFofnFile,
                    '': _addUnknownFile,
                    'file': _addUnknownFile}
    url = urlparse(filename)
    fileType = url.scheme
    fileLocation = url.path.strip()
    if url.netloc:
        fileLocation = url.netloc
    elif os.path.exists(fileLocation):
        fileLocation = os.path.abspath(fileLocation)
    handledTypes[fileType](dset, fileLocation)
    dset.makePathsAbsolute(curStart=os.path.dirname(fileLocation))

def _addXmlFile(dset, path):
    with open(path, 'rb') as xml_file:
        tree = ET.parse(xml_file)
    root = tree.getroot()
    dset.merge(_parseXml(dset, root), copyOnMerge=False)

def _addFofnFile(dset, path):
    """Open a fofn file by calling parseFiles on the new filename list"""
    with open(path, 'r') as fofnFile:
        files = []
        for infn in fofnFile:
            tmp = os.path.abspath(infn)
            if os.path.exists(tmp):
                files.append(tmp)
            else:
                files.append(os.path.join(os.path.dirname(path), infn))
        populateDataSet(dset, files)

def _addUnknownFile(dset, path):
    """Open non-uri files
    """
    if path.endswith('xml'):
        return _addXmlFile(dset, path)
    elif path.endswith('bam'):
        return _addGenericFile(dset, path)
    elif path.endswith('fofn'):
        return _addFofnFile(dset, path)
    else:
        return _addGenericFile(dset, path)

def _addGenericFile(dset, path):
    """Create and populate an Element object, put it in an available members
    dictionary, return"""
    possible_indices = ['.fai', '.pbi', '.bai', '.metadata.xml']
    for ext in possible_indices:
        if path.endswith(ext):
            log.debug('Index file {f} given as regular file, will be treated '
                      ' as an index file instead'.format(f=path))
            return
    extRes = ExternalResource()
    extRes.resourceId = path
    index_files = [path + ext for ext in possible_indices if
                   os.path.exists(path + ext)]
    if index_files:
        extRes.addIndices(index_files)
    extRess = ExternalResources()
    extRess.append(extRes)
    # We'll update them all at the end, skip updating counts for now
    dset.addExternalResources(extRess, updateCount=False)

def _parseXml(dset, element):
    """Parse an XML DataSet tag, or the root tag of a DataSet XML file (they
    should be equivalent)

    Doctest:
        >>> import pbcore.data.datasets as data
        >>> ds = _openXmlFile(data.getXml(no=8).split(':')[-1])
        >>> type(ds).__name__
        'SubreadSet'
    """
    result = type(dset)()
    result.objMetadata = element.attrib
    namer = functools.partial(_namespaceTag, XMLNS)
    element = _updateDataset(element)
    for child in element:
        if child.tag == namer('ExternalResources'):
            result.externalResources = _parseXmlExtResources(child)
        elif child.tag == namer('DataSets'):
            result.subdatasets = _parseXmls(dset, child)
        elif child.tag == namer('Filters'):
            result.filters = _parseXmlFilters(child)
        elif child.tag == namer('DataSetMetadata'):
            result.metadata = _parseXmlDataSetMetadata(child)
        else:
            # Unknown tag found in XML
            pass
    return result

def _parseXmls(dset, element):
    """DataSets can exist as elements in other datasets, representing subsets.
    Pull these datasets, parse them, and return a list of them."""
    result = []
    for child in element:
        result.append(_parseXml(type(dset)(), child))
    return result

def _updateDataset(element):
    namer = functools.partial(_namespaceTag, XMLNS)
    updateMap = {
        './/' + namer('ExternalDataReferences'): 'ExternalResources',
        './/' + namer('ExternalReference'): 'ExternalResource',
        './/' + namer('BioSampleReferences'): 'BioSamplePointers',
        './/' + namer('BioSampleReference'): 'BioSamplePointer',
        './/' + namer('PacBioIndex'): 'FileIndex',
        './/' + namer('CCSreadSet'): 'ConsensusReadSet',
        }
    for old, new in updateMap.items():
        #while element.find('.//' + namer(old)) is not None:
        while element.find(old) is not None:
            log.error("Outdated XML received: {t}".format(
                t=old.split('}')[-1]))
            element.find(old).tag = namer(new)

    auton = ('.//' + namer('CollectionMetadata') + '/' +
             namer('AutomationName'))
    if element.find(auton) is not None:
        log.error("Outdated XML received: AutomationName")
        autonele = element.find(auton)
        autonele.tag = namer('Automation')
        val = autonele.text
        autonele.text = None
        newParams = AutomationParameters()
        newParams.addParameter(None, None)
        autonele.append(_eleFromDictList(newParams.record))
    return element

def _updateStats(element):
    namer = functools.partial(
        _namespaceTag,
        "http://pacificbiosciences.com/PipelineStats/PipeStats.xsd")
    binCounts = [
        './/' + namer('MedianInsertDist') + '/' + namer('BinCount'),
        './/' + namer('ProdDist') + '/' + namer('BinCount'),
        './/' + namer('ReadTypeDist') + '/' + namer('BinCount'),
        './/' + namer('ReadLenDist') + '/' + namer('BinCount'),
        './/' + namer('ReadQualDist') + '/' + namer('BinCount'),
        './/' + namer('InsertReadQualDist') + '/' + namer('BinCount'),
        './/' + namer('InsertReadLenDist') + '/' + namer('BinCount'),
        './/' + namer('ControlReadQualDist') + '/' + namer('BinCount'),
        './/' + namer('ControlReadLenDist') + '/' + namer('BinCount'),
        ]
    binLabels = [
        './/' + namer('ProdDist') + '/' + namer('BinLabel'),
        './/' + namer('ReadTypeDist') + '/' + namer('BinLabel'),
        ]
    for tag in binCounts:
        if element.findall(tag):
            log.error("Outdated stats XML received")
            finds = element.findall(tag)
            parent = tag.split('Dist')[0] + 'Dist'
            parent = element.find(parent)
            for sub_ele in finds:
                parent.remove(sub_ele)
            binCounts = ET.Element(namer('BinCounts'))
            for sub_ele in finds:
                binCounts.append(sub_ele)
            parent.append(binCounts)
    for tag in binLabels:
        if element.findall(tag):
            log.error("Outdated stats XML received")
            finds = element.findall(tag)
            parent = tag.split('Dist')[0] + 'Dist'
            parent = element.find(parent)
            for sub_ele in finds:
                parent.remove(sub_ele)
            binCounts = ET.Element(namer('BinLabels'))
            for sub_ele in finds:
                binCounts.append(sub_ele)
            parent.append(binCounts)
    return element

def _namespaceTag(xmlns, tagName):
    """Preface an XML tag name with the provided namespace"""
    return ''.join(["{", xmlns, "}", tagName])

def _tagCleaner(tagName):
    """Remove the namespace prefix from a tag name"""
    return tagName.split('}')[-1]

def _parseXmlExtResources(element):
    """Parse the ExternalResources tag, populating a list of
    ExternalResource objects"""
    return ExternalResources(_eleToDictList(element))

def _parseXmlDataSetMetadata(element):
    """Parse the DataSetMetadata field of XML inputs. This data can be
    extremely extensive."""
    result = []
    for child in element:
        result.append(_eleToDictList(child))
    tbr = DataSetMetadata()
    tbr.extend(result)
    return tbr.record

def _eleToDictList(element):
    """A last ditch capture method for uknown Elements"""
    tag = _tagCleaner(element.tag)
    text = element.text
    if text:
        text = text.strip()
    attrib = element.attrib
    children = []
    for child in element:
        children.append(_eleToDictList(child))
    return {'tag': tag, 'text': text, 'attrib': attrib,
            'children': children}

def _parseXmlFilters(element):
    """Pull filters from XML file, put them in a list of dictionaries, where
    each dictionary contains a representation of a Filter tag: key, value pairs
    with parameter names and value expressions.

    Doctest:
        >>> import xml.etree.ElementTree as ET
        >>> import pbcore.data.datasets as data
        >>> tree = ET.parse(data.getXml(no=8).split(':')[1])
        >>> root = tree.getroot()
        >>> filters = root[1]
        >>> str(_parseXmlFilters(filters))
        '( rq > 0.75 ) OR ( qname == 100/0/0_100 )'
    """
    """
    namer = functools.partial(_namespaceTag, XMLNS)
    result = []
    for filtTag in filters:
        #filt = Filter()
        filt = {}
        # This is essentially to skip the <Parameters> level
        for child in filtTag:
            if child.tag == namer('Parameters'):
                for param in child:
                    filt[param.attrib['Name'].lower()] = param.attrib['Value']
        result.append(filt)
    return result
    """
    return Filters(_eleToDictList(element))

def parseStats(filename):
    url = urlparse(filename)
    fileType = url.scheme
    fileLocation = url.path.strip()
    if url.netloc:
        fileLocation = url.netloc
    tree = ET.parse(fileLocation)
    root = tree.getroot()
    root = _updateStats(root)
    stats = StatsMetadata(_eleToDictList(root))
    stats.record['tag'] = 'SummaryStats'
    whitelist = ['ShortInsertFraction', 'AdapterDimerFraction',
                 'MedianInsertDist', 'ProdDist', 'ReadTypeDist',
                 'ReadLenDist', 'ReadQualDist', 'InsertReadQualDist',
                 'InsertReadLenDist', 'ControlReadQualDist',
                 'ControlReadLenDist', 'NumSequencingZmws']
    stats.pruneChildrenTo(whitelist)
    return stats

