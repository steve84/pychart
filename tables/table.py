from weasyprint import HTML, CSS


def createTable(
    data, columnDict, cssString, filename,
    resolution=300, na_rep='-'):

    data_r = data.rename(columns=columnDict)
    cols = [c for c in columnDict.values()]

    css = CSS(string=cssString)

    html = HTML(string=data_r.to_html(
        index=False, columns=cols, na_rep=na_rep))
    html.write_png(
        filename + '.png', stylesheets=[css], resolution=resolution)