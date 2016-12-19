
import logging
import os
from pbcore.util.Process import backticks

log = logging.getLogger(__name__)

def _pbtestdata():
    try:
        import pbtestdata
        return True
    except ImportError:
        return False

def _check_constools():
    cmd = "pbindex"
    o, r, m = backticks(cmd)
    if r != 1:
        return False

    cmd = "samtools"
    o, r, m = backticks(cmd)
    if r != 1:
        return False

    cmd = "pbmerge"
    o, r, m = backticks(cmd)
    if r != 1:
        return False
    return True

def _internal_data():
    if os.path.exists("/pbi/dept/secondary/siv/testdata"):
        return True
    return False
