# ./_pbrk.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:82fd17ff8c81a0cc423cbd13a9167bcda5f96419
# Generated 2015-12-08 13:20:39.138291 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace http://pacificbiosciences.com/PacBioReagentKit.xsd [xmlns:pbrk]

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
import _pbbase as _ImportedBinding__pbbase

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://pacificbiosciences.com/PacBioReagentKit.xsd', create_if_missing=True)
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


# Atomic simple type: {http://pacificbiosciences.com/PacBioReagentKit.xsd}TubeLocation
class TubeLocation (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TubeLocation')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 122, 1)
    _Documentation = None
TubeLocation._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TubeLocation, enum_prefix=None)
TubeLocation.ReagentTube0 = TubeLocation._CF_enumeration.addEnumeration(unicode_value='ReagentTube0', tag='ReagentTube0')
TubeLocation.ReagentTube1 = TubeLocation._CF_enumeration.addEnumeration(unicode_value='ReagentTube1', tag='ReagentTube1')
TubeLocation._InitializeFacetMap(TubeLocation._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TubeLocation', TubeLocation)

# Atomic simple type: {http://pacificbiosciences.com/PacBioReagentKit.xsd}TubeSize
class TubeSize (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TubeSize')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 128, 1)
    _Documentation = None
TubeSize._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TubeSize, enum_prefix=None)
TubeSize.DeepTube = TubeSize._CF_enumeration.addEnumeration(unicode_value='DeepTube', tag='DeepTube')
TubeSize.ShallowTube = TubeSize._CF_enumeration.addEnumeration(unicode_value='ShallowTube', tag='ShallowTube')
TubeSize._InitializeFacetMap(TubeSize._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TubeSize', TubeSize)

# Atomic simple type: {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentKey
class ReagentKey (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReagentKey')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 134, 1)
    _Documentation = None
ReagentKey._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ReagentKey, enum_prefix=None)
ReagentKey.Base = ReagentKey._CF_enumeration.addEnumeration(unicode_value='Base', tag='Base')
ReagentKey.DTT = ReagentKey._CF_enumeration.addEnumeration(unicode_value='DTT', tag='DTT')
ReagentKey.DilBuffer = ReagentKey._CF_enumeration.addEnumeration(unicode_value='DilBuffer', tag='DilBuffer')
ReagentKey.MineralOil = ReagentKey._CF_enumeration.addEnumeration(unicode_value='MineralOil', tag='MineralOil')
ReagentKey.MIXED_DilBuffer = ReagentKey._CF_enumeration.addEnumeration(unicode_value='MIXED_DilBuffer', tag='MIXED_DilBuffer')
ReagentKey.MIXED_OS = ReagentKey._CF_enumeration.addEnumeration(unicode_value='MIXED_OS', tag='MIXED_OS')
ReagentKey.OSbuffer = ReagentKey._CF_enumeration.addEnumeration(unicode_value='OSbuffer', tag='OSbuffer')
ReagentKey.OSenzyme = ReagentKey._CF_enumeration.addEnumeration(unicode_value='OSenzyme', tag='OSenzyme')
ReagentKey.PhospholinkedNT = ReagentKey._CF_enumeration.addEnumeration(unicode_value='PhospholinkedNT', tag='PhospholinkedNT')
ReagentKey.SABuffer = ReagentKey._CF_enumeration.addEnumeration(unicode_value='SABuffer', tag='SABuffer')
ReagentKey.Spike = ReagentKey._CF_enumeration.addEnumeration(unicode_value='Spike', tag='Spike')
ReagentKey.Streptavidin = ReagentKey._CF_enumeration.addEnumeration(unicode_value='Streptavidin', tag='Streptavidin')
ReagentKey.SubstrateOS = ReagentKey._CF_enumeration.addEnumeration(unicode_value='SubstrateOS', tag='SubstrateOS')
ReagentKey.TSQ = ReagentKey._CF_enumeration.addEnumeration(unicode_value='TSQ', tag='TSQ')
ReagentKey.WashBuffer = ReagentKey._CF_enumeration.addEnumeration(unicode_value='WashBuffer', tag='WashBuffer')
ReagentKey.WettingBuffer = ReagentKey._CF_enumeration.addEnumeration(unicode_value='WettingBuffer', tag='WettingBuffer')
ReagentKey.PCA = ReagentKey._CF_enumeration.addEnumeration(unicode_value='PCA', tag='PCA')
ReagentKey.PCD = ReagentKey._CF_enumeration.addEnumeration(unicode_value='PCD', tag='PCD')
ReagentKey.Analog = ReagentKey._CF_enumeration.addEnumeration(unicode_value='Analog', tag='Analog')
ReagentKey.Sample = ReagentKey._CF_enumeration.addEnumeration(unicode_value='Sample', tag='Sample')
ReagentKey.PEGDilBuffer = ReagentKey._CF_enumeration.addEnumeration(unicode_value='PEGDilBuffer', tag='PEGDilBuffer')
ReagentKey.ExtraBuffer = ReagentKey._CF_enumeration.addEnumeration(unicode_value='ExtraBuffer', tag='ExtraBuffer')
ReagentKey.PrewetBuffer = ReagentKey._CF_enumeration.addEnumeration(unicode_value='PrewetBuffer', tag='PrewetBuffer')
ReagentKey._InitializeFacetMap(ReagentKey._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReagentKey', ReagentKey)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """The root element of the reagent kit standalone file"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 11, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentKit uses Python identifier ReagentKit
    __ReagentKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentKit'), 'ReagentKit', '__httppacificbiosciences_comPacBioReagentKit_xsd_CTD_ANON_httppacificbiosciences_comPacBioReagentKit_xsdReagentKit', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 18, 1), )

    
    ReagentKit = property(__ReagentKit.value, __ReagentKit.set, None, None)

    _ElementMap.update({
        __ReagentKit.name() : __ReagentKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 70, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioReagentKit.xsd}Reagent uses Python identifier Reagent
    __Reagent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reagent'), 'Reagent', '__httppacificbiosciences_comPacBioReagentKit_xsd_CTD_ANON__httppacificbiosciences_comPacBioReagentKit_xsdReagent', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 17, 1), )

    
    Reagent = property(__Reagent.value, __Reagent.set, None, None)

    _ElementMap.update({
        __Reagent.name() : __Reagent
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 77, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentTube uses Python identifier ReagentTube
    __ReagentTube = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube'), 'ReagentTube', '__httppacificbiosciences_comPacBioReagentKit_xsd_CTD_ANON_2_httppacificbiosciences_comPacBioReagentKit_xsdReagentTube', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 19, 1), )

    
    ReagentTube = property(__ReagentTube.value, __ReagentTube.set, None, None)

    _ElementMap.update({
        __ReagentTube.name() : __ReagentTube
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 84, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentPlateRow uses Python identifier ReagentPlateRow
    __ReagentPlateRow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRow'), 'ReagentPlateRow', '__httppacificbiosciences_comPacBioReagentKit_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioReagentKit_xsdReagentPlateRow', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 20, 1), )

    
    ReagentPlateRow = property(__ReagentPlateRow.value, __ReagentPlateRow.set, None, None)

    _ElementMap.update({
        __ReagentPlateRow.name() : __ReagentPlateRow
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentType with content type ELEMENT_ONLY
class ReagentType (_ImportedBinding__pbbase.BaseEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReagentType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 54, 1)
    _ElementMap = _ImportedBinding__pbbase.BaseEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.BaseEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ReagentKey uses Python identifier ReagentKey
    __ReagentKey = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ReagentKey'), 'ReagentKey', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentType_ReagentKey', ReagentKey, required=True)
    __ReagentKey._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 57, 4)
    __ReagentKey._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 57, 4)
    
    ReagentKey = property(__ReagentKey.value, __ReagentKey.set, None, None)

    
    # Attribute PlateColumn uses Python identifier PlateColumn
    __PlateColumn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PlateColumn'), 'PlateColumn', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentType_PlateColumn', pyxb.binding.datatypes.string, required=True)
    __PlateColumn._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 58, 4)
    __PlateColumn._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 58, 4)
    
    PlateColumn = property(__PlateColumn.value, __PlateColumn.set, None, None)

    
    # Attribute Volume uses Python identifier Volume
    __Volume = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Volume'), 'Volume', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentType_Volume', pyxb.binding.datatypes.int, required=True)
    __Volume._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 59, 4)
    __Volume._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 59, 4)
    
    Volume = property(__Volume.value, __Volume.set, None, None)

    
    # Attribute DeadVolume uses Python identifier DeadVolume
    __DeadVolume = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DeadVolume'), 'DeadVolume', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentType_DeadVolume', pyxb.binding.datatypes.int, required=True)
    __DeadVolume._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 60, 4)
    __DeadVolume._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 60, 4)
    
    DeadVolume = property(__DeadVolume.value, __DeadVolume.set, None, None)

    
    # Attribute ActiveInHour uses Python identifier ActiveInHour
    __ActiveInHour = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ActiveInHour'), 'ActiveInHour', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentType_ActiveInHour', pyxb.binding.datatypes.int, required=True)
    __ActiveInHour._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 61, 4)
    __ActiveInHour._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 61, 4)
    
    ActiveInHour = property(__ActiveInHour.value, __ActiveInHour.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ReagentKey.name() : __ReagentKey,
        __PlateColumn.name() : __PlateColumn,
        __Volume.name() : __Volume,
        __DeadVolume.name() : __DeadVolume,
        __ActiveInHour.name() : __ActiveInHour
    })
