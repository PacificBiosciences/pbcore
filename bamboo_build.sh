#!/bin/bash -ex

mkdir -p tmp
/opt/python-2.7.9/bin/python /mnt/software/v/virtualenv/13.0.1/virtualenv.py tmp/venv
source tmp/venv/bin/activate

(cd .circleci && bash installHDF5.sh)
HDF5_DIR=$PWD/.circleci/prefix pip install -r requirements.txt
HDF5_DIR=$PWD/.circleci/prefix pip install -r requirements-dev.txt
    
python setup.py install
make test
