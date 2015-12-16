import inspect
import os

import h5py
import nose.tools
import numpy
import numpy.testing

import pbcore.data

from pbcore.io.BasH5IO import BasH5Reader, Zmw, ZmwRead, CCSZmwRead
from pbcore.chemistry import ChemistryLookupError

class TestBasH5Reader_14:
    """Tests of BasH5Reader against a 1.4 bas.h5 file, no multipart with
    CCS.
    """

    def __init__(self):
        self.cmpH5 = pbcore.io.CmpH5Reader(pbcore.data.getCmpH5())
        basFiles = pbcore.data.getBasH5s()
        self.bas1, self.bas2 = map(pbcore.io.BasH5Reader, basFiles)

    def test_BasH5Reader_basicTest(self):
        """Test that BasH5Reader correctly sets moviename, identifies the
        sequencingZmws, and finds the subreads for each Zmw.
        """

        nose.tools.assert_equal(pbcore.data.MOVIE_NAME_14, self.bas1.movieName)
        numpy.testing.assert_array_equal([   7,    8,    9, 1000, 1006, 1007,
                                          2001, 2003, 2007, 2008, 3004, 3006,
                                          3008, 4004, 4005, 4006, 4007, 4009],
                                          self.bas1.sequencingZmws)
        numpy.testing.assert_array_equal([   7,    8,    9, 1000, 1001, 1002,
                                          1003, 1004, 1005, 1006, 1007, 1008,
                                          1009, 2000, 2001, 2002, 2003, 2004,
                                          2005, 2006, 2007, 2008, 2009, 3000,
                                          3001, 3002, 3003, 3004, 3005, 3006,
                                          3007, 3008, 3009, 4000, 4001, 4002,
                                          4003, 4004, 4005, 4006, 4007, 4008,
                                          4009],
                                          self.bas1.allSequencingZmws)

        for zmw in self.bas1:
            nose.tools.assert_greater(len(zmw.subreads), 0)

    def test_BasH5Reader_basecallsVsCmpH5(self):
        """Compare datasets in the bas.h5 file against those in a corresponding
        cmp.h5 file.
        """

        aln = self.cmpH5[2]
        nose.tools.assert_equal(os.path.join(pbcore.data.MOVIE_NAME_14, "2001", "3580_3922"),
                                aln.readName)

        zmwRead = self.bas1[2001].read(3580, 3922)
        nose.tools.assert_equal(os.path.join(pbcore.data.MOVIE_NAME_14, "2001", "3580_3922"),
                                zmwRead.readName)

        # Verify that the bases and a couple of quality values are the same
        nose.tools.assert_equal(aln.read(aligned=False), zmwRead.basecalls())
        numpy.testing.assert_array_equal(aln.InsertionQV(aligned=False),
                                         zmwRead.InsertionQV())
        numpy.testing.assert_array_equal(aln.DeletionQV(aligned=False),
                                         zmwRead.DeletionQV())
        numpy.testing.assert_array_equal(aln.QualityValue(aligned=False),
                                         zmwRead.QualityValue())

    def test_BasH5Reader_regionTableAccessors(self):
        """Test that BasH5Reader can read the region table and find
        HQ, insert, and adapter regions.
        """
        zmw = self.bas1[7]
        numpy.testing.assert_array_equal(
            numpy.array([(7, 1, 0, 299, -1),
                         (7, 1, 343, 991, -1),
                         (7, 1, 1032, 1840, -1),
                         (7, 0, 299, 343, 681),
                         (7, 0, 991, 1032, 804),
                         (7, 2, 0, 1578, 0)],
                  dtype=(numpy.record, [('holeNumber', '<i4'),
                                        ('regionType', '<i4'),
                                        ('regionStart', '<i4'),
                                        ('regionEnd', '<i4'),
                                        ('regionScore', '<i4')])),
            zmw.regionTable.view(dtype=numpy.ndarray))

        nose.tools.assert_equal((0, 1578), zmw.hqRegion)
        nose.tools.assert_equal([(299, 343), (991, 1032)], zmw.adapterRegions)
        nose.tools.assert_equal([(0, 299), (343, 991), (1032, 1578)],
                                zmw.insertRegions)

    def test_BasH5Reader_ccs(self):
        """Test that BasH5Reader can read the CCS bases."""

        nose.tools.assert_equal(self.bas1[4006].ccsRead.basecalls(),
           ''.join(['GGCGCACGGAGGAGCAAGCGTGACAGTCCCACGTCATGCCCGCCGACG',
                    'ATATCGAGCTCGCGCTCACCGCCAGGGTGTGAAGTGAATTCACGGTGC',
                    'CGCCGAAAGCTGGGCCGGCTTTCGTTCCTTCGCCGGTCAGGAGAAGGC',
                    'GGACCCCGTCGTGGGCCATTCCGAGCCTGGAGACAGCGGTCGAAAAAG',
                    'CCTTCGCCAAGCCGGTGGCCAAATGGTCGGCCAGCGAGAATCCGTGC']))

    def test_BasH5Reader_productivity(self):
        nose.tools.assert_equal(1, self.bas1[4006].productivity)

    def test_BasH5Reader_readScore(self):
        nose.tools.assert_almost_equal(0.7822426, self.bas1[4006].readScore)

    @nose.tools.raises(ChemistryLookupError)
    def test_14_missing_chemistry(self):
        """Tests that we raise an exception when we can't find chemistry information"""
        self.bas1.sequencingChemistry

    def test_ZmwRead_len(self):
        """Test that ZmwRead objects have the correct len."""
        nose.tools.assert_equal(1126, len(self.bas1[4006].read().basecalls()))
        nose.tools.assert_equal(1126, len(self.bas1[4006].read()))
        nose.tools.assert_equal(464,
                                len(self.bas1[4006].subreads[0].basecalls()))
        nose.tools.assert_equal(464, len(self.bas1[4006].subreads[0]))
        nose.tools.assert_equal(239, len(self.bas1[4006].ccsRead.basecalls()))
        nose.tools.assert_equal(239, len(self.bas1[4006].ccsRead))

