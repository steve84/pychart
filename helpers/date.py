import pandas as pd
import matplotlib.dates as mpl_dates


def convertTimestampToNumber(data):
    data = pd.to_datetime(data)
    data = pd.Series(data.values)
    data = data.apply(mpl_dates.date2num)
    return data.values