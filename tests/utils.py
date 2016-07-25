
import logging
import os
from pbcore.util.Process import backticks
from pbcore.io.dataset.utils import BamtoolsVersion

log = logging.getLogger(__name__)

def _pbtestdata():
    try:
        import pbtestdata
        return True
    except ImportError:
        return False

def _check_constools():
    if not BamtoolsVersion().good:
        log.warn("Bamtools not found or out of date")
        return False

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
