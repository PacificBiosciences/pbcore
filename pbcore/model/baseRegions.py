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
    return [x for x in lst if x!=None]


class BaseRegionsMixin:
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
