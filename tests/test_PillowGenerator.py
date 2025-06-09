import os

from app import emojis
from app.gen import PillowGenerator
from app.models import Emoji, Color


def test_gen():
    gen = PillowGenerator(
        emoji=Emoji("artist-palette"),
        colors=[
            Color("#98D9C2"),
            Color("#B9FFB7"),
            Color("#ABEDC6"),
            Color("#F19A3E"), 
            Color("#9D2C95")
        ],
        save_path="tests/data/"
    )

    with emojis.unzip():
        img_path = gen.generate()

    assert os.path.exists(img_path)
