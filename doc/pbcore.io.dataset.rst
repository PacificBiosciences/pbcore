pbcore.io.dataset
=============================

The Python DataSet XML API is designed to be a lightweight interface for
creating, opening, manipulating and writing DataSet XML files. It provides both
a native Python API and console entry points for use in manual dataset curation
or as a resource for P_Module developers.

The API and console entry points are designed with the set operations one might
perform on the various types of data held by a DataSet XML in mind: merge,
split, write etc. While various types of DataSets can be found in XML files,
the API (and in a way the console entry point, dataset.py) has DataSet as its
base type, with various subtypes extending or replacing functionality as
needed.


Console Entry Point Usage
=============================
The following entry points are available through the main script: dataset.py::

    usage: dataset.py [-h] [-v] [--debug]
                      {create,filter,merge,split,validate,loadstats,consolidate}
                      ...

    Run dataset.py by specifying a command.

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      --debug               Turn on debug level logging

    DataSet sub-commands:
      {create,filter,merge,split,validate,loadstats,consolidate}
                            Type {command} -h for a command's options

Create::

    usage: dataset.py create [-h] [--type DSTYPE] [--novalidate] [--relative]
                             outfile infile [infile ...]

    Create an XML file from a fofn or bam

    positional arguments:
      outfile        The XML to create
      infile         The fofn or BAM file(s) to make into an XML

    optional arguments:
      -h, --help     show this help message and exit
      --type DSTYPE  The type of XML to create
      --novalidate   Don't validate the resulting XML, don't touch paths
      --relative     Make the included paths relative instead of absolute (not
                     compatible with --novalidate)

Filter::

    usage: dataset.py filter [-h] infile outfile filters [filters ...]

    Add filters to an XML file. Suggested fields: ['bcf', 'bcq', 'bcr',
    'length', 'pos', 'qend', 'qname', 'qstart', 'readstart', 'rname', 'rq',
    'tend', 'tstart', 'zm']. More expensive fields: ['accuracy', 'bc', 'movie',
    'qs']

    positional arguments:
      infile      The xml file to filter
      outfile     The resulting xml file
      filters     The values and thresholds to filter (e.g. 'rq>0.85')

    optional arguments:
      -h, --help  show this help message and exit

Union::

    usage: dataset.py union [-h] outfile infiles [infiles ...]

    Combine XML (and BAM) files

    positional arguments:
      outfile     The resulting XML file
      infiles     The XML files to merge

    optional arguments:
      -h, --help  show this help message and exit

Validate::

    usage: dataset.py validate [-h] infile

    Validate ResourceId files (XML validation only available in testing)

    positional arguments:
      infile      The XML file to validate

    optional arguments:
      -h, --help  show this help message and exit

Load PipeStats::

    usage: dataset.py loadstats [-h] [--outfile OUTFILE] infile statsfile

    Load an sts.xml file into a DataSet XML file

    positional arguments:
      infile             The XML file to modify
      statsfile          The .sts.xml file to load

    optional arguments:
      -h, --help         show this help message and exit
      --outfile OUTFILE  The XML file to output

Split::

    usage: dataset.py split [-h] [--contigs] [--chunks CHUNKS] [--subdatasets]
                            [--outdir OUTDIR]
                            infile ...

    Split the dataset

    positional arguments:
      infile           The xml file to split
      outfiles         The resulting xml files

    optional arguments:
      -h, --help       show this help message and exit
      --contigs        Split on contigs
      --chunks CHUNKS  Split contigs into <chunks> total windows
      --subdatasets    Split on subdatasets
      --outdir OUTDIR  Specify an output directory

Consolidate::

    usage: dataset.py consolidate [-h] [--numFiles NUMFILES] [--noTmp]
                                  infile datafile xmlfile

    Consolidate the XML files

    positional arguments:
      infile               The XML file to consolidate
      datafile             The resulting data file
      xmlfile              The resulting XML file

    optional arguments:
      -h, --help           show this help message and exit
      --numFiles NUMFILES  The number of data files to produce (1)
      --noTmp              Don't copy to a tmp location to ensure local disk
                           use

Usage Examples
=============================

Filter Reads (CLI version)
--------------------------

In this scenario we have one or more bam files worth of subreads, aligned or
otherwise, that we want to filter and put in a single bam file. This is
possible using the CLI with the following steps, starting with a DataSet XML
file::

    # usage: dataset.py filter <in_fn.xml> <out_fn.xml> <filters>
    dataset.py filter in_fn.subreadset.xml filtered_fn.subreadset.xml 'rq>0.85'

    # usage: dataset.py consolidate <in_fn.xml> <out_data_fn.bam> <out_fn.xml>
    dataset.py consolidate filtered_fn.subreadset.xml consolidate.subreads.bam out_fn.subreadset.xml

