from __future__ import absolute_import, division, print_function

class h5py_dummy(object):
    def __getattr__(self, name):
        raise ImportError("The h5py module is required to use this optional feature; you can install it using 'pip install h5py' (requires HDF5 library already installed).")
