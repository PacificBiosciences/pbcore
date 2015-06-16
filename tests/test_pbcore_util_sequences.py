import nose
from nose.tools import assert_equal, assert_true, assert_false
from pbcore import sequence

class TestReverseComplement:

    def setup(self):
        self.sequence = "GATTACA" * 20
        self.reverse = "ACATTAG" * 20
        self.complement = "CTAATGT" * 20
        self.reverse_complement = "TGTAATC" * 20
        self.iupac_sequence = "ACTURY" * 20
        self.iupac_complement = "TGANNN" * 20
        self.iupac_reverse_complement = "NNNAGT" * 20
        self.bad_sequence = "AGCTQ" * 20  # contains non-IUPAC char


    def test_reverse(self):
        assert_equal(self.sequence,
                     sequence.reverse(sequence.reverse(self.sequence)))
        assert_equal(self.reverse,
                     sequence.reverse(self.sequence))
        assert_equal(self.complement,
                     sequence.reverse(self.reverse_complement))

    def test_complement(self):
        assert_equal(self.sequence,
                     sequence.complement(self.complement))
        assert_equal(self.complement,
                     sequence.complement(self.sequence))
        assert_equal(self.reverse,
                     sequence.complement(self.reverse_complement))

    def test_reverseComplement(self):
        assert_equal(self.reverse_complement,
                     sequence.reverseComplement(self.sequence))
        assert_equal(self.sequence,
                     sequence.reverseComplement(self.reverse_complement))

    def test_iupac(self):
        assert_equal(self.iupac_complement,
                     sequence.complement(self.iupac_sequence))
        assert_equal(self.iupac_reverse_complement,
                     sequence.reverseComplement(self.iupac_sequence))

    @nose.tools.raises(ValueError)
    def test_complement_error(self):
        sequence.complement(self.bad_sequence)

    @nose.tools.raises(ValueError)
    def test_reverse_complement_error(self):
        sequence.reverseComplement(self.bad_sequence)


class TestSplitRecordName:

    def setup(self):
        pass
