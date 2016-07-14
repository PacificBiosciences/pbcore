
import logging
from urlparse import urlparse
import unittest
import tempfile
import os
import itertools
import numpy as np
import copy
import pysam

from pbcore.util.Process import backticks
from pbcore.io.dataset.utils import (consolidateBams, _infixFname,
                                    BamtoolsVersion)
from pbcore.io import (DataSet, SubreadSet, ConsensusReadSet,
                       ReferenceSet, ContigSet, AlignmentSet, BarcodeSet,
                       FastaReader, FastaWriter, IndexedFastaReader,
                       HdfSubreadSet, ConsensusAlignmentSet,
                       openDataFile, FastaWriter, FastqReader, openDataSet,
                       GmapReferenceSet)
from pbcore.io.dataset.DataSetErrors import InvalidDataSetIOError
from pbcore.io.dataset.DataSetMembers import CollectionMetadata
import pbcore.data as upstreamData
import pbcore.data.datasets as data
from pbcore.io.dataset.DataSetValidator import validateXml, validateFile
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

    def test_existing(self):
        ds = SubreadSet(data.getSubreadSet(), skipMissing=True)
        self.assertEqual(ds.metadata.bioSamples[0].name,
                         'consectetur purus')

        self.assertTrue(ds.metadata.collections[0].getV('children',
                                                        'Automation'))
        self.assertTrue(ds.metadata.collections[0].automation)


    def test_de_novo(self):
        ofn = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        log.info(ofn)
        ss = SubreadSet(data.getXml(10))
        col = CollectionMetadata()
        self.assertFalse(ss.metadata.collections)

        ss.metadata.collections.append(col)
        self.assertTrue(ss.metadata.collections)

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


