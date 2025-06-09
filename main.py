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
        color=color.replace('#', '')
        if any((
            len(color) != 6,
            not color.isalnum()
        )): 
            raise InvalidColor(color)

    return PillowGenerator(
        emoji=emoji,
        colors=colors, # type: ignore
        save_path='.'
    )
    

def main():
    try:
        with emojis.unzip():
            gen = gen_from_argv()
            pic_path = gen.generate()
        print(f"Done, see {pic_path}")

    except InvalidUsage:
        print("Usage: gen-botpic <emoji> <hex-color-1> [hex-color-2] ... [hex-color-n]")
        sys.exit(1)

    except InvalidColor as e:
        print(f"Invalid color: {e.args[0]}, required format: [#]000000 (hex)")
        sys.exit(1)

    except UnknownEmoji:
        print("Unknown emoji, consider kebab case naming (i.e hugging-face)")
        sys.exit(1)


if __name__ == "__main__":
    main()
