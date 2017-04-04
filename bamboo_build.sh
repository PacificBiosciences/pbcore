#!/bin/bash -ex

NX3PBASEURL=http://nexus.pacificbiosciences.com/repository/maven-thirdparty/gcc-4.9.2
export PATH=$PWD/build/bin:/mnt/software/a/anaconda2/4.2.0/bin:$PATH
export PYTHONUSERBASE=$PWD/build
export CFLAGS="-I/mnt/software/a/anaconda2/4.2.0/include"
PIP="pip --cache-dir=$bamboo_build_working_directory/.pip"
type module >& /dev/null || . /mnt/software/Modules/current/init/bash
module load gcc/4.9.2

rm -rf   build
mkdir -p build/bin build/lib build/include build/share
$PIP install --user \
  $NX3PBASEURL/pythonpkgs/pysam-0.9.1.4-cp27-cp27mu-linux_x86_64.whl
$PIP install --user -r requirements.txt
$PIP install --user -r requirements-dev.txt
$PIP install --user -e ./    

make test
