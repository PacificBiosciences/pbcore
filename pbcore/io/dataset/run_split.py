"""A simple script to scatter a (filtered) subreadset into units of input files.

This was copied almost verbatim from the falcon3 repo, "falcon_kit/util/dataset_split.py".
Since pbcore is not python3-ready, we need to store this in a python2 repo.
In order to avoid extra work with mobs, we will call this via

    python2 -m pbcore.io.dataset.run_split -h
"""

from pbcore.io import (SubreadSet, ExternalResource) # pylint: disable=import-error
import argparse
import logging
import os
import sys
import copy

log = logging.getLogger(__name__)

def split_dataset(subreadset, out_prefix):
    """
    Takes an input dataset, and for each entry generates one separate dataset
    file, while maintaining all the filters.
    Returns a list of the generated datasets.

    To create an example filtered dataset for testing:
    dataset create --type SubreadSet test.subreadset.xml subreads1.bam subreads2.bam
    dataset filter test.subreadset.xml test.filtered.subreadset.xml 'length>1000'
    """
    out_prefix_abs = os.path.abspath(out_prefix)

    dset = SubreadSet(subreadset, strict=True, skipCounts=True)
    fns = dset.toFofn()

    log.info('resources in {!r}:\n{}'.format(subreadset, '\n'.join(fns)))

    split_fns = []
    for i, bam_fn in enumerate(fns):
        out_fn = '{}.{:05}.subreadset.xml'.format(out_prefix_abs, i)
        new_dataset = SubreadSet(bam_fn, skipCounts=True)
        new_dataset.newUuid()
        new_dataset._filters = copy.deepcopy(dset._filters)
        new_dataset.write(out_fn)
        split_fns.append(out_fn)

    return split_fns

def run_split_dataset(subreadset, out_prefix):
    out_prefix_abs = os.path.abspath(out_prefix)

    split_fns = split_dataset(subreadset, out_prefix_abs)

    out_fofn_fn = '{}.fofn'.format(out_prefix_abs)
    with open(out_fofn_fn, 'w') as ofs:
        for fn in split_fns:
            ofs.write('{}\n'.format(fn))

    log.info('Wrote {} chunks into "{}"'.format(len(split_fns), out_fofn_fn))

def main(argv=sys.argv):
    description = """Scatter subreadsets from one input subreadset.
"""
    epilog = """The results are 'uncounted', which is fast; TotalLength and NumRecords
are not calculated. We split only on bam-files, which is very fast since we do not
need to read the bam-files at all. The number of "chunks" is the number of bam-files.
"""
    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('subreadset',
        help='Input subreadset XML filename. Can be filtered.')
    parser.add_argument('out_prefix',
        help='Prefix of the output sub-datasets "{output_prefix}.?????.subreadset.xml, plus "{output_prefix}.fofn".')
    args = parser.parse_args(argv[1:])

    run_split_dataset(args.subreadset, args.out_prefix)

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    main(sys.argv)
