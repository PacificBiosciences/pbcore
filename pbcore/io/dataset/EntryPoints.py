#/usr/bin/env python

import os
import argparse
from collections import defaultdict
from pbcore.io import DataSet, ContigSet, openDataSet
from pbcore.io.dataset.DataSetValidator import validateFile
import logging

log = logging.getLogger(__name__)

def summarizeXml(args):
    dset = openDataSet(args.infile, strict=args.strict)
    for fname in dset.toExternalFiles():
        print fname
    print "Number of records: {r}".format(r=dset.numRecords)
    print "Total number of bases: {r}".format(r=dset.totalLength)

def summarize_options(parser):
    parser.description = "Summarize a DataSet XML file"
    parser.add_argument("infile", type=str,
                        help="The xml file to summarize")
    parser.set_defaults(func=summarizeXml)

def createXml(args):
    dsTypes = DataSet.castableTypes()
    dset = dsTypes[args.dsType](*args.infile, strict=args.strict,
                                skipCounts=args.skipCounts)
    log.debug("Dataset created")
    dset.write(args.outfile, validate=args.novalidate, modPaths=True,
               relPaths=args.relative)
    log.debug("Dataset written")


def create_options(parser):
    parser.description = ('Create an XML file from a fofn or bam. Possible '
                          'types: SubreadSet, AlignmentSet, ReferenceSet, '
                          'HdfSubreadSet, BarcodeSet, ConsensusAlignmentSet, '
                          'ConsensusReadSet, ContigSet')
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
    if args.infile.endswith('xml'):
        dataSet = openDataSet(args.infile, strict=args.strict)
        filters = defaultdict(list)
        separators = ['<=', '>=', '!=', '==', '>', '<', '=']
        for filt in args.filters:
            for sep in separators:
                if sep in filt:
                    param, condition = filt.split(sep)
                    condition = (sep, condition)
                    filters[param].append(condition)
                    break
        dataSet.filters.addRequirement(**filters)
        dataSet.updateCounts()
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
    dataSet = openDataSet(args.infile, strict=args.strict)
    chunks = len(args.outfiles)
    if args.chunks:
        chunks = args.chunks
    dss = dataSet.split(chunks=chunks,
                        ignoreSubDatasets=(not args.subdatasets),
                        contigs=args.contigs,
                        maxChunks=args.maxChunks,
                        breakContigs=args.breakContigs,
                        targetSize=args.targetSize,
                        zmws=args.zmws,
                        barcodes=args.barcodes,
                        byRecords=(not args.byRefLength),
                        updateCounts=(not args.noCounts))
    log.debug("Splitting into {i} chunks".format(i=len(dss)))
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
            num = len(dss)
            end = ''
            if num > 5:
                num = 5
                end = '...'
            log.debug("Emitting {f} {e}".format(
                f=', '.join(args.outfiles[:num]),
                e=end))
    log.debug("Finished splitting, now writing")
    for out_fn, dset in zip(args.outfiles, dss):
        dset.write(out_fn)
    log.debug("Done writing files")

def split_options(parser):
    parser.description = "Split the dataset"
    parser.add_argument("infile", type=str,
                        help="The xml file to split")
    parser.add_argument("--contigs", default=False, action='store_true',
                        help="Split on contigs")
    parser.add_argument("--barcodes", default=False, action='store_true',
                        help="Split on barcodes")
    parser.add_argument("--zmws", default=False, action='store_true',
                        help="Split on zmws")
    parser.add_argument("--byRefLength", default=False, action='store_true',
                        help="Split contigs by contig length")
    parser.add_argument("--noCounts", default=False, action='store_true',
                        help="Update dataset counts after split")
    parser.add_argument("--chunks", default=0, type=int,
                        help="Split contigs into <chunks> total windows")
    parser.add_argument("--maxChunks", default=0, type=int,
                        help="Split contig list into at most <chunks> groups")
    parser.add_argument("--targetSize", default=5000, type=int,
                        help="Target number of records per chunk")
    parser.add_argument("--breakContigs", default=False, action='store_true',
                        help="Break contigs to get closer to maxCounts")
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
        dss.append(openDataSet(infn, strict=args.strict))
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
    dset = openDataSet(args.infile, strict=args.strict)
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
    dset = openDataSet(args.infile)
    dset.consolidate(args.datafile, numFiles=args.numFiles)
    dset.write(args.xmlfile)

def consolidate_options(parser):
    parser.description = 'Consolidate the XML files'
    #parser.add_argument("infile", type=validate_file,
    parser.add_argument("--numFiles", type=int, default=1,
                        help="The number of data files to produce (1)")
    parser.add_argument("infile", type=str,
                        help="The XML file to consolidate")
    parser.add_argument("datafile", type=str,
                        help="The resulting data file")
    parser.add_argument("xmlfile", type=str,
                        help="The resulting XML file")
    parser.set_defaults(func=consolidateXml)
