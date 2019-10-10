from __future__ import absolute_import, division, print_function

import pbcore
from pbcore.io import M4Reader, M5Reader


def test_m4():
    l = list(M4Reader(pbcore.data.getBlasrM4()))

def test_m5():
    l = list(M5Reader(pbcore.data.getBlasrM5()))
