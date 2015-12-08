# ./_pbbase.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:304355e4be645ec0738f0143f32dd444bf98ad15
# Generated 2015-12-08 13:20:39.133886 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace http://pacificbiosciences.com/PacBioBaseDataModel.xsd [xmlns:pbbase]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:8749368c-9df1-11e5-86b0-001a4acb6b14')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://pacificbiosciences.com/PacBioBaseDataModel.xsd', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 128, 3)
    _Documentation = None
STD_ANON._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 136, 3)
    _Documentation = None
STD_ANON_._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.ID):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 151, 5)
    _Documentation = None
STD_ANON_2._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_2._CF_pattern.addPattern(pattern='[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_pattern)

# Atomic simple type: {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SupportedAcquisitionStates
class SupportedAcquisitionStates (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedAcquisitionStates')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 638, 1)
    _Documentation = None
SupportedAcquisitionStates._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SupportedAcquisitionStates, enum_prefix=None)
SupportedAcquisitionStates.Ready = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Ready', tag='Ready')
SupportedAcquisitionStates.Initializing = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Initializing', tag='Initializing')
SupportedAcquisitionStates.Acquiring = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Acquiring', tag='Acquiring')
SupportedAcquisitionStates.Aligning = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Aligning', tag='Aligning')
SupportedAcquisitionStates.Aligned = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Aligned', tag='Aligned')
SupportedAcquisitionStates.Aborting = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Aborting', tag='Aborting')
SupportedAcquisitionStates.Aborted = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Aborted', tag='Aborted')
SupportedAcquisitionStates.Failed = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Failed', tag='Failed')
SupportedAcquisitionStates.Completing = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Completing', tag='Completing')
SupportedAcquisitionStates.Complete = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Complete', tag='Complete')
SupportedAcquisitionStates.Calibrating = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Calibrating', tag='Calibrating')
SupportedAcquisitionStates.Unknown = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
SupportedAcquisitionStates.Pending = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Pending', tag='Pending')
SupportedAcquisitionStates.ReadyToCalibrate = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='ReadyToCalibrate', tag='ReadyToCalibrate')
SupportedAcquisitionStates.CalibrationComplete = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='CalibrationComplete', tag='CalibrationComplete')
SupportedAcquisitionStates.ReadyToAcquire = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='ReadyToAcquire', tag='ReadyToAcquire')
SupportedAcquisitionStates.FinishingAnalysis = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='FinishingAnalysis', tag='FinishingAnalysis')
SupportedAcquisitionStates.PostPrimaryPending = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='PostPrimaryPending', tag='PostPrimaryPending')
SupportedAcquisitionStates.PostPrimaryAnalysis = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='PostPrimaryAnalysis', tag='PostPrimaryAnalysis')
SupportedAcquisitionStates.TransferPending = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='TransferPending', tag='TransferPending')
SupportedAcquisitionStates.TransferringResults = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='TransferringResults', tag='TransferringResults')
SupportedAcquisitionStates.Error = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Error', tag='Error')
SupportedAcquisitionStates.Stopped = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='Stopped', tag='Stopped')
SupportedAcquisitionStates.TransferFailed = SupportedAcquisitionStates._CF_enumeration.addEnumeration(unicode_value='TransferFailed', tag='TransferFailed')
SupportedAcquisitionStates._InitializeFacetMap(SupportedAcquisitionStates._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SupportedAcquisitionStates', SupportedAcquisitionStates)

# Atomic simple type: {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SupportedDataTypes
class SupportedDataTypes (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedDataTypes')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 666, 1)
    _Documentation = None
SupportedDataTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SupportedDataTypes, enum_prefix=None)
SupportedDataTypes.Int16 = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Int16', tag='Int16')
SupportedDataTypes.Int32 = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Int32', tag='Int32')
SupportedDataTypes.Int64 = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Int64', tag='Int64')
SupportedDataTypes.UInt16 = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='UInt16', tag='UInt16')
SupportedDataTypes.UInt32 = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='UInt32', tag='UInt32')
SupportedDataTypes.UInt64 = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='UInt64', tag='UInt64')
SupportedDataTypes.Single = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Single', tag='Single')
SupportedDataTypes.Double = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Double', tag='Double')
SupportedDataTypes.String = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='String', tag='String')
SupportedDataTypes.DateTime = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='DateTime', tag='DateTime')
SupportedDataTypes.Int16_1D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Int16_1D', tag='Int16_1D')
SupportedDataTypes.Int32_1D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Int32_1D', tag='Int32_1D')
SupportedDataTypes.Int64_1D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Int64_1D', tag='Int64_1D')
SupportedDataTypes.UInt16_1D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='UInt16_1D', tag='UInt16_1D')
SupportedDataTypes.UInt32_1D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='UInt32_1D', tag='UInt32_1D')
SupportedDataTypes.UInt64_1D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='UInt64_1D', tag='UInt64_1D')
SupportedDataTypes.Single_1D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Single_1D', tag='Single_1D')
SupportedDataTypes.Double_1D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Double_1D', tag='Double_1D')
SupportedDataTypes.String_1D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='String_1D', tag='String_1D')
SupportedDataTypes.DateTime_1D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='DateTime_1D', tag='DateTime_1D')
SupportedDataTypes.Int16_2D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Int16_2D', tag='Int16_2D')
SupportedDataTypes.Int32_2D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Int32_2D', tag='Int32_2D')
SupportedDataTypes.Int64_2D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Int64_2D', tag='Int64_2D')
SupportedDataTypes.UInt16_2D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='UInt16_2D', tag='UInt16_2D')
SupportedDataTypes.UInt32_2D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='UInt32_2D', tag='UInt32_2D')
SupportedDataTypes.UInt64_2D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='UInt64_2D', tag='UInt64_2D')
SupportedDataTypes.Single_2D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Single_2D', tag='Single_2D')
SupportedDataTypes.Double_2D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Double_2D', tag='Double_2D')
SupportedDataTypes.String_2D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='String_2D', tag='String_2D')
SupportedDataTypes.DateTime_2D = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='DateTime_2D', tag='DateTime_2D')
SupportedDataTypes.XML = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='XML', tag='XML')
SupportedDataTypes.JSON = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='JSON', tag='JSON')
SupportedDataTypes.Object = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Object', tag='Object')
SupportedDataTypes.Other = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
SupportedDataTypes.Unknown = SupportedDataTypes._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
SupportedDataTypes._InitializeFacetMap(SupportedDataTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SupportedDataTypes', SupportedDataTypes)

# Atomic simple type: {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SupportedNucleotides
class SupportedNucleotides (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedNucleotides')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 705, 1)
    _Documentation = None
SupportedNucleotides._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SupportedNucleotides, enum_prefix=None)
SupportedNucleotides.A = SupportedNucleotides._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
SupportedNucleotides.C = SupportedNucleotides._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
SupportedNucleotides.T = SupportedNucleotides._CF_enumeration.addEnumeration(unicode_value='T', tag='T')
SupportedNucleotides.G = SupportedNucleotides._CF_enumeration.addEnumeration(unicode_value='G', tag='G')
SupportedNucleotides._InitializeFacetMap(SupportedNucleotides._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SupportedNucleotides', SupportedNucleotides)

# Atomic simple type: {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SupportedRunStates
class SupportedRunStates (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedRunStates')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 713, 1)
    _Documentation = None
SupportedRunStates._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SupportedRunStates, enum_prefix=None)
SupportedRunStates.Ready = SupportedRunStates._CF_enumeration.addEnumeration(unicode_value='Ready', tag='Ready')
SupportedRunStates.Idle = SupportedRunStates._CF_enumeration.addEnumeration(unicode_value='Idle', tag='Idle')
SupportedRunStates.System_Test = SupportedRunStates._CF_enumeration.addEnumeration(unicode_value='System Test', tag='System_Test')
SupportedRunStates.Starting = SupportedRunStates._CF_enumeration.addEnumeration(unicode_value='Starting', tag='Starting')
SupportedRunStates.Running = SupportedRunStates._CF_enumeration.addEnumeration(unicode_value='Running', tag='Running')
SupportedRunStates.Aborting = SupportedRunStates._CF_enumeration.addEnumeration(unicode_value='Aborting', tag='Aborting')
SupportedRunStates.Aborted = SupportedRunStates._CF_enumeration.addEnumeration(unicode_value='Aborted', tag='Aborted')
SupportedRunStates.Terminated = SupportedRunStates._CF_enumeration.addEnumeration(unicode_value='Terminated', tag='Terminated')
SupportedRunStates.Completing = SupportedRunStates._CF_enumeration.addEnumeration(unicode_value='Completing', tag='Completing')
SupportedRunStates.Complete = SupportedRunStates._CF_enumeration.addEnumeration(unicode_value='Complete', tag='Complete')
SupportedRunStates.Paused = SupportedRunStates._CF_enumeration.addEnumeration(unicode_value='Paused', tag='Paused')
SupportedRunStates.Unknown = SupportedRunStates._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
SupportedRunStates._InitializeFacetMap(SupportedRunStates._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SupportedRunStates', SupportedRunStates)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """A vector of probabilities, given in the order of increasing filter-bin wavelength, that light emitted by the analog will fall in the corresponding filter bin of the instrument detection system. By convention, the values are normalized to sum to 1."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 14, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Values uses Python identifier Values
    __Values = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Values'), 'Values', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_httppacificbiosciences_comPacBioBaseDataModel_xsdValues', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 16, 8), )

    
    Values = property(__Values.value, __Values.set, None, None)

    
    # Attribute NumberFilterBins uses Python identifier NumberFilterBins
    __NumberFilterBins = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberFilterBins'), 'NumberFilterBins', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_NumberFilterBins', pyxb.binding.datatypes.int, required=True)
    __NumberFilterBins._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 29, 7)
    __NumberFilterBins._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 29, 7)
    
    NumberFilterBins = property(__NumberFilterBins.value, __NumberFilterBins.set, None, 'number of bins describing the spectrum, green to red')

    _ElementMap.update({
        __Values.name() : __Values
    })
    _AttributeMap.update({
        __NumberFilterBins.name() : __NumberFilterBins
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 17, 9)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON__httppacificbiosciences_comPacBioBaseDataModel_xsdValue', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 19, 11), )

    
    Value = property(__Value.value, __Value.set, None, 'There should be as many values as specified in the Number of Filter Bins attribute.\nEach value is a probability, in the range of [0, 1].')

    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 87, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExtensionElement uses Python identifier ExtensionElement
    __ExtensionElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExtensionElement'), 'ExtensionElement', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_2_httppacificbiosciences_comPacBioBaseDataModel_xsdExtensionElement', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 736, 1), )

    
    ExtensionElement = property(__ExtensionElement.value, __ExtensionElement.set, None, 'A generic element whose contents are undefined at the schema level.  This is used to extend the data model.')

    _ElementMap.update({
        __ExtensionElement.name() : __ExtensionElement
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Pointer list to UniqueIds in the system"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 226, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataPointer uses Python identifier DataPointer
    __DataPointer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataPointer'), 'DataPointer', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioBaseDataModel_xsdDataPointer', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 228, 4), )

    
    DataPointer = property(__DataPointer.value, __DataPointer.set, None, None)

    _ElementMap.update({
        __DataPointer.name() : __DataPointer
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Pointers to data that do not reside inside the parent structure"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 260, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResource uses Python identifier ExternalResource
    __ExternalResource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExternalResource'), 'ExternalResource', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_4_httppacificbiosciences_comPacBioBaseDataModel_xsdExternalResource', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 758, 1), )

    
    ExternalResource = property(__ExternalResource.value, __ExternalResource.set, None, 'for example, an output file could be the BAM file, which could be associated with multiple indices into it.')

    _ElementMap.update({
        __ExternalResource.name() : __ExternalResource
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 276, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}FileIndex uses Python identifier FileIndex
    __FileIndex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FileIndex'), 'FileIndex', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioBaseDataModel_xsdFileIndex', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 278, 8), )

    
    FileIndex = property(__FileIndex.value, __FileIndex.set, None, 'e.g. index for output files, allowing one to find information in the output file')

    _ElementMap.update({
        __FileIndex.name() : __FileIndex
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 296, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AutomationParameter uses Python identifier AutomationParameter
    __AutomationParameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter'), 'AutomationParameter', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_6_httppacificbiosciences_comPacBioBaseDataModel_xsdAutomationParameter', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 321, 1), )

    
    AutomationParameter = property(__AutomationParameter.value, __AutomationParameter.set, None, 'One or more collection parameters, such as MovieLength, InsertSize, UseStageStart, IsControl, etc..')

    _ElementMap.update({
        __AutomationParameter.name() : __AutomationParameter
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 407, 11)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Analog uses Python identifier Analog
    __Analog = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Analog'), 'Analog', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_7_httppacificbiosciences_comPacBioBaseDataModel_xsdAnalog', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 409, 13), )

    
    Analog = property(__Analog.value, __Analog.set, None, None)

    _ElementMap.update({
        __Analog.name() : __Analog
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Root element for document containing the container of analog set, SequencingChemistryConfig"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 426, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ChemistryConfig uses Python identifier ChemistryConfig
    __ChemistryConfig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChemistryConfig'), 'ChemistryConfig', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_8_httppacificbiosciences_comPacBioBaseDataModel_xsdChemistryConfig', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 797, 1), )

    
    ChemistryConfig = property(__ChemistryConfig.value, __ChemistryConfig.set, None, None)

    _ElementMap.update({
        __ChemistryConfig.name() : __ChemistryConfig
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 440, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Analog uses Python identifier Analog
    __Analog = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Analog'), 'Analog', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_9_httppacificbiosciences_comPacBioBaseDataModel_xsdAnalog', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 442, 8), )

    
    Analog = property(__Analog.value, __Analog.set, None, None)

    _ElementMap.update({
        __Analog.name() : __Analog
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 452, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute SNR_A uses Python identifier SNR_A
    __SNR_A = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SNR_A'), 'SNR_A', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_10_SNR_A', pyxb.binding.datatypes.float, required=True)
    __SNR_A._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 453, 7)
    __SNR_A._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 453, 7)
    
    SNR_A = property(__SNR_A.value, __SNR_A.set, None, None)

    
    # Attribute SNR_C uses Python identifier SNR_C
    __SNR_C = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SNR_C'), 'SNR_C', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_10_SNR_C', pyxb.binding.datatypes.float, required=True)
    __SNR_C._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 454, 7)
    __SNR_C._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 454, 7)
    
    SNR_C = property(__SNR_C.value, __SNR_C.set, None, None)

    
    # Attribute SNR_G uses Python identifier SNR_G
    __SNR_G = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SNR_G'), 'SNR_G', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_10_SNR_G', pyxb.binding.datatypes.float, required=True)
    __SNR_G._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 455, 7)
    __SNR_G._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 455, 7)
    
    SNR_G = property(__SNR_G.value, __SNR_G.set, None, None)

    
    # Attribute SNR_T uses Python identifier SNR_T
    __SNR_T = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SNR_T'), 'SNR_T', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_10_SNR_T', pyxb.binding.datatypes.float, required=True)
    __SNR_T._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 456, 7)
    __SNR_T._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 456, 7)
    
    SNR_T = property(__SNR_T.value, __SNR_T.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __SNR_A.name() : __SNR_A,
        __SNR_C.name() : __SNR_C,
        __SNR_G.name() : __SNR_G,
        __SNR_T.name() : __SNR_T
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 477, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BinCount uses Python identifier BinCount
    __BinCount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinCount'), 'BinCount', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_11_httppacificbiosciences_comPacBioBaseDataModel_xsdBinCount', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 479, 8), )

    
    BinCount = property(__BinCount.value, __BinCount.set, None, None)

    _ElementMap.update({
        __BinCount.name() : __BinCount
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 503, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BinCount uses Python identifier BinCount
    __BinCount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinCount'), 'BinCount', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_12_httppacificbiosciences_comPacBioBaseDataModel_xsdBinCount', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 505, 8), )

    
    BinCount = property(__BinCount.value, __BinCount.set, None, None)

    _ElementMap.update({
        __BinCount.name() : __BinCount
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 511, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BinLabel uses Python identifier BinLabel
    __BinLabel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinLabel'), 'BinLabel', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_13_httppacificbiosciences_comPacBioBaseDataModel_xsdBinLabel', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 513, 8), )

    
    BinLabel = property(__BinLabel.value, __BinLabel.set, None, None)

    _ElementMap.update({
        __BinLabel.name() : __BinLabel
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 533, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Val uses Python identifier Val
    __Val = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Val'), 'Val', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_14_httppacificbiosciences_comPacBioBaseDataModel_xsdVal', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 535, 8), )

    
    Val = property(__Val.value, __Val.set, None, None)

    _ElementMap.update({
        __Val.name() : __Val
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}UserDefinedFieldsType with content type ELEMENT_ONLY
class UserDefinedFieldsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}UserDefinedFieldsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UserDefinedFieldsType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 729, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntities uses Python identifier DataEntities
    __DataEntities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataEntities'), 'DataEntities', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_UserDefinedFieldsType_httppacificbiosciences_comPacBioBaseDataModel_xsdDataEntities', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 731, 3), )

    
    DataEntities = property(__DataEntities.value, __DataEntities.set, None, None)

    _ElementMap.update({
        __DataEntities.name() : __DataEntities
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'UserDefinedFieldsType', UserDefinedFieldsType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}FilterType with content type ELEMENT_ONLY
class FilterType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}FilterType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FilterType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 741, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Properties uses Python identifier Properties
    __Properties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Properties'), 'Properties', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_FilterType_httppacificbiosciences_comPacBioBaseDataModel_xsdProperties', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 743, 3), )

    
    Properties = property(__Properties.value, __Properties.set, None, None)

    _ElementMap.update({
        __Properties.name() : __Properties
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'FilterType', FilterType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 744, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Property uses Python identifier Property
    __Property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Property'), 'Property', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioBaseDataModel_xsdProperty', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 746, 6), )

    
    Property = property(__Property.value, __Property.set, None, None)

    _ElementMap.update({
        __Property.name() : __Property
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 747, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_16_Name', pyxb.binding.datatypes.string, required=True)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 748, 8)
    __Name._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 748, 8)
    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_16_Value', pyxb.binding.datatypes.string, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 749, 8)
    __Value._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 749, 8)
    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Attribute Operator uses Python identifier Operator
    __Operator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Operator'), 'Operator', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_16_Operator', pyxb.binding.datatypes.string, required=True)
    __Operator._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 750, 8)
    __Operator._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 750, 8)
    
    Operator = property(__Operator.value, __Operator.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Name.name() : __Name,
        __Value.name() : __Value,
        __Operator.name() : __Operator
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 769, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Items uses Python identifier Items
    __Items = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Items'), 'Items', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_17_httppacificbiosciences_comPacBioBaseDataModel_xsdItems', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 771, 4), )

    
    Items = property(__Items.value, __Items.set, None, None)

    _ElementMap.update({
        __Items.name() : __Items
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 772, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Item uses Python identifier Item
    __Item = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Item'), 'Item', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_18_httppacificbiosciences_comPacBioBaseDataModel_xsdItem', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 774, 7), )

    
    Item = property(__Item.value, __Item.set, None, None)

    _ElementMap.update({
        __Item.name() : __Item
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}MapType with content type ELEMENT_ONLY
class MapType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}MapType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MapType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 785, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}KeyValueMap uses Python identifier KeyValueMap
    __KeyValueMap = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KeyValueMap'), 'KeyValueMap', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_MapType_httppacificbiosciences_comPacBioBaseDataModel_xsdKeyValueMap', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 768, 1), )

    
    KeyValueMap = property(__KeyValueMap.value, __KeyValueMap.set, None, None)

    _ElementMap.update({
        __KeyValueMap.name() : __KeyValueMap
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'MapType', MapType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}MapItemType with content type ELEMENT_ONLY
class MapItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}MapItemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MapItemType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 790, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Key uses Python identifier Key
    __Key = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Key'), 'Key', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_MapItemType_httppacificbiosciences_comPacBioBaseDataModel_xsdKey', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 792, 3), )

    
    Key = property(__Key.value, __Key.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_MapItemType_httppacificbiosciences_comPacBioBaseDataModel_xsdValue', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 793, 3), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Description'), 'Description', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_MapItemType_httppacificbiosciences_comPacBioBaseDataModel_xsdDescription', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 794, 3), )

    
    Description = property(__Description.value, __Description.set, None, None)

    _ElementMap.update({
        __Key.name() : __Key,
        __Value.name() : __Value,
        __Description.name() : __Description
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'MapItemType', MapItemType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType with content type ELEMENT_ONLY
class BaseEntityType (pyxb.binding.basis.complexTypeDefinition):
    """This is the base element type for all types in this data model"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BaseEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 81, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_BaseEntityType_httppacificbiosciences_comPacBioBaseDataModel_xsdExtensions', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, None)

    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_BaseEntityType_Name', pyxb.binding.datatypes.string)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 94, 2)
    __Name._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 94, 2)
    
    Name = property(__Name.value, __Name.set, None, 'A short text identifier; uniqueness not necessary')

    
    # Attribute Description uses Python identifier Description
    __Description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Description'), 'Description', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_BaseEntityType_Description', pyxb.binding.datatypes.string)
    __Description._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 99, 2)
    __Description._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 99, 2)
    
    Description = property(__Description.value, __Description.set, None, 'A long text description of the object')

    
    # Attribute Tags uses Python identifier Tags
    __Tags = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Tags'), 'Tags', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_BaseEntityType_Tags', pyxb.binding.datatypes.string)
    __Tags._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 104, 2)
    __Tags._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 104, 2)
    
    Tags = property(__Tags.value, __Tags.set, None, 'A set of keywords assigned to the object to help describe it and allow it to be found via search')

    
    # Attribute Format uses Python identifier Format
    __Format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Format'), 'Format', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_BaseEntityType_Format', pyxb.binding.datatypes.string)
    __Format._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 109, 2)
    __Format._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 109, 2)
    
    Format = property(__Format.value, __Format.set, None, 'Optional, but recommended.  The MIME-Type of the referenced file.  See http://www.iana.org/assignments/media-types/media-types.xhtml for examples')

    
    # Attribute ResourceId uses Python identifier ResourceId
    __ResourceId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ResourceId'), 'ResourceId', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_BaseEntityType_ResourceId', pyxb.binding.datatypes.anyURI)
    __ResourceId._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 114, 2)
    __ResourceId._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 114, 2)
    
    ResourceId = property(__ResourceId.value, __ResourceId.set, None, 'A uniform resource identifier used to identify a "web" resource. e.g. svc://run/acquisition/alignment/gridding')

    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Version'), 'Version', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_BaseEntityType_Version', pyxb.binding.datatypes.string)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 119, 2)
    __Version._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 119, 2)
    
    Version = property(__Version.value, __Version.set, None, 'An optional identifier denoting the revision of this particular entity')

    
    # Attribute CreatedAt uses Python identifier CreatedAt
    __CreatedAt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CreatedAt'), 'CreatedAt', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_BaseEntityType_CreatedAt', STD_ANON)
    __CreatedAt._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 124, 2)
    __CreatedAt._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 124, 2)
    
    CreatedAt = property(__CreatedAt.value, __CreatedAt.set, None, 'Timestamp designating the creation of this object, relative to UTC; millisecond precision is expected.')

    
    # Attribute ModifiedAt uses Python identifier ModifiedAt
    __ModifiedAt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ModifiedAt'), 'ModifiedAt', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_BaseEntityType_ModifiedAt', STD_ANON_)
    __ModifiedAt._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 132, 2)
    __ModifiedAt._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 132, 2)
    
    ModifiedAt = property(__ModifiedAt.value, __ModifiedAt.set, None, 'Timestamp designating the modification of this object, relative to UTC; millisecond precision is expected.')

    _ElementMap.update({
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __Name.name() : __Name,
        __Description.name() : __Description,
        __Tags.name() : __Tags,
        __Format.name() : __Format,
        __ResourceId.name() : __ResourceId,
        __Version.name() : __Version,
        __CreatedAt.name() : __CreatedAt,
        __ModifiedAt.name() : __ModifiedAt
    })
Namespace.addCategoryObject('typeBinding', 'BaseEntityType', BaseEntityType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType with content type ELEMENT_ONLY
class AnalogType (BaseEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnalogType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 6, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Spectrum uses Python identifier Spectrum
    __Spectrum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Spectrum'), 'Spectrum', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AnalogType_httppacificbiosciences_comPacBioBaseDataModel_xsdSpectrum', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 10, 5), )

    
    Spectrum = property(__Spectrum.value, __Spectrum.set, None, 'A vector of probabilities, given in the order of increasing filter-bin wavelength, that light emitted by the analog will fall in the corresponding filter bin of the instrument detection system. By convention, the values are normalized to sum to 1.')

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}RelativeAmplitude uses Python identifier RelativeAmplitude
    __RelativeAmplitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RelativeAmplitude'), 'RelativeAmplitude', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AnalogType_httppacificbiosciences_comPacBioBaseDataModel_xsdRelativeAmplitude', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 36, 5), )

    
    RelativeAmplitude = property(__RelativeAmplitude.value, __RelativeAmplitude.set, None, 'Relative intensity of emission vs. a reference analog using standardized metrology \u2013 e.g., relative to the amplitude of the \u201c542\u201d analog as measured by the mean DWS pkMid on the Astro instrument.')

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}IntraPulseXsnCV uses Python identifier IntraPulseXsnCV
    __IntraPulseXsnCV = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IntraPulseXsnCV'), 'IntraPulseXsnCV', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AnalogType_httppacificbiosciences_comPacBioBaseDataModel_xsdIntraPulseXsnCV', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 41, 5), )

    
    IntraPulseXsnCV = property(__IntraPulseXsnCV.value, __IntraPulseXsnCV.set, None, 'The 1-sigma fractional variation of the intra-pulse signal, independent of any Shot noise associated with that signal')

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}InterPulseXsnCV uses Python identifier InterPulseXsnCV
    __InterPulseXsnCV = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InterPulseXsnCV'), 'InterPulseXsnCV', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AnalogType_httppacificbiosciences_comPacBioBaseDataModel_xsdInterPulseXsnCV', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 46, 5), )

    
    InterPulseXsnCV = property(__InterPulseXsnCV.value, __InterPulseXsnCV.set, None, 'The 1-sigma fractional variation, pulse-to-pulse, of the mean signal level (i.e., the pkMid).')

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DiffusionXsnCV uses Python identifier DiffusionXsnCV
    __DiffusionXsnCV = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DiffusionXsnCV'), 'DiffusionXsnCV', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AnalogType_httppacificbiosciences_comPacBioBaseDataModel_xsdDiffusionXsnCV', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 51, 5), )

    
    DiffusionXsnCV = property(__DiffusionXsnCV.value, __DiffusionXsnCV.set, None, None)

    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Base uses Python identifier Base
    __Base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Base'), 'Base', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AnalogType_Base', SupportedNucleotides)
    __Base._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 53, 4)
    __Base._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 53, 4)
    
    Base = property(__Base.value, __Base.set, None, 'The base label, A, C, T, or G')

    
    # Attribute Nucleotide uses Python identifier Nucleotide
    __Nucleotide = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Nucleotide'), 'Nucleotide', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AnalogType_Nucleotide', pyxb.binding.datatypes.string)
    __Nucleotide._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 58, 4)
    __Nucleotide._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 58, 4)
    
    Nucleotide = property(__Nucleotide.value, __Nucleotide.set, None, 'The type and number of nucleotides on a given analog. e.g. (dT6P)6')

    
    # Attribute Wavelength uses Python identifier Wavelength
    __Wavelength = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Wavelength'), 'Wavelength', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AnalogType_Wavelength', pyxb.binding.datatypes.float)
    __Wavelength._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 63, 4)
    __Wavelength._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 63, 4)
    
    Wavelength = property(__Wavelength.value, __Wavelength.set, None, 'The peak emission wavelength associated with the dye label in nm.')

    
    # Attribute CompoundID uses Python identifier CompoundID
    __CompoundID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CompoundID'), 'CompoundID', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AnalogType_CompoundID', pyxb.binding.datatypes.string)
    __CompoundID._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 68, 4)
    __CompoundID._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 68, 4)
    
    CompoundID = property(__CompoundID.value, __CompoundID.set, None, 'Identification code of the final compound.  The suffix \u2018N\u2019 should be used to distinguish these values from enzyme identifiers.\te.g. 5031N')

    
    # Attribute LotID uses Python identifier LotID
    __LotID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'LotID'), 'LotID', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AnalogType_LotID', pyxb.binding.datatypes.string)
    __LotID._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 73, 4)
    __LotID._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 73, 4)
    
    LotID = property(__LotID.value, __LotID.set, None, 'Identification code for the build of the final compound, written as initials/date, where date is written as YYYY-MM-DD.\te.g. js/2014-06-30')

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __Spectrum.name() : __Spectrum,
        __RelativeAmplitude.name() : __RelativeAmplitude,
        __IntraPulseXsnCV.name() : __IntraPulseXsnCV,
        __InterPulseXsnCV.name() : __InterPulseXsnCV,
        __DiffusionXsnCV.name() : __DiffusionXsnCV
    })
    _AttributeMap.update({
        __Base.name() : __Base,
        __Nucleotide.name() : __Nucleotide,
        __Wavelength.name() : __Wavelength,
        __CompoundID.name() : __CompoundID,
        __LotID.name() : __LotID
    })
Namespace.addCategoryObject('typeBinding', 'AnalogType', AnalogType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StrictEntityType with content type ELEMENT_ONLY
class StrictEntityType (BaseEntityType):
    """This is the base element type for all types in this data model"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StrictEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 141, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute UniqueId uses Python identifier UniqueId
    __UniqueId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UniqueId'), 'UniqueId', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StrictEntityType_UniqueId', STD_ANON_2, required=True)
    __UniqueId._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 147, 4)
    __UniqueId._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 147, 4)
    
    UniqueId = property(__UniqueId.value, __UniqueId.set, None, 'A unique identifier, such as a GUID - likely autogenerated')

    
    # Attribute MetaType uses Python identifier MetaType
    __MetaType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MetaType'), 'MetaType', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StrictEntityType_MetaType', pyxb.binding.datatypes.string, required=True)
    __MetaType._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 157, 4)
    __MetaType._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 157, 4)
    
    MetaType = property(__MetaType.value, __MetaType.set, None, 'Controlled Vocabulary, meant as a means to group similar entities; the type of the object, e.g. Instrument Run, Secondary Run, Assay, Sample, Barcode, Alignment File, Alarm, Exception, Metric, SystemEvent, etc.')

    
    # Attribute TimeStampedName uses Python identifier TimeStampedName
    __TimeStampedName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TimeStampedName'), 'TimeStampedName', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StrictEntityType_TimeStampedName', pyxb.binding.datatypes.string, required=True)
    __TimeStampedName._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 162, 4)
    __TimeStampedName._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 162, 4)
    
    TimeStampedName = property(__TimeStampedName.value, __TimeStampedName.set, None, 'This is NOT intended to be used as a unique field.  For uniqueness, use UniqueId.  In order to not utilize customer provided names, this attribute may be used as an alternative means of Human Readable ID, e.g. instrumentId-Run-150304_231155')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __UniqueId.name() : __UniqueId,
        __MetaType.name() : __MetaType,
        __TimeStampedName.name() : __TimeStampedName
    })
