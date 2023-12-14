# see also test_mapped_sequence_identity.py

import pytest
import sys

from pbcore.util.statistics import accuracy_as_phred_qv, phred_qv_as_accuracy


class TestStatistics:

    def test_accuracy_as_phred_qv(self):
        qv = accuracy_as_phred_qv(0.999)
        assert int(round(qv)) == 30
        qv = accuracy_as_phred_qv(1.0, max_qv=60)
        assert int(round(qv)) == 60
        qv = accuracy_as_phred_qv([0.95, 1.0, 0.99999])
        qvs = [int(round(x)) for x in qv]
        assert qvs == [13, 60, 50]
        assert accuracy_as_phred_qv(-1) == 0

    def test_phred_qv_as_accuracy(self):
        assert phred_qv_as_accuracy(20) == 0.99
        assert phred_qv_as_accuracy(30) == 0.999
        assert phred_qv_as_accuracy(10) == 0.9
        assert phred_qv_as_accuracy(0) == 0
        with pytest.raises(ValueError):
            x = phred_qv_as_accuracy(-1)
