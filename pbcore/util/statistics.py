# NOTE: sequence identity functions are tested in
#   tests/est_mapped_sequence_identity.py

import math

import numpy as np


class Constants:
    MAX_QV = 60
    # (identical) cutoffs for RQ and QV for "High-Fidelity" reads
    HIFI_QV = 20
    HIFI_RQ = 0.99


def accuracy_as_phred_qv(accuracy, max_qv=Constants.MAX_QV):
    """
    Convert fractional accuracy to Phred QV: 0.999 --> 30
    Negative accuracy is not allowed except for the value -1, which is output
    by CCS for unpolished reads, and is treated as Q0.

    returns: float or numpy array
    """
    if isinstance(accuracy, (float, int)):
        if accuracy == -1:
            return 0
        assert 0 <= accuracy <= 1.0
        if accuracy == 1:
            return max_qv
        return -10 * math.log10(1 - accuracy)
    else:
        if isinstance(accuracy, (tuple, list)):
            accuracy = np.array(accuracy)
        accuracy[accuracy == -1] = 0.0
        error_rate = 1.0 - accuracy
        min_error_rate = 10 ** (-max_qv / 10.0)
        zero_error = error_rate < min_error_rate
        error_rate[zero_error] = min_error_rate
        return -10 * np.log10(error_rate)


def phred_qv_as_accuracy(qv):
    if qv == 0:
        return 0
    elif qv < 0:
        raise ValueError("Negative Phred scores not allowed")
    else:
        return 1.0 - 10**(-qv/10)


def pb_identity(n_mismatches, n_ins, n_del, read_length):
    """
    Old PacBio sequence identity computation used in SMRT Link v10 and
    earlier (but not elsewhere): 1 - (X + I + D) / L
    This also corresponds to the 'mc' tag output by pbmm2.
    Arguments can be either scalars or numpy arrays.
    """
    x = 1 - ((n_mismatches + n_ins + n_del) / read_length)
    if isinstance(x, float):
        return max(0, x)
    else:  # numpy arrays
        x[x < 0] = 0
        return x


def blast_identity(n_matches, n_mismatches, n_ins, n_del):
    """
    Sequence identity formula used in BLAST: M/(M+X+I+D)
    This also corresponds to the 'mi' tag output by pbmm2, and is now the
    primary user-facing metric in the mapping stats report.
    Arguments can be either scalars or numpy arrays.
    """
    return n_matches / (n_matches + n_mismatches + n_ins + n_del)


def gap_compressed_identity(n_matches, n_mismatches, n_ins_ops, n_del_ops):
    """
    Gap-compressed sequence identity, which simply counts insertion and
    deletion operations instead of alignment columns: M/(M+X+iOps+dOps)
    Arguments can be either scalars or numpy arrays.
    """
    return blast_identity(n_matches, n_mismatches, n_ins_ops, n_del_ops)
