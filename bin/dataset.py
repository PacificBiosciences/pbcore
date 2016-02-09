#!/usr/bin/env python

import sys

def main(argv=sys.argv):
    """This file, its use in setup.py should be removed after 1.2.8 is cut"""
    print ("WARNING: dataset.py is no longer part of pbcore. It has moved to "
           "pbcoretools (https://github.com/PacificBiosciences/pbcoretools) "
           "and is now just 'dataset'")
    exit(1)

if __name__ == '__main__':
    sys.exit(main())
