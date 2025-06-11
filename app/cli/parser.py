from argparse import (
    ArgumentParser,
    ArgumentDefaultsHelpFormatter,
    RawTextHelpFormatter
)


class CustomFormatter(
    RawTextHelpFormatter,
    ArgumentDefaultsHelpFormatter,
): ...


DESCRIPTION = \
"""Bot Picture Generator
Used to generate profile pictures for Telegram bots

Generates random gradient background from provided colours
Then places chosen emoji in the centre of the image
"""


# region parser

parser = ArgumentParser(
    prog="botpic",
    formatter_class=CustomFormatter,
    description=DESCRIPTION
)

subparsers = parser.add_subparsers(title="commands")

# endregion


# region parser_gen

parser_gen = subparsers.add_parser("gen", help="generates botpics")
parser_gen.description = DESCRIPTION
parser_gen.set_defaults(func="gen")
parser_gen.formatter_class = CustomFormatter

parser_gen.add_argument("emoji", help="to place on the foreground")
parser_gen.add_argument("main_color", help="base background color")
parser_gen.add_argument("additional_colors", nargs='*', default=[], help="to create gradient")

parser_gen.add_argument("-s", "--emoji_scale", type=float, default=1.5, help="scale of emoji")
parser_gen.add_argument("-d", "--drops", type=int, default=20, help="number of gradient drops")

# endregion


# region parser_emojis

parser_emojis = subparsers.add_parser("emojis", help="displays list of available emojis")
parser_emojis.description = "opens list of available emojis in less"
parser_emojis.set_defaults(func="emojis")
parser_emojis.formatter_class = CustomFormatter

# endregion
