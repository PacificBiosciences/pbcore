* Version 0.9.1 (SMRTanalysis 2.3.0p1)
- FASTA header parsing into "id" and "metadata" now available in the
  FastaRecord types

* Version 0.9.0 (SMRTanalysis 2.3.0)
- pbcore.chemistry: a new subpackage for decoding barcode information
  to the human-readable chemistry name
- BasH5Reader: more robust handling of broken region tables
- CmpH5Reader: loading an empty cmp.h5 will raise an EmptyCmpH5Error.
  This is because the semantics of an empty cmp.h5 were never defined,
  and for example it is not defined whether or not a cmp.h5 lacking a
  movie table is compliant.
