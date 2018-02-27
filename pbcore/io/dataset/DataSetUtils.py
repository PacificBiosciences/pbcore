###############################################################################
# Copyright (c) 2011-2018, Pacific Biosciences of California, Inc.
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
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT
# NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR
# ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
###############################################################################

# Author: Martin D. Smith

from __future__ import absolute_import

import os
import logging

log = logging.getLogger(__name__)

def fileType(fname):
    """Get the extension of fname (with h5 type)"""
    remainder, ftype = os.path.splitext(fname)
    if ftype == '.h5':
        _, prefix = os.path.splitext(remainder)
        ftype = prefix + ftype
    elif ftype == '.index':
        _, prefix = os.path.splitext(remainder)
        if prefix == '.contig':
            ftype = prefix + ftype
    ftype = ftype.strip('.')
    return ftype

def getDataSetUuid(xmlfile):
    """
    Quickly retrieve the uuid from the root element of a dataset XML file,
    using a streaming parser to avoid loading the entire dataset into memory.
    Returns None if the parsing fails.
    """
    try:
        import xml.etree.cElementTree as ET
        for event, element in ET.iterparse(xmlfile, events=("start",)):
            return element.get("UniqueId")
    except Exception:
        return None


def getDataSetMetaType(xmlfile):
    """
    Quickly retrieve the MetaType from the root element of a dataset XML file,
    using a streaming parser to avoid loading the entire dataset into memory.
    Returns None if the parsing fails.
    """
    try:
        import xml.etree.cElementTree as ET
        for event, element in ET.iterparse(xmlfile, events=("start",)):
            return element.get("MetaType")
    except Exception:
        return None

