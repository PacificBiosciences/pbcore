#!/bin/bash

# ---- error handling
set -o errexit;
set -o posix;
set -o pipefail;
set -o errtrace;
unexpected_error() {
    local errstat=$?
    echo "${g_prog:-$(basename $0)}: Error! Encountered unexpected error at 'line $(caller)', bailing out..." 1>&2
    exit $errstat;
}
trap unexpected_error ERR;

# Force the path to only what we need, saving off the original path
PATH_ORIG=$PATH;
PATH=/usr/bin:/bin

g_prog=$(basename "$0");
g_progdir=$(dirname "$0");
g_progdir_abs=$(readlink -f "$g_progdir");

# ---- error functions
merror() {
    echo "$g_prog: Error! ""$@" 1>&2;
    exit 1;
}
minterror() {
    echo "$g_prog: Internal Error! ""$@" 1>&2;
    exit 1;
}
mwarn() {
    echo "$g_prog: Warning! ""$@" 1>&2;
}


# ---- usage

usage() {
  local exitstat=2;
  if [[ ! -z "$2" ]] ; then
      exitstat=$2;
  fi

  # Only redirect to stderr on non-zero exit status
  if [[ $exitstat -ne 0 ]] ; then
      exec 1>&2;
  fi

  if [[ ! -z "$1" ]] ; then
      echo "$g_prog: Error! $1" 1>&2;
  fi

  echo "Usage: $g_prog [--help] \\"
  echo "              [--clean] [--build] [--install]";
  echo "         --clean       -- clean the build (def: clean if no args specified)";
  echo "         --build       -- build the build (def: build if no args specified)";
  echo "         --install     -- install the build (def: install if no args specified)";
  echo "         --help        -- print this usage";
  echo "";

  # bash only:
  if [[ $exitstat -ne 0 ]] ; then
      echo "  at: $(caller)";
  fi
  exit $exitstat;
}

# ---- argument parsing

# Save off the original args, use as "${g_origargs[@]}" (with double quotes)
declare -a g_origargs;
g_origargs=( ${1+"$@"} )

opt_clean=false;
opt_build=false;
opt_install=false;
while [[ $# != 0 ]]; do
    opt="$1"; shift;
    case "$opt" in
	# Flag with no argument example:
	#   --flag|--fla|--fl|--f)
	#     opt_flag=true;;
	# Option with argument example:
	#   --arg|--ar|--a)
	#     [[ $# -eq 0 ]] && usage;
	#     opt_somearg=$1; shift;;
	--clean) opt_clean=true;;
	--build) opt_build=true;;
	--install) opt_install=true;;
	-h|-help|--help|--hel|--he|--h) usage "" 0;;
	-*) usage "Unrecognized option: $opt";;
	*)  usage "Extra trailing arguments: $opt $@";;
    esac
done

if ! $opt_clean && ! $opt_build && ! $opt_install; then
    # No args specified, perform all the actions
    opt_clean=true;
    opt_build=true;
    opt_install=true;
fi

# ---- global

g_pkgname="pbcore"
g_topdir_abs="${g_progdir_abs}/../../../../.."

g_wheel_version="0.24.0"
g_wheel_rootdir="${g_topdir_abs}/prebuilt.tmpsrc/pythonpkgs/wheel/wheel_${g_wheel_version}/_output/install"
g_wheel_pythonpath="${g_wheel_rootdir}/lib/python2.7/site-packages"

g_pip_version="6.0.8"
g_pip_rootdir="${g_topdir_abs}/prebuilt.tmpsrc/pythonpkgs/pip/pip_${g_pip_version}/_output/install"
g_pip_pythonpath="${g_pip_rootdir}/lib/python2.7/site-packages"

g_setuptools_version="14.3.1"
g_setuptools_rootdir="${g_topdir_abs}/prebuilt.tmpsrc/pythonpkgs/setuptools/setuptools_${g_setuptools_version}/_output/install"
g_setuptools_pythonpath="${g_setuptools_rootdir}/lib/python2.7/site-packages"

g_python_exe="${g_topdir_abs}/prebuilt.out/python/python-2.7.3/centos-5/bin/python"
g_python_ldlibpath="${g_topdir_abs}/prebuilt.out/installerdeps/installerdeps-pacbio-0.1/centos-5/lib"