Namespace.addCategoryObject('typeBinding', 'StrictEntityType', StrictEntityType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType with content type ELEMENT_ONLY
class DataEntityType (BaseEntityType):
    """Extends BaseEntityType and adds a value element.  The intent is to have only one of the value elements exist at any point in time; however, this is not enforced."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 181, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}EncodedValue uses Python identifier EncodedValue
    __EncodedValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue'), 'EncodedValue', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_DataEntityType_httppacificbiosciences_comPacBioBaseDataModel_xsdEncodedValue', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5), )

    
    EncodedValue = property(__EncodedValue.value, __EncodedValue.set, None, 'A complex data type element, such as an image, file, binary object, etc.')

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}CheckSum uses Python identifier CheckSum
    __CheckSum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CheckSum'), 'CheckSum', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_DataEntityType_httppacificbiosciences_comPacBioBaseDataModel_xsdCheckSum', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5), )

    
    CheckSum = property(__CheckSum.value, __CheckSum.set, None, 'small-size datum of the attached value for the purpose of detecting errors or modification which may have been introduced during its transmission or storage')

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType uses Python identifier ValueDataType
    __ValueDataType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ValueDataType'), 'ValueDataType', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_DataEntityType_ValueDataType', SupportedDataTypes, unicode_default='Object')
    __ValueDataType._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 199, 4)
    __ValueDataType._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 199, 4)
    
    ValueDataType = property(__ValueDataType.value, __ValueDataType.set, None, 'The datatype of the simple or encoded value.  If not specified, a string is assumed.')

    
    # Attribute SimpleValue uses Python identifier SimpleValue
    __SimpleValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SimpleValue'), 'SimpleValue', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_DataEntityType_SimpleValue', pyxb.binding.datatypes.anySimpleType)
    __SimpleValue._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 204, 4)
    __SimpleValue._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 204, 4)
    
    SimpleValue = property(__SimpleValue.value, __SimpleValue.set, None, 'A simple data type element, such as a string, int, float, etc.')

    
    # Attribute MetaType uses Python identifier MetaType
    __MetaType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MetaType'), 'MetaType', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_DataEntityType_MetaType', pyxb.binding.datatypes.string)
    __MetaType._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 209, 4)
    __MetaType._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 209, 4)
    
    MetaType = property(__MetaType.value, __MetaType.set, None, 'Controlled Vocabulary, meant as a means to group similar entities; the type of the object, e.g. Instrument Run, Secondary Run, Assay, Sample, Barcode, Alignment File, Alarm, Exception, Metric, SystemEvent, etc.')

    
    # Attribute TimeStampedName uses Python identifier TimeStampedName
    __TimeStampedName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TimeStampedName'), 'TimeStampedName', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_DataEntityType_TimeStampedName', pyxb.binding.datatypes.string)
    __TimeStampedName._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 214, 4)
    __TimeStampedName._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 214, 4)
    
    TimeStampedName = property(__TimeStampedName.value, __TimeStampedName.set, None, 'This is NOT intended to be used as a unique field.  For uniqueness, use UniqueId.  In order to not utilize customer provided names, this attribute may be used as an alternative means of Human Readable ID, e.g. instrumentId-Run-150304_231155')

    _ElementMap.update({
        __EncodedValue.name() : __EncodedValue,
        __CheckSum.name() : __CheckSum
    })
    _AttributeMap.update({
        __ValueDataType.name() : __ValueDataType,
        __SimpleValue.name() : __SimpleValue,
        __MetaType.name() : __MetaType,
        __TimeStampedName.name() : __TimeStampedName
    })
Namespace.addCategoryObject('typeBinding', 'DataEntityType', DataEntityType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DNABarcode with content type ELEMENT_ONLY
class DNABarcode (BaseEntityType):
    """Composite of uuid, sequence, and name"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DNABarcode')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 232, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute DNASequence uses Python identifier DNASequence
    __DNASequence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DNASequence'), 'DNASequence', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_DNABarcode_DNASequence', pyxb.binding.datatypes.anySimpleType)
    __DNASequence._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 238, 4)
    __DNASequence._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 238, 4)
    
    DNASequence = property(__DNASequence.value, __DNASequence.set, None, "This is the sample's DNA barcode")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __DNASequence.name() : __DNASequence
    })
