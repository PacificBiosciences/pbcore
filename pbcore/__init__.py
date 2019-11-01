from __future__ import absolute_import, division, print_function

import pkg_resources

try:
    __VERSION__ = pkg_resources.get_distribution('pbcore').version
except Exception:
    __VERSION__ = 'unknown'
