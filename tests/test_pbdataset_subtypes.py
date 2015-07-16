
import logging
from urlparse import urlparse
import unittest

#from pbcore.util.Process import backticks
from pbcore.io import (DataSet, SubreadSet, ConsensusReadSet,
                       ReferenceSet, ContigSet, AlignmentSet)
import pbcore.data.datasets as data

log = logging.getLogger(__name__)

class TestDataSet(unittest.TestCase):
    """Unit and integrationt tests for the DataSet class and \
    associated module functions"""


    def test_subread_build(self):
        ds1 = SubreadSet(data.getXml(no=5))
        ds2 = SubreadSet(data.getXml(no=5))
        self.assertEquals(type(ds1).__name__, 'SubreadSet')
        self.assertEquals(ds1._metadata.__class__.__name__,
                          'SubreadSetMetadata')
        self.assertEquals(type(ds1._metadata).__name__, 'SubreadSetMetadata')
        self.assertEquals(type(ds1.metadata).__name__, 'SubreadSetMetadata')
        self.assertEquals(len(ds1.metadata.collections), 1)
        self.assertEquals(len(ds2.metadata.collections), 1)
        ds3 = ds1 + ds2
        self.assertEquals(len(ds3.metadata.collections), 2)
        ds4 = SubreadSet(data.getSubreadSet())
        self.assertEquals(type(ds4).__name__, 'SubreadSet')
        self.assertEquals(type(ds4._metadata).__name__, 'SubreadSetMetadata')
        self.assertEquals(len(ds4.metadata.collections), 1)

    def test_autofilled_metatypes(self):
        ds = ReferenceSet(data.getXml(9))
        for extRes in ds.externalResources:
            self.assertEqual(extRes.metaType,
                             'PacBio.ReferenceFile.ReferenceFastaFile')
            self.assertEqual(len(extRes.indices), 1)
            for index in extRes.indices:
                self.assertEqual(index.metaType, "PacBio.Index.SamIndex")
        ds = AlignmentSet(data.getXml(8))
        for extRes in ds.externalResources:
            self.assertEqual(extRes.metaType,
                             'PacBio.SubreadFile.SubreadBamFile')
            self.assertEqual(len(extRes.indices), 2)
            for index in extRes.indices:
                if index.resourceId.endswith('pbi'):
                    self.assertEqual(index.metaType,
                                     "PacBio.Index.PacBioIndex")
                if index.resourceId.endswith('bai'):
                    self.assertEqual(index.metaType,
                                     "PacBio.Index.BamIndex")


    def test_referenceset_contigs(self):
        names = [
            'A.baumannii.1', 'A.odontolyticus.1', 'B.cereus.1', 'B.cereus.2',
            'B.cereus.4', 'B.cereus.6', 'B.vulgatus.1', 'B.vulgatus.2',
            'B.vulgatus.3', 'B.vulgatus.4', 'B.vulgatus.5', 'C.beijerinckii.1',
            'C.beijerinckii.2', 'C.beijerinckii.3', 'C.beijerinckii.4',
            'C.beijerinckii.5', 'C.beijerinckii.6', 'C.beijerinckii.7',
            'C.beijerinckii.8', 'C.beijerinckii.9', 'C.beijerinckii.10',
            'C.beijerinckii.11', 'C.beijerinckii.12', 'C.beijerinckii.13',
            'C.beijerinckii.14', 'D.radiodurans.1', 'D.radiodurans.2',
            'E.faecalis.1', 'E.faecalis.2', 'E.coli.1', 'E.coli.2', 'E.coli.4',
            'E.coli.5', 'E.coli.6', 'E.coli.7', 'H.pylori.1', 'L.gasseri.1',
            'L.monocytogenes.1', 'L.monocytogenes.2', 'L.monocytogenes.3',
            'L.monocytogenes.5', 'N.meningitidis.1', 'P.acnes.1',
            'P.aeruginosa.1', 'P.aeruginosa.2', 'R.sphaeroides.1',
            'R.sphaeroides.3', 'S.aureus.1', 'S.aureus.4', 'S.aureus.5',
            'S.epidermidis.1', 'S.epidermidis.2', 'S.epidermidis.3',
            'S.epidermidis.4', 'S.epidermidis.5', 'S.agalactiae.1',
            'S.mutans.1', 'S.mutans.2', 'S.pneumoniae.1']
        seqlens = [1458, 1462, 1472, 1473, 1472, 1472, 1449, 1449, 1449, 1449,
                   1449, 1433, 1433, 1433, 1433, 1433, 1433, 1433, 1433, 1433,
                   1433, 1433, 1433, 1433, 1433, 1423, 1423, 1482, 1482, 1463,
                   1463, 1463, 1463, 1463, 1463, 1424, 1494, 1471, 1471, 1471,
                   1471, 1462, 1446, 1457, 1457, 1386, 1388, 1473, 1473, 1473,
                   1472, 1472, 1472, 1472, 1472, 1470, 1478, 1478, 1467]
        ds = ReferenceSet(data.getXml(9))
        log.debug([contig.id for contig in ds])
        for contig, name, seqlen in zip(ds.contigs, names, seqlens):
            self.assertEqual(contig.id, name)
            self.assertEqual(len(contig.sequence), seqlen)

        for name in names:
            self.assertTrue(ds.get_contig(name))

    def test_ccsread_build(self):
        ds1 = ConsensusReadSet(data.getXml(2), strict=False)
        self.assertEquals(type(ds1).__name__, 'ConsensusReadSet')
        self.assertEquals(type(ds1._metadata).__name__, 'SubreadSetMetadata')
        ds2 = ConsensusReadSet(data.getXml(2), strict=False)
        self.assertEquals(type(ds2).__name__, 'ConsensusReadSet')
        self.assertEquals(type(ds2._metadata).__name__, 'SubreadSetMetadata')

    def test_contigset_build(self):
        ds1 = ContigSet(data.getXml(3))
        self.assertEquals(type(ds1).__name__, 'ContigSet')
        self.assertEquals(type(ds1._metadata).__name__, 'ContigSetMetadata')
        ds2 = ContigSet(data.getXml(3))
        self.assertEquals(type(ds2).__name__, 'ContigSet')
        self.assertEquals(type(ds2._metadata).__name__, 'ContigSetMetadata')
        for contigmd in ds2.metadata.contigs:
            self.assertEquals(type(contigmd).__name__, 'ContigMetadata')

    def test_alignment_reference(self):
        rs1 = ReferenceSet(data.getXml(9))
        fasta_res = rs1.externalResources[0]
        fasta_file = urlparse(fasta_res.resourceId).path
        ds1 = AlignmentSet(data.getXml(8),
            referenceFastaFname=fasta_file)
        ds1.addReference(fasta_file)
        aln_ref = None
        for aln in ds1:
            aln_ref = aln.reference()
            break
        self.assertTrue(aln_ref is not None)
