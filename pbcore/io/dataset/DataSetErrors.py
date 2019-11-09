# Author: Martin D. Smith

from __future__ import absolute_import, division, print_function

from builtins import super

class InvalidDataSetIOError(Exception):
    """The base class for all DataSetIO related custom exceptions
    """


class ResourceMismatchError(InvalidDataSetIOError):

    def __init__(self, responses):
        super().__init__()
        self.responses = responses

    def __str__(self):
        return "Resources responded differently: " + ', '.join(
            map(str, self.responses))


