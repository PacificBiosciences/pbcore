from __future__ import absolute_import, division, print_function

import pytest

from pbcore import data
from pbcore.io import BamReader
from pbcore.io.align._BamSupport import UnavailableFeature

class TestUnalignedBam(object):

    @classmethod
    def setup_class(cls):
        cls.bam = BamReader(data.getUnalignedBam())
        cls.bamRead0 = next(iter(cls.bam))

    def testInvalidOperations(self):

        # These kinds of things presently work.  Do we want them to
        # fail?

        # with assert_raises(UnavailableFeature):
        #     self.bamRead0.isForwardStrand
        # with assert_raises(UnavailableFeature):
        #     self.bamRead0.tStart

        # attempts to get read aligned or oriented
        with pytest.raises(UnavailableFeature):
            self.bamRead0.read(aligned=True, orientation="native")
        with pytest.raises(UnavailableFeature):
            self.bamRead0.read(aligned=False, orientation="genomic")
        with pytest.raises(UnavailableFeature):
            self.bamRead0.read()
        with pytest.raises(UnavailableFeature):
            self.bamRead0.InsertionQV(aligned=True, orientation="native")
        with pytest.raises(UnavailableFeature):
            self.bamRead0.InsertionQV(aligned=False, orientation="genomic")
        with pytest.raises(UnavailableFeature):
            self.bamRead0.InsertionQV()

    def testIpd(self):
        """Check that 'Ipd' feature is recognized correctly."""
        pfa = self.bam.baseFeaturesAvailable()
        assert pfa == frozenset(['Ipd', 'DeletionTag', 'MergeQV', 'SubstitutionQV',
                                 'InsertionQV', 'DeletionQV'])
        ipd = self.bamRead0.IPD(aligned=False, orientation="native")
