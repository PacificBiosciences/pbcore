"""Validate DataSet XML files"""

import os
import re
from urlparse import urlparse
import xml.etree.ElementTree as ET

XMLNS = "http://pacificbiosciences.com/PacBioDataModel.xsd"

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
    from pbcore.io.dataset import DataSetXsd
    fixedString = re.sub('UniqueId="[0-9]', 'UniqueId="f',
                         ET.tostring(xmlroot))
    DataSetXsd.CreateFromDocument(fixedString)

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