Namespace.addCategoryObject('typeBinding', 'DNABarcode', DNABarcode)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AutomationType with content type ELEMENT_ONLY
class AutomationType (BaseEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AutomationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AutomationType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 291, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AutomationParameters uses Python identifier AutomationParameters
    __AutomationParameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameters'), 'AutomationParameters', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AutomationType_httppacificbiosciences_comPacBioBaseDataModel_xsdAutomationParameters', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 295, 5), )

    
    AutomationParameters = property(__AutomationParameters.value, __AutomationParameters.set, None, None)

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute PartNumber uses Python identifier PartNumber
    __PartNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PartNumber'), 'PartNumber', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AutomationType_PartNumber', pyxb.binding.datatypes.string)
    __PartNumber._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 303, 4)
    __PartNumber._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 303, 4)
    
    PartNumber = property(__PartNumber.value, __PartNumber.set, None, 'Defines a part number, mainly for use in defining incompatibility with other PB kit PNs, if necessary')

    
    # Attribute IsRestricted uses Python identifier IsRestricted
    __IsRestricted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IsRestricted'), 'IsRestricted', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AutomationType_IsRestricted', pyxb.binding.datatypes.boolean, unicode_default='false')
    __IsRestricted._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 308, 4)
    __IsRestricted._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 308, 4)
    
    IsRestricted = property(__IsRestricted.value, __IsRestricted.set, None, 'Allows for an automation to be marked for internal use or by admin users only')

    
    # Attribute IsObsolete uses Python identifier IsObsolete
    __IsObsolete = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IsObsolete'), 'IsObsolete', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_AutomationType_IsObsolete', pyxb.binding.datatypes.boolean, unicode_default='false')
    __IsObsolete._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 313, 4)
    __IsObsolete._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 313, 4)
    
    IsObsolete = property(__IsObsolete.value, __IsObsolete.set, None, 'Allows for an automation to be marked as obsolete')

    _ElementMap.update({
        __AutomationParameters.name() : __AutomationParameters
    })
    _AttributeMap.update({
        __PartNumber.name() : __PartNumber,
        __IsRestricted.name() : __IsRestricted,
        __IsObsolete.name() : __IsObsolete
    })
