from pbcore.io import PlxH5Reader

P = PlxH5Reader("~/Data/DeepPrimary/m141008_060349_42194_c100704972550000001823137703241586_s1_p0.1.plx.h5")

z = P[12]


subread0       = z.subreads[0]
subread0pulses = z.pulsesByBaseInterval(0, 49)

CMAP = np.array([ "red", "orange", "blue", "green" ])

def plotPulses(zmwPulses):
    starts = zmwPulses.startFrame()
    widths = zmwPulses.widthInFrame()
    amplitudes = zmwPulses.midSignal()
    colors = zmwPulses.channel()


    zPulses = zip(starts, widths, amplitudes, colors)

    for color in range(4):
        for (start, width, amp, color) in zPulses:
