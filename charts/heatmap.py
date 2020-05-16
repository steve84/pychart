import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt


def createHeatmap(
        data, labels, filename, xtick_rotation=45,
        xtick_position='right', hscaling=1, vscaling=1):

    mask = np.triu(np.ones_like(data, dtype=np.bool), 1)

    fig, axes = plt.subplots(1, 1, squeeze=False)
    g = sb.heatmap(
        data, mask=mask, annot=True, fmt=".2f", linewidths=.5,
        xticklabels=labels, yticklabels=labels)

    g.set_xticklabels(
        g.get_xticklabels(), rotation=xtick_rotation,
        ha=xtick_position)

    fig.set_size_inches(
        np.array([
            fig.get_size_inches()[0] * hscaling,
            fig.get_size_inches()[1] * vscaling
        ])
    )

    plt.tight_layout()
    plt.savefig(filename, format='png')