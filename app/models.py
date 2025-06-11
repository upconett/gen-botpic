import os
import re
from app.util import get_resource_path


class Emoji:
    name: str

    def __init__(self, name: str):
        self.name = name

    @property
    def path(self) -> str:
        return os.path.join(
            get_resource_path("resources/emoji"),
            f"{self.name}.png"
        )


class Color:
    """ Color in hex code """
    code: str

    def __init__(self, code: str):
        self.code = code.replace('#', '')

    @staticmethod
    def valid(color: str) -> bool:
        return re.match(r"#?[0-9a-fA-f]{6}", color) is not None

    @property
    def hex(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"#{self.code}"
