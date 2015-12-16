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

__all__ = [ "BaseRegionsMixin",
            "ExtraBaseRegionsMixin",
            "ADAPTER_REGION",
            "INSERT_REGION",
            "HQ_REGION" ]

# Region types
ADAPTER_REGION = 0
INSERT_REGION  = 1
HQ_REGION      = 2


# Interval arithmetic
def intersectRanges(r1, r2):
    b1, e1 = r1
    b2, e2 = r2
    b, e = max(b1, b2), min(e1, e2)
    return (b, e) if (b < e) else None

def removeNones(lst):
    return filter(lambda x: x!=None, lst)


class BaseRegionsMixin(object):
    """
    Mixin class for "ZMW" client classes providing access to base
    regions and reads sliced to those regions.

    Requires the client subclass to provide 'regionsTable' and 'read'
    (subrange slicing) methods with the correct semantics.

    The "...Region[s]" calls here return one or more intervals ((int, int));

    *All accessors in this mixin class implicitly clip regions to the
     HQ region.*
    """
    @property
    def hqRegion(self):
        """
        Return the HQ region interval.

        The HQ region is an interval of basecalls where the basecaller has
        inferred that a single sequencing reaction is taking place.
        Secondary analysis should only use subreads within the HQ
        region.  Methods in this class, with the exception of the
        "NoQC" methods, return data appropriately clipped/filtered to
        the HQ region.
        """
        rt = self.regionTable
        hqRows = rt[rt.regionType == HQ_REGION]
        assert len(hqRows) == 1
        hqRow = hqRows[0]
        return hqRow.regionStart, hqRow.regionEnd

    def _unclippedInsertRegions(self):
        return [ (region.regionStart, region.regionEnd)
                 for region in self.regionTable
                 if region.regionType == INSERT_REGION ]

    @property
    def insertRegions(self):
        """
        Get insert regions as intervals, clipped to the HQ region
        """
        hqRegion = self.hqRegion
        return removeNones([ intersectRanges(hqRegion, region)
                             for region in self._unclippedInsertRegions() ])

    @property
    def subreads(self):
        """
        Get the subreads as a list of ZmwRead objects.  Restricts focus,
        and clips to, the HQ region.  This method can be used by
        production code.
        """
        return [ self.read(readStart, readEnd)
                 for (readStart, readEnd) in self.insertRegions ]

    def _unclippedAdapterRegions(self):
        return [ (region.regionStart, region.regionEnd)
                 for region in self.regionTable
                 if region.regionType == ADAPTER_REGION ]

    @property
    def adapterRegions(self):
        """
        Get adapter regions as intervals, performing clipping to the HQ region
        """
        hqRegion = self.hqRegion
        return removeNones([ intersectRanges(hqRegion, region)
                             for region in self._unclippedAdapterRegions() ])


    @property
    def adapters(self):
        """
        Get the adapter hits as a list of ZmwRead objects.  Restricts
        focus, and clips to, the HQ region.  This method can be used
        by production code.
        """
        return [ self.read(readStart, readEnd)
                 for (readStart, readEnd) in self.adapterRegions ]



class ExtraBaseRegionsMixin(BaseRegionsMixin):
    """
    Mixin class for a "ZMW" class providing the basic region
    accessors, and additional region accessors that do not clip to the
    HQ region.

    These accessors only make sense for bas.h5 ZMW objects, where we
    have access to region information extending beyond the HQ region.
    In the BAM world, "regions" are all inherently clipped to HQ by
    design of PPA.

    Requires 'readNoQC' accessor
    """
    @property
    def adapterRegionsNoQC(self):
        """
        Get adapter regions as intervals, without clipping to the HQ
        region.  Don't use this unless you know what you're doing.
        """
        return self._unclippedAdapterRegions()

    @property
    def adaptersNoQC(self):
        """
        Get the adapters, including data beyond the bounds of the HQ
        region.

        .. warning::

            It is not recommended that production code use this method
            as we make no guarantees about what happens outside of the
            HQ region.
        """
        return [ self.read(readStart, readEnd)
                 for (readStart, readEnd) in self.adapterRegionsNoQC ]

    @property
    def insertRegionsNoQC(self):
        """
        Get insert regions as intervals, without clipping to the HQ
        region.  Don't use this unless you know what you're doing.
        """
        return self._unclippedInsertRegions()

    @property
    def subreadsNoQC(self):
        """
        Get the subreads, including data beyond the bounds of the HQ region.

        .. warning::

            It is not recommended that production code use this method
            as we make no guarantees about what happens outside of the
            HQ region.
        """
        return [ self.read(readStart, readEnd)
                 for (readStart, readEnd) in self.insertRegionsNoQC ]
