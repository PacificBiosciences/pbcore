
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