Namespace.addCategoryObject('typeBinding', 'ReagentType', ReagentType)


# Complex type {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentKitType with content type ELEMENT_ONLY
class ReagentKitType (_ImportedBinding__pbbase.BaseEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentKitType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReagentKitType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 65, 1)
    _ElementMap = _ImportedBinding__pbbase.BaseEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.BaseEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ChemistryConfig uses Python identifier ChemistryConfig
    __ChemistryConfig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ChemistryConfig'), 'ChemistryConfig', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentKitType_httppacificbiosciences_comPacBioBaseDataModel_xsdChemistryConfig', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 797, 1), )

    
    ChemistryConfig = property(__ChemistryConfig.value, __ChemistryConfig.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioReagentKit.xsd}Reagents uses Python identifier Reagents
    __Reagents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reagents'), 'Reagents', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentKitType_httppacificbiosciences_comPacBioReagentKit_xsdReagents', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 69, 5), )

    
    Reagents = property(__Reagents.value, __Reagents.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentTubes uses Python identifier ReagentTubes
    __ReagentTubes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentTubes'), 'ReagentTubes', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentKitType_httppacificbiosciences_comPacBioReagentKit_xsdReagentTubes', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 76, 5), )

    
    ReagentTubes = property(__ReagentTubes.value, __ReagentTubes.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentPlateRows uses Python identifier ReagentPlateRows
    __ReagentPlateRows = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRows'), 'ReagentPlateRows', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentKitType_httppacificbiosciences_comPacBioReagentKit_xsdReagentPlateRows', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 83, 5), )

    
    ReagentPlateRows = property(__ReagentPlateRows.value, __ReagentPlateRows.set, None, None)

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ProductCode uses Python identifier ProductCode
    __ProductCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ProductCode'), 'ProductCode', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentKitType_ProductCode', pyxb.binding.datatypes.string)
    __ProductCode._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 92, 4)
    __ProductCode._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 92, 4)
    
    ProductCode = property(__ProductCode.value, __ProductCode.set, None, None)

    
    # Attribute PlateType uses Python identifier PlateType
    __PlateType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PlateType'), 'PlateType', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentKitType_PlateType', pyxb.binding.datatypes.string)
    __PlateType._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 93, 4)
    __PlateType._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 93, 4)
    
    PlateType = property(__PlateType.value, __PlateType.set, None, None)

    
    # Attribute ActiveInHour uses Python identifier ActiveInHour
    __ActiveInHour = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ActiveInHour'), 'ActiveInHour', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentKitType_ActiveInHour', pyxb.binding.datatypes.int)
    __ActiveInHour._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 94, 4)
    __ActiveInHour._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 94, 4)
    
    ActiveInHour = property(__ActiveInHour.value, __ActiveInHour.set, None, None)

    
    # Attribute BasesPerSecond uses Python identifier BasesPerSecond
    __BasesPerSecond = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'BasesPerSecond'), 'BasesPerSecond', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentKitType_BasesPerSecond', pyxb.binding.datatypes.decimal)
    __BasesPerSecond._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 95, 4)
    __BasesPerSecond._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 95, 4)
    
    BasesPerSecond = property(__BasesPerSecond.value, __BasesPerSecond.set, None, None)

    
    # Attribute AcquisitionCount uses Python identifier AcquisitionCount
    __AcquisitionCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'AcquisitionCount'), 'AcquisitionCount', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentKitType_AcquisitionCount', pyxb.binding.datatypes.int)
    __AcquisitionCount._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 96, 4)
    __AcquisitionCount._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 96, 4)
    
    AcquisitionCount = property(__AcquisitionCount.value, __AcquisitionCount.set, None, None)

    _ElementMap.update({
        __ChemistryConfig.name() : __ChemistryConfig,
        __Reagents.name() : __Reagents,
        __ReagentTubes.name() : __ReagentTubes,
        __ReagentPlateRows.name() : __ReagentPlateRows
    })
    _AttributeMap.update({
        __ProductCode.name() : __ProductCode,
        __PlateType.name() : __PlateType,
        __ActiveInHour.name() : __ActiveInHour,
        __BasesPerSecond.name() : __BasesPerSecond,
        __AcquisitionCount.name() : __AcquisitionCount
    })
