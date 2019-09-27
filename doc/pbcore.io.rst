pbcore.io
=========

The ``pbcore.io`` package provides a number of lightweight interfaces
to PacBio data files and other standard bioinformatics file formats.
Preferred usage is to import classes directly from the ``pbcore.io``
package.

The classes within ``pbcore.io`` adhere to a few conventions, in order
to provide a uniform API:

  - Each data file type is thought of as a container of a `Record`
    type; all `Reader` classes support streaming access by iterating on the
    reader object, and `IndexedBarReader` additionally provides
    random-access to alignments/reads.

    For example::

      from pbcore.io import *
      with IndexedBamReader(filename) as f:
        for r in f:
            process(r)

    To make scripts a bit more user friendly, a progress bar can be
    easily added using the `tqdm` third-party package::

      from pbcore.io import *
      from tqdm import tqdm
      with IndexedBamReader(filename) as f:
        for r in tqdm(f):
            process(r)

  - The constructor argument needed to instantiate `Reader` and
    `Writer` objects can be either a filename (which can be suffixed
    by ".gz" for all file types) or an open file handle.
    The reader/writer classes will do what you would expect.


BAM format
----------

The BAM format is a standard format described aligned and unaligned
reads.  PacBio uses the BAM format exclusively.
For basic functionality, one should use :class:`BamReader`;
use :class:`IndexedBamReader` API for full index operation support,
which requires the auxiliary *PacBio BAM index file* (``bam.pbi`` file).

.. autoclass:: pbcore.io.BamAlignment
    :members:
    :undoc-members:

.. autoclass:: pbcore.io.BamReader
    :members:
    :undoc-members:

.. autoclass:: pbcore.io.IndexedBamReader
    :members:
    :undoc-members:


FASTA Format
------------

FASTA is a standard format for sequence data.  We recommmend using the
`FastaTable` class, which provides random access to indexed FASTA
files (using the conventional SAMtools "fai" index).

.. autoclass:: pbcore.io.FastaTable
    :members:

.. autoclass:: pbcore.io.FastaRecord
    :members:

.. autoclass:: pbcore.io.FastaReader
    :members:

.. autoclass:: pbcore.io.FastaWriter
    :members:


FASTQ Format
------------

FASTQ is a standard format for sequence data with associated quality scores.

.. autoclass:: pbcore.io.FastqRecord
    :members:

.. autoclass:: pbcore.io.FastqReader
    :members:

.. autoclass:: pbcore.io.FastqWriter
    :members:



GFF Format (Version 3)
----------------------

The GFF format is an open and flexible standard for representing genomic features.

.. autoclass:: pbcore.io.Gff3Record
    :members:

.. autoclass:: pbcore.io.GffReader
    :members:

.. autoclass:: pbcore.io.GffWriter
    :members:
