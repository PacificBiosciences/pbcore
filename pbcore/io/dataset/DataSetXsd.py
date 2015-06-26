# ./DataSetXsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:3c1eccef1b156ac43379b476cb78e3eecd9f5c97
# Generated 2015-06-23 13:50:43.883039 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace http://pacificbiosciences.com/PacBioDataModel.xsd

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:83991eee-19e9-11e5-8315-001a4acb6b14')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://pacificbiosciences.com/PacBioDataModel.xsd', create_if_missing=True)
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
class STD_ANON (pyxb.binding.datatypes.ID):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 69, 3)
    _Documentation = None
STD_ANON._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON._CF_pattern.addPattern(pattern='[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}')
STD_ANON._InitializeFacetMap(STD_ANON._CF_pattern)

# Atomic simple type: {http://pacificbiosciences.com/PacBioDataModel.xsd}SupportedAcquisitionStates
class SupportedAcquisitionStates (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedAcquisitionStates')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 555, 1)
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
SupportedAcquisitionStates._InitializeFacetMap(SupportedAcquisitionStates._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SupportedAcquisitionStates', SupportedAcquisitionStates)

# Atomic simple type: {http://pacificbiosciences.com/PacBioDataModel.xsd}SupportedDataTypes
class SupportedDataTypes (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedDataTypes')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 571, 1)
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

# Atomic simple type: {http://pacificbiosciences.com/PacBioDataModel.xsd}SupportedNucleotides
class SupportedNucleotides (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedNucleotides')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 610, 1)
    _Documentation = None
SupportedNucleotides._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SupportedNucleotides, enum_prefix=None)
SupportedNucleotides.A = SupportedNucleotides._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
SupportedNucleotides.C = SupportedNucleotides._CF_enumeration.addEnumeration(unicode_value='C', tag='C')
SupportedNucleotides.T = SupportedNucleotides._CF_enumeration.addEnumeration(unicode_value='T', tag='T')
SupportedNucleotides.G = SupportedNucleotides._CF_enumeration.addEnumeration(unicode_value='G', tag='G')
SupportedNucleotides._InitializeFacetMap(SupportedNucleotides._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SupportedNucleotides', SupportedNucleotides)

# Atomic simple type: {http://pacificbiosciences.com/PacBioDataModel.xsd}SupportedRunStates
class SupportedRunStates (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupportedRunStates')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 618, 1)
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
SupportedRunStates.Unknown = SupportedRunStates._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
SupportedRunStates._InitializeFacetMap(SupportedRunStates._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'SupportedRunStates', SupportedRunStates)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 47, 6)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.Instrument = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Instrument', tag='Instrument')
STD_ANON_.User = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='User', tag='User')
STD_ANON_.AnalysisJob = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='AnalysisJob', tag='AnalysisJob')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: {http://pacificbiosciences.com/PacBioDataModel.xsd}PapOutputFile
class PapOutputFile (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Defines a list of available file output types from primary output that can be copied out to the CollectionPathUri. The types Pulse, Base, Fasta, and Fastq are for legacy use only."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PapOutputFile')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 624, 1)
    _Documentation = 'Defines a list of available file output types from primary output that can be copied out to the CollectionPathUri. The types Pulse, Base, Fasta, and Fastq are for legacy use only.'
PapOutputFile._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PapOutputFile, enum_prefix=None)
PapOutputFile.Movie = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='Movie', tag='Movie')
PapOutputFile.Trace = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='Trace', tag='Trace')
PapOutputFile.Pulse = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='Pulse', tag='Pulse')
PapOutputFile.Base = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='Base', tag='Base')
PapOutputFile.Baz = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='Baz', tag='Baz')
PapOutputFile.Bam = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='Bam', tag='Bam')
PapOutputFile.Fasta = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='Fasta', tag='Fasta')
PapOutputFile.Bam_ = PapOutputFile._CF_enumeration.addEnumeration(unicode_value='Bam', tag='Bam_')
PapOutputFile._InitializeFacetMap(PapOutputFile._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PapOutputFile', PapOutputFile)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 72, 4)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.AverageReadLength = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='AverageReadLength', tag='AverageReadLength')
STD_ANON_2.AcquisitionTime = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='AcquisitionTime', tag='AcquisitionTime')
STD_ANON_2.InsertSize = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='InsertSize', tag='InsertSize')
STD_ANON_2.ReuseComplex = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='ReuseComplex', tag='ReuseComplex')
STD_ANON_2.StageHS = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='StageHS', tag='StageHS')
STD_ANON_2.JobId = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='JobId', tag='JobId')
STD_ANON_2.JobName = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='JobName', tag='JobName')
STD_ANON_2.NumberOfCollections = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='NumberOfCollections', tag='NumberOfCollections')
STD_ANON_2.StrobeByTime = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='StrobeByTime', tag='StrobeByTime')
STD_ANON_2.UsedControl = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='UsedControl', tag='UsedControl')
STD_ANON_2.Use2ndLook = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Use2ndLook', tag='Use2ndLook')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 182, 4)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.PlateId = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='PlateId', tag='PlateId')
STD_ANON_3.PlateDefinition = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='PlateDefinition', tag='PlateDefinition')
STD_ANON_3.SchemaVersion = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='SchemaVersion', tag='SchemaVersion')
STD_ANON_3.DefType = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='DefType', tag='DefType')
STD_ANON_3.Owner = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Owner', tag='Owner')
STD_ANON_3.CreatedBy = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='CreatedBy', tag='CreatedBy')
STD_ANON_3.Comments = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Comments', tag='Comments')
STD_ANON_3.OutputPath = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='OutputPath', tag='OutputPath')
STD_ANON_3.Collections = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Collections', tag='Collections')
STD_ANON_3.Collection = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Collection', tag='Collection')
STD_ANON_3.DNATemplatePrepKitDefinition = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='DNATemplatePrepKitDefinition', tag='DNATemplatePrepKitDefinition')
STD_ANON_3.BindingKitDefinition = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='BindingKitDefinition', tag='BindingKitDefinition')
STD_ANON_3.RunResources = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='RunResources', tag='RunResources')
STD_ANON_3.CompatibleChipLayouts = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='CompatibleChipLayouts', tag='CompatibleChipLayouts')
STD_ANON_3.ChipLayout = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='ChipLayout', tag='ChipLayout')
STD_ANON_3.CompatibleSequencingKits = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='CompatibleSequencingKits', tag='CompatibleSequencingKits')
STD_ANON_3.SequencingKit = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='SequencingKit', tag='SequencingKit')
STD_ANON_3.RequiredTips = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='RequiredTips', tag='RequiredTips')
STD_ANON_3.EstimatedTotalRunTime = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='EstimatedTotalRunTime', tag='EstimatedTotalRunTime')
STD_ANON_3.RequiredSMRTCells = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='RequiredSMRTCells', tag='RequiredSMRTCells')
STD_ANON_3.CollectionAutomation = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='CollectionAutomation', tag='CollectionAutomation')
STD_ANON_3.Basecaller = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Basecaller', tag='Basecaller')
STD_ANON_3.SecondaryAnalysisAutomation = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='SecondaryAnalysisAutomation', tag='SecondaryAnalysisAutomation')
STD_ANON_3.WellNo = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='WellNo', tag='WellNo')
STD_ANON_3.SampleName = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='SampleName', tag='SampleName')
STD_ANON_3.Barcode = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Barcode', tag='Barcode')
STD_ANON_3.AcquisitionTime = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='AcquisitionTime', tag='AcquisitionTime')
STD_ANON_3.InsertSize = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='InsertSize', tag='InsertSize')
STD_ANON_3.ReuseComplex = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='ReuseComplex', tag='ReuseComplex')
STD_ANON_3.StageHS = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='StageHS', tag='StageHS')
STD_ANON_3.NumberOfCollections = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='NumberOfCollections', tag='NumberOfCollections')
STD_ANON_3.Confidence = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Confidence', tag='Confidence')
STD_ANON_3.SampleComment = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='SampleComment', tag='SampleComment')
STD_ANON_3.StrobeByTime = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='StrobeByTime', tag='StrobeByTime')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic simple type: {http://pacificbiosciences.com/PacBioDataModel.xsd}TubeLocation
class TubeLocation (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TubeLocation')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 128, 1)
    _Documentation = None
TubeLocation._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TubeLocation, enum_prefix=None)
TubeLocation.ReagentTube0 = TubeLocation._CF_enumeration.addEnumeration(unicode_value='ReagentTube0', tag='ReagentTube0')
TubeLocation.ReagentTube1 = TubeLocation._CF_enumeration.addEnumeration(unicode_value='ReagentTube1', tag='ReagentTube1')
TubeLocation._InitializeFacetMap(TubeLocation._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TubeLocation', TubeLocation)

# Atomic simple type: {http://pacificbiosciences.com/PacBioDataModel.xsd}TubeSize
class TubeSize (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TubeSize')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 134, 1)
    _Documentation = None
TubeSize._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TubeSize, enum_prefix=None)
TubeSize.DeepTube = TubeSize._CF_enumeration.addEnumeration(unicode_value='DeepTube', tag='DeepTube')
TubeSize.ShallowTube = TubeSize._CF_enumeration.addEnumeration(unicode_value='ShallowTube', tag='ShallowTube')
TubeSize._InitializeFacetMap(TubeSize._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TubeSize', TubeSize)

# Atomic simple type: {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentKey
class ReagentKey (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReagentKey')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 140, 1)
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
ReagentKey._InitializeFacetMap(ReagentKey._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ReagentKey', ReagentKey)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """The root element of the Automation Constraints """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 13, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}AutomationConstraints uses Python identifier AutomationConstraints
    __AutomationConstraints = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationConstraints'), 'AutomationConstraints', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_httppacificbiosciences_comPacBioDataModel_xsdAutomationConstraints', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 19, 1), )

    
    AutomationConstraints = property(__AutomationConstraints.value, __AutomationConstraints.set, None, None)

    _ElementMap.update({
        __AutomationConstraints.name() : __AutomationConstraints
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 20, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}AutomationConstraint uses Python identifier AutomationConstraint
    __AutomationConstraint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationConstraint'), 'AutomationConstraint', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON__httppacificbiosciences_comPacBioDataModel_xsdAutomationConstraint', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 26, 1), )

    
    AutomationConstraint = property(__AutomationConstraint.value, __AutomationConstraint.set, None, None)

    _ElementMap.update({
        __AutomationConstraint.name() : __AutomationConstraint
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Names of automations that are all similarly constrained"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 38, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Automation uses Python identifier Automation
    __Automation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Automation'), 'Automation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_2_httppacificbiosciences_comPacBioDataModel_xsdAutomation', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 40, 8), )

    
    Automation = property(__Automation.value, __Automation.set, None, None)

    _ElementMap.update({
        __Automation.name() : __Automation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """A list of insert sizes (buckets) recommended for use"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 48, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}InsertSize uses Python identifier InsertSize
    __InsertSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InsertSize'), 'InsertSize', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_3_httppacificbiosciences_comPacBioDataModel_xsdInsertSize', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 50, 8), )

    
    InsertSize = property(__InsertSize.value, __InsertSize.set, None, None)

    _ElementMap.update({
        __InsertSize.name() : __InsertSize
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 58, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ExtensionElement uses Python identifier ExtensionElement
    __ExtensionElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExtensionElement'), 'ExtensionElement', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_4_httppacificbiosciences_comPacBioDataModel_xsdExtensionElement', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 640, 1), )

    
    ExtensionElement = property(__ExtensionElement.value, __ExtensionElement.set, None, 'A generic element whose contents are undefined at the schema level.  This is used to extend the data model.')

    _ElementMap.update({
        __ExtensionElement.name() : __ExtensionElement
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Pointer to Run/Outputs/Output/@UniqueId"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 172, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DataPointer uses Python identifier DataPointer
    __DataPointer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataPointer'), 'DataPointer', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_5_httppacificbiosciences_comPacBioDataModel_xsdDataPointer', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 174, 4), )

    
    DataPointer = property(__DataPointer.value, __DataPointer.set, None, None)

    _ElementMap.update({
        __DataPointer.name() : __DataPointer
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Pointers to data that do not reside inside the parent structure"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 206, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResource uses Python identifier ExternalResource
    __ExternalResource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExternalResource'), 'ExternalResource', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_6_httppacificbiosciences_comPacBioDataModel_xsdExternalResource', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 662, 1), )

    
    ExternalResource = property(__ExternalResource.value, __ExternalResource.set, None, 'for example, an output file could be the BAM file, which could be associated with multiple indices into it.')

    _ElementMap.update({
        __ExternalResource.name() : __ExternalResource
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 222, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}FileIndex uses Python identifier FileIndex
    __FileIndex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FileIndex'), 'FileIndex', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_7_httppacificbiosciences_comPacBioDataModel_xsdFileIndex', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 224, 8), )

    
    FileIndex = property(__FileIndex.value, __FileIndex.set, None, 'e.g. index for output files, allowing one to find information in the output file')

    _ElementMap.update({
        __FileIndex.name() : __FileIndex
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 242, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}AutomationParameter uses Python identifier AutomationParameter
    __AutomationParameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter'), 'AutomationParameter', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_8_httppacificbiosciences_comPacBioDataModel_xsdAutomationParameter', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 253, 1), )

    
    AutomationParameter = property(__AutomationParameter.value, __AutomationParameter.set, None, 'One or more collection parameters, such as MovieLength, InsertSize, UseStageStart, IsControl, etc..')

    _ElementMap.update({
        __AutomationParameter.name() : __AutomationParameter
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """By default, a PN is compatible for use with other PNs in the system.  In order to exclude the usage of one or more PNs with this one, the incompatible PNs are listed here."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 271, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatiblePartNumber uses Python identifier IncompatiblePartNumber
    __IncompatiblePartNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePartNumber'), 'IncompatiblePartNumber', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_9_httppacificbiosciences_comPacBioDataModel_xsdIncompatiblePartNumber', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 273, 8), )

    
    IncompatiblePartNumber = property(__IncompatiblePartNumber.value, __IncompatiblePartNumber.set, None, 'A reference to the incompatible part number UID')

    _ElementMap.update({
        __IncompatiblePartNumber.name() : __IncompatiblePartNumber
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """By default, a PN is compatible for use with all automations in the system.  In order to exclude the usage of automations with this PN, the incompatible automation names are listed here."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 285, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatibleAutomation uses Python identifier IncompatibleAutomation
    __IncompatibleAutomation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleAutomation'), 'IncompatibleAutomation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_10_httppacificbiosciences_comPacBioDataModel_xsdIncompatibleAutomation', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 287, 8), )

    
    IncompatibleAutomation = property(__IncompatibleAutomation.value, __IncompatibleAutomation.set, None, 'A reference to the incompatible automation type UID')

    _ElementMap.update({
        __IncompatibleAutomation.name() : __IncompatibleAutomation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 347, 11)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Analog uses Python identifier Analog
    __Analog = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Analog'), 'Analog', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_11_httppacificbiosciences_comPacBioDataModel_xsdAnalog', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 349, 13), )

    
    Analog = property(__Analog.value, __Analog.set, None, None)

    _ElementMap.update({
        __Analog.name() : __Analog
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Root element for document containing the container of analog set, SequencingChemistryConfig"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 366, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ChemistryConfig uses Python identifier ChemistryConfig
    __ChemistryConfig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChemistryConfig'), 'ChemistryConfig', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_12_httppacificbiosciences_comPacBioDataModel_xsdChemistryConfig', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 368, 4), )

    
    ChemistryConfig = property(__ChemistryConfig.value, __ChemistryConfig.set, None, None)

    _ElementMap.update({
        __ChemistryConfig.name() : __ChemistryConfig
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 380, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Analog uses Python identifier Analog
    __Analog = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Analog'), 'Analog', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_13_httppacificbiosciences_comPacBioDataModel_xsdAnalog', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 382, 8), )

    
    Analog = property(__Analog.value, __Analog.set, None, None)

    _ElementMap.update({
        __Analog.name() : __Analog
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 404, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BinCount uses Python identifier BinCount
    __BinCount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinCount'), 'BinCount', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_14_httppacificbiosciences_comPacBioDataModel_xsdBinCount', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 406, 8), )

    
    BinCount = property(__BinCount.value, __BinCount.set, None, None)

    _ElementMap.update({
        __BinCount.name() : __BinCount
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 430, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BinCount uses Python identifier BinCount
    __BinCount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinCount'), 'BinCount', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_15_httppacificbiosciences_comPacBioDataModel_xsdBinCount', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 432, 8), )

    
    BinCount = property(__BinCount.value, __BinCount.set, None, None)

    _ElementMap.update({
        __BinCount.name() : __BinCount
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 438, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BinLabel uses Python identifier BinLabel
    __BinLabel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinLabel'), 'BinLabel', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_16_httppacificbiosciences_comPacBioDataModel_xsdBinLabel', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 440, 8), )

    
    BinLabel = property(__BinLabel.value, __BinLabel.set, None, None)

    _ElementMap.update({
        __BinLabel.name() : __BinLabel
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
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 460, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Val uses Python identifier Val
    __Val = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Val'), 'Val', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_17_httppacificbiosciences_comPacBioDataModel_xsdVal', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 462, 8), )

    
    Val = property(__Val.value, __Val.set, None, None)

    _ElementMap.update({
        __Val.name() : __Val
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}UserDefinedFieldsType with content type ELEMENT_ONLY
class UserDefinedFieldsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}UserDefinedFieldsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UserDefinedFieldsType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 633, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntities uses Python identifier DataEntities
    __DataEntities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataEntities'), 'DataEntities', '__httppacificbiosciences_comPacBioDataModel_xsd_UserDefinedFieldsType_httppacificbiosciences_comPacBioDataModel_xsdDataEntities', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 635, 3), )

    
    DataEntities = property(__DataEntities.value, __DataEntities.set, None, None)

    _ElementMap.update({
        __DataEntities.name() : __DataEntities
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'UserDefinedFieldsType', UserDefinedFieldsType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}FilterType with content type ELEMENT_ONLY
class FilterType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}FilterType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FilterType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 645, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Properties uses Python identifier Properties
    __Properties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Properties'), 'Properties', '__httppacificbiosciences_comPacBioDataModel_xsd_FilterType_httppacificbiosciences_comPacBioDataModel_xsdProperties', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 647, 3), )

    
    Properties = property(__Properties.value, __Properties.set, None, None)

    _ElementMap.update({
        __Properties.name() : __Properties
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'FilterType', FilterType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 648, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Property uses Python identifier Property
    __Property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Property'), 'Property', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_18_httppacificbiosciences_comPacBioDataModel_xsdProperty', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 650, 6), )

    
    Property = property(__Property.value, __Property.set, None, None)

    _ElementMap.update({
        __Property.name() : __Property
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 651, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_19_Name', pyxb.binding.datatypes.string, required=True)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 652, 8)
    __Name._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 652, 8)
    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_19_Value', pyxb.binding.datatypes.string, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 653, 8)
    __Value._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 653, 8)
    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Attribute Operator uses Python identifier Operator
    __Operator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Operator'), 'Operator', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_19_Operator', pyxb.binding.datatypes.string, required=True)
    __Operator._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 654, 8)
    __Operator._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 654, 8)
    
    Operator = property(__Operator.value, __Operator.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Name.name() : __Name,
        __Value.name() : __Value,
        __Operator.name() : __Operator
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Root element of a standalone CollectionMetadata file."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 13, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CollectionMetadata uses Python identifier CollectionMetadata
    __CollectionMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata'), 'CollectionMetadata', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_20_httppacificbiosciences_comPacBioDataModel_xsdCollectionMetadata', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 136, 1), )

    
    CollectionMetadata = property(__CollectionMetadata.value, __CollectionMetadata.set, None, 'Root-level element for the metadata.  The purpose of which is to contain pertinent instrument information related to the conditions present during a movie acquisition.  It also serves to provide key pieces of information for integration with primary and secondary analysis.  This file is associated with 1 movie. ')

    _ElementMap.update({
        __CollectionMetadata.name() : __CollectionMetadata
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType with content type ELEMENT_ONLY
class DataSetMetadataType (pyxb.binding.basis.complexTypeDefinition):
    """Extend this type to provide DataSetMetadata element in each DataSet."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 31, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}TotalLength uses Python identifier TotalLength
    __TotalLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TotalLength'), 'TotalLength', '__httppacificbiosciences_comPacBioDataModel_xsd_DataSetMetadataType_httppacificbiosciences_comPacBioDataModel_xsdTotalLength', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 36, 3), )

    
    TotalLength = property(__TotalLength.value, __TotalLength.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}NumRecords uses Python identifier NumRecords
    __NumRecords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumRecords'), 'NumRecords', '__httppacificbiosciences_comPacBioDataModel_xsd_DataSetMetadataType_httppacificbiosciences_comPacBioDataModel_xsdNumRecords', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 37, 3), )

    
    NumRecords = property(__NumRecords.value, __NumRecords.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Provenance uses Python identifier Provenance
    __Provenance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Provenance'), 'Provenance', '__httppacificbiosciences_comPacBioDataModel_xsd_DataSetMetadataType_httppacificbiosciences_comPacBioDataModel_xsdProvenance', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3), )

    
    Provenance = property(__Provenance.value, __Provenance.set, None, None)

    _ElementMap.update({
        __TotalLength.name() : __TotalLength,
        __NumRecords.name() : __NumRecords,
        __Provenance.name() : __Provenance
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DataSetMetadataType', DataSetMetadataType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 66, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}AdapterDimerFraction uses Python identifier AdapterDimerFraction
    __AdapterDimerFraction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdapterDimerFraction'), 'AdapterDimerFraction', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_21_httppacificbiosciences_comPacBioDataModel_xsdAdapterDimerFraction', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 68, 8), )

    
    AdapterDimerFraction = property(__AdapterDimerFraction.value, __AdapterDimerFraction.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ShortInsertFraction uses Python identifier ShortInsertFraction
    __ShortInsertFraction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ShortInsertFraction'), 'ShortInsertFraction', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_21_httppacificbiosciences_comPacBioDataModel_xsdShortInsertFraction', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 69, 8), )

    
    ShortInsertFraction = property(__ShortInsertFraction.value, __ShortInsertFraction.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}NumSequencingZmws uses Python identifier NumSequencingZmws
    __NumSequencingZmws = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumSequencingZmws'), 'NumSequencingZmws', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_21_httppacificbiosciences_comPacBioDataModel_xsdNumSequencingZmws', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 70, 8), )

    
    NumSequencingZmws = property(__NumSequencingZmws.value, __NumSequencingZmws.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ProdDist uses Python identifier ProdDist
    __ProdDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ProdDist'), 'ProdDist', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_21_httppacificbiosciences_comPacBioDataModel_xsdProdDist', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 71, 8), )

    
    ProdDist = property(__ProdDist.value, __ProdDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ReadTypeDist uses Python identifier ReadTypeDist
    __ReadTypeDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReadTypeDist'), 'ReadTypeDist', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_21_httppacificbiosciences_comPacBioDataModel_xsdReadTypeDist', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 72, 8), )

    
    ReadTypeDist = property(__ReadTypeDist.value, __ReadTypeDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ReadLenDist uses Python identifier ReadLenDist
    __ReadLenDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReadLenDist'), 'ReadLenDist', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_21_httppacificbiosciences_comPacBioDataModel_xsdReadLenDist', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 73, 8), )

    
    ReadLenDist = property(__ReadLenDist.value, __ReadLenDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ReadQualDist uses Python identifier ReadQualDist
    __ReadQualDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReadQualDist'), 'ReadQualDist', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_21_httppacificbiosciences_comPacBioDataModel_xsdReadQualDist', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 74, 8), )

    
    ReadQualDist = property(__ReadQualDist.value, __ReadQualDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ControlReadLenDist uses Python identifier ControlReadLenDist
    __ControlReadLenDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlReadLenDist'), 'ControlReadLenDist', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_21_httppacificbiosciences_comPacBioDataModel_xsdControlReadLenDist', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 75, 8), )

    
    ControlReadLenDist = property(__ControlReadLenDist.value, __ControlReadLenDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ControlReadQualDist uses Python identifier ControlReadQualDist
    __ControlReadQualDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlReadQualDist'), 'ControlReadQualDist', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_21_httppacificbiosciences_comPacBioDataModel_xsdControlReadQualDist', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 76, 8), )

    
    ControlReadQualDist = property(__ControlReadQualDist.value, __ControlReadQualDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}MedianInsertDist uses Python identifier MedianInsertDist
    __MedianInsertDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MedianInsertDist'), 'MedianInsertDist', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_21_httppacificbiosciences_comPacBioDataModel_xsdMedianInsertDist', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 77, 8), )

    
    MedianInsertDist = property(__MedianInsertDist.value, __MedianInsertDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}InsertReadLenDist uses Python identifier InsertReadLenDist
    __InsertReadLenDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InsertReadLenDist'), 'InsertReadLenDist', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_21_httppacificbiosciences_comPacBioDataModel_xsdInsertReadLenDist', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 78, 8), )

    
    InsertReadLenDist = property(__InsertReadLenDist.value, __InsertReadLenDist.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}InsertReadQualDist uses Python identifier InsertReadQualDist
    __InsertReadQualDist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InsertReadQualDist'), 'InsertReadQualDist', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_21_httppacificbiosciences_comPacBioDataModel_xsdInsertReadQualDist', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 79, 8), )

    
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
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 108, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Filter uses Python identifier Filter
    __Filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Filter'), 'Filter', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_22_httppacificbiosciences_comPacBioDataModel_xsdFilter', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 110, 8), )

    
    Filter = property(__Filter.value, __Filter.set, None, None)

    _ElementMap.update({
        __Filter.name() : __Filter
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 115, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSet uses Python identifier DataSet
    __DataSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSet'), 'DataSet', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_23_httppacificbiosciences_comPacBioDataModel_xsdDataSet', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 135, 1), )

    
    DataSet = property(__DataSet.value, __DataSet.set, None, None)

    _ElementMap.update({
        __DataSet.name() : __DataSet
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """A set of acquisition definitions"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 129, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CollectionMetadata uses Python identifier CollectionMetadata
    __CollectionMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata'), 'CollectionMetadata', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_24_httppacificbiosciences_comPacBioDataModel_xsdCollectionMetadata', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 136, 1), )

    
    CollectionMetadata = property(__CollectionMetadata.value, __CollectionMetadata.set, None, 'Root-level element for the metadata.  The purpose of which is to contain pertinent instrument information related to the conditions present during a movie acquisition.  It also serves to provide key pieces of information for integration with primary and secondary analysis.  This file is associated with 1 movie. ')

    _ElementMap.update({
        __CollectionMetadata.name() : __CollectionMetadata
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """Information related to an instrument run.  A run can contain multiple chips, wells, and movies. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 252, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RunId uses Python identifier RunId
    __RunId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RunId'), 'RunId', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_25_httppacificbiosciences_comPacBioDataModel_xsdRunId', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 254, 4), )

    
    RunId = property(__RunId.value, __RunId.set, None, 'A unique identifier for this run.  Format is r[sid]_[iname]_[ts]. Where [id] is a system generated id and [iname] is the instrument name and [ts] is a timestamp YYMMDD Example:  r000123_00117_100713 ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Name'), 'Name', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_25_httppacificbiosciences_comPacBioDataModel_xsdName', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 259, 4), )

    
    Name = property(__Name.value, __Name.set, None, 'Assigned name for a run, which consists of multiple wells. There is no constraint on the uniqueness of this data. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CreatedBy uses Python identifier CreatedBy
    __CreatedBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CreatedBy'), 'CreatedBy', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_25_httppacificbiosciences_comPacBioDataModel_xsdCreatedBy', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 264, 4), )

    
    CreatedBy = property(__CreatedBy.value, __CreatedBy.set, None, 'Who created the run. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}WhenCreated uses Python identifier WhenCreated
    __WhenCreated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WhenCreated'), 'WhenCreated', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_25_httppacificbiosciences_comPacBioDataModel_xsdWhenCreated', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 269, 4), )

    
    WhenCreated = property(__WhenCreated.value, __WhenCreated.set, None, 'Date and time of when the overall run was created in the system. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}StartedBy uses Python identifier StartedBy
    __StartedBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartedBy'), 'StartedBy', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_25_httppacificbiosciences_comPacBioDataModel_xsdStartedBy', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 274, 4), )

    
    StartedBy = property(__StartedBy.value, __StartedBy.set, None, 'Who started the run. Could be different from who created it. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}WhenStarted uses Python identifier WhenStarted
    __WhenStarted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WhenStarted'), 'WhenStarted', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_25_httppacificbiosciences_comPacBioDataModel_xsdWhenStarted', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 279, 4), )

    
    WhenStarted = property(__WhenStarted.value, __WhenStarted.set, None, 'Date and time of when the overall run was started. ')

    _ElementMap.update({
        __RunId.name() : __RunId,
        __Name.name() : __Name,
        __CreatedBy.name() : __CreatedBy,
        __WhenCreated.name() : __WhenCreated,
        __StartedBy.name() : __StartedBy,
        __WhenStarted.name() : __WhenStarted
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """A movie corresponds to one acquisition for a chip, one set (look) and one strobe. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 291, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}WhenStarted uses Python identifier WhenStarted
    __WhenStarted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WhenStarted'), 'WhenStarted', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_26_httppacificbiosciences_comPacBioDataModel_xsdWhenStarted', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 293, 4), )

    
    WhenStarted = property(__WhenStarted.value, __WhenStarted.set, None, 'Date and time of when this movie acquisition started. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DurationInSec uses Python identifier DurationInSec
    __DurationInSec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DurationInSec'), 'DurationInSec', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_26_httppacificbiosciences_comPacBioDataModel_xsdDurationInSec', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 298, 4), )

    
    DurationInSec = property(__DurationInSec.value, __DurationInSec.set, None, 'The actual length of the movie acquisition (in seconds), irrespective of the movie duration specified by an automation parameter. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Number uses Python identifier Number
    __Number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Number'), 'Number', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_26_httppacificbiosciences_comPacBioDataModel_xsdNumber', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 303, 4), )

    
    Number = property(__Number.value, __Number.set, None, "The number of this movie within the set (i.e., look).  This is unique when combined with the 'SetNumber'. ")

    _ElementMap.update({
        __WhenStarted.name() : __WhenStarted,
        __DurationInSec.name() : __DurationInSec,
        __Number.name() : __Number
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Container for the expired consumable data. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 315, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}EightPacPastExpiration uses Python identifier EightPacPastExpiration
    __EightPacPastExpiration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EightPacPastExpiration'), 'EightPacPastExpiration', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_27_httppacificbiosciences_comPacBioDataModel_xsdEightPacPastExpiration', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 317, 4), )

    
    EightPacPastExpiration = property(__EightPacPastExpiration.value, __EightPacPastExpiration.set, None, 'Number of days past expiration the eight pac was (if at all). ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentKitPastExpiration uses Python identifier ReagentKitPastExpiration
    __ReagentKitPastExpiration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentKitPastExpiration'), 'ReagentKitPastExpiration', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_27_httppacificbiosciences_comPacBioDataModel_xsdReagentKitPastExpiration', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 322, 4), )

    
    ReagentKitPastExpiration = property(__ReagentKitPastExpiration.value, __ReagentKitPastExpiration.set, None, 'Number of days past expiration the reagent kit was (if at all). ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentTube0PastExpiration uses Python identifier ReagentTube0PastExpiration
    __ReagentTube0PastExpiration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube0PastExpiration'), 'ReagentTube0PastExpiration', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_27_httppacificbiosciences_comPacBioDataModel_xsdReagentTube0PastExpiration', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 327, 4), )

    
    ReagentTube0PastExpiration = property(__ReagentTube0PastExpiration.value, __ReagentTube0PastExpiration.set, None, 'Number of days past expiration the reagent tube 0 was (if at all). ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentTube1PastExpiration uses Python identifier ReagentTube1PastExpiration
    __ReagentTube1PastExpiration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube1PastExpiration'), 'ReagentTube1PastExpiration', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_27_httppacificbiosciences_comPacBioDataModel_xsdReagentTube1PastExpiration', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 332, 4), )

    
    ReagentTube1PastExpiration = property(__ReagentTube1PastExpiration.value, __ReagentTube1PastExpiration.set, None, 'Number of days past expiration the reagent tube 1 was (if at all). ')

    _ElementMap.update({
        __EightPacPastExpiration.name() : __EightPacPastExpiration,
        __ReagentKitPastExpiration.name() : __ReagentKitPastExpiration,
        __ReagentTube0PastExpiration.name() : __ReagentTube0PastExpiration,
        __ReagentTube1PastExpiration.name() : __ReagentTube1PastExpiration
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """A list of barcodes associated with the biological sample"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 351, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Barcode uses Python identifier Barcode
    __Barcode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Barcode'), 'Barcode', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_28_httppacificbiosciences_comPacBioDataModel_xsdBarcode', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 353, 8), )

    
    Barcode = property(__Barcode.value, __Barcode.set, None, 'A sequence of barcodes associated with the biological sample')

    _ElementMap.update({
        __Barcode.name() : __Barcode
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """Container for the primary analysis related data. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 507, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SampleTrace uses Python identifier SampleTrace
    __SampleTrace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SampleTrace'), 'SampleTrace', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_29_httppacificbiosciences_comPacBioDataModel_xsdSampleTrace', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 509, 4), )

    
    SampleTrace = property(__SampleTrace.value, __SampleTrace.set, None, 'Tag to indicate that the trace file will be sampled. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}AutomationName uses Python identifier AutomationName
    __AutomationName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationName'), 'AutomationName', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_29_httppacificbiosciences_comPacBioDataModel_xsdAutomationName', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 528, 4), )

    
    AutomationName = property(__AutomationName.value, __AutomationName.set, None, 'Name of primary analysis protocol. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ConfigFileName uses Python identifier ConfigFileName
    __ConfigFileName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ConfigFileName'), 'ConfigFileName', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_29_httppacificbiosciences_comPacBioDataModel_xsdConfigFileName', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 533, 4), )

    
    ConfigFileName = property(__ConfigFileName.value, __ConfigFileName.set, None, 'Name of primary analysis config file. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SequencingCondition uses Python identifier SequencingCondition
    __SequencingCondition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingCondition'), 'SequencingCondition', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_29_httppacificbiosciences_comPacBioDataModel_xsdSequencingCondition', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 538, 4), )

    
    SequencingCondition = property(__SequencingCondition.value, __SequencingCondition.set, None, 'A sequencing condition tag to be used by primary analysis, e.g., to select basecaller calibration or training parameters. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ResultsFolder uses Python identifier ResultsFolder
    __ResultsFolder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResultsFolder'), 'ResultsFolder', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_29_httppacificbiosciences_comPacBioDataModel_xsdResultsFolder', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 543, 4), )

    
    ResultsFolder = property(__ResultsFolder.value, __ResultsFolder.set, None, "NOTE: not for customers. A sub-folder under the CollectionPath created by Primary Analysis. This is a field that will be updated by the primary analysis pipeline.  The default (as created by homer) should be set to 'Reports_Sms' for now.  Consumers of the data should be aware that they will find collection metadata (and trace files if acquisition is so-configured) at the CollectionPathUri, and all primary analysis results in the sub-folder PrimaryResultsFolder. ")

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CollectionPathUri uses Python identifier CollectionPathUri
    __CollectionPathUri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollectionPathUri'), 'CollectionPathUri', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_29_httppacificbiosciences_comPacBioDataModel_xsdCollectionPathUri', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 548, 4), )

    
    CollectionPathUri = property(__CollectionPathUri.value, __CollectionPathUri.set, None, 'User-specified location of where the results should be copied after an analysis has been completed. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CopyFiles uses Python identifier CopyFiles
    __CopyFiles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CopyFiles'), 'CopyFiles', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_29_httppacificbiosciences_comPacBioDataModel_xsdCopyFiles', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 553, 4), )

    
    CopyFiles = property(__CopyFiles.value, __CopyFiles.set, None, None)

    _ElementMap.update({
        __SampleTrace.name() : __SampleTrace,
        __AutomationName.name() : __AutomationName,
        __ConfigFileName.name() : __ConfigFileName,
        __SequencingCondition.name() : __SequencingCondition,
        __ResultsFolder.name() : __ResultsFolder,
        __CollectionPathUri.name() : __CollectionPathUri,
        __CopyFiles.name() : __CopyFiles
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """Tag to indicate that the trace file will be sampled. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 513, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}TraceSamplingFactor uses Python identifier TraceSamplingFactor
    __TraceSamplingFactor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TraceSamplingFactor'), 'TraceSamplingFactor', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_30_httppacificbiosciences_comPacBioDataModel_xsdTraceSamplingFactor', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 515, 7), )

    
    TraceSamplingFactor = property(__TraceSamplingFactor.value, __TraceSamplingFactor.set, None, 'Percentage of traces to sample. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}FullPulseFile uses Python identifier FullPulseFile
    __FullPulseFile = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FullPulseFile'), 'FullPulseFile', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_30_httppacificbiosciences_comPacBioDataModel_xsdFullPulseFile', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 520, 7), )

    
    FullPulseFile = property(__FullPulseFile.value, __FullPulseFile.set, None, 'Whether full or sampled pulse file is transferred if requested. ')

    _ElementMap.update({
        __TraceSamplingFactor.name() : __TraceSamplingFactor,
        __FullPulseFile.name() : __FullPulseFile
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 554, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CollectionFileCopy uses Python identifier CollectionFileCopy
    __CollectionFileCopy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollectionFileCopy'), 'CollectionFileCopy', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_31_httppacificbiosciences_comPacBioDataModel_xsdCollectionFileCopy', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 556, 7), )

    
    CollectionFileCopy = property(__CollectionFileCopy.value, __CollectionFileCopy.set, None, 'Defines the set of files to be copied to the CollectionPathUri. 1 or more. ')

    _ElementMap.update({
        __CollectionFileCopy.name() : __CollectionFileCopy
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """Container for the primary analysis related data. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 572, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}AutomationName uses Python identifier AutomationName
    __AutomationName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationName'), 'AutomationName', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_32_httppacificbiosciences_comPacBioDataModel_xsdAutomationName', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 574, 4), )

    
    AutomationName = property(__AutomationName.value, __AutomationName.set, None, 'The secondary analysis protocol name specified in the sample sheet. Ignored by secondary. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}AutomationParameters uses Python identifier AutomationParameters
    __AutomationParameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameters'), 'AutomationParameters', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_32_httppacificbiosciences_comPacBioDataModel_xsdAutomationParameters', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 579, 4), )

    
    AutomationParameters = property(__AutomationParameters.value, __AutomationParameters.set, None, 'The parameters for secondary analysis specified in the sample sheet. Ignored by secondary. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CellCountInJob uses Python identifier CellCountInJob
    __CellCountInJob = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CellCountInJob'), 'CellCountInJob', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_32_httppacificbiosciences_comPacBioDataModel_xsdCellCountInJob', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 593, 4), )

    
    CellCountInJob = property(__CellCountInJob.value, __CellCountInJob.set, None, "The number of cells in this secondary analysis job, identified by the secondary analysis parameter 'JobName'.  Supports automated secondary analysis. ")

    _ElementMap.update({
        __AutomationName.name() : __AutomationName,
        __AutomationParameters.name() : __AutomationParameters,
        __CellCountInJob.name() : __CellCountInJob
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    """The parameters for secondary analysis specified in the sample sheet. Ignored by secondary. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 583, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}AutomationParameter uses Python identifier AutomationParameter
    __AutomationParameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter'), 'AutomationParameter', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_33_httppacificbiosciences_comPacBioDataModel_xsdAutomationParameter', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 585, 7), )

    
    AutomationParameter = property(__AutomationParameter.value, __AutomationParameter.set, None, 'One or more secondary analysis parameters, such as JobName, Workflow, etc..')

    _ElementMap.update({
        __AutomationParameter.name() : __AutomationParameter
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    """One custom, possibly non-unique, key-value pair. """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 611, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute key uses Python identifier key
    __key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'key'), 'key', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_34_key', pyxb.binding.datatypes.string, required=True)
    __key._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 614, 5)
    __key._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 614, 5)
    
    key = property(__key.value, __key.set, None, 'Key (attribute) and Value (element content). ')

    
    # Attribute label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_34_label', pyxb.binding.datatypes.string)
    __label._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 619, 5)
    __label._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 619, 5)
    
    label = property(__label.value, __label.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __key.name() : __key,
        __label.name() : __label
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    """Back references to other BarcodedSampleType object UniqueIds which utilize this sample"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 643, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSamplePointer uses Python identifier BioSamplePointer
    __BioSamplePointer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BioSamplePointer'), 'BioSamplePointer', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_35_httppacificbiosciences_comPacBioDataModel_xsdBioSamplePointer', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 650, 5), )

    
    BioSamplePointer = property(__BioSamplePointer.value, __BioSamplePointer.set, None, 'Pointer to a single biological sample')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BarcodedSamplePointers uses Python identifier BarcodedSamplePointers
    __BarcodedSamplePointers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointers'), 'BarcodedSamplePointers', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_35_httppacificbiosciences_comPacBioDataModel_xsdBarcodedSamplePointers', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 659, 1), )

    
    BarcodedSamplePointers = property(__BarcodedSamplePointers.value, __BarcodedSamplePointers.set, None, 'Back references to other BarcodedSampleType object UniqueIds which utilize this sample')

    _ElementMap.update({
        __BioSamplePointer.name() : __BioSamplePointer,
        __BarcodedSamplePointers.name() : __BarcodedSamplePointers
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    """Back references to other BarcodedSampleType object UniqueIds which utilize this sample"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 663, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BarcodedSamplePointer uses Python identifier BarcodedSamplePointer
    __BarcodedSamplePointer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointer'), 'BarcodedSamplePointer', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_36_httppacificbiosciences_comPacBioDataModel_xsdBarcodedSamplePointer', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 665, 4), )

    
    BarcodedSamplePointer = property(__BarcodedSamplePointer.value, __BarcodedSamplePointer.set, None, 'Pointer to a group of barcoded samples')

    _ElementMap.update({
        __BarcodedSamplePointer.name() : __BarcodedSamplePointer
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 674, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSample uses Python identifier BioSample
    __BioSample = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BioSample'), 'BioSample', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_37_httppacificbiosciences_comPacBioDataModel_xsdBioSample', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 680, 1), )

    
    BioSample = property(__BioSample.value, __BioSample.set, None, None)

    _ElementMap.update({
        __BioSample.name() : __BioSample
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_38 (pyxb.binding.basis.complexTypeDefinition):
    """Part of the RunResources; specifies a ChipLayout which is compatible with the collection protocols defined on the plate"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 16, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_38_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_38_Name', pyxb.binding.datatypes.string, required=True)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 20, 3)
    __Name._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 20, 3)
    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Attribute PartNumber uses Python identifier PartNumber
    __PartNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PartNumber'), 'PartNumber', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_38_PartNumber', pyxb.binding.datatypes.string, required=True)
    __PartNumber._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 21, 3)
    __PartNumber._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 21, 3)
    
    PartNumber = property(__PartNumber.value, __PartNumber.set, None, None)

    _ElementMap.update({
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        __Name.name() : __Name,
        __PartNumber.name() : __PartNumber
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_39 (pyxb.binding.basis.complexTypeDefinition):
    """A set of Chip Layouts deemed compatible with the current plate"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 28, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ChipLayout uses Python identifier ChipLayout
    __ChipLayout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout'), 'ChipLayout', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_39_httppacificbiosciences_comPacBioDataModel_xsdChipLayout', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 12, 1), )

    
    ChipLayout = property(__ChipLayout.value, __ChipLayout.set, None, 'Part of the RunResources; specifies a ChipLayout which is compatible with the collection protocols defined on the plate')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RequiredSMRTCells uses Python identifier RequiredSMRTCells
    __RequiredSMRTCells = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RequiredSMRTCells'), 'RequiredSMRTCells', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_39_httppacificbiosciences_comPacBioDataModel_xsdRequiredSMRTCells', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 106, 1), )

    
    RequiredSMRTCells = property(__RequiredSMRTCells.value, __RequiredSMRTCells.set, None, 'Part of the RunResources; specifies the required number of SMRT cells')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_39_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    _ElementMap.update({
        __ChipLayout.name() : __ChipLayout,
        __RequiredSMRTCells.name() : __RequiredSMRTCells,
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_40 (pyxb.binding.basis.complexTypeDefinition):
    """A set of reagent kits deemed compatible with the current plate"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 40, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}EstimatedTotalRunTime uses Python identifier EstimatedTotalRunTime
    __EstimatedTotalRunTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EstimatedTotalRunTime'), 'EstimatedTotalRunTime', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_40_httppacificbiosciences_comPacBioDataModel_xsdEstimatedTotalRunTime', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 48, 1), )

    
    EstimatedTotalRunTime = property(__EstimatedTotalRunTime.value, __EstimatedTotalRunTime.set, None, 'The total amount of time the run is estimated to require.  A confidence value (defaulted to 90%) indicates the degree of certainty associated with the estimate')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RequiredTips uses Python identifier RequiredTips
    __RequiredTips = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RequiredTips'), 'RequiredTips', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_40_httppacificbiosciences_comPacBioDataModel_xsdRequiredTips', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 117, 1), )

    
    RequiredTips = property(__RequiredTips.value, __RequiredTips.set, None, 'Part of the RunResources; specifies the required number of tips via two attributes, Left and Right')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SequencingKit uses Python identifier SequencingKit
    __SequencingKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit'), 'SequencingKit', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_40_httppacificbiosciences_comPacBioDataModel_xsdSequencingKit', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 67, 1), )

    
    SequencingKit = property(__SequencingKit.value, __SequencingKit.set, None, None)

    _ElementMap.update({
        __EstimatedTotalRunTime.name() : __EstimatedTotalRunTime,
        __RequiredTips.name() : __RequiredTips,
        __SequencingKit.name() : __SequencingKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_41 (pyxb.binding.basis.complexTypeDefinition):
    """The total amount of time the run is estimated to require.  A confidence value (defaulted to 90%) indicates the degree of certainty associated with the estimate"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 52, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_41_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_41_Value', pyxb.binding.datatypes.string, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 56, 3)
    __Value._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 56, 3)
    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Attribute Confidence uses Python identifier Confidence
    __Confidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Confidence'), 'Confidence', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_41_Confidence', pyxb.binding.datatypes.int, required=True)
    __Confidence._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 57, 3)
    __Confidence._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 57, 3)
    
    Confidence = property(__Confidence.value, __Confidence.set, None, None)

    _ElementMap.update({
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        __Value.name() : __Value,
        __Confidence.name() : __Confidence
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_42 (pyxb.binding.basis.complexTypeDefinition):
    """PacBio Data Model root element"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 95, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ExperimentContainer uses Python identifier ExperimentContainer
    __ExperimentContainer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExperimentContainer'), 'ExperimentContainer', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_42_httppacificbiosciences_comPacBioDataModel_xsdExperimentContainer', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 97, 4), )

    
    ExperimentContainer = property(__ExperimentContainer.value, __ExperimentContainer.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __ExperimentContainer.name() : __ExperimentContainer
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_43 (pyxb.binding.basis.complexTypeDefinition):
    """Part of the RunResources; specifies the required number of SMRT cells"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 110, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_43_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    
    # Attribute Quantity uses Python identifier Quantity
    __Quantity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Quantity'), 'Quantity', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_43_Quantity', pyxb.binding.datatypes.int, required=True)
    __Quantity._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 114, 3)
    __Quantity._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 114, 3)
    
    Quantity = property(__Quantity.value, __Quantity.set, None, None)

    _ElementMap.update({
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        __Quantity.name() : __Quantity
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_44 (pyxb.binding.basis.complexTypeDefinition):
    """Part of the RunResources; specifies the required number of tips via two attributes, Left and Right"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 121, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_44_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    
    # Attribute Left uses Python identifier Left
    __Left = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Left'), 'Left', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_44_Left', pyxb.binding.datatypes.int, required=True)
    __Left._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 125, 3)
    __Left._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 125, 3)
    
    Left = property(__Left.value, __Left.set, None, None)

    
    # Attribute Right uses Python identifier Right
    __Right = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Right'), 'Right', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_44_Right', pyxb.binding.datatypes.int, required=True)
    __Right._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 126, 3)
    __Right._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 126, 3)
    
    Right = property(__Right.value, __Right.set, None, None)

    _ElementMap.update({
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        __Left.name() : __Left,
        __Right.name() : __Right
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_45 (pyxb.binding.basis.complexTypeDefinition):
    """This is an output field specifying the requirements for the run, e.g. number of tips, estimated run time, etc."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 133, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CompatibleChipLayouts uses Python identifier CompatibleChipLayouts
    __CompatibleChipLayouts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CompatibleChipLayouts'), 'CompatibleChipLayouts', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_45_httppacificbiosciences_comPacBioDataModel_xsdCompatibleChipLayouts', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 24, 1), )

    
    CompatibleChipLayouts = property(__CompatibleChipLayouts.value, __CompatibleChipLayouts.set, None, 'A set of Chip Layouts deemed compatible with the current plate')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CompatibleSequencingKits uses Python identifier CompatibleSequencingKits
    __CompatibleSequencingKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CompatibleSequencingKits'), 'CompatibleSequencingKits', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_45_httppacificbiosciences_comPacBioDataModel_xsdCompatibleSequencingKits', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 36, 1), )

    
    CompatibleSequencingKits = property(__CompatibleSequencingKits.value, __CompatibleSequencingKits.set, None, 'A set of reagent kits deemed compatible with the current plate')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_45_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    _ElementMap.update({
        __CompatibleChipLayouts.name() : __CompatibleChipLayouts,
        __CompatibleSequencingKits.name() : __CompatibleSequencingKits,
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_46 (pyxb.binding.basis.complexTypeDefinition):
    """A general sample description"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 145, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_46_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_46_Value', pyxb.binding.datatypes.string)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 149, 3)
    __Value._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 149, 3)
    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        __Value.name() : __Value
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_47 (pyxb.binding.basis.complexTypeDefinition):
    """Multiple acquisitions from different instrument runs"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 271, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Run uses Python identifier Run
    __Run = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Run'), 'Run', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_47_httppacificbiosciences_comPacBioDataModel_xsdRun', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 273, 8), )

    
    Run = property(__Run.value, __Run.set, None, None)

    _ElementMap.update({
        __Run.name() : __Run
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_48 (pyxb.binding.basis.complexTypeDefinition):
    """Pointers to various data elements associated with the acquisitions"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 281, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSet uses Python identifier DataSet
    __DataSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSet'), 'DataSet', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_48_httppacificbiosciences_comPacBioDataModel_xsdDataSet', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 135, 1), )

    
    DataSet = property(__DataSet.value, __DataSet.set, None, None)

    _ElementMap.update({
        __DataSet.name() : __DataSet
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_49 (pyxb.binding.basis.complexTypeDefinition):
    """Journal of metrics, system events, or alarms that were generated during this container's lifetime"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 291, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RecordedEvent uses Python identifier RecordedEvent
    __RecordedEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvent'), 'RecordedEvent', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_49_httppacificbiosciences_comPacBioDataModel_xsdRecordedEvent', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 293, 8), )

    
    RecordedEvent = property(__RecordedEvent.value, __RecordedEvent.set, None, "Journal of metrics, system events, or alarms that were generated during this container's lifetime")

    _ElementMap.update({
        __RecordedEvent.name() : __RecordedEvent
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_50 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 302, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSample uses Python identifier BioSample
    __BioSample = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BioSample'), 'BioSample', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_50_httppacificbiosciences_comPacBioDataModel_xsdBioSample', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 304, 8), )

    
    BioSample = property(__BioSample.value, __BioSample.set, None, None)

    _ElementMap.update({
        __BioSample.name() : __BioSample
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_51 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 322, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Input uses Python identifier Input
    __Input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Input'), 'Input', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_51_httppacificbiosciences_comPacBioDataModel_xsdInput', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 61, 1), )

    
    Input = property(__Input.value, __Input.set, None, None)

    _ElementMap.update({
        __Input.name() : __Input
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_52 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 329, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Output uses Python identifier Output
    __Output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Output'), 'Output', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_52_httppacificbiosciences_comPacBioDataModel_xsdOutput', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 62, 1), )

    
    Output = property(__Output.value, __Output.set, None, None)

    _ElementMap.update({
        __Output.name() : __Output
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_53 (pyxb.binding.basis.complexTypeDefinition):
    """Journal of metrics, system events, or alarms that were generated during this run's lifetime"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 345, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RecordedEvent uses Python identifier RecordedEvent
    __RecordedEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvent'), 'RecordedEvent', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_53_httppacificbiosciences_comPacBioDataModel_xsdRecordedEvent', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 347, 8), )

    
    RecordedEvent = property(__RecordedEvent.value, __RecordedEvent.set, None, "Journal of metrics, system events, or alarms that were generated during this run's lifetime.\nIn the case of Primary generating the DataSet containing the sts.xml, this RecordedEvent object should be a pointer to the DataSet object generated.")

    _ElementMap.update({
        __RecordedEvent.name() : __RecordedEvent
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_54 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 388, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CollectionMetadataRef uses Python identifier CollectionMetadataRef
    __CollectionMetadataRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadataRef'), 'CollectionMetadataRef', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_54_httppacificbiosciences_comPacBioDataModel_xsdCollectionMetadataRef', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 390, 4), )

    
    CollectionMetadataRef = property(__CollectionMetadataRef.value, __CollectionMetadataRef.set, None, None)

    _ElementMap.update({
        __CollectionMetadataRef.name() : __CollectionMetadataRef
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_55 (pyxb.binding.basis.complexTypeDefinition):
    """The root element of the Part Numbers """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SequencingKits uses Python identifier SequencingKits
    __SequencingKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingKits'), 'SequencingKits', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_55_httppacificbiosciences_comPacBioDataModel_xsdSequencingKits', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 14, 4), )

    
    SequencingKits = property(__SequencingKits.value, __SequencingKits.set, None, 'List the sequencing kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BindingKits uses Python identifier BindingKits
    __BindingKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BindingKits'), 'BindingKits', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_55_httppacificbiosciences_comPacBioDataModel_xsdBindingKits', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 24, 4), )

    
    BindingKits = property(__BindingKits.value, __BindingKits.set, None, 'List the binding kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}TemplatePrepKits uses Python identifier TemplatePrepKits
    __TemplatePrepKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKits'), 'TemplatePrepKits', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_55_httppacificbiosciences_comPacBioDataModel_xsdTemplatePrepKits', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 34, 4), )

    
    TemplatePrepKits = property(__TemplatePrepKits.value, __TemplatePrepKits.set, None, 'List the sample prep kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ControlKits uses Python identifier ControlKits
    __ControlKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlKits'), 'ControlKits', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_55_httppacificbiosciences_comPacBioDataModel_xsdControlKits', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 44, 4), )

    
    ControlKits = property(__ControlKits.value, __ControlKits.set, None, 'List the DNA control complex part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CellPackKits uses Python identifier CellPackKits
    __CellPackKits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CellPackKits'), 'CellPackKits', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_55_httppacificbiosciences_comPacBioDataModel_xsdCellPackKits', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 54, 4), )

    
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
class CTD_ANON_56 (pyxb.binding.basis.complexTypeDefinition):
    """List the sequencing kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 18, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SequencingKit uses Python identifier SequencingKit
    __SequencingKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit'), 'SequencingKit', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_56_httppacificbiosciences_comPacBioDataModel_xsdSequencingKit', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 67, 1), )

    
    SequencingKit = property(__SequencingKit.value, __SequencingKit.set, None, None)

    _ElementMap.update({
        __SequencingKit.name() : __SequencingKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_57 (pyxb.binding.basis.complexTypeDefinition):
    """List the binding kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 28, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BindingKit uses Python identifier BindingKit
    __BindingKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BindingKit'), 'BindingKit', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_57_httppacificbiosciences_comPacBioDataModel_xsdBindingKit', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 68, 1), )

    
    BindingKit = property(__BindingKit.value, __BindingKit.set, None, None)

    _ElementMap.update({
        __BindingKit.name() : __BindingKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_58 (pyxb.binding.basis.complexTypeDefinition):
    """List the sample prep kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 38, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}TemplatePrepKit uses Python identifier TemplatePrepKit
    __TemplatePrepKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit'), 'TemplatePrepKit', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_58_httppacificbiosciences_comPacBioDataModel_xsdTemplatePrepKit', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 69, 1), )

    
    TemplatePrepKit = property(__TemplatePrepKit.value, __TemplatePrepKit.set, None, None)

    _ElementMap.update({
        __TemplatePrepKit.name() : __TemplatePrepKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_59 (pyxb.binding.basis.complexTypeDefinition):
    """List the DNA control complex part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 48, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ControlKit uses Python identifier ControlKit
    __ControlKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ControlKit'), 'ControlKit', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_59_httppacificbiosciences_comPacBioDataModel_xsdControlKit', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 70, 1), )

    
    ControlKit = property(__ControlKit.value, __ControlKit.set, None, None)

    _ElementMap.update({
        __ControlKit.name() : __ControlKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_60 (pyxb.binding.basis.complexTypeDefinition):
    """List the cell tray part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 58, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CellPackKit uses Python identifier CellPackKit
    __CellPackKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CellPackKit'), 'CellPackKit', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_60_httppacificbiosciences_comPacBioDataModel_xsdCellPackKit', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 71, 1), )

    
    CellPackKit = property(__CellPackKit.value, __CellPackKit.set, None, None)

    _ElementMap.update({
        __CellPackKit.name() : __CellPackKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_61 (pyxb.binding.basis.complexTypeDefinition):
    """The root element of the reagent kit standalone file"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 11, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentKit uses Python identifier ReagentKit
    __ReagentKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentKit'), 'ReagentKit', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_61_httppacificbiosciences_comPacBioDataModel_xsdReagentKit', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 18, 1), )

    
    ReagentKit = property(__ReagentKit.value, __ReagentKit.set, None, None)

    _ElementMap.update({
        __ReagentKit.name() : __ReagentKit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_62 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 70, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Reagent uses Python identifier Reagent
    __Reagent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reagent'), 'Reagent', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_62_httppacificbiosciences_comPacBioDataModel_xsdReagent', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 17, 1), )

    
    Reagent = property(__Reagent.value, __Reagent.set, None, None)

    _ElementMap.update({
        __Reagent.name() : __Reagent
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_63 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 77, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentTube uses Python identifier ReagentTube
    __ReagentTube = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube'), 'ReagentTube', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_63_httppacificbiosciences_comPacBioDataModel_xsdReagentTube', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 19, 1), )

    
    ReagentTube = property(__ReagentTube.value, __ReagentTube.set, None, None)

    _ElementMap.update({
        __ReagentTube.name() : __ReagentTube
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_64 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 84, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentPlateRow uses Python identifier ReagentPlateRow
    __ReagentPlateRow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRow'), 'ReagentPlateRow', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_64_httppacificbiosciences_comPacBioDataModel_xsdReagentPlateRow', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 20, 1), )

    
    ReagentPlateRow = property(__ReagentPlateRow.value, __ReagentPlateRow.set, None, None)

    _ElementMap.update({
        __ReagentPlateRow.name() : __ReagentPlateRow
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_65 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 91, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CompatibleAutomation uses Python identifier CompatibleAutomation
    __CompatibleAutomation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CompatibleAutomation'), 'CompatibleAutomation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_65_httppacificbiosciences_comPacBioDataModel_xsdCompatibleAutomation', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 93, 8), )

    
    CompatibleAutomation = property(__CompatibleAutomation.value, __CompatibleAutomation.set, None, None)

    _ElementMap.update({
        __CompatibleAutomation.name() : __CompatibleAutomation
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType with content type ELEMENT_ONLY
class BaseEntityType (pyxb.binding.basis.complexTypeDefinition):
    """This is the base element type for all types in this data model"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BaseEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 52, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions uses Python identifier Extensions
    __Extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), 'Extensions', '__httppacificbiosciences_comPacBioDataModel_xsd_BaseEntityType_httppacificbiosciences_comPacBioDataModel_xsdExtensions', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3), )

    
    Extensions = property(__Extensions.value, __Extensions.set, None, None)

    
    # Attribute UniqueId uses Python identifier UniqueId
    __UniqueId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UniqueId'), 'UniqueId', '__httppacificbiosciences_comPacBioDataModel_xsd_BaseEntityType_UniqueId', STD_ANON)
    __UniqueId._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 65, 2)
    __UniqueId._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 65, 2)
    
    UniqueId = property(__UniqueId.value, __UniqueId.set, None, 'A unique identifier, such as a GUID - likely autogenerated')

    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__httppacificbiosciences_comPacBioDataModel_xsd_BaseEntityType_Name', pyxb.binding.datatypes.string)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 75, 2)
    __Name._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 75, 2)
    
    Name = property(__Name.value, __Name.set, None, 'A short text identifier; uniqueness not necessary')

    
    # Attribute TimeStampedName uses Python identifier TimeStampedName
    __TimeStampedName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TimeStampedName'), 'TimeStampedName', '__httppacificbiosciences_comPacBioDataModel_xsd_BaseEntityType_TimeStampedName', pyxb.binding.datatypes.string)
    __TimeStampedName._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 80, 2)
    __TimeStampedName._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 80, 2)
    
    TimeStampedName = property(__TimeStampedName.value, __TimeStampedName.set, None, 'This is NOT intended to be used as a unique field.  For uniqueness, use UniqueId.  In order to not utilize customer provided names, this attribute may be used as an alternative means of Human Readable ID, e.g. Run-20150304_231155')

    
    # Attribute Description uses Python identifier Description
    __Description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Description'), 'Description', '__httppacificbiosciences_comPacBioDataModel_xsd_BaseEntityType_Description', pyxb.binding.datatypes.string)
    __Description._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 85, 2)
    __Description._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 85, 2)
    
    Description = property(__Description.value, __Description.set, None, 'A long text description of the object')

    
    # Attribute MetaType uses Python identifier MetaType
    __MetaType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MetaType'), 'MetaType', '__httppacificbiosciences_comPacBioDataModel_xsd_BaseEntityType_MetaType', pyxb.binding.datatypes.string)
    __MetaType._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 90, 2)
    __MetaType._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 90, 2)
    
    MetaType = property(__MetaType.value, __MetaType.set, None, 'Controlled Vocabulary, meant as a means to group similar entities; the type of the object, e.g. Instrument Run, Secondary Run, Assay, Sample, Barcode, Alignment File, Alarm, Exception, Metric, SystemEvent, etc.')

    
    # Attribute Tags uses Python identifier Tags
    __Tags = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Tags'), 'Tags', '__httppacificbiosciences_comPacBioDataModel_xsd_BaseEntityType_Tags', pyxb.binding.datatypes.string)
    __Tags._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 95, 2)
    __Tags._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 95, 2)
    
    Tags = property(__Tags.value, __Tags.set, None, 'A set of keywords assigned to the object to help describe it and allow it to be found via search')

    
    # Attribute ResourceId uses Python identifier ResourceId
    __ResourceId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ResourceId'), 'ResourceId', '__httppacificbiosciences_comPacBioDataModel_xsd_BaseEntityType_ResourceId', pyxb.binding.datatypes.anyURI)
    __ResourceId._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 100, 2)
    __ResourceId._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 100, 2)
    
    ResourceId = property(__ResourceId.value, __ResourceId.set, None, 'A uniform resource identifier used to identify a "web" resource. e.g. svc://run/acquisition/alignment/gridding')

    
    # Attribute Format uses Python identifier Format
    __Format = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Format'), 'Format', '__httppacificbiosciences_comPacBioDataModel_xsd_BaseEntityType_Format', pyxb.binding.datatypes.string)
    __Format._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 105, 2)
    __Format._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 105, 2)
    
    Format = property(__Format.value, __Format.set, None, 'Optional, but recommended.  The MIME-Type of the referenced file.  See http://www.iana.org/assignments/media-types/media-types.xhtml for examples')

    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Version'), 'Version', '__httppacificbiosciences_comPacBioDataModel_xsd_BaseEntityType_Version', pyxb.binding.datatypes.string)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 110, 2)
    __Version._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 110, 2)
    
    Version = property(__Version.value, __Version.set, None, 'An optional identifier denoting the revision of this particular entity')

    
    # Attribute CreatedAt uses Python identifier CreatedAt
    __CreatedAt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CreatedAt'), 'CreatedAt', '__httppacificbiosciences_comPacBioDataModel_xsd_BaseEntityType_CreatedAt', pyxb.binding.datatypes.dateTime)
    __CreatedAt._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 115, 2)
    __CreatedAt._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 115, 2)
    
    CreatedAt = property(__CreatedAt.value, __CreatedAt.set, None, 'Timestamp designating the creation of this object, relative to UTC; millisecond precision is expected.')

    
    # Attribute ModifiedAt uses Python identifier ModifiedAt
    __ModifiedAt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ModifiedAt'), 'ModifiedAt', '__httppacificbiosciences_comPacBioDataModel_xsd_BaseEntityType_ModifiedAt', pyxb.binding.datatypes.dateTime)
    __ModifiedAt._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 120, 2)
    __ModifiedAt._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 120, 2)
    
    ModifiedAt = property(__ModifiedAt.value, __ModifiedAt.set, None, 'Timestamp designating the modification of this object, relative to UTC; millisecond precision is expected.')

    _ElementMap.update({
        __Extensions.name() : __Extensions
    })
    _AttributeMap.update({
        __UniqueId.name() : __UniqueId,
        __Name.name() : __Name,
        __TimeStampedName.name() : __TimeStampedName,
        __Description.name() : __Description,
        __MetaType.name() : __MetaType,
        __Tags.name() : __Tags,
        __ResourceId.name() : __ResourceId,
        __Format.name() : __Format,
        __Version.name() : __Version,
        __CreatedAt.name() : __CreatedAt,
        __ModifiedAt.name() : __ModifiedAt
    })
