from setuptools import setup, Extension, find_packages
import sys

if sys.version_info < (2, 7, 0):
    print "pbcore requires Python 2.7"
    sys.exit(-1)

setup(
    name = 'pbcore',
    version='0.5.0',
    author='Pacific Biosciences',
    author_email='devnet@pacificbiosciences.com',
    license=open('LICENSES.txt').read(),
    packages = find_packages('src'),
    package_dir = {'':'src'},
    package_data = {'pbcore': ['data/*.h5', 'data/*.gff3', 'data/*.fasta'] },
    zip_safe = False,
    install_requires=[
        'h5py >= 2.0.1',
        'numpy >= 1.6.0'
        ]
    )
