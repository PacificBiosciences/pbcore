import pytest
import sys

from pbcore.util.statistics import accuracy_as_phred_qv


class TestStatistics:

    def test_accuracy_as_phred_qv(self):
        qv = accuracy_as_phred_qv(0.999)
        assert int(round(qv)) == 30
        qv = accuracy_as_phred_qv(1.0, max_qv=60)
        assert int(round(qv)) == 60
        qv = accuracy_as_phred_qv([0.95, 1.0, 0.99999])
        qvs = [int(round(x)) for x in qv]
        assert qvs == [13, 60, 50]
