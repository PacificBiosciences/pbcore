# pbcore/io/dataset/pyxb/DataSetXsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:3c1eccef1b156ac43379b476cb78e3eecd9f5c97
# Generated 2017-12-05 18:43:16.353544 by PyXB version 1.2.4 using Python 2.7.9.final.0
# Namespace http://pacificbiosciences.com/PacBioDataModel.xsd

from __future__ import unicode_literals
from __future__ import absolute_import
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:35b41036-da2f-11e7-80cf-0026b9fe0a90')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
from . import _pbbase as _ImportedBinding__pbbase
from . import _pbds as _ImportedBinding__pbds
from . import _pbsample as _ImportedBinding__pbsample
from . import _pbpn as _ImportedBinding__pbpn
import pyxb.binding.datatypes
from . import _pbrk as _ImportedBinding__pbrk

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://pacificbiosciences.com/PacBioDataModel.xsd', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_pbpn = _ImportedBinding__pbpn.Namespace
_Namespace_pbpn.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_pbds = _ImportedBinding__pbds.Namespace
_Namespace_pbds.configureCategories(['typeBinding', 'elementBinding'])
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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 75, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.AverageReadLength = STD_ANON._CF_enumeration.addEnumeration(unicode_value='AverageReadLength', tag='AverageReadLength')
STD_ANON.AcquisitionTime = STD_ANON._CF_enumeration.addEnumeration(unicode_value='AcquisitionTime', tag='AcquisitionTime')
STD_ANON.InsertSize = STD_ANON._CF_enumeration.addEnumeration(unicode_value='InsertSize', tag='InsertSize')
STD_ANON.ReuseComplex = STD_ANON._CF_enumeration.addEnumeration(unicode_value='ReuseComplex', tag='ReuseComplex')
STD_ANON.StageHS = STD_ANON._CF_enumeration.addEnumeration(unicode_value='StageHS', tag='StageHS')
STD_ANON.JobId = STD_ANON._CF_enumeration.addEnumeration(unicode_value='JobId', tag='JobId')
STD_ANON.JobName = STD_ANON._CF_enumeration.addEnumeration(unicode_value='JobName', tag='JobName')
STD_ANON.NumberOfCollections = STD_ANON._CF_enumeration.addEnumeration(unicode_value='NumberOfCollections', tag='NumberOfCollections')
STD_ANON.StrobeByTime = STD_ANON._CF_enumeration.addEnumeration(unicode_value='StrobeByTime', tag='StrobeByTime')
STD_ANON.UsedControl = STD_ANON._CF_enumeration.addEnumeration(unicode_value='UsedControl', tag='UsedControl')
STD_ANON.Use2ndLook = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Use2ndLook', tag='Use2ndLook')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 190, 4)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.PlateId = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='PlateId', tag='PlateId')
STD_ANON_.PlateDefinition = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='PlateDefinition', tag='PlateDefinition')
STD_ANON_.SchemaVersion = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='SchemaVersion', tag='SchemaVersion')
STD_ANON_.DefType = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='DefType', tag='DefType')
STD_ANON_.Owner = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Owner', tag='Owner')
STD_ANON_.CreatedBy = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='CreatedBy', tag='CreatedBy')
STD_ANON_.Comments = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Comments', tag='Comments')
STD_ANON_.OutputPath = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='OutputPath', tag='OutputPath')
STD_ANON_.Collections = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Collections', tag='Collections')
STD_ANON_.Collection = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Collection', tag='Collection')
STD_ANON_.DNATemplatePrepKitDefinition = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='DNATemplatePrepKitDefinition', tag='DNATemplatePrepKitDefinition')
STD_ANON_.BindingKitDefinition = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='BindingKitDefinition', tag='BindingKitDefinition')
STD_ANON_.RunResources = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='RunResources', tag='RunResources')
STD_ANON_.CompatibleChipLayouts = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='CompatibleChipLayouts', tag='CompatibleChipLayouts')
STD_ANON_.ChipLayout = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='ChipLayout', tag='ChipLayout')
STD_ANON_.CompatibleSequencingKits = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='CompatibleSequencingKits', tag='CompatibleSequencingKits')
STD_ANON_.SequencingKit = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='SequencingKit', tag='SequencingKit')
STD_ANON_.RequiredTips = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='RequiredTips', tag='RequiredTips')
STD_ANON_.EstimatedTotalRunTime = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='EstimatedTotalRunTime', tag='EstimatedTotalRunTime')
STD_ANON_.RequiredSMRTCells = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='RequiredSMRTCells', tag='RequiredSMRTCells')
STD_ANON_.CollectionAutomation = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='CollectionAutomation', tag='CollectionAutomation')
STD_ANON_.Basecaller = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Basecaller', tag='Basecaller')
STD_ANON_.SecondaryAnalysisAutomation = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='SecondaryAnalysisAutomation', tag='SecondaryAnalysisAutomation')
STD_ANON_.WellNo = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='WellNo', tag='WellNo')
STD_ANON_.SampleName = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='SampleName', tag='SampleName')
STD_ANON_.Barcode = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Barcode', tag='Barcode')
STD_ANON_.AcquisitionTime = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='AcquisitionTime', tag='AcquisitionTime')
STD_ANON_.InsertSize = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='InsertSize', tag='InsertSize')
STD_ANON_.ReuseComplex = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='ReuseComplex', tag='ReuseComplex')
STD_ANON_.StageHS = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='StageHS', tag='StageHS')
STD_ANON_.NumberOfCollections = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='NumberOfCollections', tag='NumberOfCollections')
STD_ANON_.Confidence = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Confidence', tag='Confidence')
STD_ANON_.SampleComment = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='SampleComment', tag='SampleComment')
STD_ANON_.StrobeByTime = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='StrobeByTime', tag='StrobeByTime')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 408, 5)
    _Documentation = None
