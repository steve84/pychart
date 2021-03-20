import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt


def createHeatmap(
        data, labels, filename, title=None,
        xtick_rotation=45, xtick_position='right',
        hscaling=1, vscaling=1):

    mask = np.triu(np.ones_like(data, dtype=np.bool), 1)

    fig, axes = plt.subplots(1, 1, squeeze=False)
    g = sb.heatmap(
        data, mask=mask, annot=True, fmt=".2f", linewidths=.5,
        xticklabels=labels, yticklabels=labels,
        cmap='RdYlGn', vmin=-1.0, vmax=1.0)

    cbar = g.collections[0].colorbar
    cbar.set_ticks([-1, -.75, -.5, -.25, 0, .25, .5, .75, 1])
    cbar.set_ticklabels(
        ['-1.0', '-0.75', '-0.5', '-0.25', '0',
        '0.25', '0.5', '0.75', '1.0']
    )

    g.set_xticklabels(
        g.get_xticklabels(), rotation=xtick_rotation,
        ha=xtick_position)

    fig.set_size_inches(
        np.array([
            fig.get_size_inches()[0] * hscaling,
            fig.get_size_inches()[1] * vscaling
        ])
    )

    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, format='png')
