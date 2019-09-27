from __future__ import absolute_import, division, print_function

from numpy.testing import (assert_array_almost_equal as ASIM,
                           assert_array_equal        as AEQ)
from nose.tools import (nottest,
                        assert_raises,
                        assert_equal as EQ)
from nose import SkipTest

import numpy as np
import bisect
from collections import Counter

from pbcore import data
from pbcore.io import BamReader
from pbcore.io.align._BamSupport import UnavailableFeature

from pbcore.sequence import reverseComplement as RC

class TestUnalignedBam(object):

    def setup_class(self):
        self.bam = BamReader(data.getUnalignedBam())

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

    def testIpd(self):
        """Check that 'Ipd' feature is recognized correctly."""
        pfa = self.bam.baseFeaturesAvailable()
        EQ(pfa, frozenset(['Ipd', 'DeletionTag', 'MergeQV', 'SubstitutionQV',
                           'InsertionQV', 'DeletionQV']))
        ipd = self.bamRead0.IPD(aligned=False, orientation="native")