STD_ANON_2._InitializeFacetMap()

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 416, 5)
    _Documentation = None
STD_ANON_3._InitializeFacetMap()

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Part of the RunResources; specifies a ChipLayout which is compatible with the collection protocols defined on the plate"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 15, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_Name', pyxb.binding.datatypes.string, required=True)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 19, 3)
    __Name._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 19, 3)
    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Attribute PartNumber uses Python identifier PartNumber
    __PartNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PartNumber'), 'PartNumber', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_PartNumber', pyxb.binding.datatypes.string, required=True)
    __PartNumber._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 20, 3)
    __PartNumber._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 20, 3)
    
    PartNumber = property(__PartNumber.value, __PartNumber.set, None, None)

    
    # Attribute Quantity uses Python identifier Quantity
    __Quantity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Quantity'), 'Quantity', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_Quantity', pyxb.binding.datatypes.anySimpleType)
    __Quantity._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 21, 3)
    __Quantity._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 21, 3)
    
    Quantity = property(__Quantity.value, __Quantity.set, None, 'The number of cells required, of a particular part number')

    _ElementMap.update({
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        __Name.name() : __Name,
        __PartNumber.name() : __PartNumber,
        __Quantity.name() : __Quantity
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """A set of Chip Layouts deemed compatible with the current plate"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 32, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ChipLayout uses Python identifier ChipLayout
    __ChipLayout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout'), 'ChipLayout', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON__httppacificbiosciences_comPacBioDataModel_xsdChipLayout', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 11, 1), )

    
    ChipLayout = property(__ChipLayout.value, __ChipLayout.set, None, 'Part of the RunResources; specifies a ChipLayout which is compatible with the collection protocols defined on the plate')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON__httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    _ElementMap.update({
        __ChipLayout.name() : __ChipLayout,
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """A set of reagent kits deemed compatible with the current plate"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 43, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}EstimatedTotalRunTime uses Python identifier EstimatedTotalRunTime
    __EstimatedTotalRunTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EstimatedTotalRunTime'), 'EstimatedTotalRunTime', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_2_httppacificbiosciences_comPacBioDataModel_xsdEstimatedTotalRunTime', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 51, 1), )

    
    EstimatedTotalRunTime = property(__EstimatedTotalRunTime.value, __EstimatedTotalRunTime.set, None, 'The total amount of time the run is estimated to require.  A confidence value (defaulted to 90%) indicates the degree of certainty associated with the estimate')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RequiredTips uses Python identifier RequiredTips
    __RequiredTips = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RequiredTips'), 'RequiredTips', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_2_httppacificbiosciences_comPacBioDataModel_xsdRequiredTips', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 125, 1), )

    
    RequiredTips = property(__RequiredTips.value, __RequiredTips.set, None, 'Part of the RunResources; specifies the required number of tips via two attributes, Left and Right')

    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}SequencingKit uses Python identifier SequencingKit
    __SequencingKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_pbpn, 'SequencingKit'), 'SequencingKit', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_2_httppacificbiosciences_comPacBioPartNumbers_xsdSequencingKit', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 14, 1), )

    
    SequencingKit = property(__SequencingKit.value, __SequencingKit.set, None, None)

    _ElementMap.update({
        __EstimatedTotalRunTime.name() : __EstimatedTotalRunTime,
        __RequiredTips.name() : __RequiredTips,
        __SequencingKit.name() : __SequencingKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """The total amount of time the run is estimated to require.  A confidence value (defaulted to 90%) indicates the degree of certainty associated with the estimate"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 55, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_3_Value', pyxb.binding.datatypes.string, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 59, 3)
    __Value._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 59, 3)
    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Attribute Confidence uses Python identifier Confidence
    __Confidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Confidence'), 'Confidence', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_3_Confidence', pyxb.binding.datatypes.int, required=True)
    __Confidence._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 60, 3)
    __Confidence._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 60, 3)
    
    Confidence = property(__Confidence.value, __Confidence.set, None, None)

    _ElementMap.update({
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        __Value.name() : __Value,
        __Confidence.name() : __Confidence
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """PacBio Data Model root element"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 98, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ExperimentContainer uses Python identifier ExperimentContainer
    __ExperimentContainer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExperimentContainer'), 'ExperimentContainer', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_4_httppacificbiosciences_comPacBioDataModel_xsdExperimentContainer', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 100, 4), )

    
    ExperimentContainer = property(__ExperimentContainer.value, __ExperimentContainer.set, None, None)

    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Version'), 'Version', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_4_Version', pyxb.binding.datatypes.string)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 107, 3)
    __Version._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 107, 3)
    
    Version = property(__Version.value, __Version.set, None, 'An optional identifier denoting the revision of this particular entity')

    _HasWildcardElement = True
    _ElementMap.update({
        __ExperimentContainer.name() : __ExperimentContainer
    })
    _AttributeMap.update({
        __Version.name() : __Version
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Part of the RunResources; specifies the required number of SMRT cells"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 118, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    
    # Attribute Quantity uses Python identifier Quantity
    __Quantity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Quantity'), 'Quantity', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_5_Quantity', pyxb.binding.datatypes.int, required=True)
    __Quantity._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 122, 3)
    __Quantity._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 122, 3)
    
    Quantity = property(__Quantity.value, __Quantity.set, None, None)

    _ElementMap.update({
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        __Quantity.name() : __Quantity
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Part of the RunResources; specifies the required number of tips via two attributes, Left and Right"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 129, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_6_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    
    # Attribute Left uses Python identifier Left
    __Left = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Left'), 'Left', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_6_Left', pyxb.binding.datatypes.int, required=True)
    __Left._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 133, 3)
    __Left._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 133, 3)
    
    Left = property(__Left.value, __Left.set, None, None)

    
    # Attribute Right uses Python identifier Right
    __Right = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Right'), 'Right', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_6_Right', pyxb.binding.datatypes.int, required=True)
    __Right._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 134, 3)
    __Right._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 134, 3)
    
    Right = property(__Right.value, __Right.set, None, None)

    _ElementMap.update({
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        __Left.name() : __Left,
        __Right.name() : __Right
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """This is an output field specifying the requirements for the run, e.g. number of tips, estimated run time, etc."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 141, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CompatibleChipLayouts uses Python identifier CompatibleChipLayouts
    __CompatibleChipLayouts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CompatibleChipLayouts'), 'CompatibleChipLayouts', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_7_httppacificbiosciences_comPacBioDataModel_xsdCompatibleChipLayouts', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 28, 1), )

    
    CompatibleChipLayouts = property(__CompatibleChipLayouts.value, __CompatibleChipLayouts.set, None, 'A set of Chip Layouts deemed compatible with the current plate')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CompatibleSequencingKits uses Python identifier CompatibleSequencingKits
    __CompatibleSequencingKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CompatibleSequencingKits'), 'CompatibleSequencingKits', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_7_httppacificbiosciences_comPacBioDataModel_xsdCompatibleSequencingKits', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 39, 1), )

    
    CompatibleSequencingKits = property(__CompatibleSequencingKits.value, __CompatibleSequencingKits.set, None, 'A set of reagent kits deemed compatible with the current plate')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_7_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    _ElementMap.update({
        __CompatibleChipLayouts.name() : __CompatibleChipLayouts,
        __CompatibleSequencingKits.name() : __CompatibleSequencingKits,
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """A general sample description"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 153, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_8_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_8_Value', pyxb.binding.datatypes.string)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 157, 3)
    __Value._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 157, 3)
    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        __Value.name() : __Value
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Multiple acquisitions from different instrument runs"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 279, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Run uses Python identifier Run
    __Run = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Run'), 'Run', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_9_httppacificbiosciences_comPacBioDataModel_xsdRun', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 281, 8), )

    
    Run = property(__Run.value, __Run.set, None, None)

    _ElementMap.update({
        __Run.name() : __Run
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Pointers to various data elements associated with the acquisitions"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 289, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSet uses Python identifier DataSet
    __DataSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_pbds, 'DataSet'), 'DataSet', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_10_httppacificbiosciences_comPacBioDatasets_xsdDataSet', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDatasets.xsd', 85, 1), )

    
    DataSet = property(__DataSet.value, __DataSet.set, None, None)

    _ElementMap.update({
        __DataSet.name() : __DataSet
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Journal of metrics, system events, or alarms that were generated during this container's lifetime"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 299, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RecordedEvent uses Python identifier RecordedEvent
    __RecordedEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvent'), 'RecordedEvent', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_11_httppacificbiosciences_comPacBioDataModel_xsdRecordedEvent', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 301, 8), )

    
    RecordedEvent = property(__RecordedEvent.value, __RecordedEvent.set, None, "Journal of metrics, system events, or alarms that were generated during this container's lifetime")

    _ElementMap.update({
        __RecordedEvent.name() : __RecordedEvent
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 310, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSample uses Python identifier BioSample
    __BioSample = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BioSample'), 'BioSample', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_12_httppacificbiosciences_comPacBioDataModel_xsdBioSample', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 312, 8), )

    
    BioSample = property(__BioSample.value, __BioSample.set, None, None)

    _ElementMap.update({
        __BioSample.name() : __BioSample
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 336, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Output'), 'Output', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_13_httppacificbiosciences_comPacBioDataModel_xsdOutput', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 65, 1), )

    
    Output = property(__Output.value, __Output.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}MultiJobId uses Python identifier MultiJobId
    __MultiJobId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MultiJobId'), 'MultiJobId', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_13_httppacificbiosciences_comPacBioDataModel_xsdMultiJobId', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 346, 8), )

    
    MultiJobId = property(__MultiJobId.value, __MultiJobId.set, None, 'Id of the SMRT Link MultiJob that will create Jobs to process the Outputs (e.g. SubreadSets) of this Run.')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SubreadSets uses Python identifier SubreadSets
    __SubreadSets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubreadSets'), 'SubreadSets', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_13_httppacificbiosciences_comPacBioDataModel_xsdSubreadSets', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 430, 1), )

    
    SubreadSets = property(__SubreadSets.value, __SubreadSets.set, None, None)

    _ElementMap.update({
        __Output.name() : __Output,
        __MultiJobId.name() : __MultiJobId,
        __SubreadSets.name() : __SubreadSets
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 355, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Input uses Python identifier Input
    __Input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Input'), 'Input', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_14_httppacificbiosciences_comPacBioDataModel_xsdInput', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 64, 1), )

    
    Input = property(__Input.value, __Input.set, None, None)

    _ElementMap.update({
        __Input.name() : __Input
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Journal of metrics, system events, or alarms that were generated during this run's lifetime"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 371, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RecordedEvent uses Python identifier RecordedEvent
    __RecordedEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvent'), 'RecordedEvent', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioDataModel_xsdRecordedEvent', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 373, 8), )

    
    RecordedEvent = property(__RecordedEvent.value, __RecordedEvent.set, None, "Journal of metrics, system events, or alarms that were generated during this run's lifetime.\nIn the case of Primary generating the DataSet containing the sts.xml, this RecordedEvent object should be a pointer to the DataSet object generated.")

    _ElementMap.update({
        __RecordedEvent.name() : __RecordedEvent
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 424, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CollectionMetadataRef uses Python identifier CollectionMetadataRef
    __CollectionMetadataRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadataRef'), 'CollectionMetadataRef', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_16_httppacificbiosciences_comPacBioDataModel_xsdCollectionMetadataRef', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 426, 4), )

    
    CollectionMetadataRef = property(__CollectionMetadataRef.value, __CollectionMetadataRef.set, None, None)

    _ElementMap.update({
        __CollectionMetadataRef.name() : __CollectionMetadataRef
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 431, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}SubreadSet uses Python identifier SubreadSet
    __SubreadSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_pbds, 'SubreadSet'), 'SubreadSet', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_17_httppacificbiosciences_comPacBioDatasets_xsdSubreadSet', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDatasets.xsd', 117, 1), )

    
    SubreadSet = property(__SubreadSet.value, __SubreadSet.set, None, None)

    _ElementMap.update({
        __SubreadSet.name() : __SubreadSet
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """A variable, as a name/value pair, associated with a protocol (one of Collection, Primary, and Secondary)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 70, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_18_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_18_Name', STD_ANON, required=True)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 74, 3)
    __Name._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 74, 3)
    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_18_Value', pyxb.binding.datatypes.string, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 91, 3)
    __Value._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 91, 3)
    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        __Name.name() : __Name,
        __Value.name() : __Value
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """
        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 166, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute IsValid uses Python identifier IsValid
    __IsValid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IsValid'), 'IsValid', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_19_IsValid', pyxb.binding.datatypes.boolean, required=True)
    __IsValid._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 167, 3)
    __IsValid._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 167, 3)
    
    IsValid = property(__IsValid.value, __IsValid.set, None, '\n            Indicates whether or not the element is valid.  The assumption is that the\n            Validation element is omitted unless the element is invalid, in which case,\n            the Validation element would describe the problem.\n          ')

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_19_ID', pyxb.binding.datatypes.string, required=True)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 176, 3)
    __ID._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 176, 3)
    
    ID = property(__ID.value, __ID.set, None, '\n            An identifier which can be used by client applications to translate/map\n            to a human decipherable message.\n          ')

    
    # Attribute Source uses Python identifier Source
    __Source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Source'), 'Source', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_19_Source', STD_ANON_, required=True)
    __Source._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 184, 3)
    __Source._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 184, 3)
    
    Source = property(__Source.value, __Source.set, None, '\n            This is the element which has experienced a validation issue.\n          ')

    
    # Attribute ElementPath uses Python identifier ElementPath
    __ElementPath = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ElementPath'), 'ElementPath', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_19_ElementPath', pyxb.binding.datatypes.string)
    __ElementPath._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 229, 3)
    __ElementPath._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 229, 3)
    
    ElementPath = property(__ElementPath.value, __ElementPath.set, None, '\n            An optional string attribute which holds the path to the offending element.\n          ')

    
    # Attribute SupplementalInfo uses Python identifier SupplementalInfo
    __SupplementalInfo = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SupplementalInfo'), 'SupplementalInfo', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_19_SupplementalInfo', pyxb.binding.datatypes.string)
    __SupplementalInfo._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 236, 3)
    __SupplementalInfo._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 236, 3)
    
    SupplementalInfo = property(__SupplementalInfo.value, __SupplementalInfo.set, None, '\n            An optional string attribute which holds extraneous information.\n          ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __IsValid.name() : __IsValid,
        __ID.name() : __ID,
        __Source.name() : __Source,
        __ElementPath.name() : __ElementPath,
        __SupplementalInfo.name() : __SupplementalInfo
    })



# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ExperimentContainerType with content type ELEMENT_ONLY
class ExperimentContainerType (_ImportedBinding__pbbase.BaseEntityType):
    """A composite object type that can encompass multiple runs, possibly across multiple instruments.  

One use case may be that a user may have a large genome they'd like to sequence, and it may take multiple runs on multiple instruments, to get enough data.  Another use case may be that a user has multiple samples of the same phenotype which they would like to analyze in a similar fashion/automation, and as such these samples are run as part of one experiment.

The experiment object is intended to be packagable, such that the metadata of all acquisitions within is contained."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExperimentContainerType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 254, 1)
    _ElementMap = _ImportedBinding__pbbase.BaseEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.BaseEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}InvestigatorName uses Python identifier InvestigatorName
    __InvestigatorName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InvestigatorName'), 'InvestigatorName', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_httppacificbiosciences_comPacBioDataModel_xsdInvestigatorName', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 265, 5), )

    
    InvestigatorName = property(__InvestigatorName.value, __InvestigatorName.set, None, 'An optional PI name')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CreatedDate uses Python identifier CreatedDate
    __CreatedDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CreatedDate'), 'CreatedDate', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_httppacificbiosciences_comPacBioDataModel_xsdCreatedDate', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 270, 5), )

    
    CreatedDate = property(__CreatedDate.value, __CreatedDate.set, None, 'Automatically generated creation date')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Runs uses Python identifier Runs
    __Runs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Runs'), 'Runs', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_httppacificbiosciences_comPacBioDataModel_xsdRuns', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 275, 5), )

    
    Runs = property(__Runs.value, __Runs.set, None, 'Multiple acquisitions from different instrument runs')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets uses Python identifier DataSets
    __DataSets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSets'), 'DataSets', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_httppacificbiosciences_comPacBioDataModel_xsdDataSets', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 285, 5), )

    
    DataSets = property(__DataSets.value, __DataSets.set, None, 'Pointers to various data elements associated with the acquisitions')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RecordedEvents uses Python identifier RecordedEvents
    __RecordedEvents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvents'), 'RecordedEvents', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_httppacificbiosciences_comPacBioDataModel_xsdRecordedEvents', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 295, 5), )

    
    RecordedEvents = property(__RecordedEvents.value, __RecordedEvents.set, None, "Journal of metrics, system events, or alarms that were generated during this container's lifetime")

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSamples uses Python identifier BioSamples
    __BioSamples = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BioSamples'), 'BioSamples', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_httppacificbiosciences_comPacBioDataModel_xsdBioSamples', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 309, 5), )

    
    BioSamples = property(__BioSamples.value, __BioSamples.set, None, None)

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ExperimentId uses Python identifier ExperimentId
    __ExperimentId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ExperimentId'), 'ExperimentId', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_ExperimentId', pyxb.binding.datatypes.string)
    __ExperimentId._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 317, 4)
    __ExperimentId._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 317, 4)
    
    ExperimentId = property(__ExperimentId.value, __ExperimentId.set, None, None)

    
    # Attribute TimeStampedName uses Python identifier TimeStampedName
    __TimeStampedName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TimeStampedName'), 'TimeStampedName', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_TimeStampedName', pyxb.binding.datatypes.string)
    __TimeStampedName._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 318, 4)
    __TimeStampedName._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 318, 4)
    
    TimeStampedName = property(__TimeStampedName.value, __TimeStampedName.set, None, 'This is NOT intended to be used as a unique field.  For uniqueness, use UniqueId.  In order to not utilize customer provided names, this attribute may be used as an alternative means of Human Readable ID, e.g. instrumentId-Run-150304_231155')

    _ElementMap.update({
        __InvestigatorName.name() : __InvestigatorName,
        __CreatedDate.name() : __CreatedDate,
        __Runs.name() : __Runs,
        __DataSets.name() : __DataSets,
        __RecordedEvents.name() : __RecordedEvents,
        __BioSamples.name() : __BioSamples
    })
    _AttributeMap.update({
        __ExperimentId.name() : __ExperimentId,
        __TimeStampedName.name() : __TimeStampedName
    })
Namespace.addCategoryObject('typeBinding', 'ExperimentContainerType', ExperimentContainerType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}AssayType with content type ELEMENT_ONLY
class AssayType (_ImportedBinding__pbbase.DataEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}AssayType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssayType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 245, 1)
    _ElementMap = _ImportedBinding__pbbase.DataEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.DataEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.DataEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SubreadSets uses Python identifier SubreadSets
    __SubreadSets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubreadSets'), 'SubreadSets', '__httppacificbiosciences_comPacBioDataModel_xsd_AssayType_httppacificbiosciences_comPacBioDataModel_xsdSubreadSets', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 430, 1), )

    
    SubreadSets = property(__SubreadSets.value, __SubreadSets.set, None, None)

    
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
        __SubreadSets.name() : __SubreadSets
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AssayType', AssayType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}RunType with content type ELEMENT_ONLY
class RunType (_ImportedBinding__pbbase.StrictEntityType):
    """A run is defined as a set of one or more data collections acquired in sequence on an instrument.  A run specifies the wells and SMRT Cells to include in the sequencing run, along with the collection and analysis automation to use for the selected wells and cells.

