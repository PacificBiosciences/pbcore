# sequence.py: module of basic sequence methods
# Authors: Brett Bowman, David Alexander

from __future__ import absolute_import, division, print_function

__all__ = [ "complement",
            "reverseComplement"]

from string import maketrans
import re

DNA_COMPLEMENT = maketrans('agcturyswkmbdhvnAGCTURYSWKMBDHV-N',
                           'tcgannnnnnnnnnnnTCGANNNNNNNNNNN-N')

def reverse( sequence ):
    """Return the reverse of any sequence
    """
    return sequence[::-1]

def complement( sequence ):
    """
    Return the complement of a sequence
    """
    if re.search('[^agcturyswkmbdhvnAGCTURYSWKMBDHVN-]', sequence):
        raise ValueError("Sequence contains invalid DNA characters - "
                         "only standard IUPAC nucleotide codes allowed")
    return sequence.translate( DNA_COMPLEMENT )

def reverseComplement( sequence ):
    """
    Return the reverse-complement of a sequence
    NOTE: This only currently supports DNA
    """
    return complement(sequence)[::-1]
