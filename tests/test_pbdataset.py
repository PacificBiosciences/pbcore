
import os
import re
import logging
import itertools
import tempfile

import numpy as np
import unittest
import shutil
import copy
from random import shuffle
from unittest.case import SkipTest

from pbcore.io import PacBioBamIndex, IndexedBamReader
from pbcore.io import openIndexedAlignmentFile
from pbcore.io.dataset.utils import BamtoolsVersion
from pbcore.io import (DataSet, SubreadSet, ReferenceSet, AlignmentSet,
                       openDataSet, DataSetMetaTypes, HdfSubreadSet,
                       ConsensusReadSet, ConsensusAlignmentSet, openDataFile,
                       divideKeys, keysToRanges, getDataSetUuid,
                       getDataSetMetaType)
from pbcore.io.dataset.DataSetIO import _dsIdToSuffix, InvalidDataSetIOError
from pbcore.io.dataset.DataSetMembers import ExternalResource, Filters
from pbcore.io.dataset.DataSetValidator import validateFile
from pbcore.util.Process import backticks
import pbcore.data.datasets as data
import pbcore.data as upstreamdata

log = logging.getLogger(__name__)

def _check_constools():
    if not BamtoolsVersion().good:
        log.warn("Bamtools not found or out of date")
        return False

    cmd = "pbindex"
    o, r, m = backticks(cmd)
    if r != 1:
        return False

    cmd = "samtools"
    o, r, m = backticks(cmd)
    if r != 1:
        return False
    return True

