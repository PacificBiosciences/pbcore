# pbcore/io/dataset/pyxb/_pbmeta.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:9efc6641c22b876b2d5ab7b8523f84c3396b188b
# Generated 2018-09-11 15:55:27.648503 by PyXB version 1.2.4 using Python 2.7.9.final.0
# Namespace http://pacificbiosciences.com/PacBioCollectionMetadata.xsd [xmlns:pbmeta]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:c6229580-b615-11e8-aed3-1803730e031b')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import _pbrk as _ImportedBinding__pbrk
import _pbbase as _ImportedBinding__pbbase
import _pbsample as _ImportedBinding__pbsample

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://pacificbiosciences.com/PacBioCollectionMetadata.xsd', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_pbsample = _ImportedBinding__pbsample.Namespace
_Namespace_pbsample.configureCategories(['typeBinding', 'elementBinding'])
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 410, 8)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.Pulses = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Pulses', tag='Pulses')
STD_ANON.Bases = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Bases', tag='Bases')
STD_ANON.Bases_Without_QVs = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Bases_Without_QVs', tag='Bases_Without_QVs')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 422, 8)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.Minimal = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Minimal', tag='Minimal')
STD_ANON_.High = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='High', tag='High')
STD_ANON_.None_ = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 440, 11)
    _Documentation = None