Namespace.addCategoryObject('typeBinding', 'BaseEntityType', BaseEntityType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_66 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 39, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CommonServicesInstanceId uses Python identifier CommonServicesInstanceId
    __CommonServicesInstanceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CommonServicesInstanceId'), 'CommonServicesInstanceId', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_66_httppacificbiosciences_comPacBioDataModel_xsdCommonServicesInstanceId', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 41, 6), )

    
    CommonServicesInstanceId = property(__CommonServicesInstanceId.value, __CommonServicesInstanceId.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CreatorUserId uses Python identifier CreatorUserId
    __CreatorUserId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CreatorUserId'), 'CreatorUserId', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_66_httppacificbiosciences_comPacBioDataModel_xsdCreatorUserId', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 42, 6), )

    
    CreatorUserId = property(__CreatorUserId.value, __CreatorUserId.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ParentJobId uses Python identifier ParentJobId
    __ParentJobId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ParentJobId'), 'ParentJobId', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_66_httppacificbiosciences_comPacBioDataModel_xsdParentJobId', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 43, 6), )

    
    ParentJobId = property(__ParentJobId.value, __ParentJobId.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ParentTool uses Python identifier ParentTool
    __ParentTool = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ParentTool'), 'ParentTool', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_66_httppacificbiosciences_comPacBioDataModel_xsdParentTool', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 44, 6), )

    
    ParentTool = property(__ParentTool.value, __ParentTool.set, None, None)

    
    # Attribute CreatedBy uses Python identifier CreatedBy
    __CreatedBy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CreatedBy'), 'CreatedBy', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_66_CreatedBy', STD_ANON_, required=True)
    __CreatedBy._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 46, 5)
    __CreatedBy._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 46, 5)
    
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



# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ReadSetMetadataType with content type ELEMENT_ONLY
class ReadSetMetadataType (DataSetMetadataType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ReadSetMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReadSetMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 59, 1)
    _ElementMap = DataSetMetadataType._ElementMap.copy()
    _AttributeMap = DataSetMetadataType._AttributeMap.copy()
    # Base type is DataSetMetadataType
    
    # Element TotalLength ({http://pacificbiosciences.com/PacBioDataModel.xsd}TotalLength) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element NumRecords ({http://pacificbiosciences.com/PacBioDataModel.xsd}NumRecords) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element Provenance ({http://pacificbiosciences.com/PacBioDataModel.xsd}Provenance) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SummaryStats uses Python identifier SummaryStats
    __SummaryStats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SummaryStats'), 'SummaryStats', '__httppacificbiosciences_comPacBioDataModel_xsd_ReadSetMetadataType_httppacificbiosciences_comPacBioDataModel_xsdSummaryStats', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 65, 5), )

    
    SummaryStats = property(__SummaryStats.value, __SummaryStats.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Collections uses Python identifier Collections
    __Collections = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Collections'), 'Collections', '__httppacificbiosciences_comPacBioDataModel_xsd_ReadSetMetadataType_httppacificbiosciences_comPacBioDataModel_xsdCollections', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 125, 1), )

    
    Collections = property(__Collections.value, __Collections.set, None, 'A set of acquisition definitions')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSamples uses Python identifier BioSamples
    __BioSamples = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BioSamples'), 'BioSamples', '__httppacificbiosciences_comPacBioDataModel_xsd_ReadSetMetadataType_httppacificbiosciences_comPacBioDataModel_xsdBioSamples', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 673, 1), )

    
    BioSamples = property(__BioSamples.value, __BioSamples.set, None, None)

    _ElementMap.update({
        __SummaryStats.name() : __SummaryStats,
        __Collections.name() : __Collections,
        __BioSamples.name() : __BioSamples
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ReadSetMetadataType', ReadSetMetadataType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}SubreadSetMetadataType with content type ELEMENT_ONLY
class SubreadSetMetadataType (DataSetMetadataType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}SubreadSetMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubreadSetMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 87, 1)
    _ElementMap = DataSetMetadataType._ElementMap.copy()
    _AttributeMap = DataSetMetadataType._AttributeMap.copy()
    # Base type is DataSetMetadataType
    
    # Element TotalLength ({http://pacificbiosciences.com/PacBioDataModel.xsd}TotalLength) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element NumRecords ({http://pacificbiosciences.com/PacBioDataModel.xsd}NumRecords) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element Provenance ({http://pacificbiosciences.com/PacBioDataModel.xsd}Provenance) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}AverageSubreadLength uses Python identifier AverageSubreadLength
    __AverageSubreadLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AverageSubreadLength'), 'AverageSubreadLength', '__httppacificbiosciences_comPacBioDataModel_xsd_SubreadSetMetadataType_httppacificbiosciences_comPacBioDataModel_xsdAverageSubreadLength', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 91, 5), )

    
    AverageSubreadLength = property(__AverageSubreadLength.value, __AverageSubreadLength.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}AverageSubreadQuality uses Python identifier AverageSubreadQuality
    __AverageSubreadQuality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AverageSubreadQuality'), 'AverageSubreadQuality', '__httppacificbiosciences_comPacBioDataModel_xsd_SubreadSetMetadataType_httppacificbiosciences_comPacBioDataModel_xsdAverageSubreadQuality', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 92, 5), )

    
    AverageSubreadQuality = property(__AverageSubreadQuality.value, __AverageSubreadQuality.set, None, None)

    _ElementMap.update({
        __AverageSubreadLength.name() : __AverageSubreadLength,
        __AverageSubreadQuality.name() : __AverageSubreadQuality
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SubreadSetMetadataType', SubreadSetMetadataType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_67 (pyxb.binding.basis.complexTypeDefinition):
    """A variable, as a name/value pair, associated with a protocol (one of Collection, Primary, and Secondary)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 67, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Validation uses Python identifier Validation
    __Validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Validation'), 'Validation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_67_httppacificbiosciences_comPacBioDataModel_xsdValidation', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1), )

    
    Validation = property(__Validation.value, __Validation.set, None, '\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ')

    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Name'), 'Name', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_67_Name', STD_ANON_2, required=True)
    __Name._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 71, 3)
    __Name._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 71, 3)
    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Attribute Value uses Python identifier Value
    __Value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Value'), 'Value', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_67_Value', pyxb.binding.datatypes.string, required=True)
    __Value._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 88, 3)
    __Value._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 88, 3)
    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Validation.name() : __Validation
    })
    _AttributeMap.update({
        __Name.name() : __Name,
        __Value.name() : __Value
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_68 (pyxb.binding.basis.complexTypeDefinition):
    """
        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 158, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute IsValid uses Python identifier IsValid
    __IsValid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IsValid'), 'IsValid', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_68_IsValid', pyxb.binding.datatypes.boolean, required=True)
    __IsValid._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 159, 3)
    __IsValid._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 159, 3)
    
    IsValid = property(__IsValid.value, __IsValid.set, None, '\n            Indicates whether or not the element is valid.  The assumption is that the\n            Validation element is omitted unless the element is invalid, in which case,\n            the Validation element would describe the problem.\n          ')

    
    # Attribute ID uses Python identifier ID
    __ID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ID'), 'ID', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_68_ID', pyxb.binding.datatypes.string, required=True)
    __ID._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 168, 3)
    __ID._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 168, 3)
    
    ID = property(__ID.value, __ID.set, None, '\n            An identifier which can be used by client applications to translate/map\n            to a human decipherable message.\n          ')

    
    # Attribute Source uses Python identifier Source
    __Source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Source'), 'Source', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_68_Source', STD_ANON_3, required=True)
    __Source._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 176, 3)
    __Source._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 176, 3)
    
    Source = property(__Source.value, __Source.set, None, '\n            This is the element which has experienced a validation issue.\n          ')

    
    # Attribute ElementPath uses Python identifier ElementPath
    __ElementPath = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ElementPath'), 'ElementPath', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_68_ElementPath', pyxb.binding.datatypes.string)
    __ElementPath._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 221, 3)
    __ElementPath._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 221, 3)
    
    ElementPath = property(__ElementPath.value, __ElementPath.set, None, '\n            An optional string attribute which holds the path to the offending element.\n          ')

    
    # Attribute SupplementalInfo uses Python identifier SupplementalInfo
    __SupplementalInfo = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SupplementalInfo'), 'SupplementalInfo', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_68_SupplementalInfo', pyxb.binding.datatypes.string)
    __SupplementalInfo._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 228, 3)
    __SupplementalInfo._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 228, 3)
    
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



# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}AlignmentSetMetadataType with content type ELEMENT_ONLY
class AlignmentSetMetadataType (DataSetMetadataType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}AlignmentSetMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlignmentSetMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 137, 1)
    _ElementMap = DataSetMetadataType._ElementMap.copy()
    _AttributeMap = DataSetMetadataType._AttributeMap.copy()
    # Base type is DataSetMetadataType
    
    # Element TotalLength ({http://pacificbiosciences.com/PacBioDataModel.xsd}TotalLength) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element NumRecords ({http://pacificbiosciences.com/PacBioDataModel.xsd}NumRecords) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element Provenance ({http://pacificbiosciences.com/PacBioDataModel.xsd}Provenance) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Aligner uses Python identifier Aligner
    __Aligner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Aligner'), 'Aligner', '__httppacificbiosciences_comPacBioDataModel_xsd_AlignmentSetMetadataType_httppacificbiosciences_comPacBioDataModel_xsdAligner', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 141, 5), )

    
    Aligner = property(__Aligner.value, __Aligner.set, None, None)

    _ElementMap.update({
        __Aligner.name() : __Aligner
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AlignmentSetMetadataType', AlignmentSetMetadataType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ContigSetMetadataType with content type ELEMENT_ONLY
class ContigSetMetadataType (DataSetMetadataType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ContigSetMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContigSetMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 146, 1)
    _ElementMap = DataSetMetadataType._ElementMap.copy()
    _AttributeMap = DataSetMetadataType._AttributeMap.copy()
    # Base type is DataSetMetadataType
    
    # Element TotalLength ({http://pacificbiosciences.com/PacBioDataModel.xsd}TotalLength) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element NumRecords ({http://pacificbiosciences.com/PacBioDataModel.xsd}NumRecords) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element Provenance ({http://pacificbiosciences.com/PacBioDataModel.xsd}Provenance) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Contigs uses Python identifier Contigs
    __Contigs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contigs'), 'Contigs', '__httppacificbiosciences_comPacBioDataModel_xsd_ContigSetMetadataType_httppacificbiosciences_comPacBioDataModel_xsdContigs', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 114, 1), )

    
    Contigs = property(__Contigs.value, __Contigs.set, None, 'List of contigs in a ContigSet')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Organism uses Python identifier Organism
    __Organism = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Organism'), 'Organism', '__httppacificbiosciences_comPacBioDataModel_xsd_ContigSetMetadataType_httppacificbiosciences_comPacBioDataModel_xsdOrganism', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 150, 5), )

    
    Organism = property(__Organism.value, __Organism.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Ploidy uses Python identifier Ploidy
    __Ploidy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ploidy'), 'Ploidy', '__httppacificbiosciences_comPacBioDataModel_xsd_ContigSetMetadataType_httppacificbiosciences_comPacBioDataModel_xsdPloidy', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 151, 5), )

    
    Ploidy = property(__Ploidy.value, __Ploidy.set, None, None)

    _ElementMap.update({
        __Contigs.name() : __Contigs,
        __Organism.name() : __Organism,
        __Ploidy.name() : __Ploidy
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ContigSetMetadataType', ContigSetMetadataType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}BarcodeSetMetadataType with content type ELEMENT_ONLY
class BarcodeSetMetadataType (DataSetMetadataType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}BarcodeSetMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BarcodeSetMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 157, 1)
    _ElementMap = DataSetMetadataType._ElementMap.copy()
    _AttributeMap = DataSetMetadataType._AttributeMap.copy()
    # Base type is DataSetMetadataType
    
    # Element TotalLength ({http://pacificbiosciences.com/PacBioDataModel.xsd}TotalLength) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element NumRecords ({http://pacificbiosciences.com/PacBioDataModel.xsd}NumRecords) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element Provenance ({http://pacificbiosciences.com/PacBioDataModel.xsd}Provenance) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadataType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BarcodeConstruction uses Python identifier BarcodeConstruction
    __BarcodeConstruction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BarcodeConstruction'), 'BarcodeConstruction', '__httppacificbiosciences_comPacBioDataModel_xsd_BarcodeSetMetadataType_httppacificbiosciences_comPacBioDataModel_xsdBarcodeConstruction', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 161, 5), )

    
    BarcodeConstruction = property(__BarcodeConstruction.value, __BarcodeConstruction.set, None, None)

    _ElementMap.update({
        __BarcodeConstruction.name() : __BarcodeConstruction
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BarcodeSetMetadataType', BarcodeSetMetadataType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}AutomationConstraintType with content type ELEMENT_ONLY
class AutomationConstraintType (BaseEntityType):
    """This data type defines constraints that an automation has.  The information here, along with the availability of an exclusionary list of automations in the PartNumberType, allows for defining a robust compatibility matrix."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AutomationConstraintType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 27, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Automations uses Python identifier Automations
    __Automations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Automations'), 'Automations', '__httppacificbiosciences_comPacBioDataModel_xsd_AutomationConstraintType_httppacificbiosciences_comPacBioDataModel_xsdAutomations', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 34, 5), )

    
    Automations = property(__Automations.value, __Automations.set, None, 'Names of automations that are all similarly constrained')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}InsertSizes uses Python identifier InsertSizes
    __InsertSizes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InsertSizes'), 'InsertSizes', '__httppacificbiosciences_comPacBioDataModel_xsd_AutomationConstraintType_httppacificbiosciences_comPacBioDataModel_xsdInsertSizes', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 44, 5), )

    
    InsertSizes = property(__InsertSizes.value, __InsertSizes.set, None, 'A list of insert sizes (buckets) recommended for use')

    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute SupportsCellReuse uses Python identifier SupportsCellReuse
    __SupportsCellReuse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SupportsCellReuse'), 'SupportsCellReuse', '__httppacificbiosciences_comPacBioDataModel_xsd_AutomationConstraintType_SupportsCellReuse', pyxb.binding.datatypes.boolean)
    __SupportsCellReuse._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 55, 4)
    __SupportsCellReuse._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 55, 4)
    
    SupportsCellReuse = property(__SupportsCellReuse.value, __SupportsCellReuse.set, None, 'Does this automation support cell reuse?')

    
    # Attribute MaxCollectionsPerCell uses Python identifier MaxCollectionsPerCell
    __MaxCollectionsPerCell = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MaxCollectionsPerCell'), 'MaxCollectionsPerCell', '__httppacificbiosciences_comPacBioDataModel_xsd_AutomationConstraintType_MaxCollectionsPerCell', pyxb.binding.datatypes.int)
    __MaxCollectionsPerCell._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 60, 4)
    __MaxCollectionsPerCell._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 60, 4)
    
    MaxCollectionsPerCell = property(__MaxCollectionsPerCell.value, __MaxCollectionsPerCell.set, None, 'If cell reuse is supported (i.e. above attribute is true) how many times can the cell be reused?')

    
    # Attribute MinMovieLength uses Python identifier MinMovieLength
    __MinMovieLength = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MinMovieLength'), 'MinMovieLength', '__httppacificbiosciences_comPacBioDataModel_xsd_AutomationConstraintType_MinMovieLength', pyxb.binding.datatypes.int)
    __MinMovieLength._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 65, 4)
    __MinMovieLength._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 65, 4)
    
    MinMovieLength = property(__MinMovieLength.value, __MinMovieLength.set, None, 'Minimum length of movie acquisition')

    
    # Attribute MaxMovieLength uses Python identifier MaxMovieLength
    __MaxMovieLength = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MaxMovieLength'), 'MaxMovieLength', '__httppacificbiosciences_comPacBioDataModel_xsd_AutomationConstraintType_MaxMovieLength', pyxb.binding.datatypes.int)
    __MaxMovieLength._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 70, 4)
    __MaxMovieLength._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 70, 4)
    
    MaxMovieLength = property(__MaxMovieLength.value, __MaxMovieLength.set, None, 'Maximum length of movie acquisition')

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __Automations.name() : __Automations,
        __InsertSizes.name() : __InsertSizes
    })
    _AttributeMap.update({
        __SupportsCellReuse.name() : __SupportsCellReuse,
        __MaxCollectionsPerCell.name() : __MaxCollectionsPerCell,
        __MinMovieLength.name() : __MinMovieLength,
        __MaxMovieLength.name() : __MaxMovieLength
    })
Namespace.addCategoryObject('typeBinding', 'AutomationConstraintType', AutomationConstraintType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType with content type ELEMENT_ONLY
class AnalogType (BaseEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnalogType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 6, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Base uses Python identifier Base
    __Base = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Base'), 'Base', '__httppacificbiosciences_comPacBioDataModel_xsd_AnalogType_Base', SupportedNucleotides)
    __Base._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 9, 4)
    __Base._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 9, 4)
    
    Base = property(__Base.value, __Base.set, None, 'The base label, A, C, T, or G')

    
    # Attribute SpectralAngle uses Python identifier SpectralAngle
    __SpectralAngle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SpectralAngle'), 'SpectralAngle', '__httppacificbiosciences_comPacBioDataModel_xsd_AnalogType_SpectralAngle', pyxb.binding.datatypes.float)
    __SpectralAngle._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 14, 4)
    __SpectralAngle._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 14, 4)
    
    SpectralAngle = property(__SpectralAngle.value, __SpectralAngle.set, None, 'In radians (0 \u2264 \u03b1 \u2264 \u03c0/2), it is the estimate of arctan(red_pixel / green_pixel), where red[green]_pixel is the relative amplitude, as measured by the instrument\u2019s detector, of emitted light that is collected in the red[green] pixel channel.')

    
    # Attribute RelativeAmplitude uses Python identifier RelativeAmplitude
    __RelativeAmplitude = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'RelativeAmplitude'), 'RelativeAmplitude', '__httppacificbiosciences_comPacBioDataModel_xsd_AnalogType_RelativeAmplitude', pyxb.binding.datatypes.float)
    __RelativeAmplitude._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 19, 4)
    __RelativeAmplitude._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 19, 4)
    
    RelativeAmplitude = property(__RelativeAmplitude.value, __RelativeAmplitude.set, None, 'Relative intensity vs. a specific molecule used as a baseline measure.  The expected relative amplitude (DWS-normalized) of the analog label relative to 542 as measured on Astro.')

    
    # Attribute Label uses Python identifier Label
    __Label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Label'), 'Label', '__httppacificbiosciences_comPacBioDataModel_xsd_AnalogType_Label', pyxb.binding.datatypes.string)
    __Label._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 24, 4)
    __Label._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 24, 4)
    
    Label = property(__Label.value, __Label.set, None, 'Identifier of the acceptor dye which determines the emission spectrum')

    
    # Attribute Nucleotide uses Python identifier Nucleotide
    __Nucleotide = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Nucleotide'), 'Nucleotide', '__httppacificbiosciences_comPacBioDataModel_xsd_AnalogType_Nucleotide', pyxb.binding.datatypes.string)
    __Nucleotide._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 29, 4)
    __Nucleotide._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 29, 4)
    
    Nucleotide = property(__Nucleotide.value, __Nucleotide.set, None, 'The type and number of nucleotides on a given analog. e.g. (dT6P)6')

    
    # Attribute Wavelength uses Python identifier Wavelength
    __Wavelength = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Wavelength'), 'Wavelength', '__httppacificbiosciences_comPacBioDataModel_xsd_AnalogType_Wavelength', pyxb.binding.datatypes.float)
    __Wavelength._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 34, 4)
    __Wavelength._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 34, 4)
    
    Wavelength = property(__Wavelength.value, __Wavelength.set, None, 'The peak emission wavelength associated with the dye label in nm.')

    
    # Attribute CompoundID uses Python identifier CompoundID
    __CompoundID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CompoundID'), 'CompoundID', '__httppacificbiosciences_comPacBioDataModel_xsd_AnalogType_CompoundID', pyxb.binding.datatypes.string)
    __CompoundID._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 39, 4)
    __CompoundID._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 39, 4)
    
    CompoundID = property(__CompoundID.value, __CompoundID.set, None, 'Identification code of the final compound.  The suffix \u2018N\u2019 should be used to distinguish these values from enzyme identifiers.\te.g. 5031N')

    
    # Attribute LotID uses Python identifier LotID
    __LotID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'LotID'), 'LotID', '__httppacificbiosciences_comPacBioDataModel_xsd_AnalogType_LotID', pyxb.binding.datatypes.string)
    __LotID._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 44, 4)
    __LotID._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 44, 4)
    
    LotID = property(__LotID.value, __LotID.set, None, 'Identification code for the build of the final compound, written as initials/date, where date is written as YYYY-MM-DD.\te.g. js/2014-06-30')

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Base.name() : __Base,
        __SpectralAngle.name() : __SpectralAngle,
        __RelativeAmplitude.name() : __RelativeAmplitude,
        __Label.name() : __Label,
        __Nucleotide.name() : __Nucleotide,
        __Wavelength.name() : __Wavelength,
        __CompoundID.name() : __CompoundID,
        __LotID.name() : __LotID
    })
Namespace.addCategoryObject('typeBinding', 'AnalogType', AnalogType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType with content type ELEMENT_ONLY
class DataEntityType (BaseEntityType):
    """Extends BaseEntityType and adds a value element.  The intent is to have only one of the value elements exist at any point in time; however, this is not enforced."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataEntityType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 137, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue uses Python identifier EncodedValue
    __EncodedValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue'), 'EncodedValue', '__httppacificbiosciences_comPacBioDataModel_xsd_DataEntityType_httppacificbiosciences_comPacBioDataModel_xsdEncodedValue', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5), )

    
    EncodedValue = property(__EncodedValue.value, __EncodedValue.set, None, 'A complex data type element, such as an image, file, binary object, etc.')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum uses Python identifier CheckSum
    __CheckSum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CheckSum'), 'CheckSum', '__httppacificbiosciences_comPacBioDataModel_xsd_DataEntityType_httppacificbiosciences_comPacBioDataModel_xsdCheckSum', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5), )

    
    CheckSum = property(__CheckSum.value, __CheckSum.set, None, 'small-size datum of the attached value for the purpose of detecting errors or modification which may have been introduced during its transmission or storage')

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType uses Python identifier ValueDataType
    __ValueDataType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ValueDataType'), 'ValueDataType', '__httppacificbiosciences_comPacBioDataModel_xsd_DataEntityType_ValueDataType', SupportedDataTypes, unicode_default='Object')
    __ValueDataType._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 155, 4)
    __ValueDataType._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 155, 4)
    
    ValueDataType = property(__ValueDataType.value, __ValueDataType.set, None, 'The datatype of the simple or encoded value.  If not specified, a string is assumed.')

    
    # Attribute SimpleValue uses Python identifier SimpleValue
    __SimpleValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SimpleValue'), 'SimpleValue', '__httppacificbiosciences_comPacBioDataModel_xsd_DataEntityType_SimpleValue', pyxb.binding.datatypes.anySimpleType)
    __SimpleValue._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 160, 4)
    __SimpleValue._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 160, 4)
    
    SimpleValue = property(__SimpleValue.value, __SimpleValue.set, None, 'A simple data type element, such as a string, int, float, etc.')

    _ElementMap.update({
        __EncodedValue.name() : __EncodedValue,
        __CheckSum.name() : __CheckSum
    })
    _AttributeMap.update({
        __ValueDataType.name() : __ValueDataType,
        __SimpleValue.name() : __SimpleValue
    })
Namespace.addCategoryObject('typeBinding', 'DataEntityType', DataEntityType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}DNABarcode with content type ELEMENT_ONLY
class DNABarcode (BaseEntityType):
    """Composite of uuid, sequence, and name"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DNABarcode')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 178, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute DNASequence uses Python identifier DNASequence
    __DNASequence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DNASequence'), 'DNASequence', '__httppacificbiosciences_comPacBioDataModel_xsd_DNABarcode_DNASequence', pyxb.binding.datatypes.anySimpleType)
    __DNASequence._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 184, 4)
    __DNASequence._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 184, 4)
    
    DNASequence = property(__DNASequence.value, __DNASequence.set, None, "This is the sample's DNA barcode")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __DNASequence.name() : __DNASequence
    })
Namespace.addCategoryObject('typeBinding', 'DNABarcode', DNABarcode)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}AutomationType with content type ELEMENT_ONLY
class AutomationType (BaseEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}AutomationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AutomationType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 237, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}AutomationParameters uses Python identifier AutomationParameters
    __AutomationParameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameters'), 'AutomationParameters', '__httppacificbiosciences_comPacBioDataModel_xsd_AutomationType_httppacificbiosciences_comPacBioDataModel_xsdAutomationParameters', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 241, 5), )

    
    AutomationParameters = property(__AutomationParameters.value, __AutomationParameters.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute IsObsolete uses Python identifier IsObsolete
    __IsObsolete = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IsObsolete'), 'IsObsolete', '__httppacificbiosciences_comPacBioDataModel_xsd_AutomationType_IsObsolete', pyxb.binding.datatypes.boolean)
    __IsObsolete._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 249, 4)
    __IsObsolete._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 249, 4)
    
    IsObsolete = property(__IsObsolete.value, __IsObsolete.set, None, None)

    _ElementMap.update({
        __AutomationParameters.name() : __AutomationParameters
    })
    _AttributeMap.update({
        __IsObsolete.name() : __IsObsolete
    })
Namespace.addCategoryObject('typeBinding', 'AutomationType', AutomationType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_69 (BaseEntityType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 342, 6)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Analogs uses Python identifier Analogs
    __Analogs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Analogs'), 'Analogs', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_69_httppacificbiosciences_comPacBioDataModel_xsdAnalogs', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 346, 10), )

    
    Analogs = property(__Analogs.value, __Analogs.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __Analogs.name() : __Analogs
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}SequencingChemistryConfig with content type ELEMENT_ONLY
class SequencingChemistryConfig (BaseEntityType):
    """A container for a set of analogs"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequencingChemistryConfig')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 372, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Analogs uses Python identifier Analogs
    __Analogs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Analogs'), 'Analogs', '__httppacificbiosciences_comPacBioDataModel_xsd_SequencingChemistryConfig_httppacificbiosciences_comPacBioDataModel_xsdAnalogs', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 379, 5), )

    
    Analogs = property(__Analogs.value, __Analogs.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __Analogs.name() : __Analogs
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SequencingChemistryConfig', SequencingChemistryConfig)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}StatsContinuousDistType with content type ELEMENT_ONLY
class StatsContinuousDistType (BaseEntityType):
    """Continuous distribution class"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StatsContinuousDistType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 390, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SampleSize uses Python identifier SampleSize
    __SampleSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SampleSize'), 'SampleSize', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioDataModel_xsdSampleSize', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 397, 5), )

    
    SampleSize = property(__SampleSize.value, __SampleSize.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SampleMean uses Python identifier SampleMean
    __SampleMean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SampleMean'), 'SampleMean', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioDataModel_xsdSampleMean', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 398, 5), )

    
    SampleMean = property(__SampleMean.value, __SampleMean.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SampleMed uses Python identifier SampleMed
    __SampleMed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SampleMed'), 'SampleMed', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioDataModel_xsdSampleMed', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 399, 5), )

    
    SampleMed = property(__SampleMed.value, __SampleMed.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SampleStd uses Python identifier SampleStd
    __SampleStd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SampleStd'), 'SampleStd', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioDataModel_xsdSampleStd', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 400, 5), )

    
    SampleStd = property(__SampleStd.value, __SampleStd.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Sample95thPct uses Python identifier Sample95thPct
    __Sample95thPct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Sample95thPct'), 'Sample95thPct', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioDataModel_xsdSample95thPct', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 401, 5), )

    
    Sample95thPct = property(__Sample95thPct.value, __Sample95thPct.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}NumBins uses Python identifier NumBins
    __NumBins = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumBins'), 'NumBins', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioDataModel_xsdNumBins', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 402, 5), )

    
    NumBins = property(__NumBins.value, __NumBins.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BinCounts uses Python identifier BinCounts
    __BinCounts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinCounts'), 'BinCounts', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioDataModel_xsdBinCounts', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 403, 5), )

    
    BinCounts = property(__BinCounts.value, __BinCounts.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BinWidth uses Python identifier BinWidth
    __BinWidth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinWidth'), 'BinWidth', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioDataModel_xsdBinWidth', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 410, 5), )

    
    BinWidth = property(__BinWidth.value, __BinWidth.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}MinOutlierValue uses Python identifier MinOutlierValue
    __MinOutlierValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MinOutlierValue'), 'MinOutlierValue', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioDataModel_xsdMinOutlierValue', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 411, 5), )

    
    MinOutlierValue = property(__MinOutlierValue.value, __MinOutlierValue.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}MinBinValue uses Python identifier MinBinValue
    __MinBinValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MinBinValue'), 'MinBinValue', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioDataModel_xsdMinBinValue', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 412, 5), )

    
    MinBinValue = property(__MinBinValue.value, __MinBinValue.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}MaxBinValue uses Python identifier MaxBinValue
    __MaxBinValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MaxBinValue'), 'MaxBinValue', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioDataModel_xsdMaxBinValue', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 413, 5), )

    
    MaxBinValue = property(__MaxBinValue.value, __MaxBinValue.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}MaxOutlierValue uses Python identifier MaxOutlierValue
    __MaxOutlierValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MaxOutlierValue'), 'MaxOutlierValue', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioDataModel_xsdMaxOutlierValue', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 414, 5), )

    
    MaxOutlierValue = property(__MaxOutlierValue.value, __MaxOutlierValue.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}MetricDescription uses Python identifier MetricDescription
    __MetricDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MetricDescription'), 'MetricDescription', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_httppacificbiosciences_comPacBioDataModel_xsdMetricDescription', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 415, 5), )

    
    MetricDescription = property(__MetricDescription.value, __MetricDescription.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Channel uses Python identifier Channel
    __Channel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Channel'), 'Channel', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsContinuousDistType_Channel', pyxb.binding.datatypes.string)
    __Channel._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 417, 4)
    __Channel._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 417, 4)
    
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


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}StatsDiscreteDistType with content type ELEMENT_ONLY
class StatsDiscreteDistType (BaseEntityType):
    """Discrete distribution class"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StatsDiscreteDistType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 421, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}NumBins uses Python identifier NumBins
    __NumBins = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumBins'), 'NumBins', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsDiscreteDistType_httppacificbiosciences_comPacBioDataModel_xsdNumBins', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 428, 5), )

    
    NumBins = property(__NumBins.value, __NumBins.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BinCounts uses Python identifier BinCounts
    __BinCounts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinCounts'), 'BinCounts', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsDiscreteDistType_httppacificbiosciences_comPacBioDataModel_xsdBinCounts', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 429, 5), )

    
    BinCounts = property(__BinCounts.value, __BinCounts.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}MetricDescription uses Python identifier MetricDescription
    __MetricDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MetricDescription'), 'MetricDescription', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsDiscreteDistType_httppacificbiosciences_comPacBioDataModel_xsdMetricDescription', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 436, 5), )

    
    MetricDescription = property(__MetricDescription.value, __MetricDescription.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BinLabels uses Python identifier BinLabels
    __BinLabels = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BinLabels'), 'BinLabels', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsDiscreteDistType_httppacificbiosciences_comPacBioDataModel_xsdBinLabels', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 437, 5), )

    
    BinLabels = property(__BinLabels.value, __BinLabels.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __NumBins.name() : __NumBins,
        __BinCounts.name() : __BinCounts,
        __MetricDescription.name() : __MetricDescription,
        __BinLabels.name() : __BinLabels
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'StatsDiscreteDistType', StatsDiscreteDistType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}StatsTimeSeriesType with content type ELEMENT_ONLY
class StatsTimeSeriesType (BaseEntityType):
    """Time series (for time-dependent metrics)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StatsTimeSeriesType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 448, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}TimeUnits uses Python identifier TimeUnits
    __TimeUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeUnits'), 'TimeUnits', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsTimeSeriesType_httppacificbiosciences_comPacBioDataModel_xsdTimeUnits', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 455, 5), )

    
    TimeUnits = property(__TimeUnits.value, __TimeUnits.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ValueUnits uses Python identifier ValueUnits
    __ValueUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValueUnits'), 'ValueUnits', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsTimeSeriesType_httppacificbiosciences_comPacBioDataModel_xsdValueUnits', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 456, 5), )

    
    ValueUnits = property(__ValueUnits.value, __ValueUnits.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), 'StartTime', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsTimeSeriesType_httppacificbiosciences_comPacBioDataModel_xsdStartTime', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 457, 5), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}MeasInterval uses Python identifier MeasInterval
    __MeasInterval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MeasInterval'), 'MeasInterval', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsTimeSeriesType_httppacificbiosciences_comPacBioDataModel_xsdMeasInterval', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 458, 5), )

    
    MeasInterval = property(__MeasInterval.value, __MeasInterval.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Values uses Python identifier Values
    __Values = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Values'), 'Values', '__httppacificbiosciences_comPacBioDataModel_xsd_StatsTimeSeriesType_httppacificbiosciences_comPacBioDataModel_xsdValues', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 459, 5), )

    
    Values = property(__Values.value, __Values.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
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


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType with content type ELEMENT_ONLY
class DataSetType (BaseEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataSetType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 102, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources uses Python identifier ExternalResources
    __ExternalResources = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources'), 'ExternalResources', '__httppacificbiosciences_comPacBioDataModel_xsd_DataSetType_httppacificbiosciences_comPacBioDataModel_xsdExternalResources', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 202, 1), )

    
    ExternalResources = property(__ExternalResources.value, __ExternalResources.set, None, 'Pointers to data that do not reside inside the parent structure')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Filters uses Python identifier Filters
    __Filters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Filters'), 'Filters', '__httppacificbiosciences_comPacBioDataModel_xsd_DataSetType_httppacificbiosciences_comPacBioDataModel_xsdFilters', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5), )

    
    Filters = property(__Filters.value, __Filters.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets uses Python identifier DataSets
    __DataSets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSets'), 'DataSets', '__httppacificbiosciences_comPacBioDataModel_xsd_DataSetType_httppacificbiosciences_comPacBioDataModel_xsdDataSets', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5), )

    
    DataSets = property(__DataSets.value, __DataSets.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __ExternalResources.name() : __ExternalResources,
        __Filters.name() : __Filters,
        __DataSets.name() : __DataSets
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DataSetType', DataSetType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_70 (BaseEntityType):
    """Root-level element for the metadata.  The purpose of which is to contain pertinent instrument information related to the conditions present during a movie acquisition.  It also serves to provide key pieces of information for integration with primary and secondary analysis.  This file is associated with 1 movie. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 140, 2)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}InstCtrlVer uses Python identifier InstCtrlVer
    __InstCtrlVer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InstCtrlVer'), 'InstCtrlVer', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdInstCtrlVer', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 144, 6), )

    
    InstCtrlVer = property(__InstCtrlVer.value, __InstCtrlVer.set, None, 'Instrument control software version. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SigProcVer uses Python identifier SigProcVer
    __SigProcVer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SigProcVer'), 'SigProcVer', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdSigProcVer', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 149, 6), )

    
    SigProcVer = property(__SigProcVer.value, __SigProcVer.set, None, 'Signal processing software version. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Automation uses Python identifier Automation
    __Automation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Automation'), 'Automation', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdAutomation', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 171, 6), )

    
    Automation = property(__Automation.value, __Automation.set, None, 'Defines the collection workflow (e.g., robotic movement, movie acquisition) for a particular cell. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CollectionNumber uses Python identifier CollectionNumber
    __CollectionNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CollectionNumber'), 'CollectionNumber', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdCollectionNumber', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 176, 6), )

    
    CollectionNumber = property(__CollectionNumber.value, __CollectionNumber.set, None, 'Collection number for this plate well. Sample from one plate well or tube can be distributed to more than one cell. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CellIndex uses Python identifier CellIndex
    __CellIndex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CellIndex'), 'CellIndex', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdCellIndex', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 181, 6), )

    
    CellIndex = property(__CellIndex.value, __CellIndex.set, None, 'The zero-based index of this particular cell within the cell tray.  Likely to be in the range of [0-3]')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SetNumber uses Python identifier SetNumber
    __SetNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SetNumber'), 'SetNumber', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdSetNumber', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 186, 6), )

    
    SetNumber = property(__SetNumber.value, __SetNumber.set, None, 'Formerly known as the look number.  1 - N.  Defaults to 1. 0 if the look is unknown. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CellPac uses Python identifier CellPac
    __CellPac = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CellPac'), 'CellPac', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdCellPac', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 191, 6), )

    
    CellPac = property(__CellPac.value, __CellPac.set, None, 'The SMRT cell packaging supply information. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}TemplatePrepKit uses Python identifier TemplatePrepKit
    __TemplatePrepKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit'), 'TemplatePrepKit', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdTemplatePrepKit', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 196, 6), )

    
    TemplatePrepKit = property(__TemplatePrepKit.value, __TemplatePrepKit.set, None, 'Defines the template (sample) prep kit used for this experiment. Can be used to get back to the primary and adapter used. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BindingKit uses Python identifier BindingKit
    __BindingKit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BindingKit'), 'BindingKit', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdBindingKit', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 201, 6), )

    
    BindingKit = property(__BindingKit.value, __BindingKit.set, None, 'The binding kit supply information. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SequencingKitPlate uses Python identifier SequencingKitPlate
    __SequencingKitPlate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitPlate'), 'SequencingKitPlate', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdSequencingKitPlate', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 206, 6), )

    
    SequencingKitPlate = property(__SequencingKitPlate.value, __SequencingKitPlate.set, None, 'The sequencing kit supply information. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RunDetails uses Python identifier RunDetails
    __RunDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RunDetails'), 'RunDetails', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdRunDetails', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 248, 1), )

    
    RunDetails = property(__RunDetails.value, __RunDetails.set, None, 'Information related to an instrument run.  A run can contain multiple chips, wells, and movies. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Movie uses Python identifier Movie
    __Movie = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Movie'), 'Movie', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdMovie', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 287, 1), )

    
    Movie = property(__Movie.value, __Movie.set, None, 'A movie corresponds to one acquisition for a chip, one set (look) and one strobe. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ExpirationData uses Python identifier ExpirationData
    __ExpirationData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExpirationData'), 'ExpirationData', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdExpirationData', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 311, 1), )

    
    ExpirationData = property(__ExpirationData.value, __ExpirationData.set, None, 'Container for the expired consumable data. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}WellSample uses Python identifier WellSample
    __WellSample = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WellSample'), 'WellSample', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdWellSample', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 432, 1), )

    
    WellSample = property(__WellSample.value, __WellSample.set, None, 'Container for the sample related data. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Primary uses Python identifier Primary
    __Primary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Primary'), 'Primary', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdPrimary', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 503, 1), )

    
    Primary = property(__Primary.value, __Primary.set, None, 'Container for the primary analysis related data. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Secondary uses Python identifier Secondary
    __Secondary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Secondary'), 'Secondary', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdSecondary', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 568, 1), )

    
    Secondary = property(__Secondary.value, __Secondary.set, None, 'Container for the primary analysis related data. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}UserDefinedFields uses Python identifier UserDefinedFields
    __UserDefinedFields = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UserDefinedFields'), 'UserDefinedFields', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_httppacificbiosciences_comPacBioDataModel_xsdUserDefinedFields', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 602, 1), )

    
    UserDefinedFields = property(__UserDefinedFields.value, __UserDefinedFields.set, None, 'A set of key-value pairs specified by a user via the run input mechanism. Note that uniqueness of keys is not enforced here and so may contain duplicate keys. ')

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Context uses Python identifier Context
    __Context = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Context'), 'Context', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_Context', pyxb.binding.datatypes.string)
    __Context._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 232, 5)
    __Context._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 232, 5)
    
    Context = property(__Context.value, __Context.set, None, None)

    
    # Attribute Status uses Python identifier Status
    __Status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Status'), 'Status', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_Status', SupportedAcquisitionStates)
    __Status._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 233, 5)
    __Status._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 233, 5)
    
    Status = property(__Status.value, __Status.set, None, None)

    
    # Attribute InstrumentId uses Python identifier InstrumentId
    __InstrumentId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'InstrumentId'), 'InstrumentId', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_InstrumentId', pyxb.binding.datatypes.string)
    __InstrumentId._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 234, 5)
    __InstrumentId._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 234, 5)
    
    InstrumentId = property(__InstrumentId.value, __InstrumentId.set, None, 'World unique id assigned by PacBio. ')

    
    # Attribute InstrumentName uses Python identifier InstrumentName
    __InstrumentName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'InstrumentName'), 'InstrumentName', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_70_InstrumentName', pyxb.binding.datatypes.string)
    __InstrumentName._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 239, 5)
    __InstrumentName._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 239, 5)
    
    InstrumentName = property(__InstrumentName.value, __InstrumentName.set, None, 'Friendly name assigned by customer')

    _ElementMap.update({
        __InstCtrlVer.name() : __InstCtrlVer,
        __SigProcVer.name() : __SigProcVer,
        __Automation.name() : __Automation,
        __CollectionNumber.name() : __CollectionNumber,
        __CellIndex.name() : __CellIndex,
        __SetNumber.name() : __SetNumber,
        __CellPac.name() : __CellPac,
        __TemplatePrepKit.name() : __TemplatePrepKit,
        __BindingKit.name() : __BindingKit,
        __SequencingKitPlate.name() : __SequencingKitPlate,
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



# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSampleType with content type ELEMENT_ONLY
class BioSampleType (BaseEntityType):
    """The actual biological sample; this could be prep'd, or in original form; could be bound, or annealed..."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BioSampleType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 365, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSamples uses Python identifier BioSamples
    __BioSamples = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BioSamples'), 'BioSamples', '__httppacificbiosciences_comPacBioDataModel_xsd_BioSampleType_httppacificbiosciences_comPacBioDataModel_xsdBioSamples', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 673, 1), )

    
    BioSamples = property(__BioSamples.value, __BioSamples.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute DateReceived uses Python identifier DateReceived
    __DateReceived = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DateReceived'), 'DateReceived', '__httppacificbiosciences_comPacBioDataModel_xsd_BioSampleType_DateReceived', pyxb.binding.datatypes.dateTime)
    __DateReceived._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 374, 4)
    __DateReceived._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 374, 4)
    
    DateReceived = property(__DateReceived.value, __DateReceived.set, None, 'Date the sample was received by the lab')

    
    # Attribute Organism uses Python identifier Organism
    __Organism = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Organism'), 'Organism', '__httppacificbiosciences_comPacBioDataModel_xsd_BioSampleType_Organism', pyxb.binding.datatypes.string)
    __Organism._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 379, 4)
    __Organism._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 379, 4)
    
    Organism = property(__Organism.value, __Organism.set, None, 'e.g. HIV, E.coli')

    
    # Attribute Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Reference'), 'Reference', '__httppacificbiosciences_comPacBioDataModel_xsd_BioSampleType_Reference', pyxb.binding.datatypes.string)
    __Reference._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 384, 4)
    __Reference._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 384, 4)
    
    Reference = property(__Reference.value, __Reference.set, None, 'Name of reference, or pointer to one at e.g. NCBI RefSeq')

    
    # Attribute DNAType uses Python identifier DNAType
    __DNAType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DNAType'), 'DNAType', '__httppacificbiosciences_comPacBioDataModel_xsd_BioSampleType_DNAType', pyxb.binding.datatypes.string)
    __DNAType._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 389, 4)
    __DNAType._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 389, 4)
    
    DNAType = property(__DNAType.value, __DNAType.set, None, 'shotgun library, amplicon, etc.')

    
    # Attribute Concentration uses Python identifier Concentration
    __Concentration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Concentration'), 'Concentration', '__httppacificbiosciences_comPacBioDataModel_xsd_BioSampleType_Concentration', pyxb.binding.datatypes.float)
    __Concentration._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 394, 4)
    __Concentration._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 394, 4)
    
    Concentration = property(__Concentration.value, __Concentration.set, None, 'in ng/uL, e.g. 250')

    
    # Attribute QuantificationMethod uses Python identifier QuantificationMethod
    __QuantificationMethod = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'QuantificationMethod'), 'QuantificationMethod', '__httppacificbiosciences_comPacBioDataModel_xsd_BioSampleType_QuantificationMethod', pyxb.binding.datatypes.string)
    __QuantificationMethod._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 399, 4)
    __QuantificationMethod._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 399, 4)
    
    QuantificationMethod = property(__QuantificationMethod.value, __QuantificationMethod.set, None, 'e.g. Qubit')

    
    # Attribute SMRTBellConcentration uses Python identifier SMRTBellConcentration
    __SMRTBellConcentration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SMRTBellConcentration'), 'SMRTBellConcentration', '__httppacificbiosciences_comPacBioDataModel_xsd_BioSampleType_SMRTBellConcentration', pyxb.binding.datatypes.float)
    __SMRTBellConcentration._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 404, 4)
    __SMRTBellConcentration._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 404, 4)
    
    SMRTBellConcentration = property(__SMRTBellConcentration.value, __SMRTBellConcentration.set, None, 'in ng/uL, e.g. 4.5')

    
    # Attribute SMRTBellQuantificationMethod uses Python identifier SMRTBellQuantificationMethod
    __SMRTBellQuantificationMethod = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SMRTBellQuantificationMethod'), 'SMRTBellQuantificationMethod', '__httppacificbiosciences_comPacBioDataModel_xsd_BioSampleType_SMRTBellQuantificationMethod', pyxb.binding.datatypes.string)
    __SMRTBellQuantificationMethod._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 409, 4)
    __SMRTBellQuantificationMethod._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 409, 4)
    
    SMRTBellQuantificationMethod = property(__SMRTBellQuantificationMethod.value, __SMRTBellQuantificationMethod.set, None, 'e.g. Qubit')

    
    # Attribute BufferName uses Python identifier BufferName
    __BufferName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'BufferName'), 'BufferName', '__httppacificbiosciences_comPacBioDataModel_xsd_BioSampleType_BufferName', pyxb.binding.datatypes.string)
    __BufferName._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 414, 4)
    __BufferName._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 414, 4)
    
    BufferName = property(__BufferName.value, __BufferName.set, None, 'e.g. Tris HCl')

    
    # Attribute SamplePrepKit uses Python identifier SamplePrepKit
    __SamplePrepKit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SamplePrepKit'), 'SamplePrepKit', '__httppacificbiosciences_comPacBioDataModel_xsd_BioSampleType_SamplePrepKit', pyxb.binding.datatypes.string)
    __SamplePrepKit._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 419, 4)
    __SamplePrepKit._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 419, 4)
    
    SamplePrepKit = property(__SamplePrepKit.value, __SamplePrepKit.set, None, 'e.g. SMRTbell Template Prep Kit')

    
    # Attribute TargetLibrarySize uses Python identifier TargetLibrarySize
    __TargetLibrarySize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TargetLibrarySize'), 'TargetLibrarySize', '__httppacificbiosciences_comPacBioDataModel_xsd_BioSampleType_TargetLibrarySize', pyxb.binding.datatypes.string)
    __TargetLibrarySize._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 424, 4)
    __TargetLibrarySize._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 424, 4)
    
    TargetLibrarySize = property(__TargetLibrarySize.value, __TargetLibrarySize.set, None, '2000, 10000, 20000')

    _ElementMap.update({
        __BioSamples.name() : __BioSamples
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
Namespace.addCategoryObject('typeBinding', 'BioSampleType', BioSampleType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_71 (BaseEntityType):
    """Container for the sample related data. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 436, 2)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}PlateId uses Python identifier PlateId
    __PlateId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PlateId'), 'PlateId', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_71_httppacificbiosciences_comPacBioDataModel_xsdPlateId', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 440, 6), )

    
    PlateId = property(__PlateId.value, __PlateId.set, None, 'The ID of the sample plate. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}WellName uses Python identifier WellName
    __WellName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WellName'), 'WellName', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_71_httppacificbiosciences_comPacBioDataModel_xsdWellName', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 445, 6), )

    
    WellName = property(__WellName.value, __WellName.set, None, 'Identifies which well this sample came from (e.g., coordinate on a plate). ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Concentration uses Python identifier Concentration
    __Concentration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Concentration'), 'Concentration', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_71_httppacificbiosciences_comPacBioDataModel_xsdConcentration', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 450, 6), )

    
    Concentration = property(__Concentration.value, __Concentration.set, None, 'Sample input concentration. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SampleReuseEnabled uses Python identifier SampleReuseEnabled
    __SampleReuseEnabled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SampleReuseEnabled'), 'SampleReuseEnabled', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_71_httppacificbiosciences_comPacBioDataModel_xsdSampleReuseEnabled', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 455, 6), )

    
    SampleReuseEnabled = property(__SampleReuseEnabled.value, __SampleReuseEnabled.set, None, 'Whether or not complex reuse is enabled for this well. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}StageHotstartEnabled uses Python identifier StageHotstartEnabled
    __StageHotstartEnabled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StageHotstartEnabled'), 'StageHotstartEnabled', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_71_httppacificbiosciences_comPacBioDataModel_xsdStageHotstartEnabled', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 460, 6), )

    
    StageHotstartEnabled = property(__StageHotstartEnabled.value, __StageHotstartEnabled.set, None, 'Whether or not hotstart at the stage is enabled for this well. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SizeSelectionEnabled uses Python identifier SizeSelectionEnabled
    __SizeSelectionEnabled = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SizeSelectionEnabled'), 'SizeSelectionEnabled', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_71_httppacificbiosciences_comPacBioDataModel_xsdSizeSelectionEnabled', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 465, 6), )

    
    SizeSelectionEnabled = property(__SizeSelectionEnabled.value, __SizeSelectionEnabled.set, None, 'Whether or not size selection is enabled for this well. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}UseCount uses Python identifier UseCount
    __UseCount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UseCount'), 'UseCount', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_71_httppacificbiosciences_comPacBioDataModel_xsdUseCount', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 470, 6), )

    
    UseCount = property(__UseCount.value, __UseCount.set, None, 'Count of usages for this batch of complex. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Comments uses Python identifier Comments
    __Comments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Comments'), 'Comments', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_71_httppacificbiosciences_comPacBioDataModel_xsdComments', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 475, 6), )

    
    Comments = property(__Comments.value, __Comments.set, None, 'User-supplied comments about the sample. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DNAControlComplex uses Python identifier DNAControlComplex
    __DNAControlComplex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DNAControlComplex'), 'DNAControlComplex', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_71_httppacificbiosciences_comPacBioDataModel_xsdDNAControlComplex', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 480, 6), )

    
    DNAControlComplex = property(__DNAControlComplex.value, __DNAControlComplex.set, None, 'Indicating what kind (if any) control was used. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SampleBarcodeInfo uses Python identifier SampleBarcodeInfo
    __SampleBarcodeInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SampleBarcodeInfo'), 'SampleBarcodeInfo', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_71_httppacificbiosciences_comPacBioDataModel_xsdSampleBarcodeInfo', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 485, 6), )

    
    SampleBarcodeInfo = property(__SampleBarcodeInfo.value, __SampleBarcodeInfo.set, None, 'When utilizing DNA barcoding, store the list of smaple barcodes in this element.')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSamplePointers uses Python identifier BioSamplePointers
    __BioSamplePointers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BioSamplePointers'), 'BioSamplePointers', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_71_httppacificbiosciences_comPacBioDataModel_xsdBioSamplePointers', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 639, 1), )

    
    BioSamplePointers = property(__BioSamplePointers.value, __BioSamplePointers.set, None, 'Back references to other BarcodedSampleType object UniqueIds which utilize this sample')

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __PlateId.name() : __PlateId,
        __WellName.name() : __WellName,
        __Concentration.name() : __Concentration,
        __SampleReuseEnabled.name() : __SampleReuseEnabled,
        __StageHotstartEnabled.name() : __StageHotstartEnabled,
        __SizeSelectionEnabled.name() : __SizeSelectionEnabled,
        __UseCount.name() : __UseCount,
        __Comments.name() : __Comments,
        __DNAControlComplex.name() : __DNAControlComplex,
        __SampleBarcodeInfo.name() : __SampleBarcodeInfo,
        __BioSamplePointers.name() : __BioSamplePointers
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentType with content type ELEMENT_ONLY
class ReagentType (BaseEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReagentType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 54, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ReagentKey uses Python identifier ReagentKey
    __ReagentKey = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ReagentKey'), 'ReagentKey', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentType_ReagentKey', ReagentKey, required=True)
    __ReagentKey._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 57, 4)
    __ReagentKey._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 57, 4)
    
    ReagentKey = property(__ReagentKey.value, __ReagentKey.set, None, None)

    
    # Attribute PlateColumn uses Python identifier PlateColumn
    __PlateColumn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PlateColumn'), 'PlateColumn', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentType_PlateColumn', pyxb.binding.datatypes.string, required=True)
    __PlateColumn._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 58, 4)
    __PlateColumn._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 58, 4)
    
    PlateColumn = property(__PlateColumn.value, __PlateColumn.set, None, None)

    
    # Attribute Volume uses Python identifier Volume
    __Volume = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Volume'), 'Volume', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentType_Volume', pyxb.binding.datatypes.int, required=True)
    __Volume._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 59, 4)
    __Volume._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 59, 4)
    
    Volume = property(__Volume.value, __Volume.set, None, None)

    
    # Attribute DeadVolume uses Python identifier DeadVolume
    __DeadVolume = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DeadVolume'), 'DeadVolume', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentType_DeadVolume', pyxb.binding.datatypes.int, required=True)
    __DeadVolume._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 60, 4)
    __DeadVolume._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 60, 4)
    
    DeadVolume = property(__DeadVolume.value, __DeadVolume.set, None, None)

    
    # Attribute ActiveInHour uses Python identifier ActiveInHour
    __ActiveInHour = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ActiveInHour'), 'ActiveInHour', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentType_ActiveInHour', pyxb.binding.datatypes.int, required=True)
    __ActiveInHour._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 61, 4)
    __ActiveInHour._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 61, 4)
    
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


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentKitType with content type ELEMENT_ONLY
class ReagentKitType (BaseEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentKitType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReagentKitType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 65, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Reagents uses Python identifier Reagents
    __Reagents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reagents'), 'Reagents', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentKitType_httppacificbiosciences_comPacBioDataModel_xsdReagents', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 69, 5), )

    
    Reagents = property(__Reagents.value, __Reagents.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentTubes uses Python identifier ReagentTubes
    __ReagentTubes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentTubes'), 'ReagentTubes', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentKitType_httppacificbiosciences_comPacBioDataModel_xsdReagentTubes', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 76, 5), )

    
    ReagentTubes = property(__ReagentTubes.value, __ReagentTubes.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentPlateRows uses Python identifier ReagentPlateRows
    __ReagentPlateRows = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRows'), 'ReagentPlateRows', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentKitType_httppacificbiosciences_comPacBioDataModel_xsdReagentPlateRows', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 83, 5), )

    
    ReagentPlateRows = property(__ReagentPlateRows.value, __ReagentPlateRows.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CompatibleAutomations uses Python identifier CompatibleAutomations
    __CompatibleAutomations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CompatibleAutomations'), 'CompatibleAutomations', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentKitType_httppacificbiosciences_comPacBioDataModel_xsdCompatibleAutomations', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 90, 5), )

    
    CompatibleAutomations = property(__CompatibleAutomations.value, __CompatibleAutomations.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ProductCode uses Python identifier ProductCode
    __ProductCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ProductCode'), 'ProductCode', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentKitType_ProductCode', pyxb.binding.datatypes.string)
    __ProductCode._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 98, 4)
    __ProductCode._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 98, 4)
    
    ProductCode = property(__ProductCode.value, __ProductCode.set, None, None)

    
    # Attribute PlateType uses Python identifier PlateType
    __PlateType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PlateType'), 'PlateType', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentKitType_PlateType', pyxb.binding.datatypes.string)
    __PlateType._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 99, 4)
    __PlateType._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 99, 4)
    
    PlateType = property(__PlateType.value, __PlateType.set, None, None)

    
    # Attribute ActiveInHour uses Python identifier ActiveInHour
    __ActiveInHour = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ActiveInHour'), 'ActiveInHour', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentKitType_ActiveInHour', pyxb.binding.datatypes.int)
    __ActiveInHour._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 100, 4)
    __ActiveInHour._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 100, 4)
    
    ActiveInHour = property(__ActiveInHour.value, __ActiveInHour.set, None, None)

    
    # Attribute BasesPerSecond uses Python identifier BasesPerSecond
    __BasesPerSecond = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'BasesPerSecond'), 'BasesPerSecond', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentKitType_BasesPerSecond', pyxb.binding.datatypes.decimal)
    __BasesPerSecond._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 101, 4)
    __BasesPerSecond._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 101, 4)
    
    BasesPerSecond = property(__BasesPerSecond.value, __BasesPerSecond.set, None, None)

    
    # Attribute AcquisitionCount uses Python identifier AcquisitionCount
    __AcquisitionCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'AcquisitionCount'), 'AcquisitionCount', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentKitType_AcquisitionCount', pyxb.binding.datatypes.int)
    __AcquisitionCount._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 102, 4)
    __AcquisitionCount._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 102, 4)
    
    AcquisitionCount = property(__AcquisitionCount.value, __AcquisitionCount.set, None, None)

    _ElementMap.update({
        __Reagents.name() : __Reagents,
        __ReagentTubes.name() : __ReagentTubes,
        __ReagentPlateRows.name() : __ReagentPlateRows,
        __CompatibleAutomations.name() : __CompatibleAutomations
    })
    _AttributeMap.update({
        __ProductCode.name() : __ProductCode,
        __PlateType.name() : __PlateType,
        __ActiveInHour.name() : __ActiveInHour,
        __BasesPerSecond.name() : __BasesPerSecond,
        __AcquisitionCount.name() : __AcquisitionCount
    })
