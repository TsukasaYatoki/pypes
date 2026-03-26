import argparse

from core import Animation


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="A terminal animation of pipes flowing across the screen."
    )

    parser.add_argument("-f", "--fps", type=int, default=30, help="Frames per second")
    parser.add_argument(
        "-p", "--turn_prob", type=float, default=0.1, help="Probability of pipe turning"
    )
    parser.add_argument(
        "-n", "--pipe_num", type=int, default=1, help="Number of pipes to animate"
    )
    parser.add_argument(
        "-l",
        "--frame_limit",
        type=int,
        default=0,
        help="Number of frames to run before clearing (0 for infinite)",
    )
    parser.add_argument(
        "-t",
        "--pipe_type",
        type=int,
        default=0,
        choices=range(5),
        help="Pipe character set type",
    )
    parser.add_argument(
        "-b",
        "--bg_color",
        type=str,
        default="black",
        help="Background color, can be a named color or hex code",
    )
    parser.add_argument(
        "-m",
        "--border_mode",
        choices=["reset", "cycle"],
        default="reset",
        help="How pipes behave at the border",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    animation = Animation(args)
    animation.loop()


if __name__ == "__main__":
    main()
