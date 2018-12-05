#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from setuptools import setup, find_packages

import sys
import os

if sys.version_info[0:2] != (2, 7):
    print('pbcore requires Python 2.7')
    sys.exit(-1)

test_deps = [
    'coverage',
    'nose == 1.3.4',
    'pyxb == 1.2.4',
    'sphinx',
    'h5py >= 2.0.1',
    'pylint == 1.6.4',
]

setup(
    name='pbcore',
    version='1.6.6', # don't forget to update pbcore/__init__.py and doc/conf.py too
    author='Pacific Biosciences',
    author_email='devnet@pacificbiosciences.com',
    description='A Python library for reading and writing PacBio® data files',
    license='BSD-3-Clause-Clear',
    packages=find_packages(),
    include_package_data=True,
    exclude_package_data={'pbcore.data': ['Makefile']},
    entry_points={'console_scripts': ['.open = pbcore.io.opener:entryPoint']},
    install_requires=[
        'numpy >= 1.7.1',
        'pysam >= 0.15.1',
    ],
    test_requires=test_deps,
    extras_require={'test': test_deps},
)
