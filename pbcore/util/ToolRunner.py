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

import argparse, cProfile, logging, pstats


LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"


class PBToolRunner(object):

    #
    # Interface to be overridden in subclasses (client code)
    #
    def getVersion(self):
        raise NotImplementedError()

    def run(self):
        raise NotImplementedError()

    def validateArgs(self):
        '''
        Method to validate args
        '''
        pass

    #
    # Methods below should not be overriden
    #
    def __init__(self, description):
        self._setupParsers(description)
        self._addStandardArguments()

    def _addStandardArguments(self):
        self.parser.add_argument(
            "--verbose", "-v",
            dest="verbosity", action="count",
            help="Set the verbosity level")
        self.parser.add_argument(
            '--version',
            action='version', version= '%(prog)s ' + self.getVersion())
        self.parser.add_argument(
            "--profile", action="store_true",
            help="Print runtime profile at exit")
        self.parser.add_argument(
            "--debug", action="store_true",
            help="Catch exceptions in debugger (requires ipdb)")

    def _setupParsers(self, description):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                              description=description)

    def _parseArgs(self):
        self.args = self.parser.parse_args()

    def _setupLogging(self):
        if self.args.verbosity >= 2:
            logLevel = logging.DEBUG
        elif self.args.verbosity == 1:
            logLevel = logging.INFO
        else:
            logLevel = logging.WARN
        logging.basicConfig(level=logLevel, format=LOG_FORMAT)

    def start(self):
        self._parseArgs()
        self._setupLogging()
        self.validateArgs()

        if self.args.debug:
            try:
                import ipdb
            except ImportError:
                print "--debug requires module 'ipdb'"
                return -1
            with ipdb.launch_ipdb_on_exception():
                self.run()

        elif self.args.profile:
            l = locals()
            cProfile.runctx("_rv=self.run()", globals(), l, "profile.out")
            pstats.Stats("profile.out").sort_stats("time").print_stats(20)
            return l["_rv"]
        else:
            return self.run()

class PBMultiToolRunner(PBToolRunner):
    def _setupParsers(self, description):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                              description=description)
        self.subParsers = self.parser.add_subparsers(dest="subCommand")
