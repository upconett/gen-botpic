import os
import sys
from argparse import Namespace

from app.models import Color, Emoji
from app.exceptions import (
    InvalidColor,
    UnknownEmoji
)

from app.emojis import EMOJI_DIR_P
from app import emojis
from app.gen import StandartGenerator


def to_generation_context(ns):
    with emojis.unzip():
        _perform_actions(ns)


def _perform_actions(ns: Namespace):
    try:
        _ensure_emoji_exists(ns)
        _ensure_correct_colors(ns)

        gen = StandartGenerator(
            emoji=Emoji(ns.emoji),
            main_color=Color(ns.main_color),
            additional_colors=[Color(c) for c in ns.additional_colors],
            emoji_scale=ns.emoji_scale,
            drops=ns.drops
        )
        image_path = gen.generate()

        print(f"  Done, see {image_path}")
    
    except UnknownEmoji as e:
        print(
           f"  Unknown emoji: {e.args[0]}\n"
            "  Use \"botpic emojis\" to see the list of available emojis"
        )
    
    except InvalidColor as e:
        print(
           f"  Invalid hex color: {e.args[0]}\n"
            "  Valid format: \"#000000\" or \"000000\" with characters: [0-9a-f]"
        )


def _ensure_correct_colors(ns: Namespace):
    for c in [ns.main_color] + ns.additional_colors:
        if not Color.valid(c):
            raise InvalidColor(c)


def _ensure_emoji_exists(ns: Namespace):
    for e in os.listdir(EMOJI_DIR_P):
        if ns.emoji == e.replace(".png", ''):
            return
    raise UnknownEmoji(ns.emoji)
