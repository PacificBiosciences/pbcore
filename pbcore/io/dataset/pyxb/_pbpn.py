# pbcore/io/dataset/pyxb/_pbpn.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:20ebb32585e5dee1a245d71277cd3ba8c5a400aa
# Generated 2017-12-05 18:43:16.350462 by PyXB version 1.2.4 using Python 2.7.9.final.0
# Namespace http://pacificbiosciences.com/PacBioPartNumbers.xsd [xmlns:pbpn]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:35b41036-da2f-11e7-80cf-0026b9fe0a90')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _pbrk as _ImportedBinding__pbrk
import pyxb.binding.datatypes
import _pbbase as _ImportedBinding__pbbase

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://pacificbiosciences.com/PacBioPartNumbers.xsd', create_if_missing=True)
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


# Atomic simple type: {http://pacificbiosciences.com/PacBioPartNumbers.xsd}PartTypes
class PartTypes (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartTypes')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 28, 1)
    _Documentation = None
PartTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PartTypes, enum_prefix=None)
PartTypes.WFA = PartTypes._CF_enumeration.addEnumeration(unicode_value='WFA', tag='WFA')
PartTypes.BDK = PartTypes._CF_enumeration.addEnumeration(unicode_value='BDK', tag='BDK')
PartTypes.TPK = PartTypes._CF_enumeration.addEnumeration(unicode_value='TPK', tag='TPK')
PartTypes.SQK = PartTypes._CF_enumeration.addEnumeration(unicode_value='SQK', tag='SQK')
PartTypes.CCK = PartTypes._CF_enumeration.addEnumeration(unicode_value='CCK', tag='CCK')
PartTypes.CPK = PartTypes._CF_enumeration.addEnumeration(unicode_value='CPK', tag='CPK')
PartTypes.OSE = PartTypes._CF_enumeration.addEnumeration(unicode_value='OSE', tag='OSE')
PartTypes.CMO = PartTypes._CF_enumeration.addEnumeration(unicode_value='CMO', tag='CMO')
PartTypes.PRK = PartTypes._CF_enumeration.addEnumeration(unicode_value='PRK', tag='PRK')
PartTypes.Other = PartTypes._CF_enumeration.addEnumeration(unicode_value='Other', tag='Other')
PartTypes._InitializeFacetMap(PartTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PartTypes', PartTypes)

# Complex type {http://pacificbiosciences.com/PacBioPartNumbers.xsd}PacBioPartNumbersType with content type ELEMENT_ONLY
class PacBioPartNumbersType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://pacificbiosciences.com/PacBioPartNumbers.xsd}PacBioPartNumbersType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PacBioPartNumbersType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 42, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}KeyValueMap uses Python identifier KeyValueMap
    __KeyValueMap = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'KeyValueMap'), 'KeyValueMap', '__httppacificbiosciences_comPacBioPartNumbers_xsd_PacBioPartNumbersType_httppacificbiosciences_comPacBioBaseDataModel_xsdKeyValueMap', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 853, 1), )

    
    KeyValueMap = property(__KeyValueMap.value, __KeyValueMap.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}CellMaxMovieTimes uses Python identifier CellMaxMovieTimes
    __CellMaxMovieTimes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'CellMaxMovieTimes'), 'CellMaxMovieTimes', '__httppacificbiosciences_comPacBioPartNumbers_xsd_PacBioPartNumbersType_httppacificbiosciences_comPacBioBaseDataModel_xsdCellMaxMovieTimes', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 854, 1), )

    
    CellMaxMovieTimes = property(__CellMaxMovieTimes.value, __CellMaxMovieTimes.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}Automations uses Python identifier Automations
    __Automations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Automations'), 'Automations', '__httppacificbiosciences_comPacBioPartNumbers_xsd_PacBioPartNumbersType_httppacificbiosciences_comPacBioPartNumbers_xsdAutomations', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 46, 3), )

    
    Automations = property(__Automations.value, __Automations.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}BindingKits uses Python identifier BindingKits
    __BindingKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BindingKits'), 'BindingKits', '__httppacificbiosciences_comPacBioPartNumbers_xsd_PacBioPartNumbersType_httppacificbiosciences_comPacBioPartNumbers_xsdBindingKits', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 53, 3), )

    
    BindingKits = property(__BindingKits.value, __BindingKits.set, None, 'List the binding kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}TemplatePrepKits uses Python identifier TemplatePrepKits
    __TemplatePrepKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKits'), 'TemplatePrepKits', '__httppacificbiosciences_comPacBioPartNumbers_xsd_PacBioPartNumbersType_httppacificbiosciences_comPacBioPartNumbers_xsdTemplatePrepKits', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 63, 3), )

    
    TemplatePrepKits = property(__TemplatePrepKits.value, __TemplatePrepKits.set, None, 'List the sample prep kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}SequencingKits uses Python identifier SequencingKits
    __SequencingKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingKits'), 'SequencingKits', '__httppacificbiosciences_comPacBioPartNumbers_xsd_PacBioPartNumbersType_httppacificbiosciences_comPacBioPartNumbers_xsdSequencingKits', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 73, 3), )

    
    SequencingKits = property(__SequencingKits.value, __SequencingKits.set, None, 'List the sequencing kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}ControlKits uses Python identifier ControlKits
    __ControlKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlKits'), 'ControlKits', '__httppacificbiosciences_comPacBioPartNumbers_xsd_PacBioPartNumbersType_httppacificbiosciences_comPacBioPartNumbers_xsdControlKits', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 83, 3), )

    
    ControlKits = property(__ControlKits.value, __ControlKits.set, None, 'List the DNA control complex part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}CellPackKits uses Python identifier CellPackKits
    __CellPackKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CellPackKits'), 'CellPackKits', '__httppacificbiosciences_comPacBioPartNumbers_xsd_PacBioPartNumbersType_httppacificbiosciences_comPacBioPartNumbers_xsdCellPackKits', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 93, 3), )

    
    CellPackKits = property(__CellPackKits.value, __CellPackKits.set, None, 'List the cell tray part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}OtherKits uses Python identifier OtherKits
    __OtherKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OtherKits'), 'OtherKits', '__httppacificbiosciences_comPacBioPartNumbers_xsd_PacBioPartNumbersType_httppacificbiosciences_comPacBioPartNumbers_xsdOtherKits', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 103, 3), )

    
    OtherKits = property(__OtherKits.value, __OtherKits.set, None, 'A placeholder for miscellaneous parts, such as OS Enzyme tubes')

    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}IncompatibleParts uses Python identifier IncompatibleParts
    __IncompatibleParts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleParts'), 'IncompatibleParts', '__httppacificbiosciences_comPacBioPartNumbers_xsd_PacBioPartNumbersType_httppacificbiosciences_comPacBioPartNumbers_xsdIncompatibleParts', False, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 113, 3), )

    
    IncompatibleParts = property(__IncompatibleParts.value, __IncompatibleParts.set, None, None)

    _ElementMap.update({
        __KeyValueMap.name() : __KeyValueMap,
        __CellMaxMovieTimes.name() : __CellMaxMovieTimes,
        __Automations.name() : __Automations,
        __BindingKits.name() : __BindingKits,
        __TemplatePrepKits.name() : __TemplatePrepKits,
        __SequencingKits.name() : __SequencingKits,
        __ControlKits.name() : __ControlKits,
        __CellPackKits.name() : __CellPackKits,
        __OtherKits.name() : __OtherKits,
        __IncompatibleParts.name() : __IncompatibleParts
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'PacBioPartNumbersType', PacBioPartNumbersType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 47, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}Automation uses Python identifier Automation
    __Automation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Automation'), 'Automation', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_httppacificbiosciences_comPacBioPartNumbers_xsdAutomation', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 49, 6), )

    
    Automation = property(__Automation.value, __Automation.set, None, None)

    _ElementMap.update({
        __Automation.name() : __Automation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """List the binding kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 57, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}BindingKit uses Python identifier BindingKit
    __BindingKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BindingKit'), 'BindingKit', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON__httppacificbiosciences_comPacBioPartNumbers_xsdBindingKit', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 15, 1), )

    
    BindingKit = property(__BindingKit.value, __BindingKit.set, None, None)

    _ElementMap.update({
        __BindingKit.name() : __BindingKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """List the sample prep kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 67, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}TemplatePrepKit uses Python identifier TemplatePrepKit
    __TemplatePrepKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit'), 'TemplatePrepKit', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_2_httppacificbiosciences_comPacBioPartNumbers_xsdTemplatePrepKit', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 16, 1), )

    
    TemplatePrepKit = property(__TemplatePrepKit.value, __TemplatePrepKit.set, None, None)

    _ElementMap.update({
        __TemplatePrepKit.name() : __TemplatePrepKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """List the sequencing kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 77, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}SequencingKit uses Python identifier SequencingKit
    __SequencingKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit'), 'SequencingKit', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioPartNumbers_xsdSequencingKit', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 14, 1), )

    
    SequencingKit = property(__SequencingKit.value, __SequencingKit.set, None, None)

    _ElementMap.update({
        __SequencingKit.name() : __SequencingKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """List the DNA control complex part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 87, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}ControlKit uses Python identifier ControlKit
    __ControlKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlKit'), 'ControlKit', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_4_httppacificbiosciences_comPacBioPartNumbers_xsdControlKit', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 17, 1), )

    
    ControlKit = property(__ControlKit.value, __ControlKit.set, None, None)

    _ElementMap.update({
        __ControlKit.name() : __ControlKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """List the cell tray part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 97, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}CellPackKit uses Python identifier CellPackKit
    __CellPackKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CellPackKit'), 'CellPackKit', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioPartNumbers_xsdCellPackKit', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 18, 1), )

    
    CellPackKit = property(__CellPackKit.value, __CellPackKit.set, None, None)

    _ElementMap.update({
        __CellPackKit.name() : __CellPackKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """A placeholder for miscellaneous parts, such as OS Enzyme tubes"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 107, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}OtherKit uses Python identifier OtherKit
    __OtherKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OtherKit'), 'OtherKit', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_6_httppacificbiosciences_comPacBioPartNumbers_xsdOtherKit', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 19, 1), )

    
    OtherKit = property(__OtherKit.value, __OtherKit.set, None, None)

    _ElementMap.update({
        __OtherKit.name() : __OtherKit
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 114, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}IncompatiblePart uses Python identifier IncompatiblePart
    __IncompatiblePart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePart'), 'IncompatiblePart', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_7_httppacificbiosciences_comPacBioPartNumbers_xsdIncompatiblePart', True, pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 116, 6), )

    
    IncompatiblePart = property(__IncompatiblePart.value, __IncompatiblePart.set, None, None)

    _ElementMap.update({
        __IncompatiblePart.name() : __IncompatiblePart
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (_ImportedBinding__pbbase.PartNumberType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 20, 2)
    _ElementMap = _ImportedBinding__pbbase.PartNumberType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.PartNumberType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.PartNumberType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataEntityType
    
    # Element Defaults ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Defaults) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}PartNumberType
    
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
    
    # Attribute MaxCollections uses Python identifier MaxCollections
    __MaxCollections = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MaxCollections'), 'MaxCollections', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_8_MaxCollections', pyxb.binding.datatypes.int)
    __MaxCollections._DeclarationLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 23, 5)
    __MaxCollections._UseLocation = pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 23, 5)
    
    MaxCollections = property(__MaxCollections.value, __MaxCollections.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __MaxCollections.name() : __MaxCollections
    })



