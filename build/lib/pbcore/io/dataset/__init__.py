
VERSION = (0, 1)

from DataSetIO import *

import logging

log = logging.getLogger(__name__)
if not log.handlers:
    log.addHandler(logging.NullHandler())

#def get_version():
#    """Return the version as a string. e.g. "0.7"
#
#    This uses a major.minor format
#
#    Each python module of the system (e.g, butler, detective, siv_butler.py)
#    will use this version +  individual changelist. This allows top level
#    versioning, and sub-component to be versioned based on a p4 changelist.
#
#    .. note:: This should be improved to be compliant with PEP 440.
#    """
#    return ".".join([str(i) for i in VERSION])
