import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


def createScatter(
        data, x, y, hue, x_label, y_label, title, legend_title,
        filename, size=None, dot_size=100, annotation=None,
        annotation_func=None, annotation_text_size=10, avg_ratio=None,
        avg_line_color='k', hscaling=1, vscaling=1):

    fig, axes = plt.subplots(1, 1, squeeze=False)
    g = sb.scatterplot(
        x=x, y=y, hue=hue, data=data, size=size, legend='full',
        palette='rainbow', s=dot_size)

    if annotation is not None or annotation_func is not None:
        for i, row in data.iterrows():
            txt = (
                annotation_func(row) if annotation_func is not None
                else row[annotation])
            if np.isfinite(row[x]) and np.isfinite(row[y]):
                g.text(
                    row[x] + 0.5, row[y] + 0.5,
                    txt, fontsize=annotation_text_size)

    g.set(xlabel=x_label, ylabel=y_label, title=title)

    handles, labels = g.get_legend_handles_labels()
    end_index = len(labels)
    if size is not None:
        end_index = [i.get_text() for i in g.legend().texts].index(size)
    g.legend(handles=handles[1:end_index], labels=labels[1:end_index], title=legend_title)

    if avg_ratio is not None:
        y_min = data[y].min()
        y_max = data[y].max()
        y_spread = y_max - y_min
        y_pct = 0
        y_delta = y_spread * y_pct
        y_serie = np.linspace(y_min - y_delta, y_max + y_delta, 10000)

        x_serie = pd.Series(list(map(lambda x: x * avg_ratio, y_serie)))

        x_min = data[x].min()
        x_max = data[x].max()
        x_spread = x_max - x_min
        x_pct = 0.01
        x_delta = x_spread * x_pct

        x_cond = (x_serie <= x_max + x_delta) & (x_serie >= x_min - x_delta)
        x_max_index = x_serie[x_cond].index.max()
        x_min_index = x_serie[x_cond].index.min()

        if np.isnan(x_min_index):
            x_min_index = 0
        if np.isnan(x_max_index):
            x_max_index = len(x_serie)

        x_serie = x_serie.to_list()[x_min_index:x_max_index]
        y_serie = y_serie[x_min_index:x_max_index]

        plt.plot(x_serie, y_serie, color=avg_line_color)

    fig.set_size_inches(
        np.array([
            fig.get_size_inches()[0] * hscaling,
            fig.get_size_inches()[1] * vscaling
        ])
    )

    plt.tight_layout()
    plt.savefig(filename, format='png')