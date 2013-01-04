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

__doc__="""Simple storage classes for performing one-dimensional set
operations on integer ranges."""
import bisect

class Range:
    """Simple storage class for performing one-dimensional set
operations on integer ranges.

    Ranges are stored as [start,end) with start<end (i.e. end is exclusive)
    """
    def __init__( self, start=0, end=0 ):
        start = int(start)
        end   = int(end)
        if end<start:
            self.start = end
            self.end = start
        else:
            self.start = start
            self.end = end

    def getLength( self ):
        return len(self)

    def getStart( self ):
        return self.start

    def getEnd( self ):
        return self.end

    def copy( self ):
        return Range(self.start, self.end)

    def __getitem__( self, i ):
        if i==0:
            return self.start
        if i==1:
            return self.end
        raise Exception( "Can't access key=%s in Range" % str(i) )

    def __iter__(self):
        return xrange( self.start, self.end ).__iter__()

    def __len__(self):
        return self.end - self.start

    def __contains__( self, x ):
        return x >= self.start and x < self.end

    def __str__( self ):
        return '[%d,%d)' % ( self.start, self.end )

    def __eq__( self, v ):
        return self.start==v.start and self.end==v.end

    def addDelta(self, delta):
        self.start += delta
        self.end += delta

    def intersects( self, range2 ):
        return self.contains(range2.start) or range2.contains(self.start)

    def intersect( self, range2 ):
        "Returns Range corresponding to intersection."
        if not self.intersects( range2 ):
            return Range(0,0)
        return Range( max(self.start,range2.start), min(self.end,range2.end) )

    def contains( self, x ):
        return x in self

    def containsRange( self, otherRange ):
        return self.contains(otherRange.start) and \
               self.contains(otherRange.end - 1)

    def union( self, range2 ):
        """Replaces self with a range which encompasses the current
        range and the provided range."""
        self.start = min( range2.start, self.start )
        self.end = max( range2.end, self.end )

class Ranges:
    """Represents an ordered and non-overlapping collection of ranges.
    Not an efficient implementation for large N.  
    TODO: more efficient would be i.e. an interval tree"""
    def __init__( self, key=lambda x:x.start ):
        self._ranges = []
        self._key = key

    def addRange( self, range ):
        bisect.insort_right( self._ranges, ( self._key(range), range.copy() ) )
        self.__normalize()

    def removeRange( self, range ):
        del_list = []
        new_list = []
        for i, r in enumerate(self._ranges):
            if r[1].intersects(range):
                if range.containsRange(r[1]):
                    del_list.append(i)
                elif r[1].containsRange( range ):
                    del_list.append(i)
                    r1 = Range(r[1].start,range.start)
                    if len(r1)>0: new_list.append( r1 )
                    r2 = Range(range.end,r[1].end)
                    if len(r2)>0: new_list.append( r2 )
                else:
                    if r[1].start < range.start:
                        r[1].end = range.start
                    else:
                        r[1].start = range.end
        nDel = 0
        for i in del_list:
            del self._ranges[i-nDel]
            nDel += 1
        for r in new_list:
            self.addRange( r )

    def __normalize( self ):
        """Ensure that the class invariant is maintained.
           Namely that the list of ranges is ordered and non-overlapping.
        """
        if len(self._ranges)<2:
            return
        del_list = []
        j = 0
        for i in xrange(0,len(self._ranges)):
            if i==j: continue
            r1 = self._ranges[j][1]
            r2 = self._ranges[i][1]
            if r1.intersects(r2):
                r1.union( r2 )
                del_list.append(i)
            else:
                j = i
        nDel = 0
        for i in del_list:
            del self._ranges[i-nDel]
            nDel += 1

    def __len__( self ):
        if len(self._ranges)==0: return 0
        return self._ranges[-1][1].end - self._ranges[0][1].start

    def __iter__( self ):
        """Iterates over Range"""
        for r in self._ranges: yield r[1]

    def __contains__( self, x ):
        """Returns True if integer x is contained in these ranges."""
        for r in self._ranges:
            if x in r:
                return True
        return False

    def span( self ):
        """Returns a Range object representing the span of these Ranges"""
        if len(self._ranges)==0: return Range(0,0)
        return Range( self._ranges[0][1].start, self._ranges[-1][1].end )

    def intersects( self, range2 ):
        """Returns True if range2 intersects any Range in self."""
        for r in self:
            if r.intersects(range2):
                return True
        return False

    def getIntersectingRange( self, range2 ):
        """Returns the Range in self that overlaps range2 or None if
        no range overlaps."""
        for r in self:
            if r.intersects(range2):
                return r
        return None
    
    def getIntersectingRanges( self, range2 ):
        """Returns the Ranges in self that overlap range2"""
        for r in self:
            if r.intersects(range2):
                yield r

    def __str__( self ):
        """For debugging"""
        return 'Rs {'+' '.join([ str(r[1]) for r in self._ranges ])+'}'

    def gaps( self ):
        """Iterates over 'gaps', which are defined by pairs of flanking ranges."""
        for i in range(1,len(self._ranges)):
            yield ( self._ranges[i-1][1], self._ranges[i][1] )

    def merge( self, ranges ):
        """Merges the ranges in ranges (class Ranges) with this object."""
        for range in ranges:
            bisect.insort_right( self._ranges, ( self._key(range), range.copy() ) )
        self.__normalize()

