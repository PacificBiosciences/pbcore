__all__ = ["openAlignmentFile",
           "openIndexedAlignmentFile",
           "entryPoint"]

from pbcore.io import (IndexedFastaReader, FastaReader,
                       BamReader, IndexedBamReader,
                       GffReader, FastqReader,
                       PacBioBamIndex, openDataSet)


def raise_no_h5():
    raise NotImplementedError("hdf5 file support has been removed")


def openIndexedAlignmentFile(fname, referenceFastaFname=None, sharedIndex=None):
    """
    Factory function to get a handle to a reader for an alignment file (BAM),
    requires bam.pbi index

    The reference FASTA, if provided, must have a FASTA index
    (fasta.fai).
    """
    if fname.endswith(".h5"):
        raise_no_h5()
    elif fname.endswith("bam"):
        return IndexedBamReader(fname, referenceFastaFname=referenceFastaFname, sharedIndex=sharedIndex)
    else:
        raise ValueError("Invalid alignment file suffix")


def openAlignmentFile(fname, referenceFastaFname=None, sharedIndex=None):
    """
    Factory function to get a handle to a reader for an alignment file (BAM),
    not requiring index capability
    """
    if fname.endswith("cmp.h5"):
        raise_no_h5()
    elif fname.endswith("bam"):
        return BamReader(fname, referenceFastaFname)


def _openersFor(ext):
    if ext == "gff":
        return (GffReader,)
    elif ext in ("fq", "fastq"):
        return (FastqReader,)
    elif ext in ("fa", "fasta"):
        return (IndexedFastaReader, FastaReader)
    elif ext == "cmp.h5":
        raise_no_h5()
    elif ext == "bas.h5":
        raise_no_h5()
    elif ext == "bax.h5":
        raise_no_h5()
    elif ext == "fofn":
        raise_no_h5()
    elif ext == "bam":
        return (IndexedBamReader, BamReader)
    elif ext == "pbi":
        return (PacBioBamIndex,)
    elif ext == "xml":
        return (openDataSet,)
    else:
        raise ValueError("No known opener class for extension %s" % ext)


def _extension(fname):
    parts = fname.split(".")
    if parts[-1] == "h5":
        raise_no_h5()
    else:
        return parts[-1]


def _openAny(fname, *extraArgs):
    ext = _extension(fname)
    openers = _openersFor(ext)
    lastException = None
    for opener in openers:
        try:
            f = opener(fname, *extraArgs)
            return f
        except IOError as e:
            lastException = e
    else:
        assert lastException is not None
        raise lastException  # pylint: disable=raising-bad-type


def entryPoint():
    """
    This entry point (callable from the command line as ".open")
    provides a convenient way to load up a data file for inspection.
    """
    import sys
    import code
    import numpy as np

    if len(sys.argv) < 2:
        print("Requires at least one argument!")
        return 1

    fname = sys.argv[1]
    extraArgs = sys.argv[2:]

    f = _openAny(fname, *extraArgs)
    banner = "Your file has been opened as object 'f'"
    try:
        from IPython import embed
        embed(banner1=banner)
    except ImportError:
        code.InteractiveConsole(locals=locals()).interact(banner=banner)