"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RunType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 326, 1)
    _ElementMap = _ImportedBinding__pbbase.StrictEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.StrictEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.StrictEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Assay uses Python identifier Assay
    __Assay = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Assay'), 'Assay', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_httppacificbiosciences_comPacBioDataModel_xsdAssay', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 10, 1), )

    
    Assay = property(__Assay.value, __Assay.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RunResources uses Python identifier RunResources
    __RunResources = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RunResources'), 'RunResources', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_httppacificbiosciences_comPacBioDataModel_xsdRunResources', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 137, 1), )

    
    RunResources = property(__RunResources.value, __RunResources.set, None, 'This is an output field specifying the requirements for the run, e.g. number of tips, estimated run time, etc.')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Outputs uses Python identifier Outputs
    __Outputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Outputs'), 'Outputs', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_httppacificbiosciences_comPacBioDataModel_xsdOutputs', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 335, 5), )

    
    Outputs = property(__Outputs.value, __Outputs.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Inputs uses Python identifier Inputs
    __Inputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Inputs'), 'Inputs', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_httppacificbiosciences_comPacBioDataModel_xsdInputs', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 354, 5), )

    
    Inputs = property(__Inputs.value, __Inputs.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RecordedEvents uses Python identifier RecordedEvents
    __RecordedEvents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvents'), 'RecordedEvents', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_httppacificbiosciences_comPacBioDataModel_xsdRecordedEvents', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 367, 5), )

    
    RecordedEvents = property(__RecordedEvents.value, __RecordedEvents.set, None, "Journal of metrics, system events, or alarms that were generated during this run's lifetime")

    
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
    
    # Attribute Status uses Python identifier Status
    __Status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Status'), 'Status', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_Status', _ImportedBinding__pbbase.SupportedRunStates)
    __Status._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 383, 4)
    __Status._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 383, 4)
    
    Status = property(__Status.value, __Status.set, None, None)

    
    # Attribute InstrumentId uses Python identifier InstrumentId
    __InstrumentId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'InstrumentId'), 'InstrumentId', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_InstrumentId', pyxb.binding.datatypes.string)
    __InstrumentId._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 384, 4)
    __InstrumentId._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 384, 4)
    
    InstrumentId = property(__InstrumentId.value, __InstrumentId.set, None, 'World unique id assigned by PacBio. ')

    
    # Attribute InstrumentName uses Python identifier InstrumentName
    __InstrumentName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'InstrumentName'), 'InstrumentName', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_InstrumentName', pyxb.binding.datatypes.string)
    __InstrumentName._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 389, 4)
    __InstrumentName._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 389, 4)
    
    InstrumentName = property(__InstrumentName.value, __InstrumentName.set, None, 'Friendly name assigned by customer')

    
    # Attribute CreatedBy uses Python identifier CreatedBy
    __CreatedBy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CreatedBy'), 'CreatedBy', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_CreatedBy', pyxb.binding.datatypes.string)
    __CreatedBy._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 394, 4)
    __CreatedBy._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 394, 4)
    
    CreatedBy = property(__CreatedBy.value, __CreatedBy.set, None, 'Who created the run. ')

    
    # Attribute StartedBy uses Python identifier StartedBy
    __StartedBy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'StartedBy'), 'StartedBy', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_StartedBy', pyxb.binding.datatypes.string)
    __StartedBy._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 399, 4)
    __StartedBy._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 399, 4)
    
    StartedBy = property(__StartedBy.value, __StartedBy.set, None, 'Who started the run. Could be different from who created it. ')

    
    # Attribute WhenStarted uses Python identifier WhenStarted
    __WhenStarted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'WhenStarted'), 'WhenStarted', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_WhenStarted', STD_ANON_2)
    __WhenStarted._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 404, 4)
    __WhenStarted._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 404, 4)
    
    WhenStarted = property(__WhenStarted.value, __WhenStarted.set, None, 'Date and time of when the overall run was started. ')

    
    # Attribute WhenCompleted uses Python identifier WhenCompleted
    __WhenCompleted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'WhenCompleted'), 'WhenCompleted', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_WhenCompleted', STD_ANON_3)
    __WhenCompleted._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 412, 4)
    __WhenCompleted._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 412, 4)
    
    WhenCompleted = property(__WhenCompleted.value, __WhenCompleted.set, None, 'Date and time of when the overall run was completed. ')

    _ElementMap.update({
        __Assay.name() : __Assay,
        __RunResources.name() : __RunResources,
        __Outputs.name() : __Outputs,
        __Inputs.name() : __Inputs,
        __RecordedEvents.name() : __RecordedEvents
    })
    _AttributeMap.update({
        __Status.name() : __Status,
        __InstrumentId.name() : __InstrumentId,
        __InstrumentName.name() : __InstrumentName,
        __CreatedBy.name() : __CreatedBy,
        __StartedBy.name() : __StartedBy,
        __WhenStarted.name() : __WhenStarted,
        __WhenCompleted.name() : __WhenCompleted
    })