Namespace.addCategoryObject('typeBinding', 'AutomationType', AutomationType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}IncompatiblePairType with content type ELEMENT_ONLY
class IncompatiblePairType (BaseEntityType):
    """Describes a bidirectional incompatibility between part numbers.

By default, any PN is compatible for use with other PNs in the system.  In order to exclude the usage of one or more PNs with this one, the pairwise incompatible PNs are listed here."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePairType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 326, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute PartA uses Python identifier PartA
    __PartA = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PartA'), 'PartA', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_IncompatiblePairType_PartA', pyxb.binding.datatypes.string, required=True)
    __PartA._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 334, 4)
    __PartA._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 334, 4)
    
    PartA = property(__PartA.value, __PartA.set, None, "An automation or kit Part Number that's incompatible with Part Number B")

    
    # Attribute PartB uses Python identifier PartB
    __PartB = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PartB'), 'PartB', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_IncompatiblePairType_PartB', pyxb.binding.datatypes.string, required=True)
    __PartB._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 339, 4)
    __PartB._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 339, 4)
    
    PartB = property(__PartB.value, __PartB.set, None, "An automation or kit Part Number that's incompatible with Part Number A")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __PartA.name() : __PartA,
        __PartB.name() : __PartB
    })
Namespace.addCategoryObject('typeBinding', 'IncompatiblePairType', IncompatiblePairType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (BaseEntityType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 402, 6)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Analogs uses Python identifier Analogs
    __Analogs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Analogs'), 'Analogs', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_CTD_ANON_19_httppacificbiosciences_comPacBioBaseDataModel_xsdAnalogs', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 406, 10), )

    
    Analogs = property(__Analogs.value, __Analogs.set, None, None)

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __Analogs.name() : __Analogs
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StatsContinuousDistType with content type ELEMENT_ONLY
class StatsContinuousDistType (BaseEntityType):
    """Continuous distribution class"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StatsContinuousDistType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 463, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SampleSize uses Python identifier SampleSize
    __SampleSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SampleSize'), 'SampleSize', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdSampleSize', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 470, 5), )

    
    SampleSize = property(__SampleSize.value, __SampleSize.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SampleMean uses Python identifier SampleMean
    __SampleMean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SampleMean'), 'SampleMean', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdSampleMean', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 471, 5), )

    
    SampleMean = property(__SampleMean.value, __SampleMean.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SampleMed uses Python identifier SampleMed
    __SampleMed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SampleMed'), 'SampleMed', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdSampleMed', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 472, 5), )

    
    SampleMed = property(__SampleMed.value, __SampleMed.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SampleStd uses Python identifier SampleStd
    __SampleStd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SampleStd'), 'SampleStd', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdSampleStd', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 473, 5), )

    
    SampleStd = property(__SampleStd.value, __SampleStd.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Sample95thPct uses Python identifier Sample95thPct
    __Sample95thPct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Sample95thPct'), 'Sample95thPct', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdSample95thPct', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 474, 5), )

    
    Sample95thPct = property(__Sample95thPct.value, __Sample95thPct.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}NumBins uses Python identifier NumBins
    __NumBins = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumBins'), 'NumBins', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdNumBins', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 475, 5), )

    
    NumBins = property(__NumBins.value, __NumBins.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BinCounts uses Python identifier BinCounts
    __BinCounts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinCounts'), 'BinCounts', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdBinCounts', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 476, 5), )

    
    BinCounts = property(__BinCounts.value, __BinCounts.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BinWidth uses Python identifier BinWidth
    __BinWidth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinWidth'), 'BinWidth', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdBinWidth', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 483, 5), )

    
    BinWidth = property(__BinWidth.value, __BinWidth.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}MinOutlierValue uses Python identifier MinOutlierValue
    __MinOutlierValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MinOutlierValue'), 'MinOutlierValue', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdMinOutlierValue', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 484, 5), )

    
    MinOutlierValue = property(__MinOutlierValue.value, __MinOutlierValue.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}MinBinValue uses Python identifier MinBinValue
    __MinBinValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MinBinValue'), 'MinBinValue', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdMinBinValue', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 485, 5), )

    
    MinBinValue = property(__MinBinValue.value, __MinBinValue.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}MaxBinValue uses Python identifier MaxBinValue
    __MaxBinValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MaxBinValue'), 'MaxBinValue', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdMaxBinValue', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 486, 5), )

    
    MaxBinValue = property(__MaxBinValue.value, __MaxBinValue.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}MaxOutlierValue uses Python identifier MaxOutlierValue
    __MaxOutlierValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MaxOutlierValue'), 'MaxOutlierValue', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdMaxOutlierValue', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 487, 5), )

    
    MaxOutlierValue = property(__MaxOutlierValue.value, __MaxOutlierValue.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}MetricDescription uses Python identifier MetricDescription
    __MetricDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MetricDescription'), 'MetricDescription', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdMetricDescription', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 488, 5), )

    
    MetricDescription = property(__MetricDescription.value, __MetricDescription.set, None, None)

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Channel uses Python identifier Channel
    __Channel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Channel'), 'Channel', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsContinuousDistType_Channel', pyxb.binding.datatypes.string)
    __Channel._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 490, 4)
    __Channel._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 490, 4)
    
    Channel = property(__Channel.value, __Channel.set, None, None)

    _ElementMap.update({
        __SampleSize.name() : __SampleSize,
        __SampleMean.name() : __SampleMean,
        __SampleMed.name() : __SampleMed,
        __SampleStd.name() : __SampleStd,
        __Sample95thPct.name() : __Sample95thPct,
        __NumBins.name() : __NumBins,
        __BinCounts.name() : __BinCounts,
        __BinWidth.name() : __BinWidth,
        __MinOutlierValue.name() : __MinOutlierValue,
        __MinBinValue.name() : __MinBinValue,
        __MaxBinValue.name() : __MaxBinValue,
        __MaxOutlierValue.name() : __MaxOutlierValue,
        __MetricDescription.name() : __MetricDescription
    })
    _AttributeMap.update({
        __Channel.name() : __Channel
    })
