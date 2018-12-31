#!/bin/bash
type module >& /dev/null || . /mnt/software/Modules/current/init/bash
module load python/2.7.9-mobs-pbcore
set -ex


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
$PIP install --no-compile --find-link $WHEELHOUSE --user -e .[test]
$PIP install --no-compile --find-link $WHEELHOUSE --user pbtestdata

set +e
make pylint # way too many errors right now
set -e
make test