Namespace.addCategoryObject('typeBinding', 'ReagentKitType', ReagentKitType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentTubeType with content type ELEMENT_ONLY
class ReagentTubeType (BaseEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentTubeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReagentTubeType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 106, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ProductCode uses Python identifier ProductCode
    __ProductCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ProductCode'), 'ProductCode', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentTubeType_ProductCode', pyxb.binding.datatypes.string, required=True)
    __ProductCode._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 109, 4)
    __ProductCode._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 109, 4)
    
    ProductCode = property(__ProductCode.value, __ProductCode.set, None, None)

    
    # Attribute ReagentKey uses Python identifier ReagentKey
    __ReagentKey = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ReagentKey'), 'ReagentKey', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentTubeType_ReagentKey', ReagentKey, required=True)
    __ReagentKey._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 110, 4)
    __ReagentKey._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 110, 4)
    
    ReagentKey = property(__ReagentKey.value, __ReagentKey.set, None, None)

    
    # Attribute Volume uses Python identifier Volume
    __Volume = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Volume'), 'Volume', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentTubeType_Volume', pyxb.binding.datatypes.short, required=True)
    __Volume._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 111, 4)
    __Volume._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 111, 4)
    
    Volume = property(__Volume.value, __Volume.set, None, None)

    
    # Attribute DeadVolume uses Python identifier DeadVolume
    __DeadVolume = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DeadVolume'), 'DeadVolume', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentTubeType_DeadVolume', pyxb.binding.datatypes.short, required=True)
    __DeadVolume._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 112, 4)
    __DeadVolume._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 112, 4)
    
    DeadVolume = property(__DeadVolume.value, __DeadVolume.set, None, None)

    
    # Attribute ActiveInHour uses Python identifier ActiveInHour
    __ActiveInHour = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ActiveInHour'), 'ActiveInHour', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentTubeType_ActiveInHour', pyxb.binding.datatypes.int, required=True)
    __ActiveInHour._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 113, 4)
    __ActiveInHour._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 113, 4)
    
    ActiveInHour = property(__ActiveInHour.value, __ActiveInHour.set, None, None)

    
    # Attribute TubeWellType uses Python identifier TubeWellType
    __TubeWellType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TubeWellType'), 'TubeWellType', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentTubeType_TubeWellType', TubeSize, required=True)
    __TubeWellType._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 114, 4)
    __TubeWellType._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 114, 4)
    
    TubeWellType = property(__TubeWellType.value, __TubeWellType.set, None, None)

    
    # Attribute ReagentTubeType uses Python identifier ReagentTubeType
    __ReagentTubeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ReagentTubeType'), 'ReagentTubeType', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentTubeType_ReagentTubeType', TubeLocation, required=True)
    __ReagentTubeType._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 115, 4)
    __ReagentTubeType._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 115, 4)
    
    ReagentTubeType = property(__ReagentTubeType.value, __ReagentTubeType.set, None, None)

    
    # Attribute InitialUse uses Python identifier InitialUse
    __InitialUse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'InitialUse'), 'InitialUse', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentTubeType_InitialUse', pyxb.binding.datatypes.dateTime)
    __InitialUse._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 116, 4)
    __InitialUse._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 116, 4)
    
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


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentPlateRowType with content type ELEMENT_ONLY
class ReagentPlateRowType (BaseEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentPlateRowType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRowType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 120, 1)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute PlateRow uses Python identifier PlateRow
    __PlateRow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PlateRow'), 'PlateRow', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentPlateRowType_PlateRow', pyxb.binding.datatypes.string, required=True)
    __PlateRow._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 123, 4)
    __PlateRow._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 123, 4)
    
    PlateRow = property(__PlateRow.value, __PlateRow.set, None, None)

    
    # Attribute InitialUse uses Python identifier InitialUse
    __InitialUse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'InitialUse'), 'InitialUse', '__httppacificbiosciences_comPacBioDataModel_xsd_ReagentPlateRowType_InitialUse', pyxb.binding.datatypes.dateTime)
    __InitialUse._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 124, 4)
    __InitialUse._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 124, 4)
    
    InitialUse = property(__InitialUse.value, __InitialUse.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __PlateRow.name() : __PlateRow,
        __InitialUse.name() : __InitialUse
    })
Namespace.addCategoryObject('typeBinding', 'ReagentPlateRowType', ReagentPlateRowType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_72 (BaseEntityType):
    """List of contigs in a ContigSet"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 118, 2)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Contig uses Python identifier Contig
    __Contig = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Contig'), 'Contig', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_72_httppacificbiosciences_comPacBioDataModel_xsdContig', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 122, 6), )

    
    Contig = property(__Contig.value, __Contig.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __Contig.name() : __Contig
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_73 (BaseEntityType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 123, 7)
    _ElementMap = BaseEntityType._ElementMap.copy()
    _AttributeMap = BaseEntityType._AttributeMap.copy()
    # Base type is BaseEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Length uses Python identifier Length
    __Length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Length'), 'Length', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_73_Length', pyxb.binding.datatypes.anySimpleType, required=True)
    __Length._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 126, 10)
    __Length._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 126, 10)
    
    Length = property(__Length.value, __Length.set, None, None)

    
    # Attribute Digest uses Python identifier Digest
    __Digest = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Digest'), 'Digest', '__httppacificbiosciences_comPacBioDataModel_xsd_CTD_ANON_73_Digest', pyxb.binding.datatypes.anySimpleType, required=True)
    __Digest._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 127, 10)
    __Digest._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 127, 10)
    
    Digest = property(__Digest.value, __Digest.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Length.name() : __Length,
        __Digest.name() : __Digest
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_74 (AnalogType):
    """An unlimited number of analogs listed for the purposes of hosting in a configuration file. e.g. a list of all possible analogs on the system"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 130, 2)
    _ElementMap = AnalogType._ElementMap.copy()
    _AttributeMap = AnalogType._AttributeMap.copy()
    # Base type is AnalogType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Base inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute SpectralAngle inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute RelativeAmplitude inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute Label inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute Nucleotide inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute Wavelength inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute CompoundID inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute LotID inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_75 (AnalogType):
    """A set of four analogs, one for each of the nucleotides, grouped together for the purposes of a single experiment."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 196, 2)
    _ElementMap = AnalogType._ElementMap.copy()
    _AttributeMap = AnalogType._AttributeMap.copy()
    # Base type is AnalogType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Base inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute SpectralAngle inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute RelativeAmplitude inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute Label inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute Nucleotide inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute Wavelength inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute CompoundID inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute LotID inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AnalogType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}InputOutputDataType with content type ELEMENT_ONLY
class InputOutputDataType (DataEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}InputOutputDataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InputOutputDataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 212, 1)
    _ElementMap = DataEntityType._ElementMap.copy()
    _AttributeMap = DataEntityType._AttributeMap.copy()
    # Base type is DataEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'InputOutputDataType', InputOutputDataType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType with content type ELEMENT_ONLY
class PartNumberType (DataEntityType):
    """Generic representation of a supply kit. 

If the part number has an NFC associated with it, the contents of the NFC may be encoded here."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartNumberType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 258, 1)
    _ElementMap = DataEntityType._ElementMap.copy()
    _AttributeMap = DataEntityType._AttributeMap.copy()
    # Base type is DataEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatiblePartNumbers uses Python identifier IncompatiblePartNumbers
    __IncompatiblePartNumbers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePartNumbers'), 'IncompatiblePartNumbers', '__httppacificbiosciences_comPacBioDataModel_xsd_PartNumberType_httppacificbiosciences_comPacBioDataModel_xsdIncompatiblePartNumbers', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5), )

    
    IncompatiblePartNumbers = property(__IncompatiblePartNumbers.value, __IncompatiblePartNumbers.set, None, 'By default, a PN is compatible for use with other PNs in the system.  In order to exclude the usage of one or more PNs with this one, the incompatible PNs are listed here.')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatibleAutomations uses Python identifier IncompatibleAutomations
    __IncompatibleAutomations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleAutomations'), 'IncompatibleAutomations', '__httppacificbiosciences_comPacBioDataModel_xsd_PartNumberType_httppacificbiosciences_comPacBioDataModel_xsdIncompatibleAutomations', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5), )

    
    IncompatibleAutomations = property(__IncompatibleAutomations.value, __IncompatibleAutomations.set, None, 'By default, a PN is compatible for use with all automations in the system.  In order to exclude the usage of automations with this PN, the incompatible automation names are listed here.')

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute PartNumber uses Python identifier PartNumber
    __PartNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PartNumber'), 'PartNumber', '__httppacificbiosciences_comPacBioDataModel_xsd_PartNumberType_PartNumber', pyxb.binding.datatypes.string)
    __PartNumber._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 296, 4)
    __PartNumber._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 296, 4)
    
    PartNumber = property(__PartNumber.value, __PartNumber.set, None, 'The kit part number')

    
    # Attribute LotNumber uses Python identifier LotNumber
    __LotNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'LotNumber'), 'LotNumber', '__httppacificbiosciences_comPacBioDataModel_xsd_PartNumberType_LotNumber', pyxb.binding.datatypes.string)
    __LotNumber._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 301, 4)
    __LotNumber._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 301, 4)
    
    LotNumber = property(__LotNumber.value, __LotNumber.set, None, 'The kit lot number')

    
    # Attribute Barcode uses Python identifier Barcode
    __Barcode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Barcode'), 'Barcode', '__httppacificbiosciences_comPacBioDataModel_xsd_PartNumberType_Barcode', pyxb.binding.datatypes.string)
    __Barcode._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 306, 4)
    __Barcode._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 306, 4)
    
    Barcode = property(__Barcode.value, __Barcode.set, None, 'The kit barcode; used for tracking purposes.')

    
    # Attribute ExpirationDate uses Python identifier ExpirationDate
    __ExpirationDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ExpirationDate'), 'ExpirationDate', '__httppacificbiosciences_comPacBioDataModel_xsd_PartNumberType_ExpirationDate', pyxb.binding.datatypes.date)
    __ExpirationDate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 311, 4)
    __ExpirationDate._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 311, 4)
    
    ExpirationDate = property(__ExpirationDate.value, __ExpirationDate.set, None, "The kit's shelf life")

    
    # Attribute IsObsolete uses Python identifier IsObsolete
    __IsObsolete = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IsObsolete'), 'IsObsolete', '__httppacificbiosciences_comPacBioDataModel_xsd_PartNumberType_IsObsolete', pyxb.binding.datatypes.boolean, unicode_default='false')
    __IsObsolete._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 316, 4)
    __IsObsolete._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 316, 4)
    
    IsObsolete = property(__IsObsolete.value, __IsObsolete.set, None, None)

    _ElementMap.update({
        __IncompatiblePartNumbers.name() : __IncompatiblePartNumbers,
        __IncompatibleAutomations.name() : __IncompatibleAutomations
    })
    _AttributeMap.update({
        __PartNumber.name() : __PartNumber,
        __LotNumber.name() : __LotNumber,
        __Barcode.name() : __Barcode,
        __ExpirationDate.name() : __ExpirationDate,
        __IsObsolete.name() : __IsObsolete
    })
Namespace.addCategoryObject('typeBinding', 'PartNumberType', PartNumberType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}RecordedEventType with content type ELEMENT_ONLY
class RecordedEventType (DataEntityType):
    """Metrics, system events, alarms, and logs may utilize this type"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RecordedEventType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 320, 1)
    _ElementMap = DataEntityType._ElementMap.copy()
    _AttributeMap = DataEntityType._AttributeMap.copy()
    # Base type is DataEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute Context uses Python identifier Context
    __Context = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Context'), 'Context', '__httppacificbiosciences_comPacBioDataModel_xsd_RecordedEventType_Context', pyxb.binding.datatypes.string)
    __Context._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 326, 4)
    __Context._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 326, 4)
    
    Context = property(__Context.value, __Context.set, None, 'The part of the system in effect when the event was recorded')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Context.name() : __Context
    })
Namespace.addCategoryObject('typeBinding', 'RecordedEventType', RecordedEventType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}SequencingChemistry with content type ELEMENT_ONLY
class SequencingChemistry (DataEntityType):
    """A container for a set of analogs"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SequencingChemistry')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 334, 1)
    _ElementMap = DataEntityType._ElementMap.copy()
    _AttributeMap = DataEntityType._AttributeMap.copy()
    # Base type is DataEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DyeSet uses Python identifier DyeSet
    __DyeSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DyeSet'), 'DyeSet', '__httppacificbiosciences_comPacBioDataModel_xsd_SequencingChemistry_httppacificbiosciences_comPacBioDataModel_xsdDyeSet', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 341, 5), )

    
    DyeSet = property(__DyeSet.value, __DyeSet.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    _ElementMap.update({
        __DyeSet.name() : __DyeSet
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SequencingChemistry', SequencingChemistry)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ReadSetType with content type ELEMENT_ONLY
class ReadSetType (DataSetType):
    """Type for DataSets consisting of unaligned subreads and CCS reads DataSets"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ReadSetType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 19, 1)
    _ElementMap = DataSetType._ElementMap.copy()
    _AttributeMap = DataSetType._AttributeMap.copy()
    # Base type is DataSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadata uses Python identifier DataSetMetadata
    __DataSetMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), 'DataSetMetadata', '__httppacificbiosciences_comPacBioDataModel_xsd_ReadSetType_httppacificbiosciences_comPacBioDataModel_xsdDataSetMetadata', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 26, 5), )

    
    DataSetMetadata = property(__DataSetMetadata.value, __DataSetMetadata.set, None, None)

    
    # Element Filters ({http://pacificbiosciences.com/PacBioDataModel.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __DataSetMetadata.name() : __DataSetMetadata
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ReadSetType', ReadSetType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}BarcodedSampleType with content type ELEMENT_ONLY
class BarcodedSampleType (BioSampleType):
    """This is a data type to hold a barcoded biological sample, or a raw biological sample - so, barcode is optional."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BarcodedSampleType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 340, 1)
    _ElementMap = BioSampleType._ElementMap.copy()
    _AttributeMap = BioSampleType._AttributeMap.copy()
    # Base type is BioSampleType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Barcodes uses Python identifier Barcodes
    __Barcodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Barcodes'), 'Barcodes', '__httppacificbiosciences_comPacBioDataModel_xsd_BarcodedSampleType_httppacificbiosciences_comPacBioDataModel_xsdBarcodes', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 347, 5), )

    
    Barcodes = property(__Barcodes.value, __Barcodes.set, None, 'A list of barcodes associated with the biological sample')

    
    # Element BioSamples ({http://pacificbiosciences.com/PacBioDataModel.xsd}BioSamples) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSampleType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute DateReceived inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSampleType
    
    # Attribute Organism inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSampleType
    
    # Attribute Reference inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSampleType
    
    # Attribute DNAType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSampleType
    
    # Attribute Concentration inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSampleType
    
    # Attribute QuantificationMethod inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSampleType
    
    # Attribute SMRTBellConcentration inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSampleType
    
    # Attribute SMRTBellQuantificationMethod inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSampleType
    
    # Attribute BufferName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSampleType
    
    # Attribute SamplePrepKit inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSampleType
    
    # Attribute TargetLibrarySize inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSampleType
    _ElementMap.update({
        __Barcodes.name() : __Barcodes
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BarcodedSampleType', BarcodedSampleType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}AssayType with content type ELEMENT_ONLY
class AssayType (DataEntityType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}AssayType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssayType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 237, 1)
    _ElementMap = DataEntityType._ElementMap.copy()
    _AttributeMap = DataEntityType._AttributeMap.copy()
    # Base type is DataEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SubreadSet uses Python identifier SubreadSet
    __SubreadSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubreadSet'), 'SubreadSet', '__httppacificbiosciences_comPacBioDataModel_xsd_AssayType_httppacificbiosciences_comPacBioDataModel_xsdSubreadSet', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 681, 1), )

    
    SubreadSet = property(__SubreadSet.value, __SubreadSet.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    _ElementMap.update({
        __SubreadSet.name() : __SubreadSet
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AssayType', AssayType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ExperimentContainerType with content type ELEMENT_ONLY
class ExperimentContainerType (DataEntityType):
    """A composite object type that can encompass multiple runs, possibly across multiple instruments.  

One use case may be that a user may have a large genome they'd like to sequence, and it may take multiple runs on multiple instruments, to get enough data.  Another use case may be that a user has multiple samples of the same phenotype which they would like to analyze in a similar fashion/automation, and as such these samples are run as part of one experiment.

The experiment object is intended to be packagable, such that the metadata of all acquisitions within is contained."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExperimentContainerType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 246, 1)
    _ElementMap = DataEntityType._ElementMap.copy()
    _AttributeMap = DataEntityType._AttributeMap.copy()
    # Base type is DataEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}InvestigatorName uses Python identifier InvestigatorName
    __InvestigatorName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InvestigatorName'), 'InvestigatorName', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_httppacificbiosciences_comPacBioDataModel_xsdInvestigatorName', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 257, 5), )

    
    InvestigatorName = property(__InvestigatorName.value, __InvestigatorName.set, None, 'An optional PI name')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}CreatedDate uses Python identifier CreatedDate
    __CreatedDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CreatedDate'), 'CreatedDate', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_httppacificbiosciences_comPacBioDataModel_xsdCreatedDate', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 262, 5), )

    
    CreatedDate = property(__CreatedDate.value, __CreatedDate.set, None, 'Automatically generated creation date')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Runs uses Python identifier Runs
    __Runs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Runs'), 'Runs', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_httppacificbiosciences_comPacBioDataModel_xsdRuns', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 267, 5), )

    
    Runs = property(__Runs.value, __Runs.set, None, 'Multiple acquisitions from different instrument runs')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets uses Python identifier DataSets
    __DataSets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSets'), 'DataSets', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_httppacificbiosciences_comPacBioDataModel_xsdDataSets', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 277, 5), )

    
    DataSets = property(__DataSets.value, __DataSets.set, None, 'Pointers to various data elements associated with the acquisitions')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RecordedEvents uses Python identifier RecordedEvents
    __RecordedEvents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvents'), 'RecordedEvents', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_httppacificbiosciences_comPacBioDataModel_xsdRecordedEvents', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 287, 5), )

    
    RecordedEvents = property(__RecordedEvents.value, __RecordedEvents.set, None, "Journal of metrics, system events, or alarms that were generated during this container's lifetime")

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}BioSamples uses Python identifier BioSamples
    __BioSamples = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BioSamples'), 'BioSamples', '__httppacificbiosciences_comPacBioDataModel_xsd_ExperimentContainerType_httppacificbiosciences_comPacBioDataModel_xsdBioSamples', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 301, 5), )

    
    BioSamples = property(__BioSamples.value, __BioSamples.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    _ElementMap.update({
        __InvestigatorName.name() : __InvestigatorName,
        __CreatedDate.name() : __CreatedDate,
        __Runs.name() : __Runs,
        __DataSets.name() : __DataSets,
        __RecordedEvents.name() : __RecordedEvents,
        __BioSamples.name() : __BioSamples
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ExperimentContainerType', ExperimentContainerType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}RunType with content type ELEMENT_ONLY
class RunType (DataEntityType):
    """A run is defined as a set of one or more data collections acquired in sequence on an instrument.  A run specifies the wells and SMRT Cells to include in the sequencing run, along with the collection and analysis automation to use for the selected wells and cells.

"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RunType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 312, 1)
    _ElementMap = DataEntityType._ElementMap.copy()
    _AttributeMap = DataEntityType._AttributeMap.copy()
    # Base type is DataEntityType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SubreadSet uses Python identifier SubreadSet
    __SubreadSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubreadSet'), 'SubreadSet', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_httppacificbiosciences_comPacBioDataModel_xsdSubreadSet', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 681, 1), )

    
    SubreadSet = property(__SubreadSet.value, __SubreadSet.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Assay uses Python identifier Assay
    __Assay = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Assay'), 'Assay', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_httppacificbiosciences_comPacBioDataModel_xsdAssay', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 11, 1), )

    
    Assay = property(__Assay.value, __Assay.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RunResources uses Python identifier RunResources
    __RunResources = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RunResources'), 'RunResources', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_httppacificbiosciences_comPacBioDataModel_xsdRunResources', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 129, 1), )

    
    RunResources = property(__RunResources.value, __RunResources.set, None, 'This is an output field specifying the requirements for the run, e.g. number of tips, estimated run time, etc.')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Inputs uses Python identifier Inputs
    __Inputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Inputs'), 'Inputs', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_httppacificbiosciences_comPacBioDataModel_xsdInputs', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 321, 5), )

    
    Inputs = property(__Inputs.value, __Inputs.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Outputs uses Python identifier Outputs
    __Outputs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Outputs'), 'Outputs', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_httppacificbiosciences_comPacBioDataModel_xsdOutputs', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 328, 5), )

    
    Outputs = property(__Outputs.value, __Outputs.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RecordedEvents uses Python identifier RecordedEvents
    __RecordedEvents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvents'), 'RecordedEvents', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_httppacificbiosciences_comPacBioDataModel_xsdRecordedEvents', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 341, 5), )

    
    RecordedEvents = property(__RecordedEvents.value, __RecordedEvents.set, None, "Journal of metrics, system events, or alarms that were generated during this run's lifetime")

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute Status uses Python identifier Status
    __Status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Status'), 'Status', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_Status', SupportedRunStates)
    __Status._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 358, 4)
    __Status._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 358, 4)
    
    Status = property(__Status.value, __Status.set, None, None)

    
    # Attribute InstrumentId uses Python identifier InstrumentId
    __InstrumentId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'InstrumentId'), 'InstrumentId', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_InstrumentId', pyxb.binding.datatypes.string)
    __InstrumentId._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 359, 4)
    __InstrumentId._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 359, 4)
    
    InstrumentId = property(__InstrumentId.value, __InstrumentId.set, None, 'World unique id assigned by PacBio. ')

    
    # Attribute InstrumentName uses Python identifier InstrumentName
    __InstrumentName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'InstrumentName'), 'InstrumentName', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_InstrumentName', pyxb.binding.datatypes.string)
    __InstrumentName._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 364, 4)
    __InstrumentName._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 364, 4)
    
    InstrumentName = property(__InstrumentName.value, __InstrumentName.set, None, 'Friendly name assigned by customer')

    
    # Attribute CreatedBy uses Python identifier CreatedBy
    __CreatedBy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CreatedBy'), 'CreatedBy', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_CreatedBy', pyxb.binding.datatypes.string)
    __CreatedBy._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 369, 4)
    __CreatedBy._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 369, 4)
    
    CreatedBy = property(__CreatedBy.value, __CreatedBy.set, None, 'Who created the run. ')

    
    # Attribute StartedBy uses Python identifier StartedBy
    __StartedBy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'StartedBy'), 'StartedBy', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_StartedBy', pyxb.binding.datatypes.string)
    __StartedBy._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 374, 4)
    __StartedBy._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 374, 4)
    
    StartedBy = property(__StartedBy.value, __StartedBy.set, None, 'Who started the run. Could be different from who created it. ')

    
    # Attribute WhenStarted uses Python identifier WhenStarted
    __WhenStarted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'WhenStarted'), 'WhenStarted', '__httppacificbiosciences_comPacBioDataModel_xsd_RunType_WhenStarted', pyxb.binding.datatypes.dateTime)
    __WhenStarted._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 379, 4)
    __WhenStarted._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 379, 4)
    
    WhenStarted = property(__WhenStarted.value, __WhenStarted.set, None, 'Date and time of when the overall run was started. ')

    _ElementMap.update({
        __SubreadSet.name() : __SubreadSet,
        __Assay.name() : __Assay,
        __RunResources.name() : __RunResources,
        __Inputs.name() : __Inputs,
        __Outputs.name() : __Outputs,
        __RecordedEvents.name() : __RecordedEvents
    })
    _AttributeMap.update({
        __Status.name() : __Status,
        __InstrumentId.name() : __InstrumentId,
        __InstrumentName.name() : __InstrumentName,
        __CreatedBy.name() : __CreatedBy,
        __StartedBy.name() : __StartedBy,
        __WhenStarted.name() : __WhenStarted
    })