The filtered DataSet and the consolidated DataSet should be read for read
equivalent when used with SMRT Analysis software.

Filter Reads (API version)
--------------------------

The API version of filtering allows for more advanced filtering criteria::

    ss = SubreadSet('in_fn.subreadset.xml')
    ss.filters.addRequirement(rname=[('=', 'E.faecalis.2'),
                                     ('=', 'E.faecalis.2')],
                              tStart=[('<', '99'),
                                      ('<', '299')],
                              tEnd=[('>', '0'),
                                    ('>', '200')])

Produces the following conditions for a read to be considered passing:

(rname = E.faecalis.2 AND tstart < 99 AND tend > 0)
OR
(rname = E.faecalis.2 AND tstart < 299 AND tend > 200)

You can add sets of filters by providing equal length lists of requirements for
each filter.

Additional requirements added singly will be added to all filters::

    ss.filters.addRequirement(rq=[('>', '0.85')]) 

(rname = E.faecalis.2 AND tstart < 99 AND tend > 0 AND rq > 0.85)
OR
(rname = E.faecalis.2 AND tstart < 299 AND tend > 100 AND rq > 0.85)

Additional requirements added with a plurality of options will duplicate the
previous requiremnts for each option::

    ss.filters.addRequirement(length=[('>', 500), ('>', 1000)])

(rname = E.faecalis.2 AND tstart < 99 AND tend > 0 AND rq > 0.85 AND length > 500)
OR
(rname = E.faecalis.2 AND tstart < 299 AND tend > 100 AND rq > 0.85 AND length > 500)
OR
(rname = E.faecalis.2 AND tstart < 99 AND tend > 0 AND rq > 0.85 AND length > 1000)
OR
(rname = E.faecalis.2 AND tstart < 299 AND tend > 100 AND rq > 0.85 AND length > 1000)

Of course you can always wipe the filters and start over::

    ss.filters = None

Consolidation is more similar to the CLI version::

    ss.consolidate('cons.bam')
    ss.write('cons.xml')

Resequencing Pipeline (CLI version)
-----------------------------------

In this scenario, we have two movies worth of subreads in two SubreadSets that
we want to align to a reference, merge together, split into DataSet chunks by
contig, then send through quiver on a chunkwise basis (in parallel).

1. Align each movie to the reference, producing a dataset with one bam file for
   each execution::

    pbalign movie1.subreadset.xml referenceset.xml movie1.alignmentset.xml
    pbalign movie2.subreadset.xml referenceset.xml movie2.alignmentset.xml

