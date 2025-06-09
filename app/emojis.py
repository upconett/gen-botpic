import os
import zipfile as zipf
from contextlib import contextmanager


@contextmanager
def unzip():
    """ Context manager \\
    Unzips archive with emoji images to `resources/emoji/`,
    removes the `resources/emoji/` after escaping the with block
    """
    try:
        os.makedirs("resources/emoji/", exist_ok=True)
        with zipf.ZipFile("resources/emoji.zip") as file:
            file.extractall('resources/emoji/')
        yield
    finally:
        _super_remove("resources/emoji/")


def _super_remove(_path: str):
    """ DANGEROUS FUNC \\
    Annihilates the directory (or file) from FS \\
    If there is something in the directory - goes recursive
    """
    if os.path.isfile(_path):
        os.remove(_path)
    else:
        for fname in os.listdir(_path):
            _super_remove(os.path.join(_path, fname))
        os.rmdir(_path)
