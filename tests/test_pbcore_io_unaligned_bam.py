from numpy.testing import (assert_array_almost_equal as ASIM,
                           assert_array_equal        as AEQ)
from nose.tools import (nottest,
                        assert_raises,
                        assert_equal as EQ)
from nose import SkipTest

import numpy as np
import bisect
import h5py
from collections import Counter

from pbcore import data
from pbcore.io import BamReader, BaxH5Reader
from pbcore.io.align._BamSupport import UnavailableFeature

from pbcore.sequence import reverseComplement as RC

class TestUnalignedBam(object):

    def __init__(self):
        self.bam = BamReader  (data.getUnalignedBam())
        self.bax = BaxH5Reader(data.getBaxForBam())

        self.baxRead0 = next(self.bax.subreads())
        self.bamRead0 = next(iter(self.bam))

    def testInvalidOperations(self):

        # These kinds of things presently work.  Do we want them to
        # fail?

        # with assert_raises(UnavailableFeature):
        #     self.bamRead0.isForwardStrand
        # with assert_raises(UnavailableFeature):
        #     self.bamRead0.tStart

        # attempts to get read aligned or oriented
        with assert_raises(UnavailableFeature):
            self.bamRead0.read(aligned=True, orientation="native")
        with assert_raises(UnavailableFeature):
            self.bamRead0.read(aligned=False, orientation="genomic")
        with assert_raises(UnavailableFeature):
            self.bamRead0.read()
        with assert_raises(UnavailableFeature):
            self.bamRead0.InsertionQV(aligned=True, orientation="native")
        with assert_raises(UnavailableFeature):
            self.bamRead0.InsertionQV(aligned=False, orientation="genomic")
        with assert_raises(UnavailableFeature):
            self.bamRead0.InsertionQV()

    def testReadAccess(self):
        EQ(self.bamRead0.read(aligned=False, orientation="native"), self.baxRead0.basecalls())

    def testQvAccess(self):
        AEQ(self.bamRead0.SubstitutionQV(aligned=False, orientation="native"), self.baxRead0.SubstitutionQV())
        AEQ(self.bamRead0.InsertionQV(aligned=False, orientation="native"),    self.baxRead0.InsertionQV())
        AEQ(self.bamRead0.DeletionTag(aligned=False, orientation="native"),    self.baxRead0.DeletionTag())

    def testZmwInfo(self):
        # WAT.  Need to make these accessors more uniform.  This is
        # totally crazy.
        EQ(self.bamRead0.HoleNumber, self.baxRead0.holeNumber)
        EQ(self.bamRead0.qStart,     self.baxRead0.readStart)
        EQ(self.bamRead0.qEnd,       self.baxRead0.readEnd)

    def testNames(self):
        EQ(self.bamRead0.queryName, self.baxRead0.readName)

    def testIpd(self):
        """Check that 'Ipd' feature is recognized correctly."""
        pfa = self.bam.baseFeaturesAvailable()
        EQ(pfa, frozenset(['Ipd', 'DeletionTag', 'MergeQV', 'SubstitutionQV',
                           'InsertionQV', 'DeletionQV']))
        ipd = self.bamRead0.IPD(aligned=False, orientation="native")
