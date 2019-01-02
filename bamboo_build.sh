#!/bin/bash
type module >& /dev/null || . /mnt/software/Modules/current/init/bash
module load python/2
set -ex
nproc

export PATH=$PWD/build/bin:$PATH
export PYTHONUSERBASE=$PWD/build

PIP="pip --cache-dir=${bamboo_build_working_directory:-$PWD}/.pip"
if [[ -z ${bamboo_repository_branch_name+x} ]]; then
  WHEELHOUSE=/mnt/software/p/python/wheelhouse/develop
elif [[ ${bamboo_repository_branch_name} == develop ]]; then
  WHEELHOUSE=/mnt/software/p/python/wheelhouse/develop
elif [[ ${bamboo_repository_branch_name} == master ]]; then
  WHEELHOUSE=/mnt/software/p/python/wheelhouse/master
else
  WHEELHOUSE=/mnt/software/p/python/wheelhouse/develop
fi

rm -rf   build
mkdir -p build/bin build/lib build/include build/share
$PIP install --user --no-index --find-link $WHEELHOUSE --no-compile -e .[test]
$PIP install --user --no-index --find-link $WHEELHOUSE pbtestdata
$PIP install --user --no-index --find-link $WHEELHOUSE pytest-xdist
$PIP install --user --no-index --find-link $WHEELHOUSE pytest-cov
#$PIP install --user --no-index --find-link $WHEELHOUSE pytest-parallel # not sure why this fails
pytest --trace-config

set +e
make pylint # way too many errors right now
set -e
make test
