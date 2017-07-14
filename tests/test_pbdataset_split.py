
import os
import logging
import tempfile
import unittest
from unittest.case import SkipTest

import numpy as np

from pbcore.io import openIndexedAlignmentFile
from pbcore.io import (DataSet, SubreadSet, ReferenceSet, AlignmentSet,
                       openDataSet, HdfSubreadSet,
                       openDataFile)
import pbcore.data.datasets as data
import pbcore.data as upstreamdata

from utils import _pbtestdata, _check_constools, _internal_data

log = logging.getLogger(__name__)

class TestDataSetSplit(unittest.TestCase):
    """Unit and integrationt tests for the DataSet class and \
    associated module functions"""

    def test_split(self):
        ds1 = openDataSet(data.getXml(12))
        self.assertTrue(ds1.numExternalResources > 1)
        dss = ds1.split()
        self.assertTrue(len(dss) == ds1.numExternalResources)
        self.assertEqual(sum(ds.numRecords for ds in dss), ds1.numRecords)
        self.assertEqual(sum(ds.totalLength for ds in dss), ds1.totalLength)
        self.assertEqual(sum(len(ds) for ds in dss), len(ds1))
        dss = ds1.split(chunks=1)
        self.assertTrue(len(dss) == 1)
        self.assertEqual(sum(ds.numRecords for ds in dss), ds1.numRecords)
        self.assertEqual(sum(ds.totalLength for ds in dss), ds1.totalLength)
        self.assertEqual(sum(len(ds) for ds in dss), len(ds1))
        dss = ds1.split(chunks=2)
        self.assertTrue(len(dss) == 2)
        self.assertEqual(sum(ds.numRecords for ds in dss), ds1.numRecords)
        self.assertEqual(sum(ds.totalLength for ds in dss), ds1.totalLength)
        self.assertEqual(sum(len(ds) for ds in dss), len(ds1))
        dss = ds1.split(chunks=2, ignoreSubDatasets=True)
        self.assertTrue(len(dss) == 2)
        self.assertEqual(sum(ds.numRecords for ds in dss), ds1.numRecords)
        self.assertEqual(sum(ds.totalLength for ds in dss), ds1.totalLength)
        self.assertEqual(sum(len(ds) for ds in dss), len(ds1))
        self.assertFalse(dss[0].uuid == dss[1].uuid)
        self.assertTrue(dss[0].name == dss[1].name)
        # Lets try merging and splitting on subdatasets
        ds1 = openDataSet(data.getXml(8))
        self.assertEquals(ds1.totalLength, 123588)
        ds1tl = ds1.totalLength
        ds2 = openDataSet(data.getXml(11))
        self.assertEquals(ds2.totalLength, 117086)
        ds2tl = ds2.totalLength
        dss = ds1 + ds2
        self.assertTrue(dss.totalLength == (ds1tl + ds2tl))
        ds1, ds2 = sorted(dss.split(2, ignoreSubDatasets=False),
                          key=lambda x: x.totalLength,
                          reverse=True)
        self.assertTrue(ds1.totalLength == ds1tl)
        self.assertTrue(ds2.totalLength == ds2tl)

    def test_split_zmws(self):
        N_RECORDS = 117
        test_file = upstreamdata.getUnalignedBam()
        ds1 = openDataFile(test_file)
        self.assertEqual(len([r for r in ds1]), N_RECORDS)
        self.assertEqual(len(ds1), N_RECORDS)
        dss = ds1.split(chunks=1, zmws=True)
        self.assertEqual(len(dss), 1)
        self.assertEqual(sum([len([r for r in ds_]) for ds_ in dss]),
                         N_RECORDS)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         N_RECORDS)

        # We have a lower limit on the number of zmws, now
        dss = ds1.split(chunks=12, zmws=True)
        self.assertEqual(len(dss), 2)
        self.assertEqual(sum([len([r for r in ds_]) for ds_ in dss]),
                         N_RECORDS)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         N_RECORDS)
        self.assertEqual(
            dss[0].zmwRanges,
            [('m140905_042212_sidney_c100564852550000001823085912221377_s1_X0',
              1650, 32328)])
        self.assertEqual(
            dss[-1].zmwRanges,
            [('m140905_042212_sidney_c100564852550000001823085912221377_s1_X0',
              32560, 54396)])
        ranges = sorted([c.zmwRanges[0][1:] for c in dss])
        interspans = []
        last = None
        for rg in ranges:
            if not last is None:
                interspans.append((last, rg[0]))
                self.assertFalse(last == rg[0])
            last = rg[1]
        for rg in interspans:
            self.assertEqual(len(np.nonzero(np.logical_and(
                ds1.index.holeNumber < rg[1],
                ds1.index.holeNumber > rg[0]))[0]), 0)

    def test_split_zmws_targetsize(self):
        N_RECORDS = 117
        N_ZMWS = 48
        test_file = upstreamdata.getUnalignedBam()
        ds1 = openDataFile(test_file)
        self.assertEqual(len([r for r in ds1]), N_RECORDS)
        self.assertEqual(len(ds1), N_RECORDS)
        self.assertEqual(len(set(ds1.index.holeNumber)), N_ZMWS)

        # with no split
        dss = ds1.split(targetSize=1000, zmws=True)
        self.assertEqual(len(dss), 1)
        self.assertEqual(sum([len([r for r in ds_]) for ds_ in dss]),
                         N_RECORDS)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         N_RECORDS)
        exp = [48]
        obs = sorted([len(set(ds.index.holeNumber)) for ds in dss])
        self.assertListEqual(exp, obs)

        # with a split
        dss = ds1.split(targetSize=25, zmws=True)
        self.assertEqual(len(dss), 2)
        self.assertEqual(sum([len([r for r in ds_]) for ds_ in dss]),
                         N_RECORDS)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         N_RECORDS)
        exp = [24, 24]
        obs = sorted([len(set(ds.index.holeNumber)) for ds in dss])
        self.assertListEqual(exp, obs)

        # with a split
        dss = ds1.split(targetSize=5, zmws=True)
        self.assertEqual(len(dss), 10)
        self.assertEqual(sum([len([r for r in ds_]) for ds_ in dss]),
                         N_RECORDS)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         N_RECORDS)
        exp = [4, 4, 5, 5, 5, 5, 5, 5, 5, 5]
        obs = sorted([len(set(ds.index.holeNumber)) for ds in dss])
        self.assertListEqual(exp, obs)

    #@unittest.skipUnless(os.path.isdir("/pbi/dept/secondary/siv/testdata"),
    #                     "Missing testadata directory")
    @unittest.skip("Too expensive")
    def test_large_split_zmws(self):
        N_RECORDS = 959539
        test_file = ("/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/"
                     "2372215/0007/Analysis_Results/m150404_101626_42"
                     "267_c100807920800000001823174110291514_s1_p0.al"
                     "l.subreadset.xml")
        ds1 = openDataFile(test_file)
        self.assertEqual(len(ds1), N_RECORDS)
        dss = ds1.split(chunks=1, zmws=True)
        self.assertEqual(len(dss), 1)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         N_RECORDS)
        dss = ds1.split(chunks=12, zmws=True)
        self.assertEqual(len(dss), 12)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         N_RECORDS)
        self.assertEqual(
            dss[0].zmwRanges,
            [('m150404_101626_42267_c100807920800000001823174110291514_s1_p0',
              7, 14009)])
        self.assertEqual(
            dss[-1].zmwRanges,
            [('m150404_101626_42267_c100807920800000001823174110291514_s1_p0',
              149881, 163475)])
        ranges = sorted([c.zmwRanges[0][1:] for c in dss])
        interspans = []
        last = None
        for rg in ranges:
            if not last is None:
                interspans.append((last, rg[0]))
                self.assertFalse(last == rg[0])
            last = rg[1]
        for rg in interspans:
            self.assertEqual(len(np.nonzero(np.logical_and(
                ds1.index.holeNumber < rg[1],
                ds1.index.holeNumber > rg[0]))[0]), 0)


    @unittest.skipUnless(os.path.isdir("/pbi/dept/secondary/siv/testdata"),
                         "Missing testadata directory")
    def test_multi_movie_split_zmws(self):
        N_RECORDS = 1745161
        test_file_1 = ("/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/"
                       "2372215/0007/Analysis_Results/m150404_101626_42"
                       "267_c100807920800000001823174110291514_s1_p0.al"
                       "l.subreadset.xml")
        test_file_2 = ("/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/"
                       "2590980/0008/Analysis_Results/m141115_075238_et"
                       "han_c100699872550000001823139203261572_s1_p0.al"
                       "l.subreadset.xml")
        ds1 = SubreadSet(test_file_1, test_file_2)
        # used to get total:
        #self.assertEqual(sum(1 for _ in ds1), N_RECORDS)
        self.assertEqual(len(ds1), N_RECORDS)
        dss = ds1.split(chunks=1, zmws=True)
        self.assertEqual(len(dss), 1)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         N_RECORDS)

        dss = ds1.split(chunks=12, zmws=True)
        self.assertEqual(len(dss), 12)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         N_RECORDS)
        self.assertEqual(
            dss[0].zmwRanges,
            [('m150404_101626_42267_c100807920800000001823174110291514_s1_p0',
              7, 22099)])
        self.assertEqual(
            dss[-1].zmwRanges,
            [('m141115_075238_ethan_c100699872550000001823139203261572_s1_p0',
              127819, 163468)])

    def test_multi_movie_split_zmws_existing_simple_filters(self):
        N_RECORDS = 1745161
        test_file_1 = ("/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/"
                       "2372215/0007/Analysis_Results/m150404_101626_42"
                       "267_c100807920800000001823174110291514_s1_p0.al"
                       "l.subreadset.xml")
        test_file_2 = ("/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/"
                       "2590980/0008/Analysis_Results/m141115_075238_et"
                       "han_c100699872550000001823139203261572_s1_p0.al"
                       "l.subreadset.xml")
        ds1 = SubreadSet(test_file_1, test_file_2)
        # used to get total:
        #self.assertEqual(sum(1 for _ in ds1), N_RECORDS)
        self.assertEqual(len(ds1), N_RECORDS)
        ds1.filters.addRequirement(rq=[('>', '0.7'), ('<', '0.5')])
        FILT_RECORDS = 1732613
        self.assertEqual(len(ds1), FILT_RECORDS)
        ds1._index = None
        ds1.updateCounts()
        self.assertEqual(len(ds1), FILT_RECORDS)

        dss = ds1.split(chunks=1, zmws=True)
        dss[0]._index = None
        dss[0].updateCounts()

        self.assertEqual(len(dss), 1)
        self.assertEqual(len(dss[0]), FILT_RECORDS)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         FILT_RECORDS)

        dss = ds1.split(chunks=12, zmws=True)
        self.assertEqual(len(dss), 12)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         FILT_RECORDS)
        self.assertEqual(
            dss[0].zmwRanges,
            [('m150404_101626_42267_c100807920800000001823174110291514_s1_p0',
              7, 22073)])
        self.assertEqual(
            dss[-1].zmwRanges,
            [('m141115_075238_ethan_c100699872550000001823139203261572_s1_p0',
              127695, 163468)])

    def test_multi_movie_split_zmws_existing_filters(self):
        N_RECORDS = 1745161
        test_file_1 = ("/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/"
                       "2372215/0007/Analysis_Results/m150404_101626_42"
                       "267_c100807920800000001823174110291514_s1_p0.al"
                       "l.subreadset.xml")
        test_file_2 = ("/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/"
                       "2590980/0008/Analysis_Results/m141115_075238_et"
                       "han_c100699872550000001823139203261572_s1_p0.al"
                       "l.subreadset.xml")
        ds1 = SubreadSet(test_file_1, test_file_2)
        # used to get total:
        #self.assertEqual(sum(1 for _ in ds1), N_RECORDS)
        self.assertEqual(len(ds1), N_RECORDS)
        ds1.filters.addRequirement(
            movie=[('=',
                'm150404_101626_42267_c100807920800000001823174110291514_s1_p0'),
                   ('=',
                'm141115_075238_ethan_c100699872550000001823139203261572_s1_p0')],
            zm=[('>', 10), ('>', 127900)])
        ds1.filters.mapRequirement(
            zm=[('<', 10000), ('<', 140000)])
        FILT_RECORDS = 117776
        self.assertEqual(len(ds1), FILT_RECORDS)
        ds1._index = None
        ds1.updateCounts()
        self.assertEqual(len(ds1), FILT_RECORDS)

        dss = ds1.split(chunks=1, zmws=True)

        self.assertEqual(len(dss), 1)
        self.assertEqual(len(dss[0]), FILT_RECORDS)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         FILT_RECORDS)

        dss = ds1.split(chunks=12, zmws=True)
        self.assertEqual(len(dss), 12)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         FILT_RECORDS)
        self.assertEqual(
            dss[0].zmwRanges,
            [('m150404_101626_42267_c100807920800000001823174110291514_s1_p0',
              11, 1515)])
        self.assertEqual(
            dss[-1].zmwRanges,
            [('m141115_075238_ethan_c100699872550000001823139203261572_s1_p0',
              137634, 139999)])

    @unittest.skipUnless(os.path.isdir("/pbi/dept/secondary/siv/testdata"),
                         "Missing testadata directory")
    def test_movie_split(self):
        N_RECORDS = 1745161
        N_RECORDS_1 = 959539
        N_RECORDS_2 = 785622
        test_file_1 = ("/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/"
                       "2372215/0007/Analysis_Results/m150404_101626_42"
                       "267_c100807920800000001823174110291514_s1_p0.al"
                       "l.subreadset.xml")
        test_file_2 = ("/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/"
                       "2590980/0008/Analysis_Results/m141115_075238_et"
                       "han_c100699872550000001823139203261572_s1_p0.al"
                       "l.subreadset.xml")
        ds1 = SubreadSet(test_file_1, test_file_2)
        # used to get total:
        #self.assertEqual(sum(1 for _ in ds1), N_RECORDS)
        self.assertEqual(len(ds1), N_RECORDS)
        dss = ds1.split_movies(1)
        self.assertEqual(len(dss), 1)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         N_RECORDS)
        self.assertEqual(len(ds1), N_RECORDS)
        self.assertFalse(ds1.filters)

        dss = ds1.split_movies(12)
        self.assertEqual(len(dss), 2)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         N_RECORDS)
        self.assertEqual(len(set(dss[0].index.qId)), 1)
        self.assertEqual(len(set(dss[-1].index.qId)), 1)
        self.assertEqual(
            dss[0].qid2mov[list(set(dss[0].index.qId))[0]],
            'm150404_101626_42267_c100807920800000001823174110291514_s1_p0')
        self.assertEqual(len(dss[0]), N_RECORDS_1)
        self.assertEqual(
            dss[-1].qid2mov[list(set(dss[-1].index.qId))[0]],
            'm141115_075238_ethan_c100699872550000001823139203261572_s1_p0')
        self.assertEqual(len(dss[-1]), N_RECORDS_2)

    @unittest.skipUnless(os.path.isdir("/pbi/dept/secondary/siv/testdata"),
                         "Missing testadata directory")
    def test_split_references(self):
        test_file_1 = ('/pbi/dept/secondary/siv/testdata/SA3-RS/lambda/'
                       '2372215/0007_tiny/Alignment_Results/m150404_1016'
                       '26_42267_c100807920800000001823174110291514_s1_p'
                       '0.1.aligned.bam')
        test_file_2 = ('/pbi/dept/secondary/siv/testdata/SA3-Sequel/ecoli/'
                       '315/3150204/r54049_20160508_152025/1_A01/Alignment'
                       '_Results/m54049_160508_155917.alignmentset.xml')
        test_file_3 = ('/pbi/dept/secondary/siv/testdata/SA3-RS/ecoli/'
                       'tiny-multimovie/Alignment_Results/'
                       'combined.alignmentset.xml')
        NREC1 = len(AlignmentSet(test_file_1))
        NREC2 = len(AlignmentSet(test_file_2))
        NREC3 = len(AlignmentSet(test_file_3))
        NREC = NREC1 + NREC2 + NREC3
        self.assertNotEqual(NREC1, 0)
        self.assertNotEqual(NREC2, 0)
        self.assertNotEqual(NREC3, 0)
        self.assertNotEqual(NREC, 0)
        ds1 = AlignmentSet(test_file_1, test_file_2, test_file_3)
        # used to get total:
        #self.assertEqual(sum(1 for _ in ds1), N_RECORDS)
        self.assertEqual(len(ds1), NREC)
        dss = ds1.split_references(1)
        self.assertEqual(len(dss), 1)
        self.assertEqual(sum([len(ds_) for ds_ in dss]), NREC)
        self.assertEqual(len(ds1), NREC)
        self.assertFalse(ds1.filters)

        dss = ds1.split_references(12)
        self.assertEqual(len(dss), 2)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         NREC)
        self.assertEqual(len(set(dss[0].index.tId)), 1)
        self.assertEqual(len(set(dss[-1].index.tId)), 1)
        self.assertEqual(
            dss[0].tid2rname[list(set(dss[0].index.tId))[0]],
            'ecoliK12_pbi_March2013')
        self.assertEqual(len(dss[0]), NREC2 + NREC3)
        self.assertEqual(
            dss[-1].tid2rname[list(set(dss[-1].index.tId))[0]],
            'lambda_NEB3011')
        self.assertEqual(len(dss[-1]), NREC1)

    @unittest.skipUnless(os.path.isdir("/pbi/dept/secondary/siv/testdata"),
                         "Missing testadata directory")
    def test_multi_movie_split_zmws_with_existing_movie_filter(self):
        # TODO: test with three movies and two chunks
        N_RECORDS = 959539
        test_file_1 = ("/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/"
                       "2372215/0007/Analysis_Results/m150404_101626_42"
                       "267_c100807920800000001823174110291514_s1_p0.al"
                       "l.subreadset.xml")
        test_file_2 = ("/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/"
                       "2590980/0008/Analysis_Results/m141115_075238_et"
                       "han_c100699872550000001823139203261572_s1_p0.al"
                       "l.subreadset.xml")
        ds1 = SubreadSet(test_file_1, test_file_2)
        dss = ds1.split_movies(2)
        self.assertEqual(len(dss), 2)
        ds1 = dss[0]
        # used to get total:
        #self.assertEqual(sum(1 for _ in ds1), N_RECORDS)
        self.assertEqual(len(ds1), N_RECORDS)
        dss = ds1.split(chunks=1, zmws=True)
        self.assertEqual(len(dss), 1)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         N_RECORDS)

        dss = ds1.split(chunks=12, zmws=True)
        self.assertEqual(len(dss), 12)
        self.assertEqual(sum([len(ds_) for ds_ in dss]),
                         N_RECORDS)
        for ds in dss:
            self.assertEqual(
                ds.zmwRanges[0][0],
                'm150404_101626_42267_c100807920800000001823174110291514_s1_p0')

    @SkipTest
    def test_split_by_contigs_presplit(self):
        # Consumes too much memory for Jenkins

        # Test to make sure the result of a split by contigs has an appropriate
        # number of records (make sure filters are appropriately aggressive)
        ds2 = DataSet(data.getXml(15))
        bams = ds2.externalResources.resourceIds
        self.assertEqual(len(bams), 2)
        refwindows = ds2.refWindows
        self.assertEqual(refwindows, [(0, 0, 224992)])
        res1 = openIndexedAlignmentFile(bams[0][7:])
        res2 = openIndexedAlignmentFile(bams[1][7:])
        def count(iterable):
            count = 0
            for _ in iterable:
                count += 1
            return count
        self.assertEqual(count(res1.readsInRange(*refwindows[0])), 1409)
        self.assertEqual(count(res2.readsInRange(*refwindows[0])), 1375)
        self.assertEqual(count(ds2.readsInRange(*refwindows[0])), 2784)
        self.assertEqual(count(ds2.records), 2784)
        ds2.disableFilters()
        self.assertEqual(count(ds2.records), 53552)
        self.assertEqual(ds2.countRecords(), 53552)

    def test_split_by_contigs_with_split_and_maxChunks(self):
        # test to make sure the refWindows work when chunks == # refs
        ds3 = AlignmentSet(data.getBam())
        dss = ds3.split(contigs=True)
        self.assertEqual(len(dss), 12)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        # not all references have something mapped to them, refWindows doesn't
        # care...
        self.assertNotEqual(refWindows, sorted(ds3.refWindows))
        self.assertEqual(refWindows,
            [('B.vulgatus.4', 0, 1449), ('B.vulgatus.5', 0, 1449),
             ('C.beijerinckii.13', 0, 1433), ('C.beijerinckii.14', 0, 1433),
             ('C.beijerinckii.9', 0, 1433), ('E.coli.6', 0, 1463),
             ('E.faecalis.1', 0, 1482), ('E.faecalis.2', 0, 1482),
             ('R.sphaeroides.1', 0, 1386), ('S.epidermidis.2', 0, 1472),
             ('S.epidermidis.3', 0, 1472), ('S.epidermidis.4', 0, 1472)])
        old_refWindows = refWindows
        random_few = [('C.beijerinckii.13', 0, 1433),
                      ('B.vulgatus.4', 0, 1449),
                      ('E.faecalis.1', 0, 1482)]

        dss = ds3.split(contigs=True, maxChunks=1)
        self.assertEqual(len(dss), 1)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        self.assertEqual(refWindows, old_refWindows)

        dss = ds3.split(contigs=True, maxChunks=24)
        # This isn't expected if num refs >= 100, as map check isn't made
        # for now (too expensive)
        # There are only 12 refs represented in this set, however...
        self.assertEqual(len(dss), 12)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))

        for ref in random_few:
            found = False
            for window in refWindows:
                if ref == window:
                    found = True
            if not found:
                log.debug(ref)
            self.assertTrue(found)

        # test with maxchunks but no breaking contigs
        dss = ds3.split(contigs=True, maxChunks=36)
        self.assertEqual(len(dss), 12)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        for ref in random_few:
            found = False
            for window in refWindows:
                if ref == window:
                    found = True
            self.assertTrue(found)

        # test with maxchunks and breaking contigs is allowed (triggers
        # targetsize, may result in fewer chunks)
        dss = ds3.split(contigs=True, maxChunks=36, breakContigs=True)
        self.assertEqual(len(dss), 2)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        for ref in random_few:
            found = False
            for window in refWindows:
                if ref == window:
                    found = True
            self.assertTrue(found)

        # test with previous setup and smaller targetSize, resulting in more
        # chunks
        dss = ds3.split(contigs=True, maxChunks=36, breakContigs=True,
                        targetSize=10)
        self.assertEqual(len(dss), 9)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        for ref in random_few:
            found = False
            for window in refWindows:
                if ref == window:
                    found = True
            self.assertTrue(found)

        # test with byRecords and fewer chunks than atoms
        dss = ds3.split(contigs=True, chunks=3, byRecords=True)
        self.assertEqual(len(dss), 3)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        for ref in random_few:
            found = False
            for window in refWindows:
                if ref == window:
                    found = True
            self.assertTrue(found)

        # test with byRecords and more chunks than atoms
        orf = random_few
        random_few = [('C.beijerinckii.13', 0, 747),
                      ('B.vulgatus.4', 0, 1449),
                      ('E.faecalis.1', 0, 742)]
        dss = ds3.split(contigs=True, chunks=16, byRecords=True)
        self.assertEqual(len(dss), 16)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        for ref in random_few:
            found = False
            for window in refWindows:
                if ref == window:
                    found = True
            self.assertTrue(found)

        # test with byRecords and updateCounts
        random_few = orf
        dss = ds3.split(contigs=True, chunks=3, byRecords=True,
                        updateCounts=True)
        self.assertEqual(len(dss), 3)
        sizes = sorted([dset.numRecords for dset in dss])
        self.assertListEqual(sizes, [30, 31, 31])
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        for ref in random_few:
            found = False
            for window in refWindows:
                if ref == window:
                    found = True
            self.assertTrue(found)

        # test with byRefLength and updateCounts
        random_few = orf
        dss = ds3.split(contigs=True, chunks=3, updateCounts=True)
        self.assertEqual(len(dss), 3)
        sizes = sorted([dset.numRecords for dset in dss])
        self.assertListEqual(sizes, [20, 24, 48])
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        for ref in random_few:
            found = False
            for window in refWindows:
                if ref == window:
                    found = True
            self.assertTrue(found)

    def test_split_by_contigs_with_split(self):
        # test to make sure the refWindows work when chunks == # refs
        ds3 = AlignmentSet(data.getBam())
        dss = ds3.split(contigs=True)
        self.assertEqual(len(dss), 12)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        # not all references have something mapped to them, refWindows doesn't
        # care...
        self.assertNotEqual(refWindows, sorted(ds3.refWindows))
        random_few = [('C.beijerinckii.13', 0, 1433),
                      ('B.vulgatus.4', 0, 1449),
                      ('E.faecalis.1', 0, 1482)]
        for reference in random_few:
            found = False
            for ref in refWindows:
                if ref == reference:
                    found = True
            self.assertTrue(found)
        old_refWindows = refWindows

        dss = ds3.split(contigs=True, chunks=1)
        self.assertEqual(len(dss), 1)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        self.assertEqual(refWindows, old_refWindows)

        dss = ds3.split(contigs=True, chunks=24)
        self.assertEqual(len(dss), 24)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))

        random_few = [('E.faecalis.2', 0, 741),
                      ('E.faecalis.2', 741, 1482)]
        for ref in random_few:
            found = False
            for window in refWindows:
                if ref == window:
                    found = True
            if not found:
                log.debug(ref)
            self.assertTrue(found)

        dss = ds3.split(contigs=True, chunks=36)
        self.assertEqual(len(dss), 36)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        random_few = [('E.faecalis.2', 0, 494),
                      ('E.faecalis.2', 494, 988),
                      ('E.faecalis.2', 988, 1482)]
        for ref in random_few:
            found = False
            for window in refWindows:
                if ref == window:
                    found = True
            self.assertTrue(found)

    def test_refWindows(self):
        ds = AlignmentSet(data.getBam())
        dss = ds.split(chunks=2, contigs=True)
        self.assertEqual(len(dss), 2)
        log.debug(dss[0].filters)
        log.debug(dss[1].filters)
        self.assertTrue(
            '( rname = E.faecalis.2 '
            in str(dss[0].filters)
            or
            '( rname = E.faecalis.2 '
            in str(dss[1].filters))
        ds = AlignmentSet(data.getBam())
        ds.filters.addRequirement(rname=[('=', 'E.faecalis.2'),
                                         ('=', 'E.faecalis.2')],
                                  tStart=[('<', '99'),
                                          ('<', '299')],
                                  tEnd=[('>', '0'),
                                        ('>', '100')])
        self.assertEqual(str(ds.filters),
                         '( rname = E.faecalis.2 AND tstart '
                         '< 99 AND tend > 0 ) OR ( rname = '
                         'E.faecalis.2 AND tstart < 299 AND tend > 100 )')
        self.assertEqual(ds.refWindows, [('E.faecalis.2', 0, 99),
                                         ('E.faecalis.2', 100, 299)])


    @unittest.skip("Too expensive")
    def test_huge_zmw_split(self):
        human = ('/pbi/dept/secondary/siv/testdata/SA3-DS/'
                 'human/JCV_85x_v030/jcv_85x_v030.subreadset.xml')
        sset = SubreadSet(human)
        ssets = sset.split(zmws=True, maxChunks=5)

    @unittest.skipIf(not _internal_data(),
                     "Internal data not found, skipping")
    def test_subreadset_split_metadata_element_name(self):
        fn = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        log.debug(fn)
        sset = SubreadSet("/pbi/dept/secondary/siv/testdata/"
                          "SA3-Sequel/phi29/315/3150101/"
                          "r54008_20160219_002905/1_A01/"
                          "m54008_160219_003234.subreadset.xml")
        chunks = sset.split(chunks=5, zmws=False, ignoreSubDatasets=True)
        chunks[0].write(fn)

    def test_contigset_split(self):
        ref = ReferenceSet(data.getXml(9))
        exp_n_contigs = len(ref)
        refs = ref.split(10)
        self.assertEqual(len(refs), 10)
        obs_n_contigs = 0
        for r in refs:
            obs_n_contigs += sum(1 for _ in r)
        self.assertEqual(obs_n_contigs, exp_n_contigs)


    def test_split_hdfsubreadset(self):
        hdfds = HdfSubreadSet(*upstreamdata.getBaxH5_v23())
        self.assertEqual(len(hdfds.toExternalFiles()), 3)
        hdfdss = hdfds.split(chunks=2, ignoreSubDatasets=True)
        self.assertEqual(len(hdfdss), 2)
        self.assertEqual(len(hdfdss[0].toExternalFiles()), 2)
        self.assertEqual(len(hdfdss[1].toExternalFiles()), 1)

    @unittest.skipIf((not _internal_data() or not _check_constools()),
                     "Internal data or binaries not found, skipping")
    def test_isBarcoded(self):
        empty = upstreamdata.getEmptyBam()
        nonempty = ('/pbi/dept/secondary/siv/testdata/'
                    'pblaa-unittest/Sequel/Phi29/m54008_160219_003234'
                    '.tiny.subreadset.xml')

        # One empty one non empty
        sset = SubreadSet(nonempty, empty, skipMissing=True)
        self.assertTrue(sset.isBarcoded)

        # Just nonempty
        sset = SubreadSet(nonempty, skipMissing=True)
        self.assertEqual(len(sset), 15133)
        self.assertTrue(sset.isBarcoded)

        # Just empty
        #   This is crazy, the pbi must be out of date:
        sset = SubreadSet(empty)
        self.assertEqual(len(sset), 0)
        self.assertTrue(sset.isBarcoded)
        #   To confirm current behavior, I will regenerate the pbi with a
        #   current pbindex:
        efn = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        log.info("Copying to {}".format(efn))
        sset.copyTo(efn)
        sset.induceIndices(force=True)
        self.assertFalse(sset.isBarcoded)

    @unittest.skipIf(not _internal_data(),
                     "Internal data not found, skipping")
    def test_barcode_split_cornercases(self):
        fn = ('/pbi/dept/secondary/siv/testdata/'
              'pblaa-unittest/Sequel/Phi29/m54008_160219_003234'
              '.tiny.subreadset.xml')
        sset = SubreadSet(fn, skipMissing=True)
        ssets = sset.split(chunks=3, barcodes=True)
        self.assertEqual([str(ss.filters) for ss in ssets],
                         ["( bc = [0, 0] )",
                          "( bc = [1, 1] )",
                          "( bc = [2, 2] )"])
        sset = SubreadSet(fn, skipMissing=True)
        self.assertEqual(len(sset), 15133)
        sset.filters = None
        self.assertEqual(str(sset.filters), "")
        sset.updateCounts()
        self.assertEqual(len(sset), 2667562)

        sset.filters.addRequirement(bc=[('=', '[2, 2]')])
        self.assertEqual(str(sset.filters), "( bc = [2, 2] )")
        sset.updateCounts()
        self.assertEqual(len(sset), 4710)

        sset.filters = None
        self.assertEqual(str(sset.filters), "")
        sset.updateCounts()
        self.assertEqual(len(sset), 2667562)

        sset.filters.addRequirement(bc=[('=', '[2,2]')])
        self.assertEqual(str(sset.filters), "( bc = [2,2] )")
        sset.updateCounts()
        self.assertEqual(len(sset), 4710)

    @unittest.skipIf(not _internal_data(),
                     "Internal data not found, skipping")
    def test_barcode_split_maxChunks(self):
        fn = ('/pbi/dept/secondary/siv/testdata/'
              'pblaa-unittest/Sequel/Phi29/m54008_160219_003234'
              '.tiny.subreadset.xml')
        sset = SubreadSet(fn, skipMissing=True)
        ssets = sset.split(maxChunks=2, barcodes=True)
        self.assertEqual([str(ss.filters) for ss in ssets],
                         ["( bc = [0, 0] )",
                          "( bc = [1, 1] ) OR ( bc = [2, 2] )"])
        sset = SubreadSet(fn, skipMissing=True)
        self.assertEqual(len(sset), 15133)
        sset.filters = None
        self.assertEqual(str(sset.filters), "")
        sset.updateCounts()
        self.assertEqual(len(sset), 2667562)


        sset.filters = ssets[0].filters
        self.assertEqual(str(sset.filters), "( bc = [0, 0] )")
        sset.updateCounts()
        self.assertEqual(len(sset), 5370)

        sset.filters = None
        self.assertEqual(str(sset.filters), "")
        sset.updateCounts()
        self.assertEqual(len(sset), 2667562)

        sset.filters = ssets[1].filters
        self.assertEqual(str(sset.filters),
                         "( bc = [1, 1] ) OR ( bc = [2, 2] )")
        sset.updateCounts()
        self.assertEqual(len(sset), 9763)

