
import logging
from urlparse import urlparse
import unittest
import tempfile
import os
import itertools
import numpy as np

import pysam

from pbcore.util.Process import backticks
from pbcore.io.dataset.utils import (consolidateBams, _infixFname,
                                    BamtoolsVersion)
from pbcore.io import (DataSet, SubreadSet, ConsensusReadSet,
                       ReferenceSet, ContigSet, AlignmentSet, BarcodeSet,
                       FastaReader, FastaWriter, IndexedFastaReader,
                       HdfSubreadSet, ConsensusAlignmentSet,
                       openDataFile, FastaWriter, FastqReader, openDataSet)
import pbcore.data as upstreamData
import pbcore.data.datasets as data
from pbcore.io.dataset.DataSetValidator import validateXml
import xml.etree.ElementTree as ET

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


    def test_subread_build(self):
        ds1 = SubreadSet(data.getXml(no=5), skipMissing=True)
        ds2 = SubreadSet(data.getXml(no=5), skipMissing=True)
        self.assertEquals(type(ds1).__name__, 'SubreadSet')
        self.assertEquals(ds1._metadata.__class__.__name__,
                          'SubreadSetMetadata')
        self.assertEquals(type(ds1._metadata).__name__, 'SubreadSetMetadata')
        self.assertEquals(type(ds1.metadata).__name__, 'SubreadSetMetadata')
        self.assertEquals(len(ds1.metadata.collections), 1)
        self.assertEquals(len(ds2.metadata.collections), 1)
        ds3 = ds1 + ds2
        self.assertEquals(len(ds3.metadata.collections), 2)
        ds4 = SubreadSet(data.getSubreadSet(), skipMissing=True)
        self.assertEquals(type(ds4).__name__, 'SubreadSet')
        self.assertEquals(type(ds4._metadata).__name__, 'SubreadSetMetadata')
        self.assertEquals(len(ds4.metadata.collections), 1)

    def test_valid_referencesets(self):
        validateXml(ET.parse(data.getXml(9)).getroot(), skipResources=True)

    def test_valid_hdfsubreadsets(self):
        validateXml(ET.parse(data.getXml(17)).getroot(), skipResources=True)
        validateXml(ET.parse(data.getXml(18)).getroot(), skipResources=True)
        validateXml(ET.parse(data.getXml(19)).getroot(), skipResources=True)

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

        for name in names:
            self.assertTrue(ds[name].id == name)

    def test_contigset_split(self):
        ref = ReferenceSet(data.getXml(9))
        exp_n_contigs = len(ref)
        refs = ref.split(10)
        self.assertEqual(len(refs), 10)
        obs_n_contigs = 0
        for r in refs:
            obs_n_contigs += sum(1 for _ in r)
        self.assertEqual(obs_n_contigs, exp_n_contigs)


    def test_contigset_len(self):
        ref = ReferenceSet(data.getXml(9))
        exp_n_contigs = len(ref)
        refs = ref.split(10)
        self.assertEqual(len(refs), 10)
        obs_n_contigs = 0
        for r in refs:
            obs_n_contigs += len(r)
        self.assertEqual(obs_n_contigs, exp_n_contigs)


    def test_ccsread_build(self):
        ds1 = ConsensusReadSet(data.getXml(2), strict=False, skipMissing=True)
        self.assertEquals(type(ds1).__name__, 'ConsensusReadSet')
        self.assertEquals(type(ds1._metadata).__name__, 'SubreadSetMetadata')
        ds2 = ConsensusReadSet(data.getXml(2), strict=False, skipMissing=True)
        self.assertEquals(type(ds2).__name__, 'ConsensusReadSet')
        self.assertEquals(type(ds2._metadata).__name__, 'SubreadSetMetadata')

    def test_ccsset_from_bam(self):
        # DONE bug 28698
        ds1 = ConsensusReadSet(upstreamData.getCCSBAM(), strict=False)
        fn = tempfile.NamedTemporaryFile(suffix=".consensusreadset.xml").name
        log.debug(fn)
        ds1.write(fn, validate=False)
        ds1.write(fn)

    def test_subreadset_from_bam(self):
        # DONE control experiment for bug 28698
        bam = upstreamData.getUnalignedBam()
        ds1 = SubreadSet(bam, strict=False)
        fn = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        log.debug(fn)
        ds1.write(fn)

    def test_ccsalignment_build(self):
        ds1 = ConsensusAlignmentSet(data.getXml(20), strict=False,
                                    skipMissing=True)
        self.assertEquals(type(ds1).__name__, 'ConsensusAlignmentSet')
        self.assertEquals(type(ds1._metadata).__name__, 'SubreadSetMetadata')
        # XXX strict=True requires actual existing .bam files
        #ds2 = ConsensusAlignmentSet(data.getXml(20), strict=True)
        #self.assertEquals(type(ds2).__name__, 'ConsensusAlignmentSet')
        #self.assertEquals(type(ds2._metadata).__name__, 'SubreadSetMetadata')

    def test_contigset_write(self):
        fasta = upstreamData.getLambdaFasta()
        ds = ContigSet(fasta)
        self.assertTrue(isinstance(ds.resourceReaders()[0],
                                   IndexedFastaReader))
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'test.fasta')
        w = FastaWriter(outfn)
        for rec in ds:
            w.writeRecord(rec)
        w.close()
        fas = FastaReader(outfn)
        for rec in fas:
            # make sure a __repr__ didn't slip through:
            self.assertFalse(rec.sequence.startswith('<'))

    def test_contigset_empty(self):
        fa_file = tempfile.NamedTemporaryFile(suffix=".fasta").name
        ds_file = tempfile.NamedTemporaryFile(suffix=".contigset.xml").name
        open(fa_file, "w").write("")
        ds = ContigSet(fa_file, strict=False)
        ds.write(ds_file)
        fai_file = fa_file + ".fai"
        open(fai_file, "w").write("")
        ds = ContigSet(fa_file, strict=True)
        ds.write(ds_file)
        self.assertEqual(len(ds), 0)

    def test_file_factory(self):
        # TODO: add ConsensusReadSet, cmp.h5 alignmentSet
        types = [AlignmentSet(data.getXml(8)),
                 ReferenceSet(data.getXml(9)),
                 SubreadSet(data.getXml(10)),
                 #ConsensusAlignmentSet(data.getXml(20)),
                 HdfSubreadSet(data.getXml(19))]
        for ds in types:
            mystery = openDataFile(ds.toExternalFiles()[0])
            self.assertEqual(type(mystery), type(ds))

    def test_file_factory_fofn(self):
        mystery = openDataFile(data.getFofn())
        self.assertEqual(type(mystery), AlignmentSet)

    @unittest.skipUnless(os.path.isdir("/pbi/dept/secondary/siv/testdata/"
                                       "ccs-unittest/tiny"),
                         "Missing testadata directory")
    def test_file_factory_css(self):
        fname = ("/pbi/dept/secondary/siv/testdata/ccs-unittest/"
                 "tiny/little.ccs.bam")
        myster = openDataFile(fname)
        self.assertEqual(type(myster), ConsensusReadSet)


    def test_contigset_build(self):
        ds1 = ContigSet(data.getXml(3), skipMissing=True)
        self.assertEquals(type(ds1).__name__, 'ContigSet')
        self.assertEquals(type(ds1._metadata).__name__, 'ContigSetMetadata')
        ds2 = ContigSet(data.getXml(3), skipMissing=True)
        self.assertEquals(type(ds2).__name__, 'ContigSet')
        self.assertEquals(type(ds2._metadata).__name__, 'ContigSetMetadata')
        for contigmd in ds2.metadata.contigs:
            self.assertEquals(type(contigmd).__name__, 'ContigMetadata')

    @unittest.skipIf(not _check_constools(),
                     "bamtools or pbindex not found, skipping")
    def test_alignmentset_consolidate(self):
        log.debug("Test methods directly")
        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(aln.toExternalFiles()), 2)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        consolidateBams(aln.toExternalFiles(), outfn, filterDset=aln,
                        useTmp=False)
        self.assertTrue(os.path.exists(outfn))
        consAln = AlignmentSet(outfn)
        self.assertEqual(len(consAln.toExternalFiles()), 1)
        for read1, read2 in zip(sorted(list(aln)), sorted(list(consAln))):
            self.assertEqual(read1, read2)
        self.assertEqual(len(aln), len(consAln))

        log.debug("Test methods directly in tmp")
        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(aln.toExternalFiles()), 2)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        consolidateBams(aln.toExternalFiles(), outfn, filterDset=aln,
                        useTmp=True)
        self.assertTrue(os.path.exists(outfn))
        consAln = AlignmentSet(outfn)
        self.assertEqual(len(consAln.toExternalFiles()), 1)
        for read1, read2 in zip(sorted(list(aln)), sorted(list(consAln))):
            self.assertEqual(read1, read2)
        self.assertEqual(len(aln), len(consAln))

        log.debug("Test through API")
        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(aln.toExternalFiles()), 2)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        self.assertTrue(os.path.exists(outfn))
        self.assertEqual(len(aln.toExternalFiles()), 1)
        nonCons = AlignmentSet(data.getXml(12))
        self.assertEqual(len(nonCons.toExternalFiles()), 2)
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            self.assertEqual(read1, read2)
        self.assertEqual(len(aln), len(nonCons))

        # Test that it is a valid xml:
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        datafile = os.path.join(outdir, "apimerged.bam")
        xmlfile = os.path.join(outdir, "apimerged.xml")
        log.debug(xmlfile)
        aln.write(xmlfile)

        log.debug("Test with cheap filter")
        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        aln.filters.addRequirement(rname=[('=', 'B.vulgatus.5')])
        self.assertEqual(len(list(aln)), 7)
        self.assertEqual(len(aln.toExternalFiles()), 2)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        self.assertTrue(os.path.exists(outfn))
        self.assertEqual(len(aln.toExternalFiles()), 1)
        nonCons = AlignmentSet(data.getXml(12))
        nonCons.filters.addRequirement(rname=[('=', 'B.vulgatus.5')])
        self.assertEqual(len(nonCons.toExternalFiles()), 2)
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            self.assertEqual(read1, read2)
        self.assertEqual(len(list(aln)), len(list(nonCons)))

        log.debug("Test with not refname filter")
        # This isn't trivial with bamtools
        """
        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        aln.filters.addRequirement(rname=[('!=', 'B.vulgatus.5')])
        self.assertEqual(len(list(aln)), 7)
        self.assertEqual(len(aln.toExternalFiles()), 2)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        self.assertTrue(os.path.exists(outfn))
        self.assertEqual(len(aln.toExternalFiles()), 1)
        nonCons = AlignmentSet(data.getXml(12))
        nonCons.filters.addRequirement(rname=[('!=', 'B.vulgatus.5')])
        self.assertEqual(len(nonCons.toExternalFiles()), 2)
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            self.assertEqual(read1, read2)
        self.assertEqual(len(list(aln)), len(list(nonCons)))
        """

        log.debug("Test with expensive filter")
        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        aln.filters.addRequirement(accuracy=[('>', '.85')])
        self.assertEqual(len(list(aln)), 174)
        self.assertEqual(len(aln.toExternalFiles()), 2)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        self.assertTrue(os.path.exists(outfn))
        self.assertEqual(len(aln.toExternalFiles()), 1)
        nonCons = AlignmentSet(data.getXml(12))
        nonCons.filters.addRequirement(accuracy=[('>', '.85')])
        self.assertEqual(len(nonCons.toExternalFiles()), 2)
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            self.assertEqual(read1, read2)
        self.assertEqual(len(list(aln)), len(list(nonCons)))

        log.debug("Test with one reference")
        aln = AlignmentSet(data.getXml(12))
        reference = upstreamData.getFasta()
        aln.externalResources[0].reference = reference
        nonCons = aln.copy()
        self.assertEqual(len(aln.toExternalFiles()), 2)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        self.assertTrue(os.path.exists(outfn))
        self.assertEqual(len(aln.toExternalFiles()), 1)
        #nonCons = AlignmentSet(data.getXml(12))
        self.assertEqual(len(nonCons.toExternalFiles()), 2)
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            self.assertEqual(read1, read2)
        self.assertEqual(len(aln), len(nonCons))
        self.assertEqual(aln.externalResources[0].reference, reference)

        log.debug("Test with two references")
        aln = AlignmentSet(data.getXml(12))
        reference = upstreamData.getFasta()
        for extRes in aln.externalResources:
            extRes.reference = reference
        self.assertEqual(len(aln.toExternalFiles()), 2)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        self.assertTrue(os.path.exists(outfn))
        self.assertEqual(len(aln.toExternalFiles()), 1)
        #nonCons = AlignmentSet(data.getXml(12))
        self.assertEqual(len(nonCons.toExternalFiles()), 2)
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            self.assertEqual(read1, read2)
        self.assertEqual(len(aln), len(nonCons))
        self.assertEqual(aln.externalResources[0].reference, reference)


    def test_accuracy_filter(self):
        aln = AlignmentSet(data.getXml(12))
        self.assertEqual(len(list(aln)), 177)
        aln.filters.addRequirement(accuracy=[('>', '.85')])
        self.assertEqual(len(list(aln)), 174)

    def test_contigset_filter(self):
        ref = ReferenceSet(data.getXml(9))
        self.assertEqual(len(list(ref)), 59)
        ref.filters.addRequirement(length=[('>', '1450')])
        self.assertEqual(len(list(ref)), 34)

    @unittest.skipIf(not _check_constools() or not _internal_data(),
                     "bamtools, pbindex or data not found, skipping")
    def test_alignmentset_partial_consolidate(self):
        testFile = ("/pbi/dept/secondary/siv/testdata/SA3-DS/"
                    "lambda/2372215/0007_tiny/Alignment_"
                    "Results/m150404_101626_42267_c10080"
                    "7920800000001823174110291514_s1_p0."
                    "all.alignmentset.xml")
        aln = AlignmentSet(testFile)
        nonCons = AlignmentSet(testFile)
        self.assertEqual(len(aln.toExternalFiles()), 3)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn, numFiles=2)
        self.assertFalse(os.path.exists(outfn))
        self.assertTrue(os.path.exists(_infixFname(outfn, "0")))
        self.assertTrue(os.path.exists(_infixFname(outfn, "1")))
        self.assertEqual(len(aln.toExternalFiles()), 2)
        self.assertEqual(len(nonCons.toExternalFiles()), 3)
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            self.assertEqual(read1, read2)
        self.assertEqual(len(aln), len(nonCons))


    @unittest.skipIf(not _check_constools(),
                     "bamtools or pbindex not found, skipping")
    def test_subreadset_consolidate(self):
        log.debug("Test methods directly")
        aln = SubreadSet(data.getXml(10), data.getXml(13))
        self.assertEqual(len(aln.toExternalFiles()), 2)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        consolidateBams(aln.toExternalFiles(), outfn, filterDset=aln)
        self.assertTrue(os.path.exists(outfn))
        consAln = SubreadSet(outfn)
        self.assertEqual(len(consAln.toExternalFiles()), 1)
        for read1, read2 in zip(sorted(list(aln)), sorted(list(consAln))):
            self.assertEqual(read1, read2)
        self.assertEqual(len(aln), len(consAln))

        log.debug("Test through API")
        aln = SubreadSet(data.getXml(10), data.getXml(13))
        self.assertEqual(len(aln.toExternalFiles()), 2)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        self.assertTrue(os.path.exists(outfn))
        self.assertEqual(len(aln.toExternalFiles()), 1)
        nonCons = SubreadSet(data.getXml(10), data.getXml(13))
        self.assertEqual(len(nonCons.toExternalFiles()), 2)
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            self.assertEqual(read1, read2)
        self.assertEqual(len(aln), len(nonCons))

    def test_contigset_consolidate(self):
        #build set to merge
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")

        inFas = os.path.join(outdir, 'infile.fasta')
        outFas1 = os.path.join(outdir, 'tempfile1.fasta')
        outFas2 = os.path.join(outdir, 'tempfile2.fasta')

        # copy fasta reference to hide fai and ensure FastaReader is used
        backticks('cp {i} {o}'.format(
                      i=ReferenceSet(data.getXml(9)).toExternalFiles()[0],
                      o=inFas))
        rs1 = ContigSet(inFas)

        singletons = ['A.baumannii.1', 'A.odontolyticus.1']
        double = 'B.cereus.1'
        reader = rs1.resourceReaders()[0]
        exp_double = rs1.get_contig(double)
        exp_singles = [rs1.get_contig(name) for name in singletons]

        # todo: modify the names first:
        with FastaWriter(outFas1) as writer:
            writer.writeRecord(exp_singles[0])
            writer.writeRecord(exp_double.name + '_10_20', exp_double.sequence)
        with FastaWriter(outFas2) as writer:
            writer.writeRecord(exp_double.name + '_0_10',
                               exp_double.sequence + 'ATCGATCGATCG')
            writer.writeRecord(exp_singles[1])

        exp_double_seq = ''.join([exp_double.sequence,
                                  'ATCGATCGATCG',
                                  exp_double.sequence])
        exp_single_seqs = [rec.sequence for rec in exp_singles]

        acc_file = ContigSet(outFas1, outFas2)
        acc_file.induceIndices()
        log.debug(acc_file.toExternalFiles())
        self.assertEqual(len(acc_file), 4)
        self.assertEqual(len(list(acc_file)), 4)
        acc_file.consolidate()
        log.debug(acc_file.toExternalFiles())

        # open acc and compare to exp
        for name, seq in zip(singletons, exp_single_seqs):
            self.assertEqual(acc_file.get_contig(name).sequence[:], seq)
        self.assertEqual(acc_file.get_contig(double).sequence[:],
                         exp_double_seq)

        self.assertEqual(len(acc_file._openReaders), 1)
        self.assertEqual(len(acc_file.index), 3)
        self.assertEqual(len(acc_file._indexMap), 3)
        self.assertEqual(len(acc_file), 3)
        self.assertEqual(len(list(acc_file)), 3)

    def test_contigset_consolidate_int_names(self):
        #build set to merge
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")

        inFas = os.path.join(outdir, 'infile.fasta')
        outFas1 = os.path.join(outdir, 'tempfile1.fasta')
        outFas2 = os.path.join(outdir, 'tempfile2.fasta')

        # copy fasta reference to hide fai and ensure FastaReader is used
        backticks('cp {i} {o}'.format(
                      i=ReferenceSet(data.getXml(9)).toExternalFiles()[0],
                      o=inFas))
        rs1 = ContigSet(inFas)

        double = 'B.cereus.1'
        exp_double = rs1.get_contig(double)

        # todo: modify the names first:
        with FastaWriter(outFas1) as writer:
            writer.writeRecord('5141', exp_double.sequence)
        with FastaWriter(outFas2) as writer:
            writer.writeRecord('5142', exp_double.sequence)

        exp_double_seqs = [exp_double.sequence, exp_double.sequence]
        exp_names = ['5141', '5142']

        obs_file = ContigSet(outFas1, outFas2)
        log.debug(obs_file.toExternalFiles())
        obs_file.consolidate()
        log.debug(obs_file.toExternalFiles())

        # open obs and compare to exp
        for name, seq in zip(exp_names, exp_double_seqs):
            self.assertEqual(obs_file.get_contig(name).sequence[:], seq)


    def test_contigset_consolidate_genomic_consensus(self):
        """
        Verify that the contigs output by GenomicConsensus (e.g. quiver) can
        be consolidated.
        """
        FASTA1 = ("lambda_NEB3011_0_60",
            "GGGCGGCGACCTCGCGGGTTTTCGCTATTTATGAAAATTTTCCGGTTTAAGGCGTTTCCG")
        FASTA2 = ("lambda_NEB3011_120_180",
            "CACTGAATCATGGCTTTATGACGTAACATCCGTTTGGGATGCGACTGCCACGGCCCCGTG")
        FASTA3 = ("lambda_NEB3011_60_120",
            "GTGGACTCGGAGCAGTTCGGCAGCCAGCAGGTGAGCCGTAATTATCATCTGCGCGGGCGT")
        files = []
        for i, (header, seq) in enumerate([FASTA1, FASTA2, FASTA3]):
            _files = []
            for suffix in ["", "|quiver", "|plurality", "|arrow", "|poa"]:
                tmpfile = tempfile.NamedTemporaryFile(suffix=".fasta").name
                with open(tmpfile, "w") as f:
                    f.write(">{h}{s}\n{q}".format(h=header, s=suffix, q=seq))
                _files.append(tmpfile)
            files.append(_files)
        for i in range(3):
            ds = ContigSet(*[f[i] for f in files])
            out1 = tempfile.NamedTemporaryFile(suffix=".contigset.xml").name
            fa1 = tempfile.NamedTemporaryFile(suffix=".fasta").name
            ds.consolidate(fa1)
            ds.write(out1)
            with ContigSet(out1) as ds_new:
                self.assertEqual(len([rec for rec in ds_new]), 1,
                                 "failed on %d" % i)

    def test_split_hdfsubreadset(self):
        hdfds = HdfSubreadSet(*upstreamData.getBaxH5_v23())
        self.assertEqual(len(hdfds.toExternalFiles()), 3)
        hdfdss = hdfds.split(chunks=2, ignoreSubDatasets=True)
        self.assertEqual(len(hdfdss), 2)
        self.assertEqual(len(hdfdss[0].toExternalFiles()), 2)
        self.assertEqual(len(hdfdss[1].toExternalFiles()), 1)

    @unittest.skipIf(not _internal_data(),
                     "Internal data not found, skipping")
    def test_len_fastq(self):
        fn = ('/pbi/dept/secondary/siv/testdata/SA3-RS/'
              'lambda/2590980/0008/Analysis_Results/'
              'm141115_075238_ethan_c100699872550000001'
              '823139203261572_s1_p0.1.subreads.fastq')
        fq_out = tempfile.NamedTemporaryFile(suffix=".fastq").name
        with open(fq_out, 'w') as fqh:
            with open(fn, 'r') as fih:
                for line in itertools.islice(fih, 24):
                    fqh.write(line)
        cset = ContigSet(fq_out)
        self.assertFalse(cset.isIndexed)
        self.assertTrue(isinstance(cset.resourceReaders()[0], FastqReader))
        self.assertEqual(sum(1 for _ in cset),
                         sum(1 for _ in FastqReader(fq_out)))
        self.assertEqual(sum(1 for _ in cset), 6)
        # XXX not possible, fastq files can't be indexed:
        #self.assertEqual(len(cset), sum(1 for _ in cset))

    @unittest.skipIf(not _internal_data(),
                     "Internal data not found, skipping")
    def test_fastq_consolidate(self):
        fn = ('/pbi/dept/secondary/siv/testdata/SA3-RS/'
              'lambda/2590980/0008/Analysis_Results/'
              'm141115_075238_ethan_c100699872550000001'
              '823139203261572_s1_p0.1.subreads.fastq')
        fq_out = tempfile.NamedTemporaryFile(suffix=".fastq").name
        cfq_out = tempfile.NamedTemporaryFile(suffix=".fastq").name
        with open(fq_out, 'w') as fqh:
            with open(fn, 'r') as fih:
                for line in itertools.islice(fih, 240):
                    fqh.write(line)
        cset = ContigSet(fq_out)
        cset_l = sum(1 for _ in cset)
        self.assertEqual(cset_l, 60)
        cset.filters.addRequirement(length=[('>', 1000)])
        cset_l = sum(1 for _ in cset)
        self.assertEqual(cset_l, 23)
        cset.consolidate(cfq_out)
        cset_l = sum(1 for _ in cset)
        cfq = FastqReader(cfq_out)
        self.assertEqual(cset_l, 23)
        self.assertEqual(cset_l, sum(1 for _ in cfq))


    @unittest.skipIf(not _internal_data(),
                     "Internal data not found, skipping")
    def test_empty_fastq_consolidate(self):
        fn = ('/pbi/dept/secondary/siv/testdata/SA3-RS/'
              'lambda/2590980/0008/Analysis_Results/'
              'm141115_075238_ethan_c100699872550000001'
              '823139203261572_s1_p0.1.subreads.fastq')
        fq1_out = tempfile.NamedTemporaryFile(suffix="1.fastq").name
        fq2_out = tempfile.NamedTemporaryFile(suffix="2.fastq").name
        cfq_out = tempfile.NamedTemporaryFile(suffix=".fastq").name

        # Two full
        with open(fq1_out, 'w') as fqh:
            with open(fn, 'r') as fih:
                for line in itertools.islice(fih, 240):
                    fqh.write(line)
        with open(fq2_out, 'w') as fqh:
            with open(fn, 'r') as fih:
                for line in itertools.islice(fih, 240, 480):
                    fqh.write(line)
        cset = ContigSet(fq1_out, fq2_out)
        cset_l = sum(1 for _ in cset)
        self.assertEqual(cset_l, 120)
        cset.consolidate(cfq_out)
        cset_l = sum(1 for _ in cset)
        cfq = FastqReader(cfq_out)
        self.assertEqual(cset_l, 120)
        self.assertEqual(cset_l, sum(1 for _ in cfq))

        # one full one empty
        with open(fq1_out, 'w') as fqh:
            with open(fn, 'r') as fih:
                for line in itertools.islice(fih, 240):
                    fqh.write(line)
        with open(fq2_out, 'w') as fqh:
            with open(fn, 'r') as fih:
                fqh.write("")
        cset = ContigSet(fq1_out, fq2_out)
        cset_l = sum(1 for _ in cset)
        self.assertEqual(cset_l, 60)
        cset.consolidate(cfq_out)
        cset_l = sum(1 for _ in cset)
        cfq = FastqReader(cfq_out)
        self.assertEqual(cset_l, 60)
        self.assertEqual(cset_l, sum(1 for _ in cfq))

        # one empty one full
        with open(fq1_out, 'w') as fqh:
            with open(fn, 'r') as fih:
                fqh.write("")
        with open(fq2_out, 'w') as fqh:
            with open(fn, 'r') as fih:
                for line in itertools.islice(fih, 240):
                    fqh.write(line)
        cset = ContigSet(fq1_out, fq2_out)
        cset_l = sum(1 for _ in cset)
        self.assertEqual(cset_l, 60)
        cset.consolidate(cfq_out)
        cset_l = sum(1 for _ in cset)
        cfq = FastqReader(cfq_out)
        self.assertEqual(cset_l, 60)
        self.assertEqual(cset_l, sum(1 for _ in cfq))

        # both empty
        with open(fq1_out, 'w') as fqh:
            with open(fn, 'r') as fih:
                fqh.write("")
        with open(fq2_out, 'w') as fqh:
            with open(fn, 'r') as fih:
                fqh.write("")
        cset = ContigSet(fq1_out, fq2_out)
        cset_l = sum(1 for _ in cset)
        self.assertEqual(cset_l, 0)
        cset.consolidate(cfq_out)
        cset_l = sum(1 for _ in cset)
        cfq = FastqReader(cfq_out)
        self.assertEqual(cset_l, 0)
        self.assertEqual(cset_l, sum(1 for _ in cfq))


    def test_len(self):
        # AlignmentSet
        aln = AlignmentSet(data.getXml(8), strict=True)
        self.assertEqual(len(aln), 92)
        self.assertEqual(aln._length, (92, 123588))
        self.assertEqual(aln.totalLength, 123588)
        self.assertEqual(aln.numRecords, 92)
        aln.totalLength = -1
        aln.numRecords = -1
        self.assertEqual(aln.totalLength, -1)
        self.assertEqual(aln.numRecords, -1)
        aln.updateCounts()
        self.assertEqual(aln.totalLength, 123588)
        self.assertEqual(aln.numRecords, 92)
        self.assertEqual(sum(1 for _ in aln), 92)
        self.assertEqual(sum(len(rec) for rec in aln), 123588)

        # AlignmentSet with filters
        aln = AlignmentSet(data.getXml(15), strict=True)
        self.assertEqual(len(aln), 40)
        self.assertEqual(aln._length, (40, 52023))
        self.assertEqual(aln.totalLength, 52023)
        self.assertEqual(aln.numRecords, 40)
        aln.totalLength = -1
        aln.numRecords = -1
        self.assertEqual(aln.totalLength, -1)
        self.assertEqual(aln.numRecords, -1)
        aln.updateCounts()
        self.assertEqual(aln.totalLength, 52023)
        self.assertEqual(aln.numRecords, 40)

        # AlignmentSet with cmp.h5
        aln = AlignmentSet(upstreamData.getBamAndCmpH5()[1], strict=True)
        self.assertEqual(len(aln), 112)
        self.assertEqual(aln._length, (112, 59970))
        self.assertEqual(aln.totalLength, 59970)
        self.assertEqual(aln.numRecords, 112)
        aln.totalLength = -1
        aln.numRecords = -1
        self.assertEqual(aln.totalLength, -1)
        self.assertEqual(aln.numRecords, -1)
        aln.updateCounts()
        self.assertEqual(aln.totalLength, 59970)
        self.assertEqual(aln.numRecords, 112)


        # SubreadSet
        sset = SubreadSet(data.getXml(10), strict=True)
        self.assertEqual(len(sset), 92)
        self.assertEqual(sset._length, (92, 124093))
        self.assertEqual(sset.totalLength, 124093)
        self.assertEqual(sset.numRecords, 92)
        sset.totalLength = -1
        sset.numRecords = -1
        self.assertEqual(sset.totalLength, -1)
        self.assertEqual(sset.numRecords, -1)
        sset.updateCounts()
        self.assertEqual(sset.totalLength, 124093)
        self.assertEqual(sset.numRecords, 92)
        self.assertEqual(sum(1 for _ in sset), 92)
        self.assertEqual(sum(len(rec) for rec in sset), 124093)

        # HdfSubreadSet
        # len means something else in bax/bas land. These numbers may actually
        # be correct...
        sset = HdfSubreadSet(data.getXml(17), strict=True)
        self.assertEqual(len(sset), 9)
        self.assertEqual(sset._length, (9, 128093))
        self.assertEqual(sset.totalLength, 128093)
        self.assertEqual(sset.numRecords, 9)
        sset.totalLength = -1
        sset.numRecords = -1
        self.assertEqual(sset.totalLength, -1)
        self.assertEqual(sset.numRecords, -1)
        sset.updateCounts()
        self.assertEqual(sset.totalLength, 128093)
        self.assertEqual(sset.numRecords, 9)

        # ReferenceSet
        sset = ReferenceSet(data.getXml(9), strict=True)
        self.assertEqual(len(sset), 59)
        self.assertEqual(sset.totalLength, 85774)
        self.assertEqual(sset.numRecords, 59)
        sset.totalLength = -1
        sset.numRecords = -1
        self.assertEqual(sset.totalLength, -1)
        self.assertEqual(sset.numRecords, -1)
        sset.updateCounts()
        self.assertEqual(sset.totalLength, 85774)
        self.assertEqual(sset.numRecords, 59)

    def test_alignment_reference(self):
        rs1 = ReferenceSet(data.getXml(9))
        fasta_res = rs1.externalResources[0]
        fasta_file = urlparse(fasta_res.resourceId).path

        ds1 = AlignmentSet(data.getXml(8),
            referenceFastaFname=rs1)
        aln_ref = None
        for aln in ds1:
            aln_ref = aln.reference()
            break
        self.assertTrue(aln_ref is not None)

        ds1 = AlignmentSet(data.getXml(8),
            referenceFastaFname=fasta_file)
        aln_ref = None
        for aln in ds1:
            aln_ref = aln.reference()
            break
        self.assertTrue(aln_ref is not None)

        ds1 = AlignmentSet(data.getXml(8))
        ds1.addReference(fasta_file)
        aln_ref = None
        for aln in ds1:
            aln_ref = aln.reference()
            break
        self.assertTrue(aln_ref is not None)

    def test_nested_external_resources(self):
        log.debug("Testing nested externalResources in AlignmentSets")
        aln = AlignmentSet(data.getXml(0), skipMissing=True)
        self.assertTrue(aln.externalResources[0].pbi)
        self.assertTrue(aln.externalResources[0].reference)
        self.assertEqual(
            aln.externalResources[0].externalResources[0].metaType,
            'PacBio.ReferenceFile.ReferenceFastaFile')
        self.assertEqual(aln.externalResources[0].scraps, None)

        log.debug("Testing nested externalResources in SubreadSets")
        subs = SubreadSet(data.getXml(5), skipMissing=True)
        self.assertTrue(subs.externalResources[0].scraps)
        self.assertEqual(
            subs.externalResources[0].externalResources[0].metaType,
            'PacBio.SubreadFile.ScrapsBamFile')
        self.assertEqual(subs.externalResources[0].reference, None)

        log.debug("Testing added nested externalResoruces to SubreadSet")
        subs = SubreadSet(data.getXml(10))
        self.assertFalse(subs.externalResources[0].scraps)
        subs.externalResources[0].scraps = 'fake.fasta'
        self.assertTrue(subs.externalResources[0].scraps)
        self.assertEqual(
            subs.externalResources[0].externalResources[0].metaType,
            'PacBio.SubreadFile.ScrapsBamFile')
        subs.externalResources[0].barcodes = 'bc.fasta'
        self.assertTrue(subs.externalResources[0].barcodes)
        self.assertEqual(
            subs.externalResources[0].externalResources[1].metaType,
            "PacBio.DataSet.BarcodeSet")

        log.debug("Testing adding nested externalResources to AlignmetnSet "
                  "manually")
        aln = AlignmentSet(data.getXml(8))
        self.assertTrue(aln.externalResources[0].bai)
        self.assertTrue(aln.externalResources[0].pbi)
        self.assertFalse(aln.externalResources[0].reference)
        aln.externalResources[0].reference = 'fake.fasta'
        self.assertTrue(aln.externalResources[0].reference)
        self.assertEqual(
            aln.externalResources[0].externalResources[0].metaType,
            'PacBio.ReferenceFile.ReferenceFastaFile')

        # Disabling until this feature is considered valuable. At the moment I
        # think it might cause accidental pollution.
        #log.debug("Testing adding nested externalResources to AlignmetnSet "
        #          "on construction")
        #aln = AlignmentSet(data.getXml(8), referenceFastaFname=data.getXml(9))
        #self.assertTrue(aln.externalResources[0].bai)
        #self.assertTrue(aln.externalResources[0].pbi)
        #self.assertTrue(aln.externalResources[0].reference)
        #self.assertEqual(
        #    aln.externalResources[0].externalResources[0].metaType,
        #    'PacBio.ReferenceFile.ReferenceFastaFile')

        #log.debug("Testing adding nested externalResources to "
        #          "AlignmentSets with multiple external resources "
        #          "on construction")
        #aln = AlignmentSet(data.getXml(12), referenceFastaFname=data.getXml(9))
        #for i in range(1):
        #    self.assertTrue(aln.externalResources[i].bai)
        #    self.assertTrue(aln.externalResources[i].pbi)
        #    self.assertTrue(aln.externalResources[i].reference)
        #    self.assertEqual(
        #        aln.externalResources[i].externalResources[0].metaType,
        #        'PacBio.ReferenceFile.ReferenceFastaFile')


    def test_contigset_index(self):
        fasta = upstreamData.getLambdaFasta()
        ds = ContigSet(fasta)
        self.assertEqual(ds[0].name, "lambda_NEB3011")

    def test_alignmentset_index(self):
        aln = AlignmentSet(upstreamData.getBamAndCmpH5()[1], strict=True)
        reads = aln.readsInRange(aln.refNames[0], 0, 1000)
        self.assertEqual(len(list(reads)), 2)
        self.assertEqual(len(list(aln)), 112)
        self.assertEqual(len(aln.index), 112)

    def test_barcodeset(self):
        fa_out = tempfile.NamedTemporaryFile(suffix=".fasta").name
        with open(fa_out, "w") as f:
            f.write(">bc1\nAAAAAAAAAAAAAAAA\n>bc2\nCCCCCCCCCCCCCCCC")
        ds = BarcodeSet(fa_out)
        ds.induceIndices()
        self.assertEqual([r.id for r in ds], ["bc1","bc2"])
        ds_out = tempfile.NamedTemporaryFile(suffix=".barcodeset.xml").name
        ds.write(ds_out)

    @unittest.skipIf(not _internal_data(),
                     "Internal data not found, skipping")
    def test_barcode_split_cornercases(self):
        fn = ('/pbi/dept/secondary/siv/testdata/'
              'pblaa-unittest/Sequel/Phi29/m54008_160219_003234'
              '.tiny.subreadset.xml')
        sset = SubreadSet(fn)
        ssets = sset.split(chunks=3, barcodes=True)
        self.assertEqual([str(ss.filters) for ss in ssets],
                         ["( bc = [0, 0] )",
                          "( bc = [1, 1] )",
                          "( bc = [2, 2] )"])
        sset = SubreadSet(fn)
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

    def test_merged_contigset(self):
        fn = tempfile.NamedTemporaryFile(suffix=".contigset.xml").name
        with ContigSet(upstreamData.getLambdaFasta(),
                upstreamData.getFasta()) as cset:
            self.assertEqual(len(list(cset)), 49)
            self.assertEqual(len(cset), 49)
            cset.consolidate()
            cset.write(fn)
            log.debug("Writing to {f}".format(f=fn))
            self.assertEqual(len(list(cset)), 49)
            self.assertEqual(len(cset), 49)
        with ContigSet(fn) as cset:
            self.assertEqual(len(list(cset)), 49)
            self.assertEqual(len(cset), 49)

    def test_getitem(self):
        types = [AlignmentSet(data.getXml(8)),
                 ReferenceSet(data.getXml(9)),
                 SubreadSet(data.getXml(10)),
                ]
        for ds in types:
            self.assertTrue(ds[0])


    def test_incorrect_len_getitem(self):
        types = [AlignmentSet(data.getXml(8)),
                 ReferenceSet(data.getXml(9)),
                 SubreadSet(data.getXml(10)),
                 HdfSubreadSet(data.getXml(19))]
        fn = tempfile.NamedTemporaryFile(suffix=".xml").name
        for ds in types:
            explen = -2
            with openDataFile(ds.toExternalFiles()[0]) as mystery:
                # try to avoid crashes...
                explen = len(mystery)
                mystery.numRecords = 1000000000
                mystery.write(fn)
            with openDataFile(fn) as mystery:
                self.assertEqual(len(list(mystery)), explen)

    def test_missing_fai_error_message(self):
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")

        inFas = os.path.join(outdir, 'infile.fasta')

        # copy fasta reference to hide fai and ensure FastaReader is used
        backticks('cp {i} {o}'.format(
            i=ReferenceSet(data.getXml(9)).toExternalFiles()[0],
            o=inFas))
        rs1 = ContigSet(inFas)
        with self.assertRaises(IOError) as cm:
            rs1.assertIndexed()
        self.assertEqual(
            str(cm.exception),
            ( "Companion FASTA index (.fai) file not found or malformatted! "
             "Use 'samtools faidx' to generate FASTA index."))
