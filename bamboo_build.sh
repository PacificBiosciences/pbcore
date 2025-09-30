#!/bin/bash
set -ex
nproc

export PATH=$PWD/build/bin:$PATH
export PYTHONUSERBASE=$PWD/build

PIP="pip --cache-dir=${bamboo_build_working_directory:-$PWD}/.pip"

rm -rf build
mkdir -p build/bin build/lib build/include build/share

python3 -m venv venv
. venv/bin/activate
$PIP install --constraint constraint.lock --index-url="https://artifactory.pacificbiosciences.com/artifactory/api/pypi/sl-pypi-local/simple" --no-compile -e repos/PacBioTestData -e '.[test]'

pytest --trace-config --collect-only

set +e
make pylint # way too many errors right now
set -e
make test

bash bamboo_wheel.sh
