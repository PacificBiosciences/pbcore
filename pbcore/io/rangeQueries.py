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

import h5py as h
import numpy as n
import bisect

def rightmostBinSearch(vec, val):
    """
    Return the rightmost position in the vector vec of val. If val is
    absent then we return the leftmost position of the value:
    min(vec[vec > val]). If val is greater than all elements in vec we
    return len(vec).
    """
    assert(len(vec) > 0)

    i = bisect.bisect_left(vec, val)

    if (len(vec) == i):
        return(i)

    while (i + 1 < len(vec) and vec[i + 1] == val):
        i += 1

    return(i)

def leftmostBinSearch(vec, val):
    """
    Return the leftmost position in the vector vec of val. If val is
    absent then we return the lefternmost position for the value:
    max(vec[vec < val]). The time complexity here is potentially worse
    than log(n) because of the extra step of walking backwards.
    """
    assert(len(vec) > 0)
    i = bisect.bisect_left(vec, val)

    if (i == 0):
        return(i)
    elif (i == len(vec)):
        v = vec[i-1]
        i -= 1
    else:
        v = vec[i]

    if (v > val):
        i -= 1

    while (i > 0 and vec[i-1] == vec[i]):
        i -= 1

    return(i)


def getOverlappingRanges(tStart, tEnd, nBack, nOverlap, rangeStart, rangeEnd):
    """
    Return indices overlapping the range defined by [rangeStart,
    rangeEnd). Here tStart, tEnd, nBack, nOverlap are vectors of
    length n sorted according to tStart and tEnd. The vectors nBack
    and nOverlap are typically produced by computeIndices[DP].
    """
    assert(rangeEnd > rangeStart and
           len(tStart) == len(tEnd) == len(nBack) == len(nOverlap))

    lM = leftmostBinSearch(tStart, rangeStart)
    lM = lM - nBack[lM]
    rM = rightmostBinSearch(tStart, rangeEnd - .5)

    assert(rM >= lM and rM >= 0 and lM >= 0)

    if (lM == rM):
        return(n.array([], dtype = "uint32"))
    else:
        # We only keep the reads in the range lM .. rM that
        # actually overlap the range, as determined by
        # tEnd > rangeStart
        idxs   = n.arange(lM, rM, dtype = "uint32")   # lM .. rM
        toKeep = tEnd[idxs] > rangeStart
        return(idxs[toKeep])

def projectIntoRange(tStart, tEnd, winStart, winEnd):
    """
    Find coverage in the range [winStart, winEnd) implied by tStart,
    tEnd vectors.  Coverage can be most efficiently calculated by
    first obtaining all reads overlapping the range using the
    getOverlappingRanges function then projecting them into the same
    or smaller range
    """
    assert(len(tStart) == len(tEnd))
    res = n.zeros(shape=winEnd-winStart, dtype=n.uint)
    # Clip to window and translate.
    # Be careful to avoid underflow!
    tStart_ = n.clip(tStart, winStart, winEnd) - winStart
    tEnd_   = n.clip(tEnd,   winStart, winEnd) - winStart
    for (s, e) in zip(tStart_, tEnd_):
        res[s:e] += 1
    return res

def makeReadLocator(cmpH5, refSeq):
    """
    Return a function which can be called iteratively to find reads
    quickly.
    """
    if not cmpH5.isSorted: raise Exception, "CmpH5 is not sorted"
    refInfo = cmpH5.referenceInfo(refSeq)
    offStart, offEnd = refInfo.StartRow, refInfo.EndRow

    if (offEnd - offStart > 0):
        refAlignIdx = cmpH5.alignmentIndex[offStart:offEnd, ]
        returnEmpty = False
    else:
        refAlignIdx = cmpH5.alignmentIndex[1:2, ]
        returnEmpty = True

    def f(rangeStart, rangeEnd, justIndices = False):
        if returnEmpty:
            ## This looks strange, but the idea is that a rowless matrix
            ## still has columns and these are what I want to preserve --
            ## h5py objects cannot be subset by a vector of length 0,
            ## however, numpy allows this.
            idxs = n.array([], dtype = 'uint32')
        else:
            idxs = getOverlappingRanges(refAlignIdx.tStart, refAlignIdx.tEnd,
                                        refAlignIdx.nBackRead, refAlignIdx.nReadOverlap,
                                        rangeStart, rangeEnd)
        if justIndices:
            return(idxs + offStart)
        else:
            return(refAlignIdx[idxs,])
    return f

def getReadsInRange(cmpH5, coords, justIndices = False):
    """
    Return an ndarray representing the portion of the reads which
    overlap the range specfied by coords, where coords is a
    three-tuple composed of (refSeqID, rangeStart, rangeEnd).  Here,
    cmpH5 is an hdf5 object representing a pointer to a sorted cmp.h5
    file.
    """
    if not cmpH5.isSorted: raise Exception, "CmpH5 is not sorted"
    return makeReadLocator(cmpH5, coords[0])(coords[1], coords[2], justIndices)

def getCoverageInRange(cmpH5, coords, rowNumbers=None):
    """
    Return a vector of length: coords[2] - coords[1] where each
    element represents the number of reads overlapping that position
    in the cmp.h5 file.
    """
    if not cmpH5.isSorted: raise Exception, "CmpH5 is not sorted"
    if rowNumbers==None:
        rowNumbers  = getReadsInRange(cmpH5, coords, justIndices=True)
    if (len(rowNumbers))==0:
        return n.array([0]*(coords[2] - coords[1]))
    else:
        return(projectIntoRange(cmpH5.tStart[rowNumbers], cmpH5.tEnd[rowNumbers], coords[1], coords[2]))

