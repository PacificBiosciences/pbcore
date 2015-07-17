"""Validate DataSet XML files"""

import os
import re
from urlparse import urlparse
import xml.etree.ElementTree as ET
import logging

XMLNS = "http://pacificbiosciences.com/PacBioDataModel.xsd"

log = logging.getLogger(__name__)

def validateResources(xmlroot, relTo=False):
    stack = [xmlroot]
    while stack:
        element = stack.pop()
        stack.extend(element.getchildren())
        resId = element.get('ResourceId')
        if resId:
            parsedId = urlparse(resId)
            rfn = urlparse(resId).path.strip()
            if not os.path.isfile(rfn):
                if not os.path.isfile(os.path.join(os.path.dirname(relTo),
                                                   rfn)):
                    raise IOError, "{f} not found".format(f=rfn)

def validateXml(xmlroot):
    # pyxb precompiles and therefore does not need the original xsd file.
    #if not os.path.isfile(XSD):
        #raise SystemExit, "Validation xsd {s} not found".format(s=XSD)

    validateResources(xmlroot)

    # Conceal the first characters of UniqueIds if they are legal numbers that
    # would for some odd reason be considered invalid. Let all illegal
    # characters fall through to the validator.
    try:
        from pbcore.io.dataset import DataSetXsd
        log.debug('Validating with PyXb')
        fixedString = re.sub('UniqueId="[0-9]', 'UniqueId="f',
                             ET.tostring(xmlroot))
        DataSetXsd.CreateFromDocument(fixedString)
    except ImportError:
        log.debug('PyXb not found, validation disabled')

def validateFile(xmlfn):
    if ':' in xmlfn:
        xmlfn = urlparse(xmlfn).path.strip()
    with open(xmlfn, 'r') as xmlfile:
        #root = etree.parse(xmlfile)
        root = ET.parse(xmlfile).getroot()
        return validateXml(root)

def validateString(xmlstring, relTo=None):
    #root = etree.parse(xmlfile)
    root = ET.fromstring(xmlstring)
    validateResources(root, relTo=relTo)
    #return validateXml(root)


