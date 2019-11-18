import os
import pytest
import sys

from pbcore.io.dataset.utils import which


def _check_constools():
    return which('pbindex') and which('samtools') and which('pbmerge')


def _internal_data():
    return os.path.exists("/pbi/dept/secondary/siv/testdata")


def pytest_runtest_setup(item):
    for mark in item.iter_markers():
        if mark.name == 'internal_data':
            if not _internal_data():
                pytest.skip(
                    "need access to '/pbi/dept/secondary/siv/testdata'")
        elif mark.name == 'constools':
            if not _check_constools():
                pytest.skip("need 'pbindex'/'samtools'/'pbmerge'")
        elif mark.name == 'linux':
            if sys.platform != "linux":
                pytest.skip(
                    "cannot run linux tests on platform: '{}'".format(
                        sys.platform))
        else:
            raise LookupError("Unknown pytest mark: '{}'".format(mark.name))
