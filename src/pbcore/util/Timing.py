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


__doc__="""Useful classes and functions for monitoring resource consumption (time and memory)"""
import os
import time
import datetime

class Timer:
    def __init__(self):
        self.results = []
       
    def startTask(self, taskName):
        r = TimingResult( taskName )
        r.tick()
        self.results.append(r)
        
    def endTask(self):
        self.results[-1].tock()
        
    def report(self, out):
        for result in self.results:
            out.write( str(result) + os.linesep )
    
    def getTaskDuration(self, taskName):
        for result in self.results:
            if result.taskName == taskName:
                return result.deltaTime
        
class TimingResult:
    def __init__(self, taskName):
        self.taskName = taskName
        self.startTime = 0.0
        self.deltaTime = None
        
    def tick(self):
        self.startTime = time.time()
        
    def tock(self):
        self.deltaTime = datetime.timedelta( \
            seconds=time.time()-self.startTime )
        
    def __str__(self):
        return 'task: %s; start: %s; delta: %s' % ( self.taskName, \
                                                    time.strftime('%H:%M:%S', time.localtime(self.startTime)),
                                                    str(self.deltaTime) )
        
# from O'Reilly Python Cookbook ( A Martelli, et al )
_proc_status = '/proc/%d/status' % os.getpid()
_scale = { 'kB': 1024.0, 'mB': 1024.0*1024.0, 'KB':1024.0, 'MB':1024.0*1024.0 }

def _VmB( VmKey ):
    """ Given a VmKey string, returns a number of bytes. """
    # get pseudo file /proc/<pid>/status
    try:
        t = open( _proc_status )
        v = t.read()
        t.close()
    except IOError:
        return 0.0
    # get VmKey line e.g. 'VMRSS: 9999 kB\n ...'
    i = v.index(VmKey)
    v = v[i:].split(None,3)
    if len(v)<3:
        return 0.0
    # convert Vm value to bytes
    return float(v[1]) * _scale[v[2]]

def memory( since=0.0 ):
    ''' Return virtual memory usage in bytes. '''
    return _VmB( 'VmSize:' ) - since

def resident( since=0.0 ):
    ''' Return resident memory usage in bytes. '''
    return _VmB( 'VmRSS:' ) - since

def stacksize( since=0.0 ):
    ''' Return stack size in bytes. '''
    return _VmB( 'VmStk:' ) - since

