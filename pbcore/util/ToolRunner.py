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
                print("--debug requires module 'ipdb'")
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
