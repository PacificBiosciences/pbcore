
import logging
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
        ds1 = DataSet(data.getXml(no=8))
        ds2 = DataSet(data.getXml(no=9))
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
        ds = ReferenceSet(data.getXml(18))
        for extRes in ds.externalResources:
            self.assertEqual(extRes.metaType,
                             'PacBio.ReferenceFile.ReferenceFastaFile')
            self.assertEqual(len(extRes.indices), 1)
            for index in extRes.indices:
                self.assertEqual(index.metaType, "PacBio.Index.SamIndex")
        ds = AlignmentSet(data.getXml(16))
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
            'm150207_001141_42139_c100713842550000001823146504221590_s1_p0/147739/0_3702',
            'm150207_001141_42139_c100713842550000001823146504221590_s1_p0/90702/10278_35281',
            'm150207_001141_42139_c100713842550000001823146504221590_s1_p0/135718/2228_18512',
            'm150207_001141_42139_c100713842550000001823146504221590_s1_p0/34381/28363_30724']
        seqlens = [3702, 25003, 16284, 2361]
        ds = ReferenceSet(data.getXml(18))
        for contig, name, seqlen in zip(ds.contigs, names, seqlens):
            self.assertEqual(contig.id, name)
            self.assertEqual(len(contig.sequence), seqlen)

        for name in names:
            self.assertTrue(ds.get_contig(name))

    def test_ref_names(self):
        ds = DataSet(data.getXml(18))
        refNames = ds.refNames
        expected = [
            'm150207_001141_42139_c100713842550000001823146504221590_s1_p0/147739/0_3702',
            'm150207_001141_42139_c100713842550000001823146504221590_s1_p0/90702/10278_35281',
            'm150207_001141_42139_c100713842550000001823146504221590_s1_p0/135718/2228_18512',
            'm150207_001141_42139_c100713842550000001823146504221590_s1_p0/34381/28363_30724'
            ]
        self.assertEqual(sorted(refNames), sorted(expected))

    def test_ccsread_build(self):
        ds1 = DataSet(data.getXml(5))
        self.assertEquals(type(ds1).__name__, 'ConsensusReadSet')
        self.assertEquals(type(ds1._metadata).__name__, 'SubreadSetMetadata')
        ds2 = ConsensusReadSet(data.getXml(5))
        self.assertEquals(type(ds2).__name__, 'ConsensusReadSet')
        self.assertEquals(type(ds2._metadata).__name__, 'SubreadSetMetadata')

    def test_contigset_build(self):
        ds1 = DataSet(data.getXml(6))
        self.assertEquals(type(ds1).__name__, 'ContigSet')
        self.assertEquals(type(ds1._metadata).__name__, 'ContigSetMetadata')
        ds2 = ContigSet(data.getXml(6))
        self.assertEquals(type(ds2).__name__, 'ContigSet')
        self.assertEquals(type(ds2._metadata).__name__, 'ContigSetMetadata')
        for contigmd in ds2.metadata.contigs:
            self.assertEquals(type(contigmd).__name__, 'ContigMetadata')


