import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates

from datetime import datetime
from mplfinance.original_flavor import candlestick_ohlc

date_format = '%d.%m.%Y'


def findIndexByDate(data, dateStr):
    dt = datetime.strptime(dateStr, date_format)
    ndt = mpl_dates.date2num(dt)
    for i in range(0, len(data)):
        if ndt == data[i][0] or (i < len(data) - 1 and ndt > data[i][0] and ndt < data[i+1][0]):
            return i
    return None


def createVolumeSubplot(
    data, axis, date_column, xtick_rotation=45, xtick_position='right'):

    column_subset = list()
    column_subset.append(date_column)
    column_subset.append('Volume')

    volume_data = data[column_subset].values
    volume_data = volume_data.astype(float)
    volume_weekday_data = [tuple([i] + list(quote[1:]))
                            for i, quote in enumerate(volume_data)]
    axis.bar(
        [d[0] for d in volume_weekday_data],
        [d[1] for d in volume_weekday_data])

    axis.set_xticks(range(0, len(volume_weekday_data), 5))
    axis.set_xticklabels([mpl_dates.num2date(volume_data[index][0]).strftime(
        date_format) for index in axis.get_xticks()])
    axis.set_xticklabels(
        axis.get_xticklabels(), rotation=xtick_rotation, ha=xtick_position)


def createCandlestick(
        data, filename, date_column, xtick_rotation=45,
        title=None, xlabel=None, ylabel=None,
        xtick_position='right', plots=[], lines=[],
        cones=[], markers=[], annotations=[], volume=False,
        hscaling=1, vscaling=1):

    sb.set()

    if volume:
        fig, axes = plt.subplots(
            2, 1, squeeze=False, gridspec_kw={'height_ratios': [2, 1]})
    else:
        fig, axes = plt.subplots(
            1, 1, squeeze=False)

    column_subset = list()
    column_subset.append(date_column)
    column_subset = column_subset + [ 'Open', 'High', 'Low', 'Close']

    candlestick_data = data[column_subset].values
    candlestick_data = candlestick_data.astype(float)
    weekday_data = [tuple([i] + list(quote[1:]))
                    for i, quote in enumerate(candlestick_data)]

    candlestick_ohlc(axes[0][0], weekday_data, width=0.6,
                     colorup='green', colordown='red', alpha=0.8)

    if volume:
        createVolumeSubplot(data, axes[1][0], date_column)

    for plot in plots:
        sb.lineplot([x[0] for x in weekday_data], data[plot], ax=axes[0][0])

    for line in lines:
        axes[0][0].plot([
            findIndexByDate(candlestick_data, line[0][0]),
            findIndexByDate(candlestick_data, line[0][1])
        ], line[1], '%s-' % line[2])

    for cone in cones:
        t = np.arange(findIndexByDate(candlestick_data, cone[0][0]), findIndexByDate(candlestick_data, cone[0][1]))
        y1 = np.linspace(cone[1][0], cone[1][1], len(t))
        y2 = np.linspace(cone[2][0], cone[2][1], len(t))
        axes[0][0].fill_between(t, y1, y2, facecolor=cone[3], alpha=0.2)

    for marker in markers:
        t = findIndexByDate(candlestick_data, marker[0])
        i = column_subset.index(marker[1])
        axes[0][0].scatter(t, candlestick_data[t][i] * marker[2], color=marker[3], marker=marker[4])

    for annotation in annotations:
        t = findIndexByDate(candlestick_data, annotation[0])
        i = column_subset.index(annotation[1])
        axes[0][0].annotate(annotation[3], (t, candlestick_data[t][i] * annotation[2]))

    if volume:
        axes[0][0].set_xticklabels([])
    else:
        axes[0][0].set_xticks(range(0, len(weekday_data), 5))
        axes[0][0].set_xticklabels([mpl_dates.num2date(candlestick_data[index][0]).strftime(
            date_format) for index in axes[0][0].get_xticks()])
        axes[0][0].set_xticklabels(
            axes[0][0].get_xticklabels(), rotation=xtick_rotation, ha=xtick_position)

    if title is not None:
        axes[0][0].set_title(title)
    if xlabel is not None:
        axes[0][0].set_xlabel(xlabel)
    if ylabel is not None:
        axes[0][0].set_ylabel(ylabel)

    fig.set_size_inches(
        np.array([
            fig.get_size_inches()[0] * hscaling,
            fig.get_size_inches()[1] * vscaling
        ])
    )
    plt.tight_layout()
    plt.savefig(filename, format='png')