Namespace.addCategoryObject('typeBinding', 'ReagentKitType', ReagentKitType)


# Complex type {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentTubeType with content type ELEMENT_ONLY
class ReagentTubeType (_ImportedBinding__pbbase.BaseEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentTubeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReagentTubeType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 100, 1)
    _ElementMap = _ImportedBinding__pbbase.BaseEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.BaseEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ProductCode uses Python identifier ProductCode
    __ProductCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ProductCode'), 'ProductCode', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentTubeType_ProductCode', pyxb.binding.datatypes.string, required=True)
    __ProductCode._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 103, 4)
    __ProductCode._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 103, 4)
    
    ProductCode = property(__ProductCode.value, __ProductCode.set, None, None)

    
    # Attribute ReagentKey uses Python identifier ReagentKey
    __ReagentKey = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ReagentKey'), 'ReagentKey', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentTubeType_ReagentKey', ReagentKey, required=True)
    __ReagentKey._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 104, 4)
    __ReagentKey._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 104, 4)
    
    ReagentKey = property(__ReagentKey.value, __ReagentKey.set, None, None)

    
    # Attribute Volume uses Python identifier Volume
    __Volume = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Volume'), 'Volume', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentTubeType_Volume', pyxb.binding.datatypes.short, required=True)
    __Volume._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 105, 4)
    __Volume._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 105, 4)
    
    Volume = property(__Volume.value, __Volume.set, None, None)

    
    # Attribute DeadVolume uses Python identifier DeadVolume
    __DeadVolume = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DeadVolume'), 'DeadVolume', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentTubeType_DeadVolume', pyxb.binding.datatypes.short, required=True)
    __DeadVolume._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 106, 4)
    __DeadVolume._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 106, 4)
    
    DeadVolume = property(__DeadVolume.value, __DeadVolume.set, None, None)

    
    # Attribute ActiveInHour uses Python identifier ActiveInHour
    __ActiveInHour = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ActiveInHour'), 'ActiveInHour', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentTubeType_ActiveInHour', pyxb.binding.datatypes.int, required=True)
    __ActiveInHour._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 107, 4)
    __ActiveInHour._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 107, 4)
    
    ActiveInHour = property(__ActiveInHour.value, __ActiveInHour.set, None, None)

    
    # Attribute TubeWellType uses Python identifier TubeWellType
    __TubeWellType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TubeWellType'), 'TubeWellType', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentTubeType_TubeWellType', TubeSize, required=True)
    __TubeWellType._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 108, 4)
    __TubeWellType._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 108, 4)
    
    TubeWellType = property(__TubeWellType.value, __TubeWellType.set, None, None)

    
    # Attribute ReagentTubeType uses Python identifier ReagentTubeType
    __ReagentTubeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ReagentTubeType'), 'ReagentTubeType', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentTubeType_ReagentTubeType', TubeLocation, required=True)
    __ReagentTubeType._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 109, 4)
    __ReagentTubeType._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 109, 4)
    
    ReagentTubeType = property(__ReagentTubeType.value, __ReagentTubeType.set, None, None)

    
    # Attribute InitialUse uses Python identifier InitialUse
    __InitialUse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'InitialUse'), 'InitialUse', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentTubeType_InitialUse', pyxb.binding.datatypes.dateTime)
    __InitialUse._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 110, 4)
    __InitialUse._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 110, 4)
    
    InitialUse = property(__InitialUse.value, __InitialUse.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ProductCode.name() : __ProductCode,
        __ReagentKey.name() : __ReagentKey,
        __Volume.name() : __Volume,
        __DeadVolume.name() : __DeadVolume,
        __ActiveInHour.name() : __ActiveInHour,
        __TubeWellType.name() : __TubeWellType,
        __ReagentTubeType.name() : __ReagentTubeType,
        __InitialUse.name() : __InitialUse
    })
