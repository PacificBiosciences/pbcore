

import logging
import tempfile
import unittest
from unittest.case import SkipTest

import numpy as np

from pbcore.io import DataSet, SubreadSet, ReferenceSet, AlignmentSet
from pbcore.io.dataset.DataSetMembers import Filters
import pbcore.data.datasets as data
import pbcore.data as upstreamdata

from utils import _pbtestdata, _check_constools, _internal_data

log = logging.getLogger(__name__)


class TestDataSetFilters(unittest.TestCase):
    """Unit and integrationt tests for the DataSet class and \
    associated module functions"""

    def test_addFilters(self):
        ds1 = DataSet()
        filt = Filters()
        filt.addRequirement(rq=[('>', '0.85')])
        ds1.addFilters(filt)
        self.assertEquals(str(ds1.filters), '( rq > 0.85 )')
        # Or added from a source XML
        ds2 = DataSet(data.getXml(16))
        self.assertTrue(str(ds2.filters).startswith(
            '( rname = E.faecalis'))

    def test_setFilters(self):
        ds1 = DataSet()
        filt = Filters()
        filt.addRequirement(rq=[('>', '0.85')])
        ds1.addFilters(filt)
        self.assertEquals(str(ds1.filters), '( rq > 0.85 )')
        # Or added from a source XML
        ds2 = DataSet()
        ds2.filters = ds1.filters
        self.assertEquals(str(ds2.filters), '( rq > 0.85 )')

    def test_add_double_bound_filters(self):
        ds1 = AlignmentSet(data.getXml(8))
        ds1.filters.addRequirement(rq=[('>', '0.85'),
                                       ('<', '0.99')])
        self.assertEquals(str(ds1.filters), '( rq > 0.85 ) OR ( rq < 0.99 )')

        ds1 = AlignmentSet(data.getXml(8))
        self.assertEquals(str(ds1.filters), '')
        ds1.filters.addFilter(rq=[('>', '0.85'),
                                  ('<', '0.99')])
        self.assertEquals(str(ds1.filters), '( rq > 0.85 AND rq < 0.99 )')

        ds1.filters.addFilter(length=[('>', '1000')])
        self.assertEquals(str(ds1.filters),
                          '( rq > 0.85 AND rq < 0.99 ) OR ( length > 1000 )')

        ds1.filters.removeFilter(0)
        self.assertEquals(str(ds1.filters),
                          '( length > 1000 )')

    def test_n_subreads_filter(self):
        ds2 = AlignmentSet(data.getXml(8))
        ds2.filters.addRequirement(n_subreads=[('>', '4')])
        self.assertEqual(len(list(ds2.records)), 87)
        self.assertEqual(len(ds2), 87)

    def test_mapqv_filter(self):
        ds2 = AlignmentSet(data.getXml(8))
        self.assertEqual(len(list(ds2.records)), 92)
        ds2.filters.addRequirement(mapqv=[('>', '128')])
        self.assertEqual(len(list(ds2.records)), 16)

    def test_filter(self):
        ds2 = AlignmentSet(data.getXml(8))
        ds2.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
        self.assertEqual(len(list(ds2.records)), 20)
        ds2.disableFilters()
        self.assertEqual(len(list(ds2.records)), 92)
        ds2.enableFilters()
        self.assertEqual(len(list(ds2.records)), 20)

    def test_broadcastFilters(self):
        # test the broadcastFilters function with different numbers of existing
        # and new filters
        filt1 = [[('zm', '<', 1000),
                  ('zm', '>', 0)]]
        filt2 = [[('zm', '<', 1000),
                  ('zm', '>', 0)],
                 [('zm', '<', 2000),
                  ('zm', '>', '1000')]]

        # no filters:
        ds0 = AlignmentSet(data.getXml(8))
        self.assertEqual(len(list(ds0.records)), 92)

        ds0.filters.broadcastFilters(filt1)
        self.assertEqual(str(ds0.filters), '( zm < 1000 AND zm > 0 )')

        ds0 = AlignmentSet(data.getXml(8))
        ds0.filters.broadcastFilters(filt2)
        self.assertEqual(
            str(ds0.filters),
            '( zm < 1000 AND zm > 0 ) OR ( zm < 2000 AND zm > 1000 )')

        # one filter:
        ds1 = AlignmentSet(data.getXml(8))
        ds1.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
        self.assertEqual(len(list(ds1.records)), 20)

        ds1.filters.broadcastFilters(filt1)
        self.assertEqual(
            str(ds1.filters),
            '( rname = E.faecalis.1 AND zm < 1000 AND zm > 0 )')

        ds1 = AlignmentSet(data.getXml(8))
        ds1.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
        ds1.filters.broadcastFilters(filt2)
        self.assertEqual(
            str(ds1.filters),
            ('( rname = E.faecalis.1 AND zm < 1000 AND zm > 0 ) OR '
             '( rname = E.faecalis.1 AND zm < 2000 AND zm > 1000 )'))

        # two filters:
        ds2 = AlignmentSet(data.getXml(8))
        ds2.filters.addRequirement(rname=[('=', 'E.faecalis.1'),
                                          ('=', 'E.faecalis.2')])
        self.assertEqual(len(list(ds2.records)), 23)

        ds2.filters.broadcastFilters(filt1)
        self.assertEqual(
            str(ds2.filters),
            ('( rname = E.faecalis.1 AND zm < 1000 AND zm > 0 ) OR '
             '( rname = E.faecalis.2 AND zm < 1000 AND zm > 0 )'))

        ds2 = AlignmentSet(data.getXml(8))
        ds2.filters.addRequirement(rname=[('=', 'E.faecalis.1'),
                                          ('=', 'E.faecalis.2')])
        ds2.filters.broadcastFilters(filt2)
        self.assertEqual(
            str(ds2.filters),
            ('( rname = E.faecalis.1 AND zm < 1000 AND zm > 0 ) OR '
             '( rname = E.faecalis.2 AND zm < 1000 AND zm > 0 ) OR '
             '( rname = E.faecalis.1 AND zm < 2000 AND zm > 1000 ) OR '
             '( rname = E.faecalis.2 AND zm < 2000 AND zm > 1000 )'))

    def test_context_filters(self):
        ss = SubreadSet(upstreamdata.getUnalignedBam())
        self.assertEqual(set(ss.index.contextFlag), {0, 1, 2, 3})
        self.assertEqual(
            [len(np.flatnonzero(ss.index.contextFlag == cx))
             for cx in sorted(set(ss.index.contextFlag))],
            [15, 33, 32, 37])
        self.assertEqual(len(ss.index), 117)

        # no adapters/barcodes
        ss.filters.addRequirement(cx=[('=', 0)])
        self.assertEqual(len(ss.index), 15)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # no adapters/barcodes
        ss.filters.addRequirement(cx=[('=', 'NO_LOCAL_CONTEXT')])
        self.assertEqual(len(ss.index), 15)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # some adapters/barcodes
        ss.filters.addRequirement(cx=[('!=', 0)])
        self.assertEqual(len(ss.index), 102)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # adapter before
        ss.filters.addRequirement(cx=[('&', 1)])
        self.assertEqual(len(ss.index), 70)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # adapter before
        ss.filters.addRequirement(cx=[('&', 'ADAPTER_BEFORE')])
        self.assertEqual(len(ss.index), 70)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # adapter after
        ss.filters.addRequirement(cx=[('&', 2)])
        self.assertEqual(len(ss.index), 69)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # adapter before or after
        ss.filters.addRequirement(cx=[('&', 3)])
        self.assertEqual(len(ss.index), 102)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # adapter before or after
        ss.filters.addRequirement(cx=[('&', 'ADAPTER_BEFORE | ADAPTER_AFTER')])
        self.assertEqual(len(ss.index), 102)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # adapter before or after but not both
        ss.filters.addRequirement(cx=[('!=', 0)])
        ss.filters.addRequirement(cx=[('~', 1),
                                      ('~', 2)])
        self.assertEqual(len(ss.index), 65)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # adapter before or after
        ss.filters.addRequirement(cx=[('&', 1),
                                      ('&', 2)])
        self.assertEqual(len(ss.index), 102)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # adapter before and after
        ss.filters.addRequirement(cx=[('&', 1)])
        ss.filters.addRequirement(cx=[('&', 2)])
        self.assertEqual(len(ss.index), 37)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # adapter before but not after
        ss.filters.addRequirement(cx=[('&', 1)])
        ss.filters.addRequirement(cx=[('~', 2)])
        self.assertEqual(len(ss.index), 33)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # no adapter before
        ss.filters.addRequirement(cx=[('~', 1)])
        self.assertEqual(len(ss.index), 47)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # no adapter before or after
        ss.filters.addRequirement(cx=[('~', 1)])
        ss.filters.addRequirement(cx=[('~', 2)])
        self.assertEqual(len(ss.index), 15)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

        # no adapter before or after
        ss.filters.addRequirement(cx=[('~', 3)])
        self.assertEqual(len(ss.index), 15)
        ss.filters.removeRequirement('cx')
        self.assertEqual(len(ss.index), 117)

    def test_filter_reference_contigs(self):
        ds2 = ReferenceSet(data.getRef())
        self.assertEqual(len(list(ds2.refNames)), 59)
        self.assertEqual(len(list(ds2.records)), len(ds2.index))
        filt = Filters()
        filt.addRequirement(id=[('==', 'E.faecalis.1')])
        ds2.addFilters(filt)
        self.assertEqual(str(ds2.filters),
                         "( id == E.faecalis.1 )")
        self.assertEqual(len(ds2.refNames), 1)
        self.assertEqual(len(list(ds2.records)), 1)
        self.assertEqual(len(list(ds2.records)), len(ds2.index))
        ds2.disableFilters()
        self.assertEqual(len(list(ds2.refNames)), 59)
        self.assertEqual(len(list(ds2.records)), 59)
        self.assertEqual(len(list(ds2.records)), len(ds2.index))
        ds2.enableFilters()
        self.assertEqual(len(list(ds2.refNames)), 1)
        self.assertEqual(len(list(ds2.records)), 1)
        self.assertEqual(len(list(ds2.records)), len(ds2.index))

    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_qname_filter_scaling(self):
        # unaligned bam
        bam0 = ("/pbi/dept/secondary/siv/testdata/"
                "SA3-DS/ecoli/2590956/0003/"
                "Analysis_Results/m140913_222218_42240_c10069"
                "9952400000001823139203261564_s1_p0.all.subreadset.xml")
        bam1 = ("/pbi/dept/secondary/siv/testdata/"
                "SA3-DS/ecoli/2590953/0001/"
                "Analysis_Results/m140913_005018_42139_c10071"
                "3652400000001823152404301534_s1_p0.all.subreadset.xml")
        sset = SubreadSet(bam0, bam1)
        self.assertEqual(len(sset), 178570)
        size = 10
        qn = [r.qName for r in sset[:size]]
        good_qn = [('=', name) for name in qn]
        sset.filters.addRequirement(qname=good_qn)
        self.assertEqual(size, sum(1 for _ in sset))
        self.assertEqual(size, len(sset))


        sset = SubreadSet(data.getXml(10))
        self.assertEqual(len(sset), 92)
        size = 10
        qn = [r.qName for r in sset[:size]]
        good_qn = [('=', name) for name in qn]
        sset.filters.addRequirement(qname=good_qn)
        self.assertEqual(size, sum(1 for _ in sset))
        self.assertEqual(size, len(sset))


    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_movie_filter(self):
        # unaligned bam
        bam0 = ("/pbi/dept/secondary/siv/testdata/"
                "SA3-DS/ecoli/2590956/0003/"
                "Analysis_Results/m140913_222218_42240_c10069"
                "9952400000001823139203261564_s1_p0.all.subreadset.xml")
        bam1 = ("/pbi/dept/secondary/siv/testdata/"
                "SA3-DS/ecoli/2590953/0001/"
                "Analysis_Results/m140913_005018_42139_c10071"
                "3652400000001823152404301534_s1_p0.all.subreadset.xml")
        aln = SubreadSet(bam0, bam1)
        self.assertEqual(len(set(aln.readGroupTable['ID'])),
                         len(aln.readGroupTable['ID']))
        self.assertEqual(len(set(aln.readGroupTable['ID'])), 2)
        self.assertEqual(len(set(aln.readGroupTable['ID'])),
                         len(set(aln.index.qId)))
        self.assertEqual(len(aln), 178570)
        aln.filters.addRequirement(movie=[(
            '=',
            'm140913_005018_42139_c100713652400000001823152404301534_s1_p0')])
        self.assertEqual(len(SubreadSet(bam1)), len(aln))

        # aligned bam
        #bam0 = ("/pbi/dept/secondary/siv/testdata/"
        #        "SA3-DS/ecoli/2590956/0003/Alignment_Results/"
        #        "m140913_222218_42240_c1006999524000000018231"
        #        "39203261564_s1_p0.all.alignmentset.xml")
        bam0 = upstreamdata.getBamAndCmpH5()[0]
        bam1 = ("/pbi/dept/secondary/siv/testdata/"
                "SA3-DS/ecoli/2590953/0001/Alignment_Results/"
                "m140913_005018_42139_c1007136524000000018231"
                "52404301534_s1_p0.all.alignmentset.xml")
        aln = AlignmentSet(bam0, bam1)
        self.assertEqual(len(set(aln.readGroupTable['ID'])),
                         len(aln.readGroupTable['ID']))
        self.assertEqual(len(set(aln.readGroupTable['ID'])), 2)
        self.assertEqual(len(set(aln.readGroupTable['ID'])),
                         len(set(aln.index.qId)))
        self.assertEqual(len(aln), 103144)
        aln.filters.addRequirement(movie=[(
            '=',
            'm140913_005018_42139_c100713652400000001823152404301534_s1_p0')])
        self.assertEqual(len(AlignmentSet(bam1)), len(aln))

        # cmpH5
        cmp1 = upstreamdata.getBamAndCmpH5()[1]
        cmp2 = ("/pbi/dept/secondary/siv/testdata/"
                "genomic_consensus-unittest/bam_c4p6_tests/"
                "ecoli_c4p6.cmp.h5")
        aln = AlignmentSet(cmp1, cmp2)
        self.assertEqual(len(set(aln.readGroupTable['ID'])),
                         len(aln.readGroupTable['ID']))
        self.assertEqual(len(set(aln.readGroupTable['ID'])),
                         len(set(aln.index.MovieID)))
        self.assertEqual(len(set(aln.readGroupTable['ID'])), 2)
        self.assertEqual(len(aln), 57147)
        aln.filters.addRequirement(movie=[(
            '=',
            'm140905_042212_sidney_c100564852550000001823085912221377_s1_X0')])
        len1 = len(AlignmentSet(cmp1))
        self.assertEqual(len1, len(aln))

        aln.filters.removeRequirement('movie')
        self.assertEqual(len(aln), 57147)

    def test_accuracy_filter(self):
        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        aln.filters.addRequirement(accuracy=[('>', '.85')])
        self.assertEqual(len(list(aln)), 174)

    def test_membership_filter(self):
        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        hns = np.unique(aln.index.holeNumber)[:1]
        aln.filters.addRequirement(zm=[('in', hns)])
        self.assertEqual(len(list(aln)), 5)

        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        hns = np.unique(aln.index.holeNumber)
        aln.filters.addRequirement(zm=[('in', hns)])
        self.assertEqual(len(list(aln)), 177)

        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        hns = np.unique(aln.index.holeNumber)
        hns = [n for _ in range(10000) for n in hns]
        hns = np.array(hns)
        aln.filters.addRequirement(zm=[('in', hns)])
        self.assertEqual(len(list(aln)), 177)

        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        hns = np.unique(aln.index.holeNumber)[:1]
        hns = list(hns)
        aln.filters.addRequirement(zm=[('in', hns)])
        self.assertEqual(len(list(aln)), 5)

        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        hns = np.unique(aln.index.holeNumber)[:1]
        hns = set(hns)
        aln.filters.addRequirement(zm=[('in', hns)])
        self.assertEqual(len(list(aln)), 5)

        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        qnames = [r.qName for r in aln[:10]]
        aln.filters.addRequirement(qname=[('in', qnames)])
        self.assertEqual(len(list(aln)), 10)

        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        qnames = [r.qName for r in aln[:1]]
        aln.filters.addRequirement(qname=[('in', qnames)])
        self.assertEqual(len(list(aln)), 1)

        fn = tempfile.NamedTemporaryFile(suffix="alignmentset.xml").name
        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        hns = np.unique(aln.index.holeNumber)[:1]
        aln.filters.addRequirement(zm=[('in', hns)])
        aln.write(fn)
        aln.close()
        aln2 = AlignmentSet(fn)
        self.assertEqual(len(list(aln2)), 5)

    def test_membership_filter_with_equal_operator(self):
        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        hns = np.unique(aln.index.holeNumber)[:1]
        aln.filters.addRequirement(zm=[('=', hns)])
        self.assertEqual(len(list(aln)), 5)

        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        hns = np.unique(aln.index.holeNumber)
        aln.filters.addRequirement(zm=[('==', hns)])
        self.assertEqual(len(list(aln)), 177)

        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        hns = np.unique(aln.index.holeNumber)
        hns = [n for _ in range(10000) for n in hns]
        hns = np.array(hns)
        aln.filters.addRequirement(zm=[('==', hns)])
        self.assertEqual(len(list(aln)), 177)

        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        hns = np.unique(aln.index.holeNumber)[:1]
        hns = list(hns)
        aln.filters.addRequirement(zm=[('==', hns)])
        self.assertEqual(len(list(aln)), 5)

        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        hns = np.unique(aln.index.holeNumber)[:1]
        hns = set(hns)
        aln.filters.addRequirement(zm=[('==', hns)])
        self.assertEqual(len(list(aln)), 5)

        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        qnames = [r.qName for r in aln[:10]]
        aln.filters.addRequirement(qname=[('==', qnames)])
        self.assertEqual(len(list(aln)), 10)

        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        qnames = [r.qName for r in aln[:1]]
        aln.filters.addRequirement(qname=[('==', qnames)])
        self.assertEqual(len(list(aln)), 1)

        fn = tempfile.NamedTemporaryFile(suffix="alignmentset.xml").name
        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        hns = np.unique(aln.index.holeNumber)[:1]
        aln.filters.addRequirement(zm=[('==', hns)])
        aln.write(fn)
        aln.close()
        aln2 = AlignmentSet(fn)
        self.assertEqual(len(list(aln2)), 5)

    def test_contigset_filter(self):
        ref = ReferenceSet(data.getXml(9))
        self.assertEqual(len(list(ref)), 59)
        ref.filters.addRequirement(length=[('>', '1450')])
        self.assertEqual(len(list(ref)), 34)

    def test_cmp_alignmentset_filters(self):
        aln = AlignmentSet(upstreamdata.getBamAndCmpH5()[1], strict=True)
        self.assertEqual(len(aln), 112)
        aln.filters.addRequirement(length=[('>=', 1000)])
        self.assertEqual(len(aln), 12)
