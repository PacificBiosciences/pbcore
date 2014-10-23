#################################################################################
# Copyright (c) 2011-2013, Pacific Biosciences of California, Inc.
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

from __future__ import absolute_import
from string import maketrans
import re


DNA_COMPLEMENT = maketrans('agctAGCT-N', 'tcgaTCGA-N')

def reverse( sequence ):
    """Return the reverse of any sequence
    """
    return sequence[::-1]

def complement( sequence ):
    """
    Return the complement of a sequence
    NOTE: This only currently supports DNA
    """
    if re.search('[^AGCTN-]', sequence.upper()):
        raise ValueError("Sequence contains invalid DNA characters - "
                         "only [AGCTN-] allowed")
    return sequence.translate( DNA_COMPLEMENT )

def reverseComplement( sequence ):
    """
    Return the reverse-complement of a sequence
    NOTE: This only currently supports DNA
    """
    return reverse(complement(sequence))

def splitRecordName( name ):
    """Separate a record name into it's Id and Metadata
    """
    nameParts = re.split('\s', name, maxsplit=1)
    id_ = nameParts[0]
    if len(nameParts) > 1:
        metadata = nameParts[1].strip()
    else:
        metadata = None
    return (id_, metadata)
