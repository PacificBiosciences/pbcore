from __future__ import absolute_import

__all__ = ["tripleFromMetadataXML",
           "decodeTriple",
           "ChemistryLookupError" ]

import xml.etree.ElementTree as ET, os.path
from pkg_resources import Requirement, resource_filename
from collections import OrderedDict

class ChemistryLookupError(Exception): pass

def _loadBarcodeMappingsFromFile(mapFile):
    try:
        tree = ET.parse(mapFile)
        root = tree.getroot()
        mappingElements = root.findall("Mapping")
        mappings = OrderedDict()
        mapKeys = ["BindingKit", "SequencingKit", "SoftwareVersion", "SequencingChemistry"]
        for mapElement in mappingElements:
            bindingKit          = mapElement.find("BindingKit").text
            sequencingKit       = mapElement.find("SequencingKit").text
            softwareVersion     = mapElement.find("SoftwareVersion").text
            sequencingChemistry = mapElement.find("SequencingChemistry").text
            mappings[(bindingKit, sequencingKit, softwareVersion)] = sequencingChemistry
        return mappings
    except:
        raise ChemistryLookupError("Error loading chemistry mapping xml")

def _loadBarcodeMappings():
    mappingFname = resource_filename(Requirement.parse('pbcore'),'pbcore/chemistry/resources/mapping.xml')
    mappings = _loadBarcodeMappingsFromFile(mappingFname)
    updMappingDir = os.getenv("SMRT_CHEMISTRY_BUNDLE_DIR")
    if updMappingDir:
        import logging
        from os.path import join
        logging.info("Loading updated chemistry mapping XML from {}".format(updMappingDir))
        mappings.update(_loadBarcodeMappingsFromFile(join(updMappingDir, 'chemistry.xml')))
    return mappings

_BARCODE_MAPPINGS = _loadBarcodeMappings()

def tripleFromMetadataXML(metadataXmlPath):
    """
    Scrape the triple from the metadata.xml, or exception if the file
    or the relevant contents are not found
    """
    nsd = {None: "http://pacificbiosciences.com/PAP/Metadata.xsd",
           "pb": "http://pacificbiosciences.com/PAP/Metadata.xsd"}
    try:
        tree = ET.parse(metadataXmlPath)
        root = tree.getroot()
        bindingKit = root.find("pb:BindingKit/pb:PartNumber", namespaces=nsd).text
        sequencingKit = root.find("pb:SequencingKit/pb:PartNumber", namespaces=nsd).text
        # The instrument version is truncated to the first 2 dot delimited components
        instrumentControlVersion = root.find("pb:InstCtrlVer", namespaces=nsd).text
        verComponents = instrumentControlVersion.split(".")[0:2]
        instrumentControlVersion = ".".join(verComponents)
        return (bindingKit, sequencingKit, instrumentControlVersion)
    except Exception as e:
        raise ChemistryLookupError("Could not find, or extract chemistry information from, %s" % (metadataXmlPath,))

def decodeTriple(bindingKit, sequencingKit, softwareVersion):
    """
    Return the name of the chemisty configuration given the
    configuration triple that was recorded on the instrument.
    """
    return _BARCODE_MAPPINGS.get((bindingKit, sequencingKit, softwareVersion), "unknown")
