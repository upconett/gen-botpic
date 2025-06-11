import os
import tempfile
import subprocess

from app import emojis


def show_emojis_list(): 
    with emojis.unzip() as emoji_dir_path: # type: ignore
        emoji_list = [e.replace(".png", '') for e in os.listdir(emoji_dir_path)]

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
        tmp_file.write('\n'.join(emoji_list))
        tmp_file_path = tmp_file.name

    try:
        subprocess.run(["less", tmp_file_path])
    finally:
        os.unlink(tmp_file_path)
