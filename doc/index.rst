Welcome to pbcore documentation
==================================

############
Introduction
############

The `pbcore` package provides the essential python modules for
proecessing PacBio RS (data).  The package currently contains three
major sub-packages:

    (1) ``pbcore.io``: 

         Provides various IO modules that contain data access objects
         for various sequencing related file types. Specifically, the
         io packages provides support for accessing compare H5
         (cmp.h5) and base H5 (bas.h5) files.

    (2) ``pbcore.model``:

         Provides classes for processing sequence alignments and
         analyzing the data from a compare H5 file.

    (3) ``pbcore.util``:

         Provides general utility functions.

There is also a module called ``pbcore.data`` which contains a number
of small file that can be used for testing code.

####################
Library API document
####################

    :doc:`pbcore`

    :doc:`pbcore.io`

    :doc:`pbcore.model`

    :doc:`pbcore.util`

    :doc:`pbcore.data`

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