class CommonTests(object):

    ZMW_ATTRIBUTES = ['QualityValue', 'InsertionQV', 'DeletionQV',
                      'DeletionTag', 'SubstitutionQV', 'SubstitutionTag',
                      'MergeQV', 'IPD', 'PreBaseFrames', 'PulseWidth',
                      'WidthInFrames']

    def test_all_fields_accessible(self):
        # Test that zmws have correct pulse/quality attributes
        reader = pbcore.io.BasH5Reader(self.bash5_filename)

        for zmw in reader.sequencingZmws:
            read = reader[zmw].read()
            for attribute in self.ZMW_ATTRIBUTES:
                nose.tools.assert_is_instance(getattr(read, attribute)(),
                                              numpy.ndarray)
            numpy.testing.assert_array_equal(read.IPD(), read.PreBaseFrames())
            numpy.testing.assert_array_equal(read.PulseWidth(),
                                             read.WidthInFrames())

    def test_zmw_region_table(self):
        reader = pbcore.io.BasH5Reader(self.bash5_filename)

        sequencing_zmws = set(reader.sequencingZmws)

        for zmw in reader.allSequencingZmws:
            region_table = reader[zmw].regionTable.tolist()
            hq_entry = [k for k in region_table if k[1] == 2][0]

            hq_size = hq_entry[3] - hq_entry[2]
            # Sequencing Zmws should have an HQ region
            if zmw not in sequencing_zmws:
                nose.tools.assert_equal(hq_size, 0)
            else:
                nose.tools.assert_greater(hq_size, 0)

            for entry in region_table:
                nose.tools.assert_equal(entry[0], zmw)
                nose.tools.assert_less_equal(entry[2], entry[3])
        reader.close()

class ReadIteratorTests(object):

    def test_read_iterators(self):
        for fname in [self.bash5_filename] + self.baxh5_filenames:
            reader = pbcore.io.BasH5Reader(self.bash5_filename)

            if reader.hasConsensusBasecalls:
                ccsReads = [ zmw.ccsRead
                             for zmw in reader
                             if zmw.ccsRead is not None ]
                nose.tools.assert_equal(ccsReads, list(reader.ccsReads()))
            else:
                nose.tools.assert_equal([], list(reader.ccsReads()))

            if reader.hasRawBasecalls:
                subreads = [ subread
                             for zmw in reader
                             for subread in zmw.subreads ]
                nose.tools.assert_equal(subreads, list(reader.subreads()))

                reads = [ zmw.read()
                          for zmw in reader ]
                nose.tools.assert_equal(reads, list(reader.reads()))
            else:
                nose.tools.assert_equal([], list(reader.reads()))
                nose.tools.assert_equal([], list(reader.subreads()))

