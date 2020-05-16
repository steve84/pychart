import mplfinance as mpf


def createLine(
               data, add_plots, title, ylabel, filename,
               volume=False, figratio=(16, 9), figscale=1.25):

    mpf.plot(data, addplot=add_plots, type='line',
             title=title, ylabel=ylabel,
             volume=volume, savefig=filename,
             figratio=figratio, figscale=figscale)