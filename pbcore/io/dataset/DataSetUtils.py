
import os
import logging

log = logging.getLogger(__name__)

def fileType(fname):
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

