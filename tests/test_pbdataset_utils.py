
import logging
import tempfile
import unittest

from pbcore.io.dataset.DataSetMetaTypes import dsIdToSuffix
from pbcore.io import (DataSetMetaTypes, divideKeys,
                       SubreadSet, getDataSetUuid, getDataSetMetaType)
from pbcore.io.dataset.utils import load_mock_collection_metadata

import pbcore.data as upstreamdata

from utils import _pbtestdata, _check_constools, _internal_data

log = logging.getLogger(__name__)

def keysToRanges(keys):
    key_ranges = [[min(k), max(k)] for k in keys]
    return key_ranges

class TestDataSetUtils(unittest.TestCase):
    """Unit and integrationt tests for the DataSet class and \
    associated module functions"""

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

    def test_dsIdToSuffix(self):
        suffixes = ['subreadset.xml', 'hdfsubreadset.xml', 'alignmentset.xml',
                    'barcodeset.xml', 'consensusreadset.xml',
                    'consensusalignmentset.xml',
                    'referenceset.xml', 'contigset.xml']
        for dsId, exp in zip(DataSetMetaTypes.ALL, suffixes):
            self.assertEqual(dsIdToSuffix(dsId), exp)

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

    def test_load_mock_collection_metadata(self):
        md = load_mock_collection_metadata()
        self.assertEqual(md.wellSample.name, "unknown")
