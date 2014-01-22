
from pbcore.io import M4Reader, M5Reader
import pbcore.data as D


def test_m4():
    l = list(M4Reader(D.getBlasrM4()))

def test_m5():
    l = list(M5Reader(D.getBlasrM5()))