PacBioPartNumbers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PacBioPartNumbers'), PacBioPartNumbersType, documentation='The root element of the Part Numbers ', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 9, 1))
Namespace.addCategoryObject('elementBinding', PacBioPartNumbers.name().localName(), PacBioPartNumbers)

SequencingKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit'), _ImportedBinding__pbrk.SupplyKitSequencing, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 14, 1))
Namespace.addCategoryObject('elementBinding', SequencingKit.name().localName(), SequencingKit)

BindingKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BindingKit'), _ImportedBinding__pbbase.SupplyKitBinding, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 15, 1))
Namespace.addCategoryObject('elementBinding', BindingKit.name().localName(), BindingKit)

TemplatePrepKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit'), _ImportedBinding__pbbase.SupplyKitTemplate, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 16, 1))
Namespace.addCategoryObject('elementBinding', TemplatePrepKit.name().localName(), TemplatePrepKit)

ControlKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlKit'), _ImportedBinding__pbbase.SupplyKitControl, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 17, 1))
Namespace.addCategoryObject('elementBinding', ControlKit.name().localName(), ControlKit)

CellPackKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellPackKit'), _ImportedBinding__pbbase.SupplyKitCellPack, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 18, 1))
Namespace.addCategoryObject('elementBinding', CellPackKit.name().localName(), CellPackKit)

OtherKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherKit'), CTD_ANON_8, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 19, 1))
Namespace.addCategoryObject('elementBinding', OtherKit.name().localName(), OtherKit)



PacBioPartNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'KeyValueMap'), _ImportedBinding__pbbase.KeyValueMap_, scope=PacBioPartNumbersType, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 853, 1)))

PacBioPartNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'CellMaxMovieTimes'), _ImportedBinding__pbbase.KeyValueMap_, scope=PacBioPartNumbersType, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 854, 1)))

PacBioPartNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Automations'), CTD_ANON, scope=PacBioPartNumbersType, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 46, 3)))

PacBioPartNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BindingKits'), CTD_ANON_, scope=PacBioPartNumbersType, documentation='List the binding kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 53, 3)))

PacBioPartNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKits'), CTD_ANON_2, scope=PacBioPartNumbersType, documentation='List the sample prep kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 63, 3)))

PacBioPartNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKits'), CTD_ANON_3, scope=PacBioPartNumbersType, documentation='List the sequencing kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 73, 3)))

PacBioPartNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlKits'), CTD_ANON_4, scope=PacBioPartNumbersType, documentation='List the DNA control complex part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 83, 3)))

PacBioPartNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellPackKits'), CTD_ANON_5, scope=PacBioPartNumbersType, documentation='List the cell tray part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 93, 3)))

PacBioPartNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherKits'), CTD_ANON_6, scope=PacBioPartNumbersType, documentation='A placeholder for miscellaneous parts, such as OS Enzyme tubes', location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 103, 3)))

PacBioPartNumbersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleParts'), CTD_ANON_7, scope=PacBioPartNumbersType, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 113, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 46, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 53, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 63, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 73, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 83, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 93, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 103, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 113, 3))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PacBioPartNumbersType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'KeyValueMap')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 44, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PacBioPartNumbersType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'CellMaxMovieTimes')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 45, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PacBioPartNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Automations')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 46, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PacBioPartNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BindingKits')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 53, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PacBioPartNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKits')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 63, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PacBioPartNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingKits')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 73, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(PacBioPartNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlKits')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 83, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(PacBioPartNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellPackKits')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 93, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(PacBioPartNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OtherKits')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 103, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(PacBioPartNumbersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleParts')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 113, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PacBioPartNumbersType._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Automation'), _ImportedBinding__pbbase.AutomationType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 49, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Automation')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 49, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BindingKit'), _ImportedBinding__pbbase.SupplyKitBinding, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 15, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BindingKit')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 59, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit'), _ImportedBinding__pbbase.SupplyKitTemplate, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 16, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 69, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit'), _ImportedBinding__pbrk.SupplyKitSequencing, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 14, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 79, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_4()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlKit'), _ImportedBinding__pbbase.SupplyKitControl, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 17, 1)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlKit')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 89, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_5()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellPackKit'), _ImportedBinding__pbbase.SupplyKitCellPack, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 18, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellPackKit')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 99, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_6()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OtherKit'), CTD_ANON_8, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 19, 1)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OtherKit')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 109, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_7()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePart'), _ImportedBinding__pbbase.IncompatiblePairType, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 116, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePart')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioPartNumbers.xsd', 116, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_8()




def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 88, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 195, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 420, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 88, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'CheckSum')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 195, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Defaults')), pyxb.utils.utility.Location('/tmp/user/71303/tmpJ18jOTxsds/PacBioBaseDataModel.xsd', 420, 5))
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
CTD_ANON_8._Automaton = _BuildAutomaton_9()

