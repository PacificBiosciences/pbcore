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

import argparse
import logging

class PBToolRunner(object):
    @staticmethod
    def getLogFormat(): 
        return '%(asctime)s [%(levelname)s] %(message)s'

    def getVersion(self):
        raise NotImplementedError()

    def __init__(self, description):
        self._parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                               description=description)
        self._setMainParser()

        self._parser.add_argument('-i', '--info', action='store_true', dest='info', default=False, 
                                 help='turn on progress monitoring to stdout [%(default)s]')
        self._parser.add_argument('-d', '--debug', action='store_true', dest='debug', default=False, 
                                 help='turn on progress monitoring to stdout and keep temp files [%(default)s]')
        self._parser.add_argument('-v', '--version', action='version', version= '%(prog)s ' + self.getVersion())

    def _setMainParser(self):
        self.parser = self._parser

    def parseArgs(self):
        self.args = self._parser.parse_args()
    
    def setupLogging(self):
        logLevel = logging.INFO if self.args.info else logging.WARN
        logLevel = logging.DEBUG if self.args.debug else logLevel
        logging.basicConfig(level=logLevel, format=self.getLogFormat())
        
    def validateArgs(self):
        '''
        Method to validate args
        '''
        pass

    def start(self):
        self.parseArgs()
        self.setupLogging()
        self.validateArgs()
        self.run()

    def run(self):
        pass

class PBMultiToolRunner(PBToolRunner):

    def _setMainParser(self):
        self.parser = argparse.ArgumentParser(add_help=False)

    def getSubParsers(self):
        return self._parser.add_subparsers(dest='subName') 


