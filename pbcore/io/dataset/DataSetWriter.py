# Author: Martin D. Smith


""" Input and output functions for DataSet XML files"""

import xml.etree.ElementTree as ET
import logging
import copy
import time

log = logging.getLogger(__name__)

XML_VERSION = "3.0.1"

__all__ = ['toXml']

# XML Writer:


def toXml(dataset, core=False):
    """Generate an XML representation of this object. This is a function
    independent of "write" so that it can also be used to generate new
    UniqueIds, which are based on the concept of a Core Dataset.

    Args:
        core: T/F whether or not to strip out user editable attributes
              throughout the xml.
    Returns:
        The XML representation as a string.
    """
    log.debug('Making elementtree...')
    root = _toElementTree(dataset, root=None, core=core)
    log.debug('Done making ElementTree...')
    log.debug('Converting ElementTree to string...')
    xmlstring = ET.tostring(root, encoding="UTF-8")
    log.debug('Done converting ElementTree to string')
    return xmlstring


NAMESPACES = {
    'pbbase': 'http://pacificbiosciences.com/PacBioBaseDataModel.xsd',
    'pbsample': 'http://pacificbiosciences.com/PacBioSampleInfo.xsd',
    'pbstats': 'http://pacificbiosciences.com/PipelineStats/PipeStats.xsd',
    'pbmeta': 'http://pacificbiosciences.com/PacBioCollectionMetadata.xsd',
    '': 'http://pacificbiosciences.com/PacBioDatasets.xsd',
    'pbds': 'http://pacificbiosciences.com/PacBioDatasets.xsd',
    'pbrk': 'http://pacificbiosciences.com/PacBioReagentKit.xsd'
}

# These are either deep in the weeds and don't have their own class, or way up
# in the hierarchy and aren't part of the DataSetMetadata tree
TAGS = [
    "pbbase:BinCount",
    "pbbase:BinCounts",
    "pbbase:BinLabel",
    "pbbase:BinLabels",
    "pbbase:BinWidth",
    "pbbase:MaxBinValue",
    "pbbase:MaxOutlierValue",
    "pbbase:MetricDescription",
    "pbbase:MinBinValue",
    "pbbase:MinOutlierValue",
    "pbbase:NumBins",
    "pbbase:Sample95thPct",
    "pbbase:SampleMean",
    "pbbase:SampleMed",
    "pbbase:SampleSize",
    "pbbase:SampleStd",
    ":AdapterDimerFraction",
    ":BarcodeConstruction",
    ":ControlReadLenDist",
    ":ControlReadQualDist",
    ":DataSet",
    ":DataSets",
    ":InsertReadLenDist",
    ":InsertReadQualDist",
    ":MedianInsertDist",
    ":NumRecords",
    ":NumSequencingZmws",
    ":ProdDist",
    ":ReadLenDist",
    ":ReadQualDist",
    ":ReadTypeDist",
    ":ShortInsertFraction",
    ":SubreadSet",
    ":SummaryStats",
    ":TotalLength",
    "pbmeta:AutomationName",
    "pbmeta:CellIndex",
    "pbmeta:CollectionFileCopy",
    "pbmeta:CollectionNumber",
    "pbmeta:CollectionPathUri",
    "pbmeta:Concentration",
    "pbmeta:ConfigFileName",
    "pbmeta:CopyFiles",
    "pbmeta:InstCtrlVer",
    "pbmeta:MetricsVerbosity",
    "pbmeta:Name",
    "pbmeta:PlateId",
    "pbmeta:Readout",
    "pbmeta:ResultsFolder",
    "pbmeta:RunId",
    "pbmeta:SampleReuseEnabled",
    "pbmeta:SequencingCondition",
    "pbmeta:SigProcVer",
    "pbmeta:SizeSelectionEnabled",
    "pbmeta:StageHotstartEnabled",
    "pbmeta:UseCount",
    "pbmeta:WellName",
    "pbrk:ReagentTubes",
    ":AlignmentSet",
    ":BarcodeSet",
    ":ConsensusReadSet",
    ":ContigSet",
    ":ReferenceSet",
    ":Ploidy",
    ":Organism",
    ":Contig",
    ":Contigs"
]


def register_namespaces():
    for (prefix, uri) in NAMESPACES.items():
        ET.register_namespace(prefix, uri)


def _toElementTree(dataSet, root=None, core=False):
    """Generate an ElementTree representation of this object. This is a
    function independent of "write" and "toXml" so that it can also be used
    to generate DataSet Elements, which can be nested into other Dataset
    elements but don't share the same root tag.

    Args:
        root: The root to which to append the elementTree
        core: T/F whether or not to strip out user editable attributes
              throughout the xml.
    Returns:
        The XML representation as an ElementTree.
    """
    # 'if not root:' would conflict with testing root for children
    if root is None:
        register_namespaces()
        rootType = '{{{n}}}{t}'.format(n=NAMESPACES[''],
                                       t=type(dataSet).__name__)
        attribs = dataSet.objMetadata
        if core:
            attribs = _coreClean(attribs)
        root = ET.Element(rootType, attribs)

    _addExternalResourcesElement(dataSet, root, core)
    _addFiltersElement(dataSet, root, core)
    _addDataSetsElement(dataSet, root, core)
    _addDataSetMetadataElement(dataSet, root, core)
    xsi = "{http://www.w3.org/2001/XMLSchema-instance}"
    # The ElementTree element dictionary doesn't quite work the same as a
    # regular dictionary, it seems, thus the convoluted get/set business
    # instead of setdefault
    if not root.get('CreatedAt') and not core:
        root.set('CreatedAt', time.strftime("%Y-%m-%dT%H:%M:%S"))
    if not root.get('Version'):
        root.set('Version', XML_VERSION)
    if not root.get(xsi + 'schemaLocation'):
        root.set(xsi + 'schemaLocation', ("http://pacificbiosciences.com"
                                          "/PacBioDataModel.xsd"))
    return root


