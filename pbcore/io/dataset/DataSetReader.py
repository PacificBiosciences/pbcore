""" Input and output functions for DataSet XML files"""

import os.path
import functools
import xml.etree.ElementTree as ET
import logging
from urlparse import urlparse
import DataSetIO
from pbcore.io.dataset.DataSetMembers import (ExternalResource,
                                              ExternalResources,
                                              DataSetMetadata, RecordWrapper,
                                              Filters, AutomationParameters)
from pbcore.io.dataset.DataSetWriter import _eleFromDictList

XMLNS = "http://pacificbiosciences.com/PacBioDataModel.xsd"

__all__ = ['parseFiles']

log = logging.getLogger(__name__)

def parseFiles(filenames):
    """Open files with a helper function, feed any available members into a
    dictionary to be collected by the DataSet object

    Args:
        filenames: a list of filenames to parse
    Returns:
        A list of dictionaries of what will be copied into DataSet members
    Doctest:
        >>> from pbcore.io import DataSet
        >>> import pbcore.data.datasets as data
        >>> inBam = data.getBam()
        >>> ds = parseFiles([inBam])
        >>> type(ds).__name__
        'DataSet'
    """
    dataSetRecords = []
    # Create a DataSet object for each filename
    for filename in filenames:
        dataSetRecords.append(_parseFile(filename))
    tbr = reduce(lambda x, y: x + y, dataSetRecords)
    tbr.fileNames = filenames
    tbr.updateCounts()
    tbr.close()
    return tbr

def _parseFile(filename):
    """Opens a single filename, returns a list of one or more member
    dictionaries (more than one in the case of XML files or malformed
    concatenated XML
    files)."""
    handledTypes = {'xml': _openXmlFile,
                    'bam': _openBamFile,
                    'fofn': _openFofnFile,
                    '': _openUnknownFile,
                    'file': _openUnknownFile}
    url = urlparse(filename)
    fileType = url.scheme
    fileLocation = url.path.strip()
    if url.netloc:
        fileLocation = url.netloc
    elif os.path.exists(fileLocation):
        fileLocation = os.path.abspath(fileLocation)
    else:
        log.error("{f} not found".format(f=fileLocation))
    dataSetRecord = handledTypes[fileType](fileLocation)
    dataSetRecord.makePathsAbsolute(curStart=os.path.dirname(fileLocation))
    return dataSetRecord

def _openFofnFile(path):
    """Open a fofn file by calling parseFiles on the new filename list"""
    with open(path, 'r') as fofnFile:
        files = []
        for infn in fofnFile:
            tmp = os.path.abspath(infn)
            if os.path.exists(tmp):
                files.append(tmp)
            else:
                files.append(os.path.join(os.path.dirname(path), infn))
        return parseFiles(files)

def _openUnknownFile(path):
    """Open non-uri files
    """
    if path.endswith('xml'):
        return _openXmlFile(path)
    elif path.endswith('bam'):
        return _openBamFile(path)
    elif path.endswith('fofn'):
        return _openFofnFile(path)
    else:
        return _openGenericFile(path)

def _openGenericFile(path):
    """Create and populate an Element object, put it in an available members
    dictionary, return"""
    extRes = ExternalResource()
    extRes.resourceId = path
    # Perhaps this should be in its own _openFastaFile function. Or
    # _openBamFile should be rolled into this...
    possible_indices = ['.fai']
    extRes.addIndices([path + ext for ext in possible_indices if
                       os.path.exists(path + ext)])
    extRess = ExternalResources()
    extRess.append(extRes)
    tbr = DataSetIO.DataSet()
    tbr.addExternalResources(extRess)
    tbr.newUuid()
    return tbr

def _openBamFile(path):
    """Create and populate an Element object, put it in an available members
    dictionary, return"""
    extRes = ExternalResource()
    extRes.resourceId = path
    possible_indices = ['.pbi', '.bai', '.metadata.xml']
    extRes.addIndices([path + ext for ext in possible_indices if
                       os.path.exists(path + ext)])
    extRess = ExternalResources()
    extRess.append(extRes)
    tbr = DataSetIO.DataSet()
    tbr.addExternalResources(extRess)
    tbr.newUuid()
    return tbr

def _openXmlFile(path):
    """Open the XML file, extract information, create and populate Element
    objects, put them in an available members dictionary, return

    Doctest:
        >>> import pbcore.data.datasets as data
        >>> import xml.etree.ElementTree as ET
        >>> dsr = _openXmlFile(data.getXml(8).split(':')[1])
        >>> dsr.externalResources != None
        True
        >>> dsr.filters != None
        True
    """
    with open(path, 'rb') as xml_file:
        tree = ET.parse(xml_file)
    root = tree.getroot()
    return _parseXmlDataSet(root)

def _parseXmlDataSet(element):
    """Parse an XML DataSet tag, or the root tag of a DataSet XML file (they
    should be equivalent)

    Doctest:
        >>> import pbcore.data.datasets as data
        >>> ds = _openXmlFile(data.getXml(no=8).split(':')[-1])
        >>> type(ds).__name__
        'SubreadSet'
    """
    dsTypeMap = {'DataSet': DataSetIO.DataSet,
                 'SubreadSet': DataSetIO.SubreadSet,
                 'HdfSubreadSet': DataSetIO.HdfSubreadSet,
                 'ConsensusReadSet': DataSetIO.ConsensusReadSet,
                 'AlignmentSet': DataSetIO.AlignmentSet,
                 'ReferenceSet': DataSetIO.ReferenceSet,
                 'ContigSet': DataSetIO.ContigSet,
                 'BarcodeSet': DataSetIO.BarcodeSet}
    try:
        result = dsTypeMap[_tagCleaner(element.tag)]()
    except KeyError:
        # Fall back to the base type (from which the others are formed) for
        # unkown DataSet types
        result = dsTypeMap['DataSet']()
    result.objMetadata = element.attrib
    namer = functools.partial(_namespaceTag, XMLNS)
    element = _updateDataset(element)
    for child in element:
        if child.tag == namer('ExternalResources'):
            result.externalResources = _parseXmlExtResources(child)
        elif child.tag == namer('DataSets'):
            result.subdatasets = _parseXmlDataSets(child)
        elif child.tag == namer('Filters'):
            result.filters = _parseXmlFilters(child)
        elif child.tag == namer('DataSetMetadata'):
            result.metadata = _parseXmlDataSetMetadata(child)
        else:
            # Unknown tag found in XML
            pass
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

def _parseXmlDataSets(element):
    """DataSets can exist as elements in other datasets, representing subsets.
    Pull these datasets, parse them, and return a list of them."""
    result = []
    for child in element:
        result.append(_parseXmlDataSet(child))
    return result

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
    stats = RecordWrapper(_eleToDictList(root))
    stats.record['tag'] = 'SummaryStats'
    whitelist = ['ShortInsertFraction', 'AdapterDimerFraction',
                 'MedianInsertDist', 'ProdDist', 'ReadTypeDist',
                 'ReadLenDist', 'ReadQualDist', 'InsertReadQualDist',
                 'InsertReadLenDist', 'ControlReadQualDist',
                 'ControlReadLenDist', 'NumSequencingZmws']
    stats.pruneChildrenTo(whitelist)
    return stats

