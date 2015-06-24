#!/usr/bin/env python

import sys
import argparse
import logging
import time
from pbcore.io.dataset import EntryPoints
from pbcore import __VERSION__


LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"

def _setup_logging():
    log = logging.getLogger()
    logging.Formatter.converter = time.gmtime
    if not log.handlers:
        logging.basicConfig(level=logging.WARN, format=LOG_FORMAT)
    return log

def get_subparsers():
    sps = [('create', EntryPoints.create_options),
           ('filter', EntryPoints.filter_options),
           ('merge', EntryPoints.merge_options),
           ('split', EntryPoints.split_options),
           ('validate', EntryPoints.validate_options),
           ('loadstats', EntryPoints.loadStatsXml_options),
           ('consolidate', EntryPoints.consolidate_options)]
    return sps

def add_subparsers(parser, sps):
    subparsers = parser.add_subparsers(
        title='DataSet sub-commands', dest='subparser_name',
        help="Type {command} -h for a command's options")
    for command_name, func in sps:
        subparser = subparsers.add_parser(command_name)
        subparser = func(subparser)
    return parser

def get_parser():
    description = 'Run dataset.py by specifying a command.'
    parser = argparse.ArgumentParser(version=__VERSION__,
            description=description)
    parser.add_argument("--debug", default=False, action='store_true',
                        help="Turn on debug level logging")
    subparser_list = get_subparsers()
    parser = add_subparsers(parser, subparser_list)
    return parser

def main(argv=sys.argv):
    """Main point of Entry"""
    log = _setup_logging()
    log.info("Starting {f} version {v} dataset manipulator".format(
        f=__file__, v=__VERSION__))
    parser = get_parser()
    args = parser.parse_args()
    if args.debug:
        log.setLevel(logging.DEBUG)
    return args.func(args)
    #return main_runner_default(argv[1:], get_parser(), log)

if __name__ == '__main__':
    sys.exit(main())
