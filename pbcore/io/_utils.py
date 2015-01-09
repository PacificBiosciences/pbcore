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

from __future__ import absolute_import
import h5py, numpy as np
from cStringIO import StringIO


def arrayFromDataset(ds, offsetBegin, offsetEnd):
    """
    Extract a one-dimensional array from an HDF5 dataset.
    """
    shape = (offsetEnd - offsetBegin,)
    a = np.ndarray(shape=shape, dtype=ds.dtype)
    mspace = h5py.h5s.create_simple(shape)
    fspace = ds.id.get_space()
    fspace.select_hyperslab((offsetBegin,), shape, (1,))
    ds.id.read(mspace, fspace, a)
    return a


def splitFileContents(f, delimiter, BLOCKSIZE=8192):
    """
    Same semantics as f.read().split(delimiter), but with memory usage
    determined by largest chunk rather than entire file size
    """
    remainder = StringIO()
    while True:
        block = f.read(BLOCKSIZE)
        if not block:
            break
        parts = block.split(delimiter)
        remainder.write(parts[0])
        for part in parts[1:]:
            yield remainder.getvalue()
            remainder = StringIO()
            remainder.write(part)
    yield remainder.getvalue()



# For reasons that are obscure to me, the recarray outer join
# functionality in numpy's lib.recfunctions is broken as of numpy
# 1.6.1.  Here is the implementation I found in matplotlib (BSD
# compatible license; need to add license note to LICENSE), which
# seems to work.
#  --DHA

def is_string_like(obj):
    'Return True if *obj* looks like a string'
    if isinstance(obj, (str, unicode)): return True
    # numpy strings are subclass of str, ma strings are not
    if ma.isMaskedArray(obj):
        if obj.ndim == 0 and obj.dtype.kind in 'SU':
            return True
        else:
            return False
    try: obj + ''
    except: return False
    return True

def rec_join(key, r1, r2, jointype='inner', defaults=None, r1postfix='1', r2postfix='2'):
    """
    Join record arrays *r1* and *r2* on *key*; *key* is a tuple of
    field names -- if *key* is a string it is assumed to be a single
    attribute name. If *r1* and *r2* have equal values on all the keys
    in the *key* tuple, then their fields will be merged into a new
    record array containing the intersection of the fields of *r1* and
    *r2*.

    *r1* (also *r2*) must not have any duplicate keys.

    The *jointype* keyword can be 'inner', 'outer', 'leftouter'.  To
    do a rightouter join just reverse *r1* and *r2*.

    The *defaults* keyword is a dictionary filled with
    ``{column_name:default_value}`` pairs.

    The keywords *r1postfix* and *r2postfix* are postfixed to column names
    (other than keys) that are both in *r1* and *r2*.
    """

    if is_string_like(key):
        key = (key, )

    for name in key:
        if name not in r1.dtype.names:
            raise ValueError('r1 does not have key field %s'%name)
        if name not in r2.dtype.names:
            raise ValueError('r2 does not have key field %s'%name)

    def makekey(row):
        return tuple([row[name] for name in key])

    r1d = dict([(makekey(row),i) for i,row in enumerate(r1)])
    r2d = dict([(makekey(row),i) for i,row in enumerate(r2)])

    r1keys = set(r1d.keys())
    r2keys = set(r2d.keys())

    common_keys = r1keys & r2keys

    r1ind = np.array([r1d[k] for k in common_keys])
    r2ind = np.array([r2d[k] for k in common_keys])

    common_len = len(common_keys)
    left_len = right_len = 0
    if jointype == "outer" or jointype == "leftouter":
        left_keys = r1keys.difference(r2keys)
        left_ind = np.array([r1d[k] for k in left_keys])
        left_len = len(left_ind)
    if jointype == "outer":
        right_keys = r2keys.difference(r1keys)
        right_ind = np.array([r2d[k] for k in right_keys])
        right_len = len(right_ind)

    def key_desc(name):
        'if name is a string key, use the larger size of r1 or r2 before merging'
        dt1 = r1.dtype[name]
        if dt1.type != np.string_:
            return (name, dt1.descr[0][1])

        dt2 = r1.dtype[name]
        assert dt2==dt1
        if dt1.num>dt2.num:
            return (name, dt1.descr[0][1])
        else:
            return (name, dt2.descr[0][1])


    keydesc = [key_desc(name) for name in key]

    def mapped_r1field(name):
        """
        The column name in *newrec* that corresponds to the column in *r1*.
        """
        if name in key or name not in r2.dtype.names: return name
        else: return name + r1postfix

    def mapped_r2field(name):
        """
        The column name in *newrec* that corresponds to the column in *r2*.
        """
        if name in key or name not in r1.dtype.names: return name
        else: return name + r2postfix

    r1desc = [(mapped_r1field(desc[0]), desc[1]) for desc in r1.dtype.descr if desc[0] not in key]
    r2desc = [(mapped_r2field(desc[0]), desc[1]) for desc in r2.dtype.descr if desc[0] not in key]
    newdtype = np.dtype(keydesc + r1desc + r2desc)

    newrec = np.recarray((common_len + left_len + right_len,), dtype=newdtype)

    if defaults is not None:
        for thiskey in defaults:
            if thiskey not in newdtype.names:
                warnings.warn('rec_join defaults key="%s" not in new dtype names "%s"'%(
                    thiskey, newdtype.names))

    for name in newdtype.names:
        dt = newdtype[name]
        if dt.kind in ('f', 'i'):
            newrec[name] = 0

    if jointype != 'inner' and defaults is not None: # fill in the defaults enmasse
        newrec_fields = newrec.dtype.fields.keys()
        for k, v in defaults.items():
            if k in newrec_fields:
                newrec[k] = v

    for field in r1.dtype.names:
        newfield = mapped_r1field(field)
        if common_len:
            newrec[newfield][:common_len] = r1[field][r1ind]
        if (jointype == "outer" or jointype == "leftouter") and left_len:
            newrec[newfield][common_len:(common_len+left_len)] = r1[field][left_ind]

    for field in r2.dtype.names:
        newfield = mapped_r2field(field)
        if field not in key and common_len:
            newrec[newfield][:common_len] = r2[field][r2ind]
        if jointype == "outer" and right_len:
            newrec[newfield][-right_len:] = r2[field][right_ind]

    newrec.sort(order=key)

    return newrec


def drop_fields(rec, names):
    """
    Return a new numpy record array with fields in *names* dropped.
    """

    names = set(names)
    Nr = len(rec)

    newdtype = np.dtype([(name, rec.dtype[name]) for name in rec.dtype.names
                       if name not in names])

    newrec = np.recarray(rec.shape, dtype=newdtype)
    for field in newdtype.names:
        newrec[field] = rec[field]

    return newrec

def print_rec_array(rec):
    """
    Pretty-print a recarray
    """
    print "foo"


class CommonEqualityMixin(object):
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)