Namespace.addCategoryObject('typeBinding', 'ReagentTubeType', ReagentTubeType)


# Complex type {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentPlateRowType with content type ELEMENT_ONLY
class ReagentPlateRowType (_ImportedBinding__pbbase.BaseEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentPlateRowType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRowType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 114, 1)
    _ElementMap = _ImportedBinding__pbbase.BaseEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.BaseEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute PlateRow uses Python identifier PlateRow
    __PlateRow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PlateRow'), 'PlateRow', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentPlateRowType_PlateRow', pyxb.binding.datatypes.string, required=True)
    __PlateRow._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 117, 4)
    __PlateRow._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 117, 4)
    
    PlateRow = property(__PlateRow.value, __PlateRow.set, None, None)

    
    # Attribute InitialUse uses Python identifier InitialUse
    __InitialUse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'InitialUse'), 'InitialUse', '__httppacificbiosciences_comPacBioReagentKit_xsd_ReagentPlateRowType_InitialUse', pyxb.binding.datatypes.dateTime)
    __InitialUse._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 118, 4)
    __InitialUse._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 118, 4)
    
    InitialUse = property(__InitialUse.value, __InitialUse.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __PlateRow.name() : __PlateRow,
        __InitialUse.name() : __InitialUse
    })
Namespace.addCategoryObject('typeBinding', 'ReagentPlateRowType', ReagentPlateRowType)


