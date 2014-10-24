import nose
from nose.tools import assert_equal, assert_true, assert_false
from pbcore.util import sequences

class TestReverseComplement:

    def setup(self):
        self.sequence = "GATTACA" * 20
        self.reverse = "ACATTAG" * 20
        self.complement = "CTAATGT" * 20
        self.reverse_complement = "TGTAATC" * 20
        self.bad_sequence = "AGCTR" * 20

    def test_reverse(self):
        assert_equal(self.sequence,
                     sequences.reverse(sequences.reverse(self.sequence)))
        assert_equal(self.reverse,
                     sequences.reverse(self.sequence))
        assert_equal(self.complement,
                     sequences.reverse(self.reverse_complement))

    def test_complement(self):
        assert_equal(self.sequence,
                     sequences.complement(self.complement))
        assert_equal(self.complement,
                     sequences.complement(self.sequence))
        assert_equal(self.reverse,
                     sequences.complement(self.reverse_complement))

    def test_reverseComplement(self):
        assert_equal(self.reverse_complement,
                     sequences.reverseComplement(self.sequence))
        assert_equal(self.sequence,
                     sequences.reverseComplement(self.reverse_complement))

    @nose.tools.raises(ValueError)
    def test_complement_error(self):
        sequences.complement(self.bad_sequence)

    @nose.tools.raises(ValueError)
    def test_reverse_complement_error(self):
        sequences.reverseComplement(self.bad_sequence)


class TestSplitRecordName:

    def setup(self):
        pass
