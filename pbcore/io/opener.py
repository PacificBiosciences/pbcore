#################################################################################
# Copyright (c) 2011-2015, Pacific Biosciences of California, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Pacific Biosciences nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE.  THIS SOFTWARE IS PROVIDED BY PACIFIC BIOSCIENCES AND ITS
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR
# ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#################################################################################


__all__ = [ "openAlignmentFile",
            "openIndexedAlignmentFile",
            "entryPoint" ]

from pbcore.io import (IndexedFastaReader, FastaReader,
                       BaxH5Reader, BasH5Reader, BasH5Collection,
                       CmpH5Reader, BamReader, IndexedBamReader,
                       GffReader, FastqReader,
                       PacBioBamIndex, openDataSet)

def openIndexedAlignmentFile(fname, referenceFastaFname=None, sharedIndex=None):
    """
    Factory function to get a handle to a reader for an alignment file
    (cmp.h5 or BAM), requiring index capability (built-in for cmp.h5;
    requires bam.pbi index for BAM

    The reference FASTA, if provided, must have a FASTA index
    (fasta.fai).
    """
    if fname.endswith("cmp.h5"):
        return CmpH5Reader(fname, sharedIndex=sharedIndex)
    elif fname.endswith("bam"):
        return IndexedBamReader(fname, referenceFastaFname=referenceFastaFname, sharedIndex=sharedIndex)
    else:
        raise ValueError, "Invalid alignment file suffix"

def openAlignmentFile(fname, referenceFastaFname=None, sharedIndex=None):
    """
    Factory function to get a handle to a reader for an alignment file
    (cmp.h5 or BAM), not requiring index capability

    (A `sharedIndex` can still be passed for opening a cmp.h5, for which
    the index is compulsory.)
    """
    if fname.endswith("cmp.h5"):
        return CmpH5Reader(fname, sharedIndex=sharedIndex)
    elif fname.endswith("bam"):
        return BamReader(fname, referenceFastaFname)

def _openersFor(ext):
    if   ext == "gff":           return (GffReader,)
    elif ext in ("fq", "fastq"): return (FastqReader,)
    elif ext in ("fa", "fasta"): return (IndexedFastaReader, FastaReader)
    elif ext == "cmp.h5":        return (CmpH5Reader,)
    elif ext == "bas.h5":        return (BasH5Reader,)
    elif ext == "bax.h5":        return (BaxH5Reader,)
    elif ext == "fofn":          return (BasH5Collection,)
    elif ext == "bam":           return (IndexedBamReader, BamReader)
    elif ext == "pbi":           return (PacBioBamIndex,)
    elif ext == "xml":           return (openDataSet,)
    else:
        raise ValueError, ("No known opener class for extension %s" % ext)

def _extension(fname):
    parts = fname.split(".")
    if parts[-1] == "h5":
        return ".".join(parts[-2:])
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
        raise lastException

def entryPoint():
    """
    This entry point (callable from the command line as ".open")
    provides a convenient way to load up a data file for inspection.
    """
    import sys, code, numpy as np

    if len(sys.argv) < 2:
        print "Requires at least one argument!"
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
