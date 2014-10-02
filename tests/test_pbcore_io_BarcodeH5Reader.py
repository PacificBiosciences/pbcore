import nose.tools
import numpy
import numpy.testing

import pbcore.data

from pbcore.data import MOVIE_NAME_BC
from pbcore.io.BarcodeH5Reader import BarcodeH5Reader, BarcodeH5Fofn, MPBarcodeH5Reader, LabeledZmw

class TestBarcodeH5Reader(object):
    """Tests of BarcodeH5Reader against a generic BarcodeH5 file
    """

    def __init__(self):
        bcFiles = pbcore.data.getBcH5s()
        print bcFiles
        self.bc1, self.bc2, self.bc3 = map(BarcodeH5Reader, bcFiles)

    def test_BarcodeH5Reader_basicTest(self):
        """Test that BcH5Reader correctly sets movie name, barcode labels, and hole numbers
        """

        nose.tools.assert_equal(MOVIE_NAME_BC, self.bc1.movieName)
        numpy.testing.assert_array_equal(["F3--R3", "F4--R4", "F6--R6", "F7--R7"],
                                         self.bc1.barcodeLabels)
        numpy.testing.assert_array_equal([ 922, 1416, 1436, 1466, 1480, 1551,
                                          1561, 1564, 1765, 1902, 1925, 1982,
                                          2111, 2133, 2136, 2139, 2210, 2306],
                                          self.bc1.holeNumbers)

        nose.tools.assert_equal(MOVIE_NAME_BC, self.bc2.movieName)
        numpy.testing.assert_array_equal(["F3--R3", "F4--R4", "F6--R6", "F7--R7"],
                                         self.bc2.barcodeLabels)
        numpy.testing.assert_array_equal([54505, 54506, 54507, 54516, 54535, 54542,
                                          54543, 54547, 54562, 54588, 54618, 54622,
                                          54632, 54633, 54645, 54650, 54653, 54658],
                                          self.bc2.holeNumbers)

        nose.tools.assert_equal(MOVIE_NAME_BC, self.bc3.movieName)
        numpy.testing.assert_array_equal(["F3--R3", "F4--R4", "F6--R6", "F7--R7"],
                                         self.bc3.barcodeLabels)
        numpy.testing.assert_array_equal([108990, 109015, 109016, 109017, 109021, 109023,
                                          109029, 109031, 109032, 109033, 109036, 109040,
                                          109042, 109045, 109047, 109071, 109075, 109081],
                                          self.bc3.holeNumbers)

    def test_BarcodeH5Reader_iterator(self):
        """Test that BcH5Reader correctly iterates over it's labeled ZMWs
        """

        labeledZmws1 = [ lZmw for lZmw in self.bc1.labeledZmws.values() ]
        sortedZmws1 = sorted(labeledZmws1, key=lambda z: z.holeNumber)
        nose.tools.assert_equal(sortedZmws1, list(self.bc1))

        labeledZmws2 = [ lZmw for lZmw in self.bc2.labeledZmws.values() ]
        sortedZmws2 = sorted(labeledZmws2, key=lambda z: z.holeNumber)
        nose.tools.assert_equal(sortedZmws2, list(self.bc2))

        labeledZmws3 = [ lZmw for lZmw in self.bc3.labeledZmws.values() ]
        sortedZmws3 = sorted(labeledZmws3, key=lambda z: z.holeNumber)
        nose.tools.assert_equal(sortedZmws3, list(self.bc3))