class OverlappingRanges:
    """Represents an ordered and potentially overlapping collection of ranges."""
    def __init__( self, key=lambda x:x.start ):
        self._ranges = []
        self._key = key

    def addRange( self, range ):
        bisect.insort_right( self._ranges, ( self._key(range), range.copy() ) )

    def __len__( self ):
        if len(self._ranges)==0: return 0
        return self._ranges[-1][1].end - self._ranges[0][1].start

    def __iter__( self ):
        for r in self._ranges: yield r[1]

    def span( self ):
        if len(self._ranges)==0: return Range(0,0)
        return Range( self._ranges[0][1].start, self._ranges[-1][1].end )

    def __str__( self ):
        return 'Rs {'+' '.join([ str(r[1]) for r in self._ranges ])+'}'

    def overlappingRanges(self, query):
        # TODO improve speed?

        startIdx = bisect.bisect( self._ranges, query.getStart() )
        for (end, target) in self._ranges[startIdx:]:
            if target.intersects(query):
                yield target


# unit tests
if __name__=='__main__':

    #--- Range unit tests
    r1 = Range( 5, 10 )
    r2 = Range( 10, 15 )
    r3 = Range( 7, 15 )
    r4 = Range( 5, 10 )

    print 'r1 = %s' % str(r1)
    print 'r2 = %s' % str(r2)
    print 'r3 = %s' % str(r3)
    print 'r4 = %s' % str(r4)

    print 'r1.contains(5) = %d' % r1.contains(5)
    print 'r1.contains(10) = %d' % r1.contains(10)

    print 'r1.intersects(r2) = %d' % r1.intersects(r2)
    print 'r1.intersects(r3) = %d' % r1.intersects(r3)

    print 'r1.intersect(r2) = %s' % r1.intersect(r2)
    print 'r1.intersect(r3) = %s' % r1.intersect(r3)

    print 'r1==r4 = %s' % str(r1==r4)

    #--- Ranges unit tests
    r = Ranges()
    r.addRange( Range( 1,3 ) )
    r.addRange( Range( 9,12 ) )
    print '------'
    print  'r = [1,3)+[9,12) = %s' % str(r)
    r.addRange( Range( 2,5 ) )
    print  'r + [2,5) = %s' % str(r)
    r.addRange( Range( 1,12 ) )
    print  'r + [1,12) = %s' % str(r)
    r.addRange( Range( 14,15 ) )
    print  'r + [14,15) = %s' % str(r)
    r.addRange( Range( 20,25 ) )
    print  'r + [20,25) = %s' % str(r)
    r.addRange( Range( 11,22 ) )
    print  'r + [11,22) = %s' % str(r)

    r5 = Ranges()
    r5.addRange( Range(1,25) )
    r5.addRange( Range(27,29) )
    r5.addRange( Range(35,40) )
    r6 = Ranges()
    r6.addRange( Range( 2, 5 ) )
    r6.addRange( Range( 20, 30 ) )
    r6.addRange( Range( 42, 45 ) )
    print '------'
    print 'r5 = %s' % str(r5)
    print 'r6 = %s' % str(r6)
    r5.merge(r6)
    print 'r5.merge(r6) = %s' % str(r5)

    # now r is 1,25
    print '------'
    print 'r = %s' % str(r)
    print 'r1 = %s' % str(r1)
    r.removeRange(r1)
    print 'r - r1 = %s' % str(r)
    # now r is [1,5) [10,25)
    r5 = Range( 3, 12 )
    print 'r5 = %s' % str(r5)
    r.removeRange(r5)
    print 'r - r5 = %s' % str(r)
    r.removeRange(Range(-1,3))
    print 'r - [-1,3) = %s' % str(r)
    r.removeRange(Range(1,3))
    print 'r - [1,3) = %s' % str(r)
    r.removeRange(Range(1,25))
    print 'r - [1,25) = %s' % str(r)

    #--- OverlappingRanges unit tests
    r = OverlappingRanges()
    r.addRange( Range( 1,3 ) )
    r.addRange( Range( 0,15 ) )
    r.addRange( Range( 9,12 ) )
    print  '\nOverlappingRanges tests\n\nr = [1,3)+[0,15)+[9,12) = %s\n' % str(r)

    queryRanges = [ Range(0,1), Range(2,4), Range(13,15), Range(15,17) ]
    for qRange in queryRanges:
        print "query %s is overlapped by:" % str(qRange)
        overlappingLengthSum = 0
        for oRange in r.overlappingRanges( qRange ):
            print str(oRange)

