# Author: Martin D. Smith


"""Validate DataSet XML files"""

from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET
import logging
import os
import re

XMLNS = "http://pacificbiosciences.com/PacBioDataModel.xsd"
XSD_FILE = os.environ.get("PB_DATASET_XSD", None)

log = logging.getLogger(__name__)


def validateResources(xmlroot, relTo='.'):
    """Validate the resources in an XML file.

    Args:
        xmlroot: The ET root of an xml tree
        relTo: ('.') The path relative to which resources may reside. This will
               work poorly if relTo is not set to the dirname of the incoming
               XML file.
    """
    # FIXME hacky workaround to avoid crashing on a field that was defined
    # improperly
    IGNORE_RESOURCES = set(["BioSamplesCsv"])
    stack = [xmlroot]
    while stack:
        element = stack.pop()
        stack.extend(element)
        resId = element.get('ResourceId')
        if resId:
            parsedId = urlparse(resId)
            rfn = unquote(urlparse(resId).path.strip())
            if not os.path.exists(rfn):
                if (not os.path.exists(os.path.join(relTo,
                                                    rfn)) and
                        not os.path.exists(os.path.join('.',
                                                        rfn))):
                    tag_name = re.sub(r"\{.*\}", "", element.tag)
                    if tag_name in IGNORE_RESOURCES:
                        log.warning("{f} not found".format(f=rfn))
                    else:
                        raise IOError("{f} not found".format(f=rfn))


def validateLxml(xml_fn, xsd_fn):
    try:
        from lxml import etree
        schema = etree.XMLSchema(etree.parse(xsd_fn))
        xml_file = etree.parse(xml_fn)
        if not schema.validate(xml_file):
            print(schema.error_log)
    except ImportError:
        log.debug('lxml not found, validation disabled')


def validateMiniXsv(xml_fn, xsd_fn):
    try:
        from minixsv import pyxsval
        pyxsval.parseAndValidate(xml_fn, xsd_fn)
    except ImportError:
        log.debug('minixsv not found, validation disabled')


def validateXmlschema(xml_src, xsd_file):
    try:
        import xmlschema
        schema = xmlschema.XMLSchema(xsd_file)
        schema.validate(xml_src)
    except ImportError:
        log.debug("xmlschema not found, validation disabled")


def validateXml(xmlroot, skipResources=False, relTo='.'):

    if not skipResources:
        validateResources(xmlroot, relTo)


def validateFile(xmlfn, skipResources=False, xsd_file=XSD_FILE):
    if ':' in xmlfn:
        xmlfn = urlparse(xmlfn).path.strip()
    with open(xmlfn, 'r') as xmlfile:
        root = ET.parse(xmlfile).getroot()
        validateXml(root,
                    skipResources=skipResources,
                    relTo=os.path.dirname(xmlfn))
        if xsd_file is not None:
            validateXmlschema(xmlfn, xsd_file)


def validateString(xmlString, skipResources=False, relTo='.', xsd_file=XSD_FILE):
    validateXml(ET.fromstring(xmlString), skipResources, relTo)
    if xsd_file is not None:
        validateXmlschema(xmlString, xsd_file)
