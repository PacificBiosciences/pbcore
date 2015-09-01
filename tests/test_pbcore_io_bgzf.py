from nose.tools import assert_equal, assert_true, assert_false
import sys, numpy as np

from tempfile import NamedTemporaryFile

from pbcore.io.align._bgzf import BgzfReader, BgzfWriter


# TODO: did Biopython have tests for it?

class TestBgzf(object):

    def __init__(self):
        pass

    def roundTripData(self, size, sizeToRead=None):
        if sizeToRead is None: sizeToRead = size
        data = (np.sin(np.arange(size))*100).astype(np.int8).tostring()
        assert size == len(data)
        with NamedTemporaryFile() as compressionOutput:
            with BgzfWriter(compressionOutput.name, compresslevel=1) as writer:
                writer.write(data)
            with BgzfReader(compressionOutput.name) as reader:
                decompressionOutput = reader.read(sizeToRead)
        assert_equal(data[:sizeToRead], decompressionOutput)

    def test_small_data(self):
        self.roundTripData(0)
        for i in xrange(8):
            self.roundTripData(10**i)

    def test_partial_reads(self):
        self.roundTripData(10**7, (10**7)/2)

    # def test_big_data(self):
    #     # This breaks because of recursion depth limit in
    #     # implementation from Biopython.
    #     self.roundTripData(10**8)

if __name__ == "__main__":
    size = int(sys.argv[1])
    TestBgzf().roundTripData(size)
