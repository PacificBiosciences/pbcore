#!/bin/bash
type module >& /dev/null || . /mnt/software/Modules/current/init/bash
set -ex

NX3PBASEURL=http://nexus/repository/unsupported/pitchfork/gcc-6.4.0
export PATH=$PWD/build/bin:/mnt/software/a/anaconda2/4.2.0/bin:$PATH
export PYTHONUSERBASE=$PWD/build
export CFLAGS="-I/mnt/software/a/anaconda2/4.2.0/include"
PIP="pip --cache-dir=$bamboo_build_working_directory/.pip"
module load gcc/6.4.0

rm -rf   build
mkdir -p build/bin build/lib build/include build/share
$PIP install --user \
  $NX3PBASEURL/pythonpkgs/pysam-0.13-cp27-cp27mu-linux_x86_64.whl
$PIP install --user -r requirements.txt
$PIP install --user -r requirements-dev.txt
$PIP install --user -e ./    

set +e
make pylint # way too many errors right now
set -e
make test
