#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, Extension, find_packages
import sys

if ("install" in sys.argv) and sys.version_info < (2, 7, 0):
    print "pbcore requires Python 2.7"
    sys.exit(-1)

globals = {}
execfile("pbcore/__init__.py", globals)
__VERSION__ = globals["__VERSION__"]

setup(
    name = 'pbcore',
    version=__VERSION__,
    author='Pacific Biosciences',
    author_email='devnet@pacificbiosciences.com',
    description="A Python library for reading and writing PacBio® data files",
    license=open('LICENSES.txt').read(),
    packages = find_packages('.'),
    package_dir = {'':'.'},
    package_data = {'pbcore': ['data/*.h5', 'data/*.gff', 'data/*.fasta',
                               'data/*.fasta.fai', 'data/*.fofn', 'data/*.m4',
                               'data/*.fa', 'data/*.fa.fai',
                               'data/*.m5', 'data/*.bam', 'data/*.bam.bai', "data/*.bam.pbi",
                               'chemistry/resources/*.xml',
                               'data/datasets/*.*',
                               'data/datasets/yieldtest/*.*']
                               },
    zip_safe = False,
    entry_points = { "console_scripts" : [ ".open = pbcore.io.opener:entryPoint" ] },
    scripts=['bin/dataset.py'],
    install_requires=[
        'h5py >= 2.0.1',
        'numpy >= 1.7.1',
        'pysam >= 0.8.4'
    ])
