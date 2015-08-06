# ./_pbpn.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:20ebb32585e5dee1a245d71277cd3ba8c5a400aa
# Generated 2015-08-04 20:41:05.071486 by PyXB version 1.2.4 using Python 2.7.6.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:cc7f6338-3b23-11e5-875e-001a4acb6b14')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _pbbase as _ImportedBinding__pbbase
import pyxb.binding.datatypes
import _pbrk as _ImportedBinding__pbrk

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://pacificbiosciences.com/PacBioPartNumbers.xsd', create_if_missing=True)
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """The root element of the Part Numbers """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}SequencingKits uses Python identifier SequencingKits
    __SequencingKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingKits'), 'SequencingKits', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_httppacificbiosciences_comPacBioPartNumbers_xsdSequencingKits', False, pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 14, 4), )

    
    SequencingKits = property(__SequencingKits.value, __SequencingKits.set, None, 'List the sequencing kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}BindingKits uses Python identifier BindingKits
    __BindingKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BindingKits'), 'BindingKits', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_httppacificbiosciences_comPacBioPartNumbers_xsdBindingKits', False, pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 24, 4), )

    
    BindingKits = property(__BindingKits.value, __BindingKits.set, None, 'List the binding kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}TemplatePrepKits uses Python identifier TemplatePrepKits
    __TemplatePrepKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKits'), 'TemplatePrepKits', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_httppacificbiosciences_comPacBioPartNumbers_xsdTemplatePrepKits', False, pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 34, 4), )

    
    TemplatePrepKits = property(__TemplatePrepKits.value, __TemplatePrepKits.set, None, 'List the sample prep kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}ControlKits uses Python identifier ControlKits
    __ControlKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlKits'), 'ControlKits', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_httppacificbiosciences_comPacBioPartNumbers_xsdControlKits', False, pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 44, 4), )

    
    ControlKits = property(__ControlKits.value, __ControlKits.set, None, 'List the DNA control complex part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}CellPackKits uses Python identifier CellPackKits
    __CellPackKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CellPackKits'), 'CellPackKits', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_httppacificbiosciences_comPacBioPartNumbers_xsdCellPackKits', False, pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 54, 4), )

    
    CellPackKits = property(__CellPackKits.value, __CellPackKits.set, None, 'List the cell tray part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    _ElementMap.update({
        __SequencingKits.name() : __SequencingKits,
        __BindingKits.name() : __BindingKits,
        __TemplatePrepKits.name() : __TemplatePrepKits,
        __ControlKits.name() : __ControlKits,
        __CellPackKits.name() : __CellPackKits
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """List the sequencing kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 18, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}SequencingKit uses Python identifier SequencingKit
    __SequencingKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit'), 'SequencingKit', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON__httppacificbiosciences_comPacBioPartNumbers_xsdSequencingKit', True, pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 67, 1), )

    
    SequencingKit = property(__SequencingKit.value, __SequencingKit.set, None, None)

    _ElementMap.update({
        __SequencingKit.name() : __SequencingKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """List the binding kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 28, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}BindingKit uses Python identifier BindingKit
    __BindingKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BindingKit'), 'BindingKit', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_2_httppacificbiosciences_comPacBioPartNumbers_xsdBindingKit', True, pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 68, 1), )

    
    BindingKit = property(__BindingKit.value, __BindingKit.set, None, None)

    _ElementMap.update({
        __BindingKit.name() : __BindingKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """List the sample prep kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 38, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}TemplatePrepKit uses Python identifier TemplatePrepKit
    __TemplatePrepKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit'), 'TemplatePrepKit', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioPartNumbers_xsdTemplatePrepKit', True, pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 69, 1), )

    
    TemplatePrepKit = property(__TemplatePrepKit.value, __TemplatePrepKit.set, None, None)

    _ElementMap.update({
        __TemplatePrepKit.name() : __TemplatePrepKit
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 48, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}ControlKit uses Python identifier ControlKit
    __ControlKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlKit'), 'ControlKit', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_4_httppacificbiosciences_comPacBioPartNumbers_xsdControlKit', True, pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 70, 1), )

    
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 58, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioPartNumbers.xsd}CellPackKit uses Python identifier CellPackKit
    __CellPackKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CellPackKit'), 'CellPackKit', '__httppacificbiosciences_comPacBioPartNumbers_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioPartNumbers_xsdCellPackKit', True, pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 71, 1), )

    
    CellPackKit = property(__CellPackKit.value, __CellPackKit.set, None, None)

    _ElementMap.update({
        __CellPackKit.name() : __CellPackKit
    })
    _AttributeMap.update({
        
    })



PacBioPartNumbers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PacBioPartNumbers'), CTD_ANON, documentation='The root element of the Part Numbers ', location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 8, 1))
Namespace.addCategoryObject('elementBinding', PacBioPartNumbers.name().localName(), PacBioPartNumbers)

SequencingKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit'), _ImportedBinding__pbrk.SupplyKitSequencing, location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 67, 1))
Namespace.addCategoryObject('elementBinding', SequencingKit.name().localName(), SequencingKit)

BindingKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BindingKit'), _ImportedBinding__pbbase.SupplyKitBinding, location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 68, 1))
Namespace.addCategoryObject('elementBinding', BindingKit.name().localName(), BindingKit)

TemplatePrepKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit'), _ImportedBinding__pbbase.SupplyKitTemplate, location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 69, 1))
Namespace.addCategoryObject('elementBinding', TemplatePrepKit.name().localName(), TemplatePrepKit)

ControlKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlKit'), _ImportedBinding__pbbase.SupplyKitControl, location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 70, 1))
Namespace.addCategoryObject('elementBinding', ControlKit.name().localName(), ControlKit)

CellPackKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellPackKit'), _ImportedBinding__pbbase.SupplyKitCellPack, location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 71, 1))
Namespace.addCategoryObject('elementBinding', CellPackKit.name().localName(), CellPackKit)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKits'), CTD_ANON_, scope=CTD_ANON, documentation='List the sequencing kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 14, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BindingKits'), CTD_ANON_2, scope=CTD_ANON, documentation='List the binding kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 24, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKits'), CTD_ANON_3, scope=CTD_ANON, documentation='List the sample prep kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 34, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlKits'), CTD_ANON_4, scope=CTD_ANON, documentation='List the DNA control complex part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 44, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellPackKits'), CTD_ANON_5, scope=CTD_ANON, documentation='List the cell tray part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 54, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 14, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 24, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 34, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 44, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 54, 4))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingKits')), pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 14, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BindingKits')), pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 24, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKits')), pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 34, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlKits')), pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 44, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellPackKits')), pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 54, 4))
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
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit'), _ImportedBinding__pbrk.SupplyKitSequencing, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 67, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit')), pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 20, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BindingKit'), _ImportedBinding__pbbase.SupplyKitBinding, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 68, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BindingKit')), pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 30, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit'), _ImportedBinding__pbbase.SupplyKitTemplate, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 69, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit')), pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 40, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlKit'), _ImportedBinding__pbbase.SupplyKitControl, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 70, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlKit')), pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 50, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellPackKit'), _ImportedBinding__pbbase.SupplyKitCellPack, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 71, 1)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellPackKit')), pyxb.utils.utility.Location('/tmp/tmpoNuZaMxsds/PacBioPartNumbers.xsd', 60, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()

