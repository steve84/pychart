import mplfinance as mpf


def createOHLC(
    data, add_plots, title, ylabel, filename,
    figratio=(16, 9), figscale=1.25):

    mpf.plot(
        data, addplot=add_plots, type='ohlc',
        title=title, ylabel=ylabel, savefig=filename,
        figratio=figratio, figscale=figscale)