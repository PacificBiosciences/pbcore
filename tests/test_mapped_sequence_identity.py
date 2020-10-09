"""
This is a rather silly functional grouping, as opposed to the module-based
organization of our other tests, but these methods are so closely related
that it makes more sense to test them together.
"""

import pytest
import numpy as np

from pbcore.util.statistics import (pb_identity,
                                    blast_identity,
                                    gap_compressed_identity)
from pbcore.io import AlignmentSet, BamReader, IndexedBamReader

from pbtestdata import get_file


def _compare_identity(x1, x2):
    assert pytest.approx(x1, 0.0001) == x2


class ExpectedValues:
    """
    Expected function outputs for the 
    """
    PB_IDENTITY = [0.9283, 0.9475]
    BLAST_IDENTITY = [0.9295, 0.9493]
    GC_IDENTITY = [0.9383, 0.9520]


class TestUtilsIdentity(ExpectedValues):

    def test_pb_identity(self):
        expected = self.PB_IDENTITY + [0]
        x = [
            pb_identity(5, 35, 13, 739),
            pb_identity(2, 4, 12, 343),
            pb_identity(1, 1, 1200, 400)
        ]
        _compare_identity(x, expected)
        nMM = np.array([5, 2, 1])
        nIns = np.array([35, 4, 1])
        nDel = np.array([13, 12, 1200])
        rl = np.array([739, 343, 400])
        ids = pb_identity(nMM, nIns, nDel, rl)
        np.testing.assert_almost_equal(ids, expected, decimal=4)

    def test_blast_identity(self):
        x = [
            blast_identity(699, 5, 35, 13),
            blast_identity(337, 2, 4, 12)
        ]
        _compare_identity(x, self.BLAST_IDENTITY)
        nM = np.array([699, 337])
        nMM = np.array([5, 2])
        nIns = np.array([35, 4])
        nDel = np.array([13, 12])
        ids = blast_identity(nM, nMM, nIns, nDel)
        np.testing.assert_almost_equal(ids, self.BLAST_IDENTITY, decimal=4)

    def test_gap_compressed_identity(self):
        x = [
            gap_compressed_identity(699, 5, 28, 13),
            gap_compressed_identity(337, 2, 3, 12)
        ]
        _compare_identity(x, self.GC_IDENTITY)
        nM = np.array([699, 337])
        nMM = np.array([5, 2])
        nInsOps = np.array([28, 3])
        nDelOps = np.array([13, 12])
        ids = gap_compressed_identity(nM, nMM, nInsOps, nDelOps)
        np.testing.assert_almost_equal(ids, self.GC_IDENTITY, decimal=4)


class TestBamIdentity(ExpectedValues):

    def _get_bam_pbi(self):
        bam = get_file("aligned-bam")
        return (iter(BamReader(bam)), iter(IndexedBamReader(bam)))

    def test_record_pb_identity(self):
        bam, bam_pbi = self._get_bam_pbi()
        x = [next(bam).pb_identity for i in range(2)]
        _compare_identity(x, self.PB_IDENTITY)
        x = [next(bam_pbi).pb_identity for i in range(2)]
        _compare_identity(x, self.PB_IDENTITY)

    def test_record_blast_identity(self):
        bam, bam_pbi = self._get_bam_pbi()
        x = [next(bam).blast_identity for i in range(2)]
        _compare_identity(x, self.BLAST_IDENTITY)
        x = [next(bam_pbi).blast_identity for i in range(2)]
        _compare_identity(x, self.BLAST_IDENTITY)

    def test_record_gc_identity(self):
        bam, bam_pbi = self._get_bam_pbi()
        x = [next(bam).gap_compressed_identity for i in range(2)]
        _compare_identity(x, self.GC_IDENTITY)
        x = [next(bam_pbi).gap_compressed_identity for i in range(2)]
        _compare_identity(x, self.GC_IDENTITY)


class TestPbiIdentity(ExpectedValues):

    def _get_pbi(self):
        ds = AlignmentSet(get_file("aligned-xml"))
        return ds.resourceReaders()[0].pbi

    def test_pbi_pb_identity(self):
        _compare_identity(self._get_pbi().pb_identity[0:2], self.PB_IDENTITY)

    def test_pbi_blast_identity(self):
        _compare_identity(self._get_pbi().blast_identity[0:2], self.BLAST_IDENTITY)

    # FIXME this will not work with this version .pbi
    #def test_pbi_pb_identity(self):
    #    _compare_identity(_get_pbi().pb_identity, self.GC_IDENTITY)
