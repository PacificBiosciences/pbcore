from __future__ import absolute_import, division, print_function

import numpy as np

import pbcore.data
from pbcore.io.align import BamReader
from pbcore.io.align.PacBioBamIndex import PacBioBamIndex, StreamingBamIndex

class TestPbIndex(object):

    BAM_FILE_NAME = pbcore.data.getUnalignedBam()

    @classmethod
    def setup_class(cls):
        cls._bam = BamReader(cls.BAM_FILE_NAME)
        cls._pbi = PacBioBamIndex(cls.BAM_FILE_NAME + ".pbi")

    def test_pbindex_bam_consistency(self):
        assert len(self._pbi) == 117
        for i_rec, rec in enumerate(self._bam):
            assert rec.qId == self._pbi.qId[i_rec]
            assert rec.HoleNumber == self._pbi.holeNumber[i_rec]
            assert rec.qStart == self._pbi.qStart[i_rec]
            assert rec.qEnd == self._pbi.qEnd[i_rec]
        assert i_rec == 116

    def test_pbindex_streaming(self):
        streamed = StreamingBamIndex(self.BAM_FILE_NAME + ".pbi", 20)
        assert streamed.nchunks == 6
        chunks = [chunk for chunk in streamed]
        for attr in ["qId", "holeNumber", "qStart", "qEnd"]:
            combined = np.concatenate([getattr(c, attr) for c in chunks])
            assert len(combined) == len(self._pbi)
            assert all(combined == getattr(self._pbi, attr))
        chunk = streamed.get_chunk(1)
        for attr in ["qId", "holeNumber", "qStart", "qEnd"]:
            assert all(getattr(chunk, attr) == getattr(chunks[1], attr))

    # with the default chunk size there should be just one chunk identical
    # to the whole index
    def test_pbindex_streaming_entire(self):
        streamed = StreamingBamIndex(self.BAM_FILE_NAME + ".pbi")
        assert streamed.nchunks == 1
        chunked = [chunk for chunk in streamed][0]
        assert len(chunked) == len(self._pbi)
        for attr in ["qId", "holeNumber", "qStart", "qEnd"]:
            assert all(getattr(chunked, attr) == getattr(self._pbi, attr))

    def test_pbindex_with_zmw_index(self):
        """
        Test that the built in sub-index of ZMW start positions is correct.
        """
        streamed = StreamingBamIndex(self.BAM_FILE_NAME + ".pbi", 20)
        unique_zmws = set()
        n_indexed_zmws = 0
        for chunk, zmw_idx in streamed.iter_with_zmw_index():
            for k, zmw_start in enumerate(zmw_idx):
                if k < len(zmw_idx) - 1:
                    idx_max = zmw_idx[k+1]
                else:
                    idx_max = len(chunk)
                zmws = chunk.holeNumber[zmw_start:idx_max]
                assert len(set(zmws)) == 1
                unique_zmws.add(zmws[0])
                n_indexed_zmws += 1
        assert len(unique_zmws) == n_indexed_zmws