Namespace.addCategoryObject('typeBinding', 'RunType', RunType)


ChipLayout = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout'), CTD_ANON, documentation='Part of the RunResources; specifies a ChipLayout which is compatible with the collection protocols defined on the plate', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 11, 1))
Namespace.addCategoryObject('elementBinding', ChipLayout.name().localName(), ChipLayout)

CompatibleChipLayouts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompatibleChipLayouts'), CTD_ANON_, documentation='A set of Chip Layouts deemed compatible with the current plate', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 28, 1))
Namespace.addCategoryObject('elementBinding', CompatibleChipLayouts.name().localName(), CompatibleChipLayouts)

CompatibleSequencingKits = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompatibleSequencingKits'), CTD_ANON_2, documentation='A set of reagent kits deemed compatible with the current plate', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 39, 1))
Namespace.addCategoryObject('elementBinding', CompatibleSequencingKits.name().localName(), CompatibleSequencingKits)

EstimatedTotalRunTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EstimatedTotalRunTime'), CTD_ANON_3, documentation='The total amount of time the run is estimated to require.  A confidence value (defaulted to 90%) indicates the degree of certainty associated with the estimate', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 51, 1))
Namespace.addCategoryObject('elementBinding', EstimatedTotalRunTime.name().localName(), EstimatedTotalRunTime)

