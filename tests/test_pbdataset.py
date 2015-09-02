
import os
import re
import logging
import itertools
import tempfile

import numpy as np
import unittest
from unittest.case import SkipTest

from pbcore.io import openIndexedAlignmentFile
from pbcore.io import (DataSet, SubreadSet, ReferenceSet, AlignmentSet,
                       openDataSet, DataSetMetaTypes, HdfSubreadSet)
from pbcore.io.dataset.DataSetIO import _dsIdToSuffix
from pbcore.io.dataset.DataSetMembers import ExternalResource, Filters
from pbcore.io.dataset.DataSetWriter import toXml
from pbcore.io.dataset.DataSetValidator import validateFile
from pbcore.util.Process import backticks
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
        ds1 = DataSet(data.getXml(11), data.getBam())
        self.assertEquals(ds1.numExternalResources, 2)
        ds1 = DataSet(data.getFofn())
        self.assertEquals(ds1.numExternalResources, 2)
        # New! Use the correct constructor:
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

    def test_split_cli(self):
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        cmd = "dataset.py split --outdir {o} --contigs --chunks 2 {d}".format(
            o=outdir,
            d=data.getXml(8))
        log.debug(cmd)
        o, r, m = backticks(cmd)
        self.assertEqual(r, 0)
        self.assertTrue(os.path.exists(
            os.path.join(outdir, os.path.basename(data.getXml(15)))))
        self.assertTrue(os.path.exists(
            os.path.join(outdir, os.path.basename(data.getXml(16)))))

    def test_create_cli(self):
        log.debug("Absolute")
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        cmd = "dataset.py create --type AlignmentSet {o} {i1} {i2}".format(
            o=os.path.join(outdir, 'pbalchemysim.alignmentset.xml'),
            i1=data.getXml(8), i2=data.getXml(11))
        log.debug(cmd)
        o, r, m = backticks(cmd)
        self.assertEqual(r, 0)
        self.assertTrue(os.path.exists(
            os.path.join(outdir, os.path.basename(data.getXml(12)))))

        log.debug("Relative")
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        cmd = ("dataset.py create --relative --type AlignmentSet "
               "{o} {i1} {i2}".format(
                   o=os.path.join(outdir, 'pbalchemysim.alignmentset.xml'),
                   i1=data.getXml(8),
                   i2=data.getXml(11)))
        log.debug(cmd)
        o, r, m = backticks(cmd)
        self.assertEqual(r, 0)
        self.assertTrue(os.path.exists(
            os.path.join(outdir, os.path.basename(data.getXml(12)))))

    def test_empty_metatype(self):
        inBam = data.getBam()
        d = DataSet(inBam)
        for extRes in d.externalResources:
            self.assertEqual(extRes.metaType, "")

    def test_nonempty_metatype(self):
        inBam = data.getBam()
        d = AlignmentSet(inBam)
        for extRes in d.externalResources:
            self.assertEqual(extRes.metaType,
                             "PacBio.AlignmentFile.AlignmentBamFile")

    def test_loading_reference(self):
        log.info('Opening Reference')
        r = ReferenceSet(data.getRef()).toExternalFiles()[0]
        log.info('Done Opening Reference')
        log.info('Opening AlignmentSet')
        d = AlignmentSet(data.getBam(), referenceFastaFname=r)
        log.info('Done Opening AlignmentSet')
        bfile = openIndexedAlignmentFile(data.getBam(),
                                         referenceFastaFname=r)
        self.assertTrue(bfile.isReferenceLoaded)
        for res in d.resourceReaders():
            self.assertTrue(res.isReferenceLoaded)

        aln = AlignmentSet(data.getBam())
        aln.addReference(r)
        for res in aln.resourceReaders():
            self.assertTrue(res.isReferenceLoaded)

    def test_factory_function(self):
        aln = data.getXml(8)
        ref = data.getXml(9)
        sub = data.getXml(10)
        inTypes = [aln, ref, sub]
        expTypes = [AlignmentSet, ReferenceSet, SubreadSet]
        for infn, exp in zip(inTypes, expTypes):
            # TODO enable this for all when simulated subread files can be
            # pbi'd
            if exp in [ReferenceSet, AlignmentSet]:
                ds = openDataSet(infn, strict=True)
            else:
                ds = openDataSet(infn, strict=False)
            self.assertEqual(type(ds), exp)

    def test_type_checking(self):
        bam = data.getBam()
        fasta = ReferenceSet(data.getXml(9)).toExternalFiles()[0]
        bax = HdfSubreadSet(data.getXml(19)).toExternalFiles()[0]

        DataSet(bam, strict=False)
        DataSet(fasta, strict=False)
        DataSet(bax, strict=False)
        with self.assertRaises(Exception):
            DataSet(bam, strict=True)
        with self.assertRaises(Exception):
            DataSet(fasta, strict=True)
        with self.assertRaises(Exception):
            DataSet(bax, strict=True)

        AlignmentSet(bam, strict=True)
        with self.assertRaises(Exception):
            AlignmentSet(fasta, strict=True)
        with self.assertRaises(Exception):
            AlignmentSet(bax, strict=True)

        ReferenceSet(fasta, strict=True)
        with self.assertRaises(Exception):
            ReferenceSet(bam, strict=True)
        with self.assertRaises(Exception):
            ReferenceSet(bax, strict=True)

        HdfSubreadSet(bax, strict=True)
        with self.assertRaises(Exception):
            HdfSubreadSet(bam, strict=True)
        with self.assertRaises(Exception):
            HdfSubreadSet(fasta, strict=True)

    def test_dsIdToSuffix(self):
        suffixes = ['subreadset.xml', 'hdfsubreadset.xml', 'alignmentset.xml',
                    'barcodeset.xml', 'consensusreadset.xml',
                    'consensusalignmentset.xml',
                    'referenceset.xml', 'contigset.xml']
        for dsId, exp in zip(DataSetMetaTypes.ALL, suffixes):
            self.assertEqual(_dsIdToSuffix(dsId), exp)

    def test_updateCounts_without_pbi(self):
        log.info("Testing updateCounts without pbi")
        data_fname = data.getBam(0)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        tempout = os.path.join(outdir, os.path.basename(data_fname))
        backticks('cp {i} {o}'.format(i=data_fname, o=tempout))
        aln = AlignmentSet(tempout, strict=False)
        self.assertEqual(aln.totalLength, -1)
        self.assertEqual(aln.numRecords, -1)

    def test_attributes(self):
        aln = AlignmentSet(data.getBam(0))
        self.assertEqual(aln.sequencingChemistry, ['unknown'])
        self.assertEqual(aln.isSorted, True)
        self.assertEqual(aln.isEmpty, False)
        self.assertEqual(aln.readType, 'standard')
        self.assertEqual(len(aln.tStart), aln.metadata.numRecords)
        self.assertEqual(len(aln.tEnd), aln.metadata.numRecords)

    def test_updateCounts(self):
        log.info("Testing updateCounts without filters")
        aln = AlignmentSet(data.getBam(0))
        readers = aln.resourceReaders()

        expLen = 0
        for reader in readers:
            for record in reader:
                expLen += record.readLength
                self.assertEqual(
                    record.aStart, record.bam.pbi[record.rowNumber]['aStart'])
                self.assertEqual(
                    record.aEnd, record.bam.pbi[record.rowNumber]['aEnd'])

        expNum = 0
        for reader in readers:
            expNum += len(reader)

        accLen = aln.metadata.totalLength
        accNum = aln.metadata.numRecords

        self.assertEqual(expLen, accLen)
        self.assertEqual(expNum, accNum)

        log.info("Testing whether filters are respected")
        aln.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
        aln.updateCounts()
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

        bfile = openIndexedAlignmentFile(data.getBam(0))
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

    # TODO: turn this back on once a bam is found with a different
    # referenceInfoTable
    @SkipTest
    def test_referenceInfoTableMerging(self):
        log.info("Testing refIds, etc. after merging")
        ds = DataSet(data.getXml(17))
        also_lambda = ds.toExternalFiles()[0]
        aln = AlignmentSet(data.getBam(0), data.getBam(0), also_lambda)
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
        # xmls with different resourceIds: success
        ds1 = DataSet(data.getXml(no=8))
        ds2 = DataSet(data.getXml(no=11))
        ds3 = ds1 + ds2
        expected = ds1.numExternalResources + ds2.numExternalResources
        self.assertTrue(ds3.numExternalResources == expected)
        # xmls with different resourceIds but conflicting filters:
        # failure to merge
        ds2 = DataSet(data.getXml(no=11))
        ds2.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
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
        ds1 = openDataSet(data.getXml(12))
        self.assertTrue(ds1.numExternalResources > 1)
        dss = ds1.split()
        self.assertTrue(len(dss) == ds1.numExternalResources)
        dss = ds1.split(chunks=1)
        self.assertTrue(len(dss) == 1)
        dss = ds1.split(chunks=2, ignoreSubDatasets=True)
        self.assertTrue(len(dss) == 2)
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
        ds1, ds2 = sorted(dss.split(2), key=lambda x: x.totalLength,
                          reverse=True)
        self.assertTrue(ds1.totalLength == ds1tl)
        self.assertTrue(ds2.totalLength == ds2tl)

    @unittest.skipUnless(os.path.isdir("/mnt/secondary-siv/testdata"),
                         "Missing testadata directory")
    def test_split_zmws(self):
        test_file = ("/mnt/secondary-siv/testdata/SA3-DS/lambda/2372215/"
                     "0007_micro/Analysis_Results/m150404_101626_42267_c"
                     "100807920800000001823174110291514_s1_p0.all."
                     "subreadset.xml")
        ds1 = openDataSet(test_file)
        self.assertEqual(len([r for r in ds1]), 1220)
        dss = ds1.split(chunks=1, zmws=True)
        self.assertEqual(sum([len([r for r in ds_]) for ds_ in dss]), 1220)
        dss = ds1.split(chunks=9, zmws=True)
        self.assertEqual(sum([len([r for r in ds_]) for ds_ in dss]), 1220)
        self.assertEqual(
            dss[0].zmwRanges,
            [('m150404_101626_42267_c100807920800000001823174110291514_s1_p0',
              55, 1815)])

    def test_copy(self):
        ds1 = DataSet(data.getXml(12))
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
        # TODO: once simulated files are indexable, turn on strict:
        ds1 = SubreadSet(data.getXml(no=10), strict=False)
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
        ds1 = AlignmentSet(data.getBam())
        ds1.write(outfile)
        log.debug('Validated file: {f}'.format(f=outfile))
        validateFile(outfile)
        ds2 = AlignmentSet(outfile)
        self.assertTrue(ds1 == ds2)

        # Should fail when strict:
        ds3 = AlignmentSet(data.getBam())
        ds3.write(outfile)

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

    def test_addMetadata(self):
        ds = DataSet()
        ds.addMetadata(None, Name='LongReadsRock')
        self.assertEquals(ds._metadata.getV(container='attrib', tag='Name'),
                          'LongReadsRock')
        ds2 = DataSet(data.getXml(no=8))
        self.assertEquals(ds2._metadata.totalLength, 123588)
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
        ds.addExternalResources([er1], updateCount=False)
        self.assertEquals(ds.numExternalResources, 1)
        # different resourceId: succeeds
        ds.addExternalResources([er2], updateCount=False)
        self.assertEquals(ds.numExternalResources, 2)
        # same resourceId: fails
        ds.addExternalResources([er3], updateCount=False)
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
        ds = AlignmentSet(data.getBam())
        for seqFile in ds.resourceReaders():
            self.assertEqual(len([row for row in seqFile]), 92)

    def test_records(self):
        ds = AlignmentSet(data.getXml(8))
        self.assertTrue(len(list(ds.records)), 112)

    def test_toFofn(self):
        self.assertEquals(DataSet("bam1.bam", "bam2.bam",
                                  strict=False).toFofn(),
                          ['bam1.bam', 'bam2.bam'])
        realDS = DataSet(data.getXml(8))
        files = realDS.toFofn()
        self.assertEqual(len(files), 1)
        self.assertTrue(os.path.exists(files[0]))
        self.assertTrue(os.path.isabs(files[0]))
        files = realDS.toFofn(relative=True)
        self.assertEqual(len(files), 1)
        self.assertTrue(os.path.exists(files[0]))
        self.assertFalse(os.path.isabs(files[0]))

    def test_toExternalFiles(self):
        bogusDS = DataSet("bam1.bam", "bam2.bam", strict=False)
        self.assertEqual(['bam1.bam', 'bam2.bam'],
                         bogusDS.externalResources.resourceIds)
        self.assertEquals(DataSet("bam1.bam", "bam2.bam",
                                  strict=False).toExternalFiles(),
                          ['bam1.bam', 'bam2.bam'])
        realDS = DataSet(data.getXml(8))
        files = realDS.toExternalFiles()
        self.assertEqual(len(files), 1)
        self.assertTrue(os.path.exists(files[0]))
        self.assertTrue(os.path.isabs(files[0]))

    def test_chunk_list(self):
        test = [1, 2, 3, 4, 5]
        chunks = DataSet()._chunkList(test, 3, balanceKey=lambda x: x)
        self.assertEqual(chunks, [[5], [4, 1], [3, 2]])

    def test_ref_names(self):
        ds = AlignmentSet(data.getBam())
        refNames = ds.refNames
        self.assertEqual(sorted(refNames)[0], 'A.baumannii.1')
        self.assertEqual(len(refNames), 59)

    def test_reads_in_range(self):
        ds = AlignmentSet(data.getBam())
        refNames = ds.refNames

        rn = refNames[15]
        reads = list(ds.readsInRange(rn, 10, 100))
        self.assertEqual(len(reads), 10)

        def lengthInWindow(hit, winStart, winEnd):
            return min(hit.tEnd, winEnd) - max(hit.tStart, winStart)

        reads = list(ds.readsInRange(rn, 10, 100, longest=True))
        last = None
        for read in reads:
            if last is None:
                last = lengthInWindow(read, 10, 100)
            else:
                self.assertTrue(last >= lengthInWindow(read, 10, 100))
                last = lengthInWindow(read, 10, 100)
        reads = list(ds._pbiReadsInRange(rn, 10, 100))
        self.assertEqual(len(reads), 10)


        ds2 = AlignmentSet(data.getBam(0))
        reads = list(ds2.readsInRange("E.faecalis.1", 0, 1400))
        self.assertEqual(len(reads), 20)

        lengths = ds.refLengths
        for rname, rId in ds.refInfo('ID'):
            rn = ds._idToRname(rId)
            self.assertEqual(rname, rn)
            rlen = lengths[rn]
            self.assertEqual(len(list(ds.readsInReference(rn))),
                             len(list(ds.readsInReference(rId))))
            self.assertEqual(len(list(ds.readsInRange(rn, 0, rlen))),
                             len(list(ds.readsInRange(rId, 0, rlen))))

    @unittest.skipUnless(os.path.isdir("/mnt/secondary-siv/testdata"),
                         "Missing testadata directory")
    def test_reads_in_range_order(self):
        log.debug("Testing with one file")
        testFile = ("/mnt/secondary-siv/testdata/SA3-DS/lambda/"
                    "2372215/0007/Alignment_Results/m150404_101"
                    "626_42267_c1008079208000000018231741102915"
                    "14_s1_p0.1.alignmentset.xml")
        aln = AlignmentSet(testFile)
        reads1 = aln.readsInRange(aln.refNames[0], 0, 400,
                                  usePbi=False)
        reads2 = aln.readsInRange(aln.refNames[0], 0, 400,
                                  usePbi=True)
        num = 0
        for r1, r2 in itertools.izip(reads1, reads2):
            self.assertEqual(r1, r2)
            num += 1
        self.assertTrue(num > 2000)

        log.debug("Testing with three files")
        testFile = ("/mnt/secondary-siv/testdata/SA3-DS/lambda/"
                    "2372215/0007/Alignment_Results/m150404_101"
                    "626_42267_c1008079208000000018231741102915"
                    "14_s1_p0.all.alignmentset.xml")
        aln = AlignmentSet(testFile)
        reads1 = aln.readsInRange(aln.refNames[0], 0, 400,
                                  usePbi=False)
        reads2 = aln.readsInRange(aln.refNames[0], 0, 400,
                                  usePbi=True)
        num = 0
        for r1, r2 in itertools.izip(reads1, reads2):
            self.assertEqual(r1, r2)
            num += 1
        self.assertTrue(num > 2000)

    def test_filter(self):
        ds2 = AlignmentSet(data.getXml(8))
        ds2.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
        self.assertEqual(len(list(ds2.records)), 20)
        ds2.disableFilters()
        self.assertEqual(len(list(ds2.records)), 92)
        ds2.enableFilters()
        self.assertEqual(len(list(ds2.records)), 20)

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
        self.assertListEqual(sizes, [22, 31, 39])
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

    # TODO: get this working again when adding manual subdatasets is good to go
    @SkipTest
    def test_reads_in_subdataset(self):
        ds = DataSet(data.getXml(8))
        #refs = ['E.faecalis.1', 'E.faecalis.2']
        #readRefs = ['E.faecalis.1'] * 2 + ['E.faecalis.2'] * 9
        #ds.filters.removeRequirement('rname')
        dss = ds.split(contigs=True)
        self.assertEqual(len(dss), 12)
        self.assertEqual(['B.vulgatus.4', 'B.vulgatus.5',
                          'C.beijerinckii.13', 'C.beijerinckii.14',
                          'C.beijerinckii.9', 'E.coli.6', 'E.faecalis.1',
                          'E.faecalis.2', 'R.sphaeroides.1',
                          'S.epidermidis.2', 'S.epidermidis.3',
                          'S.epidermidis.4'],
                         sorted([ds.filters[0][0].value for ds in dss]))
        self.assertEqual(len(list(dss[0].readsInSubDatasets())), 3)
        self.assertEqual(len(list(dss[1].readsInSubDatasets())), 20)

        #ds2 = DataSet(data.getXml(13))
        #ds2._makePerContigSubDatasets()
        #self.assertEqual(
            #sorted([read.referenceName for read in ds2.readsInSubDatasets()]),
            #sorted(readRefs))
        #ds3 = DataSet(data.getXml(13))
        #self.assertEqual(len(list(ds3.readsInSubDatasets())), 2)

    def test_refWindows(self):
        ds = AlignmentSet(data.getBam())
        dss = ds.split(chunks=2, contigs=True)
        self.assertEqual(len(dss), 2)
        log.debug(dss[0].filters)
        log.debug(dss[1].filters)
        self.assertTrue(
            '( rname = E.faecalis.2 ) '
            in str(dss[0].filters)
            or
            '( rname = E.faecalis.2 ) '
            in str(dss[1].filters))
        ds = AlignmentSet(data.getBam())
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
        # TODO: look into swapping around refWindows to make this work:
        #self.assertEqual(ds.refWindows, [('lambda_NEB3011', 0, 99),
                                         #('lambda_NEB3011', 100, 299)])


    def test_refLengths(self):
        ds = AlignmentSet(data.getBam(0))
        random_few = {'B.cereus.6': 1472, 'S.agalactiae.1': 1470,
                      'B.cereus.4': 1472}
        for key, value in random_few.items():
            self.assertEqual(ds.refLengths[key], value)

        # this is a hack to only emit refNames that actually have records
        # associated with them:
        dss = ds.split(contigs=True, chunks=1)[0]
        self.assertEqual(dss.refLengths, {'B.vulgatus.4': 1449,
                                          'B.vulgatus.5': 1449,
                                          'C.beijerinckii.13': 1433,
                                          'C.beijerinckii.14': 1433,
                                          'C.beijerinckii.9': 1433,
                                          'E.coli.6': 1463,
                                          'E.faecalis.1': 1482,
                                          'E.faecalis.2': 1482,
                                          'R.sphaeroides.1': 1386,
                                          'S.epidermidis.2': 1472,
                                          'S.epidermidis.3': 1472,
                                          'S.epidermidis.4': 1472
                                         })

    def test_reads_in_contig(self):
        log.info("Testing reads in contigs")
        ds = AlignmentSet(data.getXml(8))
        dss = ds.split(contigs=True)
        self.assertEqual(len(dss), 12)
        efaec1TimesFound = 0
        efaec1TotFound = 0
        efaec2TimesFound = 0
        efaec2TotFound = 0
        for ds in dss:
            ef1 = len(list(ds.readsInReference('E.faecalis.1')))
            ef2 = len(list(ds.readsInReference('E.faecalis.2')))
            if ef1:
                efaec1TimesFound += 1
                efaec1TotFound += ef1
            if ef2:
                efaec2TimesFound += 1
                efaec2TotFound += ef2
        self.assertEqual(efaec1TimesFound, 1)
        self.assertEqual(efaec1TotFound, 20)
        self.assertEqual(efaec2TimesFound, 1)
        self.assertEqual(efaec2TotFound, 3)

        ds = AlignmentSet(data.getXml(8))
        filt = Filters()
        filt.addRequirement(length=[('>', '100')])
        ds.addFilters(filt)
        dss = ds.split(contigs=True)
        self.assertEqual(len(dss), 12)
        efaec1TimesFound = 0
        efaec1TotFound = 0
        efaec2TimesFound = 0
        efaec2TotFound = 0
        for ds in dss:
            ef1 = len(list(ds.readsInReference('E.faecalis.1')))
            ef2 = len(list(ds.readsInReference('E.faecalis.2')))
            if ef1:
                efaec1TimesFound += 1
                efaec1TotFound += ef1
            if ef2:
                efaec2TimesFound += 1
                efaec2TotFound += ef2
        self.assertEqual(efaec1TimesFound, 1)
        self.assertEqual(efaec1TotFound, 20)
        self.assertEqual(efaec2TimesFound, 1)
        self.assertEqual(efaec2TotFound, 3)

        ds = AlignmentSet(data.getXml(8))
        filt = Filters()
        filt.addRequirement(length=[('>', '1000')])
        ds.addFilters(filt)
        dss = ds.split(contigs=True)
        self.assertEqual(len(dss), 9)
        efaec1TimesFound = 0
        efaec1TotFound = 0
        efaec2TimesFound = 0
        efaec2TotFound = 0
        for ds in dss:
            ef1 = len(list(ds.readsInReference('E.faecalis.1')))
            ef2 = len(list(ds.readsInReference('E.faecalis.2')))
            if ef1:
                efaec1TimesFound += 1
                efaec1TotFound += ef1
            if ef2:
                efaec2TimesFound += 1
                efaec2TotFound += ef2
        self.assertEqual(efaec1TimesFound, 1)
        self.assertEqual(efaec1TotFound, 20)
        self.assertEqual(efaec2TimesFound, 1)
        self.assertEqual(efaec2TotFound, 1)

    def test_get_item(self):
        # Indexed files only for now:
        # XXX Reactivate subreadsets when pbindex works for them
        #toTest = [8, 10, 11, 12, 13, 15, 16]
        toTest = [8, 11, 12, 15, 16]
        for fileNo in toTest:
            aln = openDataSet(data.getXml(fileNo))
            items1 = [aln[i] for i in range(len(aln))]
            aln = openDataSet(data.getXml(fileNo))
            items2 = [aln[i] for i in range(len(aln))]
            self.assertListEqual(items1, items2)
            aln = openDataSet(data.getXml(fileNo))
            for i, item in enumerate(aln):
                self.assertEqual(item, aln[i])

    def test_reads_in_reference(self):
        ds = AlignmentSet(data.getBam())
        refNames = ds.refNames

        # See test_ref_names for why this is expected:
        rn = refNames[15]
        reads = ds.readsInReference(rn)
        self.assertEqual(len(list(reads)), 11)

        ds2 = AlignmentSet(data.getBam(0))
        reads = ds2.readsInReference("E.faecalis.1")
        self.assertEqual(len(list(reads)), 20)

        reads = ds2.readsInReference("E.faecalis.2")
        self.assertEqual(len(list(reads)), 3)

        ds2 = AlignmentSet(data.getXml(8))
        reads = ds2.readsInReference("E.faecalis.1")
        self.assertEqual(len(list(reads)), 20)

        ds2.filters.addRequirement(rname=[('=', 'E.faecalis.1')])

        # Because of the filter!
        reads = ds2.readsInReference("E.faecalis.2")
        self.assertEqual(len(list(reads)), 0)

    def test_staggered_reads_in_range(self):
        ds = AlignmentSet(data.getXml(8))
        refNames = ds.refNames

        rn = 'B.vulgatus.5'
        reads = list(ds.readsInRange(rn, 0, 10000))
        ds2 = AlignmentSet(data.getXml(11))
        reads2 = list(ds2.readsInRange(rn, 0, 10000))
        dsBoth = AlignmentSet(data.getXml(8), data.getXml(11))
        readsBoth = list(dsBoth.readsInRange(rn, 0, 10000))
        readsBothNoPbi = list(dsBoth.readsInRange(rn, 0, 10000, usePbi=False))
        self.assertListEqual(readsBoth, readsBothNoPbi)
        self.assertEqual(len(reads), 2)
        self.assertEqual(len(reads2), 5)
        self.assertEqual(len(readsBoth), 7)
        read_starts = (0, 1053)
        for read, start in zip(reads, read_starts):
            self.assertEqual(read.tStart, start)
        read2_starts = (0, 0, 3, 3, 4)
        for read, start in zip(reads2, read2_starts):
            self.assertEqual(read.tStart, start)
        readboth_starts = (0, 0, 0, 3, 3, 4, 1053)
        for read, start in zip(readsBoth, readboth_starts):
            self.assertEqual(read.tStart, start)

    def test_referenceInfo(self):
        aln = AlignmentSet(data.getBam(0))
        readers = aln.resourceReaders()
        self.assertEqual(len(readers[0].referenceInfoTable), 59)
        self.assertEqual(
            str(readers[0].referenceInfo('E.faecalis.1')),
            "(27, 27, 'E.faecalis.1', 'E.faecalis.1', 1482, "
            "'a1a59c267ac1341e5a12bce7a7d37bcb', 0L, 0L)")
        # TODO: add a bam with a different referenceInfoTable to check merging
        # and id remapping:
        #self.assertEqual(
            #str(aln.referenceInfo('E.faecalis.1')),
            #"(27, 27, 'E.faecalis.1', 'E.faecalis.1', 1482, "
            #"'a1a59c267ac1341e5a12bce7a7d37bcb', 0L, 0L)")

    # TODO: turn this back on when a bam with a different referenceInfoTable is
    # found
    @SkipTest
    def test_referenceInfoTable(self):
        aln = AlignmentSet(data.getBam(0), data.getBam(1), data.getBam(2))
        readers = aln.resourceReaders()

        self.assertEqual(len(readers[0].referenceInfoTable), 1)
        self.assertEqual(len(readers[1].referenceInfoTable), 59)
        self.assertEqual(len(readers[2].referenceInfoTable), 1)
        self.assertEqual(readers[0].referenceInfoTable.Name,
                         readers[2].referenceInfoTable.Name)
        self.assertEqual(len(aln.referenceInfoTable), 60)

    # TODO: turn this back on when a bam with a different referenceInfoTable is
    # found
    @SkipTest
    def test_readGroupTable(self):
        aln = AlignmentSet(data.getBam(0), data.getBam(1), data.getBam(2))
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
        self.assertTrue(re.search('pbalchemysim0.pbalign.bam', rep))

    def test_stats_metadata(self):
        ds = DataSet(data.getBam())
        ds.loadStats(data.getStats())
        self.assertEqual(ds.metadata.summaryStats.prodDist.numBins, 4)
        self.assertEqual(ds.metadata.summaryStats.prodDist.bins,
                         [1576, 901, 399, 0])
        ds1 = DataSet(data.getXml(8))
        ds1.loadStats(data.getStats())
        ds2 = DataSet(data.getXml(11))
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
        ds2 = DataSet(data.getXml(11))
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
        ds2 = DataSet(data.getXml(11))
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
        ds2 = DataSet(data.getXml(11))
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

        # now lets test the subdataset metadata retention:
        ss = SubreadSet(data.getXml(10))
        ss.loadStats(data.getStats(0))
        ss.loadStats(data.getStats(1))
        self.assertEqual(153168.0, ss.metadata.summaryStats.numSequencingZmws)
        self.assertEqual(
            2876.0, ss.subdatasets[0].metadata.summaryStats.numSequencingZmws)
        self.assertEqual(
            150292.0, ss.subdatasets[1].metadata.summaryStats.numSequencingZmws)
