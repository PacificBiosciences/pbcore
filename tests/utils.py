from __future__ import absolute_import, division, print_function

import unittest
import logging
import os
from pbcore.util.Process import backticks
from pbcore.io.dataset.utils import which

log = logging.getLogger(__name__)

def _pbtestdata():
    try:
        import pbtestdata
        return True
    except ImportError:
        return False

def _check_constools():
    return which('pbindex') and which('samtools') and which('pbmerge')

def _internal_data():
    if os.path.exists("/pbi/dept/secondary/siv/testdata"):
        return True
    return False

def _h5py():
    try:
        import h5py
        return True
    except ImportError:
        return False

skip_if_no_pbtestdata = unittest.skipUnless(_pbtestdata(),
                                            "PacBioTestData not installed")
skip_if_no_h5py = unittest.skipUnless(_h5py(), "h5py not installed")
skip_if_no_internal_data = unittest.skipUnless(_internal_data(),
                                               "Internal data not available")
skip_if_no_constools = unittest.skipUnless(_check_constools(),
                                           "Binary tools not found")
