import mplfinance as mpf


def createOHLC(
    data, add_plots, title, ylabel, filename,
    figratio=(16, 9), figscale=1.25):

    mc = mpf.make_marketcolors(up='green', down='red', inherit=True)
    s  = mpf.make_mpf_style(base_mpf_style='default', marketcolors=mc)

    mpf.plot(
        data, addplot=add_plots, type='ohlc', style=s,
        title=title, ylabel=ylabel, savefig=filename,
        figratio=figratio, figscale=figscale)