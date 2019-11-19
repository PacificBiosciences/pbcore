import pytest

from pbcore import sequence

class TestReverseComplement:

    SEQUENCE = "GATTACA" * 20
    REVERSE = "ACATTAG" * 20
    COMPLEMENT = "CTAATGT" * 20
    REVERSE_COMPLEMENT = "TGTAATC" * 20
    IUPAC_SEQUENCE = "ACTURY" * 20
    IUPAC_COMPLEMENT = "TGANNN" * 20
    IUPAC_REVERSE_COMPLEMENT = "NNNAGT" * 20
    BAD_SEQUENCE = "AGCTQ" * 20  # contains non-IUPAC char

    def test_reverse(self):
        assert self.SEQUENCE == sequence.reverse(sequence.reverse(self.SEQUENCE))
        assert self.REVERSE == sequence.reverse(self.SEQUENCE)
        assert self.COMPLEMENT == sequence.reverse(self.REVERSE_COMPLEMENT)

    def test_complement(self):
        assert self.SEQUENCE == sequence.complement(self.COMPLEMENT)
        assert self.COMPLEMENT == sequence.complement(self.SEQUENCE)
        assert self.REVERSE == sequence.complement(self.REVERSE_COMPLEMENT)

    def test_reverseComplement(self):
        assert self.REVERSE_COMPLEMENT == sequence.reverseComplement(self.SEQUENCE)
        assert self.SEQUENCE == sequence.reverseComplement(self.REVERSE_COMPLEMENT)

    def test_iupac(self):
        assert self.IUPAC_COMPLEMENT == sequence.complement(self.IUPAC_SEQUENCE)
        assert self.IUPAC_REVERSE_COMPLEMENT == sequence.reverseComplement(self.IUPAC_SEQUENCE)

    def test_complement_error(self):
        with pytest.raises(ValueError):
            sequence.complement(self.BAD_SEQUENCE)

    def test_reverse_complement_error(self):
        with pytest.raises(ValueError):
            sequence.reverseComplement(self.BAD_SEQUENCE)
