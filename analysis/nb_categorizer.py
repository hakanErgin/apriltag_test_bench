import glob
from IPython.display import display, display_png, HTML
import nbformat
from data_exporter import export_data
import pandas as pd


def organize_categories(category, notebooks_type):
    df_groupby_res = {"360": {}, "720": {}, "1080": {}}

    for table in category:
        # prepare the tables
        df = pd.read_html(table["error_table"])[0]
        df.columns = df.columns.get_level_values(0)
        df = df.rename({"Unnamed: 0_level_0": "true_value"}, axis=1).set_index(
            "true_value"
        )
        df = df.drop(columns=df.columns[-5:], axis=1)
        df = df.drop(columns=["count"], axis=1)
        df.reset_index(inplace=True)

        if notebooks_type == "translations":
            tag_name, resolution = table["name"].split(" - ")
            df_groupby_res[resolution].update({tag_name: df})

        if notebooks_type == "rotations":
            tag_name, distance, resolution = table["name"].split(" - ")
            dic = {distance: df}
            if not tag_name in df_groupby_res[resolution]:
                df_groupby_res[resolution][tag_name] = {}
            df_groupby_res[resolution][tag_name].update(dic)

    return df_groupby_res


def get_category(paths, notebooks_type):
    # category as in 16h5 - 720
    category = []

    if notebooks_type == "translations" or notebooks_type == "rotations":
        for nb_path in paths[notebooks_type]:
            nb_cells = nbformat.read(nb_path, as_version=4)
            error_description, error_plot, nb_name = export_data(
                nb_cells, notebooks_type, nb_path
            )

            table = {"name": nb_name, "error_table": error_description}

            category.append(table)

    return organize_categories(category, notebooks_type)


def display_category(paths, notebooks_type):
    if notebooks_type == "translations" or notebooks_type == "rotations":
        for nb_path in paths[notebooks_type]:
            nb_cells = nbformat.read(nb_path, as_version=4)
            error_description, error_plot, nb_name = export_data(
                nb_cells, notebooks_type, nb_path
            )
            display(HTML(nb_name))
            display(HTML(error_description))
            display_png(error_plot, raw=True)

    if notebooks_type == "linear_velocity" or notebooks_type == "angular_velocity":
        for nb_path in paths[notebooks_type]:
            nb_cells = nbformat.read(nb_path, as_version=4)
            detection_ratios, error_plot, nb_name = export_data(
                nb_cells, notebooks_type, nb_path
            )
            display(HTML(nb_name))
            display(HTML(detection_ratios[:-34]))
            display_png(error_plot, raw=True)


# returns notebook paths categorized into dict
def categorize_notebooks():

    path = "../test_pipeline/scripts"

    files = glob.glob(path + "/**/result/**/*.ipynb", recursive=True)

    test_results = {
        "translations": [],
        "rotations": [],
        "linear_velocity": [],
        "angular_velocity": [],
    }

    for file in files:
        category = file.split("/")[file.split("/").index("result") - 1]
        test_results[category].append(file)

    return test_results