# Complex type {http://pacificbiosciences.com/PacBioReagentKit.xsd}SupplyKitSequencing with content type ELEMENT_ONLY
class SupplyKitSequencing (_ImportedBinding__pbbase.PartNumberType):
    """A more specific template kit representation (includes SupplyKit fields). """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplyKitSequencing')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 21, 1)
    _ElementMap = _ImportedBinding__pbbase.PartNumberType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.PartNumberType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.PartNumberType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentAutomationName uses Python identifier ReagentAutomationName
    __ReagentAutomationName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentAutomationName'), 'ReagentAutomationName', '__httppacificbiosciences_comPacBioReagentKit_xsd_SupplyKitSequencing_httppacificbiosciences_comPacBioReagentKit_xsdReagentAutomationName', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 28, 5), )

    
    ReagentAutomationName = property(__ReagentAutomationName.value, __ReagentAutomationName.set, None, 'The reagent-mixing protocol used. ')

    
    # Element {http://pacificbiosciences.com/PacBioReagentKit.xsd}ReagentTubes uses Python identifier ReagentTubes
    __ReagentTubes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentTubes'), 'ReagentTubes', '__httppacificbiosciences_comPacBioReagentKit_xsd_SupplyKitSequencing_httppacificbiosciences_comPacBioReagentKit_xsdReagentTubes', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 33, 5), )

    
    ReagentTubes = property(__ReagentTubes.value, __ReagentTubes.set, None, "Tubes associated with the reagent kit - can have up to two; don't forget to set the location, 0 or 1")

    
    # Element {http://pacificbiosciences.com/PacBioReagentKit.xsd}SequencingChemistry uses Python identifier SequencingChemistry
    __SequencingChemistry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingChemistry'), 'SequencingChemistry', '__httppacificbiosciences_comPacBioReagentKit_xsd_SupplyKitSequencing_httppacificbiosciences_comPacBioReagentKit_xsdSequencingChemistry', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 38, 5), )

    
    SequencingChemistry = property(__SequencingChemistry.value, __SequencingChemistry.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioReagentKit.xsd}SequencingKitDefinition uses Python identifier SequencingKitDefinition
    __SequencingKitDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitDefinition'), 'SequencingKitDefinition', '__httppacificbiosciences_comPacBioReagentKit_xsd_SupplyKitSequencing_httppacificbiosciences_comPacBioReagentKit_xsdSequencingKitDefinition', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 39, 5), )

    
    SequencingKitDefinition = property(__SequencingKitDefinition.value, __SequencingKitDefinition.set, None, None)

    
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
    
    # Attribute Location uses Python identifier Location
    __Location = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Location'), 'Location', '__httppacificbiosciences_comPacBioReagentKit_xsd_SupplyKitSequencing_Location', pyxb.binding.datatypes.int, unicode_default='0')
    __Location._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 41, 4)
    __Location._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 41, 4)
    
    Location = property(__Location.value, __Location.set, None, 'The location of the supply kit - for a reagent plate, it could be 0 or 1, and for a tube it could be 0 or 1')

    
    # Attribute MaxCollections uses Python identifier MaxCollections
    __MaxCollections = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MaxCollections'), 'MaxCollections', '__httppacificbiosciences_comPacBioReagentKit_xsd_SupplyKitSequencing_MaxCollections', pyxb.binding.datatypes.int, unicode_default='8')
    __MaxCollections._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 46, 4)
    __MaxCollections._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 46, 4)
    
    MaxCollections = property(__MaxCollections.value, __MaxCollections.set, None, 'The number of collections this supply kit is capable of')

    _ElementMap.update({
        __ReagentAutomationName.name() : __ReagentAutomationName,
        __ReagentTubes.name() : __ReagentTubes,
        __SequencingChemistry.name() : __SequencingChemistry,
        __SequencingKitDefinition.name() : __SequencingKitDefinition
    })
    _AttributeMap.update({
        __Location.name() : __Location,
        __MaxCollections.name() : __MaxCollections
    })
