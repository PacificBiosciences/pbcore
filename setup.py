#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

test_deps = [
    'coverage',
    'pbtestdata',
    'pylint',
    'pytest',
    'pytest-cov',
    'pytest-xdist',
    'pyxb == 1.2.6',
    'sphinx',
]

setup(
    name='pbcore',
    version='2.0.5',
    author='Pacific Biosciences',
    author_email='devnet@pacificbiosciences.com',
    description='A Python library for reading and writing PacBio® data files',
    license='BSD-3-Clause-Clear',
    packages=find_packages(),
    include_package_data=True,
    exclude_package_data={'pbcore.data': ['Makefile']},
    zip_safe=False,
    entry_points={'console_scripts': ['.open = pbcore.io.opener:entryPoint']},
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
        'biopython >= 1.74',
        'numpy >= 1.17',
        'pysam >= 0.15.1',
    ],
    test_requires=test_deps,
    extras_require={'test': test_deps},
    python_requires='>=3.7',
)
