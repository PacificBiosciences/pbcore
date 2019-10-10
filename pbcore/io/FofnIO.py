# Authors: David Alexander

from __future__ import absolute_import, division, print_function

from future.utils import string_types

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
    if isinstance(f, string_types):
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
            raise IOError("Cannot handle relative paths in StringIO FOFN")

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
