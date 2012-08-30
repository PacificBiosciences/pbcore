#################################################################################$$
# Copyright (c) 2011,2012, Pacific Biosciences of California, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright notice, this 
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice, 
#   this list of conditions and the following disclaimer in the documentation 
#   and/or other materials provided with the distribution.
# * Neither the name of Pacific Biosciences nor the names of its contributors 
#   may be used to endorse or promote products derived from this software 
#   without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY PACIFIC BIOSCIENCES AND ITS CONTRIBUTORS 
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED 
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR ITS 
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#################################################################################$$


import os
import tempfile
import subprocess
import numpy as n
import numpy.lib.recfunctions as rfn

PRINT_FORM = {n.dtype('S1').type:'%s',
              n.dtype(int).type:'%d',
              n.dtype(float).type:'%.2f'
              }

def getHeader(inFN, delim=','):
    """
    Return the header of a CSV as a list of column names.
    """
    return open(inFN,'r').readline().strip().split(delim)

def getRecArrayFromCSV(incsv, columnType=[], standardDtype=False, caseSensitive=False, sanitize=False):
    """
    Generate a record array from an input csv file. For 'strangely'
    formatted CSVs need the column type provided as a list of tuples. In
    the absence of a columnType, if standardDtype == True, all string 
    fields will have ``numpy.dtype('|S100')`` associated with them i.e.
    all string fields will be set to max length 100. caseSensitive == True
    preserves the case of the column headers. sanatize=True removes characters
    that are know to cause n.recfromcsv to error out (USE WITH CAUTION!)
    """
    data = n.ndarray([])
    if os.path.exists(incsv) and os.path.getsize(incsv) > 0:
        if sanitize:
            fout = tempfile.NamedTemporaryFile(suffix='_sanitized.csv', delete=True)
            subprocess.call('sed "s;#;;g" %s > %s' % (incsv, fout.name), shell=True)
            incsv = fout.name

        if columnType:
            dictCtype = dict(columnType)
            ctype = [(k,dictCtype[k]) for k in getHeader(incsv)]
            data = n.rec.fromrecords(n.genfromtxt(fname=incsv, delimiter=',', skip_header=1, dtype=ctype, autostrip=True), dtype=ctype)
        else:
            data = n.recfromcsv(incsv, autostrip=True, case_sensitive=caseSensitive)
            if standardDtype:
                t_dtype = [(dtn,data.dtype[dtn]) for dtn in data.dtype.names]
                t_dtype = map(lambda dt: (dt[0],n.dtype('|S100')) if dt[1].kind == 'S' else dt, t_dtype)
                data = n.rec.array(data.tolist(), dtype=t_dtype)
    
    if not data.shape:
        data.shape = (1,)    
    return data 
        
def addColumnToRecArray(baseRec, newArray, newColumn, tail=True):
    """
    Return a new record array based on baseRec with an
    extra column of name = newColumn i.e. ('PolRate','<f8')
    and values = newArray.
    """
    if tail:
        newdtype = n.dtype(baseRec.dtype.descr + [newColumn])
    else:
        newdtype = n.dtype([newColumn] + baseRec.dtype.descr)
    newRec = n.recarray((len(baseRec),), dtype=newdtype)
    for field in baseRec.dtype.fields:
        newRec[field] = baseRec[field]
    newRec[newColumn[0]] = newArray
    return newRec

def dropColumnFromRecArray(baseRec, columnNames):
    """
    Return a new record array based on baseRec with the columns
    present in the columnNames list removed.
    """
    return rfn.drop_fields(baseRec, columnNames)

def hstackRecArrays(r1, r2):
    """
    Horizontal stack record arrays fixing mismatches in str field lengths
    between the 2 dtypes.
    """
    if r1.dtype != r2.dtype:
        n_dtype = r1.dtype.descr
        for i in range(len(n_dtype)):
            if r1.dtype.descr[i][1][1] == 'S':
                n_dtype[i] = (n_dtype[i][0], 
                              '|S%d' % n.max((int(n_dtype[i][1][2:]),
                                              int(r2.dtype.descr[i][1][2:])))
                              )
        r1 = r1.astype(n_dtype)
        r2 = r2.astype(n_dtype)
    return n.hstack((r1,r2))

def printCSV_PR(data, filename, delim=','):
    """
    Print a record array to a CSV file using string formatting.
    """
    fout = open(filename,'w')
    fields = data.dtype.names
    print >>fout, delim.join(fields)
    if not data.shape:
        print >>fout, delim.join([PRINT_FORM[data[field].dtype.type] % data[field] for field in fields])
    else:
        for row in data:
            print >>fout, delim.join([PRINT_FORM[row[field].dtype.type] % row[field] for field in fields])

def printCSV(data, filename, delim=','):
    """
    Print a record array to a CSV file.
    """
    fout = open(filename,'w')
    fields = data.dtype.names
    print >>fout, delim.join(fields)
    if not data.shape:
        print >>fout, delim.join([str(data[field]) for field in fields])
    else:
        for row in data:
            print >>fout, delim.join([str(row[field]) for field in fields])

def fixCSV(inFN, outFN, delim=','):
    """
    Remove CSV rows that do not have the same number of columns as
    the header.
    """
    nColumns = len(getHeader(inFN, delim=delim))
    fout = open(outFN, 'w')
    for row in open(inFN, 'r'):
        if len(row.split(delim)) == nColumns:
            fout.write(row)
    fout.close()


