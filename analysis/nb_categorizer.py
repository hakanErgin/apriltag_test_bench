import glob

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