Namespace.addCategoryObject('typeBinding', 'SupplyKitSequencing', SupplyKitSequencing)


PacBioReagentKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PacBioReagentKit'), CTD_ANON, documentation='The root element of the reagent kit standalone file', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', PacBioReagentKit.name().localName(), PacBioReagentKit)

Reagent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reagent'), ReagentType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 17, 1))
Namespace.addCategoryObject('elementBinding', Reagent.name().localName(), Reagent)

ReagentKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentKit'), ReagentKitType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 18, 1))
Namespace.addCategoryObject('elementBinding', ReagentKit.name().localName(), ReagentKit)

ReagentTube = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube'), ReagentTubeType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 19, 1))
Namespace.addCategoryObject('elementBinding', ReagentTube.name().localName(), ReagentTube)

ReagentPlateRow = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRow'), ReagentPlateRowType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 20, 1))
Namespace.addCategoryObject('elementBinding', ReagentPlateRow.name().localName(), ReagentPlateRow)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentKit'), ReagentKitType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 18, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentKit')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 13, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reagent'), ReagentType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 17, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reagent')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 72, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube'), ReagentTubeType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 19, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 79, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRow'), ReagentPlateRowType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 20, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRow')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 86, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReagentType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReagentType._Automaton = _BuildAutomaton_4()




ReagentKitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ChemistryConfig'), _ImportedBinding__pbbase.SequencingChemistryConfig, scope=ReagentKitType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 797, 1)))

ReagentKitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reagents'), CTD_ANON_, scope=ReagentKitType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 69, 5)))

ReagentKitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentTubes'), CTD_ANON_2, scope=ReagentKitType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 76, 5)))

ReagentKitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRows'), CTD_ANON_3, scope=ReagentKitType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 83, 5)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReagentKitType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReagentKitType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reagents')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 69, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReagentKitType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentTubes')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 76, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReagentKitType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRows')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 83, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReagentKitType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ChemistryConfig')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 90, 5))
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
ReagentKitType._Automaton = _BuildAutomaton_5()




def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReagentTubeType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReagentTubeType._Automaton = _BuildAutomaton_6()




def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReagentPlateRowType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReagentPlateRowType._Automaton = _BuildAutomaton_7()




SupplyKitSequencing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentAutomationName'), pyxb.binding.datatypes.string, scope=SupplyKitSequencing, documentation='The reagent-mixing protocol used. ', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 28, 5)))

SupplyKitSequencing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentTubes'), SupplyKitSequencing, scope=SupplyKitSequencing, documentation="Tubes associated with the reagent kit - can have up to two; don't forget to set the location, 0 or 1", location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 33, 5)))

SupplyKitSequencing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingChemistry'), _ImportedBinding__pbbase.SequencingChemistry, scope=SupplyKitSequencing, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 38, 5)))

SupplyKitSequencing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitDefinition'), ReagentKitType, scope=SupplyKitSequencing, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 39, 5)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 33, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 38, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 39, 5))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 188, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 193, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentAutomationName')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentTubes')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 33, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingChemistry')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 38, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitDefinition')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioReagentKit.xsd', 39, 5))
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
SupplyKitSequencing._Automaton = _BuildAutomaton_8()