g_srcroot_dir="$g_progdir/.."
g_srcroot_dirabs="$g_progdir_abs/.."
g_output_dir="$g_srcroot_dir/_output"
g_output_dirabs="$g_srcroot_dirabs/_output"
g_wheel_dir="$g_output_dir/wheelhouse"

# ---- main

if $opt_clean; then
    # Clean the output dir
    echo "Cleaning _output dir..."
    rm -rf "$g_output_dir"
fi


if $opt_build; then
    # Make a copy of the source tree and put it in _output/src.  We will 
    # actually hardlink to the source using "rsync --link-dest".  We will
    # invoke "pip wheel"  pointing to the linked source below.
    # NOTE: this is needed because the "pip wheel" command below copies all 
    #       the source into a tmp directory, and we are setting TMPDIR to 
    #       _output/src in our build tree (to avoid pip polluting /tmp with
    #       temporary dirs from aborted builds and such).  That combination
    #       will end up in an endless recursion of copying the source tree 
    #       (in the python shutil.copytree() function) because it copies the
    #       _output directory to _output/tmp (and there is no way, via 
    #       "pip wheel", to specify excluding particular directories)
    echo "Linking source dir..."
    mkdir -p "${g_output_dir}/src"
    rsync -a --exclude "_output" --link-dest="${g_srcroot_dirabs}"  "${g_srcroot_dir}/" "${g_output_dir}/src"
    
    # Creating wheel
    # NOTE: We are setting TMPDIR to a directory under _output to avoid 
    #       littering /tmp with old directories from failed builds and such.
    #       See note above in "Linking source dir..." for more details.
    echo "Creating the ${g_pkgname} wheel from source..."
    mkdir -p "${g_output_dir}/tmp"
    TMPDIR="${g_output_dirabs}/_output/tmp" \
    PYTHONPATH="${g_setuptools_pythonpath}:${g_pip_pythonpath}:${g_wheel_pythonpath}" \
    LD_LIBRARY_PATH="$g_python_ldlibpath" \
	"$g_python_exe" \
	    "${g_pip_rootdir}/bin/pip" \
                wheel --no-clean --no-index --no-deps  --build "$g_output_dir/build" --src "$g_output_dir/src" --wheel-dir "$g_wheel_dir" --verbose "${g_output_dir}/src"
fi


if $opt_install; then
    # Use the PYTHONUSERBASE/--user method for installing a python package into
    # a different directory, as suggested here:
    #
    #   http://stackoverflow.com/questions/2915471/install-a-python-package-into-a-different-directory-using-pip/29103053#29103053
    # 
    # Note that other methods don't really give us what we want:
    #   - the --root option prepends the absolute path to the python executable
    #     after the specified rootdir (seems to to the right thing in 
    #     installing the bin, lib, share dirs, but it is inconvenient have 
    #     the full path to the python binary in output dir).
    #   - the --target method only installs the lib directory at the target, 
    #     but not the full bin, lib, share structure we want (the scripts in 
    #     bin are missing).
    #   - the --install-option="--prefix=$(pwd)/_output/install" dir option 
    #     seems to be ignored.  It always seems to instal in the site-packages
    #     dir of the python tree of the python executable.
    # Note that even this method does not give us exactly what we want:
    #   - the --user option will assign mode 700 to all the directories and 
    #     files (except for the bin directory).  This will make it so that 
    #     other users will not be able to run programs properly.  So we will 
    #     use this method and force the proper ownership after the "pip 
    #     install" command.

    # Now use the version of pip (installed into _output/build above) to create
    # a pip-only install dir (without setuptools).  Note, must specify the 
    # site-packages dir of the install build output above  in the PYTHONPATH.
    echo "Installing ${g_pkgname} (from wheel)..."
    PYTHONUSERBASE="${g_output_dirabs}/install" \
    PYTHONPATH="${g_pip_pythonpath}:${g_wheel_pythonpath}" \
    LD_LIBRARY_PATH="$g_python_ldlibpath" \
	"$g_python_exe" \
	    "${g_pip_rootdir}/bin/pip" \
                install --no-index --find-links="$g_wheel_dir" --no-deps --user --ignore-installed "$g_pkgname"

    # Add group and user permisssions, since the --user option to 'pip install'
    # forces 700 permissions on the entire install tree (with the exception of
    # 'install/bin').
    echo "Adding group/other read permissions..."
    chmod -R og=u-w "${g_output_dirabs}/install"
fi
