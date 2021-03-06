import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def plot(clean_signal, degraded_signal):

    i = 0

    # -------------- Génération signal propre -------------

    for chip in clean_signal:
        t = np.arange(i * 2 * np.pi, (i * 2 + 2) * np.pi, 0.01)

        if chip < 0:
            s = np.sin(t - np.pi) * abs(chip)
        elif chip > 0:
            s = np.sin(t) * abs(chip)
        else:
            s = np.zeros_like(t)

        plt.plot(t, s, color='b')

        i += 1

    i = 0

    # -------------- Génération signal dégradé -------------

    for chip in degraded_signal:
        t = np.arange(i * 2 * np.pi, (i * 2 + 2) * np.pi, 0.01)

        if(chip != clean_signal[i]):
            if chip < 0:
                s = np.sin(t - np.pi) * abs(chip)
            elif chip > 0:
                s = np.sin(t) * abs(chip)
            else:
                s = np.zeros_like(t)

            plt.plot(t, s, color='r', alpha=0.6)

        i += 1

    plt.ylabel('Amplitude')
    plt.xlabel('Time')

    blue_patch = mpatches.Patch(color='blue', alpha=0.6, label='Original signal')
    red_patch = mpatches.Patch(color='red', alpha=0.6, label='Degraded signal')
    plt.legend(handles=[blue_patch, red_patch])

    plt.savefig("plot.png", format="png", transparent=True)


def clear():
    plt.clf()
