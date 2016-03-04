pbcore.io
=========

The ``pbcore.io`` package provides a number of lightweight interfaces
to PacBio data files and other standard bioinformatics file formats.
Preferred usage is to import classes directly from the ``pbcore.io``
package, e.g.::

    >>> from pbcore.io import CmpH5Reader

The classes within ``pbcore.io`` adhere to a few conventions, in order
to provide a uniform API:

  - Each data file type is thought of as a container of a `Record`
    type; all `Reader` classes support streaming access by iterating on the 
    reader object, and
    `CmpH5Reader`, `BasH5Reader` and `IndexedBarReader` additionally 
    provide random-access
    to alignments/reads.
    
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
    by ".gz" for all but the h5 file types) or an open file handle.
    The reader/writer classes will do what you would expect.


  - The reader/writer classes all support the context manager idiom.
    Meaning, if you write::

      >>> with CmpH5Reader("aligned_reads.cmp.h5") as r:
      ...   print r[0].read()

    the `CmpH5Reader` object will be automatically closed after the
    block within the "with" statement is executed.

BAM/cmp.h5 compatibility: quick start
-------------------------------------

If you have an application that uses the `CmpH5Reader` and you want to
start using BAM files, your best bet is to use the following generic
factory functions:

.. autofunction:: pbcore.io.openIndexedAlignmentFile

.. autofunction:: pbcore.io.openAlignmentFile

.. note::

   Since BAM files contain a subset of the information that was
   present in cmp.h5 files, you will need to provide these functions
   an indexed FASTA file for your reference.  For *full*
   compatibility, you need the `openIndexedAlignmentFile` function,
   which requires the existence of a `bam.pbi` file (PacBio BAM index
   companion file).




`bas.h5` / `bax.h5` Formats (PacBio basecalls file)
---------------------------------------------------

The `bas.h5`/ `bax.h5` file formats are container formats for PacBio
reads, built on top of the HDF5 standard.  Originally there was just
one `bas.h5`, but eventually "multistreaming" came along and we had to
split the file into three `bax.h5` *parts* and one `bas.h5` file
containing pointers to the *parts*.  Use ``BasH5Reader`` to read any
kind of `bas.h5` file, and ``BaxH5Reader`` to read a `bax.h5`.

.. note::

    In contrast to GFF, for example, the `bas.h5` read coordinate
    system is 0-based and start-inclusive/end-exclusive, i.e. the same
    convention as Python and the C++ STL.

.. autoclass:: pbcore.io.BasH5Reader
    :members:
    :undoc-members:

.. autoclass:: pbcore.io.BasH5IO.Zmw
    :members:
    :undoc-members:

.. autoclass:: pbcore.io.BasH5IO.ZmwRead
    :members:
    :undoc-members:


BAM format
----------

The BAM format is a standard format described aligned and unaligned
reads.  PacBio is transitioning from the cmp.h5 format to the BAM
format.  For basic functionality, one should use :class:`BamReader`;
for full compatibility with the :class:`CmpH5Reader` API (including
alignment index functionality) one should use
:class:`IndexedBamReader`, which requires the auxiliary *PacBio BAM
index file* (``bam.pbi`` file).

.. autoclass:: pbcore.io.BamAlignment
    :members:
    :undoc-members:

.. autoclass:: pbcore.io.BamReader
    :members:
    :undoc-members:

.. autoclass:: pbcore.io.IndexedBamReader
    :members:
    :undoc-members:



`cmp.h5` format (legacy PacBio alignment file)
----------------------------------------------

The `cmp.h5` file format is an alignment format built on top of the HDF5
standard.  It is a simple container format for PacBio alignment records.

.. note::

    In contrast to GFF, for example, all `cmp.h5` coordinate systems
    (refererence, read) are 0-based and start-inclusive/end-exclusive,
    i.e. the same convention as Python and the C++ STL.


.. autoclass:: pbcore.io.CmpH5Reader
    :members:
    :undoc-members:

.. autoclass:: pbcore.io.CmpH5Alignment
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
