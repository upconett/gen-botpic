import os
import tempfile
import subprocess

import platform

from app import emojis


def show_emojis_list(): 
    with emojis.unzip() as emoji_dir_path: # type: ignore
        emoji_list = [e.replace(".png", '') for e in os.listdir(emoji_dir_path)]
    
    emojis_str = '\n'.join(emoji_list)

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
        tmp_file.write(emojis_str)
        tmp_file_path = tmp_file.name

    try:
        if platform.system() == "Linux":
            subprocess.run(["less", tmp_file_path])
        else:
            print(emojis_str)
    finally:
        os.unlink(tmp_file_path)
