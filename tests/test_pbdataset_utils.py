from __future__ import absolute_import, division, print_function

import logging
import tempfile

from pbcore.io.dataset.DataSetMetaTypes import dsIdToSuffix
from pbcore.io import (DataSetMetaTypes, divideKeys,
                       SubreadSet, getDataSetUuid, getDataSetMetaType)

import pbcore.data as upstreamdata

log = logging.getLogger(__name__)

def keysToRanges(keys):
    key_ranges = [[min(k), max(k)] for k in keys]
    return key_ranges

class TestDataSetUtils(object):
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
