import os
import zipfile as zipf
from contextlib import contextmanager

from app.util import get_resource_path


@contextmanager
def unzip():
    """ Context manager \\
    Unzips archive with emoji images to `resources/emoji/`,
    removes the `resources/emoji/` after escaping the with block
    """
    emoji_dir_p = get_resource_path("resources/emoji/") 
    emoji_zip_p = get_resource_path("resources/emoji.zip") 
    try:
        os.makedirs(emoji_dir_p, exist_ok=True)
        with zipf.ZipFile(emoji_zip_p) as file:
            file.extractall(emoji_dir_p)
        yield
    finally:
        _super_remove(emoji_dir_p)


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