Namespace.addCategoryObject('typeBinding', 'RunType', RunType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}BarcodeSetType with content type ELEMENT_ONLY
class BarcodeSetType (DataSetType):
    """Type for the Barcode DataSet."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BarcodeSetType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 28, 1)
    _ElementMap = DataSetType._ElementMap.copy()
    _AttributeMap = DataSetType._AttributeMap.copy()
    # Base type is DataSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDataModel.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadata uses Python identifier DataSetMetadata
    __DataSetMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), 'DataSetMetadata', '__httppacificbiosciences_comPacBioDataModel_xsd_BarcodeSetType_httppacificbiosciences_comPacBioDataModel_xsdDataSetMetadata', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 35, 5), )

    
    DataSetMetadata = property(__DataSetMetadata.value, __DataSetMetadata.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __DataSetMetadata.name() : __DataSetMetadata
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BarcodeSetType', BarcodeSetType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_76 (DataSetType):
    """DataSets of CCS reads (typically in unaligned BAM format)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 54, 2)
    _ElementMap = DataSetType._ElementMap.copy()
    _AttributeMap = DataSetType._AttributeMap.copy()
    # Base type is DataSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDataModel.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}AlignmentSetType with content type ELEMENT_ONLY
class AlignmentSetType (DataSetType):
    """Type for DataSets consisting of aligned subreads and CCS reads."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AlignmentSetType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 60, 1)
    _ElementMap = DataSetType._ElementMap.copy()
    _AttributeMap = DataSetType._AttributeMap.copy()
    # Base type is DataSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDataModel.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadata uses Python identifier DataSetMetadata
    __DataSetMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), 'DataSetMetadata', '__httppacificbiosciences_comPacBioDataModel_xsd_AlignmentSetType_httppacificbiosciences_comPacBioDataModel_xsdDataSetMetadata', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 67, 5), )

    
    DataSetMetadata = property(__DataSetMetadata.value, __DataSetMetadata.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __DataSetMetadata.name() : __DataSetMetadata
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AlignmentSetType', AlignmentSetType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}ContigSetType with content type ELEMENT_ONLY
class ContigSetType (DataSetType):
    """Type for a Contig DataSet."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContigSetType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 92, 1)
    _ElementMap = DataSetType._ElementMap.copy()
    _AttributeMap = DataSetType._AttributeMap.copy()
    # Base type is DataSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDataModel.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadata uses Python identifier DataSetMetadata
    __DataSetMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), 'DataSetMetadata', '__httppacificbiosciences_comPacBioDataModel_xsd_ContigSetType_httppacificbiosciences_comPacBioDataModel_xsdDataSetMetadata', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 99, 5), )

    
    DataSetMetadata = property(__DataSetMetadata.value, __DataSetMetadata.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        __DataSetMetadata.name() : __DataSetMetadata
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ContigSetType', ContigSetType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}IndexedDataType with content type ELEMENT_ONLY
class IndexedDataType (InputOutputDataType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}IndexedDataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IndexedDataType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 217, 1)
    _ElementMap = InputOutputDataType._ElementMap.copy()
    _AttributeMap = InputOutputDataType._AttributeMap.copy()
    # Base type is InputOutputDataType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources uses Python identifier ExternalResources
    __ExternalResources = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources'), 'ExternalResources', '__httppacificbiosciences_comPacBioDataModel_xsd_IndexedDataType_httppacificbiosciences_comPacBioDataModel_xsdExternalResources', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 202, 1), )

    
    ExternalResources = property(__ExternalResources.value, __ExternalResources.set, None, 'Pointers to data that do not reside inside the parent structure')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}FileIndices uses Python identifier FileIndices
    __FileIndices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FileIndices'), 'FileIndices', '__httppacificbiosciences_comPacBioDataModel_xsd_IndexedDataType_httppacificbiosciences_comPacBioDataModel_xsdFileIndices', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 221, 5), )

    
    FileIndices = property(__FileIndices.value, __FileIndices.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    _ElementMap.update({
        __ExternalResources.name() : __ExternalResources,
        __FileIndices.name() : __FileIndices
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'IndexedDataType', IndexedDataType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}SupplyKitBinding with content type ELEMENT_ONLY
class SupplyKitBinding (PartNumberType):
    """A more specific binding kit representation (includes SupplyKit fields). """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplyKitBinding')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 470, 1)
    _ElementMap = PartNumberType._ElementMap.copy()
    _AttributeMap = PartNumberType._AttributeMap.copy()
    # Base type is PartNumberType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element IncompatiblePartNumbers ({http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatiblePartNumbers) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Element IncompatibleAutomations ({http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatibleAutomations) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}Control uses Python identifier Control
    __Control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Control'), 'Control', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitBinding_httppacificbiosciences_comPacBioDataModel_xsdControl', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 477, 5), )

    
    Control = property(__Control.value, __Control.set, None, 'Defines the binding kit internal control name.  Present when used, otherwise not used if not defined. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}IsControlUsed uses Python identifier IsControlUsed
    __IsControlUsed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IsControlUsed'), 'IsControlUsed', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitBinding_httppacificbiosciences_comPacBioDataModel_xsdIsControlUsed', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 482, 5), )

    
    IsControlUsed = property(__IsControlUsed.value, __IsControlUsed.set, None, 'True if the control was used during run, otherwise false. ')

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute PartNumber inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute LotNumber inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute Barcode inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute ExpirationDate inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute IsObsolete inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    _ElementMap.update({
        __Control.name() : __Control,
        __IsControlUsed.name() : __IsControlUsed
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SupplyKitBinding', SupplyKitBinding)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}SupplyKitCellPack with content type ELEMENT_ONLY
class SupplyKitCellPack (PartNumberType):
    """Represents the package of cells. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplyKitCellPack')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 491, 1)
    _ElementMap = PartNumberType._ElementMap.copy()
    _AttributeMap = PartNumberType._AttributeMap.copy()
    # Base type is PartNumberType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element IncompatiblePartNumbers ({http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatiblePartNumbers) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Element IncompatibleAutomations ({http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatibleAutomations) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ChipLayout uses Python identifier ChipLayout
    __ChipLayout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout'), 'ChipLayout', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitCellPack_httppacificbiosciences_comPacBioDataModel_xsdChipLayout', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 498, 5), )

    
    ChipLayout = property(__ChipLayout.value, __ChipLayout.set, None, 'Defines the internal chip layout name, if any. ')

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute PartNumber inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute LotNumber inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute Barcode inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute ExpirationDate inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute IsObsolete inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    _ElementMap.update({
        __ChipLayout.name() : __ChipLayout
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SupplyKitCellPack', SupplyKitCellPack)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}SupplyKitControl with content type ELEMENT_ONLY
class SupplyKitControl (PartNumberType):
    """Represents the DNA control complex. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplyKitControl')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 507, 1)
    _ElementMap = PartNumberType._ElementMap.copy()
    _AttributeMap = PartNumberType._AttributeMap.copy()
    # Base type is PartNumberType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element IncompatiblePartNumbers ({http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatiblePartNumbers) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Element IncompatibleAutomations ({http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatibleAutomations) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}InternalControlName uses Python identifier InternalControlName
    __InternalControlName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InternalControlName'), 'InternalControlName', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitControl_httppacificbiosciences_comPacBioDataModel_xsdInternalControlName', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 514, 5), )

    
    InternalControlName = property(__InternalControlName.value, __InternalControlName.set, None, 'Defines the internal control name, if any. ')

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute PartNumber inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute LotNumber inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute Barcode inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute ExpirationDate inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute IsObsolete inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    _ElementMap.update({
        __InternalControlName.name() : __InternalControlName
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SupplyKitControl', SupplyKitControl)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}SupplyKitTemplate with content type ELEMENT_ONLY
class SupplyKitTemplate (PartNumberType):
    """A more specific template kit representation (includes SupplyKit fields). """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplyKitTemplate')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 523, 1)
    _ElementMap = PartNumberType._ElementMap.copy()
    _AttributeMap = PartNumberType._AttributeMap.copy()
    # Base type is PartNumberType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element IncompatiblePartNumbers ({http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatiblePartNumbers) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Element IncompatibleAutomations ({http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatibleAutomations) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}LeftAdaptorSequence uses Python identifier LeftAdaptorSequence
    __LeftAdaptorSequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LeftAdaptorSequence'), 'LeftAdaptorSequence', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitTemplate_httppacificbiosciences_comPacBioDataModel_xsdLeftAdaptorSequence', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 530, 5), )

    
    LeftAdaptorSequence = property(__LeftAdaptorSequence.value, __LeftAdaptorSequence.set, None, 'Left adapter DNA sequence.')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}LeftPrimerSequence uses Python identifier LeftPrimerSequence
    __LeftPrimerSequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LeftPrimerSequence'), 'LeftPrimerSequence', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitTemplate_httppacificbiosciences_comPacBioDataModel_xsdLeftPrimerSequence', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 535, 5), )

    
    LeftPrimerSequence = property(__LeftPrimerSequence.value, __LeftPrimerSequence.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RightAdaptorSequence uses Python identifier RightAdaptorSequence
    __RightAdaptorSequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RightAdaptorSequence'), 'RightAdaptorSequence', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitTemplate_httppacificbiosciences_comPacBioDataModel_xsdRightAdaptorSequence', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 536, 5), )

    
    RightAdaptorSequence = property(__RightAdaptorSequence.value, __RightAdaptorSequence.set, None, 'Right adapter DNA sequence.  If not specified, a symmetric adapter model is inferred, where the left adapter sequence is used wherever needed.')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}RightPrimerSequence uses Python identifier RightPrimerSequence
    __RightPrimerSequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RightPrimerSequence'), 'RightPrimerSequence', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitTemplate_httppacificbiosciences_comPacBioDataModel_xsdRightPrimerSequence', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 541, 5), )

    
    RightPrimerSequence = property(__RightPrimerSequence.value, __RightPrimerSequence.set, None, 'Right primaer sequence.  If not specified, a symmetric model is inferred, where the left primer sequence is used wherever needed.')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}InsertSize uses Python identifier InsertSize
    __InsertSize = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InsertSize'), 'InsertSize', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitTemplate_httppacificbiosciences_comPacBioDataModel_xsdInsertSize', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 546, 5), )

    
    InsertSize = property(__InsertSize.value, __InsertSize.set, None, 'Approximate size of insert. ')

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute PartNumber inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute LotNumber inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute Barcode inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute ExpirationDate inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute IsObsolete inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    _ElementMap.update({
        __LeftAdaptorSequence.name() : __LeftAdaptorSequence,
        __LeftPrimerSequence.name() : __LeftPrimerSequence,
        __RightAdaptorSequence.name() : __RightAdaptorSequence,
        __RightPrimerSequence.name() : __RightPrimerSequence,
        __InsertSize.name() : __InsertSize
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SupplyKitTemplate', SupplyKitTemplate)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}SubreadSetType with content type ELEMENT_ONLY
class SubreadSetType (ReadSetType):
    """Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}SubreadSetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubreadSetType')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 97, 1)
    _ElementMap = ReadSetType._ElementMap.copy()
    _AttributeMap = ReadSetType._AttributeMap.copy()
    # Base type is ReadSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}ReadSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDataModel.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'SubreadSetType', SubreadSetType)


# Complex type {http://pacificbiosciences.com/PacBioDataModel.xsd}SupplyKitSequencing with content type ELEMENT_ONLY
class SupplyKitSequencing (PartNumberType):
    """A more specific template kit representation (includes SupplyKit fields). """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SupplyKitSequencing')
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 21, 1)
    _ElementMap = PartNumberType._ElementMap.copy()
    _AttributeMap = PartNumberType._AttributeMap.copy()
    # Base type is PartNumberType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element EncodedValue ({http://pacificbiosciences.com/PacBioDataModel.xsd}EncodedValue) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element CheckSum ({http://pacificbiosciences.com/PacBioDataModel.xsd}CheckSum) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Element IncompatiblePartNumbers ({http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatiblePartNumbers) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Element IncompatibleAutomations ({http://pacificbiosciences.com/PacBioDataModel.xsd}IncompatibleAutomations) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentAutomationName uses Python identifier ReagentAutomationName
    __ReagentAutomationName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentAutomationName'), 'ReagentAutomationName', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitSequencing_httppacificbiosciences_comPacBioDataModel_xsdReagentAutomationName', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 28, 5), )

    
    ReagentAutomationName = property(__ReagentAutomationName.value, __ReagentAutomationName.set, None, 'The reagent-mixing protocol used. ')

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}ReagentTubes uses Python identifier ReagentTubes
    __ReagentTubes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReagentTubes'), 'ReagentTubes', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitSequencing_httppacificbiosciences_comPacBioDataModel_xsdReagentTubes', True, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 33, 5), )

    
    ReagentTubes = property(__ReagentTubes.value, __ReagentTubes.set, None, "Tubes associated with the reagent kit - can have up to two; don't forget to set the location, 0 or 1")

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SequencingChemistry uses Python identifier SequencingChemistry
    __SequencingChemistry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingChemistry'), 'SequencingChemistry', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitSequencing_httppacificbiosciences_comPacBioDataModel_xsdSequencingChemistry', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 38, 5), )

    
    SequencingChemistry = property(__SequencingChemistry.value, __SequencingChemistry.set, None, None)

    
    # Element {http://pacificbiosciences.com/PacBioDataModel.xsd}SequencingKitDefinition uses Python identifier SequencingKitDefinition
    __SequencingKitDefinition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitDefinition'), 'SequencingKitDefinition', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitSequencing_httppacificbiosciences_comPacBioDataModel_xsdSequencingKitDefinition', False, pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 39, 5), )

    
    SequencingKitDefinition = property(__SequencingKitDefinition.value, __SequencingKitDefinition.set, None, None)

    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ValueDataType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute SimpleValue inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataEntityType
    
    # Attribute PartNumber inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute LotNumber inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute Barcode inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute ExpirationDate inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute IsObsolete inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}PartNumberType
    
    # Attribute Location uses Python identifier Location
    __Location = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Location'), 'Location', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitSequencing_Location', pyxb.binding.datatypes.int, unicode_default='0')
    __Location._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 41, 4)
    __Location._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 41, 4)
    
    Location = property(__Location.value, __Location.set, None, 'The location of the supply kit - for a reagent plate, it could be 0 or 1, and for a tube it could be 0 or 1')

    
    # Attribute MaxCollections uses Python identifier MaxCollections
    __MaxCollections = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MaxCollections'), 'MaxCollections', '__httppacificbiosciences_comPacBioDataModel_xsd_SupplyKitSequencing_MaxCollections', pyxb.binding.datatypes.int, unicode_default='8')
    __MaxCollections._DeclarationLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 46, 4)
    __MaxCollections._UseLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 46, 4)
    
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_77 (AlignmentSetType):
    """DataSets for aligned subreads and CCS reads."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 12, 2)
    _ElementMap = AlignmentSetType._ElementMap.copy()
    _AttributeMap = AlignmentSetType._AttributeMap.copy()
    # Base type is AlignmentSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDataModel.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AlignmentSetType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_78 (BarcodeSetType):
    """DataSets of Barcodes. Basically a thin metadata layer on top of the barcode FASTA."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 22, 2)
    _ElementMap = BarcodeSetType._ElementMap.copy()
    _AttributeMap = BarcodeSetType._AttributeMap.copy()
    # Base type is BarcodeSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDataModel.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BarcodeSetType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_79 (AlignmentSetType):
    """DataSets of aligned CCS reads."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 44, 2)
    _ElementMap = AlignmentSetType._ElementMap.copy()
    _AttributeMap = AlignmentSetType._AttributeMap.copy()
    # Base type is AlignmentSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDataModel.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}AlignmentSetType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_80 (ContigSetType):
    """DataSets of reference sequences. Replaces the reference.info.xml"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 76, 2)
    _ElementMap = ContigSetType._ElementMap.copy()
    _AttributeMap = ContigSetType._AttributeMap.copy()
    # Base type is ContigSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDataModel.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}ContigSetType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_81 (ContigSetType):
    """DataSets of contigs sequences. Basically a thin metadata layer on top of a contigs FASTA (e.g. from HGAP)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 86, 2)
    _ElementMap = ContigSetType._ElementMap.copy()
    _AttributeMap = ContigSetType._AttributeMap.copy()
    # Base type is ContigSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDataModel.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}ContigSetType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_82 (ReadSetType):
    """DataSets of subreads in bax.h5 or bas.h5 format."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 108, 2)
    _ElementMap = ReadSetType._ElementMap.copy()
    _AttributeMap = ReadSetType._AttributeMap.copy()
    # Base type is ReadSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}ReadSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDataModel.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_83 (SubreadSetType):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 682, 2)
    _ElementMap = SubreadSetType._ElementMap.copy()
    _AttributeMap = SubreadSetType._AttributeMap.copy()
    # Base type is SubreadSetType
    
    # Element Extensions ({http://pacificbiosciences.com/PacBioDataModel.xsd}Extensions) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Element ExternalResources ({http://pacificbiosciences.com/PacBioDataModel.xsd}ExternalResources) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSetMetadata ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetMetadata) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}ReadSetType
    
    # Element Filters ({http://pacificbiosciences.com/PacBioDataModel.xsd}Filters) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Element DataSets ({http://pacificbiosciences.com/PacBioDataModel.xsd}DataSets) inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}DataSetType
    
    # Attribute UniqueId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Name inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute TimeStampedName inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Description inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute MetaType inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Tags inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ResourceId inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Format inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute Version inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute CreatedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    
    # Attribute ModifiedAt inherited from {http://pacificbiosciences.com/PacBioDataModel.xsd}BaseEntityType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })



ExtensionElement = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionElement'), pyxb.binding.datatypes.anyType, documentation='A generic element whose contents are undefined at the schema level.  This is used to extend the data model.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 640, 1))
Namespace.addCategoryObject('elementBinding', ExtensionElement.name().localName(), ExtensionElement)

PacBioAutomationConstraints = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PacBioAutomationConstraints'), CTD_ANON, documentation='The root element of the Automation Constraints ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 9, 1))
Namespace.addCategoryObject('elementBinding', PacBioAutomationConstraints.name().localName(), PacBioAutomationConstraints)

AutomationConstraints = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationConstraints'), CTD_ANON_, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 19, 1))
Namespace.addCategoryObject('elementBinding', AutomationConstraints.name().localName(), AutomationConstraints)

DataPointers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataPointers'), CTD_ANON_5, documentation='Pointer to Run/Outputs/Output/@UniqueId', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 168, 1))
Namespace.addCategoryObject('elementBinding', DataPointers.name().localName(), DataPointers)

ExternalResources = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources'), CTD_ANON_6, documentation='Pointers to data that do not reside inside the parent structure', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 202, 1))
Namespace.addCategoryObject('elementBinding', ExternalResources.name().localName(), ExternalResources)

PacBioSequencingChemistry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PacBioSequencingChemistry'), CTD_ANON_12, documentation='Root element for document containing the container of analog set, SequencingChemistryConfig', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 362, 1))
Namespace.addCategoryObject('elementBinding', PacBioSequencingChemistry.name().localName(), PacBioSequencingChemistry)

ValueDataType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValueDataType'), SupportedDataTypes, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 638, 1))
Namespace.addCategoryObject('elementBinding', ValueDataType.name().localName(), ValueDataType)

PacBioCollectionMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PacBioCollectionMetadata'), CTD_ANON_20, documentation='Root element of a standalone CollectionMetadata file.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 9, 1))
Namespace.addCategoryObject('elementBinding', PacBioCollectionMetadata.name().localName(), PacBioCollectionMetadata)

Collections = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Collections'), CTD_ANON_24, documentation='A set of acquisition definitions', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 125, 1))
Namespace.addCategoryObject('elementBinding', Collections.name().localName(), Collections)

RunDetails = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RunDetails'), CTD_ANON_25, documentation='Information related to an instrument run.  A run can contain multiple chips, wells, and movies. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 248, 1))
Namespace.addCategoryObject('elementBinding', RunDetails.name().localName(), RunDetails)

Movie = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Movie'), CTD_ANON_26, documentation='A movie corresponds to one acquisition for a chip, one set (look) and one strobe. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 287, 1))
Namespace.addCategoryObject('elementBinding', Movie.name().localName(), Movie)

ExpirationData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExpirationData'), CTD_ANON_27, documentation='Container for the expired consumable data. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 311, 1))
Namespace.addCategoryObject('elementBinding', ExpirationData.name().localName(), ExpirationData)

Primary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Primary'), CTD_ANON_29, documentation='Container for the primary analysis related data. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 503, 1))
Namespace.addCategoryObject('elementBinding', Primary.name().localName(), Primary)

Secondary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Secondary'), CTD_ANON_32, documentation='Container for the primary analysis related data. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 568, 1))
Namespace.addCategoryObject('elementBinding', Secondary.name().localName(), Secondary)

UserDefinedFields = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UserDefinedFields'), UserDefinedFieldsType, documentation='A set of key-value pairs specified by a user via the run input mechanism. Note that uniqueness of keys is not enforced here and so may contain duplicate keys. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 602, 1))
Namespace.addCategoryObject('elementBinding', UserDefinedFields.name().localName(), UserDefinedFields)

KeyValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KeyValue'), CTD_ANON_34, documentation='One custom, possibly non-unique, key-value pair. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 607, 1))
Namespace.addCategoryObject('elementBinding', KeyValue.name().localName(), KeyValue)

BioSamplePointers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSamplePointers'), CTD_ANON_35, documentation='Back references to other BarcodedSampleType object UniqueIds which utilize this sample', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 639, 1))
Namespace.addCategoryObject('elementBinding', BioSamplePointers.name().localName(), BioSamplePointers)

BarcodedSamplePointers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointers'), CTD_ANON_36, documentation='Back references to other BarcodedSampleType object UniqueIds which utilize this sample', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 659, 1))
Namespace.addCategoryObject('elementBinding', BarcodedSamplePointers.name().localName(), BarcodedSamplePointers)

BioSamples = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSamples'), CTD_ANON_37, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 673, 1))
Namespace.addCategoryObject('elementBinding', BioSamples.name().localName(), BioSamples)

ChipLayout = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout'), CTD_ANON_38, documentation='Part of the RunResources; specifies a ChipLayout which is compatible with the collection protocols defined on the plate', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 12, 1))
Namespace.addCategoryObject('elementBinding', ChipLayout.name().localName(), ChipLayout)

CompatibleChipLayouts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompatibleChipLayouts'), CTD_ANON_39, documentation='A set of Chip Layouts deemed compatible with the current plate', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 24, 1))
Namespace.addCategoryObject('elementBinding', CompatibleChipLayouts.name().localName(), CompatibleChipLayouts)

CompatibleSequencingKits = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompatibleSequencingKits'), CTD_ANON_40, documentation='A set of reagent kits deemed compatible with the current plate', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 36, 1))
Namespace.addCategoryObject('elementBinding', CompatibleSequencingKits.name().localName(), CompatibleSequencingKits)

EstimatedTotalRunTime = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EstimatedTotalRunTime'), CTD_ANON_41, documentation='The total amount of time the run is estimated to require.  A confidence value (defaulted to 90%) indicates the degree of certainty associated with the estimate', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 48, 1))
Namespace.addCategoryObject('elementBinding', EstimatedTotalRunTime.name().localName(), EstimatedTotalRunTime)

PacBioDataModel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PacBioDataModel'), CTD_ANON_42, documentation='PacBio Data Model root element', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 91, 1))
Namespace.addCategoryObject('elementBinding', PacBioDataModel.name().localName(), PacBioDataModel)

RequiredSMRTCells = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequiredSMRTCells'), CTD_ANON_43, documentation='Part of the RunResources; specifies the required number of SMRT cells', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 106, 1))
Namespace.addCategoryObject('elementBinding', RequiredSMRTCells.name().localName(), RequiredSMRTCells)

RequiredTips = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequiredTips'), CTD_ANON_44, documentation='Part of the RunResources; specifies the required number of tips via two attributes, Left and Right', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 117, 1))
Namespace.addCategoryObject('elementBinding', RequiredTips.name().localName(), RequiredTips)

RunResources = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RunResources'), CTD_ANON_45, documentation='This is an output field specifying the requirements for the run, e.g. number of tips, estimated run time, etc.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 129, 1))
Namespace.addCategoryObject('elementBinding', RunResources.name().localName(), RunResources)

SampleComment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleComment'), CTD_ANON_46, documentation='A general sample description', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 141, 1))
Namespace.addCategoryObject('elementBinding', SampleComment.name().localName(), SampleComment)

CollectionReferences = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionReferences'), CTD_ANON_54, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 387, 1))
Namespace.addCategoryObject('elementBinding', CollectionReferences.name().localName(), CollectionReferences)

PacBioPartNumbers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PacBioPartNumbers'), CTD_ANON_55, documentation='The root element of the Part Numbers ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 8, 1))
Namespace.addCategoryObject('elementBinding', PacBioPartNumbers.name().localName(), PacBioPartNumbers)

PacBioReagentKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PacBioReagentKit'), CTD_ANON_61, documentation='The root element of the reagent kit standalone file', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', PacBioReagentKit.name().localName(), PacBioReagentKit)

Parameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Parameter'), CTD_ANON_67, documentation='A variable, as a name/value pair, associated with a protocol (one of Collection, Primary, and Secondary)', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 63, 1))
Namespace.addCategoryObject('elementBinding', Parameter.name().localName(), Parameter)

Validation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_68, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1))
Namespace.addCategoryObject('elementBinding', Validation.name().localName(), Validation)

AutomationConstraint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationConstraint'), AutomationConstraintType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 26, 1))
Namespace.addCategoryObject('elementBinding', AutomationConstraint.name().localName(), AutomationConstraint)

DataEntity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataEntity'), DataEntityType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 136, 1))
Namespace.addCategoryObject('elementBinding', DataEntity.name().localName(), DataEntity)

AutomationParameter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter'), DataEntityType, documentation='One or more collection parameters, such as MovieLength, InsertSize, UseStageStart, IsControl, etc..', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 253, 1))
Namespace.addCategoryObject('elementBinding', AutomationParameter.name().localName(), AutomationParameter)

DataSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSet'), DataSetType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 135, 1))
Namespace.addCategoryObject('elementBinding', DataSet.name().localName(), DataSet)

CollectionMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata'), CTD_ANON_70, documentation='Root-level element for the metadata.  The purpose of which is to contain pertinent instrument information related to the conditions present during a movie acquisition.  It also serves to provide key pieces of information for integration with primary and secondary analysis.  This file is associated with 1 movie. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 136, 1))
Namespace.addCategoryObject('elementBinding', CollectionMetadata.name().localName(), CollectionMetadata)

WellSample = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WellSample'), CTD_ANON_71, documentation='Container for the sample related data. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 432, 1))
Namespace.addCategoryObject('elementBinding', WellSample.name().localName(), WellSample)

BioSample = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSample'), BioSampleType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 680, 1))
Namespace.addCategoryObject('elementBinding', BioSample.name().localName(), BioSample)

Reagent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reagent'), ReagentType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 17, 1))
Namespace.addCategoryObject('elementBinding', Reagent.name().localName(), Reagent)

ReagentKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentKit'), ReagentKitType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 18, 1))
Namespace.addCategoryObject('elementBinding', ReagentKit.name().localName(), ReagentKit)

ReagentTube = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube'), ReagentTubeType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 19, 1))
Namespace.addCategoryObject('elementBinding', ReagentTube.name().localName(), ReagentTube)

ReagentPlateRow = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRow'), ReagentPlateRowType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 20, 1))
Namespace.addCategoryObject('elementBinding', ReagentPlateRow.name().localName(), ReagentPlateRow)

Contigs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contigs'), CTD_ANON_72, documentation='List of contigs in a ContigSet', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 114, 1))
Namespace.addCategoryObject('elementBinding', Contigs.name().localName(), Contigs)

ConfigSetAnalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConfigSetAnalog'), CTD_ANON_74, documentation='An unlimited number of analogs listed for the purposes of hosting in a configuration file. e.g. a list of all possible analogs on the system', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 126, 1))
Namespace.addCategoryObject('elementBinding', ConfigSetAnalog.name().localName(), ConfigSetAnalog)

DyeSetAnalog = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DyeSetAnalog'), CTD_ANON_75, documentation='A set of four analogs, one for each of the nucleotides, grouped together for the purposes of a single experiment.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 192, 1))
Namespace.addCategoryObject('elementBinding', DyeSetAnalog.name().localName(), DyeSetAnalog)

Assay = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Assay'), AssayType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 11, 1))
Namespace.addCategoryObject('elementBinding', Assay.name().localName(), Assay)

Events = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Events'), RecordedEventType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 60, 1))
Namespace.addCategoryObject('elementBinding', Events.name().localName(), Events)

Input = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Input'), InputOutputDataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 61, 1))
Namespace.addCategoryObject('elementBinding', Input.name().localName(), Input)

Output = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Output'), InputOutputDataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 62, 1))
Namespace.addCategoryObject('elementBinding', Output.name().localName(), Output)

ConsensusReadSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsensusReadSet'), CTD_ANON_76, documentation='DataSets of CCS reads (typically in unaligned BAM format).', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 50, 1))
Namespace.addCategoryObject('elementBinding', ConsensusReadSet.name().localName(), ConsensusReadSet)

ExternalResource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalResource'), IndexedDataType, documentation='for example, an output file could be the BAM file, which could be associated with multiple indices into it.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 662, 1))
Namespace.addCategoryObject('elementBinding', ExternalResource.name().localName(), ExternalResource)

SequencingKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit'), SupplyKitSequencing, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 67, 1))
Namespace.addCategoryObject('elementBinding', SequencingKit.name().localName(), SequencingKit)

BindingKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BindingKit'), SupplyKitBinding, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 68, 1))
Namespace.addCategoryObject('elementBinding', BindingKit.name().localName(), BindingKit)

TemplatePrepKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit'), SupplyKitTemplate, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 69, 1))
Namespace.addCategoryObject('elementBinding', TemplatePrepKit.name().localName(), TemplatePrepKit)

ControlKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlKit'), SupplyKitControl, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 70, 1))
Namespace.addCategoryObject('elementBinding', ControlKit.name().localName(), ControlKit)

CellPackKit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellPackKit'), SupplyKitCellPack, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 71, 1))
Namespace.addCategoryObject('elementBinding', CellPackKit.name().localName(), CellPackKit)

AlignmentSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AlignmentSet'), CTD_ANON_77, documentation='DataSets for aligned subreads and CCS reads.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 8, 1))
Namespace.addCategoryObject('elementBinding', AlignmentSet.name().localName(), AlignmentSet)

BarcodeSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BarcodeSet'), CTD_ANON_78, documentation='DataSets of Barcodes. Basically a thin metadata layer on top of the barcode FASTA.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 18, 1))
Namespace.addCategoryObject('elementBinding', BarcodeSet.name().localName(), BarcodeSet)

ConsensusAlignmentSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConsensusAlignmentSet'), CTD_ANON_79, documentation='DataSets of aligned CCS reads.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 40, 1))
Namespace.addCategoryObject('elementBinding', ConsensusAlignmentSet.name().localName(), ConsensusAlignmentSet)

ReferenceSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReferenceSet'), CTD_ANON_80, documentation='DataSets of reference sequences. Replaces the reference.info.xml', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 72, 1))
Namespace.addCategoryObject('elementBinding', ReferenceSet.name().localName(), ReferenceSet)

ContigSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ContigSet'), CTD_ANON_81, documentation='DataSets of contigs sequences. Basically a thin metadata layer on top of a contigs FASTA (e.g. from HGAP).', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 82, 1))
Namespace.addCategoryObject('elementBinding', ContigSet.name().localName(), ContigSet)

HdfSubreadSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HdfSubreadSet'), CTD_ANON_82, documentation='DataSets of subreads in bax.h5 or bas.h5 format.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 104, 1))
Namespace.addCategoryObject('elementBinding', HdfSubreadSet.name().localName(), HdfSubreadSet)

SubreadSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubreadSet'), CTD_ANON_83, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 681, 1))
Namespace.addCategoryObject('elementBinding', SubreadSet.name().localName(), SubreadSet)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationConstraints'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 19, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationConstraints')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 15, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationConstraint'), AutomationConstraintType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 26, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationConstraint')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 22, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Automation'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 40, 8)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Automation')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 40, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InsertSize'), pyxb.binding.datatypes.int, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 50, 8)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InsertSize')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 50, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExtensionElement'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_4, documentation='A generic element whose contents are undefined at the schema level.  This is used to extend the data model.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 640, 1)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 60, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExtensionElement')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 60, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataPointer'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 174, 4)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 174, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataPointer')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 174, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_5()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalResource'), IndexedDataType, scope=CTD_ANON_6, documentation='for example, an output file could be the BAM file, which could be associated with multiple indices into it.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 662, 1)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResource')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 208, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_6()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FileIndex'), InputOutputDataType, scope=CTD_ANON_7, documentation='e.g. index for output files, allowing one to find information in the output file', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 224, 8)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FileIndex')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 224, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter'), DataEntityType, scope=CTD_ANON_8, documentation='One or more collection parameters, such as MovieLength, InsertSize, UseStageStart, IsControl, etc..', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 253, 1)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 244, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePartNumber'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_9, documentation='A reference to the incompatible part number UID', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 273, 8)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePartNumber')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 273, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleAutomation'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_10, documentation='A reference to the incompatible automation type UID', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 287, 8)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleAutomation')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 287, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_10()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Analog'), AnalogType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 349, 13)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=4, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 349, 13))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Analog')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 349, 13))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_11()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChemistryConfig'), SequencingChemistryConfig, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 368, 4)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChemistryConfig')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 368, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_12()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Analog'), AnalogType, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 382, 8)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=4, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 382, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Analog')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 382, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_13()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinCount'), pyxb.binding.datatypes.int, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 406, 8)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinCount')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 406, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_14()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinCount'), pyxb.binding.datatypes.int, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 432, 8)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinCount')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 432, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_15()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinLabel'), pyxb.binding.datatypes.string, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 440, 8)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinLabel')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 440, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_16()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Val'), pyxb.binding.datatypes.float, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 462, 8)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 462, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Val')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 462, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_17()




UserDefinedFieldsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataEntities'), DataEntityType, scope=UserDefinedFieldsType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 635, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UserDefinedFieldsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataEntities')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 635, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UserDefinedFieldsType._Automaton = _BuildAutomaton_18()




FilterType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Properties'), CTD_ANON_18, scope=FilterType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 647, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Properties')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 647, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FilterType._Automaton = _BuildAutomaton_19()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Property'), CTD_ANON_19, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 650, 6)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Property')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 650, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_20()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata'), CTD_ANON_70, scope=CTD_ANON_20, documentation='Root-level element for the metadata.  The purpose of which is to contain pertinent instrument information related to the conditions present during a movie acquisition.  It also serves to provide key pieces of information for integration with primary and secondary analysis.  This file is associated with 1 movie. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 136, 1)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 15, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_21()




DataSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TotalLength'), pyxb.binding.datatypes.int, scope=DataSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 36, 3)))

DataSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumRecords'), pyxb.binding.datatypes.int, scope=DataSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 37, 3)))

DataSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Provenance'), CTD_ANON_66, scope=DataSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DataSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TotalLength')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 36, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumRecords')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 37, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DataSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Provenance')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3))
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
DataSetMetadataType._Automaton = _BuildAutomaton_22()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdapterDimerFraction'), pyxb.binding.datatypes.float, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 68, 8)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShortInsertFraction'), pyxb.binding.datatypes.float, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 69, 8)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumSequencingZmws'), pyxb.binding.datatypes.int, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 70, 8)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ProdDist'), StatsDiscreteDistType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 71, 8)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReadTypeDist'), StatsDiscreteDistType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 72, 8)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReadLenDist'), StatsContinuousDistType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 73, 8)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReadQualDist'), StatsContinuousDistType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 74, 8)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlReadLenDist'), StatsContinuousDistType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 75, 8)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlReadQualDist'), StatsContinuousDistType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 76, 8)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MedianInsertDist'), StatsContinuousDistType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 77, 8)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InsertReadLenDist'), StatsContinuousDistType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 78, 8)))

CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InsertReadQualDist'), StatsContinuousDistType, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 79, 8)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdapterDimerFraction')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 68, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ShortInsertFraction')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 69, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumSequencingZmws')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 70, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ProdDist')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 71, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReadTypeDist')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 72, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReadLenDist')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 73, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReadQualDist')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 74, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlReadLenDist')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 75, 8))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlReadQualDist')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 76, 8))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MedianInsertDist')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 77, 8))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InsertReadLenDist')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 78, 8))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InsertReadQualDist')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 79, 8))
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
CTD_ANON_21._Automaton = _BuildAutomaton_23()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Filter'), FilterType, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 110, 8)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filter')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 110, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_24()




CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSet'), DataSetType, scope=CTD_ANON_23, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 135, 1)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 117, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSet')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 117, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_25()




CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata'), CTD_ANON_70, scope=CTD_ANON_24, documentation='Root-level element for the metadata.  The purpose of which is to contain pertinent instrument information related to the conditions present during a movie acquisition.  It also serves to provide key pieces of information for integration with primary and secondary analysis.  This file is associated with 1 movie. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 136, 1)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 131, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_26()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RunId'), pyxb.binding.datatypes.string, scope=CTD_ANON_25, documentation='A unique identifier for this run.  Format is r[sid]_[iname]_[ts]. Where [id] is a system generated id and [iname] is the instrument name and [ts] is a timestamp YYMMDD Example:  r000123_00117_100713 ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 254, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Name'), pyxb.binding.datatypes.string, scope=CTD_ANON_25, documentation='Assigned name for a run, which consists of multiple wells. There is no constraint on the uniqueness of this data. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 259, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CreatedBy'), pyxb.binding.datatypes.string, scope=CTD_ANON_25, documentation='Who created the run. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 264, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WhenCreated'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_25, documentation='Date and time of when the overall run was created in the system. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 269, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartedBy'), pyxb.binding.datatypes.string, scope=CTD_ANON_25, documentation='Who started the run. Could be different from who created it. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 274, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WhenStarted'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_25, documentation='Date and time of when the overall run was started. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 279, 4)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 259, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 264, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 269, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 274, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 279, 4))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RunId')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 254, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Name')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 259, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CreatedBy')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 264, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WhenCreated')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 269, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartedBy')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 274, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WhenStarted')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 279, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_27()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WhenStarted'), pyxb.binding.datatypes.dateTime, scope=CTD_ANON_26, documentation='Date and time of when this movie acquisition started. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 293, 4)))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DurationInSec'), pyxb.binding.datatypes.int, scope=CTD_ANON_26, documentation='The actual length of the movie acquisition (in seconds), irrespective of the movie duration specified by an automation parameter. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 298, 4), unicode_default='0'))

CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Number'), pyxb.binding.datatypes.int, scope=CTD_ANON_26, documentation="The number of this movie within the set (i.e., look).  This is unique when combined with the 'SetNumber'. ", location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 303, 4), unicode_default='0'))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WhenStarted')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 293, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DurationInSec')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 298, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Number')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 303, 4))
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
CTD_ANON_26._Automaton = _BuildAutomaton_28()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EightPacPastExpiration'), pyxb.binding.datatypes.int, scope=CTD_ANON_27, documentation='Number of days past expiration the eight pac was (if at all). ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 317, 4)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentKitPastExpiration'), pyxb.binding.datatypes.int, scope=CTD_ANON_27, documentation='Number of days past expiration the reagent kit was (if at all). ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 322, 4)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube0PastExpiration'), pyxb.binding.datatypes.int, scope=CTD_ANON_27, documentation='Number of days past expiration the reagent tube 0 was (if at all). ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 327, 4)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube1PastExpiration'), pyxb.binding.datatypes.int, scope=CTD_ANON_27, documentation='Number of days past expiration the reagent tube 1 was (if at all). ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 332, 4)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EightPacPastExpiration')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 317, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentKitPastExpiration')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 322, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube0PastExpiration')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 327, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube1PastExpiration')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 332, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_29()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Barcode'), DNABarcode, scope=CTD_ANON_28, documentation='A sequence of barcodes associated with the biological sample', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 353, 8)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 353, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Barcode')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 353, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_30()




CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleTrace'), CTD_ANON_30, scope=CTD_ANON_29, documentation='Tag to indicate that the trace file will be sampled. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 509, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationName'), pyxb.binding.datatypes.string, scope=CTD_ANON_29, documentation='Name of primary analysis protocol. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 528, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConfigFileName'), pyxb.binding.datatypes.string, scope=CTD_ANON_29, documentation='Name of primary analysis config file. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 533, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingCondition'), pyxb.binding.datatypes.string, scope=CTD_ANON_29, documentation='A sequencing condition tag to be used by primary analysis, e.g., to select basecaller calibration or training parameters. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 538, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResultsFolder'), pyxb.binding.datatypes.string, scope=CTD_ANON_29, documentation="NOTE: not for customers. A sub-folder under the CollectionPath created by Primary Analysis. This is a field that will be updated by the primary analysis pipeline.  The default (as created by homer) should be set to 'Reports_Sms' for now.  Consumers of the data should be aware that they will find collection metadata (and trace files if acquisition is so-configured) at the CollectionPathUri, and all primary analysis results in the sub-folder PrimaryResultsFolder. ", location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 543, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionPathUri'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON_29, documentation='User-specified location of where the results should be copied after an analysis has been completed. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 548, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CopyFiles'), CTD_ANON_31, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 553, 4)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 509, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SampleTrace')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 509, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationName')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 528, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ConfigFileName')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 533, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingCondition')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 538, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResultsFolder')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 543, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollectionPathUri')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 548, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CopyFiles')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 553, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_29._Automaton = _BuildAutomaton_31()




CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TraceSamplingFactor'), pyxb.binding.datatypes.float, scope=CTD_ANON_30, documentation='Percentage of traces to sample. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 515, 7)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FullPulseFile'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_30, documentation='Whether full or sampled pulse file is transferred if requested. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 520, 7)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TraceSamplingFactor')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 515, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FullPulseFile')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 520, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_32()




CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionFileCopy'), PapOutputFile, scope=CTD_ANON_31, documentation='Defines the set of files to be copied to the CollectionPathUri. 1 or more. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 556, 7)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollectionFileCopy')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 556, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_31._Automaton = _BuildAutomaton_33()




CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationName'), pyxb.binding.datatypes.string, scope=CTD_ANON_32, documentation='The secondary analysis protocol name specified in the sample sheet. Ignored by secondary. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 574, 4)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameters'), CTD_ANON_33, scope=CTD_ANON_32, documentation='The parameters for secondary analysis specified in the sample sheet. Ignored by secondary. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 579, 4)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellCountInJob'), pyxb.binding.datatypes.int, scope=CTD_ANON_32, documentation="The number of cells in this secondary analysis job, identified by the secondary analysis parameter 'JobName'.  Supports automated secondary analysis. ", location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 593, 4)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 579, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationName')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 574, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 579, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellCountInJob')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 593, 4))
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
CTD_ANON_32._Automaton = _BuildAutomaton_34()




CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter'), DataEntityType, scope=CTD_ANON_33, documentation='One or more secondary analysis parameters, such as JobName, Workflow, etc..', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 585, 7)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 585, 7))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameter')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 585, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_33._Automaton = _BuildAutomaton_35()




CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSamplePointer'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_35, documentation='Pointer to a single biological sample', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 650, 5)))

CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointers'), CTD_ANON_36, scope=CTD_ANON_35, documentation='Back references to other BarcodedSampleType object UniqueIds which utilize this sample', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 659, 1)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointers')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 649, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BioSamplePointer')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 650, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_35._Automaton = _BuildAutomaton_36()




CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointer'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_36, documentation='Pointer to a group of barcoded samples', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 665, 4)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BarcodedSamplePointer')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 665, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_36._Automaton = _BuildAutomaton_37()




CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSample'), BioSampleType, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 680, 1)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 676, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BioSample')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 676, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_37._Automaton = _BuildAutomaton_38()




CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_68, scope=CTD_ANON_38, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 18, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 18, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_38._Automaton = _BuildAutomaton_39()




CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout'), CTD_ANON_38, scope=CTD_ANON_39, documentation='Part of the RunResources; specifies a ChipLayout which is compatible with the collection protocols defined on the plate', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 12, 1)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequiredSMRTCells'), CTD_ANON_43, scope=CTD_ANON_39, documentation='Part of the RunResources; specifies the required number of SMRT cells', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 106, 1)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_68, scope=CTD_ANON_39, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 32, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 30, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RequiredSMRTCells')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 31, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 32, 4))
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
CTD_ANON_39._Automaton = _BuildAutomaton_40()




CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EstimatedTotalRunTime'), CTD_ANON_41, scope=CTD_ANON_40, documentation='The total amount of time the run is estimated to require.  A confidence value (defaulted to 90%) indicates the degree of certainty associated with the estimate', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 48, 1)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RequiredTips'), CTD_ANON_44, scope=CTD_ANON_40, documentation='Part of the RunResources; specifies the required number of tips via two attributes, Left and Right', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 117, 1)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit'), SupplyKitSequencing, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 67, 1)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 42, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RequiredTips')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 43, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EstimatedTotalRunTime')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 44, 4))
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
CTD_ANON_40._Automaton = _BuildAutomaton_41()




CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_68, scope=CTD_ANON_41, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 54, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 54, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_41._Automaton = _BuildAutomaton_42()




CTD_ANON_42._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExperimentContainer'), ExperimentContainerType, scope=CTD_ANON_42, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 97, 4)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 98, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_42._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExperimentContainer')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 97, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 98, 4))
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
CTD_ANON_42._Automaton = _BuildAutomaton_43()




CTD_ANON_43._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_68, scope=CTD_ANON_43, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 112, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_43._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 112, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_43._Automaton = _BuildAutomaton_44()




CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_68, scope=CTD_ANON_44, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 123, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 123, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_44._Automaton = _BuildAutomaton_45()




CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompatibleChipLayouts'), CTD_ANON_39, scope=CTD_ANON_45, documentation='A set of Chip Layouts deemed compatible with the current plate', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 24, 1)))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompatibleSequencingKits'), CTD_ANON_40, scope=CTD_ANON_45, documentation='A set of reagent kits deemed compatible with the current plate', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 36, 1)))

CTD_ANON_45._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_68, scope=CTD_ANON_45, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 137, 4))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CompatibleSequencingKits')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 135, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CompatibleChipLayouts')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 136, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_45._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 137, 4))
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
CTD_ANON_45._Automaton = _BuildAutomaton_46()




CTD_ANON_46._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_68, scope=CTD_ANON_46, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 147, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_46._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 147, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_46._Automaton = _BuildAutomaton_47()




CTD_ANON_47._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Run'), RunType, scope=CTD_ANON_47, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 273, 8)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_47._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Run')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 273, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_47._Automaton = _BuildAutomaton_48()




CTD_ANON_48._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSet'), DataSetType, scope=CTD_ANON_48, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 135, 1)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 283, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_48._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSet')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 283, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_48._Automaton = _BuildAutomaton_49()




CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvent'), RecordedEventType, scope=CTD_ANON_49, documentation="Journal of metrics, system events, or alarms that were generated during this container's lifetime", location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 293, 8)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 293, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvent')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 293, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_49._Automaton = _BuildAutomaton_50()




CTD_ANON_50._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSample'), BioSampleType, scope=CTD_ANON_50, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 304, 8)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 304, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_50._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BioSample')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 304, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_50._Automaton = _BuildAutomaton_51()




CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Input'), InputOutputDataType, scope=CTD_ANON_51, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 61, 1)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Input')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 324, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_51._Automaton = _BuildAutomaton_52()




CTD_ANON_52._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Output'), InputOutputDataType, scope=CTD_ANON_52, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 62, 1)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_52._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Output')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 331, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_52._Automaton = _BuildAutomaton_53()




CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvent'), RecordedEventType, scope=CTD_ANON_53, documentation="Journal of metrics, system events, or alarms that were generated during this run's lifetime.\nIn the case of Primary generating the DataSet containing the sts.xml, this RecordedEvent object should be a pointer to the DataSet object generated.", location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 347, 8)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 347, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvent')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 347, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_53._Automaton = _BuildAutomaton_54()




CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadataRef'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_54, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 390, 4)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollectionMetadataRef')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 390, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_54._Automaton = _BuildAutomaton_55()




CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKits'), CTD_ANON_56, scope=CTD_ANON_55, documentation='List the sequencing kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 14, 4)))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BindingKits'), CTD_ANON_57, scope=CTD_ANON_55, documentation='List the binding kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 24, 4)))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKits'), CTD_ANON_58, scope=CTD_ANON_55, documentation='List the sample prep kit part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 34, 4)))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlKits'), CTD_ANON_59, scope=CTD_ANON_55, documentation='List the DNA control complex part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 44, 4)))

CTD_ANON_55._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellPackKits'), CTD_ANON_60, scope=CTD_ANON_55, documentation='List the cell tray part numbers.  A list of incompatible part numbers and automations is available to specify in the PartNumber subtype.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 54, 4)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 14, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 24, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 34, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 44, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 54, 4))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingKits')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 14, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BindingKits')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 24, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKits')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 34, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlKits')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 44, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_55._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellPackKits')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 54, 4))
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
CTD_ANON_55._Automaton = _BuildAutomaton_56()




CTD_ANON_56._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit'), SupplyKitSequencing, scope=CTD_ANON_56, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 67, 1)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_56._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingKit')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 20, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_56._Automaton = _BuildAutomaton_57()




CTD_ANON_57._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BindingKit'), SupplyKitBinding, scope=CTD_ANON_57, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 68, 1)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_57._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BindingKit')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 30, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_57._Automaton = _BuildAutomaton_58()




CTD_ANON_58._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit'), SupplyKitTemplate, scope=CTD_ANON_58, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 69, 1)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_58._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 40, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_58._Automaton = _BuildAutomaton_59()




CTD_ANON_59._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ControlKit'), SupplyKitControl, scope=CTD_ANON_59, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 70, 1)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_59._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ControlKit')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 50, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_59._Automaton = _BuildAutomaton_60()




CTD_ANON_60._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellPackKit'), SupplyKitCellPack, scope=CTD_ANON_60, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 71, 1)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_60._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellPackKit')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioPartNumbers.xsd', 60, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_60._Automaton = _BuildAutomaton_61()




CTD_ANON_61._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentKit'), ReagentKitType, scope=CTD_ANON_61, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 18, 1)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_61._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentKit')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 13, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_61._Automaton = _BuildAutomaton_62()




CTD_ANON_62._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reagent'), ReagentType, scope=CTD_ANON_62, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 17, 1)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_62._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reagent')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 72, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_62._Automaton = _BuildAutomaton_63()




CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube'), ReagentTubeType, scope=CTD_ANON_63, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 19, 1)))

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentTube')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 79, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_63._Automaton = _BuildAutomaton_64()




CTD_ANON_64._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRow'), ReagentPlateRowType, scope=CTD_ANON_64, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 20, 1)))

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_64._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRow')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 86, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_64._Automaton = _BuildAutomaton_65()




CTD_ANON_65._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompatibleAutomation'), pyxb.binding.datatypes.string, scope=CTD_ANON_65, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 93, 8)))

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 93, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_65._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CompatibleAutomation')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 93, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_65._Automaton = _BuildAutomaton_66()




BaseEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Extensions'), CTD_ANON_4, scope=BaseEntityType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3)))

def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BaseEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BaseEntityType._Automaton = _BuildAutomaton_67()




CTD_ANON_66._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CommonServicesInstanceId'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_66, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 41, 6)))

CTD_ANON_66._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CreatorUserId'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_66, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 42, 6)))

CTD_ANON_66._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ParentJobId'), pyxb.binding.datatypes.IDREF, scope=CTD_ANON_66, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 43, 6)))

CTD_ANON_66._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ParentTool'), BaseEntityType, scope=CTD_ANON_66, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 44, 6)))

def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 41, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 42, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 43, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 44, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_66._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CommonServicesInstanceId')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 41, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_66._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CreatorUserId')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 42, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_66._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ParentJobId')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 43, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_66._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ParentTool')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 44, 6))
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
CTD_ANON_66._Automaton = _BuildAutomaton_68()




ReadSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SummaryStats'), CTD_ANON_21, scope=ReadSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 65, 5)))

ReadSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Collections'), CTD_ANON_24, scope=ReadSetMetadataType, documentation='A set of acquisition definitions', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 125, 1)))

ReadSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSamples'), CTD_ANON_37, scope=ReadSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 673, 1)))

def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 63, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 64, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 65, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TotalLength')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 36, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumRecords')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 37, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Provenance')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Collections')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 63, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BioSamples')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 64, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SummaryStats')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 65, 5))
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
ReadSetMetadataType._Automaton = _BuildAutomaton_69()




SubreadSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AverageSubreadLength'), pyxb.binding.datatypes.int, scope=SubreadSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 91, 5)))

SubreadSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AverageSubreadQuality'), pyxb.binding.datatypes.float, scope=SubreadSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 92, 5)))

def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubreadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TotalLength')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 36, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubreadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumRecords')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 37, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubreadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Provenance')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubreadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AverageSubreadLength')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 91, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SubreadSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AverageSubreadQuality')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 92, 5))
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
SubreadSetMetadataType._Automaton = _BuildAutomaton_70()




CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Validation'), CTD_ANON_68, scope=CTD_ANON_67, documentation='\n        A validation type which is an element/part of every other element in the schema.  It is used to communicate validation issues as part of the output.\n      ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 152, 1)))

def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 69, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Validation')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 69, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_67._Automaton = _BuildAutomaton_71()




AlignmentSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Aligner'), pyxb.binding.datatypes.anyType, scope=AlignmentSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 141, 5)))

def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 141, 5))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AlignmentSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TotalLength')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 36, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AlignmentSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumRecords')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 37, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AlignmentSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Provenance')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AlignmentSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Aligner')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 141, 5))
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
AlignmentSetMetadataType._Automaton = _BuildAutomaton_72()




ContigSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contigs'), CTD_ANON_72, scope=ContigSetMetadataType, documentation='List of contigs in a ContigSet', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 114, 1)))

ContigSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Organism'), pyxb.binding.datatypes.string, scope=ContigSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 150, 5)))

ContigSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ploidy'), pyxb.binding.datatypes.string, scope=ContigSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 151, 5)))

def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 150, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 151, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TotalLength')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 36, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumRecords')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 37, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Provenance')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Organism')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 150, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ploidy')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 151, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ContigSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contigs')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 152, 5))
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
ContigSetMetadataType._Automaton = _BuildAutomaton_73()




BarcodeSetMetadataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BarcodeConstruction'), pyxb.binding.datatypes.string, scope=BarcodeSetMetadataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 161, 5)))

def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TotalLength')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 36, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumRecords')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 37, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Provenance')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 38, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BarcodeSetMetadataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BarcodeConstruction')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 161, 5))
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
BarcodeSetMetadataType._Automaton = _BuildAutomaton_74()




AutomationConstraintType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Automations'), CTD_ANON_2, scope=AutomationConstraintType, documentation='Names of automations that are all similarly constrained', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 34, 5)))

AutomationConstraintType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InsertSizes'), CTD_ANON_3, scope=AutomationConstraintType, documentation='A list of insert sizes (buckets) recommended for use', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 44, 5)))

def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 34, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 44, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AutomationConstraintType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AutomationConstraintType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Automations')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 34, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AutomationConstraintType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InsertSizes')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioAutomationConstraints.xsd', 44, 5))
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
AutomationConstraintType._Automaton = _BuildAutomaton_75()




def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AnalogType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AnalogType._Automaton = _BuildAutomaton_76()




DataEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue'), pyxb.binding.datatypes.base64Binary, scope=DataEntityType, documentation='A complex data type element, such as an image, file, binary object, etc.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5)))

DataEntityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CheckSum'), pyxb.binding.datatypes.string, scope=DataEntityType, documentation='small-size datum of the attached value for the purpose of detecting errors or modification which may have been introduced during its transmission or storage', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5)))

def _BuildAutomaton_77 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DataEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DataEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DataEntityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
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
DataEntityType._Automaton = _BuildAutomaton_77()




def _BuildAutomaton_78 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DNABarcode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DNABarcode._Automaton = _BuildAutomaton_78()




AutomationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameters'), CTD_ANON_8, scope=AutomationType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 241, 5)))

def _BuildAutomaton_79 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 241, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AutomationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AutomationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AutomationParameters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 241, 5))
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
AutomationType._Automaton = _BuildAutomaton_79()




CTD_ANON_69._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Analogs'), CTD_ANON_11, scope=CTD_ANON_69, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 346, 10)))

def _BuildAutomaton_80 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_69._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_69._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Analogs')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 346, 10))
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
CTD_ANON_69._Automaton = _BuildAutomaton_80()




SequencingChemistryConfig._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Analogs'), CTD_ANON_13, scope=SequencingChemistryConfig, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 379, 5)))

def _BuildAutomaton_81 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_81
    del _BuildAutomaton_81
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequencingChemistryConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SequencingChemistryConfig._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Analogs')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 379, 5))
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
SequencingChemistryConfig._Automaton = _BuildAutomaton_81()




StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleSize'), pyxb.binding.datatypes.int, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 397, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleMean'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 398, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleMed'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 399, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleStd'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 400, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Sample95thPct'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 401, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumBins'), pyxb.binding.datatypes.int, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 402, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinCounts'), CTD_ANON_14, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 403, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinWidth'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 410, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MinOutlierValue'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 411, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MinBinValue'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 412, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaxBinValue'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 413, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaxOutlierValue'), pyxb.binding.datatypes.float, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 414, 5)))

StatsContinuousDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MetricDescription'), pyxb.binding.datatypes.string, scope=StatsContinuousDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 415, 5)))

def _BuildAutomaton_82 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_82
    del _BuildAutomaton_82
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SampleSize')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 397, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SampleMean')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 398, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SampleMed')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 399, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SampleStd')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 400, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Sample95thPct')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 401, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumBins')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 402, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinCounts')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 403, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinWidth')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 410, 5))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MinOutlierValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 411, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MinBinValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 412, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MaxBinValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 413, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MaxOutlierValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 414, 5))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatsContinuousDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MetricDescription')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 415, 5))
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
StatsContinuousDistType._Automaton = _BuildAutomaton_82()




StatsDiscreteDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumBins'), pyxb.binding.datatypes.int, scope=StatsDiscreteDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 428, 5)))

StatsDiscreteDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinCounts'), CTD_ANON_15, scope=StatsDiscreteDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 429, 5)))

StatsDiscreteDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MetricDescription'), pyxb.binding.datatypes.string, scope=StatsDiscreteDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 436, 5)))

StatsDiscreteDistType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BinLabels'), CTD_ANON_16, scope=StatsDiscreteDistType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 437, 5)))

def _BuildAutomaton_83 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_83
    del _BuildAutomaton_83
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsDiscreteDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsDiscreteDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumBins')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 428, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsDiscreteDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinCounts')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 429, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsDiscreteDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MetricDescription')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 436, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatsDiscreteDistType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BinLabels')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 437, 5))
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
StatsDiscreteDistType._Automaton = _BuildAutomaton_83()




StatsTimeSeriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeUnits'), pyxb.binding.datatypes.string, scope=StatsTimeSeriesType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 455, 5)))

StatsTimeSeriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValueUnits'), pyxb.binding.datatypes.string, scope=StatsTimeSeriesType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 456, 5)))

StatsTimeSeriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), pyxb.binding.datatypes.float, scope=StatsTimeSeriesType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 457, 5)))

StatsTimeSeriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MeasInterval'), pyxb.binding.datatypes.float, scope=StatsTimeSeriesType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 458, 5)))

StatsTimeSeriesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Values'), CTD_ANON_17, scope=StatsTimeSeriesType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 459, 5)))

def _BuildAutomaton_84 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_84
    del _BuildAutomaton_84
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 459, 5))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsTimeSeriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsTimeSeriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeUnits')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 455, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsTimeSeriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValueUnits')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 456, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(StatsTimeSeriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartTime')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 457, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StatsTimeSeriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MeasInterval')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 458, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StatsTimeSeriesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Values')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 459, 5))
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
StatsTimeSeriesType._Automaton = _BuildAutomaton_84()




DataSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources'), CTD_ANON_6, scope=DataSetType, documentation='Pointers to data that do not reside inside the parent structure', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 202, 1)))

DataSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Filters'), CTD_ANON_22, scope=DataSetType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5)))

DataSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSets'), CTD_ANON_23, scope=DataSetType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5)))

def _BuildAutomaton_85 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_85
    del _BuildAutomaton_85
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DataSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DataSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DataSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
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
DataSetType._Automaton = _BuildAutomaton_85()




CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InstCtrlVer'), pyxb.binding.datatypes.string, scope=CTD_ANON_70, documentation='Instrument control software version. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 144, 6)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SigProcVer'), pyxb.binding.datatypes.string, scope=CTD_ANON_70, documentation='Signal processing software version. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 149, 6)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Automation'), AutomationType, scope=CTD_ANON_70, documentation='Defines the collection workflow (e.g., robotic movement, movie acquisition) for a particular cell. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 171, 6)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CollectionNumber'), pyxb.binding.datatypes.int, scope=CTD_ANON_70, documentation='Collection number for this plate well. Sample from one plate well or tube can be distributed to more than one cell. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 176, 6)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellIndex'), pyxb.binding.datatypes.int, scope=CTD_ANON_70, documentation='The zero-based index of this particular cell within the cell tray.  Likely to be in the range of [0-3]', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 181, 6)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SetNumber'), pyxb.binding.datatypes.unsignedShort, scope=CTD_ANON_70, documentation='Formerly known as the look number.  1 - N.  Defaults to 1. 0 if the look is unknown. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 186, 6)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CellPac'), SupplyKitCellPack, scope=CTD_ANON_70, documentation='The SMRT cell packaging supply information. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 191, 6)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit'), SupplyKitTemplate, scope=CTD_ANON_70, documentation='Defines the template (sample) prep kit used for this experiment. Can be used to get back to the primary and adapter used. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 196, 6)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BindingKit'), SupplyKitBinding, scope=CTD_ANON_70, documentation='The binding kit supply information. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 201, 6)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitPlate'), SupplyKitSequencing, scope=CTD_ANON_70, documentation='The sequencing kit supply information. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 206, 6)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RunDetails'), CTD_ANON_25, scope=CTD_ANON_70, documentation='Information related to an instrument run.  A run can contain multiple chips, wells, and movies. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 248, 1)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Movie'), CTD_ANON_26, scope=CTD_ANON_70, documentation='A movie corresponds to one acquisition for a chip, one set (look) and one strobe. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 287, 1)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExpirationData'), CTD_ANON_27, scope=CTD_ANON_70, documentation='Container for the expired consumable data. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 311, 1)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WellSample'), CTD_ANON_71, scope=CTD_ANON_70, documentation='Container for the sample related data. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 432, 1)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Primary'), CTD_ANON_29, scope=CTD_ANON_70, documentation='Container for the primary analysis related data. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 503, 1)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Secondary'), CTD_ANON_32, scope=CTD_ANON_70, documentation='Container for the primary analysis related data. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 568, 1)))

CTD_ANON_70._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UserDefinedFields'), UserDefinedFieldsType, scope=CTD_ANON_70, documentation='A set of key-value pairs specified by a user via the run input mechanism. Note that uniqueness of keys is not enforced here and so may contain duplicate keys. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 602, 1)))

def _BuildAutomaton_86 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_86
    del _BuildAutomaton_86
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 144, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 149, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 154, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 159, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 176, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 181, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 186, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 191, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 196, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 201, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 206, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 211, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 216, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 221, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 226, 6))
    counters.add(cc_15)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InstCtrlVer')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 144, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SigProcVer')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 149, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RunDetails')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 154, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Movie')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 159, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WellSample')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 164, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Automation')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 171, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CollectionNumber')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 176, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellIndex')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 181, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SetNumber')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 186, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CellPac')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 191, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TemplatePrepKit')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 196, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BindingKit')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 201, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitPlate')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 206, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Primary')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 211, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Secondary')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 216, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UserDefinedFields')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 221, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_70._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExpirationData')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 226, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
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
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_17._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_70._Automaton = _BuildAutomaton_86()




BioSampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSamples'), CTD_ANON_37, scope=BioSampleType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 673, 1)))

def _BuildAutomaton_87 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_87
    del _BuildAutomaton_87
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 372, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BioSampleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BioSampleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BioSamples')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 372, 5))
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
BioSampleType._Automaton = _BuildAutomaton_87()




CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PlateId'), pyxb.binding.datatypes.string, scope=CTD_ANON_71, documentation='The ID of the sample plate. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 440, 6)))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WellName'), pyxb.binding.datatypes.string, scope=CTD_ANON_71, documentation='Identifies which well this sample came from (e.g., coordinate on a plate). ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 445, 6)))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Concentration'), pyxb.binding.datatypes.double, scope=CTD_ANON_71, documentation='Sample input concentration. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 450, 6)))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleReuseEnabled'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_71, documentation='Whether or not complex reuse is enabled for this well. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 455, 6)))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StageHotstartEnabled'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_71, documentation='Whether or not hotstart at the stage is enabled for this well. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 460, 6)))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SizeSelectionEnabled'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_71, documentation='Whether or not size selection is enabled for this well. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 465, 6)))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UseCount'), pyxb.binding.datatypes.int, scope=CTD_ANON_71, documentation='Count of usages for this batch of complex. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 470, 6)))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Comments'), pyxb.binding.datatypes.string, scope=CTD_ANON_71, documentation='User-supplied comments about the sample. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 475, 6)))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DNAControlComplex'), pyxb.binding.datatypes.string, scope=CTD_ANON_71, documentation='Indicating what kind (if any) control was used. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 480, 6)))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SampleBarcodeInfo'), DataEntityType, scope=CTD_ANON_71, documentation='When utilizing DNA barcoding, store the list of smaple barcodes in this element.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 485, 6)))

CTD_ANON_71._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSamplePointers'), CTD_ANON_35, scope=CTD_ANON_71, documentation='Back references to other BarcodedSampleType object UniqueIds which utilize this sample', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 639, 1)))

def _BuildAutomaton_88 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_88
    del _BuildAutomaton_88
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 480, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 485, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 490, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PlateId')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 440, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WellName')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 445, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Concentration')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 450, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SampleReuseEnabled')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 455, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StageHotstartEnabled')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 460, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SizeSelectionEnabled')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 465, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UseCount')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 470, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Comments')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 475, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DNAControlComplex')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 480, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SampleBarcodeInfo')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 485, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_71._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BioSamplePointers')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 490, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_71._Automaton = _BuildAutomaton_88()




def _BuildAutomaton_89 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_89
    del _BuildAutomaton_89
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReagentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReagentType._Automaton = _BuildAutomaton_89()




ReagentKitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reagents'), CTD_ANON_62, scope=ReagentKitType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 69, 5)))

ReagentKitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentTubes'), CTD_ANON_63, scope=ReagentKitType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 76, 5)))

ReagentKitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRows'), CTD_ANON_64, scope=ReagentKitType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 83, 5)))

ReagentKitType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CompatibleAutomations'), CTD_ANON_65, scope=ReagentKitType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 90, 5)))

def _BuildAutomaton_90 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_90
    del _BuildAutomaton_90
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 90, 5))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReagentKitType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReagentKitType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reagents')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 69, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReagentKitType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentTubes')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 76, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReagentKitType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentPlateRows')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 83, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReagentKitType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CompatibleAutomations')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 90, 5))
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
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReagentKitType._Automaton = _BuildAutomaton_90()




def _BuildAutomaton_91 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_91
    del _BuildAutomaton_91
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReagentTubeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReagentTubeType._Automaton = _BuildAutomaton_91()




def _BuildAutomaton_92 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_92
    del _BuildAutomaton_92
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReagentPlateRowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReagentPlateRowType._Automaton = _BuildAutomaton_92()




CTD_ANON_72._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Contig'), CTD_ANON_73, scope=CTD_ANON_72, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 122, 6)))

def _BuildAutomaton_93 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_93
    del _BuildAutomaton_93
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_72._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_72._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Contig')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 122, 6))
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
CTD_ANON_72._Automaton = _BuildAutomaton_93()




def _BuildAutomaton_94 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_94
    del _BuildAutomaton_94
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_73._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_73._Automaton = _BuildAutomaton_94()




def _BuildAutomaton_95 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_95
    del _BuildAutomaton_95
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_74._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_74._Automaton = _BuildAutomaton_95()




def _BuildAutomaton_96 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_96
    del _BuildAutomaton_96
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_75._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_75._Automaton = _BuildAutomaton_96()




def _BuildAutomaton_97 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_97
    del _BuildAutomaton_97
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InputOutputDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InputOutputDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(InputOutputDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
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
InputOutputDataType._Automaton = _BuildAutomaton_97()




PartNumberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePartNumbers'), CTD_ANON_9, scope=PartNumberType, documentation='By default, a PN is compatible for use with other PNs in the system.  In order to exclude the usage of one or more PNs with this one, the incompatible PNs are listed here.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5)))

PartNumberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleAutomations'), CTD_ANON_10, scope=PartNumberType, documentation='By default, a PN is compatible for use with all automations in the system.  In order to exclude the usage of automations with this PN, the incompatible automation names are listed here.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5)))

def _BuildAutomaton_98 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_98
    del _BuildAutomaton_98
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PartNumberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PartNumberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PartNumberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PartNumberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePartNumbers')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(PartNumberType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleAutomations')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5))
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
PartNumberType._Automaton = _BuildAutomaton_98()




def _BuildAutomaton_99 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_99
    del _BuildAutomaton_99
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RecordedEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RecordedEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RecordedEventType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
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
RecordedEventType._Automaton = _BuildAutomaton_99()




SequencingChemistry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DyeSet'), CTD_ANON_69, scope=SequencingChemistry, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 341, 5)))

def _BuildAutomaton_100 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_100
    del _BuildAutomaton_100
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequencingChemistry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequencingChemistry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequencingChemistry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SequencingChemistry._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DyeSet')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 341, 5))
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
SequencingChemistry._Automaton = _BuildAutomaton_100()




ReadSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), ReadSetMetadataType, scope=ReadSetType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 26, 5)))

def _BuildAutomaton_101 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_101
    del _BuildAutomaton_101
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 26, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ReadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ReadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 26, 5))
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
ReadSetType._Automaton = _BuildAutomaton_101()




BarcodedSampleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Barcodes'), CTD_ANON_28, scope=BarcodedSampleType, documentation='A list of barcodes associated with the biological sample', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 347, 5)))

def _BuildAutomaton_102 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_102
    del _BuildAutomaton_102
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 372, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 347, 5))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BarcodedSampleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BarcodedSampleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BioSamples')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 372, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BarcodedSampleType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Barcodes')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 347, 5))
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
BarcodedSampleType._Automaton = _BuildAutomaton_102()




AssayType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubreadSet'), CTD_ANON_83, scope=AssayType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 681, 1)))

def _BuildAutomaton_103 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_103
    del _BuildAutomaton_103
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssayType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssayType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AssayType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AssayType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubreadSet')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 241, 5))
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
AssayType._Automaton = _BuildAutomaton_103()




ExperimentContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InvestigatorName'), pyxb.binding.datatypes.string, scope=ExperimentContainerType, documentation='An optional PI name', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 257, 5)))

ExperimentContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CreatedDate'), pyxb.binding.datatypes.date, scope=ExperimentContainerType, documentation='Automatically generated creation date', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 262, 5)))

ExperimentContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Runs'), CTD_ANON_47, scope=ExperimentContainerType, documentation='Multiple acquisitions from different instrument runs', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 267, 5)))

ExperimentContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSets'), CTD_ANON_48, scope=ExperimentContainerType, documentation='Pointers to various data elements associated with the acquisitions', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 277, 5)))

ExperimentContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvents'), CTD_ANON_49, scope=ExperimentContainerType, documentation="Journal of metrics, system events, or alarms that were generated during this container's lifetime", location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 287, 5)))

ExperimentContainerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BioSamples'), CTD_ANON_50, scope=ExperimentContainerType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 301, 5)))

def _BuildAutomaton_104 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_104
    del _BuildAutomaton_104
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 257, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 267, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 277, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 287, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 301, 5))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InvestigatorName')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 257, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CreatedDate')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 262, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Runs')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 267, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 277, 5))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvents')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 287, 5))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ExperimentContainerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BioSamples')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 301, 5))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ExperimentContainerType._Automaton = _BuildAutomaton_104()




RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubreadSet'), CTD_ANON_83, scope=RunType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 681, 1)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Assay'), AssayType, scope=RunType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 11, 1)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RunResources'), CTD_ANON_45, scope=RunType, documentation='This is an output field specifying the requirements for the run, e.g. number of tips, estimated run time, etc.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 129, 1)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Inputs'), CTD_ANON_51, scope=RunType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 321, 5)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Outputs'), CTD_ANON_52, scope=RunType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 328, 5)))

RunType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvents'), CTD_ANON_53, scope=RunType, documentation="Journal of metrics, system events, or alarms that were generated during this run's lifetime", location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 341, 5)))

def _BuildAutomaton_105 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_105
    del _BuildAutomaton_105
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 321, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 328, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 335, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 340, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 341, 5))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Inputs')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 321, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Outputs')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 328, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Assay')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 335, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RunResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 340, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordedEvents')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 341, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RunType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubreadSet')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioDataModel.xsd', 356, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RunType._Automaton = _BuildAutomaton_105()




BarcodeSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), BarcodeSetMetadataType, scope=BarcodeSetType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 35, 5)))

def _BuildAutomaton_106 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_106
    del _BuildAutomaton_106
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BarcodeSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BarcodeSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 35, 5))
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
BarcodeSetType._Automaton = _BuildAutomaton_106()




def _BuildAutomaton_107 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_107
    del _BuildAutomaton_107
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_76._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_76._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_76._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_76._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
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
CTD_ANON_76._Automaton = _BuildAutomaton_107()




AlignmentSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), AlignmentSetMetadataType, scope=AlignmentSetType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 67, 5)))

def _BuildAutomaton_108 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_108
    del _BuildAutomaton_108
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 67, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AlignmentSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AlignmentSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AlignmentSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AlignmentSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AlignmentSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 67, 5))
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
AlignmentSetType._Automaton = _BuildAutomaton_108()




ContigSetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata'), ContigSetMetadataType, scope=ContigSetType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 99, 5)))

def _BuildAutomaton_109 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_109
    del _BuildAutomaton_109
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContigSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ContigSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 99, 5))
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
ContigSetType._Automaton = _BuildAutomaton_109()




IndexedDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources'), CTD_ANON_6, scope=IndexedDataType, documentation='Pointers to data that do not reside inside the parent structure', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 202, 1)))

IndexedDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FileIndices'), CTD_ANON_7, scope=IndexedDataType, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 221, 5)))

def _BuildAutomaton_110 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_110
    del _BuildAutomaton_110
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 221, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 232, 5))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IndexedDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IndexedDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(IndexedDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(IndexedDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FileIndices')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 221, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(IndexedDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 232, 5))
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
IndexedDataType._Automaton = _BuildAutomaton_110()




SupplyKitBinding._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Control'), SupplyKitControl, scope=SupplyKitBinding, documentation='Defines the binding kit internal control name.  Present when used, otherwise not used if not defined. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 477, 5)))

SupplyKitBinding._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IsControlUsed'), pyxb.binding.datatypes.boolean, scope=SupplyKitBinding, documentation='True if the control was used during run, otherwise false. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 482, 5)))

def _BuildAutomaton_111 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_111
    del _BuildAutomaton_111
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 477, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 482, 5))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitBinding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitBinding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitBinding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitBinding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePartNumbers')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitBinding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleAutomations')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitBinding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Control')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 477, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitBinding._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IsControlUsed')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 482, 5))
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
SupplyKitBinding._Automaton = _BuildAutomaton_111()




SupplyKitCellPack._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout'), pyxb.binding.datatypes.string, scope=SupplyKitCellPack, documentation='Defines the internal chip layout name, if any. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 498, 5)))

def _BuildAutomaton_112 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_112
    del _BuildAutomaton_112
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 498, 5))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitCellPack._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitCellPack._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitCellPack._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitCellPack._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePartNumbers')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitCellPack._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleAutomations')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitCellPack._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChipLayout')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 498, 5))
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
SupplyKitCellPack._Automaton = _BuildAutomaton_112()




SupplyKitControl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InternalControlName'), pyxb.binding.datatypes.string, scope=SupplyKitControl, documentation='Defines the internal control name, if any. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 514, 5)))

def _BuildAutomaton_113 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_113
    del _BuildAutomaton_113
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 514, 5))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePartNumbers')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleAutomations')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitControl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InternalControlName')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 514, 5))
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
SupplyKitControl._Automaton = _BuildAutomaton_113()




SupplyKitTemplate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LeftAdaptorSequence'), pyxb.binding.datatypes.string, scope=SupplyKitTemplate, documentation='Left adapter DNA sequence.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 530, 5)))

SupplyKitTemplate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LeftPrimerSequence'), pyxb.binding.datatypes.string, scope=SupplyKitTemplate, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 535, 5)))

SupplyKitTemplate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RightAdaptorSequence'), pyxb.binding.datatypes.string, scope=SupplyKitTemplate, documentation='Right adapter DNA sequence.  If not specified, a symmetric adapter model is inferred, where the left adapter sequence is used wherever needed.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 536, 5)))

SupplyKitTemplate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RightPrimerSequence'), pyxb.binding.datatypes.string, scope=SupplyKitTemplate, documentation='Right primaer sequence.  If not specified, a symmetric model is inferred, where the left primer sequence is used wherever needed.', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 541, 5)))

SupplyKitTemplate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InsertSize'), pyxb.binding.datatypes.int, scope=SupplyKitTemplate, documentation='Approximate size of insert. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 546, 5)))

def _BuildAutomaton_114 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_114
    del _BuildAutomaton_114
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 530, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 535, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 536, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 541, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 546, 5))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePartNumbers')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleAutomations')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LeftAdaptorSequence')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 530, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LeftPrimerSequence')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 535, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RightAdaptorSequence')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 536, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RightPrimerSequence')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 541, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitTemplate._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InsertSize')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 546, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SupplyKitTemplate._Automaton = _BuildAutomaton_114()




def _BuildAutomaton_115 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_115
    del _BuildAutomaton_115
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 26, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SubreadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SubreadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SubreadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SubreadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SubreadSetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 26, 5))
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
SubreadSetType._Automaton = _BuildAutomaton_115()




SupplyKitSequencing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentAutomationName'), pyxb.binding.datatypes.string, scope=SupplyKitSequencing, documentation='The reagent-mixing protocol used. ', location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 28, 5)))

SupplyKitSequencing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReagentTubes'), SupplyKitSequencing, scope=SupplyKitSequencing, documentation="Tubes associated with the reagent kit - can have up to two; don't forget to set the location, 0 or 1", location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 33, 5)))

SupplyKitSequencing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingChemistry'), SequencingChemistry, scope=SupplyKitSequencing, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 38, 5)))

SupplyKitSequencing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitDefinition'), ReagentKitType, scope=SupplyKitSequencing, location=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 39, 5)))

def _BuildAutomaton_116 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_116
    del _BuildAutomaton_116
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 28, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=2, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 33, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 38, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 39, 5))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EncodedValue')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 144, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CheckSum')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 149, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatiblePartNumbers')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 267, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncompatibleAutomations')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 281, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentAutomationName')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 28, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReagentTubes')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 33, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingChemistry')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 38, 5))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(SupplyKitSequencing._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SequencingKitDefinition')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioReagentKit.xsd', 39, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SupplyKitSequencing._Automaton = _BuildAutomaton_116()




def _BuildAutomaton_117 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_117
    del _BuildAutomaton_117
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 67, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_77._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_77._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_77._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_77._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_77._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 67, 5))
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
CTD_ANON_77._Automaton = _BuildAutomaton_117()




def _BuildAutomaton_118 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_118
    del _BuildAutomaton_118
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_78._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_78._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_78._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_78._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_78._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 35, 5))
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
CTD_ANON_78._Automaton = _BuildAutomaton_118()




def _BuildAutomaton_119 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_119
    del _BuildAutomaton_119
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 67, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_79._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 67, 5))
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
CTD_ANON_79._Automaton = _BuildAutomaton_119()




def _BuildAutomaton_120 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_120
    del _BuildAutomaton_120
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_80._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 99, 5))
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
CTD_ANON_80._Automaton = _BuildAutomaton_120()




def _BuildAutomaton_121 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_121
    del _BuildAutomaton_121
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_81._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioSecondaryDataModel.xsd', 99, 5))
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
CTD_ANON_81._Automaton = _BuildAutomaton_121()




def _BuildAutomaton_122 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_122
    del _BuildAutomaton_122
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 26, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_82._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 26, 5))
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
CTD_ANON_82._Automaton = _BuildAutomaton_122()




def _BuildAutomaton_123 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_123
    del _BuildAutomaton_123
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 26, 5))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Extensions')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioBaseDataModel.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalResources')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 106, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Filters')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 107, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSets')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 114, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_83._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataSetMetadata')), pyxb.utils.utility.Location('/tmp/tmpl4vgfXxsds/PacBioCollectionMetadata.xsd', 26, 5))
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
CTD_ANON_83._Automaton = _BuildAutomaton_123()