PacBioDataModel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PacBioDataModel'), CTD_ANON_4, documentation='PacBio Data Model root element', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 94, 1))
Namespace.addCategoryObject('elementBinding', PacBioDataModel.name().localName(), PacBioDataModel)

RequiredSMRTCells = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequiredSMRTCells'), CTD_ANON_5, documentation='Part of the RunResources; specifies the required number of SMRT cells', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 114, 1))
Namespace.addCategoryObject('elementBinding', RequiredSMRTCells.name().localName(), RequiredSMRTCells)

RequiredTips = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequiredTips'), CTD_ANON_6, documentation='Part of the RunResources; specifies the required number of tips via two attributes, Left and Right', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 125, 1))
Namespace.addCategoryObject('elementBinding', RequiredTips.name().localName(), RequiredTips)

RunResources = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RunResources'), CTD_ANON_7, documentation='This is an output field specifying the requirements for the run, e.g. number of tips, estimated run time, etc.', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 137, 1))
Namespace.addCategoryObject('elementBinding', RunResources.name().localName(), RunResources)

SampleComment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleComment'), CTD_ANON_8, documentation='A general sample description', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 149, 1))
Namespace.addCategoryObject('elementBinding', SampleComment.name().localName(), SampleComment)

CollectionReferences = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionReferences'), CTD_ANON_16, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 423, 1))
Namespace.addCategoryObject('elementBinding', CollectionReferences.name().localName(), CollectionReferences)

