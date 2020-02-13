# Author: Martin D. Smith

import logging

from .DataSetIO import *
from .DataSetUtils import *

log = logging.getLogger(__name__)
if not log.handlers:
    log.addHandler(logging.NullHandler())
