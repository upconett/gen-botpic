import os

from app.gen import PillowGenerator
from app.models import Emoji, Color


def test_gen():
    gen = PillowGenerator(
        colors=[Color("EEC643")],
        save_path="tests/data/"
    )
    img_path = gen.generate()
    assert os.path.exists(img_path)