class CommonMultiPartTests(object):

    def test_multipart_constructor_bash5(self):
        # Test the constuctor of a multipart bas.h5 file
        reader = pbcore.io.BasH5Reader(self.bash5_filename)
        nose.tools.assert_is_instance(reader.file, h5py.File)

        # Should have three parts for v2.0 and v2.1
        nose.tools.assert_equal(len(reader.parts), 3)
        nose.tools.assert_list_equal(self.baxh5_filenames,
                [k.filename for k in reader.parts])

        # All bas.h5 files should have raw base calls. 2.1 bas.h5 files don't
        # have consensus base calls
        nose.tools.assert_true(reader.hasRawBasecalls)


        for zmw in reader.sequencingZmws:
            nose.tools.assert_in(zmw, reader.allSequencingZmws)
            nose.tools.assert_is_instance(reader[zmw], Zmw)

        nose.tools.assert_less_equal(len(reader.sequencingZmws),
                                        len(reader.allSequencingZmws))

        reader.close()

    def test_multippart_constructor_baxh5(self):
        # Test constructor of baxh5 files
        for filename in self.baxh5_filenames:
            reader = pbcore.io.BasH5Reader(filename)
            nose.tools.assert_is_instance(reader.file, h5py.File)

            nose.tools.assert_equal(len(reader.parts), 1)
            nose.tools.assert_true(reader.hasRawBasecalls)

            for zmw in reader.sequencingZmws:
                nose.tools.assert_in(zmw, reader.allSequencingZmws)
                nose.tools.assert_is_instance(reader[zmw], Zmw)

            nose.tools.assert_less_equal(len(reader.sequencingZmws),
                                            len(reader.allSequencingZmws))

            reader.close()

    def test_multipart_hole_lookup(self):
        # Test that multipart files look up files and hole numbers correctly
        hole_number_to_filename = {}
        for filename in self.baxh5_filenames:
            f = h5py.File(filename, 'r')
            for hole_number in f['PulseData/BaseCalls/ZMW/HoleNumber']:
                hole_number_to_filename[hole_number] = filename
            f.close()

        reader = pbcore.io.BasH5Reader(self.bash5_filename)

        for hole_number in hole_number_to_filename:
            zmw = reader[hole_number]
            nose.tools.assert_equal(zmw.baxH5.filename,
                                    hole_number_to_filename[hole_number])
            nose.tools.assert_is_instance(zmw, Zmw)

        reader.close()

    def _clip_region(self, region, hq_region):
        end = min(region[1], hq_region[1])
        start = max(region[0], hq_region[0])
        if start >= end:
            return None
        else:
            return (start, end)

    def test_zmw_multipart_regions(self):

        regions = []

        # First read in the regions from the h5 files directly
        for filename in self.baxh5_filenames:
            with h5py.File(filename, 'r') as f:
                region_table = f['PulseData/Regions']
                regions.extend(region_table.value.tolist())

        # Now see what BasH5Reader reports for regions
        reader = pbcore.io.BasH5Reader(self.bash5_filename)
        for zmw in reader.allSequencingZmws:
            region_table = reader[zmw].regionTable.tolist()

            true_regions = [k for k in regions if k[0] == zmw]
            true_hq_region = [k for k in true_regions if k[1] == 2][0]

            reported_hq_region = reader[zmw].hqRegion
            nose.tools.assert_equal(reported_hq_region[0], true_hq_region[2])
            nose.tools.assert_equal(reported_hq_region[1], true_hq_region[3])

            # Check the reported adapter regions
            reported_adapter_regions = reader[zmw].adapterRegions
            true_adapter_regions = [k for k in true_regions if k[1] == 0]
            region_count = 0
            for region in true_adapter_regions:
                bound = (region[2], region[3])
                clipped_region = self._clip_region(bound, reported_hq_region)
                if clipped_region:
                    nose.tools.assert_in(clipped_region,
                                         reported_adapter_regions)
                    region_count += 1
            nose.tools.assert_equal(region_count, len(reported_adapter_regions))

            # And the reported insert regions
            reported_insert_regions = reader[zmw].insertRegions
            true_insert_regions = [k for k in true_regions if k[1] == 1]
            region_count = 0
            for region in true_insert_regions:
                bound = (region[2], region[3])
                clipped_region = self._clip_region(bound, reported_hq_region)
                if clipped_region:
                    nose.tools.assert_in(clipped_region,
                                         reported_insert_regions)
                    region_count += 1
            nose.tools.assert_equal(region_count, len(reported_insert_regions))


