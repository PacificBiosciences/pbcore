import logging
import tempfile
import os.path as op
import os

import pytest
import numpy as np

from pbcore.io.dataset.DataSetMetaTypes import dsIdToSuffix
from pbcore.io import (DataSetMetaTypes, divideKeys, splitKeys,
                       SubreadSet, getDataSetUuid, getDataSetMetaType)
from pbcore.io.dataset.utils import split_keys_around_read_groups, collection_file_resolver

import pbcore.data as upstreamdata

import pbtestdata

log = logging.getLogger(__name__)


def keysToRanges(keys):
    key_ranges = [[min(k), max(k)] for k in keys]
    return key_ranges


class TestDataSetUtils:
    """Unit and integrationt tests for the DataSet class and \
    associated module functions"""

    def test_get_dataset_uuid(self):
        ds = SubreadSet(upstreamdata.getUnalignedBam(), strict=True)
        ds_file = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        ds.write(ds_file)
        uuid = getDataSetUuid(ds_file)
        assert uuid == ds.uuid
        with open(ds_file, "w") as out:
            out.write("hello world!")
        uuid = getDataSetUuid(ds_file)
        assert uuid is None

    def test_get_dataset_metatype(self):
        ds = SubreadSet(upstreamdata.getUnalignedBam(), strict=True)
        ds_file = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        ds.write(ds_file)
        meta_type = getDataSetMetaType(ds_file)
        assert meta_type == "PacBio.DataSet.SubreadSet"

    def test_dsIdToSuffix(self):
        suffixes = ['subreadset.xml', 'alignmentset.xml',
                    'barcodeset.xml', 'consensusreadset.xml',
                    'consensusalignmentset.xml',
                    'referenceset.xml', 'contigset.xml']
        for dsId, exp in zip(DataSetMetaTypes.ALL, suffixes):
            assert dsIdToSuffix(dsId) == exp

    def test_divideKeys_keysToRanges(self):
        keys = [0, 1, 2, 3, 5, 8, 50]
        res = divideKeys(keys, 0)
        assert res == []
        res = keysToRanges(res)
        assert res == []

        res = divideKeys(keys, 1)
        assert res == [[0, 1, 2, 3, 5, 8, 50]]
        res = keysToRanges(res)
        assert res == [[0, 50]]

        res = divideKeys(keys, 2)
        assert res == [[0, 1, 2], [3, 5, 8, 50]]
        res = keysToRanges(res)
        assert res == [[0, 2], [3, 50]]

        res = divideKeys(keys, 3)
        assert res == [[0, 1], [2, 3], [5, 8, 50]]
        res = keysToRanges(res)
        assert res == [[0, 1], [2, 3], [5, 50]]

        res = divideKeys(keys, 7)
        assert res == [[0], [1], [2], [3], [5], [8], [50]]
        res = keysToRanges(res)
        assert res == [[0, 0], [1, 1], [2, 2], [3, 3],
                       [5, 5], [8, 8], [50, 50]]

        res = divideKeys(keys, 8)
        assert res == [[0], [1], [2], [3], [5], [8], [50]]
        res = keysToRanges(res)
        assert res == [[0, 0], [1, 1], [2, 2], [3, 3],
                       [5, 5], [8, 8], [50, 50]]

        keys = [0, 1, 2, 2, 3, 5, 8, 50, 50]
        res = divideKeys(keys, 0)
        assert res == []
        res = keysToRanges(res)
        assert res == []

        res = divideKeys(keys, 1)
        assert res == [[0, 1, 2, 2, 3, 5, 8, 50, 50]]
        res = keysToRanges(res)
        assert res == [[0, 50]]

        res = divideKeys(keys, 2)
        assert res == [[0, 1, 2, 2], [3, 5, 8, 50, 50]]
        res = keysToRanges(res)
        assert res == [[0, 2], [3, 50]]

        res = divideKeys(keys, 3)
        assert res == [[0, 1, 2], [2, 3, 5], [8, 50, 50]]
        res = keysToRanges(res)
        assert res == [[0, 2], [2, 5], [8, 50]]

        res = divideKeys(keys, 9)
        assert res == [[0], [1], [2], [2], [3], [5], [8], [50], [50]]
        res = keysToRanges(res)
        assert res == [[0, 0], [1, 1], [2, 2], [2, 2], [3, 3],
                       [5, 5], [8, 8], [50, 50], [50, 50]]

        res = divideKeys(keys, 10)
        assert res == [[0], [1], [2], [2], [3], [5], [8], [50], [50]]
        res = keysToRanges(res)
        assert res == [[0, 0], [1, 1], [2, 2], [2, 2], [3, 3],
                       [5, 5], [8, 8], [50, 50], [50, 50]]

    def test_splitKeys(self):
        keys = [(0, 1234), (0, 5678), (0, 9876), (1, 2468)]
        assert splitKeys(keys, 2) == [((0, 1234), (0, 5678)),
                                      ((0, 9876), (1, 2468))]

    def test_split_keys_around_read_groups(self):
        def to_py(a):
            return [(tuple(b), tuple(c)) for b, c in a]
        keys = np.rec.fromrecords([(0, 1234), (0, 5678), (0, 9876), (1, 2468)],
                                  names=["qId", "holeNumber"])
        chunks = to_py(split_keys_around_read_groups(keys, 2))
        assert chunks == [((0, 1234), (0, 9876)), ((1, 2468), (1, 2468))]
        chunks = to_py(split_keys_around_read_groups(keys, 3))
        assert chunks == [((0, 1234), (0, 9876)), ((1, 2468), (1, 2468))]
        with pytest.raises(RuntimeError):
            chunks = split_keys_around_read_groups(keys, 1)

    def test_collection_file_resolver(self):
        TEST_EXTS = ["subreadset.xml", "subreads.bam", "sts.xml", "sts.h5", "metadata.xml", "consensusreadset.xml", "hifi_reads.bam"]
        TEST_SUBDIRS = ["pb_internal", "pb_internal", "metadata", "pb_internal", "metadata", "pb_formats", "hifi_reads"]
        def _make_file(fn):
            with open(fn, "wb") as f_out:
                f_out.write(b"")
        # old layout
        movie1 = "m64001_220901_120000"
        tmpdir1 = tempfile.mkdtemp("dataset-contents-1")
        for ext in TEST_EXTS:
            _make_file(op.join(tmpdir1, f"{movie1}.{ext}"))
        subreads = op.join(tmpdir1, f"{movie1}.subreadset.xml")
        fn1 = collection_file_resolver(subreads, ".sts.xml")
        assert fn1.endswith(".sts.xml") and op.isfile(fn1)
        fn2 = collection_file_resolver(subreads, ".sts.h5")
        assert fn2.endswith(".sts.h5") and op.isfile(fn2)
        fn3 = collection_file_resolver(subreads, ".metadata.xml")
        assert fn3.endswith(".metadata.xml") and op.isfile(fn3)
        # new layout
        movie2 = "m84001_220901_120000_s1"
        tmpdir2 = tempfile.mkdtemp("dataset-contents-2")
        for subdir in ["pb_internal", "pb_formats", "metadata", "statistics", "hifi_reads"]:
            os.makedirs(op.join(tmpdir2, subdir))
        for subdir, ext in zip(TEST_SUBDIRS, TEST_EXTS):
            _make_file(op.join(tmpdir2, subdir, f"{movie2}.{ext}"))
        subreads2 = op.join(tmpdir2, "pb_internal", f"{movie2}.subreadset.xml")
        ccs2 = op.join(tmpdir2, "pb_formats", f"{movie2}.consensusreadset.xml")
        fn1 = collection_file_resolver(subreads2, ".sts.xml")
        assert fn1.endswith(".sts.xml") and op.isfile(fn1)
        fn2 = collection_file_resolver(subreads2, ".sts.h5")
        assert fn2.endswith(".sts.h5") and op.isfile(fn2)
        fn3 = collection_file_resolver(subreads2, ".metadata.xml")
        assert fn3.endswith(".metadata.xml") and op.isfile(fn3)
        fn4 = collection_file_resolver(ccs2, ".sts.xml")
        assert fn4.endswith(".sts.xml") and op.isfile(fn4)
        fn5 = collection_file_resolver(ccs2, ".sts.h5")
        assert fn5.endswith(".sts.h5") and op.isfile(fn5)
        fn6 = collection_file_resolver(ccs2, ".metadata.xml")
        assert fn6.endswith(".metadata.xml") and op.isfile(fn6)
        fn7 = collection_file_resolver(ccs2, ".subreads.bam")
        assert fn7.endswith(".subreads.bam") and op.isfile(fn7)