class TestBarcodeH5Fofn(object):
    """Tests of BarcodeH5RFofn against a generic 3 generic BarcodeH5 file
    """

    def __init__(self):
        bcFofn = pbcore.data.getBcFofn()
        print bcFofn
        self.bcFofn = BarcodeH5Fofn(bcFofn)
        print self.bcFofn

    def test_BasH5Fofn_basicTest(self):
        """Test that BcH5Fofn correctly sets movie name, barcode labels, and hole numbers
        """

        nose.tools.assert_equal(1, len(self.bcFofn.movieNames))
        numpy.testing.assert_array_equal(MOVIE_NAME_BC, self.bcFofn.movieNames[0])
        numpy.testing.assert_array_equal(["F3--R3", "F4--R4", "F6--R6", "F7--R7"],
                                         self.bcFofn.barcodeLabels)
        nose.tools.assert_equal("paired", self.bcFofn.scoreMode)

        numpy.testing.assert_array_equal([ 922, 1416, 1436, 1466, 1480, 1551,
                                          1561, 1564, 1765, 1902, 1925, 1982,
                                          2111, 2133, 2136, 2139, 2210, 2306,
                                          54505, 54506, 54507, 54516, 54535, 54542,
                                          54543, 54547, 54562, 54588, 54618, 54622,
                                          54632, 54633, 54645, 54650, 54653, 54658,
                                          108990, 109015, 109016, 109017, 109021, 109023,
                                          109029, 109031, 109032, 109033, 109036, 109040,
                                          109042, 109045, 109047, 109071, 109075, 109081],
                                          self.bcFofn.holeNumbers)

    def test_BcH5Fofn_iterator(self):
        """Test that BcH5Fofn correctly iterates over it's labeled ZMWs
        """

        labeledZmws = [ lZmw for reader in self.bcFofn._bcH5s
                             for lZmw in reader ]
        nose.tools.assert_equal(labeledZmws, list(self.bcFofn))

    def test_BcH5Fofn_indexing(self):
        """Test that BcH5Fofn's indexing correctly slices and returns its contents
        """

        holeNumTest = self.bcFofn[922]
        nose.tools.assert_true(isinstance(holeNumTest, LabeledZmw))
        nose.tools.assert_equal(holeNumTest.holeNumber, 922)

        barcodeTest = self.bcFofn["F3--R3"]
        nose.tools.assert_true(isinstance(barcodeTest, list))
        barcodeTestHoleNums = [lzmw.holeNumber for lzmw in barcodeTest]
        numpy.testing.assert_array_equal([ 1416,  1551,  1561,   1765,   1902,   1925,   2133,
                                          54506, 54588, 54618, 109033, 109036, 109071, 109081],
                                         barcodeTestHoleNums)

        movieTest = self.bcFofn[MOVIE_NAME_BC]
        nose.tools.assert_true(isinstance(movieTest, MPBarcodeH5Reader))
        movieTestHoleNums = [lzmw.holeNumber for lzmw in movieTest]
        numpy.testing.assert_array_equal([ 922, 1416, 1436, 1466, 1480, 1551,
                                          1561, 1564, 1765, 1902, 1925, 1982,
                                          2111, 2133, 2136, 2139, 2210, 2306,
                                          54505, 54506, 54507, 54516, 54535, 54542,
                                          54543, 54547, 54562, 54588, 54618, 54622,
                                          54632, 54633, 54645, 54650, 54653, 54658,
                                          108990, 109015, 109016, 109017, 109021, 109023,
                                          109029, 109031, 109032, 109033, 109036, 109040,
                                          109042, 109045, 109047, 109071, 109075, 109081],
                                         movieTestHoleNums)

        movieBarcodeTest = self.bcFofn[MOVIE_NAME_BC + "/F3--R3"]
        movieBarcodeTestHoleNums = [lzmw.holeNumber for lzmw in movieBarcodeTest]
        numpy.testing.assert_array_equal([ 1416,  1551,  1561,   1765,   1902,   1925,   2133,
                                          54506, 54588, 54618, 109033, 109036, 109071, 109081],
                                         movieBarcodeTestHoleNums)

        zmwTest = self.bcFofn[MOVIE_NAME_BC + "/922"]
        nose.tools.assert_equal(zmwTest.holeNumber, 922)

        subreadTest = self.bcFofn[MOVIE_NAME_BC + "/922/0_1000"]
        nose.tools.assert_equal(subreadTest.holeNumber, 922)