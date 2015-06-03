#################################################################################
# Copyright (c) 2011-2015, Pacific Biosciences of California, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Pacific Biosciences nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE.  THIS SOFTWARE IS PROVIDED BY PACIFIC BIOSCIENCES AND ITS
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR
# ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#################################################################################

# Base classes for readers and writers.
# Author: David Alexander

from __future__ import absolute_import
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
    assert mode in ("r", "w")

    if isinstance(filenameOrFile, basestring):
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
        self.file = getFileHandle(f, "r")
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
        self.file = getFileHandle(f, "w")
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