2. Merge the files into a FOFN-like dataset (bams aren't touched)::

    # dataset.py merge <out_fn> <in_fn> [<in_fn> <in_fn> ...]
    dataset.py merge merged.alignmentset.xml movie1.alignmentset.xml movie2.alignmentset.xml

3. Split the dataset into chunks by contig (rname) (bams aren't touched). Note
   that supplying output files splits the dataset into that many output files
   (up to the number of contigs), with multiple contigs per file. Not supplying
   output files splits the dataset into one output file per contig, named
   automatically. Specifying a number of chunks instead will produce that many
   files, with contig or even sub contig (reference window) splitting.::

    dataset.py split --contigs --chunks 8 merged.alignmentset.xml

4. Quiver then consumes these chunks::

    variantCaller.py --alignmentSetRefWindows --referenceFileName referenceset.xml --outputFilename chunk1consensus.fasta --algorithm quiver chunk1contigs.alignmentset.xml
    variantCaller.py --alignmentSetRefWindows --referenceFileName referenceset.xml --outputFilename chunk2consensus.fasta --algorithm quiver chunk2contigs.alignmentset.xml

The chunking works by duplicating the original merged dataset (no bam
duplication) and adding filters to each duplicate such that only reads
belonging to the appropriate contigs are emitted. The contigs are distributed
amongst the output files in such a way that the total number of records per
chunk is about even.

Tangential Information
~~~~~~~~~~~~~~~~~~~~~~

DataSet.refNames (which returns a list of reference names available in the
dataset) is also subject to the filtering imposed during the split. Therefore
you wont be running through superfluous (and apparently unsampled) contigs to
get the reads in this chunk. The DataSet.records generator is also subject to
filtering, but not as efficiently as readsInRange. If you do not have a
reference window, readsInReference() is also an option.

As the bam files are never touched, each dataset contains all the information
necessary to access all reads for all contigs. Doing so on these filtered
datasets would require disabling the filters first::

    dset.disableFilters()

Or removing the specific filter giving you problems::

    dset.filters.removeRequirement('rname')

Resequencing Pipeline (API version)
-----------------------------------

In this scenario, we have two movies worth of subreads in two SubreadSets that
we want to align to a reference, merge together, split into DataSet chunks by
contig, then send through quiver on a chunkwise basis (in parallel). We want to
do them using the API, rather than the CLI.

1. Align each movie to the reference, producing a dataset with one bam file for
   each execution

   .. code-block:: python

    # CLI (or see pbalign API):
    pbalign movie1.subreadset.xml referenceset.xml movie1.alignmentset.xml
    pbalign movie2.subreadset.xml referenceset.xml movie2.alignmentset.xml

2. Merge the files into a FOFN-like dataset (bams aren't touched)

   .. code-block:: python

    # API, filename_list is dummy data:
    filename_list = ['movie1.alignmentset.xml', 'movie2.alignmentset.xml']

    # open:
    dsets = [AlignmentSet(fn) for fn in filename_list]
    # merge with + operator:
    dset = reduce(lambda x, y: x + y, dsets)

    # OR:
    dset = AlignmentSet(*filename_list)

3. Split the dataset into chunks by contigs (or subcontig windows)

   .. code-block:: python

    # split:
    dsets = dset.split(contigs=True, chunks=8)

4. Quiver then consumes these chunks

   .. code-block:: python

    # write out if you need to (or pass directly to quiver API):
    outfilename_list = ['chunk1contigs.alignmentset.xml', 'chunk2contigs.alignmentset.xml']
    # write with 'write' method:
    map(lambda (ds, nm): ds.write(nm), zip(dsets, outfilename_list))

    # CLI (or see quiver API):
    variantCaller.py --alignmentSetRefWindows --referenceFileName referenceset.xml --outputFilename chunk1consensus.fasta --algorithm quiver chunk1contigs.alignmentset.xml
    variantCaller.py --alignmentSetRefWindows --referenceFileName referenceset.xml --outputFilename chunk2consensus.fasta --algorithm quiver chunk2contigs.alignmentset.xml

    # Inside quiver (still using python dataset API):
    aln = AlignmentSet(fname)
    # get this set's windows:
    refWindows = aln.refWindows
    # gather the reads for these windows using readsInRange, e.g.:
    reads = list(itertools.chain(aln.readsInRange(rId, start, end) for rId, start, end in refWindows))

API overview
=============================

The chunking works by duplicating the original merged dataset (no bam
duplication) and adding filters to each duplicate such that only reads
belonging to the appropriate contigs/windows are emitted. The contigs are
distributed amongst the output files in such a way that the total number of
records per chunk is about even.

DataSets can be created using the appropriate constructor (SubreadSet), or with
the common constructor (DataSet) and later cast to a specific type
(copy(asType="SubreadSet")). The DataSet constructor acts as a factory function
(an artifact of early api Designs). The factory behavior is defined in the
DataSet metaclass.

.. inheritance-diagram:: pbcore.io.dataset.DataSetIO
    :parts: 1

.. automodule:: pbcore.io.dataset.DataSetIO
    :members:
    :special-members: __call__, __init__, __metaclass__, __repr__, __add__,
                      __eq__, __deepcopy__
    :show-inheritance:

The operations possible between DataSets of the same and different types are
limited, see the DataSet XML documentation for details.

DataSet XML files have a few major components: XML metadata,
ExternalReferences, Filters, DataSet Metadata, etc. These are represented in
different ways internally, depending on their complexity. DataSet metadata
especially contains a large number of different potential elements, many of
which are accessible in the API as nested attributes. To preserve the API's
ability to grant access to any DataSet Metadata available now and in the
future, as well as to maintain the performance of dataset reading and writing,
each DataSet stores its metadata in what approximates a tree structure, with
various helper classes and functions manipulating this tree. The structure of
this tree and currently implemented helper classes are available in the
DataSetMembers module.

.. inheritance-diagram:: pbcore.io.dataset.DataSetMembers
    :parts: 1

.. automodule:: pbcore.io.dataset.DataSetMembers
    :members:
    :special-members: __getitem__, __iter__, __repr__
    :show-inheritance:
    :undoc-members:

