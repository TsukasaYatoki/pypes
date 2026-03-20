import argparse

from core import Animation


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="A terminal animation of pipes flowing across the screen."
    )

    parser.add_argument("--fps", type=int, default=20, help="Frames per second")
    parser.add_argument(
        "--turn_prob", type=float, default=0.1, help="Probability of pipe turning"
    )
    parser.add_argument(
        "--bg_color",
        type=str,
        default="black",
        help="Background color, can be a named color or hex code",
    )
    parser.add_argument(
        "--border_method",
        choices=["reset", "cycle"],
        default="reset",
        help="How pipes behave at the border",
    )

    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    animation = Animation(args)
    animation.loop()


if __name__ == "__main__":
    args = parse_args()

    main(args)
