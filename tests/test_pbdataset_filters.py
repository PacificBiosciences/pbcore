import logging
import numpy as np
import pytest
import tempfile

from pbcore.io import (DataSet, SubreadSet, ReferenceSet, AlignmentSet,
                       ConsensusReadSet)
from pbcore.io.dataset.DataSetMembers import (Filters, recordMembership,
                                              qnames2recarrays_by_size)
import pbcore.data.datasets as data
import pbcore.data as upstreamdata

log = logging.getLogger(__name__)


class TestDataSetFilters(object):
    """Unit and integrationt tests for the DataSet class and \
    associated module functions"""

    def test_addFilters(self):
        ds1 = DataSet()
        filt = Filters()
        filt.addRequirement(rq=[('>', '0.85')])
        ds1.addFilters(filt)
        assert str(ds1.filters) == '( rq > 0.85 )'
        # Or added from a source XML
        ds2 = DataSet(data.getXml(15))
        assert str(ds2.filters).startswith('( rname = E.faecalis')

    def test_setFilters(self):
        ds1 = DataSet()
        filt = Filters()
        filt.addRequirement(rq=[('>', '0.85')])
        ds1.addFilters(filt)
        assert str(ds1.filters) == '( rq > 0.85 )'
        # Or added from a source XML
        ds2 = DataSet()
        ds2.filters = ds1.filters
        assert str(ds2.filters) == '( rq > 0.85 )'

    def test_add_double_bound_filters(self):
        ds1 = AlignmentSet(data.getXml(7))
        ds1.filters.addRequirement(rq=[('>', '0.85'),
                                       ('<', '0.99')])
        assert str(ds1.filters) == '( rq > 0.85 ) OR ( rq < 0.99 )'

        ds1 = AlignmentSet(data.getXml(7))
        assert str(ds1.filters) == ''
        ds1.filters.addFilter(rq=[('>', '0.85'),
                                  ('<', '0.99')])
        assert str(ds1.filters) == '( rq > 0.85 AND rq < 0.99 )'

        ds1.filters.addFilter(length=[('>', '1000')])
        assert  str(ds1.filters) == '( rq > 0.85 AND rq < 0.99 ) OR ( length > 1000 )'

        ds1.filters.removeFilter(0)
        assert str(ds1.filters) == '( length > 1000 )'

    def test_n_subreads_filter(self):
        ds2 = AlignmentSet(data.getXml(7))
        ds2.filters.addRequirement(n_subreads=[('>', '4')])
        assert len(list(ds2.records)) == 87
        assert len(ds2) == 87

    def test_subset_filter(self):
        ds2 = AlignmentSet(data.getXml(7))
        assert len(ds2) == 92
        modvalue = 8

        # manually:
        hns = ds2.index.holeNumber
        assert np.count_nonzero(hns % modvalue == 0) == 26

        # dset filters:
        ds2.filters.addRequirement(zm=[('=', '0', modvalue)])
        assert len(ds2) == 26

        # written:
        filtstr = '( Uint32Cast(zm) % 8 = 0 )'
        assert str(ds2.filters) == filtstr

        filtxmlstr = ('<pbbase:Property Hash="Uint32Cast" Modulo="8" '
                      'Name="zm" Operator="=" Value="0"/>')
        fn = tempfile.NamedTemporaryFile(suffix="alignmentset.xml").name
        ds2.write(fn)
        with open(fn, 'r') as ifh:
            found = False
            for line in ifh:
                if filtxmlstr in line:
                    found = True
        assert found

    def test_mapqv_filter(self):
        ds2 = AlignmentSet(data.getXml(7))
        assert len(list(ds2.records)) == 92
        ds2.filters.addRequirement(mapqv=[('>', '128')])
        assert len(list(ds2.records)) == 16

    def test_filter(self):
        ds2 = AlignmentSet(data.getXml(7))
        ds2.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
        assert len(list(ds2.records)) == 20
        ds2.disableFilters()
        assert len(list(ds2.records)) == 92
        ds2.enableFilters()
        assert len(list(ds2.records)) == 20

    def test_broadcastFilters(self):
        # test the broadcastFilters function with different numbers of existing
        # and new filters
        filt1 = [[('zm', '<', 1000),
                  ('zm', '>', 0)]]
        filt2 = [[('zm', '<', 1000),
                  ('zm', '>', 0)],
                 [('zm', '<', 2000),
                  ('zm', '>', '1000')]]

        # no new filters, no existing:
        ds0 = AlignmentSet(data.getXml(7))
        ds0.filters.broadcastFilters([])
        assert str(ds0.filters) == ''
        assert len(list(ds0.records)) == 92

        # no new filters, one existing:
        ds0 = AlignmentSet(data.getXml(7))
        ds0.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
        assert str(ds0.filters) == '( rname = E.faecalis.1 )'
        assert len(list(ds0.records)) == 20
        ds0.filters.broadcastFilters([])
        assert str(ds0.filters) == '( rname = E.faecalis.1 )'
        assert len(list(ds0.records)) == 20

        # no existing filters:
        ds0 = AlignmentSet(data.getXml(7))
        assert len(list(ds0.records)) == 92

        ds0.filters.broadcastFilters(filt1)
        assert str(ds0.filters) == '( zm < 1000 AND zm > 0 )'

        ds0 = AlignmentSet(data.getXml(7))
        ds0.filters.broadcastFilters(filt2)
        assert str(ds0.filters) == '( zm < 1000 AND zm > 0 ) OR ( zm < 2000 AND zm > 1000 )'

        # one filter:
        ds1 = AlignmentSet(data.getXml(7))
        ds1.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
        assert len(list(ds1.records)) == 20

        ds1.filters.broadcastFilters(filt1)
        assert str(ds1.filters) == '( rname = E.faecalis.1 AND zm < 1000 AND zm > 0 )'

        ds1 = AlignmentSet(data.getXml(7))
        ds1.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
        ds1.filters.broadcastFilters(filt2)
        assert str(ds1.filters) == (
             '( rname = E.faecalis.1 AND zm < 1000 AND zm > 0 ) OR '
             '( rname = E.faecalis.1 AND zm < 2000 AND zm > 1000 )')

        # two filters:
        ds2 = AlignmentSet(data.getXml(7))
        ds2.filters.addRequirement(rname=[('=', 'E.faecalis.1'),
                                          ('=', 'E.faecalis.2')])
        assert len(list(ds2.records)) == 23

        ds2.filters.broadcastFilters(filt1)
        assert str(ds2.filters) == (
             '( rname = E.faecalis.1 AND zm < 1000 AND zm > 0 ) OR '
             '( rname = E.faecalis.2 AND zm < 1000 AND zm > 0 )')

        ds2 = AlignmentSet(data.getXml(7))
        ds2.filters.addRequirement(rname=[('=', 'E.faecalis.1'),
                                          ('=', 'E.faecalis.2')])
        ds2.filters.broadcastFilters(filt2)
        assert str(ds2.filters) == (
             '( rname = E.faecalis.1 AND zm < 1000 AND zm > 0 ) OR '
             '( rname = E.faecalis.2 AND zm < 1000 AND zm > 0 ) OR '
             '( rname = E.faecalis.1 AND zm < 2000 AND zm > 1000 ) OR '
             '( rname = E.faecalis.2 AND zm < 2000 AND zm > 1000 )')

    def test_context_filters(self):
        ss = SubreadSet(upstreamdata.getUnalignedBam())
        assert set(ss.index.contextFlag) == {0, 1, 2, 3}
        assert [len(np.flatnonzero(ss.index.contextFlag == cx))
                for cx in sorted(set(ss.index.contextFlag))] == [15, 33, 32, 37]
        assert len(ss.index) == 117

        # no adapters/barcodes
        ss.filters.addRequirement(cx=[('=', 0)])
        assert len(ss.index) == 15
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # no adapters/barcodes
        ss.filters.addRequirement(cx=[('=', 'NO_LOCAL_CONTEXT')])
        assert len(ss.index) == 15
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # some adapters/barcodes
        ss.filters.addRequirement(cx=[('!=', 0)])
        assert len(ss.index) == 102
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # adapter before
        ss.filters.addRequirement(cx=[('&', 1)])
        assert len(ss.index) == 70
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # adapter before
        ss.filters.addRequirement(cx=[('&', 'ADAPTER_BEFORE')])
        assert len(ss.index) == 70
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # adapter after
        ss.filters.addRequirement(cx=[('&', 2)])
        assert len(ss.index) == 69
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # adapter before or after
        ss.filters.addRequirement(cx=[('&', 3)])
        assert len(ss.index) == 102
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # adapter before or after
        ss.filters.addRequirement(cx=[('&', 'ADAPTER_BEFORE | ADAPTER_AFTER')])
        assert len(ss.index) == 102
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # adapter before or after but not both
        ss.filters.addRequirement(cx=[('!=', 0)])
        ss.filters.addRequirement(cx=[('~', 1),
                                      ('~', 2)])
        assert len(ss.index) == 65
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # adapter before or after
        ss.filters.addRequirement(cx=[('&', 1),
                                      ('&', 2)])
        assert len(ss.index) == 102
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # adapter before and after
        ss.filters.addRequirement(cx=[('&', 1)])
        ss.filters.addRequirement(cx=[('&', 2)])
        assert len(ss.index) == 37
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # adapter before but not after
        ss.filters.addRequirement(cx=[('&', 1)])
        ss.filters.addRequirement(cx=[('~', 2)])
        assert len(ss.index) == 33
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # no adapter before
        ss.filters.addRequirement(cx=[('~', 1)])
        assert len(ss.index) == 47
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # no adapter before or after
        ss.filters.addRequirement(cx=[('~', 1)])
        ss.filters.addRequirement(cx=[('~', 2)])
        assert len(ss.index) == 15
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

        # no adapter before or after
        ss.filters.addRequirement(cx=[('~', 3)])
        assert len(ss.index) == 15
        ss.filters.removeRequirement('cx')
        assert len(ss.index) == 117

    def test_filter_reference_contigs(self):
        ds2 = ReferenceSet(data.getRef())
        assert len(list(ds2.refNames)) == 59
        assert len(list(ds2.records)) == len(ds2.index)
        filt = Filters()
        filt.addRequirement(id=[('==', 'E.faecalis.1')])
        ds2.addFilters(filt)
        assert str(ds2.filters) == "( id == E.faecalis.1 )"
        assert len(ds2.refNames) == 1
        assert len(list(ds2.records)) == 1
        assert len(list(ds2.records)) == len(ds2.index)
        ds2.disableFilters()
        assert len(list(ds2.refNames)) == 59
        assert len(list(ds2.records)) == 59
        assert len(list(ds2.records)) == len(ds2.index)
        ds2.enableFilters()
        assert len(list(ds2.refNames)) == 1
        assert len(list(ds2.records)) == 1
        assert len(list(ds2.records)) == len(ds2.index)

    def test_recordMembership(self):
        # This dtype doesn't have to be exactly realistic, just internally
        # consistent for the test:
        dtype = [('qId', int), ('holenumber', int), ('qStart', int),
                 ('qEnd', int)]
        records = ['c1/0/0_10', 'c1/0/10_20', 'c1/1/0_10', 'c1/1/10_20']
        whitelist = ['c1/0/10_20', 'c1/1/0_10']
        blacklist = ['c1/1/0_10']

        records = qnames2recarrays_by_size(records, {'c1':1}, dtype)[4]
        whitelist = qnames2recarrays_by_size(whitelist, {'c1':1}, dtype)[4]
        blacklist = qnames2recarrays_by_size(blacklist, {'c1':1}, dtype)[4]

        assert np.count_nonzero(recordMembership(records, whitelist)) == 2
        assert np.count_nonzero(recordMembership(records, blacklist)) == 1
        assert np.count_nonzero(~recordMembership(records, blacklist)) == 3

        # test partial qnames

        records = ['c1/0/0_10', 'c1/0/10_20', 'c1/1/0_10', 'c1/1/10_20']
        whitelist = ['c1/0']
        blacklist = ['c1/1']

        records = qnames2recarrays_by_size(records, {'c1':1}, dtype)[4]
        whitelist = qnames2recarrays_by_size(whitelist, {'c1':1}, dtype)[2]
        blacklist = qnames2recarrays_by_size(blacklist, {'c1':1}, dtype)[2]

        assert np.count_nonzero(recordMembership(records, whitelist)) == 2
        assert np.count_nonzero(recordMembership(records, blacklist)) == 2
        assert np.count_nonzero(~recordMembership(records, blacklist)) == 2

        # test a mix of partial qnames

        records = ['c1/0/0_10', 'c1/0/10_20', 'c1/1/0_10', 'c1/1/10_20']
        whitelist = ['c1/0', 'c1/1/0_10']
        blacklist = ['c1/0/0_10', 'c1/1']

        records = qnames2recarrays_by_size(records, {'c1':1}, dtype)[4]
        whitelist = qnames2recarrays_by_size(whitelist, {'c1':1}, dtype)
        blacklist = qnames2recarrays_by_size(blacklist, {'c1':1}, dtype)

        whitelist_mask = recordMembership(records, whitelist[2])
        blacklist_mask = recordMembership(records, blacklist[2])
        whitelist_mask |= recordMembership(records, whitelist[4])
        blacklist_mask |= recordMembership(records, blacklist[4])

        assert np.count_nonzero(whitelist_mask) == 3
        assert np.count_nonzero(blacklist_mask) == 3
        assert np.count_nonzero(~blacklist_mask) == 1

    def test_file_arg(self):
        fn = tempfile.NamedTemporaryFile(suffix="filterVals.txt").name
        log.debug(fn)
        sset = SubreadSet(data.getXml(9))
        assert len(sset) == 92
        size = 10
        qn = [r.qName for r in sset[:size]]
        with open(fn, 'w') as ofh:
            for q in qn:
                ofh.write(q)
                ofh.write('\n')
        good_qn = [('=', fn)]
        sset.filters.addRequirement(qname=good_qn)
        assert size == sum(1 for _ in sset)
        assert size == len(sset)
        og = set(qn)
        for r in sset:
            og.discard(r.qName)
        assert len(og) == 0

        fn = tempfile.NamedTemporaryFile(suffix="filterVals.txt").name
        log.debug(fn)
        sset = SubreadSet(data.getXml(9))
        assert len(sset) == 92
        size = 10
        qn = [r.qName for r in sset[:size]]
        with open(fn, 'w') as ofh:
            for q in qn:
                ofh.write(q)
                ofh.write('\n')
        good_qn = [('=', fn)]
        sset.filters.addRequirement(qname_file=good_qn)
        assert size == sum(1 for _ in sset)
        assert size == len(sset)
        og = set(qn)
        for r in sset:
            og.discard(r.qName)
        assert len(og) == 0

        fn = tempfile.NamedTemporaryFile(suffix="filterVals.txt").name
        log.debug(fn)
        sset = SubreadSet(data.getXml(9))
        assert len(sset) == 92
        size = 4
        hn = [r
              for r in sorted(list(set(sset.index.holeNumber)))[:size]]
        with open(fn, 'w') as ofh:
            for h in hn:
                ofh.write(str(h))
                ofh.write('\n')
        good_hn = [('=', fn)]
        sset.filters.addRequirement(zm=good_hn)
        assert size == len(set(sset.index.holeNumber))
        og = set(hn)
        for r in sset:
            og.discard(r.holeNumber)
        assert len(og) == 0

    @pytest.mark.internal_data
    def test_qname_css(self):
        fn = ('/pbi/dept/secondary/siv/testdata/ccs-unittest/'
              'tiny/little.ccs.bam')
        sset = ConsensusReadSet(fn)

        assert len(sset) == 14
        size = 4
        qn = [r.qName for r in sset[:size]]
        good_qn = [('=', qn)]
        sset.filters.addRequirement(qname=good_qn)
        assert size == sum(1 for _ in sset)
        assert size == len(sset)

    def test_not_in_filter(self):
        nreads = 92
        fn = tempfile.NamedTemporaryFile(suffix="filterVals.txt").name
        log.debug(fn)
        sset = SubreadSet(data.getXml(9))
        nzmws = len(set(sset.index.holeNumber))
        assert len(sset) == nreads
        size = 10
        qn = [r.qName for r in sset[:size]]
        with open(fn, 'w') as ofh:
            for q in qn:
                ofh.write(q)
                ofh.write('\n')
        good_qn = [('!=', fn)]
        sset.filters.addRequirement(qname=good_qn)
        assert nreads - size == sum(1 for _ in sset)
        assert nreads - size == len(sset)
        og = set(qn)
        for r in sset:
            og.discard(r.qName)
        assert len(og) == size

        fn = tempfile.NamedTemporaryFile(suffix="filterVals.txt").name
        log.debug(fn)
        sset = SubreadSet(data.getXml(9))
        assert len(sset) == nreads
        size = 4
        hn = [r
              for r in sorted(list(set(sset.index.holeNumber)))[:size]]
        with open(fn, 'w') as ofh:
            for h in hn:
                ofh.write(str(h))
                ofh.write('\n')
        good_hn = [('!=', fn)]
        sset.filters.addRequirement(zm=good_hn)
        assert nzmws - size == len(set(sset.index.holeNumber))
        og = set(hn)
        for r in sset:
            og.discard(r.holeNumber)
        assert len(og) == size

    @pytest.mark.internal_data
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

        # separate '==' takes 120 seconds to addReq for 10k qnames:
        """
        sset = SubreadSet(bam0, bam1)
        assert len(sset) == 178570
        size = 100
        qn = [r.qName for r in sset[:size]]
        good_qn = [('=', name) for name in qn]
        sset.filters.addRequirement(qname=good_qn)
        #assert size == sum(1 for _ in sset)
        assert size == len(sset)

        sset = SubreadSet(data.getXml(9))
        assert len(sset) == 92
        size = 10
        qn = [r.qName for r in sset[:size]]
        good_qn = [('=', name) for name in qn]
        sset.filters.addRequirement(qname=good_qn)
        assert size == sum(1 for _ in sset)
        assert size == len(sset)
        """

        # "in" takes 1.2 seconds to addReq for 10k qnames:

        sset = SubreadSet(bam0, bam1)
        assert len(sset) == 178570
        size = 100
        qn = [r.qName for r in sset[:size]]
        good_qn = [('=', qn)]
        sset.filters.addRequirement(qname=good_qn)
        #assert size == sum(1 for _ in sset)
        assert size == len(sset)

        sset = SubreadSet(data.getXml(9))
        assert len(sset) == 92
        size = 10
        qn = [r.qName for r in sset[:size]]
        good_qn = [('=', qn)]
        sset.filters.addRequirement(qname=good_qn)
        assert size == sum(1 for _ in sset)
        assert size == len(sset)

    @pytest.mark.internal_data
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
        assert len(set(aln.readGroupTable['ID'])) == len(aln.readGroupTable['ID'])
        assert len(set(aln.readGroupTable['ID'])) == 2
        assert len(set(aln.readGroupTable['ID'])) == len(set(aln.index.qId))
        assert len(aln) == 178570
        aln.filters.addRequirement(movie=[(
            '=',
            'm140913_005018_42139_c100713652400000001823152404301534_s1_p0')])
        assert len(SubreadSet(bam1)) == len(aln)

        # aligned bam
        #bam0 = ("/pbi/dept/secondary/siv/testdata/"
        #        "SA3-DS/ecoli/2590956/0003/Alignment_Results/"
        #        "m140913_222218_42240_c1006999524000000018231"
        #        "39203261564_s1_p0.all.alignmentset.xml")
        bam0 = upstreamdata.getAlignedBam()
        bam1 = ("/pbi/dept/secondary/siv/testdata/"
                "SA3-DS/ecoli/2590953/0001/Alignment_Results/"
                "m140913_005018_42139_c1007136524000000018231"
                "52404301534_s1_p0.all.alignmentset.xml")
        aln = AlignmentSet(bam0, bam1)
        assert len(set(aln.readGroupTable['ID'])) == len(aln.readGroupTable['ID'])
        assert len(set(aln.readGroupTable['ID'])) == 2
        assert len(set(aln.readGroupTable['ID'])) == len(set(aln.index.qId))
        assert len(aln) == 103144
        aln.filters.addRequirement(movie=[(
            '=',
            'm140913_005018_42139_c100713652400000001823152404301534_s1_p0')])
        assert len(AlignmentSet(bam1)) == len(aln)

    def test_accuracy_filter(self):
        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        aln.filters.addRequirement(accuracy=[('>', '.85')])
        assert len(list(aln)) == 174

    def test_membership_filter(self):
        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        hns = np.unique(aln.index.holeNumber)[:1]
        aln.filters.addRequirement(zm=[('in', hns)])
        assert len(list(aln)) == 5

        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        hns = np.unique(aln.index.holeNumber)
        aln.filters.addRequirement(zm=[('in', hns)])
        assert len(list(aln)) == 177

        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        hns = np.unique(aln.index.holeNumber)
        hns = [n for _ in range(10000) for n in hns]
        hns = np.array(hns)
        aln.filters.addRequirement(zm=[('in', hns)])
        assert len(list(aln)) == 177

        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        hns = np.unique(aln.index.holeNumber)[:1]
        hns = list(hns)
        aln.filters.addRequirement(zm=[('in', hns)])
        assert len(list(aln)) == 5

        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        hns = np.unique(aln.index.holeNumber)[:1]
        hns = set(hns)
        aln.filters.addRequirement(zm=[('in', hns)])
        assert len(list(aln)) == 5

        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        qnames = [r.qName for r in aln[:10]]
        aln.filters.addRequirement(qname=[('in', qnames)])
        assert len(list(aln)) == 10

        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        qnames = [r.qName for r in aln[:1]]
        aln.filters.addRequirement(qname=[('in', qnames)])
        assert len(list(aln)) == 1

        # test partial qnames:
        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        qnames = ['/'.join(r.qName.split('/')[:2]) for r in aln[:1]]
        assert qnames == ['pbalchemy1GbRSIIsim0/6']
        aln.filters.addRequirement(qname=[('in', qnames)])
        assert len(list(aln)) == 7

        fn = tempfile.NamedTemporaryFile(suffix="alignmentset.xml").name
        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        hns = np.unique(aln.index.holeNumber)[:1]
        aln.filters.addRequirement(zm=[('in', hns)])
        aln.write(fn)
        aln.close()
        aln2 = AlignmentSet(fn)
        assert len(list(aln2)) == 5

    def test_membership_filter_with_equal_operator(self):
        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        hns = np.unique(aln.index.holeNumber)[:1]
        aln.filters.addRequirement(zm=[('=', hns)])
        assert len(list(aln)) == 5

        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        hns = np.unique(aln.index.holeNumber)
        aln.filters.addRequirement(zm=[('==', hns)])
        assert len(list(aln)) == 177

        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        hns = np.unique(aln.index.holeNumber)
        hns = [n for _ in range(10000) for n in hns]
        hns = np.array(hns)
        aln.filters.addRequirement(zm=[('==', hns)])
        assert len(list(aln)) == 177

        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        hns = np.unique(aln.index.holeNumber)[:1]
        hns = list(hns)
        aln.filters.addRequirement(zm=[('==', hns)])
        assert len(list(aln)) == 5

        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        hns = np.unique(aln.index.holeNumber)[:1]
        hns = set(hns)
        aln.filters.addRequirement(zm=[('==', hns)])
        assert len(list(aln)) == 5

        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        qnames = [r.qName for r in aln[:10]]
        aln.filters.addRequirement(qname=[('==', qnames)])
        assert len(list(aln)) == 10

        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        qnames = [r.qName for r in aln[:1]]
        aln.filters.addRequirement(qname=[('==', qnames)])
        assert len(list(aln)) == 1

        fn = tempfile.NamedTemporaryFile(suffix="alignmentset.xml").name
        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        hns = np.unique(aln.index.holeNumber)[:1]
        aln.filters.addRequirement(zm=[('==', hns)])
        aln.write(fn)
        aln.close()
        aln2 = AlignmentSet(fn)
        assert len(list(aln2)) == 5

    def test_contigset_filter(self):
        ref = ReferenceSet(data.getXml(8))
        assert len(list([seq for seq in ref])) == 59
        ref.filters.addRequirement(length=[('>', '1450')])
        assert len(list([seq for seq in ref])) == 34