class TestBasH5Reader_20(CommonTests, CommonMultiPartTests, ReadIteratorTests):
    """Tests of BasH5Reader against a 2.0 ba[sx].h5 files, consisting of a
    bas.h5 file and three bas.h5 files. The bax.h5 files also contain CCS.
    """

    def __init__(self):
        """Get the full paths to the bas and bax.h5 files."""

        self.bash5_filename = pbcore.data.getBasH5_v20()
        self.baxh5_filenames = pbcore.data.getBaxH5_v20()


    def test_20_constructor_bash5(self):
        # Tests specific to the v2.0 bas.h5 constructor
        reader = pbcore.io.BasH5Reader(self.bash5_filename)
        nose.tools.assert_true(reader.hasConsensusBasecalls)
        nose.tools.assert_equal(reader.movieName, pbcore.data.MOVIE_NAME_20)

        reader.close()

    def test_20_constructor_baxh5(self):
        # Tests specific to the v2.0 bax.h5 constructor
        for filename in self.baxh5_filenames:
            reader = pbcore.io.BasH5Reader(filename)
            nose.tools.assert_true(reader.hasConsensusBasecalls)
            nose.tools.assert_equal(reader.movieName, pbcore.data.MOVIE_NAME_20)
            reader.close()

    @nose.tools.raises(ChemistryLookupError)
    def test_20_missing_chemistry(self):
        """Tests that we raise an exception when we can't find chemistry information"""
        reader = pbcore.io.BasH5Reader(self.bash5_filename)
        reader.sequencingChemistry

    def test_productivity(self):
        """Test that productivities are set correctly for the ZMW objects."""
        productivities = {}
        for filename in self.baxh5_filenames:
            f = h5py.File(filename, 'r')
            hn_to_prod = dict(zip(f["PulseData/BaseCalls/ZMW/HoleNumber"],
                                  f["PulseData/BaseCalls/ZMWMetrics/Productivity"]))
            productivities.update(hn_to_prod)
            f.close()

        reader = pbcore.io.BasH5Reader(self.bash5_filename)

        for hn in productivities:
            nose.tools.assert_equal(reader[hn].productivity,
                                    productivities[hn])


class TestBasH5Reader_21(CommonTests, CommonMultiPartTests, ReadIteratorTests):
    """Tests of BasH5Reader against a 2.1 ba[sx].h5 files, consisting of a
    bas.h5 file and three bas.h5 files. The bax.h5 files do not contain CCS.
    """

    def __init__(self):
        """Get the full paths to the bas and bax.h5 files."""
        self.bash5_filename = pbcore.data.getBasH5_v21()
        self.baxh5_filenames = pbcore.data.getBaxH5_v21()

    def test_21_constructor_bash5(self):
        # Tests specific to the v2.0 bas.h5 constructor
        reader = pbcore.io.BasH5Reader(self.bash5_filename)
        nose.tools.assert_false(reader.hasConsensusBasecalls)
        nose.tools.assert_equal(reader.movieName, pbcore.data.MOVIE_NAME_21)

        reader.close()

    def test_21_constructor_baxh5(self):
        # Tests specific to the v2.0 bax.h5 constructor
        for filename in self.baxh5_filenames:
            reader = pbcore.io.BasH5Reader(filename)
            nose.tools.assert_false(reader.hasConsensusBasecalls)
            nose.tools.assert_equal(reader.movieName, pbcore.data.MOVIE_NAME_21)
            reader.close()

    def test_21_external_region_baxh5(self):
        """Test the optional region file override"""
        for baxfile in self.baxh5_filenames:
            # Count of the subreads using internal region table
            reader = pbcore.io.BaxH5Reader(baxfile)
            bax_subread_count = len([x for x in reader.subreads()])

            # Count of subreads using external region table
            rgnfile = baxfile.replace('bax.h5','rgn.h5')
            reader.loadExternalRegions(rgnfile)
            rgn_subread_count = len([x for x in reader.subreads()])

            nose.tools.assert_true(rgn_subread_count < bax_subread_count)

    @nose.tools.raises(ChemistryLookupError)
    def test_21_missing_chemistry(self):
        """Tests that we raise an exception when we can't find chemistry information"""
        reader = pbcore.io.BasH5Reader(self.bash5_filename)
        reader.sequencingChemistry

    @nose.tools.raises(IOError)
    def test_21_bad_external_region_baxh5(self):
        """Tests that we raise an exception when incorrect region file given"""
        baxfiles = self.baxh5_filenames
        baxfile = baxfiles[0]
        rgnfile = baxfiles[1].replace('bax.h5','rgn.h5')
        pbcore.io.BaxH5Reader(baxfile, regionH5Filename=rgnfile)

