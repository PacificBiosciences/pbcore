from nose.tools import assert_equal
from pbcore.util import Process

class TestBackticks(object):
    def test_errCode(self):
        output, errCode, errMsg = Process.backticks("exit 42")
        assert_equal(42, errCode)

    def test_output(self):
        output, errCode, errMsg = Process.backticks("echo Me stdout")
        assert_equal(["Me stdout"], output)

    def test_errMsg(self):
        output, errCode, errMsg = Process.backticks("grep -l . /proc/cpuinfo /dev/foo/bar")
        assert_equal("/proc/cpuinfo\ngrep: /dev/foo/bar: No such file or directory", errMsg)

    def test_errMsgMerge(self):
        output, errCode, errMsg = Process.backticks("grep -l . /proc/cpuinfo /dev/foo/bar", merge_stderr=False)
        assert output == ["/proc/cpuinfo"] and errMsg == "grep: /dev/foo/bar: No such file or directory"