Namespace.addCategoryObject('typeBinding', 'StatsContinuousDistType', StatsContinuousDistType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StatsDiscreteDistType with content type ELEMENT_ONLY
class StatsDiscreteDistType (BaseEntityType):
    """Discrete distribution class"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StatsDiscreteDistType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 494, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}NumBins uses Python identifier NumBins
    __NumBins = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumBins'), 'NumBins', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsDiscreteDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdNumBins', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 501, 5), )

    
    NumBins = property(__NumBins.value, __NumBins.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BinCounts uses Python identifier BinCounts
    __BinCounts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinCounts'), 'BinCounts', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsDiscreteDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdBinCounts', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 502, 5), )

    
    BinCounts = property(__BinCounts.value, __BinCounts.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}MetricDescription uses Python identifier MetricDescription
    __MetricDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MetricDescription'), 'MetricDescription', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsDiscreteDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdMetricDescription', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 509, 5), )

    
    MetricDescription = property(__MetricDescription.value, __MetricDescription.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BinLabels uses Python identifier BinLabels
    __BinLabels = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinLabels'), 'BinLabels', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsDiscreteDistType_httppacificbiosciences_comPacBioBaseDataModel_xsdBinLabels', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 510, 5), )

    
    BinLabels = property(__BinLabels.value, __BinLabels.set, None, None)

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __NumBins.name() : __NumBins,
        __BinCounts.name() : __BinCounts,
        __MetricDescription.name() : __MetricDescription,
        __BinLabels.name() : __BinLabels
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'StatsDiscreteDistType', StatsDiscreteDistType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StatsTimeSeriesType with content type ELEMENT_ONLY
class StatsTimeSeriesType (BaseEntityType):
    """Time series (for time-dependent metrics)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StatsTimeSeriesType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 521, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}TimeUnits uses Python identifier TimeUnits
    __TimeUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeUnits'), 'TimeUnits', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsTimeSeriesType_httppacificbiosciences_comPacBioBaseDataModel_xsdTimeUnits', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 528, 5), )

    
    TimeUnits = property(__TimeUnits.value, __TimeUnits.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ValueUnits uses Python identifier ValueUnits
    __ValueUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValueUnits'), 'ValueUnits', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsTimeSeriesType_httppacificbiosciences_comPacBioBaseDataModel_xsdValueUnits', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 529, 5), )

    
    ValueUnits = property(__ValueUnits.value, __ValueUnits.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), 'StartTime', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsTimeSeriesType_httppacificbiosciences_comPacBioBaseDataModel_xsdStartTime', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 530, 5), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}MeasInterval uses Python identifier MeasInterval
    __MeasInterval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MeasInterval'), 'MeasInterval', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsTimeSeriesType_httppacificbiosciences_comPacBioBaseDataModel_xsdMeasInterval', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 531, 5), )

    
    MeasInterval = property(__MeasInterval.value, __MeasInterval.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Values uses Python identifier Values
    __Values = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Values'), 'Values', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_StatsTimeSeriesType_httppacificbiosciences_comPacBioBaseDataModel_xsdValues', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 532, 5), )

    
    Values = property(__Values.value, __Values.set, None, None)

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __TimeUnits.name() : __TimeUnits,
        __ValueUnits.name() : __ValueUnits,
        __StartTime.name() : __StartTime,
        __MeasInterval.name() : __MeasInterval,
        __Values.name() : __Values
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'StatsTimeSeriesType', StatsTimeSeriesType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (AnalogType):
    """An unlimited number of analogs listed for the purposes of hosting in a configuration file. e.g. a list of all possible analogs on the system"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 174, 2)
    _ElementMap = AnalogType._ElementMap.copy()
    _AttributeMap = AnalogType._AttributeMap.copy()
    # Base type is AnalogType
    
    # Element Spectrum ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Spectrum) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Element RelativeAmplitude ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}RelativeAmplitude) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Element IntraPulseXsnCV ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}IntraPulseXsnCV) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Element InterPulseXsnCV ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}InterPulseXsnCV) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Element DiffusionXsnCV ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DiffusionXsnCV) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Base inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Attribute Nucleotide inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Attribute Wavelength inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Attribute CompoundID inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Attribute LotID inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (AnalogType):
    """A set of four analogs, one for each of the nucleotides, grouped together for the purposes of a single experiment."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 250, 2)
    _ElementMap = AnalogType._ElementMap.copy()
    _AttributeMap = AnalogType._AttributeMap.copy()
    # Base type is AnalogType
    
    # Element Spectrum ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Spectrum) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Element RelativeAmplitude ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}RelativeAmplitude) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Element IntraPulseXsnCV ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}IntraPulseXsnCV) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Element InterPulseXsnCV ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}InterPulseXsnCV) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Element DiffusionXsnCV ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DiffusionXsnCV) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Base inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Attribute Nucleotide inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Attribute Wavelength inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Attribute CompoundID inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Attribute LotID inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}AnalogType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}InputOutputDataType with content type ELEMENT_ONLY
class InputOutputDataType (StrictEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}InputOutputDataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InputOutputDataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 266, 1)
    _ElementMap = StrictEntityType._ElementMap.copy()
    _AttributeMap = StrictEntityType._AttributeMap.copy()
    # Base type is StrictEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StrictEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StrictEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StrictEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'InputOutputDataType', InputOutputDataType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType with content type ELEMENT_ONLY