STD_ANON_2._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_2._CF_pattern.addPattern(pattern='([a-zA-Z0-9_\\-])*')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_pattern)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 450, 11)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.RSYNC = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='RSYNC', tag='RSYNC')
STD_ANON_3.SRS = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='SRS', tag='SRS')
STD_ANON_3.NFS = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='NFS', tag='NFS')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic simple type: {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}PapOutputFile
class PapOutputFile (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Defines a list of available file output types from primary output that can be copied out to the CollectionPathUri. The types Pulse, Base, Fasta, and Fastq are for legacy use only."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PapOutputFile')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 544, 1)
    _Documentation = 'Defines a list of available file output types from primary output that can be copied out to the CollectionPathUri. The types Pulse, Base, Fasta, and Fastq are for legacy use only.'
PapOutputFile._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PapOutputFile, enum_prefix=None)
PapOutputFile.None_ = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
PapOutputFile.Trace = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='Trace', tag='Trace')
PapOutputFile.Fasta = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='Fasta', tag='Fasta')
PapOutputFile.Baz = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='Baz', tag='Baz')
PapOutputFile.Bam = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='Bam', tag='Bam')
PapOutputFile.DarkFrame = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='DarkFrame', tag='DarkFrame')
PapOutputFile.StatsH5 = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='StatsH5', tag='StatsH5')
PapOutputFile._InitializeFacetMap(PapOutputFile._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PapOutputFile', PapOutputFile)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Root element of a standalone CollectionMetadata file."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 14, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}CollectionMetadata uses Python identifier CollectionMetadata
    __CollectionMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata'), 'CollectionMetadata', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_httppacificbiosciences_comPacBioCollectionMetadata_xsdCollectionMetadata', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 30, 1), )

    
    CollectionMetadata = property(__CollectionMetadata.value, __CollectionMetadata.set, None, 'Root-level element for the metadata.  The purpose of which is to contain pertinent instrument information related to the conditions present during a movie acquisition.  It also serves to provide key pieces of information for integration with primary and secondary analysis.  This file is associated with 1 movie. ')

    _ElementMap.update({
        __CollectionMetadata.name() : __CollectionMetadata
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """A set of acquisition definitions"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 24, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}CollectionMetadata uses Python identifier CollectionMetadata
    __CollectionMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata'), 'CollectionMetadata', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON__httppacificbiosciences_comPacBioCollectionMetadata_xsdCollectionMetadata', True, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 30, 1), )

    
    CollectionMetadata = property(__CollectionMetadata.value, __CollectionMetadata.set, None, 'Root-level element for the metadata.  The purpose of which is to contain pertinent instrument information related to the conditions present during a movie acquisition.  It also serves to provide key pieces of information for integration with primary and secondary analysis.  This file is associated with 1 movie. ')

    _ElementMap.update({
        __CollectionMetadata.name() : __CollectionMetadata
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Subcomponents involved in the generation of the data"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 139, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}VersionInfo uses Python identifier VersionInfo
    __VersionInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'VersionInfo'), 'VersionInfo', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_2_httppacificbiosciences_comPacBioCollectionMetadata_xsdVersionInfo', True, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 141, 9), )

    
    VersionInfo = property(__VersionInfo.value, __VersionInfo.set, None, 'Each component should list its name and version attribute')

    _ElementMap.update({
        __VersionInfo.name() : __VersionInfo
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Information related to an instrument run.  A run can contain multiple chips, wells, and movies. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 174, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}TimeStampedName uses Python identifier TimeStampedName
    __TimeStampedName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeStampedName'), 'TimeStampedName', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioCollectionMetadata_xsdTimeStampedName', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 176, 4), )

    
    TimeStampedName = property(__TimeStampedName.value, __TimeStampedName.set, None, 'A unique identifier for this run.  Format is r[sid]_[iname]_[ts]. Where [id] is a system generated id and [iname] is the instrument name and [ts] is a timestamp YYMMDD Example:  r000123_00117_100713 ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioCollectionMetadata_xsdName', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 181, 4), )

    
    Name = property(__Name.value, __Name.set, None, 'Assigned name for a run, which consists of multiple wells. There is no constraint on the uniqueness of this data. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}CreatedBy uses Python identifier CreatedBy
    __CreatedBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CreatedBy'), 'CreatedBy', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioCollectionMetadata_xsdCreatedBy', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 186, 4), )

    
    CreatedBy = property(__CreatedBy.value, __CreatedBy.set, None, 'Who created the run. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}WhenCreated uses Python identifier WhenCreated
    __WhenCreated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WhenCreated'), 'WhenCreated', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioCollectionMetadata_xsdWhenCreated', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 191, 4), )

    
    WhenCreated = property(__WhenCreated.value, __WhenCreated.set, None, 'Date and time of when the overall run was created in the system. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}StartedBy uses Python identifier StartedBy
    __StartedBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartedBy'), 'StartedBy', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioCollectionMetadata_xsdStartedBy', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 196, 4), )

    
    StartedBy = property(__StartedBy.value, __StartedBy.set, None, 'Who started the run. Could be different from who created it. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}WhenStarted uses Python identifier WhenStarted
    __WhenStarted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WhenStarted'), 'WhenStarted', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioCollectionMetadata_xsdWhenStarted', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 201, 4), )

    
    WhenStarted = property(__WhenStarted.value, __WhenStarted.set, None, 'Date and time of when the overall run was started. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}WhenCompleted uses Python identifier WhenCompleted
    __WhenCompleted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WhenCompleted'), 'WhenCompleted', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioCollectionMetadata_xsdWhenCompleted', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 206, 4), )

    
    WhenCompleted = property(__WhenCompleted.value, __WhenCompleted.set, None, 'Date and time of when the overall run was completed. ')

    _ElementMap.update({
        __TimeStampedName.name() : __TimeStampedName,
        __Name.name() : __Name,
        __CreatedBy.name() : __CreatedBy,
        __WhenCreated.name() : __WhenCreated,
        __StartedBy.name() : __StartedBy,
        __WhenStarted.name() : __WhenStarted,
        __WhenCompleted.name() : __WhenCompleted
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """A movie corresponds to one acquisition for a chip, one set (look) and one strobe. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 218, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}WhenStarted uses Python identifier WhenStarted
    __WhenStarted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WhenStarted'), 'WhenStarted', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_4_httppacificbiosciences_comPacBioCollectionMetadata_xsdWhenStarted', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 220, 4), )

    
    WhenStarted = property(__WhenStarted.value, __WhenStarted.set, None, 'Date and time of when this movie acquisition started. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}DurationInSec uses Python identifier DurationInSec
    __DurationInSec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DurationInSec'), 'DurationInSec', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_4_httppacificbiosciences_comPacBioCollectionMetadata_xsdDurationInSec', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 225, 4), )

    
    DurationInSec = property(__DurationInSec.value, __DurationInSec.set, None, 'The actual length of the movie acquisition (in seconds), irrespective of the movie duration specified by an automation parameter. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}Number uses Python identifier Number
    __Number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Number'), 'Number', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_4_httppacificbiosciences_comPacBioCollectionMetadata_xsdNumber', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 230, 4), )

    
    Number = property(__Number.value, __Number.set, None, "The number of this movie within the set (i.e., look).  This is unique when combined with the 'SetNumber'. ")

    _ElementMap.update({
        __WhenStarted.name() : __WhenStarted,
        __DurationInSec.name() : __DurationInSec,
        __Number.name() : __Number
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Container for the expired consumable data. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 242, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}TemplatePrepKitPastExpiration uses Python identifier TemplatePrepKitPastExpiration
    __TemplatePrepKitPastExpiration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKitPastExpiration'), 'TemplatePrepKitPastExpiration', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioCollectionMetadata_xsdTemplatePrepKitPastExpiration', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 244, 4), )

    
    TemplatePrepKitPastExpiration = property(__TemplatePrepKitPastExpiration.value, __TemplatePrepKitPastExpiration.set, None, 'Number of days past expiration the template prep kit was (if at all). ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}BindingKitPastExpiration uses Python identifier BindingKitPastExpiration
    __BindingKitPastExpiration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BindingKitPastExpiration'), 'BindingKitPastExpiration', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioCollectionMetadata_xsdBindingKitPastExpiration', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 249, 4), )

    
    BindingKitPastExpiration = property(__BindingKitPastExpiration.value, __BindingKitPastExpiration.set, None, 'Number of days past expiration the binding kit was (if at all). ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}CellPacPastExpiration uses Python identifier CellPacPastExpiration
    __CellPacPastExpiration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CellPacPastExpiration'), 'CellPacPastExpiration', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioCollectionMetadata_xsdCellPacPastExpiration', True, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 254, 4), )

    
    CellPacPastExpiration = property(__CellPacPastExpiration.value, __CellPacPastExpiration.set, None, 'Number of days past expiration the cell pac was (if at all). ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}SequencingKitPastExpiration uses Python identifier SequencingKitPastExpiration
    __SequencingKitPastExpiration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitPastExpiration'), 'SequencingKitPastExpiration', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioCollectionMetadata_xsdSequencingKitPastExpiration', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 264, 4), )

    
    SequencingKitPastExpiration = property(__SequencingKitPastExpiration.value, __SequencingKitPastExpiration.set, None, 'Number of days past expiration the reagent kit was (if at all). ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}SequencingTube0PastExpiration uses Python identifier SequencingTube0PastExpiration
    __SequencingTube0PastExpiration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingTube0PastExpiration'), 'SequencingTube0PastExpiration', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioCollectionMetadata_xsdSequencingTube0PastExpiration', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 269, 4), )

    
    SequencingTube0PastExpiration = property(__SequencingTube0PastExpiration.value, __SequencingTube0PastExpiration.set, None, 'Number of days past expiration the reagent tube 0 was (if at all). ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}SequencingTube1PastExpiration uses Python identifier SequencingTube1PastExpiration
    __SequencingTube1PastExpiration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingTube1PastExpiration'), 'SequencingTube1PastExpiration', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioCollectionMetadata_xsdSequencingTube1PastExpiration', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 274, 4), )

    
    SequencingTube1PastExpiration = property(__SequencingTube1PastExpiration.value, __SequencingTube1PastExpiration.set, None, 'Number of days past expiration the reagent tube 1 was (if at all). ')

    _ElementMap.update({
        __TemplatePrepKitPastExpiration.name() : __TemplatePrepKitPastExpiration,
        __BindingKitPastExpiration.name() : __BindingKitPastExpiration,
        __CellPacPastExpiration.name() : __CellPacPastExpiration,
        __SequencingKitPastExpiration.name() : __SequencingKitPastExpiration,
        __SequencingTube0PastExpiration.name() : __SequencingTube0PastExpiration,
        __SequencingTube1PastExpiration.name() : __SequencingTube1PastExpiration
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Container for the primary analysis related data. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 346, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}SampleTrace uses Python identifier SampleTrace
    __SampleTrace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SampleTrace'), 'SampleTrace', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_6_httppacificbiosciences_comPacBioCollectionMetadata_xsdSampleTrace', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 348, 4), )

    
    SampleTrace = property(__SampleTrace.value, __SampleTrace.set, None, 'Tag to indicate that the trace file will be sampled. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}AutomationName uses Python identifier AutomationName
    __AutomationName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationName'), 'AutomationName', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_6_httppacificbiosciences_comPacBioCollectionMetadata_xsdAutomationName', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 367, 4), )

    
    AutomationName = property(__AutomationName.value, __AutomationName.set, None, 'Name of primary analysis protocol. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}ConfigFileName uses Python identifier ConfigFileName
    __ConfigFileName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ConfigFileName'), 'ConfigFileName', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_6_httppacificbiosciences_comPacBioCollectionMetadata_xsdConfigFileName', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 372, 8), )

    
    ConfigFileName = property(__ConfigFileName.value, __ConfigFileName.set, None, 'Name of primary analysis config file. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}SequencingCondition uses Python identifier SequencingCondition
    __SequencingCondition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingCondition'), 'SequencingCondition', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_6_httppacificbiosciences_comPacBioCollectionMetadata_xsdSequencingCondition', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 377, 4), )

    
    SequencingCondition = property(__SequencingCondition.value, __SequencingCondition.set, None, 'A sequencing condition tag to be used by primary analysis, e.g., to select basecaller calibration or training parameters. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}OutputOptions uses Python identifier OutputOptions
    __OutputOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OutputOptions'), 'OutputOptions', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_6_httppacificbiosciences_comPacBioCollectionMetadata_xsdOutputOptions', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 382, 4), )

    
    OutputOptions = property(__OutputOptions.value, __OutputOptions.set, None, None)

    _ElementMap.update({
        __SampleTrace.name() : __SampleTrace,
        __AutomationName.name() : __AutomationName,
        __ConfigFileName.name() : __ConfigFileName,
        __SequencingCondition.name() : __SequencingCondition,
        __OutputOptions.name() : __OutputOptions
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Tag to indicate that the trace file will be sampled. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 352, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}TraceSamplingFactor uses Python identifier TraceSamplingFactor
    __TraceSamplingFactor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TraceSamplingFactor'), 'TraceSamplingFactor', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_7_httppacificbiosciences_comPacBioCollectionMetadata_xsdTraceSamplingFactor', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 354, 7), )

    
    TraceSamplingFactor = property(__TraceSamplingFactor.value, __TraceSamplingFactor.set, None, 'Percentage of traces to sample. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}FullPulseFile uses Python identifier FullPulseFile
    __FullPulseFile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FullPulseFile'), 'FullPulseFile', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_7_httppacificbiosciences_comPacBioCollectionMetadata_xsdFullPulseFile', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 359, 7), )

    
    FullPulseFile = property(__FullPulseFile.value, __FullPulseFile.set, None, 'Whether full or sampled pulse file is transferred if requested. ')

    _ElementMap.update({
        __TraceSamplingFactor.name() : __TraceSamplingFactor,
        __FullPulseFile.name() : __FullPulseFile
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 383, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}ResultsFolder uses Python identifier ResultsFolder
    __ResultsFolder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResultsFolder'), 'ResultsFolder', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_8_httppacificbiosciences_comPacBioCollectionMetadata_xsdResultsFolder', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 385, 7), )

    
    ResultsFolder = property(__ResultsFolder.value, __ResultsFolder.set, None, "NOTE: not for customers. A sub-folder under the CollectionPath created by Primary Analysis. This is a field that will be updated by the primary analysis pipeline.  The default (as created by homer) should be set to 'Reports_Sms' for now.  Consumers of the data should be aware that they will find collection metadata (and trace files if acquisition is so-configured) at the CollectionPathUri, and all primary analysis results in the sub-folder PrimaryResultsFolder. ")

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}CollectionPathUri uses Python identifier CollectionPathUri
    __CollectionPathUri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollectionPathUri'), 'CollectionPathUri', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_8_httppacificbiosciences_comPacBioCollectionMetadata_xsdCollectionPathUri', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 390, 7), )

    
    CollectionPathUri = property(__CollectionPathUri.value, __CollectionPathUri.set, None, 'User-specified location of where the results should be copied after an analysis has been completed. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}CopyFiles uses Python identifier CopyFiles
    __CopyFiles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CopyFiles'), 'CopyFiles', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_8_httppacificbiosciences_comPacBioCollectionMetadata_xsdCopyFiles', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 395, 7), )

    
    CopyFiles = property(__CopyFiles.value, __CopyFiles.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}Readout uses Python identifier Readout
    __Readout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Readout'), 'Readout', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_8_httppacificbiosciences_comPacBioCollectionMetadata_xsdReadout', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 406, 7), )

    
    Readout = property(__Readout.value, __Readout.set, None, 'BazIO Readout option; valid values are Bases (default) and Pulses')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}MetricsVerbosity uses Python identifier MetricsVerbosity
    __MetricsVerbosity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MetricsVerbosity'), 'MetricsVerbosity', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_8_httppacificbiosciences_comPacBioCollectionMetadata_xsdMetricsVerbosity', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 418, 7), )

    
    MetricsVerbosity = property(__MetricsVerbosity.value, __MetricsVerbosity.set, None, 'BazIO MetricsVerbosity option; valid values are Minimal (default), High, and None')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}TransferResource uses Python identifier TransferResource
    __TransferResource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TransferResource'), 'TransferResource', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_8_httppacificbiosciences_comPacBioCollectionMetadata_xsdTransferResource', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 430, 7), )

    
    TransferResource = property(__TransferResource.value, __TransferResource.set, None, 'Transfer Resource (optional for now, but will be made required when ICS implements this)')

    _ElementMap.update({
        __ResultsFolder.name() : __ResultsFolder,
        __CollectionPathUri.name() : __CollectionPathUri,
        __CopyFiles.name() : __CopyFiles,
        __Readout.name() : __Readout,
        __MetricsVerbosity.name() : __MetricsVerbosity,
        __TransferResource.name() : __TransferResource
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 396, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}CollectionFileCopy uses Python identifier CollectionFileCopy
    __CollectionFileCopy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollectionFileCopy'), 'CollectionFileCopy', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_9_httppacificbiosciences_comPacBioCollectionMetadata_xsdCollectionFileCopy', True, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 398, 10), )

    
    CollectionFileCopy = property(__CollectionFileCopy.value, __CollectionFileCopy.set, None, 'Defines the set of files to be copied to the CollectionPathUri. 1 or more. ')

    _ElementMap.update({
        __CollectionFileCopy.name() : __CollectionFileCopy
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Transfer Resource (optional for now, but will be made required when ICS implements this)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 434, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_10_httppacificbiosciences_comPacBioCollectionMetadata_xsdId', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 436, 10), )

    
    Id = property(__Id.value, __Id.set, None, 'Id of the Transfer Resource that is unique to the Scheme Type. A tuple of (TransferScheme, Id) will be globally unique')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}TransferScheme uses Python identifier TransferScheme
    __TransferScheme = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TransferScheme'), 'TransferScheme', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_10_httppacificbiosciences_comPacBioCollectionMetadata_xsdTransferScheme', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 446, 10), )

    
    TransferScheme = property(__TransferScheme.value, __TransferScheme.set, None, 'Transfer Scheme type (this should be an enum Scheme of rsync, srs or nfs)')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_10_httppacificbiosciences_comPacBioCollectionMetadata_xsdName', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 458, 10), )

    
    Name = property(__Name.value, __Name.set, None, 'Display Name of the Transfer Resource')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Description'), 'Description', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_10_httppacificbiosciences_comPacBioCollectionMetadata_xsdDescription', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 463, 10), )

    
    Description = property(__Description.value, __Description.set, None, 'Description of the Transfer Resource')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}DestPath uses Python identifier DestPath
    __DestPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DestPath'), 'DestPath', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_10_httppacificbiosciences_comPacBioCollectionMetadata_xsdDestPath', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 468, 10), )

    
    DestPath = property(__DestPath.value, __DestPath.set, None, 'Remote Root Destination Path of the Transfer Resource')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}RelativePath uses Python identifier RelativePath
    __RelativePath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RelativePath'), 'RelativePath', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_10_httppacificbiosciences_comPacBioCollectionMetadata_xsdRelativePath', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 473, 10), )

    
    RelativePath = property(__RelativePath.value, __RelativePath.set, None, 'Remote Relative Path of the Transfer Resource')

    _ElementMap.update({
        __Id.name() : __Id,
        __TransferScheme.name() : __TransferScheme,
        __Name.name() : __Name,
        __Description.name() : __Description,
        __DestPath.name() : __DestPath,
        __RelativePath.name() : __RelativePath
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Container for the primary analysis related data. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 492, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}AutomationName uses Python identifier AutomationName
    __AutomationName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationName'), 'AutomationName', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_11_httppacificbiosciences_comPacBioCollectionMetadata_xsdAutomationName', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 494, 4), )

    
    AutomationName = property(__AutomationName.value, __AutomationName.set, None, 'The secondary analysis protocol name specified in the sample sheet. Ignored by secondary. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}AutomationParameters uses Python identifier AutomationParameters
    __AutomationParameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameters'), 'AutomationParameters', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_11_httppacificbiosciences_comPacBioCollectionMetadata_xsdAutomationParameters', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 499, 4), )

    
    AutomationParameters = property(__AutomationParameters.value, __AutomationParameters.set, None, 'The parameters for secondary analysis specified in the sample sheet. Ignored by secondary. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}CellCountInJob uses Python identifier CellCountInJob
    __CellCountInJob = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CellCountInJob'), 'CellCountInJob', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_11_httppacificbiosciences_comPacBioCollectionMetadata_xsdCellCountInJob', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 513, 4), )

    
    CellCountInJob = property(__CellCountInJob.value, __CellCountInJob.set, None, "The number of cells in this secondary analysis job, identified by the secondary analysis parameter 'JobName'.  Supports automated secondary analysis. ")

    _ElementMap.update({
        __AutomationName.name() : __AutomationName,
        __AutomationParameters.name() : __AutomationParameters,
        __CellCountInJob.name() : __CellCountInJob
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """The parameters for secondary analysis specified in the sample sheet. Ignored by secondary. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 503, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}AutomationParameter uses Python identifier AutomationParameter
    __AutomationParameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter'), 'AutomationParameter', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_12_httppacificbiosciences_comPacBioCollectionMetadata_xsdAutomationParameter', True, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 505, 7), )

    
    AutomationParameter = property(__AutomationParameter.value, __AutomationParameter.set, None, 'One or more secondary analysis parameters, such as JobName, Workflow, etc..')

    _ElementMap.update({
        __AutomationParameter.name() : __AutomationParameter
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """One custom, possibly non-unique, key-value pair. """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 531, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute key uses Python identifier key
    __key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'key'), 'key', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_13_key', pyxb.binding.datatypes.string, required=True)
    __key._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 534, 5)
    __key._UseLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 534, 5)
    
    key = property(__key.value, __key.set, None, 'Key (attribute) and Value (element content). ')

    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_13_label', pyxb.binding.datatypes.string)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 539, 5)
    __label._UseLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 539, 5)
    
    label = property(__label.value, __label.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __key.name() : __key,
        __label.name() : __label
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (_ImportedBinding__pbbase.BaseEntityType):
    """Container for the sample related data. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 286, 2)
    _ElementMap = _ImportedBinding__pbbase.BaseEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.BaseEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}WellName uses Python identifier WellName
    __WellName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WellName'), 'WellName', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_14_httppacificbiosciences_comPacBioCollectionMetadata_xsdWellName', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 290, 6), )

    
    WellName = property(__WellName.value, __WellName.set, None, 'Identifies which well this sample came from (e.g., coordinate on a plate). ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}Concentration uses Python identifier Concentration
    __Concentration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Concentration'), 'Concentration', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_14_httppacificbiosciences_comPacBioCollectionMetadata_xsdConcentration', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 295, 6), )

    
    Concentration = property(__Concentration.value, __Concentration.set, None, 'Sample input concentration. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}OnPlateLoadingConcentration uses Python identifier OnPlateLoadingConcentration
    __OnPlateLoadingConcentration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OnPlateLoadingConcentration'), 'OnPlateLoadingConcentration', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_14_httppacificbiosciences_comPacBioCollectionMetadata_xsdOnPlateLoadingConcentration', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 300, 24), )

    
    OnPlateLoadingConcentration = property(__OnPlateLoadingConcentration.value, __OnPlateLoadingConcentration.set, None, 'On plate loading concentration. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}InsertSize uses Python identifier InsertSize
    __InsertSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InsertSize'), 'InsertSize', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_14_httppacificbiosciences_comPacBioCollectionMetadata_xsdInsertSize', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 305, 6), )

    
    InsertSize = property(__InsertSize.value, __InsertSize.set, None, 'Length of the sheared template, e.g. 500, 2000, 30000')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}SampleReuseEnabled uses Python identifier SampleReuseEnabled
    __SampleReuseEnabled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SampleReuseEnabled'), 'SampleReuseEnabled', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_14_httppacificbiosciences_comPacBioCollectionMetadata_xsdSampleReuseEnabled', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 310, 6), )

    
    SampleReuseEnabled = property(__SampleReuseEnabled.value, __SampleReuseEnabled.set, None, 'Whether or not complex reuse is enabled for this well. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}StageHotstartEnabled uses Python identifier StageHotstartEnabled
    __StageHotstartEnabled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StageHotstartEnabled'), 'StageHotstartEnabled', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_14_httppacificbiosciences_comPacBioCollectionMetadata_xsdStageHotstartEnabled', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 315, 6), )

    
    StageHotstartEnabled = property(__StageHotstartEnabled.value, __StageHotstartEnabled.set, None, 'Whether or not hotstart at the stage is enabled for this well. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}SizeSelectionEnabled uses Python identifier SizeSelectionEnabled
    __SizeSelectionEnabled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SizeSelectionEnabled'), 'SizeSelectionEnabled', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_14_httppacificbiosciences_comPacBioCollectionMetadata_xsdSizeSelectionEnabled', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 320, 6), )

    
    SizeSelectionEnabled = property(__SizeSelectionEnabled.value, __SizeSelectionEnabled.set, None, 'Whether or not size selection is enabled for this well. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}UseCount uses Python identifier UseCount
    __UseCount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UseCount'), 'UseCount', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_14_httppacificbiosciences_comPacBioCollectionMetadata_xsdUseCount', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 325, 6), )

    
    UseCount = property(__UseCount.value, __UseCount.set, None, 'Count of usages for this batch of complex. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}DNAControlComplex uses Python identifier DNAControlComplex
    __DNAControlComplex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DNAControlComplex'), 'DNAControlComplex', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_14_httppacificbiosciences_comPacBioCollectionMetadata_xsdDNAControlComplex', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 330, 6), )

    
    DNAControlComplex = property(__DNAControlComplex.value, __DNAControlComplex.set, None, 'Indicating what kind (if any) control was used. ')

    
    # Element {http://pacificbiosciences.com/PacBioSampleInfo.xsd}BioSamples uses Python identifier BioSamples
    __BioSamples = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_pbsample, 'BioSamples'), 'BioSamples', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_14_httppacificbiosciences_comPacBioSampleInfo_xsdBioSamples', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioSampleInfo.xsd', 126, 1), )

    
    BioSamples = property(__BioSamples.value, __BioSamples.set, None, 'List of biological samples.')

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __WellName.name() : __WellName,
        __Concentration.name() : __Concentration,
        __OnPlateLoadingConcentration.name() : __OnPlateLoadingConcentration,
        __InsertSize.name() : __InsertSize,
        __SampleReuseEnabled.name() : __SampleReuseEnabled,
        __StageHotstartEnabled.name() : __StageHotstartEnabled,
        __SizeSelectionEnabled.name() : __SizeSelectionEnabled,
        __UseCount.name() : __UseCount,
        __DNAControlComplex.name() : __DNAControlComplex,
        __BioSamples.name() : __BioSamples
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (_ImportedBinding__pbbase.StrictEntityType):
    """Root-level element for the metadata.  The purpose of which is to contain pertinent instrument information related to the conditions present during a movie acquisition.  It also serves to provide key pieces of information for integration with primary and secondary analysis.  This file is associated with 1 movie. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 34, 2)
    _ElementMap = _ImportedBinding__pbbase.StrictEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.StrictEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.StrictEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}InstCtrlVer uses Python identifier InstCtrlVer
    __InstCtrlVer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstCtrlVer'), 'InstCtrlVer', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdInstCtrlVer', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 38, 6), )

    
    InstCtrlVer = property(__InstCtrlVer.value, __InstCtrlVer.set, None, 'Instrument control software version. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}SigProcVer uses Python identifier SigProcVer
    __SigProcVer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SigProcVer'), 'SigProcVer', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdSigProcVer', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 43, 6), )

    
    SigProcVer = property(__SigProcVer.value, __SigProcVer.set, None, 'Signal processing software version. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}Automation uses Python identifier Automation
    __Automation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Automation'), 'Automation', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdAutomation', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 65, 6), )

    
    Automation = property(__Automation.value, __Automation.set, None, 'Defines the collection workflow (e.g., robotic movement, movie acquisition) for a particular cell. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}CollectionNumber uses Python identifier CollectionNumber
    __CollectionNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollectionNumber'), 'CollectionNumber', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdCollectionNumber', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 70, 6), )

    
    CollectionNumber = property(__CollectionNumber.value, __CollectionNumber.set, None, 'Collection number for this plate well. Sample from one plate well or tube can be distributed to more than one cell. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}CellIndex uses Python identifier CellIndex
    __CellIndex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CellIndex'), 'CellIndex', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdCellIndex', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 75, 6), )

    
    CellIndex = property(__CellIndex.value, __CellIndex.set, None, 'The zero-based index of this particular cell within the cell tray.  Likely to be in the range of [0-3]')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}SetNumber uses Python identifier SetNumber
    __SetNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SetNumber'), 'SetNumber', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdSetNumber', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 80, 6), )

    
    SetNumber = property(__SetNumber.value, __SetNumber.set, None, 'Formerly known as the look number.  1 - N.  Defaults to 1. 0 if the look is unknown. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}CellPac uses Python identifier CellPac
    __CellPac = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CellPac'), 'CellPac', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdCellPac', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 85, 6), )

    
    CellPac = property(__CellPac.value, __CellPac.set, None, 'The SMRT cell packaging supply information. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}ControlKit uses Python identifier ControlKit
    __ControlKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlKit'), 'ControlKit', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdControlKit', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 90, 6), )

    
    ControlKit = property(__ControlKit.value, __ControlKit.set, None, 'Defines the DNA control used for this experiment. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}TemplatePrepKit uses Python identifier TemplatePrepKit
    __TemplatePrepKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit'), 'TemplatePrepKit', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdTemplatePrepKit', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 95, 6), )

    
    TemplatePrepKit = property(__TemplatePrepKit.value, __TemplatePrepKit.set, None, 'Defines the template (sample) prep kit used for this experiment. Can be used to get back to the primary and adapter used. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}BindingKit uses Python identifier BindingKit
    __BindingKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BindingKit'), 'BindingKit', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdBindingKit', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 100, 6), )

    
    BindingKit = property(__BindingKit.value, __BindingKit.set, None, 'The binding kit supply information. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}SequencingKitPlate uses Python identifier SequencingKitPlate
    __SequencingKitPlate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitPlate'), 'SequencingKitPlate', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdSequencingKitPlate', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 105, 6), )

    
    SequencingKitPlate = property(__SequencingKitPlate.value, __SequencingKitPlate.set, None, 'The sequencing kit supply information. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}WashKitPlate uses Python identifier WashKitPlate
    __WashKitPlate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WashKitPlate'), 'WashKitPlate', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdWashKitPlate', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 110, 6), )

    
    WashKitPlate = property(__WashKitPlate.value, __WashKitPlate.set, None, 'The wash kit supply information. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}ComponentVersions uses Python identifier ComponentVersions
    __ComponentVersions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ComponentVersions'), 'ComponentVersions', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdComponentVersions', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 135, 6), )

    
    ComponentVersions = property(__ComponentVersions.value, __ComponentVersions.set, None, 'Subcomponents involved in the generation of the data')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}RunDetails uses Python identifier RunDetails
    __RunDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RunDetails'), 'RunDetails', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdRunDetails', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 170, 1), )

    
    RunDetails = property(__RunDetails.value, __RunDetails.set, None, 'Information related to an instrument run.  A run can contain multiple chips, wells, and movies. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}Movie uses Python identifier Movie
    __Movie = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Movie'), 'Movie', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdMovie', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 214, 1), )

    
    Movie = property(__Movie.value, __Movie.set, None, 'A movie corresponds to one acquisition for a chip, one set (look) and one strobe. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}ExpirationData uses Python identifier ExpirationData
    __ExpirationData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExpirationData'), 'ExpirationData', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdExpirationData', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 238, 1), )

    
    ExpirationData = property(__ExpirationData.value, __ExpirationData.set, None, 'Container for the expired consumable data. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}WellSample uses Python identifier WellSample
    __WellSample = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WellSample'), 'WellSample', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdWellSample', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 282, 1), )

    
    WellSample = property(__WellSample.value, __WellSample.set, None, 'Container for the sample related data. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}Primary uses Python identifier Primary
    __Primary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Primary'), 'Primary', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdPrimary', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 342, 1), )

    
    Primary = property(__Primary.value, __Primary.set, None, 'Container for the primary analysis related data. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}Secondary uses Python identifier Secondary
    __Secondary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Secondary'), 'Secondary', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdSecondary', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 488, 1), )

    
    Secondary = property(__Secondary.value, __Secondary.set, None, 'Container for the primary analysis related data. ')

    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}UserDefinedFields uses Python identifier UserDefinedFields
    __UserDefinedFields = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UserDefinedFields'), 'UserDefinedFields', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioCollectionMetadata_xsdUserDefinedFields', False, pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 522, 1), )

    
    UserDefinedFields = property(__UserDefinedFields.value, __UserDefinedFields.set, None, 'A set of key-value pairs specified by a user via the run input mechanism. Note that uniqueness of keys is not enforced here and so may contain duplicate keys. ')

    
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
    
    # Attribute Context uses Python identifier Context
    __Context = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Context'), 'Context', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_Context', pyxb.binding.datatypes.string)
    __Context._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 150, 5)
    __Context._UseLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 150, 5)
    
    Context = property(__Context.value, __Context.set, None, 'Replace with TimeStampedName')

    
    # Attribute Status uses Python identifier Status
    __Status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Status'), 'Status', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_Status', _ImportedBinding__pbbase.SupportedAcquisitionStates)
    __Status._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 155, 5)
    __Status._UseLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 155, 5)
    
    Status = property(__Status.value, __Status.set, None, None)

    
    # Attribute InstrumentId uses Python identifier InstrumentId
    __InstrumentId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'InstrumentId'), 'InstrumentId', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_InstrumentId', pyxb.binding.datatypes.string)
    __InstrumentId._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 156, 5)
    __InstrumentId._UseLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 156, 5)
    
    InstrumentId = property(__InstrumentId.value, __InstrumentId.set, None, 'World unique id assigned by PacBio. ')

    
    # Attribute InstrumentName uses Python identifier InstrumentName
    __InstrumentName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'InstrumentName'), 'InstrumentName', '__httppacificbiosciences_comPacBioCollectionMetadata_xsd_CTD_ANON_15_InstrumentName', pyxb.binding.datatypes.string)
    __InstrumentName._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 161, 5)
    __InstrumentName._UseLocation = pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 161, 5)
    
    InstrumentName = property(__InstrumentName.value, __InstrumentName.set, None, 'Friendly name assigned by customer')

    _ElementMap.update({
        __InstCtrlVer.name() : __InstCtrlVer,
        __SigProcVer.name() : __SigProcVer,
        __Automation.name() : __Automation,
        __CollectionNumber.name() : __CollectionNumber,
        __CellIndex.name() : __CellIndex,
        __SetNumber.name() : __SetNumber,
        __CellPac.name() : __CellPac,
        __ControlKit.name() : __ControlKit,
        __TemplatePrepKit.name() : __TemplatePrepKit,
        __BindingKit.name() : __BindingKit,
        __SequencingKitPlate.name() : __SequencingKitPlate,
        __WashKitPlate.name() : __WashKitPlate,
        __ComponentVersions.name() : __ComponentVersions,
        __RunDetails.name() : __RunDetails,
        __Movie.name() : __Movie,
        __ExpirationData.name() : __ExpirationData,
        __WellSample.name() : __WellSample,
        __Primary.name() : __Primary,
        __Secondary.name() : __Secondary,
        __UserDefinedFields.name() : __UserDefinedFields
    })
    _AttributeMap.update({
        __Context.name() : __Context,
        __Status.name() : __Status,
        __InstrumentId.name() : __InstrumentId,
        __InstrumentName.name() : __InstrumentName
    })



PacBioCollectionMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PacBioCollectionMetadata'), CTD_ANON, documentation='Root element of a standalone CollectionMetadata file.', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 10, 1))
Namespace.addCategoryObject('elementBinding', PacBioCollectionMetadata.name().localName(), PacBioCollectionMetadata)

Collections = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Collections'), CTD_ANON_, documentation='A set of acquisition definitions', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 20, 1))
Namespace.addCategoryObject('elementBinding', Collections.name().localName(), Collections)

RunDetails = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RunDetails'), CTD_ANON_3, documentation='Information related to an instrument run.  A run can contain multiple chips, wells, and movies. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 170, 1))
Namespace.addCategoryObject('elementBinding', RunDetails.name().localName(), RunDetails)

Movie = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Movie'), CTD_ANON_4, documentation='A movie corresponds to one acquisition for a chip, one set (look) and one strobe. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 214, 1))
Namespace.addCategoryObject('elementBinding', Movie.name().localName(), Movie)

ExpirationData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExpirationData'), CTD_ANON_5, documentation='Container for the expired consumable data. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 238, 1))
Namespace.addCategoryObject('elementBinding', ExpirationData.name().localName(), ExpirationData)

Primary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Primary'), CTD_ANON_6, documentation='Container for the primary analysis related data. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 342, 1))
Namespace.addCategoryObject('elementBinding', Primary.name().localName(), Primary)

Secondary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Secondary'), CTD_ANON_11, documentation='Container for the primary analysis related data. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 488, 1))
Namespace.addCategoryObject('elementBinding', Secondary.name().localName(), Secondary)

UserDefinedFields = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UserDefinedFields'), _ImportedBinding__pbbase.UserDefinedFieldsType, documentation='A set of key-value pairs specified by a user via the run input mechanism. Note that uniqueness of keys is not enforced here and so may contain duplicate keys. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 522, 1))
Namespace.addCategoryObject('elementBinding', UserDefinedFields.name().localName(), UserDefinedFields)

KeyValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KeyValue'), CTD_ANON_13, documentation='One custom, possibly non-unique, key-value pair. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 527, 1))
Namespace.addCategoryObject('elementBinding', KeyValue.name().localName(), KeyValue)

WellSample = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WellSample'), CTD_ANON_14, documentation='Container for the sample related data. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 282, 1))
Namespace.addCategoryObject('elementBinding', WellSample.name().localName(), WellSample)

CollectionMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata'), CTD_ANON_15, documentation='Root-level element for the metadata.  The purpose of which is to contain pertinent instrument information related to the conditions present during a movie acquisition.  It also serves to provide key pieces of information for integration with primary and secondary analysis.  This file is associated with 1 movie. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 30, 1))
Namespace.addCategoryObject('elementBinding', CollectionMetadata.name().localName(), CollectionMetadata)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata'), CTD_ANON_15, scope=CTD_ANON, documentation='Root-level element for the metadata.  The purpose of which is to contain pertinent instrument information related to the conditions present during a movie acquisition.  It also serves to provide key pieces of information for integration with primary and secondary analysis.  This file is associated with 1 movie. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 30, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 16, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata'), CTD_ANON_15, scope=CTD_ANON_, documentation='Root-level element for the metadata.  The purpose of which is to contain pertinent instrument information related to the conditions present during a movie acquisition.  It also serves to provide key pieces of information for integration with primary and secondary analysis.  This file is associated with 1 movie. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 30, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 26, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'VersionInfo'), _ImportedBinding__pbbase.BaseEntityType, scope=CTD_ANON_2, documentation='Each component should list its name and version attribute', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 141, 9)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'VersionInfo')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 141, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeStampedName'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, documentation='A unique identifier for this run.  Format is r[sid]_[iname]_[ts]. Where [id] is a system generated id and [iname] is the instrument name and [ts] is a timestamp YYMMDD Example:  r000123_00117_100713 ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 176, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, documentation='Assigned name for a run, which consists of multiple wells. There is no constraint on the uniqueness of this data. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 181, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CreatedBy'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, documentation='Who created the run. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 186, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WhenCreated'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_3, documentation='Date and time of when the overall run was created in the system. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 191, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartedBy'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, documentation='Who started the run. Could be different from who created it. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 196, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WhenStarted'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_3, documentation='Date and time of when the overall run was started. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 201, 4)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WhenCompleted'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_3, documentation='Date and time of when the overall run was completed. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 206, 4)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 181, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 186, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 191, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 196, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 201, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 206, 4))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeStampedName')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 176, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 181, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CreatedBy')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 186, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WhenCreated')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 191, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartedBy')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 196, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WhenStarted')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 201, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WhenCompleted')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 206, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
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
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
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
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WhenStarted'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_4, documentation='Date and time of when this movie acquisition started. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 220, 4)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DurationInSec'), pyxb.binding.datatypes.int, scope=CTD_ANON_4, documentation='The actual length of the movie acquisition (in seconds), irrespective of the movie duration specified by an automation parameter. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 225, 4), unicode_default='0'))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Number'), pyxb.binding.datatypes.int, scope=CTD_ANON_4, documentation="The number of this movie within the set (i.e., look).  This is unique when combined with the 'SetNumber'. ", location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 230, 4), unicode_default='0'))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WhenStarted')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 220, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DurationInSec')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 225, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Number')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 230, 4))
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
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKitPastExpiration'), pyxb.binding.datatypes.int, scope=CTD_ANON_5, documentation='Number of days past expiration the template prep kit was (if at all). ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 244, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BindingKitPastExpiration'), pyxb.binding.datatypes.int, scope=CTD_ANON_5, documentation='Number of days past expiration the binding kit was (if at all). ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 249, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellPacPastExpiration'), pyxb.binding.datatypes.int, scope=CTD_ANON_5, documentation='Number of days past expiration the cell pac was (if at all). ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 254, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitPastExpiration'), pyxb.binding.datatypes.int, scope=CTD_ANON_5, documentation='Number of days past expiration the reagent kit was (if at all). ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 264, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingTube0PastExpiration'), pyxb.binding.datatypes.int, scope=CTD_ANON_5, documentation='Number of days past expiration the reagent tube 0 was (if at all). ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 269, 4)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingTube1PastExpiration'), pyxb.binding.datatypes.int, scope=CTD_ANON_5, documentation='Number of days past expiration the reagent tube 1 was (if at all). ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 274, 4)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKitPastExpiration')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 244, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BindingKitPastExpiration')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 249, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellPacPastExpiration')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 254, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellPacPastExpiration')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 259, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitPastExpiration')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 264, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingTube0PastExpiration')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 269, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingTube1PastExpiration')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 274, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
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
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleTrace'), CTD_ANON_7, scope=CTD_ANON_6, documentation='Tag to indicate that the trace file will be sampled. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 348, 4)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationName'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, documentation='Name of primary analysis protocol. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 367, 4)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConfigFileName'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, documentation='Name of primary analysis config file. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 372, 8)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingCondition'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, documentation='A sequencing condition tag to be used by primary analysis, e.g., to select basecaller calibration or training parameters. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 377, 4)))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OutputOptions'), CTD_ANON_8, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 382, 4)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 348, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 372, 8))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SampleTrace')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 348, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationName')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 367, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ConfigFileName')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 372, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingCondition')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 377, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OutputOptions')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 382, 4))
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
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TraceSamplingFactor'), pyxb.binding.datatypes.float, scope=CTD_ANON_7, documentation='Percentage of traces to sample. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 354, 7)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FullPulseFile'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_7, documentation='Whether full or sampled pulse file is transferred if requested. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 359, 7)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TraceSamplingFactor')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 354, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FullPulseFile')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 359, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResultsFolder'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, documentation="NOTE: not for customers. A sub-folder under the CollectionPath created by Primary Analysis. This is a field that will be updated by the primary analysis pipeline.  The default (as created by homer) should be set to 'Reports_Sms' for now.  Consumers of the data should be aware that they will find collection metadata (and trace files if acquisition is so-configured) at the CollectionPathUri, and all primary analysis results in the sub-folder PrimaryResultsFolder. ", location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 385, 7)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionPathUri'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_8, documentation='User-specified location of where the results should be copied after an analysis has been completed. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 390, 7)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CopyFiles'), CTD_ANON_9, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 395, 7)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Readout'), STD_ANON, scope=CTD_ANON_8, documentation='BazIO Readout option; valid values are Bases (default) and Pulses', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 406, 7), unicode_default='Bases'))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MetricsVerbosity'), STD_ANON_, scope=CTD_ANON_8, documentation='BazIO MetricsVerbosity option; valid values are Minimal (default), High, and None', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 418, 7), unicode_default='Minimal'))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TransferResource'), CTD_ANON_10, scope=CTD_ANON_8, documentation='Transfer Resource (optional for now, but will be made required when ICS implements this)', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 430, 7)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 430, 7))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResultsFolder')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 385, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollectionPathUri')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 390, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CopyFiles')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 395, 7))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Readout')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 406, 7))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MetricsVerbosity')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 418, 7))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TransferResource')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 430, 7))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
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
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionFileCopy'), PapOutputFile, scope=CTD_ANON_9, documentation='Defines the set of files to be copied to the CollectionPathUri. 1 or more. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 398, 10)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollectionFileCopy')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 398, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), STD_ANON_2, scope=CTD_ANON_10, documentation='Id of the Transfer Resource that is unique to the Scheme Type. A tuple of (TransferScheme, Id) will be globally unique', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 436, 10)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TransferScheme'), STD_ANON_3, scope=CTD_ANON_10, documentation='Transfer Scheme type (this should be an enum Scheme of rsync, srs or nfs)', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 446, 10)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=CTD_ANON_10, documentation='Display Name of the Transfer Resource', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 458, 10)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Description'), pyxb.binding.datatypes.string, scope=CTD_ANON_10, documentation='Description of the Transfer Resource', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 463, 10)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DestPath'), pyxb.binding.datatypes.string, scope=CTD_ANON_10, documentation='Remote Root Destination Path of the Transfer Resource', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 468, 10)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RelativePath'), pyxb.binding.datatypes.string, scope=CTD_ANON_10, documentation='Remote Relative Path of the Transfer Resource', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 473, 10)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 473, 10))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 436, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TransferScheme')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 446, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 458, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Description')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 463, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DestPath')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 468, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RelativePath')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 473, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
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
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_10()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationName'), pyxb.binding.datatypes.string, scope=CTD_ANON_11, documentation='The secondary analysis protocol name specified in the sample sheet. Ignored by secondary. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 494, 4)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameters'), CTD_ANON_12, scope=CTD_ANON_11, documentation='The parameters for secondary analysis specified in the sample sheet. Ignored by secondary. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 499, 4)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellCountInJob'), pyxb.binding.datatypes.int, scope=CTD_ANON_11, documentation="The number of cells in this secondary analysis job, identified by the secondary analysis parameter 'JobName'.  Supports automated secondary analysis. ", location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 513, 4)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 499, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationName')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 494, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameters')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 499, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellCountInJob')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 513, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_11()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter'), _ImportedBinding__pbbase.DataEntityType, scope=CTD_ANON_12, documentation='One or more secondary analysis parameters, such as JobName, Workflow, etc..', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 505, 7)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 505, 7))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 505, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_12()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WellName'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, documentation='Identifies which well this sample came from (e.g., coordinate on a plate). ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 290, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Concentration'), pyxb.binding.datatypes.double, scope=CTD_ANON_14, documentation='Sample input concentration. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 295, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OnPlateLoadingConcentration'), pyxb.binding.datatypes.double, scope=CTD_ANON_14, documentation='On plate loading concentration. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 300, 24)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InsertSize'), pyxb.binding.datatypes.int, scope=CTD_ANON_14, documentation='Length of the sheared template, e.g. 500, 2000, 30000', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 305, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleReuseEnabled'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_14, documentation='Whether or not complex reuse is enabled for this well. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 310, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StageHotstartEnabled'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_14, documentation='Whether or not hotstart at the stage is enabled for this well. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 315, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SizeSelectionEnabled'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_14, documentation='Whether or not size selection is enabled for this well. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 320, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UseCount'), pyxb.binding.datatypes.int, scope=CTD_ANON_14, documentation='Count of usages for this batch of complex. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 325, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DNAControlComplex'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, documentation='Indicating what kind (if any) control was used. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 330, 6)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_pbsample, 'BioSamples'), _ImportedBinding__pbsample.CTD_ANON_2, scope=CTD_ANON_14, documentation='List of biological samples.', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioSampleInfo.xsd', 126, 1)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioBaseDataModel.xsd', 98, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 300, 24))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 330, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 335, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioBaseDataModel.xsd', 98, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WellName')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 290, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Concentration')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 295, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OnPlateLoadingConcentration')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 300, 24))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InsertSize')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 305, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SampleReuseEnabled')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 310, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StageHotstartEnabled')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 315, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SizeSelectionEnabled')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 320, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UseCount')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 325, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DNAControlComplex')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 330, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbsample, 'BioSamples')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 335, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
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
    transitions.append(fac.Transition(st_10, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_13()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstCtrlVer'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, documentation='Instrument control software version. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 38, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SigProcVer'), pyxb.binding.datatypes.string, scope=CTD_ANON_15, documentation='Signal processing software version. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 43, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Automation'), _ImportedBinding__pbbase.AutomationType, scope=CTD_ANON_15, documentation='Defines the collection workflow (e.g., robotic movement, movie acquisition) for a particular cell. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 65, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionNumber'), pyxb.binding.datatypes.int, scope=CTD_ANON_15, documentation='Collection number for this plate well. Sample from one plate well or tube can be distributed to more than one cell. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 70, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellIndex'), pyxb.binding.datatypes.int, scope=CTD_ANON_15, documentation='The zero-based index of this particular cell within the cell tray.  Likely to be in the range of [0-3]', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 75, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SetNumber'), pyxb.binding.datatypes.unsignedShort, scope=CTD_ANON_15, documentation='Formerly known as the look number.  1 - N.  Defaults to 1. 0 if the look is unknown. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 80, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellPac'), _ImportedBinding__pbbase.SupplyKitCellPack, scope=CTD_ANON_15, documentation='The SMRT cell packaging supply information. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 85, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlKit'), _ImportedBinding__pbbase.SupplyKitControl, scope=CTD_ANON_15, documentation='Defines the DNA control used for this experiment. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 90, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit'), _ImportedBinding__pbbase.SupplyKitTemplate, scope=CTD_ANON_15, documentation='Defines the template (sample) prep kit used for this experiment. Can be used to get back to the primary and adapter used. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 95, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BindingKit'), _ImportedBinding__pbbase.SupplyKitBinding, scope=CTD_ANON_15, documentation='The binding kit supply information. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 100, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitPlate'), _ImportedBinding__pbrk.SupplyKitSequencing, scope=CTD_ANON_15, documentation='The sequencing kit supply information. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 105, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WashKitPlate'), _ImportedBinding__pbrk.SupplyKitSequencing, scope=CTD_ANON_15, documentation='The wash kit supply information. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 110, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ComponentVersions'), CTD_ANON_2, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_15, documentation='Subcomponents involved in the generation of the data', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 135, 6)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RunDetails'), CTD_ANON_3, scope=CTD_ANON_15, documentation='Information related to an instrument run.  A run can contain multiple chips, wells, and movies. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 170, 1)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Movie'), CTD_ANON_4, scope=CTD_ANON_15, documentation='A movie corresponds to one acquisition for a chip, one set (look) and one strobe. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 214, 1)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExpirationData'), CTD_ANON_5, scope=CTD_ANON_15, documentation='Container for the expired consumable data. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 238, 1)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WellSample'), CTD_ANON_14, scope=CTD_ANON_15, documentation='Container for the sample related data. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 282, 1)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Primary'), CTD_ANON_6, scope=CTD_ANON_15, documentation='Container for the primary analysis related data. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 342, 1)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Secondary'), CTD_ANON_11, scope=CTD_ANON_15, documentation='Container for the primary analysis related data. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 488, 1)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UserDefinedFields'), _ImportedBinding__pbbase.UserDefinedFieldsType, scope=CTD_ANON_15, documentation='A set of key-value pairs specified by a user via the run input mechanism. Note that uniqueness of keys is not enforced here and so may contain duplicate keys. ', location=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 522, 1)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioBaseDataModel.xsd', 98, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 38, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 43, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 48, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 53, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 70, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 75, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 80, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 85, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 90, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 95, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 100, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 105, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 110, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 115, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 120, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 125, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 130, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 135, 6))
    counters.add(cc_18)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioBaseDataModel.xsd', 98, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstCtrlVer')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 38, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SigProcVer')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 43, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RunDetails')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 48, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Movie')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 53, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WellSample')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 58, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Automation')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 65, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollectionNumber')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 70, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellIndex')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 75, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SetNumber')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 80, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellPac')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 85, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlKit')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 90, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 95, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BindingKit')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 100, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitPlate')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 105, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WashKitPlate')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 110, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Primary')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 115, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Secondary')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 120, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UserDefinedFields')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 125, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExpirationData')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 130, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ComponentVersions')), pyxb.utils.utility.Location('/tmp/tmpGBCw0Gxsds/PacBioCollectionMetadata.xsd', 135, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, True) ]))
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_14()

