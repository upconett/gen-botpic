import os
from abc import ABC, abstractmethod

from app.models import Color, Emoji


class Generator(ABC):
    colors: list[Color]
    emoji: Emoji | None
    size: tuple[int, int]

    def __init__(
        self, *,
        emoji: Emoji | str | None = None,
        main_color: Color,
        additional_colors: list[Color] = [],
        drops: int = 20,
        emoji_scale: float = 1.5,
        size: tuple[int, int] = (500, 500),
        save_path: str = ".",
    ):
        if isinstance(emoji, str):
            emoji = Emoji(emoji)

        self.emoji = emoji
        self.main_color = main_color
        self.additional_colors = additional_colors
        self.emoji_scale = emoji_scale
        self.drops = drops
        self.size = size

        self.save_path = save_path
        self._ensure_path()


    def _ensure_path(self):
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)


    @abstractmethod   
    def generate(self) -> str:
        """ Generates new pic and returns path to the image """
    