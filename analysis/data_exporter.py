from IPython.display import display, display_png, HTML, Image


def export_data(nb):
    error_description = None
    error_plot = None

    for cell in nb.cells:
        if cell.source == "grouped_df.error.describe()":
            error_description = HTML(cell.outputs[0].data["text/html"])
        if cell.source == "box_plotter('error')":
            error_plot = cell.outputs[0].data["image/png"]

    return (error_description, error_plot)


def get_nb_name(nb, notebooks_type):

    if notebooks_type == "translations":
        res = nb.split("_")[-2]
        tag = nb.split("_")[-6].split("/")[-1]
        return str(tag + " - " + res)

    elif notebooks_type == "rotations":
        res = nb.split("_")[-2]
        dist = nb.split("_")[-3]
        tag = nb.split("_")[-4]
        return str(tag + " - " + dist + " - " + res)
