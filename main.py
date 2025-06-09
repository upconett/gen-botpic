import sys

from app import emojis
from app.gen import PillowGenerator
from app.gen.exceptions import UnknownEmoji

class InvalidUsage(Exception): ...
class InvalidColor(Exception): ...


def gen_from_argv() -> PillowGenerator:
    args = sys.argv
    if len(args) < 3:
        raise InvalidUsage

    emoji = args[1]
    colors = args[2:]

    for color in colors:
        if any((
            len(color) != 7,
            color[0] != '#',
            not color[1:].isalnum()
        )): 
            raise InvalidColor(color)

    return PillowGenerator(
        emoji=emoji,
        colors=colors # type: ignore
    )
    

def main():
    try:
        with emojis.unzip():
            gen = gen_from_argv()
            gen.generate()

    except InvalidUsage:
        print("Usage: gen-botpic <emoji> <hex-color-1> [hex-color-2] ... [hex-color-n]")
        quit(1)

    except InvalidColor as e:
        print(f"Invalid color: {e.args[0]}, required format: \"#000000\" (hex)")
        quit(1)

    except UnknownEmoji:
        print("Unknown emoji, consider kebab case naming (i.e hugging-face)")
        quit(1)


if __name__ == "__main__":
    main()
