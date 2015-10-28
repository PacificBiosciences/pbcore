"""Validate DataSet XML files"""

import os
import re
from urlparse import urlparse
import xml.etree.ElementTree as ET
import logging

XMLNS = "http://pacificbiosciences.com/PacBioDataModel.xsd"

log = logging.getLogger(__name__)

def validateResources(xmlroot, relTo='.'):
    """Validate the resources in an XML file.

    Args:
        xmlroot: The ET root of an xml tree
        relTo: ('.') The path relative to which resources may reside. This will
               work poorly if relTo is not set to the dirname of the incoming
               XML file.
    """
    stack = [xmlroot]
    while stack:
        element = stack.pop()
        stack.extend(element.getchildren())
        resId = element.get('ResourceId')
        if resId:
            parsedId = urlparse(resId)
            rfn = urlparse(resId).path.strip()
            if not os.path.isfile(rfn):
                if (not os.path.isfile(os.path.join(relTo,
                                                    rfn)) and
                        not os.path.isfile(os.path.join('.',
                                                        rfn))):
                    raise IOError, "{f} not found".format(f=rfn)

def validateLxml(xml_fn, xsd_fn):
    try:
        from lxml import etree
        schema = etree.XMLSchema(etree.parse(xsd_fn))
        xml_file = etree.parse(xml_fn)
        if not schema.validate(xml_file):
            print schema.error_log
    except ImportError:
        log.debug('lxml not found, validation disabled')

def validateMiniXsv(xml_fn, xsd_fn):
    try:
        from minixsv import pyxsval
        pyxsval.parseAndValidate(xml_fn, xsd_fn)
    except ImportError:
        log.debug('minixsv not found, validation disabled')

def validateXml(xmlroot, skipResources=False, relTo='.'):

    if not skipResources:
        validateResources(xmlroot, relTo)

    # Conceal the first characters of UniqueIds if they are legal numbers that
    # would for some odd reason be considered invalid. Let all illegal
    # characters fall through to the validator.
    try:
        from pbcore.io.dataset import DataSetXsd
        log.debug('Validating with PyXb')
        fixedString = re.sub('UniqueId="[0-9]', 'UniqueId="f',
                             ET.tostring(xmlroot))
        fixedString = re.sub('Barcode="[0-9]', 'Barcode="f',
                             fixedString)
        fixedString = re.sub('Pointer>[0-9]', 'Pointer>f',
                             fixedString)
        DataSetXsd.CreateFromDocument(fixedString)
    except ImportError:
        log.debug('PyXb not found, validation disabled')

def validateFile(xmlfn, skipResources=False):
    if ':' in xmlfn:
        xmlfn = urlparse(xmlfn).path.strip()
    with open(xmlfn, 'r') as xmlfile:
        root = ET.parse(xmlfile).getroot()
        return validateXml(root, skipResources=skipResources,
                           relTo=os.path.dirname(xmlfn))

def validateString(xmlString, skipResources=False, relTo='.'):
    validateXml(ET.fromstring(xmlString), skipResources, relTo)
