# Author: David Alexander

from __future__ import absolute_import, division, print_function

from builtins import range
import numpy as np

class UnavailableFeature(Exception): pass
class Unimplemented(Exception):      pass
class ReferenceMismatch(Exception):  pass
class IncompatibleFile(Exception):   pass


BASE_FEATURE_TAGS =  { "InsertionQV"        : ("iq", "qv",      np.uint8),
                       "DeletionQV"         : ("dq", "qv",      np.uint8),
                       "DeletionTag"        : ("dt", "base",    np.int8 ),
                       "SubstitutionQV"     : ("sq", "qv",      np.uint8),
                       "MergeQV"            : ("mq", "qv",      np.uint8),
                       "Ipd:Frames"         : ("ip", "frames",  np.uint16),
                       "Ipd:CodecV1"        : ("ip", "codecV1", np.uint8),
                       "PulseWidth:Frames"  : ("pw", "frames",  np.uint16),
                       "PulseWidth:CodecV1" : ("pw", "codecV1", np.uint8) }

PULSE_FEATURE_TAGS = { "PulseCall"          : ("pc", "pulse",    np.uint8),
                       "StartFrame"         : ("sf", "frames32", np.uint32),
                       "PkMid"              : ("pm", "photons",  np.uint16),
                       "PkMean"             : ("pa", "photons",  np.uint16) }

ASCII_COMPLEMENT_MAP = { ord("A") : ord("T"),
                         ord("T") : ord("A"),
                         ord("C") : ord("G"),
                         ord("G") : ord("C"),
                         ord("N") : ord("N"),
                         ord("-") : ord("-") }

complementAscii = np.vectorize(ASCII_COMPLEMENT_MAP.get, otypes=[np.int8])

def reverseComplementAscii(a):
    return complementAscii(a)[::-1]


BAM_CMATCH     = 0
BAM_CINS       = 1
BAM_CDEL       = 2
BAM_CREF_SKIP  = 3
BAM_CSOFT_CLIP = 4
BAM_CHARD_CLIP = 5
BAM_CPAD       = 6
BAM_CEQUAL     = 7
BAM_CDIFF      = 8



#
# qId calculation from RG ID string
#
def rgAsInt(rgIdString):
    return np.int32(int(rgIdString, 16))

#
# Kinetics: decode the scheme we are using to encode approximate frame
# counts in 8-bits.
#
def _makeFramepoints():
    B = 2
    t = 6
    T = 2**t

    framepoints = []
    next = 0
    for i in range(256//T):
        grain = B**i
        nextOnes = next + grain * np.arange(0, T)
        next = nextOnes[-1] + grain
        framepoints = framepoints + list(nextOnes)
    return np.array(framepoints, dtype=np.uint16)

def _makeLookup(framepoints):
    # (frame -> code) involves some kind of rounding
    # basic round-to-nearest
    frameToCode = np.empty(shape=max(framepoints)+1, dtype=int)
    for i, (fl, fu) in enumerate(zip(framepoints, framepoints[1:])):
        if (fu > fl + 1):
            m = (fl + fu)//2
            for f in range(fl, m):
                frameToCode[f] = i
            for f in range(m, fu):
                frameToCode[f] = i + 1
        else:
            frameToCode[fl] = i
    # Extra entry for last:
    frameToCode[fu] = i + 1
    return frameToCode, fu

_framepoints = _makeFramepoints()
_frameToCode, _maxFramepoint = _makeLookup(_framepoints)

def framesToCode(nframes):
    nframes = np.minimum(_maxFramepoint, nframes)
    return _frameToCode[nframes]

def codeToFrames(code):
    return _framepoints[code]

def downsampleFrames(nframes):
    return codeToFrames(framesToCode(nframes))
