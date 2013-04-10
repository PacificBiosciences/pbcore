pbcore.io
=========

The ``pbcore.io`` package provides a number of lightweight interfaces
to PacBio data files and other standard bioinformatics file formats.
Preferred usage is to import classes directly from the ``pbcore.io``
package, e.g.::

    from pbcore.io import CmpH5Reader

The classes within ``pbcore.io`` adhere to a few conventions, in order
to provide a uniform API:

  - Each data file type is thought of as a container of a `Record`
    type; all `Reader` classes support streaming access, and
    `CmpH5Reader` and `BasH5Reader` additionally provide random-access
    to alignments/reads.

  - The constructor argument needed to instantiate `Reader` and
    `Writer` objects can be either a filename (which can be suffixed
    by ".gz" for all but the h5 file types) or an open file handle.
    The reader/writer classes will do what you would expect.


  - The reader/writer classes all support the context manager idiom.
    Meaning, if you write::

      with CmpH5Reader("aligned_reads.cmp.h5") as r:
          print r[0].read()

    the `CmpH5Reader` object will be automatically closed after the
    block within the "with" statement is executed.



`bas.h5` Format (PacBio basecalls file)
---------------------------------------

The `bas.h5` file format is a container format for PacBio reads, built
on top of the HDF5 standard.

.. note::

    In contrast to GFF, for example, the `bas.h5` read coordinate
    system is 0-based and start-inclusive/end-exclusive, i.e. the same
    convention as Python and the C++ STL.

.. autoclass:: pbcore.io.BasH5Reader
    :members:
    :undoc-members:

.. autoclass:: pbcore.io.BasH5Reader.Zmw
    :members:
    :undoc-members:

.. autoclass:: pbcore.io.BasH5Reader.ZmwRead
    :members:
    :undoc-members:


`cmp.h5` format (PacBio alignment file)
---------------------------------------

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

FASTA is a standard format for sequence data.

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
