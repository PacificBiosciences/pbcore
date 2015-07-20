#/usr/bin/env python

import os
import argparse
from pbcore.io import DataSet
from pbcore.io.dataset.DataSetValidator import validateFile
import logging

log = logging.getLogger(__name__)

def createXml(args):
    dsTypes = DataSet.castableTypes()
    dset = dsTypes[args.dsType](*args.infile)
    log.debug("Dataset created")
    dset.write(args.outfile, validate=args.novalidate, relPaths=args.relative)
    log.debug("Dataset written")


def create_options(parser):
    parser.description = 'Create an XML file from a fofn or bam'
    parser.add_argument("outfile", type=str, help="The XML to create")
    #parser.add_argument("infile", type=validate_file, nargs='+',
    parser.add_argument("infile", type=str, nargs='+',
                        help="The fofn or BAM file(s) to make into an XML")
    parser.add_argument("--type", type=str, default='DataSet',
                        dest='dsType', help="The type of XML to create")
    parser.add_argument("--novalidate", action='store_false', default=True,
                        help=("Don't validate the resulting XML, don't touch "
                              "paths"))
    parser.add_argument("--relative", action='store_true', default=False,
                        help=("Make the included paths relative instead of "
                              "absolute (not compatible with --novalidate)"))
    parser.set_defaults(func=createXml)

def filterXml(args):
    log.error("Adding filters via CLI is temporarily out of order")
    exit(1)
    if args.infile.endswith('xml'):
        dataSet = DataSet(args.infile)
        filters = []
        separators = ['<=', '>=', '!=', '==', '>', '<', '=']
        for filt in args.filters:
            for sep in separators:
                if sep in filt:
                    param, condition = filt.split(sep)
                    condition = sep + condition
                    filters[param] = condition
                    break
        dataSet.addFilters([filters])
        log.info("{i} filters added".format(i=len(filters)))
        dataSet.write(args.outfile)
    else:
        raise IOError("No files found/found to be compatible")

def filter_options(parser):
    parser.description = 'Add filters to an XML file'
    #parser.add_argument("infile", type=validate_file,
    parser.add_argument("infile", type=str,
                        help="The xml file to filter")
    parser.add_argument("outfile", type=str, help="The resulting xml file")
    parser.add_argument("filters", type=str, nargs='+',
                        help="The values and thresholds to filter (e.g. "
                        "rq>0.85)")
    parser.set_defaults(func=filterXml)

def splitXml(args):
    log.debug("Starting split")
    dataSet = DataSet(args.infile)
    chunks = len(args.outfiles)
    if args.chunks:
        chunks = args.chunks
    dss = dataSet.split(chunks=chunks,
                        ignoreSubDatasets=(not args.subdatasets),
                        contigs=args.contigs,
                        maxChunks=args.maxChunks)
    infix = 'chunk{i}'
    if args.contigs:
        infix += 'contigs'
    if not args.outfiles:
        if not args.outdir:
            args.outfiles = ['.'.join(args.infile.split('.')[:-1] +
                                      [infix.format(i=chNum), 'xml'])
                             for chNum in range(len(dss))]
        else:
            args.outfiles = ['.'.join(args.infile.split('.')[:-1] +
                                      [infix.format(i=chNum), 'xml'])
                             for chNum in range(len(dss))]
            args.outfiles = [os.path.join(args.outdir,
                                          os.path.basename(outfn))
                             for outfn in args.outfiles]
    log.debug("Finished splitting")
    for out_fn, dset in zip(args.outfiles, dss):
        dset.write(out_fn)

def split_options(parser):
    parser.description = "Split the dataset"
    parser.add_argument("infile", type=str,
                        help="The xml file to split")
    parser.add_argument("--contigs", default=False, action='store_true',
                        help="Split on contigs")
    parser.add_argument("--chunks", default=False, type=int,
                        help="Split contigs into <chunks> total windows")
    parser.add_argument("--maxChunks", default=False, type=int,
                        help="Split contig list into at most <chunks> groups")
    parser.add_argument("--subdatasets", default=False, action='store_true',
                        help="Split on subdatasets")
    parser.add_argument("--outdir", default=False, type=str,
                        help="Specify an output directory")
    parser.add_argument("outfiles", nargs=argparse.REMAINDER,
                        type=str, help="The resulting xml files")
    parser.set_defaults(func=splitXml)

def mergeXml(args):
    dss = []
    for infn in args.infiles:
        dss.append(DataSet(infn))
    reduce(lambda ds1, ds2: ds1 + ds2, dss).write(args.outfile)

def merge_options(parser):
    parser.description = 'Combine XML (and BAM) files'
    parser.add_argument("outfile", type=str,
                        help="The resulting XML file")
    #parser.add_argument("infiles", type=validate_file, nargs='+',
    parser.add_argument("infiles", type=str, nargs='+',
                        help="The XML files to merge")
    parser.set_defaults(func=mergeXml)

def loadStatsXml(args):
    dset = DataSet(args.infile)
    dset.loadStats(args.statsfile)
    if args.outfile:
        dset.write(args.outfile, validate=False)
    else:
        dset.write(args.infile, validate=False)

def loadStatsXml_options(parser):
    parser.description = 'Load an sts.xml file into a DataSet XML file'
    parser.add_argument("infile", type=str,
                        help="The XML file to modify")
    parser.add_argument("statsfile", type=str,
                        help="The .sts.xml file to load")
    parser.add_argument("--outfile", type=str, default=None,
                        help="The XML file to output")
    parser.set_defaults(func=loadStatsXml)

def validateXml(args):
    validateFile(args.infile, args.skipFiles)
    print("{f} is valid DataSet XML with valid ResourceId "
          "references".format(f=args.infile))

def validate_options(parser):
    parser.description = 'Validate XML and ResourceId files'
    parser.add_argument("infile", type=str,
                        help="The XML file to validate")
    parser.add_argument("--skipFiles",
                        default=False, action='store_true',
                        help="Skip validating external resources")
    parser.set_defaults(func=validateXml)

def consolidateXml(args):
    """Combine BAMs and apply the filters described in the XML file, producing
    one consolidated XML"""
    raise NotImplementedError(
        "Consolidation requires sequence file manipulation, which may never "
        "be in the scope of this API")

def consolidate_options(parser):
    parser.description = 'Consolidate the XML files'
    #parser.add_argument("infile", type=validate_file,
    parser.add_argument("infile", type=str,
                        help="The XML file to consolidate")
    parser.add_argument("outfile", type=str,
                        help="The resulting XML file")
    parser.set_defaults(func=consolidateXml)
