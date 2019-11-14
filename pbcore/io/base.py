# Base classes for readers and writers.
# Author: David Alexander

from __future__ import absolute_import, division, print_function

from future.utils import string_types

import gzip
from os.path import abspath, expanduser

__all__ = [ "ReaderBase", "WriterBase" ]

def isFileLikeObject(o):
    return hasattr(o, "read") and hasattr(o, "write")

def getFileHandle(filenameOrFile, mode="r"):
    """
    Given a filename not ending in ".gz", open the file with the
    appropriate mode.

    Given a filename ending in ".gz", return a filehandle to the
    unzipped stream.

    Given a file object, return it unless the mode is incorrect--in
    that case, raise an exception.
    """
    assert mode in ("r", "w", "rt", "wt")

    if isinstance(filenameOrFile, string_types):
        filename = abspath(expanduser(filenameOrFile))
        if filename.endswith(".gz"):
            return gzip.open(filename, mode)
        else:
            return open(filename, mode)
    elif isFileLikeObject(filenameOrFile):
        return filenameOrFile
    else:
        raise Exception("Invalid type to getFileHandle")

class ReaderBase(object):
    def __init__(self, f):
        """
        Prepare for iteration through the records in the file
        """
        self.file = getFileHandle(f, "rt")
        if hasattr(self.file, "name"):
            self.filename = self.file.name
        else:
            self.filename = "(anonymous)"

    def close(self):
        """
        Close the underlying file
        """
        self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __repr__(self):
        return "<%s for %s>" % (type(self).__name__, self.filename)

class WriterBase(object):
    def __init__(self, f):
        """
        Prepare for output to the file
        """
        self.file = getFileHandle(f, "wt")
        if hasattr(self.file, "name"):
            self.filename = self.file.name
        else:
            self.filename = "(anonymous)"

    def close(self):
        """
        Close the underlying file
        """
        self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __repr__(self):
        return "<%s for %s>" % (type(self).__name__, self.filename)

    def writeRecord(self, *args, **kwds):
        pass
