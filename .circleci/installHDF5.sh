set -x
set -e
if [ ! -e prefix/lib/libhdf5.so ]; then
  wget https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8.12/src/hdf5-1.8.12.tar.gz
  tar xzf hdf5-1.8.12.tar.gz
  mkdir -p prefix
  PREFIX=$PWD/prefix
  cd hdf5-1.8.12
  ./configure --prefix=$PREFIX
  make
  make install
else
    echo "HDF5 build/install already completed!"
fi
