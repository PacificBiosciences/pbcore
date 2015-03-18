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
# ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,g SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#################################################################################

# Authors: David Alexander

from pbcore.io.base import getFileHandle
from os.path import dirname, isabs, join, abspath, expanduser
import xml.etree.ElementTree as ET


__all__ = [ "readFofn",
            "readInputXML",
            "enumeratePulseFiles" ]

def readFofn(f):
    """
    Return iterator over filenames in a FOFN ("file-of-filenames")
    file or file-like object.

    If f is a path to a true FOFN on disk, any paths listed in the
    FOFN that are relative (i.e., do not contain a leading '/') will
    be reckoned from the directory containing the FOFN.
    """
    if isinstance(f, basestring):
        fofnRoot = dirname(abspath(expanduser(f)))
    else:
        fofnRoot = None

    for line in getFileHandle(f):
        path = line.rstrip()
        if not path:
            continue            # skip empty lines
        elif isabs(path):
            yield path
        elif fofnRoot is not None:
            yield join(fofnRoot, path)
        else:
            raise IOError, "Cannot handle relative paths in StringIO FOFN"

def readInputXML(fname):
    tree = ET.parse(fname)
    root = tree.getroot()
    for elt in root.iter():
        if elt.tag=="location":
            yield elt.text

def enumeratePulseFiles(fname):
    """
    A pulse file is a file with suffix .bax.h5, .plx.h5, or bas.h5

    fname is either a name of a pulse file, a list of names of pulse
    files, a FOFN (file of file names) listing pulse files, or an
    input.xml file.

    This is a generalization of readFofn for the case where fname is
    of type fofn|pulse, provided for convenience for tools that accept
    such an argument.
    """
    if isinstance(fname, list):
        for fname_ in fname:
            yield fname_
    elif fname.endswith(".fofn"):
        for pls in readFofn(fname):
            yield pls
    elif fname.endswith(".xml"):
        for pls in readInputXML(fname):
            yield pls
    else:
        yield fname
