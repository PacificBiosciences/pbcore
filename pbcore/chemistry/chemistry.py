#################################################################################
# Copyright (c) 2011-2015, Pacific Biosciences of California, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Pacific Biosciences nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE.  THIS SOFTWARE IS PROVIDED BY PACIFIC BIOSCIENCES AND ITS
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR
# ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#################################################################################


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
        raise ChemistryLookupError, "Error loading chemistry mapping xml"

def _loadBarcodeMappings():
    mappingFname = resource_filename(Requirement.parse('pbcore'),'pbcore/chemistry/resources/mapping.xml')
    return _loadBarcodeMappingsFromFile(mappingFname)

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
        raise ChemistryLookupError, \
            ("Could not find, or extract chemistry information from, %s" % (metadataXmlPath,))

def decodeTriple(bindingKit, sequencingKit, softwareVersion):
    """
    Return the name of the chemisty configuration given the
    configuration triple that was recorded on the instrument.
    """
    return _BARCODE_MAPPINGS.get((bindingKit, sequencingKit, softwareVersion), "unknown")
