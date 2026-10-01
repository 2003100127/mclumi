__version__ = "0.0.1"
__copyright__ = "Copyright 2025"
__license__ = "GPL v3.0"


import os


def root_dict():
    """

    Returns
    -------

    """
    ROOT_DICT = os.path.dirname(os.path.abspath(__file__))
    return ROOT_DICT


def to(path):
    """

    Parameters
    ----------
    path

    Returns
    -------

    """
    return os.path.join(
        root_dict(),
        path
    )