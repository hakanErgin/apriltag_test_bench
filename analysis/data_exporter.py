from IPython.display import display, display_png, HTML
import nbformat


def display_category(paths, notebooks_type):
    if notebooks_type == "translations" or notebooks_type == "rotations":
        for nb_path in paths[notebooks_type]:
            nb_cells = nbformat.read(nb_path, as_version=4)
            error_description, error_plot, nb_name = export_data(
                nb_cells, notebooks_type, nb_path
            )
            display(HTML(nb_name))
            display(error_description)
            display_png(error_plot, raw=True)

    if notebooks_type == "linear_velocity" or notebooks_type == "angular_velocity":
        for nb_path in paths[notebooks_type]:
            nb_cells = nbformat.read(nb_path, as_version=4)
            detection_ratios, error_plot, nb_name = export_data(
                nb_cells, notebooks_type, nb_path
            )
            display(HTML(nb_name))
            display(HTML(detection_ratios))
            display_png(error_plot, raw=True)


def export_data(nb, notebooks_type, nb_path):
    error_description = None
    error_plot = None

    if notebooks_type == "translations" or notebooks_type == "rotations":
        for cell in nb.cells:
            if cell.source == "grouped_df.error.describe()":
                error_description = HTML(cell.outputs[0].data["text/html"])
            if cell.source == "box_plotter('error')":
                error_plot = cell.outputs[0].data["image/png"]
        return (error_description, error_plot, get_nb_name(nb_path, notebooks_type))

    if notebooks_type == "linear_velocity" or notebooks_type == "angular_velocity":
        for cell in nb.cells:
            if (
                cell.source
                == "# ratio of detected to not\nratios = df.is_detected.value_counts(normalize=True)*100\nratios"
            ):
                error_description = cell.outputs[0].data["text/plain"]
            if cell.source == "ratios.plot.pie()\nplt.legend()":
                error_plot = cell.outputs[1].data["image/png"]
        return (error_description, error_plot, get_nb_name(nb_path, notebooks_type))


def get_nb_name(nb_path, notebooks_type):

    if notebooks_type == "translations":
        res = nb_path.split("_")[-2]
        tag = nb_path.split("_")[-6].split("/")[-1]
        return str(tag + " - " + res)

    elif notebooks_type == "rotations":
        res = nb_path.split("_")[-2]
        dist = nb_path.split("_")[-3]
        tag = nb_path.split("_")[-4]
        return str(tag + " - " + dist + " - " + res)

    elif notebooks_type == "linear_velocity":
        res = nb_path.split("_")[-1].split(".")[-2]
        dist = nb_path.split("_")[-4] + "." + nb_path.split("_")[-3]
        dist = dist.split("/")[-1]
        tag = nb_path.split("_")[-2]
        return str(tag + " - " + dist + " - " + res)

    elif notebooks_type == "angular_velocity":
        axis = nb_path.split("/")[-3]
        dist = nb_path.split("/")[-2]
        tag = nb_path.split("/")[-1].split(".")[0]
        return str(axis + " - " + tag + " - " + dist)