class TestBasH5Reader_23(CommonTests, CommonMultiPartTests, ReadIteratorTests):
    """Tests of BasH5Reader against a 2.3 ba[sx].h5 files, consisting of a
    bas.h5 file and three bas.h5 files. The bax.h5 files do not contain CCS,
    but do contain Chemistry information
    """

    def __init__(self):
        """Get the full paths to the bas and bax.h5 files."""
        self.bash5_filename = pbcore.data.getBasH5_v23()
        self.baxh5_filenames = pbcore.data.getBaxH5_v23()

    def test_23_constructor_bash5(self):
        # Tests specific to the v2.0 bas.h5 constructor
        reader = pbcore.io.BasH5Reader(self.bash5_filename)
        nose.tools.assert_false(reader.hasConsensusBasecalls)
        nose.tools.assert_equal(reader.movieName, pbcore.data.MOVIE_NAME_23)
        nose.tools.assert_equal(reader.sequencingChemistry, 'P6-C4')

        reader.close()

    def test_23_constructor_baxh5(self):
        # Tests specific to the v2.0 bax.h5 constructor
        for filename in self.baxh5_filenames:
            reader = pbcore.io.BasH5Reader(filename)
            nose.tools.assert_false(reader.hasConsensusBasecalls)
            nose.tools.assert_equal(reader.movieName, pbcore.data.MOVIE_NAME_23)
            nose.tools.assert_equal(reader.sequencingChemistry, 'P6-C4')
            reader.close()

class TestBasH5Reader_CCS(ReadIteratorTests):
    """Test BasH5Reader with a ccs.h5 file produced by P_CCS."""

    def __init__(self):
        """Get the full paths to the bas and bax.h5 files."""
        self.bash5_filename = pbcore.data.getCCSH5()
        self.baxh5_filenames = []

    def test_constructor_ccsh5(self):
        # Test that BasH5Reader initializes correctly with a ccs.h5 file
        reader = pbcore.io.BasH5Reader(self.bash5_filename)
        nose.tools.assert_is_instance(reader.file, h5py.File)

        nose.tools.assert_true(reader.hasConsensusBasecalls)
        nose.tools.assert_false(reader.hasRawBasecalls)
        nose.tools.assert_equal(reader.movieName, pbcore.data.MOVIE_NAME_CCS)

        nose.tools.assert_equal(len(reader.parts), 1)

        for zmw in reader.sequencingZmws:
            nose.tools.assert_in(zmw, reader.allSequencingZmws)
            nose.tools.assert_is_instance(reader[zmw], Zmw)

        nose.tools.assert_less_equal(len(reader.sequencingZmws),
                                        len(reader.allSequencingZmws))

        reader.close()

    def test_ccs_zmw(self):
        # Test Zmw objects derived from a BasH5Reader reading a ccs.h5
        reader = pbcore.io.BasH5Reader(self.bash5_filename)

        sequencing_zmws = set(reader.sequencingZmws)
        for zmw in reader.allSequencingZmws:
            region_table = reader[zmw].regionTable
            nose.tools.assert_equal(len(region_table), 1)
            nose.tools.assert_equal(region_table[0][0], zmw)
            nose.tools.assert_equal(region_table[0][1], 2)

            nose.tools.assert_equal(len(reader[zmw].insertRegions), 0)
            nose.tools.assert_equal(len(reader[zmw].adapterRegions), 0)
            nose.tools.assert_equal(len(reader[zmw].subreads), 0)


            with nose.tools.assert_raises(ValueError):
                reader[zmw].read()

            if zmw in sequencing_zmws:
                nose.tools.assert_is_instance(reader[zmw].ccsRead,
                                              CCSZmwRead)
            else:
                nose.tools.assert_is_none(reader[zmw].ccsRead)
