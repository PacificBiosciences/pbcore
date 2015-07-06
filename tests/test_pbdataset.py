
import os
import re
import logging
import tempfile

import numpy as np
import unittest
from unittest.case import SkipTest

from pbcore.io import openIndexedAlignmentFile
from pbcore.io import DataSet, SubreadSet, ReferenceSet, AlignmentSet
from pbcore.io.dataset.DataSetMembers import ExternalResource, Filters
from pbcore.io.dataset.DataSetValidator import validateFile
import pbcore.data.datasets as data

log = logging.getLogger(__name__)

class TestDataSet(unittest.TestCase):
    """Unit and integrationt tests for the DataSet class and \
    associated module functions"""

    def test_build(self):
        # Progs like pbalign provide a .bam file:
        # e.g. d = DataSet("aligned.bam")
        # Something like the test files we have:
        inBam = data.getBam()
        self.assertTrue(inBam.endswith('.bam'))
        d = DataSet(inBam)
        # A UniqueId is generated, despite being a BAM input
        self.assertTrue(d.uuid != '')
        dOldUuid = d.uuid
        # They can write this BAM to an XML:
        # e.g. d.write("alignmentset.xml")
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outXml = os.path.join(outdir, 'tempfile.xml')
        d.write(outXml)
        # And then recover the same XML (or a different one):
        # e.g. d = DataSet("alignmentset.xml")
        d = DataSet(outXml)
        # The UniqueId will be the same
        self.assertTrue(d.uuid == dOldUuid)
        # Inputs can be many and varied
        ds1 = DataSet(data.getXml(no=0), data.getXml(no=1), data.getBam())
        self.assertEquals(ds1.numExternalResources, 5)
        ds1 = DataSet(data.getFofn())
        self.assertEquals(ds1.numExternalResources, 5)
        # DataSet types are autodetected:
        self.assertEquals(type(DataSet(data.getSubreadSet())).__name__,
                          'SubreadSet')
        # But can also be used directly
        self.assertEquals(type(SubreadSet(data.getSubreadSet())).__name__,
                          'SubreadSet')
        # Even with untyped inputs
        self.assertTrue(str(SubreadSet(data.getBam())).startswith(
            '<SubreadSet'))
        self.assertEquals(type(SubreadSet(data.getBam())).__name__,
                          'SubreadSet')
        self.assertEquals(type(DataSet(data.getBam())).__name__,
                          'DataSet')
        # You can also cast up and down, but casting between siblings
        # is limited (abuse at your own risk)
        self.assertEquals(
            type(DataSet(data.getBam()).copy(asType='SubreadSet')).__name__,
            'SubreadSet')
        self.assertEquals(
            type(SubreadSet(data.getBam()).copy(asType='DataSet')).__name__,
            'DataSet')
        # Add external Resources:
        ds = DataSet()
        ds.externalResources.addResources(["IdontExist.bam"])
        self.assertTrue(
            ds.externalResources[-1].resourceId == "IdontExist.bam")
        # Add an index file
        ds.externalResources[-1].addIndices(["IdontExist.bam.pbi"])
        self.assertTrue(
            ds.externalResources[-1].indices[0].resourceId ==
            "IdontExist.bam.pbi")


    def test_empty_metatype(self):
        inBam = data.getBam()
        d = DataSet(inBam)
        for extRes in d.externalResources:
            self.assertEqual(extRes.metaType, "")

    def test_updateCounts(self):
        log.info("Testing updateCounts without filters")
        ds = DataSet(data.getXml(16))
        also_lambda = ds.toExternalFiles()[0]
        aln = AlignmentSet(data.getBam(0), data.getBam(1), also_lambda)
        readers = aln.resourceReaders()

        expLen = 0
        for reader in readers:
            for record in reader:
                expLen += record.readLength

        expNum = 0
        for reader in readers:
            expNum += len(reader)

        accLen = aln.metadata.totalLength
        accNum = aln.metadata.numRecords

        self.assertEqual(expLen, accLen)
        self.assertEqual(expNum, accNum)

        # Does it respect filters?
        log.info("Testing whether filters are respected")
        aln.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
        accLen = aln.metadata.totalLength
        accNum = aln.metadata.numRecords

        def count(gen):
            count = 0
            for _ in gen:
                count += 1
            return count

        expLen = 0
        for reader in readers:
            for record in reader:
                expLen += record.readLength

        bfile = openIndexedAlignmentFile(data.getBam(1))
        rWin = (bfile.referenceInfo('E.faecalis.1').ID,
                0,
                bfile.referenceInfo('E.faecalis.1').Length)
        reads = bfile.readsInRange(*rWin)
        expNum = count(reads)
        expLen = 0
        reads = bfile.readsInRange(*rWin)
        for read in reads:
            expLen += read.readLength

        self.assertEqual(expLen, accLen)
        self.assertEqual(expNum, accNum)

    def test_referenceInfoTableMerging(self):
        log.info("Testing refIds, etc. after merging")
        ds = DataSet(data.getXml(16))
        also_lambda = ds.toExternalFiles()[0]
        aln = AlignmentSet(data.getBam(0), data.getBam(1), also_lambda)
        readers = aln.resourceReaders()

        ids = sorted([i for _, i in aln.refInfo('ID')])
        self.assertEqual(range(len(ids)), ids)

        accNames = aln.refNames
        expNames = reduce(np.append,
                          [reader.referenceInfoTable['Name']
                           for reader in readers])
        expNames = np.unique(expNames)
        self.assertEqual(sorted(expNames), sorted(accNames))

        accNames = aln.fullRefNames
        expNames = reduce(np.append,
                          [reader.referenceInfoTable['FullName']
                           for reader in readers])
        expNames = np.unique(expNames)
        self.assertEqual(sorted(expNames), sorted(accNames))


    def test_merge(self):
        ds1 = DataSet(data.getXml(0))
        ds2 = DataSet(data.getXml(1))
        ds3 = ds1 + ds2
        # xmls with different resourceIds: success
        ds1 = DataSet(data.getXml(no=8))
        ds2 = DataSet(data.getXml(no=9))
        ds3 = ds1 + ds2
        expected = ds1.numExternalResources + ds2.numExternalResources
        self.assertTrue(ds3.numExternalResources == expected)
        # xmls with different resourceIds but conflicting filters:
        # failure to merge
        ds2 = DataSet(data.getXml(no=10))
        ds3 = ds1 + ds2
        self.assertEqual(ds3, None)
        # xmls with same resourceIds: ignores new inputs
        ds1 = DataSet(data.getXml(no=8))
        ds2 = DataSet(data.getXml(no=8))
        ds3 = ds1 + ds2
        expected = ds1.numExternalResources
        self.assertTrue(ds3.numExternalResources == expected)

    def test_newUuid(self):
        ds = DataSet()
        old = ds.uuid
        _ = ds.newUuid()
        self.assertTrue(old != ds.uuid)

    def test_split(self):
        ds1 = DataSet(data.getXml())
        self.assertTrue(ds1.numExternalResources > 1)
        dss = ds1.split()
        self.assertTrue(len(dss) == ds1.numExternalResources)
        dss = ds1.split(chunks=1)
        self.assertTrue(len(dss) == 1)
        dss = ds1.split(chunks=2)
        self.assertTrue(len(dss) == 2)
        self.assertFalse(dss[0].uuid == dss[1].uuid)
        self.assertTrue(dss[0].name == dss[1].name)
        # Lets try merging and splitting on subdatasets
        ds1 = DataSet(data.getXml(8))
        # 500000 is a lie, the resource is unopenable
        self.assertEquals(ds1.totalLength, -1)
        ds1tl = ds1.totalLength
        ds2 = DataSet(data.getXml(9))
        # 500000 is a lie, the resource is unopenable
        self.assertEquals(ds2.totalLength, -1)
        ds2tl = ds2.totalLength
        dss = ds1 + ds2
        self.assertTrue(dss.totalLength == (ds1tl + ds2tl))
        ds1, ds2 = dss.split(2)
        self.assertTrue(ds1.totalLength == ds1tl)
        self.assertTrue(ds2.totalLength == ds2tl)

    def test_copy(self):
        ds1 = DataSet(data.getXml())
        ds2 = ds1.copy()
        self.assertFalse(ds1 == ds2)
        self.assertFalse(ds1.uuid == ds2.uuid)
        self.assertFalse(ds1 is ds2)
        self.assertTrue(ds1.name == ds2.name)
        self.assertTrue(ds1.externalResources == ds2.externalResources)
        # The name and UniqueId are different:
        self.assertFalse(ds1.objMetadata == ds2.objMetadata)
        self.assertTrue(ds1.filters == ds2.filters)
        self.assertTrue(ds1.subdatasets == ds2.subdatasets)
        self.assertTrue(len(ds1.subdatasets) == 2)
        self.assertTrue(len(ds2.subdatasets) == 2)
        assert not reduce(lambda x, y: x or y,
                          [ds1d is ds2d for ds1d in
                           ds1.subdatasets for ds2d in
                           ds2.subdatasets])
        ds1 = DataSet(data.getXml(no=8))
        self.assertEquals(type(ds1.metadata).__name__,
                          'SubreadSetMetadata')
        ds2 = ds1.copy()
        self.assertEquals(type(ds2.metadata).__name__,
                          'SubreadSetMetadata')
        # Lets try casting
        ds1 = DataSet(data.getBam())
        self.assertEquals(type(ds1).__name__,
                          'DataSet')
        ds1 = ds1.copy(asType='SubreadSet')
        self.assertEquals(type(ds1).__name__,
                          'SubreadSet')
        # Lets do some illicit casting
        with self.assertRaises(TypeError):
            ds1 = ds1.copy(asType='ReferenceSet')
        # Lets try not having to cast
        ds1 = SubreadSet(data.getBam())
        self.assertEquals(type(ds1).__name__, 'SubreadSet')

    def test_write(self):
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfile = os.path.join(outdir, 'tempfile.xml')
        ds1 = DataSet(data.getBam())
        ds1.write(outfile)
        # TODO: turn back on when pyxb present:
        #validateFile(outfile)
        ds2 = DataSet(outfile)
        self.assertTrue(ds1 == ds2)

    def test_addFilters(self):
        ds1 = DataSet()
        filt = Filters()
        filt.addRequirement(rq=[('>', '0.85')])
        ds1.addFilters(filt)
        self.assertEquals(str(ds1.filters), '( rq > 0.85 )')
        # Or added from a source XML
        ds2 = DataSet(data.getXml(8))
        self.assertEquals(str(ds2.filters),
                '( rq > 0.75 ) OR ( qname == 100/0/0_100 )')

    def test_addMetadata(self):
        ds = DataSet()
        ds.addMetadata(None, Name='LongReadsRock')
        self.assertEquals(ds._metadata.getV(container='attrib', tag='Name'),
                          'LongReadsRock')
        ds2 = DataSet(data.getXml(no=8))
        # 500000 is a lie, the resource is unopenable
        self.assertEquals(ds2._metadata.totalLength, -1)
        ds2._metadata.totalLength = 100000
        self.assertEquals(ds2._metadata.totalLength, 100000)
        ds2._metadata.totalLength += 100000
        self.assertEquals(ds2._metadata.totalLength, 200000)

    def test_addExternalResources(self):
        ds = DataSet()
        er1 = ExternalResource()
        er1.resourceId = "test1.bam"
        er2 = ExternalResource()
        er2.resourceId = "test2.bam"
        er3 = ExternalResource()
        er3.resourceId = "test1.bam"
        ds.addExternalResources([er1])
        self.assertEquals(ds.numExternalResources, 1)
        # different resourceId: succeeds
        ds.addExternalResources([er2])
        self.assertEquals(ds.numExternalResources, 2)
        # same resourceId: fails
        ds.addExternalResources([er3])
        self.assertEquals(ds.numExternalResources, 2)
        for extRef in ds.externalResources:
            self.assertEqual(type(extRef).__name__, "ExternalResource")

        extRef = ds.externalResources[0]
        self.assertEqual(type(extRef).__name__, "ExternalResource")
        self.assertEqual(extRef.resourceId, 'test1.bam')

        extRef = ds.externalResources[1]
        self.assertEqual(type(extRef).__name__, "ExternalResource")
        self.assertEqual(extRef.resourceId, 'test2.bam')

    def test_resourceReaders(self):
        ds = DataSet(data.getBam())
        for seqFile in ds.resourceReaders():
            self.assertEqual(len([row for row in seqFile]), 115)

    def test_rows(self):
        # I don't agree that these are the correct holeNumbers, but pbcore
        # does:
        holenumbers = [0, 0]
        ds = DataSet(data.getXml(16))
        for row, hn in zip(ds.records, holenumbers):
            self.assertEqual(row.holeNumber, hn)

    def test_toFofn(self):
        self.assertEquals(DataSet("bam1.bam", "bam2.bam").toFofn(),
                          ['bam1.bam', 'bam2.bam'])
        realDS = DataSet(data.getXml(13))
        files = realDS.toFofn()
        self.assertEqual(len(files), 1)
        self.assertTrue(os.path.exists(files[0]))
        self.assertTrue(os.path.isabs(files[0]))
        files = realDS.toFofn(relative=True)
        self.assertEqual(len(files), 1)
        self.assertTrue(os.path.exists(files[0]))
        self.assertFalse(os.path.isabs(files[0]))

    def test_toExternalFiles(self):
        bogusDS = DataSet("bam1.bam", "bam2.bam")
        self.assertEqual(['bam1.bam', 'bam2.bam'],
                         bogusDS.externalResources.resourceIds)
        self.assertEquals(DataSet("bam1.bam", "bam2.bam").toExternalFiles(),
                          ['bam1.bam', 'bam2.bam'])
        realDS = DataSet(data.getXml(13))
        files = realDS.toExternalFiles()
        self.assertEqual(len(files), 1)
        self.assertTrue(os.path.exists(files[0]))
        self.assertTrue(os.path.isabs(files[0]))

    @SkipTest
    def test_checkFilterMatch(self):
        # different resourceIds, compatible filters:
        ds1 = DataSet(data.getXml(no=8))
        ds2 = DataSet(data.getXml(no=9))
        #self.assertTrue(ds1._checkFilterMatch(ds2.filters))
        self.assertTrue(ds1.filters.testCompatibility(ds2.filters))
        # different resourceIds, incompatible filters:
        ds3 = DataSet(data.getXml(no=10))
        #self.assertFalse(ds1._checkFilterMatch(ds3.filters))
        self.assertFalse(ds1.filters.testCompatibility(ds3.filters))

    #def test_filterOk(self):
        ## compatible filters
        #filt1 = {'rq':'>0.85'}
        #filt2 = {'rq':'>0.85'}
        #self.assertTrue(_filterOk(filt1, filt2))
        ## incompatible filters
        #filt1 = {'rq':'>0.85'}
        #filt2 = {'rq':'>0.75'}
        #self.assertFalse(_filterOk(filt1, filt2))

    def test_chunk_list(self):
        test = [1, 2, 3, 4, 5]
        chunks = DataSet()._chunkList(test, 3, balanceKey=lambda x: x)
        self.assertEqual(chunks, [[5], [4, 1], [3, 2]])

    def test_ref_names(self):
        ds = DataSet(data.getBam())
        refNames = ds.refNames
        self.assertEqual(refNames[0], 'lambda_NEB3011')
        self.assertEqual(len(refNames), 1)

    def test_reads_in_range(self):
        ds = DataSet(data.getBam())
        refNames = ds.refNames

        # See test_ref_names for why this is expected:
        rn = refNames[0]
        reads = ds.readsInRange(rn, 300, 305)
        self.assertEqual(len(list(reads)), 2)

        ds2 = DataSet(data.getBam(1))
        reads = ds2.readsInRange("E.faecalis.1", 0, 1400)
        self.assertEqual(len(list(reads)), 2)

    def test_filter(self):
        ds2 = DataSet(data.getXml(13))
        self.assertEqual(len(list(ds2.records)), 2)
        ds2.disableFilters()
        self.assertEqual(len(list(ds2.records)), 11)
        ds2.enableFilters()
        self.assertEqual(len(list(ds2.records)), 2)

    @SkipTest
    def test_split_by_contigs_presplit(self):
        # Consumes too much memory for Jenkins

        # Test to make sure the result of a split by contigs has an appropriate
        # number of records (make sure filters are appropriately aggressive)
        ds2 = DataSet(data.getXml(17))
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

    def test_split_by_contigs_with_split(self):
        # test to make sure the refWindows work when chunks == # refs
        ds3 = DataSet(data.getBam())
        dss = ds3.split(contigs=True)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        self.assertEqual(refWindows, [(0, 0, 48502)])

        dss = ds3.split(contigs=True, chunks=1)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        self.assertEqual(refWindows, [(0, 0, 48502)])

        dss = ds3.split(contigs=True, chunks=2)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        self.assertEqual(refWindows, [(0, 0, 24251), (0, 24251, 48502)])

        dss = ds3.split(contigs=True, chunks=3)
        refWindows = sorted(reduce(lambda x, y: x + y,
                                   [ds.refWindows for ds in dss]))
        self.assertEqual(refWindows, [(0, 0, 16167), (0, 16167, 32334),
                                      (0, 32334, 48502)])

    def test_filter_reference_contigs(self):
        ds2 = ReferenceSet(data.getRef())
        self.assertEqual(len(list(ds2.refNames)), 4)
        filt = Filters()
        filt.addRequirement(id=[('==', 'lambda_NEB3011_contig_1')])
        ds2.addFilters(filt)
        self.assertEqual(str(ds2.filters),
                         "( id == lambda_NEB3011_contig_1 )")
        self.assertEqual(len(ds2.refNames), 1)
        self.assertEqual(len(list(ds2.records)), 1)
        ds2.disableFilters()
        self.assertEqual(len(list(ds2.refNames)), 4)
        self.assertEqual(len(list(ds2.records)), 4)
        ds2.enableFilters()
        self.assertEqual(len(list(ds2.refNames)), 1)
        self.assertEqual(len(list(ds2.records)), 1)

    def test_reads_in_subdataset(self):
        ds = DataSet(data.getXml(13))
        refs = ['E.faecalis.1', 'E.faecalis.2']
        readRefs = ['E.faecalis.1'] * 2 + ['E.faecalis.2'] * 9
        ds.filters.removeRequirement('rname')
        dss = ds.split(contigs=True)
        self.assertEqual(len(dss), 2)
        self.assertEqual(sorted(refs),
                         sorted([ds.filters[0][0].value for ds in dss]))
        self.assertEqual(len(list(dss[0].readsInSubDatasets())), 9)
        self.assertEqual(len(list(dss[1].readsInSubDatasets())), 2)

        #ds2 = DataSet(data.getXml(13))
        #ds2._makePerContigSubDatasets()
        #self.assertEqual(
            #sorted([read.referenceName for read in ds2.readsInSubDatasets()]),
            #sorted(readRefs))
        #ds3 = DataSet(data.getXml(13))
        #self.assertEqual(len(list(ds3.readsInSubDatasets())), 2)

    def test_refWindows(self):
        ds = DataSet(data.getBam())
        dss = ds.split(chunks=2, contigs=True)
        self.assertEqual(len(dss), 2)
        self.assertEqual(str(dss[0].filters),
                         '( rname = lambda_NEB3011 AND tstart > 0 '
                         'AND tend < 24251 )')
        self.assertEqual(dss[0].refWindows, [(0, 0, 24251)])
        ds = DataSet(data.getBam())
        ds.filters.addRequirement(rname=[('=', 'lambda_NEB3011'),
                                         ('=', 'lambda_NEB3011')],
                                  tStart=[('<', '0'),
                                          ('<', '100')],
                                  tEnd=[('>', '99'),
                                        ('>', '299')])
        self.assertEqual(str(ds.filters),
                         '( rname = lambda_NEB3011 AND tstart '
                         '< 0 AND tend > 99 ) OR ( rname = lambd'
                         'a_NEB3011 AND tstart < 100 AND tend > 299 )')
        self.assertEqual(ds.refWindows, [(0, 0, 99), (0, 100, 299)])


    def test_refLengths(self):
        ds = DataSet(data.getBam())
        self.assertEqual(ds.refLengths, {'lambda_NEB3011': 48502})
        ds = DataSet(data.getBam(1))
        random_few = {'B.cereus.6': 1472, 'S.agalactiae.1': 1470,
                      'B.cereus.4': 1472}
        for key, value in random_few.items():
            self.assertEqual(ds.refLengths[key], value)

        # this is a hack to only emit refNames that actually have records
        # associated with them:
        dss = ds.split(contigs=True, chunks=1)[0]
        self.assertEqual(dss.refLengths, {'E.faecalis.1': 1482,
                                          'E.faecalis.2': 1482})

    def test_reads_in_contig(self):
        log.info("Testing reads in contigs")
        ds = DataSet(data.getXml(13))
        refs = ['E.faecalis.1', 'E.faecalis.2']
        readRefs = ['E.faecalis.1'] * 2 + ['E.faecalis.2'] * 9
        ds.filters.removeRequirement('rname')
        dss = ds.split(contigs=True)
        self.assertEqual(len(dss), 2)
        self.assertEqual(sorted(refs),
                         sorted([ds.filters[0][0].value for ds in dss]))
        self.assertEqual(len(list(dss[0].readsInReference(refs[1]))), 9)
        self.assertEqual(len(list(dss[1].readsInReference(refs[0]))), 2)

        ds = DataSet(data.getXml(13))
        refs = ['E.faecalis.1', 'E.faecalis.2']
        readRefs = ['E.faecalis.1'] * 2 + ['E.faecalis.2'] * 9
        filt = Filters()
        filt.addRequirement(length=[('>', '100')])
        ds.addFilters(filt)
        ds.filters.removeRequirement('rname')
        dss = ds.split(contigs=True)
        self.assertEqual(len(dss), 2)
        self.assertEqual(sorted(refs),
                         sorted([ds.filters[0][1].value for ds in dss]))
        self.assertEqual(len(list(dss[0].readsInReference(refs[1]))), 9)
        self.assertEqual(len(list(dss[1].readsInReference(refs[0]))), 2)

        ds = DataSet(data.getXml(13))
        refs = ['E.faecalis.1', 'E.faecalis.2']
        readRefs = ['E.faecalis.1'] * 2 + ['E.faecalis.2'] * 9
        filt = Filters()
        filt.addRequirement(length=[('>', '1000')])
        ds.addFilters(filt)
        ds.filters.removeRequirement('rname')
        dss = ds.split(contigs=True)
        self.assertEqual(len(dss), 2)
        self.assertEqual(sorted(refs),
                         sorted([ds.filters[0][1].value for ds in dss]))
        self.assertEqual(len(list(dss[0].readsInReference(refs[1]))), 8)
        self.assertEqual(len(list(dss[1].readsInReference(refs[0]))), 1)

    def test_reads_in_reference(self):
        ds = DataSet(data.getBam())
        refNames = ds.refNames

        # See test_ref_names for why this is expected:
        rn = refNames[0]
        reads = ds.readsInReference(rn)
        self.assertEqual(len(list(reads)), 115)

        ds2 = DataSet(data.getBam(1))
        reads = ds2.readsInReference("E.faecalis.1")
        self.assertEqual(len(list(reads)), 2)

        reads = ds2.readsInReference("E.faecalis.2")
        self.assertEqual(len(list(reads)), 9)

        ds2 = DataSet(data.getXml(13))
        reads = ds2.readsInReference("E.faecalis.1")
        self.assertEqual(len(list(reads)), 2)

        # Because of the filter!
        reads = ds2.readsInReference("E.faecalis.2")
        self.assertEqual(len(list(reads)), 0)

    def test_staggered_reads_in_range(self):
        ds = DataSet(data.getXml(15))
        refNames = ds.refNames

        # See test_ref_names for why this is expected:
        rn = refNames[0]
        reads = ds.readsInRange(rn, 0, 1000)
        self.assertEqual(len(list(reads)), 3)
        read_starts = (0, 302, 675)
        #for read in reads:
            #self.assertTrue(_overlap(0, 1000, read.tStart, read.tEnd))
        for read, start in zip(reads, read_starts):
            self.assertEqual(read.tStart, start)

    def test_referenceInfo(self):
        aln = AlignmentSet(data.getBam(0), data.getBam(1))
        readers = aln.resourceReaders()
        readers = aln.resourceReaders()
        self.assertEqual(len(readers[0].referenceInfoTable), 1)
        self.assertEqual(
            str(readers[0].referenceInfo('lambda_NEB3011')),
            "(0, 0, 'lambda_NEB3011', 'lambda_NEB3011', 48502, "
            "'a1319ff90e994c8190a4fe6569d0822a', 0L, 0L)")
        self.assertEqual(
            str(aln.referenceInfo('lambda_NEB3011')),
            "(0, 0, 'lambda_NEB3011', 'lambda_NEB3011', 48502, "
            "'a1319ff90e994c8190a4fe6569d0822a', 0L, 0L)")
        self.assertEqual(readers[0].referenceInfo('lambda_NEB3011'),
                         aln.referenceInfo('lambda_NEB3011'))

    def test_referenceInfoTable(self):
        ds = DataSet(data.getXml(16))
        also_lambda = ds.toExternalFiles()[0]
        aln = AlignmentSet(data.getBam(0), data.getBam(1), also_lambda)
        readers = aln.resourceReaders()

        self.assertEqual(len(readers[0].referenceInfoTable), 1)
        self.assertEqual(len(readers[1].referenceInfoTable), 59)
        self.assertEqual(len(readers[2].referenceInfoTable), 1)
        self.assertEqual(readers[0].referenceInfoTable.Name,
                         readers[2].referenceInfoTable.Name)
        self.assertEqual(len(aln.referenceInfoTable), 60)

    def test_readGroupTable(self):
        ds = DataSet(data.getXml(16))
        also_lambda = ds.toExternalFiles()[0]
        aln = AlignmentSet(data.getBam(0), data.getBam(1), also_lambda)
        readers = aln.resourceReaders()

        self.assertEqual(len(readers[0].readGroupTable), 1)
        self.assertEqual(len(readers[1].readGroupTable), 1)
        self.assertEqual(len(readers[2].readGroupTable), 1)
        self.assertEqual(len(aln.readGroupTable), 3)

    def test_repr(self):
        ds = DataSet(data.getBam())
        rep = str(ds)
        self.assertTrue(re.search('DataSet', rep))
        self.assertTrue(re.search('uuid:',
                                  rep))
        self.assertTrue(re.search('bam_mapping.bam', rep))

    def test_stats_metadata(self):
        ds = DataSet(data.getBam())
        ds.loadStats(data.getStats())
        self.assertEqual(ds.metadata.summaryStats.prodDist.numBins, 4)
        self.assertEqual(ds.metadata.summaryStats.prodDist.bins,
                         [1576, 901, 399, 0])
        ds1 = DataSet(data.getXml(8))
        ds1.loadStats(data.getStats())
        ds2 = DataSet(data.getXml(9))
        ds2.loadStats(data.getStats())
        ds3 = ds1 + ds2
        self.assertEqual(ds1.metadata.summaryStats.prodDist.bins,
                         [1576, 901, 399, 0])
        self.assertEqual(ds2.metadata.summaryStats.prodDist.bins,
                         [1576, 901, 399, 0])
        self.assertEqual(ds3.metadata.summaryStats.prodDist.bins,
                         [3152, 1802, 798, 0])
        self.assertEqual(ds1.metadata.summaryStats.readLenDist.bins,
                         [0, 62, 39, 36, 29, 37, 19, 29, 37, 32, 32, 40, 45,
                          54, 73, 77, 97, 95, 49, 17, 2, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0])
        self.assertEqual(ds2.metadata.summaryStats.readLenDist.bins,
                         [0, 62, 39, 36, 29, 37, 19, 29, 37, 32, 32, 40, 45,
                          54, 73, 77, 97, 95, 49, 17, 2, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0])
        self.assertEqual(ds3.metadata.summaryStats.readLenDist.bins,
                         [0, 124, 78, 72, 58, 74, 38, 58, 74, 64, 64, 80, 90,
                          108, 146, 154, 194, 190, 98, 34, 4, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0])
        # Lets check some manual values
        ds1 = DataSet(data.getXml(8))
        ds1.loadStats(data.getStats())
        ds2 = DataSet(data.getXml(9))
        ds2.loadStats(data.getStats())
        ds1.metadata.summaryStats.readLenDist.bins = (
            [0, 10, 9, 8, 7, 6, 4, 2, 1, 0, 0, 1])
        self.assertEqual(ds1.metadata.summaryStats.readLenDist.bins,
                         [0, 10, 9, 8, 7, 6, 4, 2, 1, 0, 0, 1])
        ds1.metadata.summaryStats.readLenDist.minBinValue = 10
        ds1.metadata.summaryStats.readLenDist.binWidth = 10
        ds2.metadata.summaryStats.readLenDist.bins = (
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1])
        self.assertEqual(ds2.metadata.summaryStats.readLenDist.bins,
                         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1])
        ds2.metadata.summaryStats.readLenDist.minBinValue = 20
        ds2.metadata.summaryStats.readLenDist.binWidth = 10
        ds3 = ds1 + ds2
        self.assertEqual(ds3.metadata.summaryStats.readLenDist.bins,
                         [0, 10, 10, 9, 8, 7, 5, 3, 2, 1, 0, 1, 1])
        # now lets swap
        ds1 = DataSet(data.getXml(8))
        ds1.loadStats(data.getStats())
        ds2 = DataSet(data.getXml(9))
        ds2.loadStats(data.getStats())
        ds1.metadata.summaryStats.readLenDist.bins = (
            [0, 10, 9, 8, 7, 6, 4, 2, 1, 0, 0, 1])
        self.assertEqual(ds1.metadata.summaryStats.readLenDist.bins,
                         [0, 10, 9, 8, 7, 6, 4, 2, 1, 0, 0, 1])
        ds1.metadata.summaryStats.readLenDist.minBinValue = 20
        ds1.metadata.summaryStats.readLenDist.binWidth = 10
        ds2.metadata.summaryStats.readLenDist.bins = (
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1])
        self.assertEqual(ds2.metadata.summaryStats.readLenDist.bins,
                         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1])
        ds2.metadata.summaryStats.readLenDist.minBinValue = 10
        ds2.metadata.summaryStats.readLenDist.binWidth = 10
        ds3 = ds1 + ds2
        self.assertEqual(ds3.metadata.summaryStats.readLenDist.bins,
                         [0, 1, 11, 10, 9, 8, 7, 5, 3, 1, 0, 1, 1])

        # now lets do some non-overlapping
        ds1 = DataSet(data.getXml(8))
        ds1.loadStats(data.getStats())
        ds2 = DataSet(data.getXml(9))
        ds2.loadStats(data.getStats())
        ds1.metadata.summaryStats.readLenDist.bins = (
            [1, 1, 1])
        self.assertEqual(ds1.metadata.summaryStats.readLenDist.bins,
                         [1, 1, 1])
        ds1.metadata.summaryStats.readLenDist.minBinValue = 10
        ds1.metadata.summaryStats.readLenDist.binWidth = 10
        ds2.metadata.summaryStats.readLenDist.bins = (
            [2, 2, 2])
        self.assertEqual(ds2.metadata.summaryStats.readLenDist.bins,
                         [2, 2, 2])
        ds2.metadata.summaryStats.readLenDist.minBinValue = 50
        ds2.metadata.summaryStats.readLenDist.binWidth = 10
        ds3 = ds1 + ds2
        self.assertEqual(ds3.metadata.summaryStats.readLenDist.bins,
                         [1, 1, 1, 0, 2, 2, 2])
