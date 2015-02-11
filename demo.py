import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib.collections import LineCollection
import numpy as np

from pbcore.io import PlxH5Reader


def makeFrame(p):
    frame = np.recarray(shape=(len(p),),
                        dtype=[("Channel",   "<u1"),
                               ("Start",     "<u4"),
                               ("Width",     "<u4"),
                               ("MidSignal", "<u4")])

    frame.Channel   = p.channel()
    frame.Start     = p.startFrame()
    frame.Width     = p.widthInFrames()
    frame.MidSignal = p.midSignal()

    return frame


def framesByChannel(frame):
    return [ frame[frame.Channel == i] for i in xrange(4) ]

def oneChannelPath(frame1):
    # Path, or LineCollection:
    # http://matplotlib.org/users/path_tutorial.html
    # http://matplotlib.org/api/collections_api.html
    assert len(set(frame1.Channel)) <= 1
    verts = []
    codes = []
    for i, pls in enumerate(frame1):
        if i == 0:
            codes.append(Path.MOVETO)
        else:
            codes.append(Path.LINETO)
        verts.append( (pls.Start, 0))

        codes.append(Path.LINETO)
        verts.append( (pls.Start, pls.MidSignal) )

        codes.append(Path.LINETO)
        verts.append( (pls.Start + pls.Width, pls.MidSignal) )

        codes.append(Path.LINETO)
        verts.append( (pls.Start + pls.Width, 0))

    path = Path(verts, codes)
    return path


def plotAllSignals(frame):
    CMAP = np.array([ "red", "orange", "blue", "green" ])
    xmargin = ymargin = 20
    xmin, xmax = 0 - xmargin, frame[-1].Start + frame[-1].Width + xmargin
    ymin, ymax = 0 - ymargin, max(frame.MidSignal) + ymargin

    allChannelFrames = framesByChannel(frame)
    paths = map(oneChannelPath, allChannelFrames)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    for path, color in zip(paths, CMAP):
        ax.add_patch(patches.PathPatch(path, edgecolor=color, fill=False, lw=2))
    plt.show()



P = PlxH5Reader("~/Data/DeepPrimary/m141008_060349_42194_c100704972550000001823137703241586_s1_p0.1.plx.h5")

z = P[12]


subread0       = z.subreads[0]
p = subread0pulses = z.pulsesByBaseInterval(0, 49)
frame = makeFrame(p)
