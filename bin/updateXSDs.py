#!/usr/bin/env python

import argparse
import tempfile
import shutil
import os
import glob
import subprocess
import shlex


def get_files(xsd_dir):
    files = []
    for path, subdirs, fns in os.walk(xsd_dir):
        for fn in fns:
            if fn.endswith('xsd'):
                files.append(os.path.join(path, fn))
    return files

def copy_xsds(xsd, dest):
    """Go ahead and copy all xsds, there will likely be many dependencies. If
    not, xsds are small"""
    files = get_files(os.path.dirname(xsd))
    for fn in files:
        shutil.copy(fn, dest)

def generate_pyxb(xsd, module):
    cmd = "pyxbgen -u {x} -m {m}".format(x=xsd, m=module)
    print cmd
    subprocess.call(shlex.split(cmd))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("xsd", type=str,
                        help="the XSD of interest")
    parser.add_argument("--mod_dest", type=str,
                        help=("the path to (and name of) the python module to "
                              "be generated"),
                        default='.')
    args = parser.parse_args()
    tempd = tempfile.mkdtemp(suffix='xsds')
    copy_xsds(args.xsd, tempd)
    xsd_name = os.path.basename(args.xsd)
    generate_pyxb(os.path.join(tempd, xsd_name), args.mod_dest)
    shutil.rmtree(tempd)

