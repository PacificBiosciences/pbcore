# pbcore/io/dataset/pyxb/_pbsample.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a7c0866985dba806fe3112e9fbc4707c9f978443
# Generated 2020-04-08 13:50:29.480031 by PyXB version 1.2.6 using Python 3.7.3.final.0
# Namespace http://pacificbiosciences.com/PacBioSampleInfo.xsd [xmlns:pbsample]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:94817b88-79da-11ea-a8e0-005056871a22')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import _pbbase as _ImportedBinding__pbbase

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://pacificbiosciences.com/PacBioSampleInfo.xsd', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_pbbase = _ImportedBinding__pbbase.Namespace
_Namespace_pbbase.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Back references to other BarcodedSampleType object UniqueIds which utilize this sample"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 96, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioSampleInfo.xsd}BioSamplePointer uses Python identifier BioSamplePointer
    __BioSamplePointer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BioSamplePointer'), 'BioSamplePointer', '__httppacificbiosciences_comPacBioSampleInfo_xsd_CTD_ANON_httppacificbiosciences_comPacBioSampleInfo_xsdBioSamplePointer', False, pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 103, 10), )

    
    BioSamplePointer = property(__BioSamplePointer.value, __BioSamplePointer.set, None, 'Pointer to a single biological sample')

    
    # Element {http://pacificbiosciences.com/PacBioSampleInfo.xsd}BarcodedSamplePointers uses Python identifier BarcodedSamplePointers
    __BarcodedSamplePointers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointers'), 'BarcodedSamplePointers', '__httppacificbiosciences_comPacBioSampleInfo_xsd_CTD_ANON_httppacificbiosciences_comPacBioSampleInfo_xsdBarcodedSamplePointers', False, pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 112, 2), )

    
    BarcodedSamplePointers = property(__BarcodedSamplePointers.value, __BarcodedSamplePointers.set, None, 'Back references to other BarcodedSampleType object UniqueIds which utilize this sample')

    _ElementMap.update({
        __BioSamplePointer.name() : __BioSamplePointer,
        __BarcodedSamplePointers.name() : __BarcodedSamplePointers
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Back references to other BarcodedSampleType object UniqueIds which utilize this sample"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 116, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioSampleInfo.xsd}BarcodedSamplePointer uses Python identifier BarcodedSamplePointer
    __BarcodedSamplePointer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointer'), 'BarcodedSamplePointer', '__httppacificbiosciences_comPacBioSampleInfo_xsd_CTD_ANON__httppacificbiosciences_comPacBioSampleInfo_xsdBarcodedSamplePointer', True, pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 118, 8), )

    
    BarcodedSamplePointer = property(__BarcodedSamplePointer.value, __BarcodedSamplePointer.set, None, 'Pointer to a group of barcoded samples')

    _ElementMap.update({
        __BarcodedSamplePointer.name() : __BarcodedSamplePointer
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """List of biological samples."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 130, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioSampleInfo.xsd}BioSample uses Python identifier BioSample
    __BioSample = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BioSample'), 'BioSample', '__httppacificbiosciences_comPacBioSampleInfo_xsd_CTD_ANON_2_httppacificbiosciences_comPacBioSampleInfo_xsdBioSample', True, pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 136, 2), )

    
    BioSample = property(__BioSample.value, __BioSample.set, None, 'An individual biological sample.')

    _ElementMap.update({
        __BioSample.name() : __BioSample
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {http://pacificbiosciences.com/PacBioSampleInfo.xsd}BioSampleType with content type ELEMENT_ONLY
class BioSampleType (_ImportedBinding__pbbase.BaseEntityType):
    """The actual biological sample; this could be prep'd, or in original form; could be bound, or annealed..."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BioSampleType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 8, 2)
    _ElementMap = _ImportedBinding__pbbase.BaseEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.BaseEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioSampleInfo.xsd}DNABarcodes uses Python identifier DNABarcodes
    __DNABarcodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DNABarcodes'), 'DNABarcodes', '__httppacificbiosciences_comPacBioSampleInfo_xsd_BioSampleType_httppacificbiosciences_comPacBioSampleInfo_xsdDNABarcodes', False, pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 15, 10), )

    
    DNABarcodes = property(__DNABarcodes.value, __DNABarcodes.set, None, 'A list of barcodes associated with the biological sample')

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute DateReceived uses Python identifier DateReceived
    __DateReceived = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DateReceived'), 'DateReceived', '__httppacificbiosciences_comPacBioSampleInfo_xsd_BioSampleType_DateReceived', pyxb.binding.datatypes.dateTime)
    __DateReceived._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 34, 8)
    __DateReceived._UseLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 34, 8)
    
    DateReceived = property(__DateReceived.value, __DateReceived.set, None, 'Date the sample was received by the lab')

    
    # Attribute Organism uses Python identifier Organism
    __Organism = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Organism'), 'Organism', '__httppacificbiosciences_comPacBioSampleInfo_xsd_BioSampleType_Organism', pyxb.binding.datatypes.string)
    __Organism._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 39, 8)
    __Organism._UseLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 39, 8)
    
    Organism = property(__Organism.value, __Organism.set, None, 'e.g. HIV, E.coli')

    
    # Attribute Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Reference'), 'Reference', '__httppacificbiosciences_comPacBioSampleInfo_xsd_BioSampleType_Reference', pyxb.binding.datatypes.string)
    __Reference._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 44, 8)
    __Reference._UseLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 44, 8)
    
    Reference = property(__Reference.value, __Reference.set, None, 'Name of reference, or pointer to one at e.g. NCBI RefSeq')

    
    # Attribute DNAType uses Python identifier DNAType
    __DNAType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DNAType'), 'DNAType', '__httppacificbiosciences_comPacBioSampleInfo_xsd_BioSampleType_DNAType', pyxb.binding.datatypes.string)
    __DNAType._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 49, 8)
    __DNAType._UseLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 49, 8)
    
    DNAType = property(__DNAType.value, __DNAType.set, None, 'shotgun library, amplicon, etc.')

    
    # Attribute Concentration uses Python identifier Concentration
    __Concentration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Concentration'), 'Concentration', '__httppacificbiosciences_comPacBioSampleInfo_xsd_BioSampleType_Concentration', pyxb.binding.datatypes.float)
    __Concentration._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 54, 8)
    __Concentration._UseLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 54, 8)
    
    Concentration = property(__Concentration.value, __Concentration.set, None, 'in ng/uL, e.g. 250')

    
    # Attribute QuantificationMethod uses Python identifier QuantificationMethod
    __QuantificationMethod = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'QuantificationMethod'), 'QuantificationMethod', '__httppacificbiosciences_comPacBioSampleInfo_xsd_BioSampleType_QuantificationMethod', pyxb.binding.datatypes.string)
    __QuantificationMethod._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 59, 8)
    __QuantificationMethod._UseLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 59, 8)
    
    QuantificationMethod = property(__QuantificationMethod.value, __QuantificationMethod.set, None, 'e.g. Qubit')

    
    # Attribute SMRTBellConcentration uses Python identifier SMRTBellConcentration
    __SMRTBellConcentration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SMRTBellConcentration'), 'SMRTBellConcentration', '__httppacificbiosciences_comPacBioSampleInfo_xsd_BioSampleType_SMRTBellConcentration', pyxb.binding.datatypes.float)
    __SMRTBellConcentration._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 64, 8)
    __SMRTBellConcentration._UseLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 64, 8)
    
    SMRTBellConcentration = property(__SMRTBellConcentration.value, __SMRTBellConcentration.set, None, 'in ng/uL, e.g. 4.5')

    
    # Attribute SMRTBellQuantificationMethod uses Python identifier SMRTBellQuantificationMethod
    __SMRTBellQuantificationMethod = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SMRTBellQuantificationMethod'), 'SMRTBellQuantificationMethod', '__httppacificbiosciences_comPacBioSampleInfo_xsd_BioSampleType_SMRTBellQuantificationMethod', pyxb.binding.datatypes.string)
    __SMRTBellQuantificationMethod._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 69, 8)
    __SMRTBellQuantificationMethod._UseLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 69, 8)
    
    SMRTBellQuantificationMethod = property(__SMRTBellQuantificationMethod.value, __SMRTBellQuantificationMethod.set, None, 'e.g. Qubit')

    
    # Attribute BufferName uses Python identifier BufferName
    __BufferName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'BufferName'), 'BufferName', '__httppacificbiosciences_comPacBioSampleInfo_xsd_BioSampleType_BufferName', pyxb.binding.datatypes.string)
    __BufferName._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 74, 8)
    __BufferName._UseLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 74, 8)
    
    BufferName = property(__BufferName.value, __BufferName.set, None, 'e.g. Tris HCl')

    
    # Attribute SamplePrepKit uses Python identifier SamplePrepKit
    __SamplePrepKit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SamplePrepKit'), 'SamplePrepKit', '__httppacificbiosciences_comPacBioSampleInfo_xsd_BioSampleType_SamplePrepKit', pyxb.binding.datatypes.string)
    __SamplePrepKit._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 79, 8)
    __SamplePrepKit._UseLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 79, 8)
    
    SamplePrepKit = property(__SamplePrepKit.value, __SamplePrepKit.set, None, 'e.g. SMRTbell Template Prep Kit')

    
    # Attribute TargetLibrarySize uses Python identifier TargetLibrarySize
    __TargetLibrarySize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TargetLibrarySize'), 'TargetLibrarySize', '__httppacificbiosciences_comPacBioSampleInfo_xsd_BioSampleType_TargetLibrarySize', pyxb.binding.datatypes.string)
    __TargetLibrarySize._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 84, 8)
    __TargetLibrarySize._UseLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 84, 8)
    
    TargetLibrarySize = property(__TargetLibrarySize.value, __TargetLibrarySize.set, None, '2000, 10000, 20000')

    _ElementMap.update({
        __DNABarcodes.name() : __DNABarcodes
    })
    _AttributeMap.update({
        __DateReceived.name() : __DateReceived,
        __Organism.name() : __Organism,
        __Reference.name() : __Reference,
        __DNAType.name() : __DNAType,
        __Concentration.name() : __Concentration,
        __QuantificationMethod.name() : __QuantificationMethod,
        __SMRTBellConcentration.name() : __SMRTBellConcentration,
        __SMRTBellQuantificationMethod.name() : __SMRTBellQuantificationMethod,
        __BufferName.name() : __BufferName,
        __SamplePrepKit.name() : __SamplePrepKit,
        __TargetLibrarySize.name() : __TargetLibrarySize
    })
