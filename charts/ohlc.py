import mplfinance as mpf


def createOHLC(
    data, add_plots, title, ylabel, filename,
    figscale=1.25):

    mc = mpf.make_marketcolors(up='white', down='white')
    s  = mpf.make_mpf_style(
        base_mpf_style='nightclouds',
        marketcolors=mc)

    mpf.plot(
        data, addplot=add_plots, type='ohlc', linecolor='white',
        title=title, ylabel=ylabel, style='nightclouds',
        savefig=filename, figscale=figscale)