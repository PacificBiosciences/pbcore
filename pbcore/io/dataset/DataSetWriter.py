""" Input and output functions for DataSet XML files"""

import copy, time
import xml.etree.ElementTree as ET

XMLNS = "http://pacificbiosciences.com/PacBioDataModel.xsd"
# Not actually sure what this should be:
XMLVERSION = '2.3.0'

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
    root = _toElementTree(dataset, root=None, core=core)
    return ET.tostring(root, encoding="UTF-8")

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
        rootType = type(dataSet).__name__
        #rootType = dataSet.metadata.get(
            #'MetaType', 'PacBio.DataSet.SubreadSet').split('.')[2]
        attribs = dataSet.objMetadata
        if core:
            attribs = _coreClean(attribs)
        root = ET.Element(rootType, attribs)

    _addExternalResourcesElement(dataSet, root, core)
    _addDataSetMetadataElement(dataSet, root)
    _addFiltersElement(dataSet, root)
    _addDataSetsElement(dataSet, root)
    xsi = "{http://www.w3.org/2001/XMLSchema-instance}"
    # The ElementTree element dictionary doesn't quite work the same as a
    # regular dictionary, it seems, thus the convoluted get/set business
    # instead of setdefault
    if not root.get('CreatedAt') and not core:
        root.set('CreatedAt', time.strftime("%Y-%m-%dT%H:%M:%S"))
    if not root.get('Version'):
        root.set('Version', XMLVERSION)
    if not root.get(xsi + 'schemaLocation'):
        root.set(xsi + 'schemaLocation', ("http://pacificbiosciences.com"
                                          "/PacBioDataModel.xsd"))
    root.set('xmlns', XMLNS)
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
    # Whether or not the hash should salt future hashes is up for debate
    #if 'UniqueId' in attribs:
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
        dsmd = ET.SubElement(root, 'ExternalResources')
        for child in dataSet.externalResources.record['children']:
            dsmd.append(_eleFromDictList(child, core))

def _addDataSetMetadataElement(dataSet, root):
    """Add DataSetMetadata Elements to the root ElementTree object. Full
    depth serialization will be both difficult and necessary.

    Args:
        root: The root ElementTree object. Extended here using SubElement
    """
    if dataSet.metadata:
        dsmd = ET.SubElement(root, 'DataSetMetadata')
        #for key, value in dataSet.datasetMetadata.items():
        #for key, value in dataSet.metadata.record.items():
        for child in dataSet.metadata.record['children']:
            #dsmd.append(_eleFromEleDict(key, value))
            #if isinstance(value, (int, float, str)):
                #ET.SubElement(dsmd, key).text = value
            #elif isinstance(value, dict):
                #dsmd.append(_eleFromDict(key, value))
            dsmd.append(_eleFromDictList(child))

def _eleFromDict(tag, eleAsDict):
    """A last ditch capture method for uknown Elements"""
    ele = ET.Element(tag, eleAsDict['attrib'])
    ele.text = eleAsDict['text']
    for childTag, childDict in eleAsDict['children'].items():
        ele.append(_eleFromDict(childTag, childDict))
    return ele

def _eleFromDictList(eleAsDict, core=False):
    """A last ditch capture method for uknown Elements"""
    if core:
        ele = ET.Element(eleAsDict['tag'], _coreClean(eleAsDict['attrib']))
    else:
        ele = ET.Element(eleAsDict['tag'], eleAsDict['attrib'])
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
        filters = ET.SubElement(root, 'Filters')
        for child in dataset.filters.record['children']:
            filters.append(_eleFromDictList(child, core))
        #for filt in dataset.filters:
            #filtElement = ET.SubElement(filters, 'Filter')
            #parameters = ET.SubElement(filtElement, 'Parameters')
            #for key, value in filt.items():
                #ET.SubElement(parameters, 'Parameter', Name=key, Value=value)

def _addDataSetsElement(dataset, root):
    """Add DataSet Elements to root, which essentially nests ElementTrees.

    Args:
        root: The root ElementTree object. Extended here using SubElement
    """
    if dataset.subdatasets:
        dse = ET.SubElement(root, 'DataSets')
        for subSet in dataset.subdatasets:
            subSetRoot = ET.SubElement(dse, subSet.__class__.__name__,
                                       subSet.objMetadata)
            _toElementTree(subSet, subSetRoot)

def _extResToXMLAttribs(extRes):
    """Clean the members of the ExternalResource dictionary into XML
    appropriate objects. This shouldn't be a method of ExternalResource,
    as it requires knowledge of which members are appropriate for XML
    attributes and which are not."""
    attr = {}
    for key, value in extRes.toDict().items():
        if value and not (key == 'PacBioIndex' or key == 'PacBioMetadata'):
            attr[key] = value
    return attr
