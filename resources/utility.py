from os import walk, path, PathLike
from os.path import dirname, abspath, join
from typing import Union
import sys


def resource_path(relative_path:Union[str, PathLike]):
    """
    Takes internal application paths.
    Formats as needed to be reached when packaged.
    :param relative_path:
    :return: modified path
    """
    try:
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = dirname(abspath(__file__))
    except AttributeError:
        base_path = abspath("..")
    return join(base_path, relative_path)

def get_all_file_paths(directory):
    file_paths = []
    for root, directories, files in walk(directory):
        for filename in files:
            filepath = path.join(root, filename)
            file_paths.append(filepath)
    return file_paths