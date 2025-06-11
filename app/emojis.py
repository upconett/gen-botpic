import os
import zipfile as zipf
from contextlib import contextmanager

from app.util import get_resource_path


EMOJI_DIR_P = get_resource_path("resources/emoji/") 
EMOJI_ZIP_P = get_resource_path("resources/emoji.zip") 


@contextmanager
def unzip():
    """ Context manager \\
    Unzips archive with emoji images to `resources/emoji/`,
    removes the `resources/emoji/` after escaping the with block
    """
    try:
        os.makedirs(EMOJI_DIR_P, exist_ok=True)
        with zipf.ZipFile(EMOJI_ZIP_P) as file:
            file.extractall(EMOJI_DIR_P)
        yield EMOJI_DIR_P
    finally:
        _super_remove(EMOJI_DIR_P)


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
