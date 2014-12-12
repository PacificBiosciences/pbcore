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

# Author: David Alexander

class AlignmentRecordMixin(object):
    """
    Mixin class providing some higher-level functionality for objects from
    """
    @property
    def referenceStart(self):
        """
        The left bound of the alignment, in reference coordinates.
        """
        return self.tStart

    @property
    def referenceEnd(self):
        """
        The right bound of the alignment, in reference coordinates.
        """
        return self.tEnd

    @property
    def readStart(self):
        """
        The left bound of the alignment, in read coordinates (from the BAS.H5 file).
        """
        return self.rStart

    @property
    def readEnd(self):
        """
        The right bound of the alignment, in read coordinates (from the BAS.H5 file).
        """
        return self.rEnd

    @property
    def referenceSpan(self):
        """
        The length along the reference implied by this alignment.
        """
        return self.tEnd - self.tStart

    @property
    def readLength(self):
        """
        The length of the read.
        """
        return self.rEnd - self.rStart

    def __len__(self):
        return self.readLength

    def spansReferencePosition(self, pos):
        """
        Does the alignment span the given reference position?
        """
        return self.tStart <= pos < self.tEnd

    def spansReferenceRange(self, start, end):
        """
        Does the alignment span the given reference range, in its entirety?
        """
        assert start <= end
        return (self.tStart <= start <= end <= self.tEnd)

    def overlapsReferenceRange(self, start, end):
        """
        Does the alignment overlap the given reference interval?
        """
        assert start <= end
        return (self.tStart < end) and (self.tEnd > start)

    def containedInReferenceRange(self, start, end):
        """
        Is the alignment wholly contained within a given reference interval?
        """
        assert start <= end
        return (start <= self.tStart <= self.tEnd <= end)