SubreadSets = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubreadSets'), CTD_ANON_17, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 430, 1))
Namespace.addCategoryObject('elementBinding', SubreadSets.name().localName(), SubreadSets)

Parameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), CTD_ANON_18, documentation='A variable, as a name/value pair, associated with a protocol (one of Collection, Primary, and Secondary)', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 66, 1))
Namespace.addCategoryObject('elementBinding', Parameter.name().localName(), Parameter)

Validation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_19, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1))
Namespace.addCategoryObject('elementBinding', Validation.name().localName(), Validation)

Assay = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Assay'), AssayType, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 10, 1))
Namespace.addCategoryObject('elementBinding', Assay.name().localName(), Assay)

Events = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Events'), _ImportedBinding__pbbase.RecordedEventType, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 63, 1))
Namespace.addCategoryObject('elementBinding', Events.name().localName(), Events)

Input = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Input'), _ImportedBinding__pbbase.InputOutputDataType, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 64, 1))
Namespace.addCategoryObject('elementBinding', Input.name().localName(), Input)

Output = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Output'), _ImportedBinding__pbbase.InputOutputDataType, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 65, 1))
Namespace.addCategoryObject('elementBinding', Output.name().localName(), Output)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_19, scope=CTD_ANON, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 17, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 17, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout'), CTD_ANON, scope=CTD_ANON_, documentation='Part of the RunResources; specifies a ChipLayout which is compatible with the collection protocols defined on the plate', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 11, 1)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_19, scope=CTD_ANON_, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 35, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 34, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 35, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EstimatedTotalRunTime'), CTD_ANON_3, scope=CTD_ANON_2, documentation='The total amount of time the run is estimated to require.  A confidence value (defaulted to 90%) indicates the degree of certainty associated with the estimate', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 51, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequiredTips'), CTD_ANON_6, scope=CTD_ANON_2, documentation='Part of the RunResources; specifies the required number of tips via two attributes, Left and Right', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 125, 1)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_pbpn, 'SequencingKit'), _ImportedBinding__pbrk.SupplyKitSequencing, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 14, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbpn, 'SequencingKit')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 45, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RequiredTips')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 46, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EstimatedTotalRunTime')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 47, 4))
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
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_19, scope=CTD_ANON_3, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 57, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 57, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExperimentContainer'), ExperimentContainerType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 100, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 101, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExperimentContainer')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 100, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 101, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_19, scope=CTD_ANON_5, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 120, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 120, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_19, scope=CTD_ANON_6, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 131, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 131, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompatibleChipLayouts'), CTD_ANON_, scope=CTD_ANON_7, documentation='A set of Chip Layouts deemed compatible with the current plate', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 28, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompatibleSequencingKits'), CTD_ANON_2, scope=CTD_ANON_7, documentation='A set of reagent kits deemed compatible with the current plate', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 39, 1)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_19, scope=CTD_ANON_7, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 145, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CompatibleSequencingKits')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 143, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CompatibleChipLayouts')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 144, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 145, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_19, scope=CTD_ANON_8, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 155, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 155, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Run'), RunType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 281, 8)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Run')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 281, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_pbds, 'DataSet'), _ImportedBinding__pbds.DataSetType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDatasets.xsd', 85, 1)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 291, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbds, 'DataSet')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 291, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_10()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvent'), _ImportedBinding__pbbase.RecordedEventType, scope=CTD_ANON_11, documentation="Journal of metrics, system events, or alarms that were generated during this container's lifetime", location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 301, 8)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 301, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvent')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 301, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_11()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSample'), _ImportedBinding__pbsample.BioSampleType, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 312, 8)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 312, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BioSample')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 312, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_12()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Output'), _ImportedBinding__pbbase.InputOutputDataType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 65, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MultiJobId'), pyxb.binding.datatypes.unsignedInt, scope=CTD_ANON_13, documentation='Id of the SMRT Link MultiJob that will create Jobs to process the Outputs (e.g. SubreadSets) of this Run.', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 346, 8)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubreadSets'), CTD_ANON_17, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 430, 1)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 338, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 339, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 346, 8))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Output')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 338, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubreadSets')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 339, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MultiJobId')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 346, 8))
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
CTD_ANON_13._Automaton = _BuildAutomaton_13()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Input'), _ImportedBinding__pbbase.InputOutputDataType, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 64, 1)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Input')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 357, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_14()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvent'), _ImportedBinding__pbbase.RecordedEventType, scope=CTD_ANON_15, documentation="Journal of metrics, system events, or alarms that were generated during this run's lifetime.\nIn the case of Primary generating the DataSet containing the sts.xml, this RecordedEvent object should be a pointer to the DataSet object generated.", location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 373, 8)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 373, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvent')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 373, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_15()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadataRef'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 426, 4)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadataRef')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 426, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_16()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_pbds, 'SubreadSet'), _ImportedBinding__pbds.CTD_ANON_16, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDatasets.xsd', 117, 1)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbds, 'SubreadSet')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 433, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_17()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_19, scope=CTD_ANON_18, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 160, 1)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 72, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 72, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_18()




ExperimentContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InvestigatorName'), pyxb.binding.datatypes.string, scope=ExperimentContainerType, documentation='An optional PI name', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 265, 5)))

ExperimentContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CreatedDate'), pyxb.binding.datatypes.date, scope=ExperimentContainerType, documentation='Automatically generated creation date', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 270, 5)))

ExperimentContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Runs'), CTD_ANON_9, scope=ExperimentContainerType, documentation='Multiple acquisitions from different instrument runs', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 275, 5)))

ExperimentContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSets'), CTD_ANON_10, scope=ExperimentContainerType, documentation='Pointers to various data elements associated with the acquisitions', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 285, 5)))

ExperimentContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvents'), CTD_ANON_11, scope=ExperimentContainerType, documentation="Journal of metrics, system events, or alarms that were generated during this container's lifetime", location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 295, 5)))

ExperimentContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSamples'), CTD_ANON_12, scope=ExperimentContainerType, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 309, 5)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 88, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 265, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 275, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 285, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 295, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 309, 5))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 88, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InvestigatorName')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 265, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CreatedDate')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 270, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Runs')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 275, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 285, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvents')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 295, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BioSamples')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 309, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ExperimentContainerType._Automaton = _BuildAutomaton_19()




AssayType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubreadSets'), CTD_ANON_17, scope=AssayType, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 430, 1)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 88, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 195, 5))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssayType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 88, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssayType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'CheckSum')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 195, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssayType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubreadSets')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 249, 5))
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AssayType._Automaton = _BuildAutomaton_20()




RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Assay'), AssayType, scope=RunType, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 10, 1)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RunResources'), CTD_ANON_7, scope=RunType, documentation='This is an output field specifying the requirements for the run, e.g. number of tips, estimated run time, etc.', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 137, 1)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Outputs'), CTD_ANON_13, scope=RunType, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 335, 5)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Inputs'), CTD_ANON_14, scope=RunType, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 354, 5)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvents'), CTD_ANON_15, scope=RunType, documentation="Journal of metrics, system events, or alarms that were generated during this run's lifetime", location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 367, 5)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 88, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 335, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 354, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 361, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 366, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 367, 5))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 88, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Outputs')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 335, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Inputs')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 354, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Assay')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 361, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RunResources')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 366, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvents')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioDataModel.xsd', 367, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
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
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RunType._Automaton = _BuildAutomaton_21()

