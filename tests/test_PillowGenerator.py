import os

from app.gen import PillowGenerator
from app.models import Color


def test_gen():
    gen = PillowGenerator(
        colors=[
            Color("#EEC643"),
            Color("#000000")
        ],
        save_path="tests/data/"
    )
    img_path = gen.generate()
    assert os.path.exists(img_path)
