import itertools
import logging
import os
import pytest
import tempfile
import time
import uuid
import shutil
import numpy as np
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

import pysam

from pbcore.io.dataset.utils import _infixFname, consolidateXml
from pbcore.io import (SubreadSet, ConsensusReadSet,
                       ReferenceSet, ContigSet, AlignmentSet, BarcodeSet,
                       FastaReader, FastaWriter, IndexedFastaReader,
                       ConsensusAlignmentSet,
                       openDataFile, FastqReader,
                       TranscriptSet, BedSet)
import pbcore.data as upstreamData
import pbcore.data.datasets as data
from pbcore.io.dataset.DataSetValidator import validateXml

log = logging.getLogger(__name__)


class TestDataSet:
    """Unit and integration tests for the DataSet class and
    associated module functions"""

    def test_subread_build(self):
        ds1 = SubreadSet(data.getXml(no=5), skipMissing=True)
        ds2 = SubreadSet(data.getXml(no=5), skipMissing=True)
        assert type(ds1).__name__ == 'SubreadSet'
        assert ds1._metadata.__class__.__name__ == 'SubreadSetMetadata'
        assert type(ds1._metadata).__name__ == 'SubreadSetMetadata'
        assert type(ds1.metadata).__name__ == 'SubreadSetMetadata'
        assert len(ds1.metadata.collections) == 1
        assert len(ds2.metadata.collections) == 1
        ds3 = ds1 + ds2
        assert len(ds3.metadata.collections) == 2
        ds4 = SubreadSet(data.getSubreadSet(), skipMissing=True)
        assert type(ds4).__name__ == 'SubreadSet'
        assert type(ds4._metadata).__name__ == 'SubreadSetMetadata'
        assert len(ds4.metadata.collections) == 1

    def test_subreadset_metadata_element_name(self):
        # without touching the element:
        sset = SubreadSet(data.getXml(9))
        log.debug(data.getXml(9))
        fn = tempfile.NamedTemporaryFile(suffix=".subreadset.xml")
        log.debug(fn.name)
        sset.write(fn.name)
        f = ET.parse(fn.name)
        assert len(f.getroot().findall(
            '{http://pacificbiosciences.com/PacBioDatasets.xsd}'
            'SubreadSetMetadata')) == 0
        assert len(f.getroot().findall(
            '{http://pacificbiosciences.com/PacBioDatasets.xsd}'
            'DataSetMetadata')) == 1
        fn.close()

        # with touching the element:
        sset = SubreadSet(data.getXml(9))
        sset.metadata.description = 'foo'
        fn = tempfile.NamedTemporaryFile(suffix=".subreadset.xml")
        sset.write(fn.name, validate=False)
        f = ET.parse(fn.name)
        assert len(f.getroot().findall(
            '{http://pacificbiosciences.com/PacBioDatasets.xsd}'
            'SubreadSetMetadata')) == 0
        assert len(f.getroot().findall(
            '{http://pacificbiosciences.com/PacBioDatasets.xsd}'
            'DataSetMetadata')) == 1
        fn.close()

    def test_valid_referencesets(self):
        validateXml(ET.parse(data.getXml(8)).getroot(), skipResources=True)

    def test_autofilled_metatypes(self):
        ds = ReferenceSet(data.getXml(8))
        for extRes in ds.externalResources:
            assert extRes.metaType == 'PacBio.ReferenceFile.ReferenceFastaFile'
            assert len(extRes.indices) == 1
            for index in extRes.indices:
                assert index.metaType == "PacBio.Index.SamIndex"
        ds = AlignmentSet(data.getXml(7))
        for extRes in ds.externalResources:
            assert extRes.metaType == 'PacBio.SubreadFile.SubreadBamFile'
            assert len(extRes.indices) == 2
            for index in extRes.indices:
                if index.resourceId.endswith('pbi'):
                    assert index.metaType == "PacBio.Index.PacBioIndex"
                if index.resourceId.endswith('bai'):
                    assert index.metaType == "PacBio.Index.BamIndex"

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
        ds = ReferenceSet(data.getXml(8))
        log.debug([contig.id for contig in ds])
        for contig, name, seqlen in zip(ds.contigs, names, seqlens):
            assert contig.id == name
            assert len(contig.sequence) == seqlen

        for name in names:
            assert ds.get_contig(name)

        for name in names:
            assert ds[name].id == name

    def test_contigset_len(self):
        ref = ReferenceSet(data.getXml(8))
        exp_n_contigs = len(ref)
        refs = ref.split(10)
        assert len(refs) == 10
        obs_n_contigs = 0
        for r in refs:
            obs_n_contigs += len(r)
        assert obs_n_contigs == exp_n_contigs

    def test_ccsread_build(self):
        ds1 = ConsensusReadSet(data.getXml(2), strict=False, skipMissing=True)
        assert type(ds1).__name__ == 'ConsensusReadSet'
        assert type(ds1._metadata).__name__ == 'SubreadSetMetadata'
        ds2 = ConsensusReadSet(data.getXml(2), strict=False, skipMissing=True)
        assert type(ds2).__name__ == 'ConsensusReadSet'
        assert type(ds2._metadata).__name__ == 'SubreadSetMetadata'

    def test_ccsset_from_bam(self):
        # DONE bug 28698
        ds1 = ConsensusReadSet(upstreamData.getCCSBAM(), strict=False)
        fn = tempfile.NamedTemporaryFile(suffix=".consensusreadset.xml")
        log.debug(fn.name)
        ds1.write(fn.name, validate=False)
        ds1.write(fn.name)
        fn.close()

    def test_subreadset_from_bam(self):
        # DONE control experiment for bug 28698
        bam = upstreamData.getUnalignedBam()
        ds1 = SubreadSet(bam, strict=False)
        fn = tempfile.NamedTemporaryFile(suffix=".subreadset.xml")
        log.debug(fn.name)
        ds1.write(fn.name)
        fn.close()

    def test_ccsalignment_build(self):
        ds1 = ConsensusAlignmentSet(data.getXml(16), strict=False,
                                    skipMissing=True)
        assert type(ds1).__name__ == 'ConsensusAlignmentSet'
        assert type(ds1._metadata).__name__ == 'SubreadSetMetadata'
        # XXX strict=True requires actual existing .bam files
        #ds2 = ConsensusAlignmentSet(data.getXml(16), strict=True)
        #assert type(ds2).__name__ == 'ConsensusAlignmentSet'
        #assert type(ds2._metadata).__name__ == 'SubreadSetMetadata'

    def test_contigset_write(self):
        fasta = upstreamData.getLambdaFasta()
        ds = ContigSet(fasta)
        assert isinstance(ds.resourceReaders()[0], IndexedFastaReader)
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'test.fasta')
        w = FastaWriter(outfn)
        for rec in ds:
            w.writeRecord(rec)
        w.close()
        fas = FastaReader(outfn)
        for rec in fas:
            # make sure a __repr__ didn't slip through:
            assert not rec.sequence.startswith('<')

    def test_contigset_empty(self):
        fa_file = tempfile.NamedTemporaryFile(suffix=".fasta")
        ds_file = tempfile.NamedTemporaryFile(suffix=".contigset.xml")
        open(fa_file.name, "w").write("")
        ds = ContigSet(fa_file.name, strict=False)
        ds.write(ds_file.name)
        fai_file = fa_file.name + ".fai"
        open(fai_file, "w").write("")
        ds = ContigSet(fa_file.name, strict=True)
        ds.write(ds_file.name)
        assert len(ds) == 0
        fa_file.close()
        ds_file.close()

    def test_file_factory(self):
        # TODO: add ConsensusReadSet, cmp.h5 alignmentSet
        types = [AlignmentSet(data.getXml(7)),
                 ReferenceSet(data.getXml(8)),
                 SubreadSet(data.getXml(9))]
        for ds in types:
            mystery = openDataFile(ds.toExternalFiles()[0])
            assert type(mystery) == type(ds)

    def test_file_factory_fofn(self):
        mystery = openDataFile(data.getFofn())
        assert type(mystery) == AlignmentSet

    @pytest.mark.internal_data
    def test_file_factory_css(self):
        fname = ("/pbi/dept/secondary/siv/testdata/ccs-unittest/"
                 "tiny/little.ccs.bam")
        myster = openDataFile(fname)
        assert type(myster) == ConsensusReadSet

    def test_contigset_build(self):
        ds1 = ContigSet(data.getXml(3), skipMissing=True)
        assert type(ds1).__name__ == 'ContigSet'
        assert type(ds1._metadata).__name__ == 'ContigSetMetadata'
        ds2 = ContigSet(data.getXml(3), skipMissing=True)
        assert type(ds2).__name__ == 'ContigSet'
        assert type(ds2._metadata).__name__ == 'ContigSetMetadata'

    @pytest.mark.constools
    def test_pbmerge(self):
        log.debug("Test through API")
        aln = AlignmentSet(data.getXml(11))
        assert len(aln.toExternalFiles()) == 2
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        log.info(outfn)

        consolidateXml(aln, outfn, cleanup=False)
        assert os.path.exists(outfn)
        assert os.path.exists(outfn + '.pbi')
        cons = AlignmentSet(outfn)
        assert len(aln) == len(cons)
        orig_stats = os.stat(outfn + '.pbi')

        cons.externalResources[0].pbi = None
        assert cons.externalResources[0].pbi is None
        # test is too quick, stat times might be within the same second
        time.sleep(1)
        cons.induceIndices()
        assert outfn + '.pbi' == cons.externalResources[0].pbi
        assert orig_stats == os.stat(cons.externalResources[0].pbi)

        cons.externalResources[0].pbi = None
        assert cons.externalResources[0].pbi is None
        # test is too quick, stat times might be within the same second
        time.sleep(1)
        cons.induceIndices(force=True)
        assert orig_stats != os.stat(cons.externalResources[0].pbi)

        aln = AlignmentSet(data.getXml(11))
        assert len(aln.toExternalFiles()) == 2
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        log.info(outfn)

        consolidateXml(aln, outfn, cleanup=False, useTmp=False)
        assert os.path.exists(outfn)
        assert os.path.exists(outfn + '.pbi')
        cons = AlignmentSet(outfn)
        assert len(aln) == len(cons)
        orig_stats = os.stat(outfn + '.pbi')

    @pytest.mark.constools
    def test_pbmerge_indexing(self):
        log.debug("Test through API")
        aln = AlignmentSet(data.getXml(11))
        assert len(aln.toExternalFiles()) == 2
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        log.info(outfn)
        consolidateXml(aln, outfn, cleanup=False)
        assert os.path.exists(outfn)
        assert os.path.exists(outfn + '.pbi')
        cons = AlignmentSet(outfn)
        assert len(aln) == len(cons)
        orig_stats = os.stat(outfn + '.pbi')
        cons.externalResources[0].pbi = None
        assert cons.externalResources[0].pbi is None
        # test is too quick, stat times might be within the same second
        time.sleep(1)
        cons.induceIndices()
        assert outfn + '.pbi' == cons.externalResources[0].pbi
        assert orig_stats == os.stat(cons.externalResources[0].pbi)
        cons.externalResources[0].pbi = None
        assert cons.externalResources[0].pbi is None
        # test is too quick, stat times might be within the same second
        time.sleep(1)
        cons.induceIndices(force=True)
        assert orig_stats != os.stat(cons.externalResources[0].pbi)

    @pytest.mark.constools
    def test_alignmentset_consolidate(self):
        log.debug("Test through API")
        aln = AlignmentSet(data.getXml(11))
        assert len(aln.toExternalFiles()) == 2
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        assert os.path.exists(outfn)
        assert len(aln.toExternalFiles()) == 1
        nonCons = AlignmentSet(data.getXml(11))
        assert len(nonCons.toExternalFiles()) == 2
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            assert read1 == read2
        assert len(aln) == len(nonCons)

        # Test that it is a valid xml:
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        datafile = os.path.join(outdir, "apimerged.bam")
        xmlfile = os.path.join(outdir, "apimerged.xml")
        log.debug(xmlfile)
        aln.write(xmlfile)

        log.debug("Test with cheap filter")
        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        aln.filters.addRequirement(rname=[('=', 'B.vulgatus.5')])
        assert len(list(aln)) == 7
        assert len(aln.toExternalFiles()) == 2
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        assert os.path.exists(outfn)
        assert len(aln.toExternalFiles()) == 1
        nonCons = AlignmentSet(data.getXml(11))
        nonCons.filters.addRequirement(rname=[('=', 'B.vulgatus.5')])
        assert len(nonCons.toExternalFiles()) == 2
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            assert read1 == read2
        assert len(list(aln)) == len(list(nonCons))

        log.debug("Test with not refname filter")
        # This isn't trivial with bamtools
        """
        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        aln.filters.addRequirement(rname=[('!=', 'B.vulgatus.5')])
        assert len(list(aln)) == 7
        assert len(aln.toExternalFiles()) == 2
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        assert os.path.exists(outfn)
        assert len(aln.toExternalFiles()) == 1
        nonCons = AlignmentSet(data.getXml(11))
        nonCons.filters.addRequirement(rname=[('!=', 'B.vulgatus.5')])
        assert len(nonCons.toExternalFiles()) == 2
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            assert read1 == read2
        assert len(list(aln)) == len(list(nonCons))
        """

        log.debug("Test with expensive filter")
        aln = AlignmentSet(data.getXml(11))
        assert len(list(aln)) == 177
        aln.filters.addRequirement(accuracy=[('>', '.85')])
        assert len(list(aln)) == 174
        assert len(aln.toExternalFiles()) == 2
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        assert os.path.exists(outfn)
        assert len(aln.toExternalFiles()) == 1
        nonCons = AlignmentSet(data.getXml(11))
        nonCons.filters.addRequirement(accuracy=[('>', '.85')])
        assert len(nonCons.toExternalFiles()) == 2
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            assert read1 == read2
        assert len(list(aln)) == len(list(nonCons))

        log.debug("Test with one reference")
        aln = AlignmentSet(data.getXml(11))
        reference = upstreamData.getFasta()
        aln.externalResources[0].reference = reference
        nonCons = aln.copy()
        assert len(aln.toExternalFiles()) == 2
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        assert os.path.exists(outfn)
        assert len(aln.toExternalFiles()) == 1
        #nonCons = AlignmentSet(data.getXml(11))
        assert len(nonCons.toExternalFiles()) == 2
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            assert read1 == read2
        assert len(aln) == len(nonCons)
        assert aln.externalResources[0].reference == reference

        log.debug("Test with two references")
        aln = AlignmentSet(data.getXml(11))
        reference = upstreamData.getFasta()
        for extRes in aln.externalResources:
            extRes.reference = reference
        assert len(aln.toExternalFiles()) == 2
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        assert os.path.exists(outfn)
        assert len(aln.toExternalFiles()) == 1
        #nonCons = AlignmentSet(data.getXml(11))
        assert len(nonCons.toExternalFiles()) == 2
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            assert read1 == read2
        assert len(aln) == len(nonCons)
        assert aln.externalResources[0].reference == reference

    @pytest.mark.internal_data
    @pytest.mark.constools
    def test_alignmentset_partial_consolidate(self):
        testFile = ("/pbi/dept/secondary/siv/testdata/SA3-DS/"
                    "lambda/2372215/0007_tiny/Alignment_"
                    "Results/m150404_101626_42267_c10080"
                    "7920800000001823174110291514_s1_p0."
                    "all.alignmentset.xml")
        aln = AlignmentSet(testFile)
        nonCons = AlignmentSet(testFile)
        assert len(aln.toExternalFiles()) == 3
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn, numFiles=2)
        assert not os.path.exists(outfn)
        assert os.path.exists(_infixFname(outfn, "0"))
        assert os.path.exists(_infixFname(outfn, "1"))
        assert len(aln.toExternalFiles()) == 2
        assert len(nonCons.toExternalFiles()) == 3
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            assert read1 == read2
        assert len(aln) == len(nonCons)

    @pytest.mark.constools
    def test_subreadset_consolidate(self):
        log.debug("Test through API")
        aln = SubreadSet(data.getXml(9), data.getXml(12))
        assert len(aln.toExternalFiles()) == 2
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")
        outfn = os.path.join(outdir, 'merged.bam')
        aln.consolidate(outfn)
        assert os.path.exists(outfn)
        assert len(aln.toExternalFiles()) == 1

        # lets make sure we're not getting extra entries:
        assert len(aln.externalResources) == 1
        assert len(aln.externalResources[0].indices) == 2

        nonCons = SubreadSet(data.getXml(9), data.getXml(12))
        assert len(nonCons.toExternalFiles()) == 2
        for read1, read2 in zip(sorted(list(aln)), sorted(list(nonCons))):
            assert read1 == read2
        assert len(aln) == len(nonCons)

    def test_contigset_consolidate(self):
        # build set to merge
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")

        inFas = os.path.join(outdir, 'infile.fasta')
        outFas1 = os.path.join(outdir, 'tempfile1.fasta')
        outFas2 = os.path.join(outdir, 'tempfile2.fasta')

        # copy fasta reference to hide fai and ensure FastaReader is used
        shutil.copyfile(ReferenceSet(data.getXml(8)).toExternalFiles()[0],
                        inFas)
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
        assert len(acc_file) == 4
        assert len(list(acc_file)) == 4
        acc_file.consolidate()
        log.debug(acc_file.toExternalFiles())

        # open acc and compare to exp
        for name, seq in zip(singletons, exp_single_seqs):
            assert acc_file.get_contig(name).sequence[:] == seq
        assert acc_file.get_contig(double).sequence[:] == exp_double_seq

        assert len(acc_file._openReaders) == 1
        assert len(acc_file.index) == 3
        assert len(acc_file._indexMap) == 3
        assert len(acc_file) == 3
        assert len(list(acc_file)) == 3

        # test merge:
        acc1 = ContigSet(outFas1)
        acc2 = ContigSet(outFas2)
        acc3 = acc1 + acc2

    def test_contigset_consolidate_int_names(self):
        # build set to merge
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")

        inFas = os.path.join(outdir, 'infile.fasta')
        outFas1 = os.path.join(outdir, 'tempfile1.fasta')
        outFas2 = os.path.join(outdir, 'tempfile2.fasta')

        # copy fasta reference to hide fai and ensure FastaReader is used
        shutil.copyfile(ReferenceSet(
            data.getXml(8)).toExternalFiles()[0], inFas)
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
            assert obs_file.get_contig(name).sequence[:] == seq

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
                assert len([rec for rec in ds_new]) == 1

    @pytest.mark.internal_data
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
        assert not cset.isIndexed
        assert isinstance(cset.resourceReaders()[0], FastqReader)
        assert sum(1 for _ in cset) == sum(1 for _ in FastqReader(fq_out))
        assert sum(1 for _ in cset) == 6
        # XXX not possible, fastq files can't be indexed:
        #assert len(cset) == sum(1 for _ in cset)

    @pytest.mark.internal_data
    def test_fastq_consolidate(self):
        fn = ('/pbi/dept/secondary/siv/testdata/SA3-RS/'
              'lambda/2590980/0008/Analysis_Results/'
              'm141115_075238_ethan_c100699872550000001'
              '823139203261572_s1_p0.1.subreads.fastq')
        fq_out = tempfile.NamedTemporaryFile(suffix=".fastq").name
        cfq_out = tempfile.NamedTemporaryFile(suffix=".fastq").name
        cset_out = tempfile.NamedTemporaryFile(suffix=".contigset.xml").name
        with open(fq_out, 'w') as fqh:
            with open(fn, 'r') as fih:
                for line in itertools.islice(fih, 240):
                    fqh.write(line)
        cset = ContigSet(fq_out)
        cset_l = sum(1 for _ in cset)
        assert cset_l == 60
        cset.filters.addRequirement(length=[('>', 1000)])
        cset_l = sum(1 for _ in cset)
        assert cset_l == 23
        cset.consolidate(cfq_out)
        cset_l = sum(1 for _ in cset)
        cfq = FastqReader(cfq_out)
        assert cset_l == 23
        assert cset_l == sum(1 for _ in cfq)
        cset.write(cset_out)

    @pytest.mark.internal_data
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
        assert cset_l == 120
        cset.consolidate(cfq_out)
        cset_l = sum(1 for _ in cset)
        cfq = FastqReader(cfq_out)
        assert cset_l == 120
        assert cset_l == sum(1 for _ in cfq)

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
        assert cset_l == 60
        cset.consolidate(cfq_out)
        cset_l = sum(1 for _ in cset)
        cfq = FastqReader(cfq_out)
        assert cset_l == 60
        assert cset_l == sum(1 for _ in cfq)

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
        assert cset_l == 60
        cset.consolidate(cfq_out)
        cset_l = sum(1 for _ in cset)
        cfq = FastqReader(cfq_out)
        assert cset_l == 60
        assert cset_l == sum(1 for _ in cfq)

        # both empty
        with open(fq1_out, 'w') as fqh:
            with open(fn, 'r') as fih:
                fqh.write("")
        with open(fq2_out, 'w') as fqh:
            with open(fn, 'r') as fih:
                fqh.write("")
        cset = ContigSet(fq1_out, fq2_out)
        cset_l = sum(1 for _ in cset)
        assert cset_l == 0
        cset.consolidate(cfq_out)
        cset_l = sum(1 for _ in cset)
        cfq = FastqReader(cfq_out)
        assert cset_l == 0
        assert cset_l == sum(1 for _ in cfq)

    def test_len(self):
        # AlignmentSet
        aln = AlignmentSet(data.getXml(7), strict=True)
        assert len(aln) == 92
        assert aln._length == (92, 123588)
        assert aln.totalLength == 123588
        assert aln.numRecords == 92
        aln.totalLength = -1
        aln.numRecords = -1
        assert aln.totalLength == -1
        assert aln.numRecords == -1
        aln.updateCounts()
        assert aln.totalLength == 123588
        assert aln.numRecords == 92
        assert sum(1 for _ in aln) == 92
        assert sum(len(rec) for rec in aln) == 123588

        # AlignmentSet with filters
        aln = AlignmentSet(data.getXml(14), strict=True)
        assert len(aln) == 40
        assert aln._length == (40, 52023)
        assert aln.totalLength == 52023
        assert aln.numRecords == 40
        aln.totalLength = -1
        aln.numRecords = -1
        assert aln.totalLength == -1
        assert aln.numRecords == -1
        aln.updateCounts()
        assert aln.totalLength == 52023
        assert aln.numRecords == 40

        # SubreadSet
        sset = SubreadSet(data.getXml(9), strict=True)
        assert len(sset) == 92
        assert sset._length == (92, 124093)
        assert sset.totalLength == 124093
        assert sset.numRecords == 92
        sset.totalLength = -1
        sset.numRecords = -1
        assert sset.totalLength == -1
        assert sset.numRecords == -1
        sset.updateCounts()
        assert sset.totalLength == 124093
        assert sset.numRecords == 92
        assert sum(1 for _ in sset) == 92
        assert sum(len(rec) for rec in sset) == 124093

        # ReferenceSet
        sset = ReferenceSet(data.getXml(8), strict=True)
        assert len(sset) == 59
        assert sset.totalLength == 85774
        assert sset.numRecords == 59
        sset.totalLength = -1
        sset.numRecords = -1
        assert sset.totalLength == -1
        assert sset.numRecords == -1
        sset.updateCounts()
        assert sset.totalLength == 85774
        assert sset.numRecords == 59

    def test_alignment_reference(self):
        rfn = data.getXml(8)
        rs1 = ReferenceSet(data.getXml(8))
        fasta_res = rs1.externalResources[0]
        fasta_file = urlparse(fasta_res.resourceId).path

        ds1 = AlignmentSet(data.getXml(7),
                           referenceFastaFname=rs1)
        aln_ref = None
        for aln in ds1:
            aln_ref = aln.reference()
            break
        assert aln_ref is not None
        assert ds1.externalResources[0].reference == fasta_file
        assert ds1.resourceReaders()[0].referenceFasta.filename == fasta_file

        ds1 = AlignmentSet(data.getXml(7),
                           referenceFastaFname=fasta_file)
        aln_ref = None
        for aln in ds1:
            aln_ref = aln.reference()
            break
        assert aln_ref is not None
        assert ds1.externalResources[0].reference == fasta_file
        assert ds1.resourceReaders()[0].referenceFasta.filename == fasta_file

        ds1 = AlignmentSet(data.getXml(7))
        ds1.addReference(fasta_file)
        aln_ref = None
        for aln in ds1:
            aln_ref = aln.reference()
            break
        assert aln_ref is not None
        assert ds1.externalResources[0].reference == fasta_file
        assert ds1.resourceReaders()[0].referenceFasta.filename == fasta_file

        fofn_out = tempfile.NamedTemporaryFile(suffix=".fofn").name
        log.debug(fofn_out)
        with open(fofn_out, 'w') as f:
            f.write(data.getXml(7))
            f.write('\n')
            f.write(data.getXml(10))
            f.write('\n')
        ds1 = AlignmentSet(fofn_out,
                           referenceFastaFname=fasta_file)
        aln_ref = None
        for aln in ds1:
            aln_ref = aln.reference()
            break
        assert aln_ref is not None
        assert ds1.externalResources[0].reference == fasta_file
        assert ds1.resourceReaders()[0].referenceFasta.filename == fasta_file

        # Re-enable when referenceset is acceptable reference
        # ds1 = AlignmentSet(data.getXml(7),
        #                   referenceFastaFname=rfn)
        #aln_ref = None
        # for aln in ds1:
        #    aln_ref = aln.reference()
        #    break
        #assert aln_ref is not None
        #assert isinstance(aln_ref, basestring)
        # assert ds1.externalResources[0]._getSubExtResByMetaType(
        #            'PacBio.ReferenceFile.ReferenceFastaFile').uniqueId == rs1.uuid

    @pytest.mark.internal_data
    def test_adapters_resource(self):
        ifn = ("/pbi/dept/secondary/siv/testdata/BlasrTestData/ctest/data/"
               "m54075_161031_164015.subreadset.xml")
        s = SubreadSet(ifn)
        assert s.externalResources[0].adapters.endswith(
            'm54075_161031_164015_adapter.fasta')
        ifn = ("/pbi/dept/secondary/siv/testdata/SA3-Sequel/ecoli/315/"
               "3150319/r54011_20160727_213451/1_A01/"
               "m54011_160727_213918.subreads.bam")
        s = SubreadSet(ifn)
        assert s.externalResources[0].adapters.endswith(
            'm54011_160727_213918.adapters.fasta')

    def test_nested_external_resources(self):
        log.debug("Testing nested externalResources in AlignmentSets")
        aln = AlignmentSet(data.getXml(0), skipMissing=True)
        assert aln.externalResources[0].pbi
        assert aln.externalResources[0].reference
        assert aln.externalResources[0].externalResources[0].metaType == 'PacBio.ReferenceFile.ReferenceFastaFile'
        assert aln.externalResources[0].scraps is None

        log.debug("Testing nested externalResources in SubreadSets")
        subs = SubreadSet(data.getXml(5), skipMissing=True)
        assert subs.externalResources[0].scraps
        assert subs.externalResources[0].externalResources[0].metaType == 'PacBio.SubreadFile.ScrapsBamFile'
        assert subs.externalResources[0].reference is None

        log.debug("Testing added nested externalResoruces to SubreadSet")
        subs = SubreadSet(data.getXml(9))
        assert not subs.externalResources[0].scraps
        subs.externalResources[0].scraps = 'fake.fasta'
        assert subs.externalResources[0].scraps
        assert subs.externalResources[0].externalResources[0].metaType == 'PacBio.SubreadFile.ScrapsBamFile'
        subs.externalResources[0].barcodes = 'bc.fasta'
        assert subs.externalResources[0].barcodes
        assert subs.externalResources[0].externalResources[1].metaType == "PacBio.DataSet.BarcodeSet"

        subs.externalResources[0].adapters = 'foo.adapters.fasta'
        assert subs.externalResources[0].adapters == 'foo.adapters.fasta'
        assert subs.externalResources[0].externalResources[2].metaType == "PacBio.SubreadFile.AdapterFastaFile"

        log.debug("Testing adding nested externalResources to AlignmetnSet "
                  "manually")
        aln = AlignmentSet(data.getXml(7))
        assert aln.externalResources[0].bai
        assert aln.externalResources[0].pbi
        assert aln.externalResources[0].reference is None
        aln.externalResources[0].reference = 'fake.fasta'
        assert aln.externalResources[0].reference
        assert aln.externalResources[0].externalResources[0].metaType == 'PacBio.ReferenceFile.ReferenceFastaFile'

        # Disabling until this feature is considered valuable. At the moment I
        # think it might cause accidental pollution.
        # log.debug("Testing adding nested externalResources to AlignmetnSet "
        #          "on construction")
        #aln = AlignmentSet(data.getXml(7), referenceFastaFname=data.getXml(8))
        #assert aln.externalResources[0].bai
        #assert aln.externalResources[0].pbi
        #assert aln.externalResources[0].reference
        # assert aln.externalResources[0].externalResources[0].metaType == 'PacBio.ReferenceFile.ReferenceFastaFile')

        # log.debug("Testing adding nested externalResources to "
        #          "AlignmentSets with multiple external resources "
        #          "on construction")
        #aln = AlignmentSet(data.getXml(11), referenceFastaFname=data.getXml(8))
        # for i in range(1):
        #    assert aln.externalResources[i].bai
        #    assert aln.externalResources[i].pbi
        #    assert aln.externalResources[i].reference
        #    assert aln.externalResources[i].externalResources[0].metaType == 'PacBio.ReferenceFile.ReferenceFastaFile')

    def test_contigset_index(self):
        fasta = upstreamData.getLambdaFasta()
        ds = ContigSet(fasta)
        assert ds[0].name == "lambda_NEB3011"

    def test_barcodeset(self):
        fa_out = tempfile.NamedTemporaryFile(suffix=".fasta").name
        with open(fa_out, "w") as f:
            f.write(">bc1\nAAAAAAAAAAAAAAAA\n>bc2\nCCCCCCCCCCCCCCCC")
        ds = BarcodeSet(fa_out)
        ds.induceIndices()
        assert [r.id for r in ds] == ["bc1", "bc2"]
        ds_out = tempfile.NamedTemporaryFile(suffix=".barcodeset.xml").name
        ds.write(ds_out)

    def test_merged_contigset(self):
        fn = tempfile.NamedTemporaryFile(suffix=".contigset.xml").name
        with ContigSet(upstreamData.getLambdaFasta(),
                       upstreamData.getFasta()) as cset:
            assert len(list(cset)) == 49
            assert len(cset) == 49
            cset.consolidate()
            cset.write(fn)
            log.debug("Writing to {f}".format(f=fn))
            assert len(list(cset)) == 49
            assert len(cset) == 49
        with ContigSet(fn) as cset:
            assert len(list(cset)) == 49
            assert len(cset) == 49

    def test_getitem(self):
        types = [AlignmentSet(data.getXml(7)),
                 ReferenceSet(data.getXml(8)),
                 SubreadSet(data.getXml(9)),
                 ]
        for ds in types:
            assert ds[0]

    def test_incorrect_len_getitem(self):
        types = [AlignmentSet(data.getXml(7)),
                 ReferenceSet(data.getXml(8)),
                 SubreadSet(data.getXml(9))]
        fn = tempfile.NamedTemporaryFile(suffix=".xml").name
        for ds in types:
            explen = -2
            with openDataFile(ds.toExternalFiles()[0]) as mystery:
                # try to avoid crashes...
                explen = len(mystery)
                mystery.numRecords = 1000000000
                mystery.write(fn)
            with openDataFile(fn) as mystery:
                assert len(list(mystery)) == explen

    def test_missing_fai_error_message(self):
        outdir = tempfile.mkdtemp(suffix="dataset-unittest")

        inFas = os.path.join(outdir, 'infile.fasta')

        # copy fasta reference to hide fai and ensure FastaReader is used
        shutil.copyfile(ReferenceSet(
            data.getXml(8)).toExternalFiles()[0], inFas)
        rs1 = ContigSet(inFas)
        with pytest.raises(IOError) as cm:
            rs1.assertIndexed()
            assert str(cm) == (
                "Companion FASTA index (.fai) file not found or malformatted! "
                "Use 'samtools faidx' to generate FASTA index.")

    def test_subreads_parent_dataset(self):
        ds1 = SubreadSet(data.getXml(no=5), skipMissing=True)
        assert ds1.metadata.provenance.parentDataSet.uniqueId == "f81cf391-b3da-41f8-84cb-a0de71f460f4"
        ds2 = SubreadSet(ds1.externalResources[0].bam, skipMissing=True)
        assert ds2.metadata.provenance.parentDataSet.uniqueId is None
        ds2.metadata.addParentDataSet("f81cf391-b3da-41f8-84cb-a0de71f460f4",
                                      "PacBio.DataSet.SubreadSet",
                                      "timestamped_name")
        assert ds2.metadata.provenance.parentDataSet.uniqueId == "f81cf391-b3da-41f8-84cb-a0de71f460f4"
        ds_out = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        ds2.write(ds_out, validate=False)

    def test_provenance_record_ordering(self):
        import pbtestdata
        ds = SubreadSet(pbtestdata.get_file("subreads-sequel"), strict=True)
        ds.metadata.addParentDataSet(
            uuid.uuid4(), ds.datasetType, createdBy="AnalysisJob", timeStampedName="")
        tmp_out = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        ds.write(tmp_out)
        ds = SubreadSet(tmp_out, strict=True)
        tags = [r['tag'] for r in ds.metadata.record['children']]
        assert tags == ['TotalLength', 'NumRecords',
                        'Provenance', 'Collections', 'SummaryStats']

    @pytest.mark.internal_data
    def test_transcriptset(self):
        fn = "/pbi/dept/secondary/siv/testdata/isoseqs/TranscriptSet/unpolished.transcriptset.xml"
        ds1 = TranscriptSet(fn, strict=True)
        assert len(ds1.resourceReaders()) == 1

    def test_consensus_read_set_ref(self):
        import pbtestdata
        ds = ConsensusReadSet(pbtestdata.get_file("ccs-sequel"), strict=True)
        uuid = ds.metadata.collections[0].consensusReadSetRef.uuid
        assert uuid == "5416f525-d3c7-496b-ba8c-18d7ec1b4499"

    @pytest.mark.skip(reason="Missing BAM resource")
    @pytest.mark.internal_data
    def test_subreads_sts_xml_merge_zero_division(self):
        fn = "/pbi/dept/secondary/siv/testdata/pbcore-unittest/data/merged.dataset.xml"
        # this just needs to not crash
        assert SubreadSet(fn) is not None

    def test_permissive_empty_bam(self):
        fn = upstreamData.getEmptyBam2()
        ds = AlignmentSet(fn)
        assert len(ds) == 0

    @pytest.mark.constools
    def test_generate_indices(self):
        import pbtestdata
        tmp_bam = tempfile.NamedTemporaryFile(suffix=".subreads.bam").name
        tmp_pbi = tmp_bam + ".pbi"
        tmp_bai = tmp_bam + ".bai"
        shutil.copyfile(pbtestdata.get_file("subreads-bam"), tmp_bam)
        ds = openDataFile(tmp_bam, strict=False, generateIndices=True)
        assert ds.externalResources[0].pbi == tmp_pbi
        assert ds.externalResources[0].bai == tmp_bai
        assert os.path.isfile(tmp_pbi)
        assert os.path.isfile(tmp_bai)
        assert len(ds) == 117

    def test_trust_counts(self):
        import pbtestdata
        f1 = pbtestdata.get_file("aligned-xml")
        f2 = pbtestdata.get_file("aligned-ds-2")
        ds = openDataFile(f1, f2, trustCounts=True)
        assert ds.numRecords == 133
        assert len(ds) == 133
        assert ds.totalLength == 274217
        assert ds._index is None
        assert len(ds._openReaders) == 0

    def test_referenceset_fsa_extension(self):
        tmp_fsa = tempfile.NamedTemporaryFile(suffix=".fsa").name
        with open(tmp_fsa, "wt") as fsa_out:
            fsa_out.write(">chr1\nacgt")
        pysam.faidx(tmp_fsa)
        ds = openDataFile(tmp_fsa, strict=True)
        assert isinstance(ds, ReferenceSet)
        assert ds.numRecords == 1
        assert ds.totalLength == 4

    @pytest.mark.internal_data
    def test_different_references(self):
        lambda_alnset = ('/pbi/dept/secondary/siv/testdata/pbcore-unittest/'
                         'data/lambda/2372215/0007_tiny/Alignment_Results/'
                         'm150404_101626_42267_c10080792080000000182317411'
                         '0291514_s1_p0.1.aligned.bam')
        ecoli_alnset = ('/pbi/dept/secondary/siv/testdata/pbcore-unittest/'
                        'data/ecoli/2590953/0001/Alignment_Results/'
                        'm140913_005018_42139_c100713652400000001823152404'
                        '301534_s1_p0.1.aligned.bam')
        combined = AlignmentSet(lambda_alnset, ecoli_alnset)
        assert len(combined.referenceInfoTable) == 2
        assert isinstance(combined.referenceInfoTable, np.recarray)

    @pytest.mark.internal_data
    def test_bams_multiple_barcodes_one_movie(self):
        DATA = "/pbi/dept/secondary/siv/testdata/pbcore-unittest/data/multi_bc_bam/mapped.consensusalignmentset.xml"
        ds = ConsensusAlignmentSet(DATA)
        assert len(ds.resourceReaders()) == 1
        assert len(ds.readGroupTable) == 4

    def test_reference_fasta_meta_type(self):
        fasta = upstreamData.getLambdaFasta()
        ds = ReferenceSet(fasta)
        assert ds.externalResources[0].metaType == "PacBio.ReferenceFile.ReferenceFastaFile"

    @pytest.mark.internal_data
    def test_load_supplemental_stats(self):
        DATA = "/pbi/dept/secondary/siv/testdata/smrtlink-functional/rhino-demux/m64000e_211108_120000.consensusreadset.xml"
        ds = ConsensusReadSet(DATA)
        ds.loadStats()
        assert ds.metadata.summaryStats

    @pytest.mark.constools
    def test_bedset(self):
        import pbtestdata
        bed_xml = pbtestdata.get_file("bedset")
        ds = BedSet(bed_xml)
        assert os.path.isfile(ds.externalResources[0].resourceId)
        records = ds.resourceReaders()[0]
        assert len(records) == 2
