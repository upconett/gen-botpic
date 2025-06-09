import os
from abc import ABC, abstractmethod

from app.models import Color, Emoji


class Generator(ABC):
    colors: list[Color]
    emoji: Emoji | None
    size: tuple[int, int]

    def __init__(
        self, *,
        colors: list[Color] = [],
        emoji: Emoji | None = None,
        size: tuple[int, int] = (500, 500),
        save_path: str = "data",
    ):
        self.colors = colors
        self.emoji = emoji
        self.size = size

        self.save_path = save_path
        self._ensure_path()

    def _ensure_path(self):
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    @abstractmethod   
    def generate(self) -> str:
        """ Generates new pic and returns path to the image """
    