from __future__ import absolute_import, division, print_function

import pbcore.io.dataset.run_split as M
import glob
import os
import pytest


@pytest.fixture(scope="module")
def script_loc(request):
    '''Return the directory of the currently running test script'''

    # uses .join instead of .dirname so we get a LocalPath object instead of
    # a string. LocalPath.join calls normpath for us when joining the path
    return request.fspath.join('..')


@pytest.mark.internal_data
def test(tmpdir, script_loc):
    tmpdir.chdir()
    dset = script_loc.join('data/test_dataset_run_split/filt.xml')
    prefix = 'myprefix'
    M.run_split_dataset(dset, prefix)
    globbed_fns = glob.glob('myprefix.*.subreadset.xml')
    assert len(globbed_fns) == 1
    fns = [os.path.basename(fn.rstrip())
           for fn in open('myprefix.fofn').readlines()]
    assert globbed_fns == fns
