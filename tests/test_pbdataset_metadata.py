
import logging
import unittest
import tempfile
import copy
import os

from pbcore.io import SubreadSet, AlignmentSet
from pbcore.io.dataset.DataSetErrors import InvalidDataSetIOError
from pbcore.io.dataset.DataSetMembers import CollectionMetadata
import pbcore.data.datasets as data
from pbcore.io.dataset.DataSetValidator import validateFile

from utils import _pbtestdata, _check_constools, _internal_data

log = logging.getLogger(__name__)

class TestDataSet(unittest.TestCase):
    """Unit and integrationt tests for the DataSet class and \
    associated module functions"""

    def test_existing(self):
        ds = SubreadSet(data.getSubreadSet(), skipMissing=True)
        self.assertEqual(ds.metadata.bioSamples[0].name,
                         'consectetur purus')

        self.assertTrue(ds.metadata.collections[0].getV('children',
                                                        'Automation'))
        self.assertTrue(ds.metadata.collections[0].automation)
        ds.metadata.collections[
            0].automation.automationParameters.addParameter('foo', 'bar')
        self.assertEqual(
            ds.metadata.collections[
                0].automation.automationParameters['foo'].value,
            'bar')
        self.assertEqual(
            ds.metadata.collections[
                0].automation.automationParameters.parameterNames,
            [None, 'foo'])


    def test_de_novo(self):
        ofn = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        log.info(ofn)
        ss = SubreadSet(data.getXml(10))
        col = CollectionMetadata()
        self.assertFalse(ss.metadata.collections)

        ss.metadata.collections.append(col)
        self.assertTrue(ss.metadata.collections)

        col.cellIndex = 1
        self.assertTrue(ss.metadata.collections[0].cellIndex, 1)

        col.instrumentName = "foo"
        self.assertTrue(ss.metadata.collections[0].instrumentName, "foo")

        col.context = 'bar'
        self.assertTrue(ss.metadata.collections[0].context, "bar")

        ss.metadata.collections[0].runDetails.name = 'foo'
        self.assertEqual('foo', ss.metadata.collections[0].runDetails.name)

        ss.metadata.collections[0].wellSample.name = 'bar'
        self.assertEqual('bar', ss.metadata.collections[0].wellSample.name)

        ss.metadata.collections[0].wellSample.wellName = 'baz'
        self.assertEqual('baz', ss.metadata.collections[0].wellSample.wellName)

        ss.metadata.collections[0].wellSample.concentration = 'baz'
        self.assertEqual('baz',
                         ss.metadata.collections[0].wellSample.concentration)
        ss.write(ofn, validate=False)

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


    def test_uuid(self):
        ds = AlignmentSet()
        old = ds.uuid
        _ = ds.newUuid()
        self.assertNotEqual(old, ds.uuid)

        aln = AlignmentSet(data.getXml(no=8))
        oldUuid = aln.uuid
        outdir = tempfile.mkdtemp(suffix="dataset-doctest")
        outXml = os.path.join(outdir, 'tempfile.xml')
        aln.write(outXml)
        aln = AlignmentSet(outXml)
        self.assertEqual(aln.uuid, oldUuid)

