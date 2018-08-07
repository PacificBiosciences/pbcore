
import unittest

import numpy as np

import pbcore.data
from pbcore.io.align import BamReader
from pbcore.io.align.PacBioBamIndex import PacBioBamIndex, StreamingBamIndex

class TestPbIndex(unittest.TestCase):
    BAM_FILE_NAME = pbcore.data.getUnalignedBam()

    def test_pbindex_bam_consistency(self):
        bam = BamReader(self.BAM_FILE_NAME)
        pbi = PacBioBamIndex(self.BAM_FILE_NAME + ".pbi")
        self.assertEqual(len(pbi), 117)
        for i_rec, rec in enumerate(bam):
            self.assertEqual(rec.qId, pbi.qId[i_rec])
            self.assertEqual(rec.HoleNumber, pbi.holeNumber[i_rec])
            self.assertEqual(rec.qStart, pbi.qStart[i_rec])
            self.assertEqual(rec.qEnd, pbi.qEnd[i_rec])
        self.assertEqual(i_rec, 116)

    def test_pbindex_streaming(self):
        pbi = PacBioBamIndex(self.BAM_FILE_NAME + ".pbi")
        streamed = StreamingBamIndex(self.BAM_FILE_NAME + ".pbi", 20)
        chunks = [chunk for chunk in streamed]
        self.assertTrue(all([len(c)==20 for c in chunks[:-1]]))
        self.assertEqual(len(chunks[-1]), 17)
        for attr in ["qId", "holeNumber", "qStart", "qEnd"]:
            combined = np.concatenate([getattr(c, attr) for c in chunks])
            self.assertEqual(len(combined), len(pbi))
            self.assertTrue(all(combined == getattr(pbi, attr)))

    # with the default chunk size there should be just one chunk identical
    # to the whole index
    def test_pbindex_streaming_entire(self):
        pbi = PacBioBamIndex(self.BAM_FILE_NAME + ".pbi")
        streamed = StreamingBamIndex(self.BAM_FILE_NAME + ".pbi")
        chunked = [chunk for chunk in streamed][0]
        self.assertEqual(len(chunked), len(pbi))
        for attr in ["qId", "holeNumber", "qStart", "qEnd"]:
            self.assertTrue(all(getattr(chunked, attr) == getattr(pbi, attr)))