class PartNumberType (DataEntityType):
    """Generic representation of a supply kit. 

If the part number has an NFC associated with it, the contents of the NFC may be encoded here."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartNumberType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 347, 1)
    _ElementMap = DataEntityType._ElementMap.copy()
    _AttributeMap = DataEntityType._AttributeMap.copy()
    # Base type is DataEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute PartNumber uses Python identifier PartNumber
    __PartNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PartNumber'), 'PartNumber', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_PartNumberType_PartNumber', pyxb.binding.datatypes.string)
    __PartNumber._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 355, 4)
    __PartNumber._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 355, 4)
    
    PartNumber = property(__PartNumber.value, __PartNumber.set, None, 'The kit part number')

    
    # Attribute LotNumber uses Python identifier LotNumber
    __LotNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'LotNumber'), 'LotNumber', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_PartNumberType_LotNumber', pyxb.binding.datatypes.string)
    __LotNumber._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 360, 4)
    __LotNumber._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 360, 4)
    
    LotNumber = property(__LotNumber.value, __LotNumber.set, None, 'The kit lot number')

    
    # Attribute Barcode uses Python identifier Barcode
    __Barcode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Barcode'), 'Barcode', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_PartNumberType_Barcode', pyxb.binding.datatypes.string)
    __Barcode._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 365, 4)
    __Barcode._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 365, 4)
    
    Barcode = property(__Barcode.value, __Barcode.set, None, 'The kit barcode; used for tracking purposes.')

    
    # Attribute ExpirationDate uses Python identifier ExpirationDate
    __ExpirationDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ExpirationDate'), 'ExpirationDate', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_PartNumberType_ExpirationDate', pyxb.binding.datatypes.date)
    __ExpirationDate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 370, 4)
    __ExpirationDate._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 370, 4)
    
    ExpirationDate = property(__ExpirationDate.value, __ExpirationDate.set, None, "The kit's shelf life")

    
    # Attribute IsObsolete uses Python identifier IsObsolete
    __IsObsolete = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IsObsolete'), 'IsObsolete', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_PartNumberType_IsObsolete', pyxb.binding.datatypes.boolean, unicode_default='false')
    __IsObsolete._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 375, 4)
    __IsObsolete._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 375, 4)
    
    IsObsolete = property(__IsObsolete.value, __IsObsolete.set, None, None)

    
    # Attribute IsRestricted uses Python identifier IsRestricted
    __IsRestricted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IsRestricted'), 'IsRestricted', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_PartNumberType_IsRestricted', pyxb.binding.datatypes.boolean, unicode_default='false')
    __IsRestricted._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 376, 4)
    __IsRestricted._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 376, 4)
    
    IsRestricted = property(__IsRestricted.value, __IsRestricted.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __PartNumber.name() : __PartNumber,
        __LotNumber.name() : __LotNumber,
        __Barcode.name() : __Barcode,
        __ExpirationDate.name() : __ExpirationDate,
        __IsObsolete.name() : __IsObsolete,
        __IsRestricted.name() : __IsRestricted
    })
Namespace.addCategoryObject('typeBinding', 'PartNumberType', PartNumberType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}RecordedEventType with content type ELEMENT_ONLY
class RecordedEventType (DataEntityType):
    """Metrics, system events, alarms, and logs may utilize this type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecordedEventType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 380, 1)
    _ElementMap = DataEntityType._ElementMap.copy()
    _AttributeMap = DataEntityType._AttributeMap.copy()
    # Base type is DataEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute Context uses Python identifier Context
    __Context = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Context'), 'Context', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_RecordedEventType_Context', pyxb.binding.datatypes.string)
    __Context._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 386, 4)
    __Context._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 386, 4)
    
    Context = property(__Context.value, __Context.set, None, 'The part of the system in effect when the event was recorded')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Context.name() : __Context
    })
Namespace.addCategoryObject('typeBinding', 'RecordedEventType', RecordedEventType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SequencingChemistry with content type ELEMENT_ONLY
class SequencingChemistry (DataEntityType):
    """A container for a set of analogs"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequencingChemistry')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 394, 1)
    _ElementMap = DataEntityType._ElementMap.copy()
    _AttributeMap = DataEntityType._AttributeMap.copy()
    # Base type is DataEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DyeSet uses Python identifier DyeSet
    __DyeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DyeSet'), 'DyeSet', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SequencingChemistry_httppacificbiosciences_comPacBioBaseDataModel_xsdDyeSet', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 401, 5), )

    
    DyeSet = property(__DyeSet.value, __DyeSet.set, None, None)

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    _ElementMap.update({
        __DyeSet.name() : __DyeSet
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SequencingChemistry', SequencingChemistry)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SequencingChemistryConfig with content type ELEMENT_ONLY
class SequencingChemistryConfig (DataEntityType):
    """A container for a set of analogs"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequencingChemistryConfig')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 432, 1)
    _ElementMap = DataEntityType._ElementMap.copy()
    _AttributeMap = DataEntityType._AttributeMap.copy()
    # Base type is DataEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Analogs uses Python identifier Analogs
    __Analogs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Analogs'), 'Analogs', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SequencingChemistryConfig_httppacificbiosciences_comPacBioBaseDataModel_xsdAnalogs', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 439, 5), )

    
    Analogs = property(__Analogs.value, __Analogs.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DefaultLaserSetPoint uses Python identifier DefaultLaserSetPoint
    __DefaultLaserSetPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DefaultLaserSetPoint'), 'DefaultLaserSetPoint', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SequencingChemistryConfig_httppacificbiosciences_comPacBioBaseDataModel_xsdDefaultLaserSetPoint', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 446, 5), )

    
    DefaultLaserSetPoint = property(__DefaultLaserSetPoint.value, __DefaultLaserSetPoint.set, None, "The laser power at the input couple, needed to achieve predefined performance requirements based on a median 'golden' SMRT Cell.")

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}TargetSNR uses Python identifier TargetSNR
    __TargetSNR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TargetSNR'), 'TargetSNR', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SequencingChemistryConfig_httppacificbiosciences_comPacBioBaseDataModel_xsdTargetSNR', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 451, 5), )

    
    TargetSNR = property(__TargetSNR.value, __TargetSNR.set, None, None)

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    _ElementMap.update({
        __Analogs.name() : __Analogs,
        __DefaultLaserSetPoint.name() : __DefaultLaserSetPoint,
        __TargetSNR.name() : __TargetSNR
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SequencingChemistryConfig', SequencingChemistryConfig)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}IndexedDataType with content type ELEMENT_ONLY
class IndexedDataType (InputOutputDataType):
    """Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}IndexedDataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IndexedDataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 271, 1)
    _ElementMap = InputOutputDataType._ElementMap.copy()
    _AttributeMap = InputOutputDataType._AttributeMap.copy()
    # Base type is InputOutputDataType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources uses Python identifier ExternalResources
    __ExternalResources = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources'), 'ExternalResources', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_IndexedDataType_httppacificbiosciences_comPacBioBaseDataModel_xsdExternalResources', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 256, 1), )

    
    ExternalResources = property(__ExternalResources.value, __ExternalResources.set, None, 'Pointers to data that do not reside inside the parent structure')

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}FileIndices uses Python identifier FileIndices
    __FileIndices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FileIndices'), 'FileIndices', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_IndexedDataType_httppacificbiosciences_comPacBioBaseDataModel_xsdFileIndices', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 275, 5), )

    
    FileIndices = property(__FileIndices.value, __FileIndices.set, None, None)

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StrictEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StrictEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StrictEntityType
    _ElementMap.update({
        __ExternalResources.name() : __ExternalResources,
        __FileIndices.name() : __FileIndices
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'IndexedDataType', IndexedDataType)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SupplyKitBinding with content type ELEMENT_ONLY
class SupplyKitBinding (PartNumberType):
    """A more specific binding kit representation (includes SupplyKit fields). """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplyKitBinding')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 543, 1)
    _ElementMap = PartNumberType._ElementMap.copy()
    _AttributeMap = PartNumberType._AttributeMap.copy()
    # Base type is PartNumberType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Control uses Python identifier Control
    __Control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Control'), 'Control', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SupplyKitBinding_httppacificbiosciences_comPacBioBaseDataModel_xsdControl', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 550, 5), )

    
    Control = property(__Control.value, __Control.set, None, 'Defines the binding kit internal control name.  Present when used, otherwise not used if not defined. ')

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}IsControlUsed uses Python identifier IsControlUsed
    __IsControlUsed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IsControlUsed'), 'IsControlUsed', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SupplyKitBinding_httppacificbiosciences_comPacBioBaseDataModel_xsdIsControlUsed', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 555, 5), )

    
    IsControlUsed = property(__IsControlUsed.value, __IsControlUsed.set, None, 'True if the control was used during run, otherwise false. ')

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute PartNumber inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute LotNumber inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute Barcode inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute ExpirationDate inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute IsObsolete inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute IsRestricted inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    _ElementMap.update({
        __Control.name() : __Control,
        __IsControlUsed.name() : __IsControlUsed
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SupplyKitBinding', SupplyKitBinding)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SupplyKitCellPack with content type ELEMENT_ONLY
class SupplyKitCellPack (PartNumberType):
    """Represents the package of cells. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplyKitCellPack')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 564, 1)
    _ElementMap = PartNumberType._ElementMap.copy()
    _AttributeMap = PartNumberType._AttributeMap.copy()
    # Base type is PartNumberType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ChipLayout uses Python identifier ChipLayout
    __ChipLayout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout'), 'ChipLayout', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SupplyKitCellPack_httppacificbiosciences_comPacBioBaseDataModel_xsdChipLayout', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 571, 5), )

    
    ChipLayout = property(__ChipLayout.value, __ChipLayout.set, None, 'Defines the internal chip layout name, if any. ')

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute PartNumber inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute LotNumber inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute Barcode inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute ExpirationDate inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute IsObsolete inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute IsRestricted inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute SupportsCellReuse uses Python identifier SupportsCellReuse
    __SupportsCellReuse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SupportsCellReuse'), 'SupportsCellReuse', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SupplyKitCellPack_SupportsCellReuse', pyxb.binding.datatypes.anySimpleType)
    __SupportsCellReuse._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 577, 4)
    __SupportsCellReuse._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 577, 4)
    
    SupportsCellReuse = property(__SupportsCellReuse.value, __SupportsCellReuse.set, None, 'If SupportsCellReuse is true, it can be used for regular sequencing as well as in a reuse scenario.')

    _ElementMap.update({
        __ChipLayout.name() : __ChipLayout
    })
    _AttributeMap.update({
        __SupportsCellReuse.name() : __SupportsCellReuse
    })
