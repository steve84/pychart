import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


def createHistogram(data, x, x_label, y_label, filename,
    palette='Blues_d', xtick_rotation=45,
    xtick_position='right', hscaling=1, vscaling=1):

    fig, axes = plt.subplots(1, 1, squeeze=False)

    g = sb.countplot(x=x, data=data, palette=palette)
    g.set_xticklabels(
        g.get_xticklabels(), rotation=xtick_rotation,
        ha=xtick_position)
    g.set_xlabel(x_label)
    g.set_ylabel(y_label)

    fig.set_size_inches(
        np.array([
            fig.get_size_inches()[0] * hscaling,
            fig.get_size_inches()[1] * vscaling
        ])
    )

    plt.tight_layout()
    plt.savefig(filename, format='png')