def _coreClean(attribs):
    """Remove the non-core elements from any attributes dictionary. This will
    allow the same toXml function to serve as both the XML output
    generator and the core for the newUuid hashing function.

    Args:
        attribs: a dictionary of attributes (both XML and DataSet)
    Returns:
        a dictionary of attributes less user-mutable members
    """
    attribs = copy.deepcopy(attribs)
    if 'Name' in attribs:
        del attribs['Name']
    if 'Description' in attribs:
        del attribs['Description']
    if 'Tags' in attribs:
        del attribs['Tags']
    if 'CreatedAt' in attribs:
        del attribs['CreatedAt']
    if 'TimeStampedName' in attribs:
        del attribs['TimeStampedName']
    # Whether or not the hash should salt future hashes is up for debate
    # if 'UniqueId' in attribs:
        #del attribs['UniqueId']
    return attribs


def _addExternalResourcesElement(dataSet, root, core=False):
    """Add ExternalResource Elements to root, complete with resourceIds,
    PacBioIndex, PacBioMetadata, tags, etc.

    Args:
        root: The root ElementTree object. Extended here using SubElement
        core=False: T/F strip out user editable attributes
    """
    if dataSet.externalResources:
        root.append(_eleFromDictList(dataSet.externalResources.record, core))


def _addDataSetMetadataElement(dataSet, root, core=False):
    """Add DataSetMetadata Elements to the root ElementTree object. Full
    depth serialization will be both difficult and necessary.

    Args:
        root: The root ElementTree object. Extended here using SubElement
    """
    if dataSet.metadata:
        provenance = dataSet.metadata.removeChildren("Provenance")
        for i, record in enumerate(dataSet.metadata.record['children']):
            if record['tag'] == "NumRecords":
                for k, value in enumerate(provenance):
                    dataSet.metadata.record['children'].insert(
                        i + k + 1, value)
                break
        else:
            dataSet.metadata.extend([p.record for p in provenance])
        # hide the stats:
        stats = None
        if dataSet.metadata.summaryStats:
            stats = dataSet.metadata.summaryStats
            dataSet.metadata.summaryStats = None
        root.append(_eleFromDictList(dataSet.metadata.record,
                                     core=core))
        if stats:
            dataSet.metadata.summaryStats = stats
        # Metadata order matters....
        #tl = dsmd.find('TotalLength')
        #tl = dsmd.remove(tl)
        #dsmd.insert(0, tl)


def _guessNs(tag):
    for option in TAGS:
        nsprefix, nstag = option.split(':')
        if nstag == tag:
            return NAMESPACES[nsprefix]
    return ''


def _eleFromDictList(eleAsDict, core=False):
    """Create an ElementTree Element from a DictList"""
    # Elements should have namespaces from the XML file. If you add new
    # elements that have classes in DataSetMembers, associated namespaces
    # should be handled there. Some elements don't get a class and are covered
    # by the TAGS map above (I'd like to replace this)
    curNS = eleAsDict['namespace']
    if curNS == '':
        curNS = _guessNs(eleAsDict['tag'])

    if core:
        ele = ET.Element("{{{n}}}{t}".format(n=curNS,
                                             t=eleAsDict['tag']),
                         _coreClean(eleAsDict['attrib']))
    else:
        ele = ET.Element("{{{n}}}{t}".format(n=curNS,
                                             t=eleAsDict['tag']),
                         eleAsDict['attrib'])
    ele.text = eleAsDict['text']
    for child in eleAsDict['children']:
        ele.append(_eleFromDictList(child))
    return ele


def _addFiltersElement(dataset, root, core=False):
    """Add Filter Elements to root, which are deep but uncluttered. Core
    option not really necessary, as filter names are fundamentally
    different than other (e.g. ExternalResource) names.

    Args:
        root: The root ElementTree object. Extended here using SubElement
    """
    if dataset.filters:
        root.append(_eleFromDictList(dataset.filters.record, core=core))


def _addDataSetsElement(dataset, root, core=False):
    """Add DataSet Elements to root, which essentially nests ElementTrees.

    Args:
        root: The root ElementTree object. Extended here using SubElement
    """
    if dataset.subdatasets:
        rootType = '{{{n}}}{t}'.format(n=NAMESPACES[''],
                                       t='DataSets')
        dse = ET.SubElement(root, rootType)
        for subSet in dataset.subdatasets:
            rootType = '{{{n}}}{t}'.format(n=NAMESPACES[''],
                                           t=subSet.__class__.__name__)
            subSetRoot = ET.SubElement(dse, rootType,
                                       subSet.objMetadata)
            _toElementTree(subSet, subSetRoot, core=core)


def _extResToXMLAttribs(extRes):
    """Clean the members of the ExternalResource dictionary into XML
    appropriate objects. This shouldn't be a method of ExternalResource,
    as it requires knowledge of which members are appropriate for XML
    attributes and which are not."""
    attr = {}
    for (key, value) in extRes.toDict().items():
        if value and not (key == 'PacBioIndex' or key == 'PacBioMetadata'):
            attr[key] = value
    return attr