Namespace.addCategoryObject('typeBinding', 'SupplyKitCellPack', SupplyKitCellPack)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SupplyKitControl with content type ELEMENT_ONLY
class SupplyKitControl (PartNumberType):
    """Represents the DNA control complex. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplyKitControl')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 585, 1)
    _ElementMap = PartNumberType._ElementMap.copy()
    _AttributeMap = PartNumberType._AttributeMap.copy()
    # Base type is PartNumberType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}InternalControlName uses Python identifier InternalControlName
    __InternalControlName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InternalControlName'), 'InternalControlName', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SupplyKitControl_httppacificbiosciences_comPacBioBaseDataModel_xsdInternalControlName', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 592, 5), )

    
    InternalControlName = property(__InternalControlName.value, __InternalControlName.set, None, 'Defines the internal control name, if any. ')

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute PartNumber inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute LotNumber inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute Barcode inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute ExpirationDate inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute IsObsolete inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute IsRestricted inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    _ElementMap.update({
        __InternalControlName.name() : __InternalControlName
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SupplyKitControl', SupplyKitControl)


# Complex type {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}SupplyKitTemplate with content type ELEMENT_ONLY
class SupplyKitTemplate (PartNumberType):
    """A more specific template kit representation (includes SupplyKit fields). """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplyKitTemplate')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 601, 1)
    _ElementMap = PartNumberType._ElementMap.copy()
    _AttributeMap = PartNumberType._AttributeMap.copy()
    # Base type is PartNumberType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}LeftAdaptorSequence uses Python identifier LeftAdaptorSequence
    __LeftAdaptorSequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LeftAdaptorSequence'), 'LeftAdaptorSequence', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SupplyKitTemplate_httppacificbiosciences_comPacBioBaseDataModel_xsdLeftAdaptorSequence', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 608, 5), )

    
    LeftAdaptorSequence = property(__LeftAdaptorSequence.value, __LeftAdaptorSequence.set, None, 'Left adapter DNA sequence.')

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}LeftPrimerSequence uses Python identifier LeftPrimerSequence
    __LeftPrimerSequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LeftPrimerSequence'), 'LeftPrimerSequence', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SupplyKitTemplate_httppacificbiosciences_comPacBioBaseDataModel_xsdLeftPrimerSequence', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 613, 5), )

    
    LeftPrimerSequence = property(__LeftPrimerSequence.value, __LeftPrimerSequence.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}RightAdaptorSequence uses Python identifier RightAdaptorSequence
    __RightAdaptorSequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RightAdaptorSequence'), 'RightAdaptorSequence', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SupplyKitTemplate_httppacificbiosciences_comPacBioBaseDataModel_xsdRightAdaptorSequence', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 614, 5), )

    
    RightAdaptorSequence = property(__RightAdaptorSequence.value, __RightAdaptorSequence.set, None, 'Right adapter DNA sequence.  If not specified, a symmetric adapter model is inferred, where the left adapter sequence is used wherever needed.')

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}RightPrimerSequence uses Python identifier RightPrimerSequence
    __RightPrimerSequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RightPrimerSequence'), 'RightPrimerSequence', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SupplyKitTemplate_httppacificbiosciences_comPacBioBaseDataModel_xsdRightPrimerSequence', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 619, 5), )

    
    RightPrimerSequence = property(__RightPrimerSequence.value, __RightPrimerSequence.set, None, 'Right primaer sequence.  If not specified, a symmetric model is inferred, where the left primer sequence is used wherever needed.')

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Attribute PartNumber inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute LotNumber inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute Barcode inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute ExpirationDate inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute IsObsolete inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute IsRestricted inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
    # Attribute MinInsertSize uses Python identifier MinInsertSize
    __MinInsertSize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MinInsertSize'), 'MinInsertSize', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SupplyKitTemplate_MinInsertSize', pyxb.binding.datatypes.int)
    __MinInsertSize._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 625, 4)
    __MinInsertSize._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 625, 4)
    
    MinInsertSize = property(__MinInsertSize.value, __MinInsertSize.set, None, 'Minimum recommended insert size')

    
    # Attribute MaxInsertSize uses Python identifier MaxInsertSize
    __MaxInsertSize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MaxInsertSize'), 'MaxInsertSize', '__httppacificbiosciences_comPacBioBaseDataModel_xsd_SupplyKitTemplate_MaxInsertSize', pyxb.binding.datatypes.int)
    __MaxInsertSize._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 630, 4)
    __MaxInsertSize._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 630, 4)
    
    MaxInsertSize = property(__MaxInsertSize.value, __MaxInsertSize.set, None, 'Maximum recommended insert size')

    _ElementMap.update({
        __LeftAdaptorSequence.name() : __LeftAdaptorSequence,
        __LeftPrimerSequence.name() : __LeftPrimerSequence,
        __RightAdaptorSequence.name() : __RightAdaptorSequence,
        __RightPrimerSequence.name() : __RightPrimerSequence
    })
    _AttributeMap.update({
        __MinInsertSize.name() : __MinInsertSize,
        __MaxInsertSize.name() : __MaxInsertSize
    })
Namespace.addCategoryObject('typeBinding', 'SupplyKitTemplate', SupplyKitTemplate)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (IndexedDataType):
    """for example, an output file could be the BAM file, which could be associated with multiple indices into it."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 762, 2)
    _ElementMap = IndexedDataType._ElementMap.copy()
    _AttributeMap = IndexedDataType._AttributeMap.copy()
    # Base type is IndexedDataType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}IndexedDataType
    
    # Element FileIndices ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}FileIndices) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}IndexedDataType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StrictEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StrictEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}StrictEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



ExtensionElement = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionElement'), pyxb.binding.datatypes.anyType, documentation='A generic element whose contents are undefined at the schema level.  This is used to extend the data model.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 736, 1))
Namespace.addCategoryObject('elementBinding', ExtensionElement.name().localName(), ExtensionElement)

DataPointers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataPointers'), CTD_ANON_3, documentation='Pointer list to UniqueIds in the system', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 222, 1))
Namespace.addCategoryObject('elementBinding', DataPointers.name().localName(), DataPointers)

ExternalResources = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources'), CTD_ANON_4, documentation='Pointers to data that do not reside inside the parent structure', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 256, 1))
Namespace.addCategoryObject('elementBinding', ExternalResources.name().localName(), ExternalResources)

PacBioSequencingChemistry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PacBioSequencingChemistry'), CTD_ANON_8, documentation='Root element for document containing the container of analog set, SequencingChemistryConfig', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 422, 1))
Namespace.addCategoryObject('elementBinding', PacBioSequencingChemistry.name().localName(), PacBioSequencingChemistry)

ValueDataType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValueDataType'), SupportedDataTypes, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 734, 1))
Namespace.addCategoryObject('elementBinding', ValueDataType.name().localName(), ValueDataType)

KeyValueMap = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KeyValueMap'), CTD_ANON_17, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 768, 1))
Namespace.addCategoryObject('elementBinding', KeyValueMap.name().localName(), KeyValueMap)

DataEntity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataEntity'), DataEntityType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 180, 1))
Namespace.addCategoryObject('elementBinding', DataEntity.name().localName(), DataEntity)

AutomationParameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter'), DataEntityType, documentation='One or more collection parameters, such as MovieLength, InsertSize, UseStageStart, IsControl, etc..', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 321, 1))
Namespace.addCategoryObject('elementBinding', AutomationParameter.name().localName(), AutomationParameter)

ConfigSetAnalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConfigSetAnalog'), CTD_ANON_20, documentation='An unlimited number of analogs listed for the purposes of hosting in a configuration file. e.g. a list of all possible analogs on the system', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 170, 1))
Namespace.addCategoryObject('elementBinding', ConfigSetAnalog.name().localName(), ConfigSetAnalog)

DyeSetAnalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DyeSetAnalog'), CTD_ANON_21, documentation='A set of four analogs, one for each of the nucleotides, grouped together for the purposes of a single experiment.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 246, 1))
Namespace.addCategoryObject('elementBinding', DyeSetAnalog.name().localName(), DyeSetAnalog)

ChemistryConfig = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChemistryConfig'), SequencingChemistryConfig, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 797, 1))
Namespace.addCategoryObject('elementBinding', ChemistryConfig.name().localName(), ChemistryConfig)

ExternalResource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalResource'), CTD_ANON_22, documentation='for example, an output file could be the BAM file, which could be associated with multiple indices into it.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 758, 1))
Namespace.addCategoryObject('elementBinding', ExternalResource.name().localName(), ExternalResource)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Values'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 16, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Values')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 16, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), pyxb.binding.datatypes.float, scope=CTD_ANON_, documentation='There should be as many values as specified in the Number of Filter Bins attribute.\nEach value is a probability, in the range of [0, 1].', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 19, 11)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 19, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionElement'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_2, documentation='A generic element whose contents are undefined at the schema level.  This is used to extend the data model.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 736, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 89, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExtensionElement')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 89, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataPointer'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 228, 4)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 228, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataPointer')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 228, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalResource'), CTD_ANON_22, scope=CTD_ANON_4, documentation='for example, an output file could be the BAM file, which could be associated with multiple indices into it.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 758, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResource')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 262, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FileIndex'), InputOutputDataType, scope=CTD_ANON_5, documentation='e.g. index for output files, allowing one to find information in the output file', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 278, 8)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FileIndex')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 278, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter'), DataEntityType, scope=CTD_ANON_6, documentation='One or more collection parameters, such as MovieLength, InsertSize, UseStageStart, IsControl, etc..', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 321, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 298, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Analog'), AnalogType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 409, 13)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=4, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 409, 13))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Analog')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 409, 13))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChemistryConfig'), SequencingChemistryConfig, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 797, 1)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChemistryConfig')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 428, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Analog'), AnalogType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 442, 8)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=4, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 442, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Analog')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 442, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinCount'), pyxb.binding.datatypes.int, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 479, 8)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinCount')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 479, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_10()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinCount'), pyxb.binding.datatypes.int, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 505, 8)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinCount')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 505, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_11()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinLabel'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 513, 8)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinLabel')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 513, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_12()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Val'), pyxb.binding.datatypes.float, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 535, 8)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 535, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Val')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 535, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_13()




UserDefinedFieldsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataEntities'), DataEntityType, scope=UserDefinedFieldsType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 731, 3)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UserDefinedFieldsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataEntities')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 731, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UserDefinedFieldsType._Automaton = _BuildAutomaton_14()




FilterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Properties'), CTD_ANON_15, scope=FilterType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 743, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Properties')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 743, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FilterType._Automaton = _BuildAutomaton_15()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Property'), CTD_ANON_16, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 746, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Property')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 746, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_16()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Items'), CTD_ANON_18, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 771, 4)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Items')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 771, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_17()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Item'), MapItemType, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 774, 7)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 774, 7))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Item')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 774, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_18()




MapType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KeyValueMap'), CTD_ANON_17, scope=MapType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 768, 1)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KeyValueMap')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 787, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MapType._Automaton = _BuildAutomaton_19()




MapItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Key'), pyxb.binding.datatypes.ID, scope=MapItemType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 792, 3)))

MapItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), pyxb.binding.datatypes.anyType, scope=MapItemType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 793, 3)))

MapItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Description'), pyxb.binding.datatypes.string, scope=MapItemType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 794, 3)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Key')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 792, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MapItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 793, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MapItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 794, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MapItemType._Automaton = _BuildAutomaton_20()




BaseEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), CTD_ANON_2, scope=BaseEntityType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BaseEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BaseEntityType._Automaton = _BuildAutomaton_21()




AnalogType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Spectrum'), CTD_ANON, scope=AnalogType, documentation='A vector of probabilities, given in the order of increasing filter-bin wavelength, that light emitted by the analog will fall in the corresponding filter bin of the instrument detection system. By convention, the values are normalized to sum to 1.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 10, 5)))

AnalogType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RelativeAmplitude'), pyxb.binding.datatypes.float, scope=AnalogType, documentation='Relative intensity of emission vs. a reference analog using standardized metrology \u2013 e.g., relative to the amplitude of the \u201c542\u201d analog as measured by the mean DWS pkMid on the Astro instrument.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 36, 5)))

AnalogType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IntraPulseXsnCV'), pyxb.binding.datatypes.float, scope=AnalogType, documentation='The 1-sigma fractional variation of the intra-pulse signal, independent of any Shot noise associated with that signal', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 41, 5)))

AnalogType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterPulseXsnCV'), pyxb.binding.datatypes.float, scope=AnalogType, documentation='The 1-sigma fractional variation, pulse-to-pulse, of the mean signal level (i.e., the pkMid).', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 46, 5)))

AnalogType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DiffusionXsnCV'), pyxb.binding.datatypes.float, scope=AnalogType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 51, 5)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalogType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalogType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Spectrum')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 10, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalogType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RelativeAmplitude')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 36, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalogType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IntraPulseXsnCV')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 41, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnalogType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterPulseXsnCV')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 46, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AnalogType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DiffusionXsnCV')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 51, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AnalogType._Automaton = _BuildAutomaton_22()




def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StrictEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StrictEntityType._Automaton = _BuildAutomaton_23()




DataEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue'), pyxb.binding.datatypes.base64Binary, scope=DataEntityType, documentation='A complex data type element, such as an image, file, binary object, etc.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5)))

DataEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CheckSum'), pyxb.binding.datatypes.string, scope=DataEntityType, documentation='small-size datum of the attached value for the purpose of detecting errors or modification which may have been introduced during its transmission or storage', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DataEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DataEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DataEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DataEntityType._Automaton = _BuildAutomaton_24()




def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DNABarcode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DNABarcode._Automaton = _BuildAutomaton_25()




AutomationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameters'), CTD_ANON_6, scope=AutomationType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 295, 5)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 295, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AutomationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AutomationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 295, 5))
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
AutomationType._Automaton = _BuildAutomaton_26()




def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IncompatiblePairType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IncompatiblePairType._Automaton = _BuildAutomaton_27()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Analogs'), CTD_ANON_7, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 406, 10)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Analogs')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 406, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_28()




StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleSize'), pyxb.binding.datatypes.int, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 470, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleMean'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 471, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleMed'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 472, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleStd'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 473, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Sample95thPct'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 474, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumBins'), pyxb.binding.datatypes.int, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 475, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinCounts'), CTD_ANON_11, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 476, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinWidth'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 483, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MinOutlierValue'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 484, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MinBinValue'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 485, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaxBinValue'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 486, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaxOutlierValue'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 487, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MetricDescription'), pyxb.binding.datatypes.string, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 488, 5)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SampleSize')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 470, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SampleMean')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 471, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SampleMed')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 472, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SampleStd')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 473, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sample95thPct')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 474, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumBins')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 475, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinCounts')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 476, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinWidth')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 483, 5))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MinOutlierValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 484, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MinBinValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 485, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MaxBinValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 486, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MaxOutlierValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 487, 5))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MetricDescription')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 488, 5))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StatsContinuousDistType._Automaton = _BuildAutomaton_29()




StatsDiscreteDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumBins'), pyxb.binding.datatypes.int, scope=StatsDiscreteDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 501, 5)))

StatsDiscreteDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinCounts'), CTD_ANON_12, scope=StatsDiscreteDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 502, 5)))

StatsDiscreteDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MetricDescription'), pyxb.binding.datatypes.string, scope=StatsDiscreteDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 509, 5)))

StatsDiscreteDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinLabels'), CTD_ANON_13, scope=StatsDiscreteDistType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 510, 5)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsDiscreteDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsDiscreteDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumBins')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 501, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsDiscreteDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinCounts')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 502, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsDiscreteDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MetricDescription')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 509, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatsDiscreteDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinLabels')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 510, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StatsDiscreteDistType._Automaton = _BuildAutomaton_30()




StatsTimeSeriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeUnits'), pyxb.binding.datatypes.string, scope=StatsTimeSeriesType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 528, 5)))

StatsTimeSeriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValueUnits'), pyxb.binding.datatypes.string, scope=StatsTimeSeriesType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 529, 5)))

StatsTimeSeriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), pyxb.binding.datatypes.float, scope=StatsTimeSeriesType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 530, 5)))

StatsTimeSeriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeasInterval'), pyxb.binding.datatypes.float, scope=StatsTimeSeriesType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 531, 5)))

StatsTimeSeriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Values'), CTD_ANON_14, scope=StatsTimeSeriesType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 532, 5)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 532, 5))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsTimeSeriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsTimeSeriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeUnits')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 528, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsTimeSeriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueUnits')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 529, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsTimeSeriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartTime')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 530, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatsTimeSeriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MeasInterval')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 531, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StatsTimeSeriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Values')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 532, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StatsTimeSeriesType._Automaton = _BuildAutomaton_31()




def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Spectrum')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 10, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RelativeAmplitude')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 36, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IntraPulseXsnCV')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 41, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterPulseXsnCV')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 46, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DiffusionXsnCV')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 51, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_32()




def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Spectrum')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 10, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RelativeAmplitude')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 36, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IntraPulseXsnCV')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 41, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterPulseXsnCV')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 46, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DiffusionXsnCV')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 51, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_33()




def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InputOutputDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InputOutputDataType._Automaton = _BuildAutomaton_34()




def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PartNumberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PartNumberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PartNumberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PartNumberType._Automaton = _BuildAutomaton_35()




def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RecordedEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RecordedEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RecordedEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RecordedEventType._Automaton = _BuildAutomaton_36()




SequencingChemistry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DyeSet'), CTD_ANON_19, scope=SequencingChemistry, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 401, 5)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequencingChemistry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequencingChemistry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequencingChemistry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SequencingChemistry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DyeSet')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 401, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SequencingChemistry._Automaton = _BuildAutomaton_37()




SequencingChemistryConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Analogs'), CTD_ANON_9, scope=SequencingChemistryConfig, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 439, 5)))

SequencingChemistryConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DefaultLaserSetPoint'), pyxb.binding.datatypes.float, scope=SequencingChemistryConfig, documentation="The laser power at the input couple, needed to achieve predefined performance requirements based on a median 'golden' SMRT Cell.", location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 446, 5)))

SequencingChemistryConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TargetSNR'), CTD_ANON_10, scope=SequencingChemistryConfig, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 451, 5)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequencingChemistryConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequencingChemistryConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequencingChemistryConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequencingChemistryConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Analogs')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 439, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequencingChemistryConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DefaultLaserSetPoint')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 446, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SequencingChemistryConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TargetSNR')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 451, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SequencingChemistryConfig._Automaton = _BuildAutomaton_38()




IndexedDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources'), CTD_ANON_4, scope=IndexedDataType, documentation='Pointers to data that do not reside inside the parent structure', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 256, 1)))

IndexedDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FileIndices'), CTD_ANON_5, scope=IndexedDataType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 275, 5)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 275, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 286, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IndexedDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IndexedDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FileIndices')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 275, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(IndexedDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 286, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IndexedDataType._Automaton = _BuildAutomaton_39()




SupplyKitBinding._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Control'), SupplyKitControl, scope=SupplyKitBinding, documentation='Defines the binding kit internal control name.  Present when used, otherwise not used if not defined. ', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 550, 5)))

SupplyKitBinding._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IsControlUsed'), pyxb.binding.datatypes.boolean, scope=SupplyKitBinding, documentation='True if the control was used during run, otherwise false. ', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 555, 5)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 550, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 555, 5))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitBinding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitBinding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitBinding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitBinding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Control')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 550, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitBinding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IsControlUsed')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 555, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SupplyKitBinding._Automaton = _BuildAutomaton_40()




SupplyKitCellPack._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout'), pyxb.binding.datatypes.string, scope=SupplyKitCellPack, documentation='Defines the internal chip layout name, if any. ', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 571, 5)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 571, 5))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitCellPack._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitCellPack._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitCellPack._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitCellPack._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 571, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SupplyKitCellPack._Automaton = _BuildAutomaton_41()




SupplyKitControl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InternalControlName'), pyxb.binding.datatypes.string, scope=SupplyKitControl, documentation='Defines the internal control name, if any. ', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 592, 5)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 592, 5))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InternalControlName')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 592, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SupplyKitControl._Automaton = _BuildAutomaton_42()




SupplyKitTemplate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LeftAdaptorSequence'), pyxb.binding.datatypes.string, scope=SupplyKitTemplate, documentation='Left adapter DNA sequence.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 608, 5)))

SupplyKitTemplate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LeftPrimerSequence'), pyxb.binding.datatypes.string, scope=SupplyKitTemplate, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 613, 5)))

SupplyKitTemplate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RightAdaptorSequence'), pyxb.binding.datatypes.string, scope=SupplyKitTemplate, documentation='Right adapter DNA sequence.  If not specified, a symmetric adapter model is inferred, where the left adapter sequence is used wherever needed.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 614, 5)))

SupplyKitTemplate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RightPrimerSequence'), pyxb.binding.datatypes.string, scope=SupplyKitTemplate, documentation='Right primaer sequence.  If not specified, a symmetric model is inferred, where the left primer sequence is used wherever needed.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 619, 5)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 608, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 613, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 614, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 619, 5))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LeftAdaptorSequence')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 608, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LeftPrimerSequence')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 613, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RightAdaptorSequence')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 614, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RightPrimerSequence')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 619, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SupplyKitTemplate._Automaton = _BuildAutomaton_43()




def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 275, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 286, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FileIndices')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 275, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 286, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_44()

