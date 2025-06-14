from app.cli import parser
from app.cli.actions import (
    show_emojis_list,
    to_generation_context
)


def main():
    ns = parser.parse_args()

    if hasattr(ns, 'func'):
        match ns.func:
            case "emojis":
                show_emojis_list()
            case "gen":
                to_generation_context(ns)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
