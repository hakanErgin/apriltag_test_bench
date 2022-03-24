from IPython.display import display, display_png, HTML, Image


def export_data(nb):
    error_description = None
    error_plot = None

    for cell in nb.cells:
        if cell.source == "grouped_df.error.describe()":
            error_description = HTML(cell.outputs[0].data["text/html"])
        if cell.source == "box_plotter('error')":
            error_plot = cell.outputs[0].data["image/png"]

    return (display(error_description), display_png(error_plot, raw=True))