_module_typeBindings.BioSampleType = BioSampleType
Namespace.addCategoryObject('typeBinding', 'BioSampleType', BioSampleType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (_ImportedBinding__pbbase.BaseEntityType):
    """A list of barcodes associated with the biological sample"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 19, 12)
    _ElementMap = _ImportedBinding__pbbase.BaseEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.BaseEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioSampleInfo.xsd}DNABarcode uses Python identifier DNABarcode
    __DNABarcode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DNABarcode'), 'DNABarcode', '__httppacificbiosciences_comPacBioSampleInfo_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioSampleInfo_xsdDNABarcode', True, pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 23, 20), )

    
    DNABarcode = property(__DNABarcode.value, __DNABarcode.set, None, 'A sequence of barcodes associated with the biological sample')

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __DNABarcode.name() : __DNABarcode
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


BioSamplePointers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSamplePointers'), CTD_ANON, documentation='Back references to other BarcodedSampleType object UniqueIds which utilize this sample', location=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 92, 2))
Namespace.addCategoryObject('elementBinding', BioSamplePointers.name().localName(), BioSamplePointers)

BarcodedSamplePointers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointers'), CTD_ANON_, documentation='Back references to other BarcodedSampleType object UniqueIds which utilize this sample', location=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 112, 2))
Namespace.addCategoryObject('elementBinding', BarcodedSamplePointers.name().localName(), BarcodedSamplePointers)

BioSamples = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSamples'), CTD_ANON_2, documentation='List of biological samples.', location=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 126, 2))
Namespace.addCategoryObject('elementBinding', BioSamples.name().localName(), BioSamples)

BioSample = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSample'), BioSampleType, documentation='An individual biological sample.', location=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 136, 2))
Namespace.addCategoryObject('elementBinding', BioSample.name().localName(), BioSample)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSamplePointer'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON, documentation='Pointer to a single biological sample', location=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 103, 10)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointers'), CTD_ANON_, scope=CTD_ANON, documentation='Back references to other BarcodedSampleType object UniqueIds which utilize this sample', location=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 112, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointers')), pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 102, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BioSamplePointer')), pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 103, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointer'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_, documentation='Pointer to a group of barcoded samples', location=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 118, 8)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointer')), pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 118, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSample'), BioSampleType, scope=CTD_ANON_2, documentation='An individual biological sample.', location=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 136, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BioSample')), pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 132, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




BioSampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DNABarcodes'), CTD_ANON_3, scope=BioSampleType, documentation='A list of barcodes associated with the biological sample', location=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 15, 10)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioBaseDataModel.xsd', 98, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 15, 10))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BioSampleType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioBaseDataModel.xsd', 98, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BioSampleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DNABarcodes')), pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 15, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BioSampleType._Automaton = _BuildAutomaton_3()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DNABarcode'), _ImportedBinding__pbbase.DNABarcode, scope=CTD_ANON_3, documentation='A sequence of barcodes associated with the biological sample', location=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 23, 20)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 19, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioBaseDataModel.xsd', 98, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 23, 20))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioBaseDataModel.xsd', 98, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DNABarcode')), pyxb.utils.utility.Location('/tmp/tmpez6980_gxsds/PacBioSampleInfo.xsd', 23, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_4()

