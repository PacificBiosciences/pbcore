from __future__ import absolute_import, division, print_function

import math

import numpy as np


class Constants(object):
    MAX_QV = 60


def accuracy_as_phred_qv(accuracy, max_qv=Constants.MAX_QV):
    """
    Convert fractional accuracy to Phred QV: 0.999 --> 30

    returns: float or numpy array
    """
    if isinstance(accuracy, (float, int)):
        assert 0 <= accuracy <= 1.0
        if accuracy == 1:
            return max_qv
        return -10 * math.log10(1 - accuracy)
    else:
        if isinstance(accuracy, (tuple, list)):
            accuracy = np.array(accuracy)
        error_rate = 1.0 - accuracy
        min_error_rate = 10 ** (-max_qv / 10.0)
        zero_error = error_rate < min_error_rate
        error_rate[zero_error] = min_error_rate
        return -10 * np.log10(error_rate)
