__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "MIT"
__lab__ = "Cribbslab"

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