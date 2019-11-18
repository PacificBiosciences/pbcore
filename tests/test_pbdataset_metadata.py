import pytest

import logging
import tempfile
import copy
import os
from collections import Counter

from pbcore.io import SubreadSet, AlignmentSet
from pbcore.io.dataset.DataSetErrors import InvalidDataSetIOError
from pbcore.io.dataset.DataSetMembers import CollectionMetadata
import pbcore.data.datasets as data
from pbcore.io.dataset.DataSetValidator import validateFile

log = logging.getLogger(__name__)

class TestDataSet(object):
    """Unit and integrationt tests for the DataSet class and \
    associated module functions"""

    def test_existing(self):
        ds = SubreadSet(data.getSubreadSet(), skipMissing=True)
        # check that we aren't adding any additional biosamples elements:
        assert Counter(ds.metadata.tags)['BioSamples'] == 1
        assert ds.metadata.bioSamples[0].name == 'consectetur purus'

        assert ds.metadata.bioSamples[0].DNABarcodes[0].name == 'F1--R1'

        assert ds.metadata.collections[0].getV('children', 'Automation')
        assert ds.metadata.collections[0].automation
        ds.metadata.collections[0].automation.automationParameters.addParameter('foo', 'bar')
        assert ds.metadata.collections[0].automation.automationParameters['foo'].value == 'bar'
        assert ds.metadata.collections[0].automation.automationParameters.parameterNames == [None, 'foo']

    def test_de_novo(self):
        ofn = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        log.info(ofn)
        ss = SubreadSet(data.getXml(9))
        col = CollectionMetadata()
        assert not ss.metadata.collections

        ss.metadata.collections.append(col)
        assert ss.metadata.collections

        col.cellIndex = 1
        assert ss.metadata.collections[0].cellIndex == '1'

        col.instrumentName = "foo"
        assert ss.metadata.collections[0].instrumentName == "foo"

        col.context = 'bar'
        assert ss.metadata.collections[0].context == "bar"

        ss.metadata.collections[0].runDetails.name = 'foo'
        assert 'foo' == ss.metadata.collections[0].runDetails.name

        ss.metadata.collections[0].wellSample.name = 'bar'
        assert 'bar' == ss.metadata.collections[0].wellSample.name

        ss.metadata.collections[0].wellSample.wellName = 'baz'
        assert 'baz' == ss.metadata.collections[0].wellSample.wellName

        ss.metadata.collections[0].wellSample.concentration = 'baz'
        assert 'baz' == ss.metadata.collections[0].wellSample.concentration

        # There are no existing biosamples:
        assert not 'BioSamples' in ss.metadata.tags
        # Therefore the metadata is falsy
        assert not ss.metadata.bioSamples

        ss.metadata.bioSamples.addSample('Clown')
        assert 'Clown' == ss.metadata.bioSamples[0].name

        ss.metadata.bioSamples[0].DNABarcodes.addBarcode('Dentist')
        assert 'Dentist' == ss.metadata.bioSamples[0].DNABarcodes[0].name

        # check that we are adding one additional biosamples element:
        assert Counter(ss.metadata.tags)['BioSamples'] == 1
        # Therefore the metadata is truthy
        assert ss.metadata.bioSamples
        ss.write(ofn, validate=False)

    @pytest.mark.internal_data
    def test_loadMetadata(self):
        aln = AlignmentSet(data.getXml(7))
        assert not aln.metadata.collections
        aln.loadMetadata('/pbi/dept/secondary/siv/testdata/'
                         'SA3-Sequel/lambda/roche_SAT/'
                         'm54013_151205_032353.run.metadata.xml')
        assert aln.metadata.collections
        sset_fn = ('/pbi/dept/secondary/siv/testdata/'
                'SA3-Sequel/lambda/roche_SAT/'
                'm54013_151205_032353.subreadset.xml')
        sset = SubreadSet(sset_fn)
        orig_metadata = copy.deepcopy(sset.metadata)
        sset.metadata.collections = None
        assert not sset.metadata.collections
        sset.loadMetadata('/pbi/dept/secondary/siv/testdata/'
                          'SA3-Sequel/lambda/roche_SAT/'
                          'm54013_151205_032353.run.metadata.xml')
        fn = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        sset.write(fn)
        validateFile(fn)
        validateFile(sset_fn)
        assert sset.metadata == orig_metadata

        # load the wrong thing...
        sset_fn = ('/pbi/dept/secondary/siv/testdata/'
                'SA3-Sequel/lambda/roche_SAT/'
                'm54013_151205_032353.subreadset.xml')
        sset = SubreadSet(sset_fn)
        orig_metadata = copy.deepcopy(sset.metadata)
        sset.metadata.collections = None
        assert not sset.metadata.collections
        with pytest.raises(InvalidDataSetIOError):
            sset.loadMetadata('/pbi/dept/secondary/siv/testdata/'
                              'SA3-Sequel/lambda/roche_SAT/'
                              'm54013_151205_032353.sts.xml')

    def test_uuid(self):
        ds = AlignmentSet()
        old = ds.uuid
        _ = ds.newUuid()
        assert not old == ds.uuid

        aln = AlignmentSet(data.getXml(7))
        oldUuid = aln.uuid
        outdir = tempfile.mkdtemp(suffix="dataset-doctest")
        outXml = os.path.join(outdir, 'tempfile.xml')
        aln.write(outXml)
        aln = AlignmentSet(outXml)
        assert aln.uuid == oldUuid

    @pytest.mark.internal_data
    def test_merge(self):
        sset_fn = ('/pbi/dept/secondary/siv/testdata/'
                'SA3-Sequel/lambda/roche_SAT/'
                'm54013_151205_032353.subreadset.xml')
        sset = SubreadSet(sset_fn)
        orig_metadata = copy.deepcopy(sset.metadata)
        assert len(sset.metadata.collections) == 1
        sset.metadata.collections.merge(orig_metadata.collections)
        assert len(sset.metadata.collections) == 2
        sset = SubreadSet(sset_fn)
        sset.metadata.collections.merge(orig_metadata.collections, forceUnique=True)
        assert len(sset.metadata.collections) == 1

    @pytest.mark.pbtestdata
    def test_merge_biosamples(self):
        import pbtestdata
        ds1 = pbtestdata.get_file("subreads-biosample-1")
        ds2 = pbtestdata.get_file("subreads-biosample-2")
        # Case 1: two biosamples
        ds = SubreadSet(ds1, ds2)
        samples = [bs.name for bs in ds.metadata.bioSamples]
        assert samples == ["Alice", "Bob"]
        # Case 2: same biosample in both files
        ds = SubreadSet(ds1, ds1)
        samples = [bs.name for bs in ds.metadata.bioSamples]
        assert samples == ["Alice"]
        assert len(ds.metadata.bioSamples[0].DNABarcodes) == 1
        # Case 3: same biosample, different barcodes
        dsTmp = SubreadSet(ds1)
        dsTmp.metadata.bioSamples[0].DNABarcodes[0].name = "F7--R7"
        tmpFile = tempfile.NamedTemporaryFile(suffix=".subreadset.xml").name
        dsTmp.write(tmpFile)
        ds = SubreadSet(ds1, tmpFile)
        samples = [bs.name for bs in ds.metadata.bioSamples]
        assert samples == ["Alice"]
        bcs = [bc.name for bc in ds.metadata.bioSamples[0].DNABarcodes]
        assert bcs == ["F1--R1", "F7--R7"]