def _internal_data():
    if os.path.exists("/pbi/dept/secondary/siv/testdata"):
        return True
    return False


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
        log.debug(outXml)
        # don't validate, type DataSet doesn't validate well
        d.write(outXml, validate=False)
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
        self.assertEquals(type(SubreadSet(data.getSubreadSet(),
                                          skipMissing=True)).__name__,
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

    def test_merge_subdatasets(self):
        # from data file
        ds1 = AlignmentSet(data.getBam(0))
        self.assertEqual(len(ds1.subdatasets), 0)
        ds2 = AlignmentSet(data.getBam(1))
        self.assertEqual(len(ds1.subdatasets), 0)
        merged = ds1 + ds2
        self.assertEqual(len(merged.subdatasets), 2)
        self.assertEqual(merged.subdatasets[0].toExternalFiles(),
                         AlignmentSet(data.getBam(0)).toExternalFiles())
        self.assertEqual(len(merged.subdatasets[0].toExternalFiles()), 1)
        self.assertEqual(merged.subdatasets[1].toExternalFiles(),
                         AlignmentSet(data.getBam(1)).toExternalFiles())
        self.assertEqual(len(merged.subdatasets[1].toExternalFiles()), 1)

        # from data set
        ds1 = AlignmentSet(data.getXml(8))
        self.assertEqual(len(ds1.subdatasets), 0)
        ds2 = AlignmentSet(data.getXml(11))
        self.assertEqual(len(ds2.subdatasets), 0)
        merged = ds1 + ds2
        self.assertEqual(len(merged.subdatasets), 2)
        self.assertEqual(merged.subdatasets[0].toExternalFiles(),
                         AlignmentSet(data.getXml(8)).toExternalFiles())
        self.assertEqual(len(merged.subdatasets[0].toExternalFiles()), 1)
        self.assertEqual(merged.subdatasets[1].toExternalFiles(),
                         AlignmentSet(data.getXml(11)).toExternalFiles())
        self.assertEqual(len(merged.subdatasets[1].toExternalFiles()), 1)

        # combined data set
        merged = AlignmentSet(data.getXml(8), data.getXml(11))
        self.assertEqual(len(merged.subdatasets), 2)
        self.assertEqual(len(merged.subdatasets[0].toExternalFiles()), 1)
        self.assertEqual(merged.subdatasets[0].toExternalFiles(),
                         AlignmentSet(data.getXml(8)).toExternalFiles())
        self.assertEqual(len(merged.subdatasets[1].toExternalFiles()), 1)
        self.assertEqual(merged.subdatasets[1].toExternalFiles(),
                         AlignmentSet(data.getXml(11)).toExternalFiles())

        # No filters, 3 files:
        ds1 = AlignmentSet(data.getXml(8))
        self.assertEqual(len(ds1.subdatasets), 0)
        ds2 = AlignmentSet(data.getXml(11))
        self.assertEqual(len(ds2.subdatasets), 0)
        ds3 = AlignmentSet(data.getXml(11))
        self.assertEqual(len(ds3.subdatasets), 0)
        ds3.externalResources[0].resourceId = "/blah.bam"
        ds4 = ds1 + ds2 + ds3
        self.assertEqual(len(ds4.externalResources), 3)
        self.assertEqual(len(ds4.subdatasets), 3)

        # Filters, 3 files:
        ds1 = AlignmentSet(data.getXml(8))
        self.assertEqual(len(ds1.subdatasets), 0)
        ds1.filters.addRequirement(rq=[('>', 0.8)])
        ds2 = AlignmentSet(data.getXml(11))
        self.assertEqual(len(ds2.subdatasets), 0)
        ds2.filters.addRequirement(rq=[('>', 0.8)])
        ds3 = AlignmentSet(data.getXml(11))
        self.assertEqual(len(ds3.subdatasets), 0)
        ds3.externalResources[0].resourceId = "/blah.bam"
        ds3.filters.addRequirement(rq=[('>', 0.8)])
        ds4 = ds1 + ds2 + ds3
        self.assertEqual(len(ds4.externalResources), 3)
        self.assertEqual(len(ds4.subdatasets), 3)
        self.assertEqual(str(ds4.filters), '( rq > 0.8 )')
        for sss in ds4.subdatasets:
            self.assertEqual(str(sss.filters), '( rq > 0.8 )')
        with self.assertRaises(TypeError):
            # mismatched Filters, 3 files:
            ds1 = AlignmentSet(data.getXml(8))
            self.assertEqual(len(ds1.subdatasets), 0)
            ds1.filters.addRequirement(rq=[('>', 0.8)])
            ds2 = AlignmentSet(data.getXml(11))
            self.assertEqual(len(ds2.subdatasets), 0)
            ds2.filters.addRequirement(rq=[('>', 0.7)])
            ds3 = AlignmentSet(data.getXml(11))
            self.assertEqual(len(ds3.subdatasets), 0)
            ds3.externalResources[0].resourceId = "/blah.bam"
            ds3.filters.addRequirement(rq=[('>', 0.8)])
            ds4 = ds1 + ds2 + ds3

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

    @unittest.skipIf(not _check_constools(),
                     "bamtools or pbindex not found, skipping")
    def test_empty_file_counts(self):
        # empty with pbi:
        dset = SubreadSet(upstreamdata.getEmptyBam())
        self.assertEqual(dset.numRecords, 0)
        self.assertEqual(dset.totalLength, 0)
        self.assertEqual(len(list(dset)), 0)
        # Don't care what they are, just don't want them to fail:
        dset.updateCounts()
        dset.index
        self.assertEqual(len(dset.resourceReaders()), 1)
        self.assertEqual(
            len(dset.split(zmws=True, maxChunks=12)),
            1)

        # empty and full:
        full_bam = SubreadSet(data.getXml(10)).toExternalFiles()[0]
        dset = SubreadSet(upstreamdata.getEmptyBam(), full_bam)
        self.assertEqual(dset.numRecords, 92)
        self.assertEqual(dset.totalLength, 124093)
        self.assertEqual(len(list(dset)), 92)
        dset.updateCounts()
        self.assertNotEqual(list(dset.index), [])
        self.assertEqual(len(dset.resourceReaders()), 2)
        # there are 9 reads in this set, < the minimum chunk size
        self.assertEqual(
            len(dset.split(zmws=True, maxChunks=12)),
            2)


        dset = AlignmentSet(upstreamdata.getEmptyBam())
        self.assertEqual(dset.numRecords, 0)
        self.assertEqual(dset.totalLength, 0)
        self.assertEqual(len(list(dset)), 0)
        dset.updateCounts()
        dset.index
        self.assertEqual(len(dset.resourceReaders()), 1)
        # there is a minimum chunk size here:
        self.assertEqual(
            len(dset.split(contigs=True, maxChunks=12, breakContigs=True)),
            1)

        # empty and full:
        dset = AlignmentSet(upstreamdata.getEmptyBam(), data.getBam())
        self.assertEqual(dset.numRecords, 92)
        self.assertEqual(dset.totalLength, 123588)
        self.assertEqual(len(list(dset)), 92)
        dset.updateCounts()
        self.assertNotEqual(list(dset.index), [])
        self.assertEqual(len(dset.resourceReaders()), 2)
        # there are 9 reads in this set, < the minimum chunk size
        self.assertEqual(
            len(dset.split(zmws=True, maxChunks=12)),
            2)

        dset = ConsensusReadSet(upstreamdata.getEmptyBam())
        self.assertEqual(dset.numRecords, 0)
        self.assertEqual(dset.totalLength, 0)
        self.assertEqual(len(list(dset)), 0)
        dset.updateCounts()
        dset.index
        self.assertEqual(len(dset.resourceReaders()), 1)

        dset = ConsensusAlignmentSet(upstreamdata.getEmptyBam())
        self.assertEqual(dset.numRecords, 0)
        self.assertEqual(dset.totalLength, 0)
        self.assertEqual(len(list(dset)), 0)
        dset.updateCounts()
        dset.index
        self.assertEqual(len(dset.resourceReaders()), 1)

        # empty without pbi:
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfile = os.path.split(upstreamdata.getEmptyBam())[1]
        outpath = os.path.join(outdir, outfile)
        shutil.copy(upstreamdata.getEmptyBam(), outpath)
        dset = SubreadSet(outpath)
        self.assertEqual(dset.numRecords, 0)
        self.assertEqual(dset.totalLength, 0)
        self.assertEqual(len(list(dset)), 0)
        dset.updateCounts()
        self.assertEqual(len(dset.resourceReaders()), 1)
        self.assertEqual(
            len(dset.split(zmws=True, maxChunks=12)),
            1)

        # empty and full:
        full_bam = SubreadSet(data.getXml(10)).toExternalFiles()[0]
        dset = SubreadSet(outpath, full_bam)
        self.assertEqual(len(dset.resourceReaders()), 2)
        dset.updateCounts()
        # without a pbi, updating counts is broken
        self.assertEqual(dset.numRecords, 0)
        self.assertEqual(dset.totalLength, 0)
        self.assertEqual(len(list(dset)), 92)
        with self.assertRaises(IOError):
            self.assertNotEqual(list(dset.index), [])
        self.assertEqual(
            len(dset.split(zmws=True, maxChunks=12)),
            1)


        dset = AlignmentSet(outpath)
        self.assertEqual(dset.numRecords, 0)
        self.assertEqual(dset.totalLength, 0)
        self.assertEqual(len(list(dset)), 0)
        dset.updateCounts()
        self.assertEqual(len(dset.resourceReaders()), 1)
        self.assertEqual(
            len(dset.split(contigs=True, maxChunks=12, breakContigs=True)),
            1)

        # empty and full:
        dset = AlignmentSet(outpath, data.getBam())
        # without a pbi, updating counts is broken
        self.assertEqual(dset.numRecords, 0)
        self.assertEqual(dset.totalLength, 0)
        self.assertEqual(len(list(dset)), 92)
        dset.updateCounts()
        with self.assertRaises(IOError):
            self.assertNotEqual(list(dset.index), [])
        self.assertEqual(len(dset.resourceReaders()), 2)
        self.assertEqual(
            len(dset.split(zmws=True, maxChunks=12)),
            1)

        dset = ConsensusReadSet(outpath)
        self.assertEqual(dset.numRecords, 0)
        self.assertEqual(dset.totalLength, 0)
        self.assertEqual(len(list(dset)), 0)
        dset.updateCounts()
        self.assertEqual(len(dset.resourceReaders()), 1)

        dset = ConsensusAlignmentSet(outpath)
        self.assertEqual(dset.numRecords, 0)
        self.assertEqual(dset.totalLength, 0)
        self.assertEqual(len(list(dset)), 0)
        dset.updateCounts()
        self.assertEqual(len(dset.resourceReaders()), 1)
        dset.induceIndices()
        dset = ConsensusAlignmentSet(outpath)
        self.assertEqual(dset.numRecords, 0)
        self.assertEqual(dset.totalLength, 0)
        self.assertEqual(len(list(dset)), 0)
        dset.updateCounts()
        self.assertEqual(len(dset.resourceReaders()), 1)

    def test_read_ranges(self):
        # This models the old and new ways by which Genomic Consensus generates
        # lists of paired tStarts and tEnds.

        full_bam = upstreamdata.getBamAndCmpH5()[0]
        empty_bam = data.getEmptyAlignedBam()
        file_lists = [[full_bam, empty_bam],
                      [empty_bam, full_bam]]
        refId_list = ['lambda_NEB3011', 0]
        minMapQV = 30

        for file_list in file_lists:
            for refId in refId_list:
                alnFile = AlignmentSet(*file_list)

                # old GC:
                # TODO(mdsmith)(2016-01-27): Remove assertRaises when tId
                # accession is fixed for empty aligned bam+pbi files
                with self.assertRaises(AttributeError):
                    for reader in alnFile.resourceReaders(refId):
                        reader.index.tId
                        refLen = reader.referenceInfo(refId).Length
                        rows = reader.readsInRange(refId, 0, refLen,
                                                   justIndices=True)

                # new GC (just testing that it doesn't raise exceptions):
                rows = alnFile.index[
                    ((alnFile.tId == alnFile.referenceInfo(refId).ID) &
                     (alnFile.mapQV >= minMapQV))]

                unsorted_tStart = rows.tStart
                unsorted_tEnd = rows.tEnd

                # Sort (expected by CoveredIntervals)
                sort_order = np.lexsort((unsorted_tEnd, unsorted_tStart))
                tStart = unsorted_tStart[sort_order].tolist()
                tEnd = unsorted_tEnd[sort_order].tolist()



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

    def test_openDataSet_unicode(self):
        # Test to see if we can't open a unicode filename
        fn = data.getXml(8)
        aln = openDataSet(unicode(fn))

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
        self.assertEqual(aln.totalLength, 0)
        self.assertEqual(aln.numRecords, 0)

    @unittest.skipUnless(os.path.isdir("/pbi/dept/secondary/siv/testdata"),
                         "Missing testadata directory")
    def test_barcode_accession(self):
        testFile = ("/pbi/dept/secondary/siv/testdata/pblaa-unittest/"
                    "P6-C4/HLA_ClassI/m150724_012016_sherri_c1008203"
                    "52550000001823172911031521_s1_p0.class_I.haploid.bam")
        # Test the pbi file:
        bam = IndexedBamReader(testFile)
        pbi = PacBioBamIndex(testFile + '.pbi')
        for brec, prec in zip(bam, pbi):
            brec_bc = list(brec.peer.opt("bc"))
            prec_bc = [prec.bcForward, prec.bcReverse]
            self.assertEqual(brec_bc, prec_bc)

        # Test split by barcode:
        ss = SubreadSet(testFile)
        sss = ss.split(chunks=2, barcodes=True)
        self.assertEqual(len(sss), 2)
        for sset in sss:
            self.assertTrue(len(sset.barcodes) >= 1)

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

    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_scraps_detection(self):
        path = ('/pbi/dept/secondary/siv/testdata/SA3-Sequel/'
                'lambda/315/3150128/r54008_20160308_001811/'
                '2_B01/m54008_160308_053311.')
        subreads = path + 'subreads.bam'
        control = path + 'control.subreads.bam'
        controlscraps = path + 'control.scraps.bam'
        scraps = path + 'scraps.bam'
        subreadspbi = subreads + '.pbi'
        scrapspbi = scraps + '.pbi'

        filesets = [[subreads],
                    [subreads, scraps],
                    [subreads, subreadspbi],
                    [subreads, scrapspbi]]

        for files in filesets:
            sset = SubreadSet(*files, strict=True)
            self.assertEqual(len(sset.externalResources), 1)
            self.assertEqual(sset.externalResources[0].resourceId, subreads)
            self.assertEqual(sset.externalResources[0].scraps, scraps)
            self.assertEqual(sset.externalResources[0].control, control)
            self.assertEqual(
                sset.externalResources[0].externalResources[0].resourceId,
                scraps)
            self.assertEqual(
                sset.externalResources[0].externalResources[1].resourceId,
                control)
            self.assertEqual(
                sset.externalResources[
                    0].externalResources[1].externalResources[0].resourceId,
                controlscraps)


    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_referenceInfoTableMerging(self):
        log.info("Testing refIds, etc. after merging")
        bam1 = ("/pbi/dept/secondary/siv/testdata/SA3-RS/ecoli/"
                "2590953/0001/Alignment_Results/"
                "m140913_005018_42139_c100713652400000001823152"
                "404301534_s1_p0.1.aligned.bam")
        bam2 = ("/pbi/dept/secondary/siv/testdata/SA3-RS/ecoli/"
                "2590953/0001/Alignment_Results/"
                "m140913_005018_42139_c100713652400000001823152"
                "404301534_s1_p0.3.aligned.bam")
        aln = AlignmentSet(bam1, bam2)
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
              7, 14007)])
        self.assertEqual(
            dss[-1].zmwRanges,
            [('m150404_101626_42267_c100807920800000001823174110291514_s1_p0',
              149876, 163475)])
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
              7, 22098)])
        self.assertEqual(
            dss[-1].zmwRanges,
            [('m141115_075238_ethan_c100699872550000001823139203261572_s1_p0',
              127814, 163468)])


    @unittest.skipUnless(os.path.isdir("/pbi/dept/secondary/siv/testdata"),
                         "Missing testadata directory")
    def test_multi_movie_readsByName(self):
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
        self.assertEqual(len(ds1), N_RECORDS)
        queries = [('m150404_101626_42267_c1008079208000'
                    '00001823174110291514_s1_p0/7/*', 2),
                   ('m141115_075238_ethan_c1006998725500'
                    '00001823139203261572_s1_p0/9/*', 39),
                   ]
        for query, count in queries:
            reads = ds1.readsByName(query)
            self.assertEqual(len(reads), count)
            parts = query.split('/')
            movie = parts[0]
            hn = int(parts[1])
            if len(parts) > 2:
                qrange = parts[2]
            for read in reads:
                self.assertEqual(read.movieName, movie)
                self.assertEqual(read.holeNumber, hn)
                # TODO: test qrange/ccs


    #@unittest.skipUnless(os.path.isdir("/pbi/dept/secondary/siv/testdata"),
    #                     "Missing testadata directory")
    @unittest.skip("Too expensive")
    def test_large_pbi(self):
        pbiFn = ('/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/simulated'
                 '/100Gb/alnsubreads/pbalchemy_100Gb_Seq_sim1_p0.'
                 'aligned.bam.pbi')
        pbi = PacBioBamIndex(pbiFn)
        self.assertFalse(pbi.aStart is None)

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

    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_loadMetadata(self):
        aln = AlignmentSet(data.getXml(no=8))
        self.assertFalse(aln.metadata.collections)
        aln.loadMetadata('/pbi/dept/secondary/siv/testdata/'
                         'SA3-Sequel/lambda/roche_SAT/'
                         'm54013_151205_032353.run.metadata.xml')
        self.assertTrue(aln.metadata.collections)
        sset_fn = ('/pbi/dept/secondary/siv/testdata/'
                'SA3-Sequel/lambda/roche_SAT/'
                'm54013_151205_032353.subreadset.xml')
        sset = SubreadSet(sset_fn)
        orig_metadata = copy.deepcopy(sset.metadata)
        sset.metadata.collections = None
        self.assertFalse(sset.metadata.collections)
        sset.loadMetadata('/pbi/dept/secondary/siv/testdata/'
                          'SA3-Sequel/lambda/roche_SAT/'
                          'm54013_151205_032353.run.metadata.xml')
        stack = zip(sset.metadata, orig_metadata)
        fn = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        sset.write(fn)
        validateFile(fn)
        validateFile(sset_fn)
        self.assertEqual(sset.metadata, orig_metadata)


        # load the wrong thing...
        sset_fn = ('/pbi/dept/secondary/siv/testdata/'
                'SA3-Sequel/lambda/roche_SAT/'
                'm54013_151205_032353.subreadset.xml')
        sset = SubreadSet(sset_fn)
        orig_metadata = copy.deepcopy(sset.metadata)
        sset.metadata.collections = None
        self.assertFalse(sset.metadata.collections)
        with self.assertRaises(InvalidDataSetIOError):
            sset.loadMetadata('/pbi/dept/secondary/siv/testdata/'
                              'SA3-Sequel/lambda/roche_SAT/'
                              'm54013_151205_032353.sts.xml')


    def test_copyTo(self):
        aln = AlignmentSet(data.getXml(no=8), strict=True)
        explen = len(aln)
        fn = tempfile.NamedTemporaryFile(suffix=".alignmentset.xml").name
        aln.copyTo(fn)
        aln.close()
        del aln
        aln = AlignmentSet(fn, strict=True)
        self.assertEqual(explen, len(aln))

        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        aln.copyTo(outdir)
        fn = os.path.join(outdir, "test.alignmentset.xml")
        aln.write(fn)
        aln.close()
        del aln
        aln = AlignmentSet(fn, strict=True)
        self.assertEqual(explen, len(aln))

        # do it twice to same dir to induce collisions
        aln = AlignmentSet(data.getXml(no=8), strict=True)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        aln.copyTo(outdir)
        fn = os.path.join(outdir, "test.alignmentset.xml")
        aln.write(fn)

        aln = AlignmentSet(data.getXml(no=8), strict=True)
        aln.copyTo(outdir)
        fn2 = os.path.join(outdir, "test2.alignmentset.xml")
        aln.write(fn2)

        aln = AlignmentSet(fn, strict=True)
        aln2 = AlignmentSet(fn2, strict=True)
        self.assertEqual(explen, len(aln))
        self.assertEqual(explen, len(aln2))
        self.assertNotEqual(sorted(aln.toExternalFiles()),
                            sorted(aln2.toExternalFiles()))

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
                                  strict=False, skipMissing=True).toFofn(),
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
        bogusDS = DataSet("bam1.bam", "bam2.bam", strict=False,
                          skipMissing=True)
        self.assertEqual(['bam1.bam', 'bam2.bam'],
                         bogusDS.externalResources.resourceIds)
        self.assertEquals(
            DataSet("bam1.bam", "bam2.bam", strict=False,
                    skipMissing=True).toExternalFiles(),
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

    def test_reads_in_range_indices(self):
        ds = AlignmentSet(data.getBam())
        refNames = ds.refNames

        rn = refNames[15]
        read_indexes = list(ds.readsInRange(rn, 10, 100, justIndices=True))
        self.assertEqual(len(read_indexes), 10)
        for read in read_indexes:
            self.assertTrue(isinstance(read, int))

        read_index_records = ds.index[read_indexes]

        reads = list(ds.readsInRange(rn, 10, 100, justIndices=False))
        self.assertEqual(len(reads), 10)

        for ri, rr in zip(ds[read_indexes], reads):
            self.assertEqual(ri, rr)


    @unittest.skipUnless(os.path.isdir("/pbi/dept/secondary/siv/testdata"),
                         "Missing testadata directory")
    def test_reads_in_range_order(self):
        log.debug("Testing with one file")
        testFile = ("/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/"
                    "2372215/0007_tiny/Alignment_Results/m150404_101"
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
        self.assertEqual(num, 28)

        log.debug("Testing with three files")
        testFile = ("/pbi/dept/secondary/siv/testdata/SA3-DS/lambda/"
                    "2372215/0007_tiny/Alignment_Results/m150404_101"
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
        self.assertEqual(num, 105)

    @unittest.skipUnless(os.path.isdir("/pbi/dept/secondary/siv/testdata"),
                         "Missing testadata directory")
    def test_reads_in_range_order_large(self):
        window = ('Staphylococcus_aureus_subsp_aureus_USA300_TCH1516',
                  558500,
                  559005)
        log.debug("Testing with one file")
        testFile = ("/pbi/dept/secondary/siv/testdata/"
                    "genomic_consensus-unittest/"
                    "Quiver/staph/m140911_084715_42139_c10070239048"
                    "0000001823141103261514_s1_p0.aligned_subreads.bam")
        aln = AlignmentSet(testFile)
        reads1 = aln.readsInRange(*window, usePbi=False)
        reads2 = aln.readsInRange(*window, usePbi=True)
        num = 0
        for r1, r2 in itertools.izip(reads1, reads2):
            self.assertEqual(r1, r2)
            num += 1
        self.assertTrue(num > 100)


        winId, winStart, winEnd = window
        def lengthInWindow(hit):
            return min(hit.tEnd, winEnd) - max(hit.tStart, winStart)

        log.debug("Testing longest sort vs no pbi")
        aln = AlignmentSet(testFile)
        reads1 = aln.readsInRange(*window, usePbi=False)
        reads2 = aln.readsInRange(*window, usePbi=True, longest=True)
        reads1 = list(reads1)
        reads2 = list(reads2)
        self.assertEqual(len(reads1), len(reads2))
        reads1 = sorted(reads1, key=lengthInWindow, reverse=True)
        for r1, r2 in itertools.izip(reads1, reads2):
            self.assertEqual(r1, r2)

        log.debug("Testing longest sort vs pbi")
        aln = AlignmentSet(testFile)
        reads1 = aln.readsInRange(*window, usePbi=True)
        reads2 = aln.readsInRange(*window, usePbi=True, longest=True)
        reads1 = list(reads1)
        reads2 = list(reads2)
        self.assertEqual(len(reads1), len(reads2))
        reads1 = sorted(reads1, key=lengthInWindow, reverse=True)
        for r1, r2 in itertools.izip(reads1, reads2):
            self.assertEqual(r1, r2)

    def test_n_subreads_filter(self):
        ds2 = AlignmentSet(data.getXml(8))
        ds2.filters.addRequirement(n_subreads=[('>', '4')])
        self.assertEqual(len(list(ds2.records)), 87)
        self.assertEqual(len(ds2), 87)

    def test_filter(self):
        ds2 = AlignmentSet(data.getXml(8))
        ds2.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
        self.assertEqual(len(list(ds2.records)), 20)
        ds2.disableFilters()
        self.assertEqual(len(list(ds2.records)), 92)
        ds2.enableFilters()
        self.assertEqual(len(list(ds2.records)), 20)

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

    def test_intervalContour(self):
        ds = AlignmentSet(data.getBam(0))
        coverage = ds.intervalContour('E.faecalis.1')
        ds.filters.addRequirement(rname=[('=', 'E.faecalis.1')])
        # regular totalLength uses aEnd/aStart, which includes insertions
        totalTargetLength = sum(ds.index.tEnd - ds.index.tStart)
        self.assertEqual(totalTargetLength, sum(coverage))

        # partial interval
        ds = AlignmentSet(data.getBam(0))
        coverage = ds.intervalContour('E.faecalis.1', tStart=100, tEnd=500)
        ds.filters.addRequirement(rname=[('=', 'E.faecalis.1')],
                                  tStart=[('<', '500')],
                                  tEnd=[('>', '100')])
        # regular totalLength uses aEnd/aStart, which includes insertions
        ends = ds.index.tEnd
        post = ends > 500
        ends[post] = 500
        starts = ds.index.tStart
        pre = starts < 100
        starts[pre] = 100
        totalTargetLength = sum(ends - starts)
        self.assertEqual(totalTargetLength, sum(coverage))

        # test a second reference in this set
        ds.filters.removeRequirement('rname')
        coverage = ds.intervalContour('E.faecalis.2')
        ds.filters.addRequirement(rname=[('=', 'E.faecalis.2')])
        totalTargetLength = sum(ds.index.tEnd - ds.index.tStart)
        self.assertEqual(totalTargetLength, sum(coverage))

        # partial interval
        ds = AlignmentSet(data.getBam(0))
        coverage = ds.intervalContour('E.faecalis.2', tStart=100, tEnd=500)
        ds.filters.addRequirement(rname=[('=', 'E.faecalis.2')],
                                  tStart=[('<', '500')],
                                  tEnd=[('>', '100')])
        # regular totalLength uses aEnd/aStart, which includes insertions
        ends = ds.index.tEnd
        post = ends > 500
        ends[post] = 500
        starts = ds.index.tStart
        pre = starts < 100
        starts[pre] = 100
        totalTargetLength = sum(ends - starts)
        self.assertEqual(totalTargetLength, sum(coverage))


        # test a cmp.h5 alignmentset
        ds = AlignmentSet(upstreamdata.getBamAndCmpH5()[1])
        coverage = ds.intervalContour('lambda_NEB3011')
        totalTargetLength = sum(ds.index.tEnd - ds.index.tStart)
        self.assertEqual(totalTargetLength, sum(coverage))

        # partial interval
        ds = AlignmentSet(upstreamdata.getBamAndCmpH5()[1])
        coverage = ds.intervalContour('lambda_NEB3011', tStart=100, tEnd=500)
        ds.filters.addRequirement(rname=[('=', 'lambda_NEB3011')],
                                  tStart=[('<', '500')],
                                  tEnd=[('>', '100')])
        # regular totalLength uses aEnd/aStart, which includes insertions
        starts = ds.index.tStart
        ends = ds.index.tEnd
        post = ends > 500
        ends[post] = 500
        pre = starts < 100
        starts[pre] = 100
        totalTargetLength = sum(ends - starts)
        self.assertEqual(totalTargetLength, sum(coverage))


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

    @unittest.skipIf(not _check_constools(),
                     "bamtools or pbindex not found, skipping")
    def test_induce_indices(self):
        # all of our test files are indexed. Copy just the main files to a temp
        # location, open as dataset, assert unindexed, open with
        # generateIndices=True, assert indexed
        toTest = [8, 9, 10, 11, 12, 15, 16]
        for fileNo in toTest:
            outdir = tempfile.mkdtemp(suffix="dataset-unittest")
            orig_dset = openDataSet(data.getXml(fileNo))
            resfnames = orig_dset.toExternalFiles()
            new_resfnames = []
            for fname in resfnames:
                newfname = os.path.join(outdir, os.path.basename(fname))
                shutil.copy(fname, newfname)
                new_resfnames.append(newfname)
            dset = type(orig_dset)(*new_resfnames)
            self.assertFalse(dset.isIndexed)
            dset = type(orig_dset)(*new_resfnames, generateIndices=True)
            self.assertTrue(dset.isIndexed)


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

    def test_missing_file(self):
        with self.assertRaises(InvalidDataSetIOError):
            aln = AlignmentSet("NOPE")

    def test_repr(self):
        ds = DataSet(data.getBam())
        rep = str(ds)
        self.assertTrue(re.search('DataSet', rep))
        self.assertTrue(re.search('uuid:',
                                  rep))
        self.assertTrue(re.search('pbalchemysim0.pbalign.bam', rep))

    def test_stats_metadata_zero_binwidth(self):
        # both zero
        ds1 = DataSet(data.getXml(8))
        ds1.loadStats(data.getStats())
        ds2 = DataSet(data.getXml(11))
        ds2.loadStats(data.getStats())
        ds1.metadata.summaryStats.readLenDist.bins = (
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(ds1.metadata.summaryStats.readLenDist.bins,
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        ds1.metadata.summaryStats.readLenDist.minBinValue = 0
        ds1.metadata.summaryStats.readLenDist.binWidth = 0
        ds2.metadata.summaryStats.readLenDist.bins = (
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(ds2.metadata.summaryStats.readLenDist.bins,
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        ds2.metadata.summaryStats.readLenDist.minBinValue = 0
        ds2.metadata.summaryStats.readLenDist.binWidth = 0
        ds3 = ds1 + ds2
        self.assertEqual(len(ds3.metadata.summaryStats.readLenDists), 1)
        self.assertEqual(ds3.metadata.summaryStats.readLenDist.bins,
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # one zero
        ds1 = DataSet(data.getXml(8))
        ds1.loadStats(data.getStats())
        ds2 = DataSet(data.getXml(11))
        ds2.loadStats(data.getStats())
        ds1.metadata.summaryStats.readLenDist.bins = (
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(ds1.metadata.summaryStats.readLenDist.bins,
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        ds1.metadata.summaryStats.readLenDist.minBinValue = 0
        ds1.metadata.summaryStats.readLenDist.binWidth = 0
        ds2.metadata.summaryStats.readLenDist.bins = (
            [0, 10, 9, 8, 7, 6, 4, 2, 1, 0, 0, 1])
        self.assertEqual(ds2.metadata.summaryStats.readLenDist.bins,
                         [0, 10, 9, 8, 7, 6, 4, 2, 1, 0, 0, 1])
        ds2.metadata.summaryStats.readLenDist.minBinValue = 20
        ds2.metadata.summaryStats.readLenDist.binWidth = 10
        ds3 = ds1 + ds2
        self.assertEqual(len(ds3.metadata.summaryStats.readLenDists), 1)
        self.assertEqual(ds3.metadata.summaryStats.readLenDist.bins,
                         [0, 10, 9, 8, 7, 6, 4, 2, 1, 0, 0, 1])

        # other zero
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
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(ds2.metadata.summaryStats.readLenDist.bins,
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        ds2.metadata.summaryStats.readLenDist.minBinValue = 0
        ds2.metadata.summaryStats.readLenDist.binWidth = 0
        ds3 = ds1 + ds2
        self.assertEqual(len(ds3.metadata.summaryStats.readLenDists), 1)
        self.assertEqual(ds3.metadata.summaryStats.readLenDist.bins,
                         [0, 10, 9, 8, 7, 6, 4, 2, 1, 0, 0, 1])

        # one zero more zero
        ds1 = DataSet(data.getXml(8))
        ds1.loadStats(data.getStats())
        ds2 = DataSet(data.getXml(11))
        ds2.loadStats(data.getStats())
        ds3 = DataSet(data.getXml(11))
        ds3.loadStats(data.getStats())
        ds1.metadata.summaryStats.readLenDist.bins = (
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(ds1.metadata.summaryStats.readLenDist.bins,
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        ds1.metadata.summaryStats.readLenDist.minBinValue = 0
        ds1.metadata.summaryStats.readLenDist.binWidth = 0
        ds2.metadata.summaryStats.readLenDist.bins = (
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1])
        self.assertEqual(ds2.metadata.summaryStats.readLenDist.bins,
                         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1])
        ds2.metadata.summaryStats.readLenDist.minBinValue = 20
        ds2.metadata.summaryStats.readLenDist.binWidth = 10
        ds3.metadata.summaryStats.readLenDist.bins = (
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(ds3.metadata.summaryStats.readLenDist.bins,
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        ds3.metadata.summaryStats.readLenDist.minBinValue = 0
        ds3.metadata.summaryStats.readLenDist.binWidth = 0
        ds4 = ds1 + ds2 + ds3
        self.assertEqual(len(ds3.metadata.summaryStats.readLenDists), 1)
        self.assertEqual(ds4.metadata.summaryStats.readLenDist.bins,
                         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1])

        # other zero
        ds1 = DataSet(data.getXml(8))
        ds1.loadStats(data.getStats())
        ds2 = DataSet(data.getXml(11))
        ds2.loadStats(data.getStats())
        ds3 = DataSet(data.getXml(11))
        ds3.loadStats(data.getStats())
        ds1.metadata.summaryStats.readLenDist.bins = (
            [0, 10, 9, 8, 7, 6, 4, 2, 1, 0, 0, 1])
        self.assertEqual(ds1.metadata.summaryStats.readLenDist.bins,
                         [0, 10, 9, 8, 7, 6, 4, 2, 1, 0, 0, 1])
        ds1.metadata.summaryStats.readLenDist.minBinValue = 10
        ds1.metadata.summaryStats.readLenDist.binWidth = 10
        ds2.metadata.summaryStats.readLenDist.bins = (
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(ds2.metadata.summaryStats.readLenDist.bins,
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        ds2.metadata.summaryStats.readLenDist.minBinValue = 0
        ds2.metadata.summaryStats.readLenDist.binWidth = 0
        ds3.metadata.summaryStats.readLenDist.bins = (
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(ds3.metadata.summaryStats.readLenDist.bins,
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        ds3.metadata.summaryStats.readLenDist.minBinValue = 0
        ds3.metadata.summaryStats.readLenDist.binWidth = 0
        ds4 = ds1 + ds2 + ds3
        self.assertEqual(len(ds3.metadata.summaryStats.readLenDists), 1)
        self.assertEqual(ds4.metadata.summaryStats.readLenDist.bins,
                         [0, 10, 9, 8, 7, 6, 4, 2, 1, 0, 0, 1])

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
            150292.0,
            ss.subdatasets[1].metadata.summaryStats.numSequencingZmws)

    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_merged_cmp(self):
        cmp1 = ("/pbi/dept/secondary/siv/testdata/pbreports"
                "-unittest/data/sat/aligned_reads.cmp.h5")
        cmp2 = upstreamdata.getBamAndCmpH5()[1]
        aln0 = AlignmentSet(cmp1)
        self.assertEqual(aln0.referenceInfoTable['EndRow'][0], 338001)
        self.assertEqual(len(aln0), 338002)
        aln1 = AlignmentSet(cmp2)
        self.assertEqual(aln1.referenceInfoTable['EndRow'][0], 111)
        self.assertEqual(len(aln1), 112)
        aln = AlignmentSet(cmp1, cmp2)
        refnames = aln.refNames
        self.assertEqual(refnames, ['lambda_NEB3011'])
        self.assertEqual(aln.refIds[aln.refNames[0]], 1)
        self.assertEqual(aln.referenceInfoTable['EndRow'][0], 338113)
        self.assertEqual(len(aln), 338114)

    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_two_cmpH5(self):
        cmp1 = ("/pbi/dept/secondary/siv/testdata/pbreports"
                "-unittest/data/sat/aligned_reads.cmp.h5")
        cmp2 = upstreamdata.getBamAndCmpH5()[1]
        len1 = len(AlignmentSet(cmp1))
        len2 = len(AlignmentSet(cmp2))
        aln = AlignmentSet(cmp1, cmp2)
        len3 = len(aln)
        self.assertEqual(len1 + len2, len3)
        self.assertEqual(len3, 338114)
        self.assertEqual(
            str(aln.referenceInfoTable),
            ("[ (1, 1, 'lambda_NEB3011', 'lambda_NEB3011', "
             "48502, 'a1319ff90e994c8190a4fe6569d0822a', 0L, 338113L)]"))
        self.assertEqual(set(aln.tId), {1})
        # + 1, because bounds are inclusive, rather than exclusive
        self.assertEqual(len3, (aln.referenceInfoTable[0].EndRow -
                                aln.referenceInfoTable[0].StartRow) + 1)
        self.assertEqual(aln.referenceInfo('lambda_NEB3011'),
                         aln.referenceInfo(1))
        # ask for the wrong one:
        self.assertEqual(aln.referenceInfo('ecoliK12_pbi_March2013'),
                         None)

    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_two_ref_cmpH5(self):
        cmp1 = upstreamdata.getBamAndCmpH5()[1]
        cmp2 = ("/pbi/dept/secondary/siv/testdata/"
                "genomic_consensus-unittest/bam_c4p6_tests/"
                "ecoli_c4p6.cmp.h5")
        len1 = len(AlignmentSet(cmp1))
        len2 = len(AlignmentSet(cmp2))
        aln = AlignmentSet(cmp1, cmp2)
        len3 = len(aln)
        self.assertEqual(len1 + len2, len3)
        self.assertEqual(len3, 57147)
        self.assertEqual(
            str(aln.referenceInfoTable),
            ("[ (0, 0, 'ecoliK12_pbi_March2013', 'ecoliK12_pbi_March2013', "
             "4642522, '52cd7c5fa92877152fa487906ae484c5', 0L, 57034L)\n"
             " (1, 1, 'lambda_NEB3011', 'lambda_NEB3011', 48502, "
             "'a1319ff90e994c8190a4fe6569d0822a', 57035L, 57146L)]"))
        self.assertEqual(set(aln.tId), {0, 1})
        # + 1, because bounds are inclusive, rather than exclusive
        self.assertEqual(len1, (aln.referenceInfoTable[1].EndRow -
                                aln.referenceInfoTable[1].StartRow) + 1)
        self.assertEqual(len2, (aln.referenceInfoTable[0].EndRow -
                                aln.referenceInfoTable[0].StartRow) + 1)
        self.assertEqual(aln.referenceInfo('ecoliK12_pbi_March2013'),
                         aln.referenceInfo(0))
        self.assertEqual(aln.referenceInfo('lambda_NEB3011'),
                         aln.referenceInfo(1))


    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_two_bam(self):
        cmp1 = ("/pbi/dept/secondary/siv/testdata/SA3-RS/ecoli/"
                "2590953/0001/Alignment_Results/"
                "m140913_005018_42139_c100713652400000001823152"
                "404301534_s1_p0.1.aligned.bam")
        cmp2 = ("/pbi/dept/secondary/siv/testdata/SA3-RS/ecoli/"
                "2590953/0001/Alignment_Results/"
                "m140913_005018_42139_c100713652400000001823152"
                "404301534_s1_p0.2.aligned.bam")
        len1 = len(AlignmentSet(cmp1))
        len2 = len(AlignmentSet(cmp2))
        aln = AlignmentSet(cmp1, cmp2)
        len3 = len(aln)
        self.assertEqual(len1 + len2, len3)
        self.assertEqual(len3, 65346)
        self.assertEqual(
            str(aln.referenceInfoTable),
            ("[ (0, 0, 'ecoliK12_pbi_March2013', 'ecoliK12_pbi_March2013', "
             "4642522, '52cd7c5fa92877152fa487906ae484c5', 0L, 0L)]"))
        self.assertEqual(set(aln.tId), {0})
        self.assertEqual(aln.referenceInfo('ecoliK12_pbi_March2013'),
                         aln.referenceInfo(0))

    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_two_xml(self):
        cmp1 = ("/pbi/dept/secondary/siv/testdata/"
                "SA3-DS/ecoli/2590953/0001/Alignment_Results/"
                "m140913_005018_42139_c1007136524000000018231"
                "52404301534_s1_p0.all.alignmentset.xml")
        cmp2 = ("/pbi/dept/secondary/siv/testdata/"
                "SA3-DS/ecoli/2590956/0003/Alignment_Results/"
                "m140913_222218_42240_c1006999524000000018231"
                "39203261564_s1_p0.all.alignmentset.xml")
        len1 = len(AlignmentSet(cmp1))
        len2 = len(AlignmentSet(cmp2))
        aln = AlignmentSet(cmp1, cmp2)
        len3 = len(aln)
        self.assertEqual(len1 + len2, len3)
        self.assertEqual(len3, 160264)
        self.assertEqual(
            str(aln.referenceInfoTable),
            ("[ (0, 0, 'ecoliK12_pbi_March2013', 'ecoliK12_pbi_March2013', "
             "4642522, '52cd7c5fa92877152fa487906ae484c5', 0L, 0L)]"))
        self.assertEqual(set(aln.tId), {0})
        self.assertEqual(aln.referenceInfo('ecoliK12_pbi_March2013'),
                         aln.referenceInfo(0))

    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_two_ref_bam(self):
        cmp1 = upstreamdata.getBamAndCmpH5()[0]
        # this is the supposedly the same data as above:
        cmp2 = ("/pbi/dept/secondary/siv/testdata/"
                "SA3-DS/ecoli/2590956/0003/Alignment_Results/"
                "m140913_222218_42240_c1006999524000000018231"
                "39203261564_s1_p0.all.alignmentset.xml")
        len1 = len(AlignmentSet(cmp1))
        len2 = len(AlignmentSet(cmp2))
        aln = AlignmentSet(cmp1, cmp2)
        len3 = len(aln)
        self.assertEqual(len1 + len2, len3)
        self.assertEqual(len3, 57344)
        # TODO(mdsmith)(2016-01-25) I would like to be able to use the startrow
        # and endrow fields for bams someday...
        self.assertEqual(
            str(aln.referenceInfoTable),
            ("[ (0, 0, 'ecoliK12_pbi_March2013', 'ecoliK12_pbi_March2013', "
             "4642522, '52cd7c5fa92877152fa487906ae484c5', 0L, 0L)\n"
             " (1, 1, 'lambda_NEB3011', 'lambda_NEB3011', 48502, "
             "'a1319ff90e994c8190a4fe6569d0822a', 0L, 0L)]"))
        self.assertEqual(set(aln.tId), {0, 1})
        self.assertEqual(aln.referenceInfo('ecoliK12_pbi_March2013'),
                         aln.referenceInfo(0))
        self.assertEqual(aln.referenceInfo('lambda_NEB3011'),
                         aln.referenceInfo(1))

    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_two_ref_three_bam(self):
        # Here we test whether duplicate references in a non-identical
        # reference situation remain duplicates or are collapsed
        cmp1 = upstreamdata.getBamAndCmpH5()[0]
        # this is the supposedly the same data as above:
        cmp2 = ("/pbi/dept/secondary/siv/testdata/"
                "SA3-DS/ecoli/2590956/0003/Alignment_Results/"
                "m140913_222218_42240_c1006999524000000018231"
                "39203261564_s1_p0.all.alignmentset.xml")
        cmp3 = ("/pbi/dept/secondary/siv/testdata/"
                "SA3-DS/ecoli/2590953/0001/Alignment_Results/"
                "m140913_005018_42139_c1007136524000000018231"
                "52404301534_s1_p0.all.alignmentset.xml")
        len1 = len(AlignmentSet(cmp1))
        len2 = len(AlignmentSet(cmp2))
        len3 = len(AlignmentSet(cmp3))
        aln = AlignmentSet(cmp1, cmp2, cmp3)
        len4 = len(aln)
        self.assertEqual(len1 + len2 + len3, len4)
        self.assertEqual(len4, 160376)
        self.assertEqual(
            str(aln.referenceInfoTable),
            ("[ (0, 0, 'ecoliK12_pbi_March2013', 'ecoliK12_pbi_March2013', "
             "4642522, '52cd7c5fa92877152fa487906ae484c5', 0L, 0L)\n"
             " (1, 1, 'lambda_NEB3011', 'lambda_NEB3011', 48502, "
             "'a1319ff90e994c8190a4fe6569d0822a', 0L, 0L)]"))
        self.assertEqual(set(aln.tId), {0, 1})
        self.assertEqual(aln.referenceInfo('ecoliK12_pbi_March2013'),
                         aln.referenceInfo(0))
        self.assertEqual(aln.referenceInfo('lambda_NEB3011'),
                         aln.referenceInfo(1))

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

    def test_exceptions(self):
        try:
            raise InvalidDataSetIOError("Wrong!")
        except InvalidDataSetIOError as e:
            self.assertEqual(e.message, "Wrong!")

    def test_createdAt(self):
        aln = AlignmentSet(data.getXml(8))
        self.assertEqual(aln.createdAt, '2015-08-05T10:25:18')

    def test_divideKeys_keysToRanges(self):
        keys = [0, 1, 2, 3, 5, 8, 50]
        res = divideKeys(keys, 0)
        self.assertEqual(res, [])
        res = keysToRanges(res)
        self.assertEqual(res, [])

        res = divideKeys(keys, 1)
        self.assertEqual(res, [[0, 1, 2, 3, 5, 8, 50]])
        res = keysToRanges(res)
        self.assertEqual(res, [[0, 50]])

        res = divideKeys(keys, 2)
        self.assertEqual(res, [[0, 1, 2], [3, 5, 8, 50]])
        res = keysToRanges(res)
        self.assertEqual(res, [[0, 2], [3, 50]])

        res = divideKeys(keys, 3)
        self.assertEqual(res, [[0, 1], [2, 3], [5, 8, 50]])
        res = keysToRanges(res)
        self.assertEqual(res, [[0, 1], [2, 3], [5, 50]])

        res = divideKeys(keys, 7)
        self.assertEqual(res, [[0], [1], [2], [3], [5], [8], [50]])
        res = keysToRanges(res)
        self.assertEqual(res, [[0, 0], [1, 1], [2, 2], [3, 3],
                               [5, 5], [8, 8], [50, 50]])

        res = divideKeys(keys, 8)
        self.assertEqual(res, [[0], [1], [2], [3], [5], [8], [50]])
        res = keysToRanges(res)
        self.assertEqual(res, [[0, 0], [1, 1], [2, 2], [3, 3],
                               [5, 5], [8, 8], [50, 50]])


        keys = [0, 1, 2, 2, 3, 5, 8, 50, 50]
        res = divideKeys(keys, 0)
        self.assertEqual(res, [])
        res = keysToRanges(res)
        self.assertEqual(res, [])

        res = divideKeys(keys, 1)
        self.assertEqual(res, [[0, 1, 2, 2, 3, 5, 8, 50, 50]])
        res = keysToRanges(res)
        self.assertEqual(res, [[0, 50]])

        res = divideKeys(keys, 2)
        self.assertEqual(res, [[0, 1, 2, 2], [3, 5, 8, 50, 50]])
        res = keysToRanges(res)
        self.assertEqual(res, [[0, 2], [3, 50]])

        res = divideKeys(keys, 3)
        self.assertEqual(res, [[0, 1, 2], [2, 3, 5], [8, 50, 50]])
        res = keysToRanges(res)
        self.assertEqual(res, [[0, 2], [2, 5], [8, 50]])

        res = divideKeys(keys, 9)
        self.assertEqual(res, [[0], [1], [2], [2], [3], [5], [8], [50], [50]])
        res = keysToRanges(res)
        self.assertEqual(res, [[0, 0], [1, 1], [2, 2], [2, 2], [3, 3],
                               [5, 5], [8, 8], [50, 50], [50, 50]])

        res = divideKeys(keys, 10)
        self.assertEqual(res, [[0], [1], [2], [2], [3], [5], [8], [50], [50]])
        res = keysToRanges(res)
        self.assertEqual(res, [[0, 0], [1, 1], [2, 2], [2, 2], [3, 3],
                               [5, 5], [8, 8], [50, 50], [50, 50]])


    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_load_sts_from_extres(self):
        # don't have a subreadset.xml with loaded sts.xml in testdata,
        # fabricate one here:
        ss = SubreadSet(data.getXml(10))
        ss.externalResources[0].sts = ('/pbi/dept/secondary/siv/testdata/'
                                         'SA3-Sequel/lambda/roche_SAT/'
                                         'm54013_151205_032353.sts.xml')
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outXml = os.path.join(outdir, 'tempfile.xml')
        ss.write(outXml)
        ss = SubreadSet(outXml)
        self.assertTrue(ss.metadata.summaryStats)
        # test validation on write with loaded stats:
        outXml = os.path.join(outdir, 'tempfileWithStats.xml')
        ss.write(outXml, validate=False)
        ss.write(outXml)

    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_fixed_bin_sts(self):
        # don't have a subreadset.xml with loaded sts.xml in testdata,
        # fabricate one here:
        ss = SubreadSet(data.getXml(10))
        ss.externalResources[0].sts = ('/pbi/dept/secondary/siv/testdata/'
                                       'pbreports-unittest/data/sts_xml/'
                                       '3120134-r54009_20160323_173308-'
                                       '1_A01-Bug30772/m54009_160323_'
                                       '173323.sts.xml')
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outXml = os.path.join(outdir, 'tempfile.xml')
        outXml2 = os.path.join(outdir, 'tempfile2.xml')
        ss.write(outXml)
        ss.write(outXml2)
        ss = SubreadSet(outXml)
        ss2 = SubreadSet(outXml2)
        ss3 = ss + ss2
        self.assertEqual(ss3.metadata.summaryStats.readLenDist.bins,
                         [b1 + b2 for b1, b2 in
                          zip(ss.metadata.summaryStats.readLenDist.bins,
                              ss2.metadata.summaryStats.readLenDist.bins)])

        # smoke tests
        ss3.metadata.summaryStats.insertReadLenDists
        ss3.metadata.summaryStats.insertReadQualDists

    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_reduced_sts_merging(self):
        # don't have a subreadset.xml with loaded sts.xml in testdata,
        # fabricate one here:

        full = ('/pbi/dept/secondary/siv/testdata/'
                'pbreports-unittest/data/sts_xml/'
                '3120134-r54009_20160323_173308-'
                '1_A01-Bug30772/m54009_160323_'
                '173323.sts.xml')
        partial = ('/pbi/dept/secondary/siv/testdata/'
                   'pbreports-unittest/data/sts_xml/'
                   '32246/m54026_160402_062929.sts.xml')

        # two partial
        ss = SubreadSet(data.getXml(10))
        ss.externalResources[0].sts = partial
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outXml = os.path.join(outdir, 'tempfile.xml')
        outXml2 = os.path.join(outdir, 'tempfile2.xml')
        ss.write(outXml)
        ss.write(outXml2)
        ss = SubreadSet(outXml)
        ss2 = SubreadSet(outXml2)
        ss3 = ss + ss2
        self.assertEqual(ss3.metadata.summaryStats.readLenDist.bins,
                         [b1 + b2 for b1, b2 in
                          zip(ss.metadata.summaryStats.readLenDist.bins,
                              ss2.metadata.summaryStats.readLenDist.bins)])
        ss4 = SubreadSet(outXml, outXml2)

        # one partial one full
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outXml = os.path.join(outdir, 'tempfile.xml')
        outXml2 = os.path.join(outdir, 'tempfile2.xml')
        ss = SubreadSet(data.getXml(10))
        ss.externalResources[0].sts = partial
        ss.write(outXml)
        ss.externalResources[0].sts = full
        ss.write(outXml2)
        ss = SubreadSet(outXml)
        ss2 = SubreadSet(outXml2)
        ss3 = ss + ss2
        self.assertEqual(ss3.metadata.summaryStats.readLenDist.bins,
                         [b1 + b2 for b1, b2 in
                          zip(ss.metadata.summaryStats.readLenDist.bins,
                              ss2.metadata.summaryStats.readLenDist.bins)])
        ss4 = SubreadSet(outXml, outXml2)

        # one full one partial
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outXml = os.path.join(outdir, 'tempfile.xml')
        outXml2 = os.path.join(outdir, 'tempfile2.xml')
        ss = SubreadSet(data.getXml(10))
        ss.externalResources[0].sts = full
        ss.write(outXml)
        ss.externalResources[0].sts = partial
        ss.write(outXml2)
        ss = SubreadSet(outXml)
        ss2 = SubreadSet(outXml2)
        ss3 = ss + ss2
        self.assertEqual(ss3.metadata.summaryStats.readLenDist.bins,
                         [b1 + b2 for b1, b2 in
                          zip(ss.metadata.summaryStats.readLenDist.bins,
                              ss2.metadata.summaryStats.readLenDist.bins)])
        ss4 = SubreadSet(outXml, outXml2)

        # two full
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outXml = os.path.join(outdir, 'tempfile.xml')
        outXml2 = os.path.join(outdir, 'tempfile2.xml')
        ss = SubreadSet(data.getXml(10))
        ss.externalResources[0].sts = full
        ss.write(outXml)
        ss.write(outXml2)
        ss = SubreadSet(outXml)
        ss2 = SubreadSet(outXml2)
        ss3 = ss + ss2
        self.assertEqual(ss3.metadata.summaryStats.readLenDist.bins,
                         [b1 + b2 for b1, b2 in
                          zip(ss.metadata.summaryStats.readLenDist.bins,
                              ss2.metadata.summaryStats.readLenDist.bins)])
        ss4 = SubreadSet(outXml, outXml2)

    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_missing_extres(self):
        # copy a file with relative paths, rescue ResourceId's
        test_file = ('/pbi/dept/secondary/siv/testdata/'
                     'SA3-Sequel/lambda/roche_SAT/'
                     'm54013_151205_032353.subreadset.xml')
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outXml = os.path.join(outdir, 'tempfile.xml')
        resXml = os.path.join(outdir, 'tempfile.rescued.xml')
        sset = SubreadSet(test_file)

        # record the original paths:
        path_map = {}
        recorder = lambda x, m=path_map: m.setdefault(os.path.split(x)[1], x)
        sset._changePaths(recorder)

        # make the paths relative and write out dataset with all missing:
        sset.makePathsRelative(os.path.dirname(test_file))
        sset.write(outXml, validate=False)

        # check that it is broken:
        with self.assertRaises(InvalidDataSetIOError):
            sset = SubreadSet(outXml)

        # check that rescuing fixes it:
        replacer = lambda x, m=path_map: m[x]
        sset = SubreadSet(outXml, skipMissing=True)
        sset._changePaths(replacer)
        sset.write(resXml, validate=False)
        sset = SubreadSet(resXml)

        # check that removing any one breaks it:
        for key in path_map.keys():
            mod_pmap = path_map.copy()

            # remove a resourceId from the map:
            mod_pmap.pop(key)
            log.debug(key)
            # use dict.get to maintain the breakage:
            replacer = lambda x, m=mod_pmap: m.get(x, x)
            sset = SubreadSet(outXml, skipMissing=True)
            sset._changePaths(replacer)
            sset.write(resXml, validate=False)
            with self.assertRaises(InvalidDataSetIOError):
                sset = SubreadSet(resXml)


    @unittest.skip("Too expensive")
    def test_huge_zmw_split(self):
        human = ('/pbi/dept/secondary/siv/testdata/SA3-DS/'
                 'human/JCV_85x_v030/jcv_85x_v030.subreadset.xml')
        sset = SubreadSet(human)
        ssets = sset.split(zmws=True, maxChunks=5)

    def test_get_dataset_uuid(self):
        ds = SubreadSet(upstreamdata.getUnalignedBam(), strict=True)
        ds_file = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        ds.write(ds_file)
        uuid = getDataSetUuid(ds_file)
        self.assertEqual(uuid, ds.uuid)
        with open(ds_file, "w") as out:
            out.write("hello world!")
        uuid = getDataSetUuid(ds_file)
        self.assertEqual(uuid, None)

    def test_get_dataset_metatype(self):
        ds = SubreadSet(upstreamdata.getUnalignedBam(), strict=True)
        ds_file = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        ds.write(ds_file)
        meta_type = getDataSetMetaType(ds_file)
        self.assertEqual(meta_type, "PacBio.DataSet.SubreadSet")
