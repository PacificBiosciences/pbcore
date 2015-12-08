# ./xsdupdate/DataSetXsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:3dc5b3a98cc462befd746fd05a18986be8ba2691
# Generated 2015-12-08 13:20:39.148321 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace http://pacificbiosciences.com/PacBioDatasets.xsd

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
import _pbsample as _ImportedBinding__pbsample
import _pbmeta as _ImportedBinding__pbmeta
import _pbbase as _ImportedBinding__pbbase

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://pacificbiosciences.com/PacBioDatasets.xsd', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_pbmeta = _ImportedBinding__pbmeta.Namespace
_Namespace_pbmeta.configureCategories(['typeBinding', 'elementBinding'])
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 202, 6)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.Instrument = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Instrument', tag='Instrument')
STD_ANON.User = STD_ANON._CF_enumeration.addEnumeration(unicode_value='User', tag='User')
STD_ANON.AnalysisJob = STD_ANON._CF_enumeration.addEnumeration(unicode_value='AnalysisJob', tag='AnalysisJob')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 115, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}Subset uses Python identifier Subset
    __Subset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Subset'), 'Subset', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_httppacificbiosciences_comPacBioDatasets_xsdSubset', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 117, 4), )

    
    Subset = property(__Subset.value, __Subset.set, None, None)

    _ElementMap.update({
        __Subset.name() : __Subset
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType with content type ELEMENT_ONLY
class DataSetMetadataType (pyxb.binding.basis.complexTypeDefinition):
    """Extend this type to provide DataSetMetadata element in each DataSet."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 186, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}TotalLength uses Python identifier TotalLength
    __TotalLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TotalLength'), 'TotalLength', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetMetadataType_httppacificbiosciences_comPacBioDatasets_xsdTotalLength', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 191, 3), )

    
    TotalLength = property(__TotalLength.value, __TotalLength.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}NumRecords uses Python identifier NumRecords
    __NumRecords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumRecords'), 'NumRecords', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetMetadataType_httppacificbiosciences_comPacBioDatasets_xsdNumRecords', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 192, 3), )

    
    NumRecords = property(__NumRecords.value, __NumRecords.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}Provenance uses Python identifier Provenance
    __Provenance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Provenance'), 'Provenance', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetMetadataType_httppacificbiosciences_comPacBioDatasets_xsdProvenance', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3), )

    
    Provenance = property(__Provenance.value, __Provenance.set, None, None)

    _ElementMap.update({
        __TotalLength.name() : __TotalLength,
        __NumRecords.name() : __NumRecords,
        __Provenance.name() : __Provenance
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DataSetMetadataType', DataSetMetadataType)


# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetRootType with content type ELEMENT_ONLY
class DataSetRootType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetRootType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataSetRootType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 214, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}AlignmentSet uses Python identifier AlignmentSet
    __AlignmentSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AlignmentSet'), 'AlignmentSet', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetRootType_httppacificbiosciences_comPacBioDatasets_xsdAlignmentSet', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 8, 1), )

    
    AlignmentSet = property(__AlignmentSet.value, __AlignmentSet.set, None, 'DataSets for aligned subreads and CCS reads.')

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}BarcodeSet uses Python identifier BarcodeSet
    __BarcodeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BarcodeSet'), 'BarcodeSet', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetRootType_httppacificbiosciences_comPacBioDatasets_xsdBarcodeSet', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 18, 1), )

    
    BarcodeSet = property(__BarcodeSet.value, __BarcodeSet.set, None, 'DataSets of Barcodes. Basically a thin metadata layer on top of the barcode FASTA.')

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}ConsensusAlignmentSet uses Python identifier ConsensusAlignmentSet
    __ConsensusAlignmentSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ConsensusAlignmentSet'), 'ConsensusAlignmentSet', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetRootType_httppacificbiosciences_comPacBioDatasets_xsdConsensusAlignmentSet', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 28, 1), )

    
    ConsensusAlignmentSet = property(__ConsensusAlignmentSet.value, __ConsensusAlignmentSet.set, None, 'DataSets of aligned CCS reads.')

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}ConsensusReadSet uses Python identifier ConsensusReadSet
    __ConsensusReadSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ConsensusReadSet'), 'ConsensusReadSet', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetRootType_httppacificbiosciences_comPacBioDatasets_xsdConsensusReadSet', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 38, 1), )

    
    ConsensusReadSet = property(__ConsensusReadSet.value, __ConsensusReadSet.set, None, 'DataSets of CCS reads (typically in unaligned BAM format).')

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}ContigSet uses Python identifier ContigSet
    __ContigSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ContigSet'), 'ContigSet', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetRootType_httppacificbiosciences_comPacBioDatasets_xsdContigSet', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 75, 1), )

    
    ContigSet = property(__ContigSet.value, __ContigSet.set, None, 'DataSets of contigs sequences. Basically a thin metadata layer on top of a contigs FASTA (e.g. from HGAP).')

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}HdfSubreadSet uses Python identifier HdfSubreadSet
    __HdfSubreadSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HdfSubreadSet'), 'HdfSubreadSet', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetRootType_httppacificbiosciences_comPacBioDatasets_xsdHdfSubreadSet', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 87, 1), )

    
    HdfSubreadSet = property(__HdfSubreadSet.value, __HdfSubreadSet.set, None, 'DataSets of subreads in bax.h5 or bas.h5 format.')

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}ReferenceSet uses Python identifier ReferenceSet
    __ReferenceSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSet'), 'ReferenceSet', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetRootType_httppacificbiosciences_comPacBioDatasets_xsdReferenceSet', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 97, 1), )

    
    ReferenceSet = property(__ReferenceSet.value, __ReferenceSet.set, None, 'DataSets of reference sequences. Replaces the reference.info.xml.')

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}SubreadSet uses Python identifier SubreadSet
    __SubreadSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubreadSet'), 'SubreadSet', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetRootType_httppacificbiosciences_comPacBioDatasets_xsdSubreadSet', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 107, 1), )

    
    SubreadSet = property(__SubreadSet.value, __SubreadSet.set, None, None)

    _ElementMap.update({
        __AlignmentSet.name() : __AlignmentSet,
        __BarcodeSet.name() : __BarcodeSet,
        __ConsensusAlignmentSet.name() : __ConsensusAlignmentSet,
        __ConsensusReadSet.name() : __ConsensusReadSet,
        __ContigSet.name() : __ContigSet,
        __HdfSubreadSet.name() : __HdfSubreadSet,
        __ReferenceSet.name() : __ReferenceSet,
        __SubreadSet.name() : __SubreadSet
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DataSetRootType', DataSetRootType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """The set of filters defined here apply to the resident data set.  Should DataSet subsets be created out of this parent DataSet, each sub-DataSet may contain its own filters."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 235, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Filter'), 'Filter', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON__httppacificbiosciences_comPacBioDatasets_xsdFilter', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 237, 8), )

    
    Filter = property(__Filter.value, __Filter.set, None, None)

    _ElementMap.update({
        __Filter.name() : __Filter
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 242, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSet uses Python identifier DataSet
    __DataSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSet'), 'DataSet', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_2_httppacificbiosciences_comPacBioDatasets_xsdDataSet', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 85, 1), )

    
    DataSet = property(__DataSet.value, __DataSet.set, None, None)

    _ElementMap.update({
        __DataSet.name() : __DataSet
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 259, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}AdapterDimerFraction uses Python identifier AdapterDimerFraction
    __AdapterDimerFraction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdapterDimerFraction'), 'AdapterDimerFraction', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDatasets_xsdAdapterDimerFraction', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 261, 8), )

    
    AdapterDimerFraction = property(__AdapterDimerFraction.value, __AdapterDimerFraction.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}ShortInsertFraction uses Python identifier ShortInsertFraction
    __ShortInsertFraction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ShortInsertFraction'), 'ShortInsertFraction', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDatasets_xsdShortInsertFraction', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 262, 8), )

    
    ShortInsertFraction = property(__ShortInsertFraction.value, __ShortInsertFraction.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}NumSequencingZmws uses Python identifier NumSequencingZmws
    __NumSequencingZmws = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumSequencingZmws'), 'NumSequencingZmws', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDatasets_xsdNumSequencingZmws', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 263, 8), )

    
    NumSequencingZmws = property(__NumSequencingZmws.value, __NumSequencingZmws.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}ProdDist uses Python identifier ProdDist
    __ProdDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProdDist'), 'ProdDist', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDatasets_xsdProdDist', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 264, 8), )

    
    ProdDist = property(__ProdDist.value, __ProdDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}ReadTypeDist uses Python identifier ReadTypeDist
    __ReadTypeDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReadTypeDist'), 'ReadTypeDist', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDatasets_xsdReadTypeDist', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 265, 8), )

    
    ReadTypeDist = property(__ReadTypeDist.value, __ReadTypeDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}ReadLenDist uses Python identifier ReadLenDist
    __ReadLenDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReadLenDist'), 'ReadLenDist', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDatasets_xsdReadLenDist', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 266, 8), )

    
    ReadLenDist = property(__ReadLenDist.value, __ReadLenDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}ReadQualDist uses Python identifier ReadQualDist
    __ReadQualDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReadQualDist'), 'ReadQualDist', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDatasets_xsdReadQualDist', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 267, 8), )

    
    ReadQualDist = property(__ReadQualDist.value, __ReadQualDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}ControlReadLenDist uses Python identifier ControlReadLenDist
    __ControlReadLenDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlReadLenDist'), 'ControlReadLenDist', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDatasets_xsdControlReadLenDist', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 268, 8), )

    
    ControlReadLenDist = property(__ControlReadLenDist.value, __ControlReadLenDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}ControlReadQualDist uses Python identifier ControlReadQualDist
    __ControlReadQualDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlReadQualDist'), 'ControlReadQualDist', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDatasets_xsdControlReadQualDist', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 269, 8), )

    
    ControlReadQualDist = property(__ControlReadQualDist.value, __ControlReadQualDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}MedianInsertDist uses Python identifier MedianInsertDist
    __MedianInsertDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MedianInsertDist'), 'MedianInsertDist', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDatasets_xsdMedianInsertDist', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 270, 8), )

    
    MedianInsertDist = property(__MedianInsertDist.value, __MedianInsertDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}InsertReadLenDist uses Python identifier InsertReadLenDist
    __InsertReadLenDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InsertReadLenDist'), 'InsertReadLenDist', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDatasets_xsdInsertReadLenDist', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 271, 8), )

    
    InsertReadLenDist = property(__InsertReadLenDist.value, __InsertReadLenDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}InsertReadQualDist uses Python identifier InsertReadQualDist
    __InsertReadQualDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InsertReadQualDist'), 'InsertReadQualDist', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDatasets_xsdInsertReadQualDist', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 272, 8), )

    
    InsertReadQualDist = property(__InsertReadQualDist.value, __InsertReadQualDist.set, None, None)

    _ElementMap.update({
        __AdapterDimerFraction.name() : __AdapterDimerFraction,
        __ShortInsertFraction.name() : __ShortInsertFraction,
        __NumSequencingZmws.name() : __NumSequencingZmws,
        __ProdDist.name() : __ProdDist,
        __ReadTypeDist.name() : __ReadTypeDist,
        __ReadLenDist.name() : __ReadLenDist,
        __ReadQualDist.name() : __ReadQualDist,
        __ControlReadLenDist.name() : __ControlReadLenDist,
        __ControlReadQualDist.name() : __ControlReadQualDist,
        __MedianInsertDist.name() : __MedianInsertDist,
        __InsertReadLenDist.name() : __InsertReadLenDist,
        __InsertReadQualDist.name() : __InsertReadQualDist
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """The set of filters defined here apply to the resident data set.  Should DataSet subsets be created out of this parent DataSet, each sub-DataSet may contain its own filters."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 315, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Filter'), 'Filter', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_4_httppacificbiosciences_comPacBioDatasets_xsdFilter', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 317, 8), )

    
    Filter = property(__Filter.value, __Filter.set, None, None)

    _ElementMap.update({
        __Filter.name() : __Filter
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}AlignmentSetMetadataType with content type ELEMENT_ONLY
class AlignmentSetMetadataType (DataSetMetadataType):
    """Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}AlignmentSetMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlignmentSetMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 121, 1)
    _ElementMap = DataSetMetadataType._ElementMap.copy()
    _AttributeMap = DataSetMetadataType._AttributeMap.copy()
    # Base type is DataSetMetadataType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}Aligner uses Python identifier Aligner
    __Aligner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Aligner'), 'Aligner', '__httppacificbiosciences_comPacBioDatasets_xsd_AlignmentSetMetadataType_httppacificbiosciences_comPacBioDatasets_xsdAligner', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 125, 5), )

    
    Aligner = property(__Aligner.value, __Aligner.set, None, None)

    
    # Element TotalLength ({http://pacificbiosciences.com/PacBioDatasets.xsd}TotalLength) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    
    # Element NumRecords ({http://pacificbiosciences.com/PacBioDatasets.xsd}NumRecords) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    
    # Element Provenance ({http://pacificbiosciences.com/PacBioDatasets.xsd}Provenance) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    _ElementMap.update({
        __Aligner.name() : __Aligner
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AlignmentSetMetadataType', AlignmentSetMetadataType)


# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}BarcodeSetMetadataType with content type ELEMENT_ONLY
class BarcodeSetMetadataType (DataSetMetadataType):
    """Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}BarcodeSetMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BarcodeSetMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 142, 1)
    _ElementMap = DataSetMetadataType._ElementMap.copy()
    _AttributeMap = DataSetMetadataType._AttributeMap.copy()
    # Base type is DataSetMetadataType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}BarcodeConstruction uses Python identifier BarcodeConstruction
    __BarcodeConstruction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BarcodeConstruction'), 'BarcodeConstruction', '__httppacificbiosciences_comPacBioDatasets_xsd_BarcodeSetMetadataType_httppacificbiosciences_comPacBioDatasets_xsdBarcodeConstruction', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 146, 5), )

    
    BarcodeConstruction = property(__BarcodeConstruction.value, __BarcodeConstruction.set, None, None)

    
    # Element TotalLength ({http://pacificbiosciences.com/PacBioDatasets.xsd}TotalLength) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    
    # Element NumRecords ({http://pacificbiosciences.com/PacBioDatasets.xsd}NumRecords) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    
    # Element Provenance ({http://pacificbiosciences.com/PacBioDatasets.xsd}Provenance) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    _ElementMap.update({
        __BarcodeConstruction.name() : __BarcodeConstruction
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BarcodeSetMetadataType', BarcodeSetMetadataType)


# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}ContigSetMetadataType with content type ELEMENT_ONLY
class ContigSetMetadataType (DataSetMetadataType):
    """Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}ContigSetMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContigSetMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 163, 1)
    _ElementMap = DataSetMetadataType._ElementMap.copy()
    _AttributeMap = DataSetMetadataType._AttributeMap.copy()
    # Base type is DataSetMetadataType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}Contigs uses Python identifier Contigs
    __Contigs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contigs'), 'Contigs', '__httppacificbiosciences_comPacBioDatasets_xsd_ContigSetMetadataType_httppacificbiosciences_comPacBioDatasets_xsdContigs', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 52, 1), )

    
    Contigs = property(__Contigs.value, __Contigs.set, None, 'List of contigs in a ContigSet')

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}Organism uses Python identifier Organism
    __Organism = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organism'), 'Organism', '__httppacificbiosciences_comPacBioDatasets_xsd_ContigSetMetadataType_httppacificbiosciences_comPacBioDatasets_xsdOrganism', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 167, 5), )

    
    Organism = property(__Organism.value, __Organism.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}Ploidy uses Python identifier Ploidy
    __Ploidy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ploidy'), 'Ploidy', '__httppacificbiosciences_comPacBioDatasets_xsd_ContigSetMetadataType_httppacificbiosciences_comPacBioDatasets_xsdPloidy', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 168, 5), )

    
    Ploidy = property(__Ploidy.value, __Ploidy.set, None, None)

    
    # Element TotalLength ({http://pacificbiosciences.com/PacBioDatasets.xsd}TotalLength) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    
    # Element NumRecords ({http://pacificbiosciences.com/PacBioDatasets.xsd}NumRecords) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    
    # Element Provenance ({http://pacificbiosciences.com/PacBioDatasets.xsd}Provenance) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    _ElementMap.update({
        __Contigs.name() : __Contigs,
        __Organism.name() : __Organism,
        __Ploidy.name() : __Ploidy
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ContigSetMetadataType', ContigSetMetadataType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 194, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}CommonServicesInstanceId uses Python identifier CommonServicesInstanceId
    __CommonServicesInstanceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CommonServicesInstanceId'), 'CommonServicesInstanceId', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioDatasets_xsdCommonServicesInstanceId', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 196, 6), )

    
    CommonServicesInstanceId = property(__CommonServicesInstanceId.value, __CommonServicesInstanceId.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}CreatorUserId uses Python identifier CreatorUserId
    __CreatorUserId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CreatorUserId'), 'CreatorUserId', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioDatasets_xsdCreatorUserId', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 197, 6), )

    
    CreatorUserId = property(__CreatorUserId.value, __CreatorUserId.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}ParentJobId uses Python identifier ParentJobId
    __ParentJobId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ParentJobId'), 'ParentJobId', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioDatasets_xsdParentJobId', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 198, 6), )

    
    ParentJobId = property(__ParentJobId.value, __ParentJobId.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}ParentTool uses Python identifier ParentTool
    __ParentTool = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ParentTool'), 'ParentTool', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioDatasets_xsdParentTool', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 199, 6), )

    
    ParentTool = property(__ParentTool.value, __ParentTool.set, None, None)

    
    # Attribute CreatedBy uses Python identifier CreatedBy
    __CreatedBy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CreatedBy'), 'CreatedBy', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_5_CreatedBy', STD_ANON, required=True)
    __CreatedBy._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 201, 5)
    __CreatedBy._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 201, 5)
    
    CreatedBy = property(__CreatedBy.value, __CreatedBy.set, None, None)

    _ElementMap.update({
        __CommonServicesInstanceId.name() : __CommonServicesInstanceId,
        __CreatorUserId.name() : __CreatorUserId,
        __ParentJobId.name() : __ParentJobId,
        __ParentTool.name() : __ParentTool
    })
    _AttributeMap.update({
        __CreatedBy.name() : __CreatedBy
    })



# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}ReadSetMetadataType with content type ELEMENT_ONLY
class ReadSetMetadataType (DataSetMetadataType):
    """Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}ReadSetMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReadSetMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 252, 1)
    _ElementMap = DataSetMetadataType._ElementMap.copy()
    _AttributeMap = DataSetMetadataType._AttributeMap.copy()
    # Base type is DataSetMetadataType
    
    # Element {http://pacificbiosciences.com/PacBioCollectionMetadata.xsd}Collections uses Python identifier Collections
    __Collections = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_pbmeta, 'Collections'), 'Collections', '__httppacificbiosciences_comPacBioDatasets_xsd_ReadSetMetadataType_httppacificbiosciences_comPacBioCollectionMetadata_xsdCollections', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioCollectionMetadata.xsd', 20, 1), )

    
    Collections = property(__Collections.value, __Collections.set, None, 'A set of acquisition definitions')

    
    # Element TotalLength ({http://pacificbiosciences.com/PacBioDatasets.xsd}TotalLength) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    
    # Element NumRecords ({http://pacificbiosciences.com/PacBioDatasets.xsd}NumRecords) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    
    # Element Provenance ({http://pacificbiosciences.com/PacBioDatasets.xsd}Provenance) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}SummaryStats uses Python identifier SummaryStats
    __SummaryStats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SummaryStats'), 'SummaryStats', '__httppacificbiosciences_comPacBioDatasets_xsd_ReadSetMetadataType_httppacificbiosciences_comPacBioDatasets_xsdSummaryStats', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 258, 5), )

    
    SummaryStats = property(__SummaryStats.value, __SummaryStats.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioSampleInfo.xsd}BioSamples uses Python identifier BioSamples
    __BioSamples = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_pbsample, 'BioSamples'), 'BioSamples', '__httppacificbiosciences_comPacBioDatasets_xsd_ReadSetMetadataType_httppacificbiosciences_comPacBioSampleInfo_xsdBioSamples', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioSampleInfo.xsd', 134, 1), )

    
    BioSamples = property(__BioSamples.value, __BioSamples.set, None, None)

    _ElementMap.update({
        __Collections.name() : __Collections,
        __SummaryStats.name() : __SummaryStats,
        __BioSamples.name() : __BioSamples
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ReadSetMetadataType', ReadSetMetadataType)


# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}SubreadSetMetadataType with content type ELEMENT_ONLY
class SubreadSetMetadataType (DataSetMetadataType):
    """Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}SubreadSetMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubreadSetMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 292, 1)
    _ElementMap = DataSetMetadataType._ElementMap.copy()
    _AttributeMap = DataSetMetadataType._AttributeMap.copy()
    # Base type is DataSetMetadataType
    
    # Element TotalLength ({http://pacificbiosciences.com/PacBioDatasets.xsd}TotalLength) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    
    # Element NumRecords ({http://pacificbiosciences.com/PacBioDatasets.xsd}NumRecords) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    
    # Element Provenance ({http://pacificbiosciences.com/PacBioDatasets.xsd}Provenance) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadataType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}AverageSubreadLength uses Python identifier AverageSubreadLength
    __AverageSubreadLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AverageSubreadLength'), 'AverageSubreadLength', '__httppacificbiosciences_comPacBioDatasets_xsd_SubreadSetMetadataType_httppacificbiosciences_comPacBioDatasets_xsdAverageSubreadLength', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 296, 5), )

    
    AverageSubreadLength = property(__AverageSubreadLength.value, __AverageSubreadLength.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}AverageSubreadQuality uses Python identifier AverageSubreadQuality
    __AverageSubreadQuality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AverageSubreadQuality'), 'AverageSubreadQuality', '__httppacificbiosciences_comPacBioDatasets_xsd_SubreadSetMetadataType_httppacificbiosciences_comPacBioDatasets_xsdAverageSubreadQuality', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 297, 5), )

    
    AverageSubreadQuality = property(__AverageSubreadQuality.value, __AverageSubreadQuality.set, None, None)

    _ElementMap.update({
        __AverageSubreadLength.name() : __AverageSubreadLength,
        __AverageSubreadQuality.name() : __AverageSubreadQuality
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SubreadSetMetadataType', SubreadSetMetadataType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (_ImportedBinding__pbbase.BaseEntityType):
    """List of contigs in a ContigSet"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 56, 2)
    _ElementMap = _ImportedBinding__pbbase.BaseEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.BaseEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}Contig uses Python identifier Contig
    __Contig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contig'), 'Contig', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_6_httppacificbiosciences_comPacBioDatasets_xsdContig', True, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 60, 6), )

    
    Contig = property(__Contig.value, __Contig.set, None, None)

    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __Contig.name() : __Contig
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (_ImportedBinding__pbbase.BaseEntityType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 61, 7)
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
    
    # Attribute Length uses Python identifier Length
    __Length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Length'), 'Length', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_7_Length', pyxb.binding.datatypes.anySimpleType, required=True)
    __Length._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 64, 10)
    __Length._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 64, 10)
    
    Length = property(__Length.value, __Length.set, None, None)

    
    # Attribute Digest uses Python identifier Digest
    __Digest = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Digest'), 'Digest', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_7_Digest', pyxb.binding.datatypes.anySimpleType, required=True)
    __Digest._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 65, 10)
    __Digest._UseLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 65, 10)
    
    Digest = property(__Digest.value, __Digest.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Length.name() : __Length,
        __Digest.name() : __Digest
    })



# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType with content type ELEMENT_ONLY
class DataSetType (_ImportedBinding__pbbase.StrictEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataSetType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 226, 1)
    _ElementMap = _ImportedBinding__pbbase.StrictEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.StrictEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.StrictEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources uses Python identifier ExternalResources
    __ExternalResources = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources'), 'ExternalResources', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetType_httppacificbiosciences_comPacBioBaseDataModel_xsdExternalResources', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 256, 1), )

    
    ExternalResources = property(__ExternalResources.value, __ExternalResources.set, None, 'Pointers to data that do not reside inside the parent structure')

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}Filters uses Python identifier Filters
    __Filters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Filters'), 'Filters', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetType_httppacificbiosciences_comPacBioDatasets_xsdFilters', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5), )

    
    Filters = property(__Filters.value, __Filters.set, None, 'The set of filters defined here apply to the resident data set.  Should DataSet subsets be created out of this parent DataSet, each sub-DataSet may contain its own filters.')

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets uses Python identifier DataSets
    __DataSets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSets'), 'DataSets', '__httppacificbiosciences_comPacBioDatasets_xsd_DataSetType_httppacificbiosciences_comPacBioDatasets_xsdDataSets', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5), )

    
    DataSets = property(__DataSets.value, __DataSets.set, None, None)

    
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
        __Filters.name() : __Filters,
        __DataSets.name() : __DataSets
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DataSetType', DataSetType)


# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}SubsetType with content type ELEMENT_ONLY
class SubsetType (_ImportedBinding__pbbase.StrictEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}SubsetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubsetType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 307, 1)
    _ElementMap = _ImportedBinding__pbbase.StrictEntityType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__pbbase.StrictEntityType._AttributeMap.copy()
    # Base type is _ImportedBinding__pbbase.StrictEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}DataPointers uses Python identifier DataPointers
    __DataPointers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'DataPointers'), 'DataPointers', '__httppacificbiosciences_comPacBioDatasets_xsd_SubsetType_httppacificbiosciences_comPacBioBaseDataModel_xsdDataPointers', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 222, 1), )

    
    DataPointers = property(__DataPointers.value, __DataPointers.set, None, 'Pointer list to UniqueIds in the system')

    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}Filters uses Python identifier Filters
    __Filters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Filters'), 'Filters', '__httppacificbiosciences_comPacBioDatasets_xsd_SubsetType_httppacificbiosciences_comPacBioDatasets_xsdFilters', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 311, 5), )

    
    Filters = property(__Filters.value, __Filters.set, None, 'The set of filters defined here apply to the resident data set.  Should DataSet subsets be created out of this parent DataSet, each sub-DataSet may contain its own filters.')

    
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
        __DataPointers.name() : __DataPointers,
        __Filters.name() : __Filters
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SubsetType', SubsetType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (DataSetType):
    """DataSets of CCS reads (typically in unaligned BAM format)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 42, 2)
    _ElementMap = DataSetType._ElementMap.copy()
    _AttributeMap = DataSetType._AttributeMap.copy()
    # Base type is DataSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadata uses Python identifier DataSetMetadata
    __DataSetMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), 'DataSetMetadata', '__httppacificbiosciences_comPacBioDatasets_xsd_CTD_ANON_8_httppacificbiosciences_comPacBioDatasets_xsdDataSetMetadata', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 46, 6), )

    
    DataSetMetadata = property(__DataSetMetadata.value, __DataSetMetadata.set, None, None)

    
    # Element Filters ({http://pacificbiosciences.com/PacBioDatasets.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
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
        __DataSetMetadata.name() : __DataSetMetadata
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}AlignmentSetType with content type ELEMENT_ONLY
class AlignmentSetType (DataSetType):
    """Type for DataSets consisting of aligned subreads and CCS reads."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlignmentSetType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 130, 1)
    _ElementMap = DataSetType._ElementMap.copy()
    _AttributeMap = DataSetType._AttributeMap.copy()
    # Base type is DataSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadata uses Python identifier DataSetMetadata
    __DataSetMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), 'DataSetMetadata', '__httppacificbiosciences_comPacBioDatasets_xsd_AlignmentSetType_httppacificbiosciences_comPacBioDatasets_xsdDataSetMetadata', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 137, 5), )

    
    DataSetMetadata = property(__DataSetMetadata.value, __DataSetMetadata.set, None, None)

    
    # Element Filters ({http://pacificbiosciences.com/PacBioDatasets.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
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
        __DataSetMetadata.name() : __DataSetMetadata
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AlignmentSetType', AlignmentSetType)


# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}BarcodeSetType with content type ELEMENT_ONLY
class BarcodeSetType (DataSetType):
    """Type for the Barcode DataSet."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BarcodeSetType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 151, 1)
    _ElementMap = DataSetType._ElementMap.copy()
    _AttributeMap = DataSetType._AttributeMap.copy()
    # Base type is DataSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadata uses Python identifier DataSetMetadata
    __DataSetMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), 'DataSetMetadata', '__httppacificbiosciences_comPacBioDatasets_xsd_BarcodeSetType_httppacificbiosciences_comPacBioDatasets_xsdDataSetMetadata', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 158, 5), )

    
    DataSetMetadata = property(__DataSetMetadata.value, __DataSetMetadata.set, None, None)

    
    # Element Filters ({http://pacificbiosciences.com/PacBioDatasets.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
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
        __DataSetMetadata.name() : __DataSetMetadata
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BarcodeSetType', BarcodeSetType)


# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}ContigSetType with content type ELEMENT_ONLY
class ContigSetType (DataSetType):
    """Type for a Contig DataSet."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContigSetType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 174, 1)
    _ElementMap = DataSetType._ElementMap.copy()
    _AttributeMap = DataSetType._AttributeMap.copy()
    # Base type is DataSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadata uses Python identifier DataSetMetadata
    __DataSetMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), 'DataSetMetadata', '__httppacificbiosciences_comPacBioDatasets_xsd_ContigSetType_httppacificbiosciences_comPacBioDatasets_xsdDataSetMetadata', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 181, 5), )

    
    DataSetMetadata = property(__DataSetMetadata.value, __DataSetMetadata.set, None, None)

    
    # Element Filters ({http://pacificbiosciences.com/PacBioDatasets.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
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
        __DataSetMetadata.name() : __DataSetMetadata
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ContigSetType', ContigSetType)


# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}ReadSetType with content type ELEMENT_ONLY
class ReadSetType (DataSetType):
    """Type for DataSets consisting of unaligned subreads and CCS reads DataSets"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReadSetType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 280, 1)
    _ElementMap = DataSetType._ElementMap.copy()
    _AttributeMap = DataSetType._AttributeMap.copy()
    # Base type is DataSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDatasets.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadata uses Python identifier DataSetMetadata
    __DataSetMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), 'DataSetMetadata', '__httppacificbiosciences_comPacBioDatasets_xsd_ReadSetType_httppacificbiosciences_comPacBioDatasets_xsdDataSetMetadata', False, pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 287, 5), )

    
    DataSetMetadata = property(__DataSetMetadata.value, __DataSetMetadata.set, None, None)

    
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
        __DataSetMetadata.name() : __DataSetMetadata
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ReadSetType', ReadSetType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (AlignmentSetType):
    """DataSets for aligned subreads and CCS reads."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 12, 2)
    _ElementMap = AlignmentSetType._ElementMap.copy()
    _AttributeMap = AlignmentSetType._AttributeMap.copy()
    # Base type is AlignmentSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}AlignmentSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDatasets.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (BarcodeSetType):
    """DataSets of Barcodes. Basically a thin metadata layer on top of the barcode FASTA."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 22, 2)
    _ElementMap = BarcodeSetType._ElementMap.copy()
    _AttributeMap = BarcodeSetType._AttributeMap.copy()
    # Base type is BarcodeSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}BarcodeSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDatasets.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (AlignmentSetType):
    """DataSets of aligned CCS reads."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 32, 2)
    _ElementMap = AlignmentSetType._ElementMap.copy()
    _AttributeMap = AlignmentSetType._AttributeMap.copy()
    # Base type is AlignmentSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}AlignmentSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDatasets.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (ContigSetType):
    """DataSets of contigs sequences. Basically a thin metadata layer on top of a contigs FASTA (e.g. from HGAP)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 79, 2)
    _ElementMap = ContigSetType._ElementMap.copy()
    _AttributeMap = ContigSetType._AttributeMap.copy()
    # Base type is ContigSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}ContigSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDatasets.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (ReadSetType):
    """DataSets of subreads in bax.h5 or bas.h5 format."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 91, 2)
    _ElementMap = ReadSetType._ElementMap.copy()
    _AttributeMap = ReadSetType._AttributeMap.copy()
    # Base type is ReadSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDatasets.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}ReadSetType
    
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



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (ContigSetType):
    """DataSets of reference sequences. Replaces the reference.info.xml."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 101, 2)
    _ElementMap = ContigSetType._ElementMap.copy()
    _AttributeMap = ContigSetType._AttributeMap.copy()
    # Base type is ContigSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}ContigSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDatasets.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
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



# Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}SubreadSetType with content type ELEMENT_ONLY
class SubreadSetType (ReadSetType):
    """Complex type {http://pacificbiosciences.com/PacBioDatasets.xsd}SubreadSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubreadSetType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 302, 1)
    _ElementMap = ReadSetType._ElementMap.copy()
    _AttributeMap = ReadSetType._AttributeMap.copy()
    # Base type is ReadSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDatasets.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}ReadSetType
    
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
Namespace.addCategoryObject('typeBinding', 'SubreadSetType', SubreadSetType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (SubreadSetType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 108, 2)
    _ElementMap = SubreadSetType._ElementMap.copy()
    _AttributeMap = SubreadSetType._AttributeMap.copy()
    # Base type is SubreadSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioBaseDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioBaseDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDatasets.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDatasets.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDatasets.xsd}ReadSetType
    
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



DataSetRoot = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetRoot'), DataSetRootType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 86, 1))
Namespace.addCategoryObject('elementBinding', DataSetRoot.name().localName(), DataSetRoot)

Subsets = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Subsets'), CTD_ANON, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 114, 1))
Namespace.addCategoryObject('elementBinding', Subsets.name().localName(), Subsets)

Contigs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contigs'), CTD_ANON_6, documentation='List of contigs in a ContigSet', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 52, 1))
Namespace.addCategoryObject('elementBinding', Contigs.name().localName(), Contigs)

DataSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSet'), DataSetType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 85, 1))
Namespace.addCategoryObject('elementBinding', DataSet.name().localName(), DataSet)

ConsensusReadSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsensusReadSet'), CTD_ANON_8, documentation='DataSets of CCS reads (typically in unaligned BAM format).', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 38, 1))
Namespace.addCategoryObject('elementBinding', ConsensusReadSet.name().localName(), ConsensusReadSet)

AlignmentSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AlignmentSet'), CTD_ANON_9, documentation='DataSets for aligned subreads and CCS reads.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 8, 1))
Namespace.addCategoryObject('elementBinding', AlignmentSet.name().localName(), AlignmentSet)

BarcodeSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BarcodeSet'), CTD_ANON_10, documentation='DataSets of Barcodes. Basically a thin metadata layer on top of the barcode FASTA.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 18, 1))
Namespace.addCategoryObject('elementBinding', BarcodeSet.name().localName(), BarcodeSet)

ConsensusAlignmentSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsensusAlignmentSet'), CTD_ANON_11, documentation='DataSets of aligned CCS reads.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 28, 1))
Namespace.addCategoryObject('elementBinding', ConsensusAlignmentSet.name().localName(), ConsensusAlignmentSet)

ContigSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContigSet'), CTD_ANON_12, documentation='DataSets of contigs sequences. Basically a thin metadata layer on top of a contigs FASTA (e.g. from HGAP).', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 75, 1))
Namespace.addCategoryObject('elementBinding', ContigSet.name().localName(), ContigSet)

HdfSubreadSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HdfSubreadSet'), CTD_ANON_13, documentation='DataSets of subreads in bax.h5 or bas.h5 format.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 87, 1))
Namespace.addCategoryObject('elementBinding', HdfSubreadSet.name().localName(), HdfSubreadSet)

ReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSet'), CTD_ANON_14, documentation='DataSets of reference sequences. Replaces the reference.info.xml.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 97, 1))
Namespace.addCategoryObject('elementBinding', ReferenceSet.name().localName(), ReferenceSet)

SubreadSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubreadSet'), CTD_ANON_15, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 107, 1))
Namespace.addCategoryObject('elementBinding', SubreadSet.name().localName(), SubreadSet)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Subset'), SubsetType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 117, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Subset')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 117, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




DataSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TotalLength'), pyxb.binding.datatypes.long, scope=DataSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 191, 3)))

DataSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumRecords'), pyxb.binding.datatypes.int, scope=DataSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 192, 3)))

DataSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Provenance'), CTD_ANON_5, scope=DataSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DataSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TotalLength')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 191, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumRecords')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 192, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DataSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Provenance')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DataSetMetadataType._Automaton = _BuildAutomaton_()




DataSetRootType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AlignmentSet'), CTD_ANON_9, scope=DataSetRootType, documentation='DataSets for aligned subreads and CCS reads.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 8, 1)))

DataSetRootType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BarcodeSet'), CTD_ANON_10, scope=DataSetRootType, documentation='DataSets of Barcodes. Basically a thin metadata layer on top of the barcode FASTA.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 18, 1)))

DataSetRootType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsensusAlignmentSet'), CTD_ANON_11, scope=DataSetRootType, documentation='DataSets of aligned CCS reads.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 28, 1)))

DataSetRootType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsensusReadSet'), CTD_ANON_8, scope=DataSetRootType, documentation='DataSets of CCS reads (typically in unaligned BAM format).', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 38, 1)))

DataSetRootType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContigSet'), CTD_ANON_12, scope=DataSetRootType, documentation='DataSets of contigs sequences. Basically a thin metadata layer on top of a contigs FASTA (e.g. from HGAP).', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 75, 1)))

DataSetRootType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HdfSubreadSet'), CTD_ANON_13, scope=DataSetRootType, documentation='DataSets of subreads in bax.h5 or bas.h5 format.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 87, 1)))

DataSetRootType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSet'), CTD_ANON_14, scope=DataSetRootType, documentation='DataSets of reference sequences. Replaces the reference.info.xml.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 97, 1)))

DataSetRootType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubreadSet'), CTD_ANON_15, scope=DataSetRootType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 107, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 216, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 217, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 218, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 219, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 220, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 221, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 222, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 223, 3))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DataSetRootType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AlignmentSet')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 216, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DataSetRootType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BarcodeSet')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 217, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DataSetRootType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ConsensusAlignmentSet')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 218, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DataSetRootType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ConsensusReadSet')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 219, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DataSetRootType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ContigSet')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 220, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DataSetRootType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HdfSubreadSet')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 221, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(DataSetRootType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSet')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 222, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(DataSetRootType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubreadSet')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 223, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DataSetRootType._Automaton = _BuildAutomaton_2()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Filter'), _ImportedBinding__pbbase.FilterType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 237, 8)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filter')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 237, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_3()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSet'), DataSetType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 85, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 244, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSet')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 244, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_4()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdapterDimerFraction'), pyxb.binding.datatypes.float, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 261, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShortInsertFraction'), pyxb.binding.datatypes.float, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 262, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumSequencingZmws'), pyxb.binding.datatypes.int, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 263, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProdDist'), _ImportedBinding__pbbase.StatsDiscreteDistType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 264, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReadTypeDist'), _ImportedBinding__pbbase.StatsDiscreteDistType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 265, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReadLenDist'), _ImportedBinding__pbbase.StatsContinuousDistType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 266, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReadQualDist'), _ImportedBinding__pbbase.StatsContinuousDistType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 267, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlReadLenDist'), _ImportedBinding__pbbase.StatsContinuousDistType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 268, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlReadQualDist'), _ImportedBinding__pbbase.StatsContinuousDistType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 269, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MedianInsertDist'), _ImportedBinding__pbbase.StatsContinuousDistType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 270, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InsertReadLenDist'), _ImportedBinding__pbbase.StatsContinuousDistType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 271, 8)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InsertReadQualDist'), _ImportedBinding__pbbase.StatsContinuousDistType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 272, 8)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdapterDimerFraction')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 261, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ShortInsertFraction')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 262, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumSequencingZmws')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 263, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProdDist')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 264, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReadTypeDist')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 265, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReadLenDist')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 266, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReadQualDist')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 267, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlReadLenDist')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 268, 8))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlReadQualDist')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 269, 8))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MedianInsertDist')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 270, 8))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InsertReadLenDist')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 271, 8))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InsertReadQualDist')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 272, 8))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_5()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Filter'), _ImportedBinding__pbbase.FilterType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 317, 8)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filter')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 317, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_6()




AlignmentSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Aligner'), pyxb.binding.datatypes.anyType, scope=AlignmentSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 125, 5)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 125, 5))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AlignmentSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TotalLength')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 191, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AlignmentSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumRecords')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 192, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AlignmentSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Provenance')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AlignmentSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Aligner')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 125, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AlignmentSetMetadataType._Automaton = _BuildAutomaton_7()




BarcodeSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BarcodeConstruction'), pyxb.binding.datatypes.string, scope=BarcodeSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 146, 5)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TotalLength')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 191, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumRecords')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 192, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Provenance')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BarcodeSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BarcodeConstruction')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 146, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BarcodeSetMetadataType._Automaton = _BuildAutomaton_8()




ContigSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contigs'), CTD_ANON_6, scope=ContigSetMetadataType, documentation='List of contigs in a ContigSet', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 52, 1)))

ContigSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organism'), pyxb.binding.datatypes.string, scope=ContigSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 167, 5)))

ContigSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ploidy'), pyxb.binding.datatypes.string, scope=ContigSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 168, 5)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 167, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 168, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TotalLength')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 191, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumRecords')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 192, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Provenance')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organism')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 167, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ploidy')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 168, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ContigSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contigs')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 169, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ContigSetMetadataType._Automaton = _BuildAutomaton_9()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CommonServicesInstanceId'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 196, 6)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CreatorUserId'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 197, 6)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ParentJobId'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 198, 6)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ParentTool'), _ImportedBinding__pbbase.BaseEntityType, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 199, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 196, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 197, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 198, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 199, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CommonServicesInstanceId')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 196, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CreatorUserId')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 197, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ParentJobId')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 198, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ParentTool')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 199, 6))
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
CTD_ANON_5._Automaton = _BuildAutomaton_10()




ReadSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_pbmeta, 'Collections'), _ImportedBinding__pbmeta.CTD_ANON_, scope=ReadSetMetadataType, documentation='A set of acquisition definitions', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioCollectionMetadata.xsd', 20, 1)))

ReadSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SummaryStats'), CTD_ANON_3, scope=ReadSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 258, 5)))

ReadSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_pbsample, 'BioSamples'), _ImportedBinding__pbsample.CTD_ANON_3, scope=ReadSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioSampleInfo.xsd', 134, 1)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 256, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 257, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 258, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TotalLength')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 191, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumRecords')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 192, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Provenance')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbmeta, 'Collections')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 256, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbsample, 'BioSamples')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 257, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SummaryStats')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 258, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReadSetMetadataType._Automaton = _BuildAutomaton_11()




SubreadSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AverageSubreadLength'), pyxb.binding.datatypes.int, scope=SubreadSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 296, 5)))

SubreadSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AverageSubreadQuality'), pyxb.binding.datatypes.float, scope=SubreadSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 297, 5)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubreadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TotalLength')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 191, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubreadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumRecords')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 192, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubreadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Provenance')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 193, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubreadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AverageSubreadLength')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 296, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SubreadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AverageSubreadQuality')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 297, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SubreadSetMetadataType._Automaton = _BuildAutomaton_12()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contig'), CTD_ANON_7, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 60, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 60, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contig')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 60, 6))
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
CTD_ANON_6._Automaton = _BuildAutomaton_13()




def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_14()




DataSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources'), _ImportedBinding__pbbase.CTD_ANON_4, scope=DataSetType, documentation='Pointers to data that do not reside inside the parent structure', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 256, 1)))

DataSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Filters'), CTD_ANON_, scope=DataSetType, documentation='The set of filters defined here apply to the resident data set.  Should DataSet subsets be created out of this parent DataSet, each sub-DataSet may contain its own filters.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5)))

DataSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSets'), CTD_ANON_2, scope=DataSetType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DataSetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataSetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DataSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DataSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
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
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DataSetType._Automaton = _BuildAutomaton_15()




SubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'DataPointers'), _ImportedBinding__pbbase.CTD_ANON_3, scope=SubsetType, documentation='Pointer list to UniqueIds in the system', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 222, 1)))

SubsetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Filters'), CTD_ANON_4, scope=SubsetType, documentation='The set of filters defined here apply to the resident data set.  Should DataSet subsets be created out of this parent DataSet, each sub-DataSet may contain its own filters.', location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 311, 5)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 311, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 321, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SubsetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SubsetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 311, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SubsetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'DataPointers')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 321, 5))
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
SubsetType._Automaton = _BuildAutomaton_16()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), DataSetMetadataType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 46, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 46, 6))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_17()




AlignmentSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), AlignmentSetMetadataType, scope=AlignmentSetType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 137, 5)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 137, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AlignmentSetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AlignmentSetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AlignmentSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AlignmentSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AlignmentSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 137, 5))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AlignmentSetType._Automaton = _BuildAutomaton_18()




BarcodeSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), BarcodeSetMetadataType, scope=BarcodeSetType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 158, 5)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BarcodeSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 158, 5))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BarcodeSetType._Automaton = _BuildAutomaton_19()




ContigSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), ContigSetMetadataType, scope=ContigSetType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 181, 5)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ContigSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 181, 5))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ContigSetType._Automaton = _BuildAutomaton_20()




ReadSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), ReadSetMetadataType, scope=ReadSetType, location=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 287, 5)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 287, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReadSetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReadSetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 287, 5))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReadSetType._Automaton = _BuildAutomaton_21()




def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 137, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 137, 5))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_22()




def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 158, 5))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_23()




def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 137, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 137, 5))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_24()




def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 181, 5))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_25()




def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 287, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 287, 5))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_26()




def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 181, 5))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_27()




def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 287, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubreadSetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SubreadSetType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SubreadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SubreadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SubreadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 287, 5))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SubreadSetType._Automaton = _BuildAutomaton_28()




def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 287, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioBaseDataModel.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(_Namespace_pbbase, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 230, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 231, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 241, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpiM7rWfxsds/PacBioDatasets.xsd', 287, 5))
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
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_29()

