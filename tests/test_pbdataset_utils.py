
import logging
import tempfile
import unittest

from pbcore.io.dataset.DataSetMetaTypes import dsIdToSuffix
from pbcore.io import (DataSetMetaTypes, divideKeys, keysToRanges,
                       SubreadSet, getDataSetUuid, getDataSetMetaType)
from pbcore.io.dataset.utils import (xy_to_hn, hn_to_xy, sampleHolesUniformly,
                                     sampleUniformly, quadratic_expand,
                                     prodround)

import pbcore.data as upstreamdata

from utils import _pbtestdata, _check_constools, _internal_data

log = logging.getLogger(__name__)

class TestDataSetUtils(unittest.TestCase):
    """Unit and integrationt tests for the DataSet class and \
    associated module functions"""

    def test_hn_xy_converters(self):
        for x in range(64, 1024, 10):
            for y in range(64, 1144, 10):
                hn = xy_to_hn(x, y)
                ox, oy = hn_to_xy(hn)
                self.assertEqual(x, ox)
                self.assertEqual(y, oy)

    def test_quadratic_expand(self):
        i = [[0, 1, 2]]
        e = [[0], [1], [2]]
        o = quadratic_expand(i)
        self.assertEqual(e, o)

        i = [[0, 1, 2], [3, 4, 5]]
        e = [[0, 3], [1, 3], [2, 3],
             [0, 4], [1, 4], [2, 4],
             [0, 5], [1, 5], [2, 5]]
        o = quadratic_expand(i)
        self.assertEqual(e, o)

    def test_prodround(self):
        i = [1.1, 2.5, 3.8]
        e = [1, 2, 4]
        o = prodround(i, 8)
        self.assertEqual(e, o)
        e = [1, 3, 3]
        o = prodround(i, 9)
        self.assertEqual(e, o)
        e = [1, 3, 4]
        o = prodround(i, 12)
        self.assertEqual(e, o)

    def test_sampleUniformly(self):
        hns = sampleUniformly(4, [(0, 1), (0, 1)])
        self.assertEqual(hns, [[0, 0], [1, 0], [0, 1], [1, 1]])

        hns = sampleUniformly(4, [(0, 4), (0, 4)])
        self.assertEqual(hns, [[1, 1], [3, 1], [1, 3], [3, 3]])

        hns = sampleUniformly(4, [(0, 4), (0, 8)])
        self.assertEqual(hns, [[1, 3], [3, 3], [1, 5], [3, 5]])

        hns = sampleUniformly(3, [(0, 4), (0, 8)])
        self.assertEqual(hns, [[2, 2], [2, 4], [2, 6]])

    def test_sampleHolesUniformly(self):
        ncols = 1144
        nrows = 1024
        bounds = [(64, ncols), (64, nrows)]
        expected = [xy_to_hn(x, y) for x,y in sampleUniformly(100, bounds)]
        all_xy = quadratic_expand([range(64, ncols), range(64, nrows)])
        all_holes = [xy_to_hn(x, y) for x, y in all_xy]
        samples = sampleHolesUniformly(100, all_holes)
        self.assertEqual(expected, samples)

    @unittest.skipIf(not _internal_data(),
                     "Internal data not available")
    def test_sampleHolesUniformly_realdata(self):
        path = ('/pbi/dept/secondary/siv/testdata/SA3-Sequel/'
                'lambda/315/3150128/r54008_20160308_001811/'
                '2_B01/m54008_160308_053311.subreads.bam')
        ds = SubreadSet(path, strict=True)
        samples = sampleHolesUniformly(100, ds.index.holeNumber)
        self.assertEqual(len(samples), 100)

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


