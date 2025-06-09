import os

from app import emojis
from app.gen import PillowGenerator
from app.models import Emoji, Color


def test_gen():
    gen = PillowGenerator(
        emoji=Emoji("printer"),
        colors=[
            Color("#EEC643"),
            Color("#000000")
        ],
        save_path="tests/data/"
    )

    with emojis.unzip():
        img_path = gen.generate()

    assert os.path.exists(img_path)
