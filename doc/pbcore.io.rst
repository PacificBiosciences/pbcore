io Package
==========

The ``io`` package provides a number of lightweight interfaces to
PacBio data files and other standard bioinformatics file formats.
Preferred usage is to import classes directly from the ``io`` package,
e.g.::

    from pbcore.io import CmpH5Reader



bas.h5 Format (PacBio basecalls file)
-------------------------------------

The bas.h5 file format is a container format for PacBio reads, built
on top of the HDF5 standard.

.. note::

    In contrast to GFF, for example, the `bas.h5` read coordinate
    system is 0-based and end-exclusive, i.e. the same convention as
    Python and the C++ STL.

.. autoclass:: pbcore.io.BasH5Reader
    :members:
    :undoc-members:


.. autoclass:: pbcore.io.BasH5IO.BasH5
    :members:
    :undoc-members:


cmp.h5 format (PacBio alignment file)
-------------------------------------

The cmp.h5 file format is an alignment format built on top of the HDF5
standard.  It is a simple container format for PacBio alignment records.

.. note::

    In contrast to GFF, for example, all `cmp.h5` coordinate systems
    (refererence, read) are 0-based and end-exclusive, i.e. the same
    convention as Python and the C++ STL.


.. autoclass:: pbcore.io.CmpH5Reader
    :members:
    :undoc-members:

.. autoclass:: pbcore.io.CmpH5Alignment
    :members:
    :undoc-members:


BED Format
----------

The BED format is an open standard for storing properties of genomic segments.

.. autoclass:: pbcore.io.BedRecord
    :members:
    :undoc-members:

.. autoclass:: pbcore.io.BedWriter
    :members:
    :undoc-members:


FASTA Format
------------

FASTA is a standard format for sequence data.

.. autoclass:: pbcore.io.FastaIO
    :members:
    :undoc-members:


GFF Format (Version 3)
----------------------

The GFF format is an open and flexible standard for representing genomic features.


.. autoclass:: pbcore.io.GffIO
    :members:
    :undoc-members:

PacBio reference repository access
----------------------------------

The `ReferenceRepository` is a PacBio databank for references uploaded
to the SMRTportal system.

.. autoclass:: pbcore.io.ReferenceEntry
    :members:
    :undoc-members:


VCF format
----------

VCF is a standard format for representing variant calls.

.. autoclass:: pbcore.io.VcfIO
    :members:
    :undoc-members:

Subpackages
-----------

.. toctree::

    pbcore.io.cmph5
