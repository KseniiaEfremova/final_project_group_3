import os


def get_path_from_root(path_to_file):
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return f"{root_path}/{path_to_file}"
