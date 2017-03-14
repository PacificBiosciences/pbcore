#!/bin/bash -ex

source /mnt/software/Modules/current/init/bash
mkdir -p tmp
/opt/python-2.7.9/bin/python /mnt/software/v/virtualenv/13.0.1/virtualenv.py tmp/venv
PIP_CACHE=$PWD/.pip_cache
find $PIP_CACHE -name '*-linux_x86_64.whl' -delete || true

source tmp/venv/bin/activate

rsync -avx /mnt/software/a/anaconda2/4.2.0/pkgs/mkl-11.3.3-0/lib/             tmp/venv/lib/
rsync -avx /mnt/software/a/anaconda2/4.2.0/pkgs/numpy-1.11.1-py27_0/bin/      tmp/venv/bin/
rsync -avx /mnt/software/a/anaconda2/4.2.0/pkgs/numpy-1.11.1-py27_0/lib/      tmp/venv/lib/

module load hdf5-tools/1.8.11
export HDF5_DIR=/mnt/software/h/hdf5-tools/1.8.11
HDF5_DIR=$PWD/.circleci/prefix pip install --cache-dir=$PIP_CACHE -r requirements.txt
HDF5_DIR=$PWD/.circleci/prefix pip install --cache-dir=$PIP_CACHE -r requirements-dev.txt
    
python setup.py install
make test
