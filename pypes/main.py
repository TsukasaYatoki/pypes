import argparse
import time

from blessed import Terminal
from pipe import Pipe
from render import Canvas


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="A terminal animation of pipes flowing across the screen."
    )

    parser.add_argument("--fps", type=int, default=20, help="Frames per second")
    parser.add_argument(
        "--straight_prob", type=float, default=0.9, help="Probability of going straight"
    )
    parser.add_argument(
        "--border_method",
        choices=["reset", "cycle"],
        default="reset",
        help="How pipes behave at the border",
    )

    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    term = Terminal()
    canvas = Canvas(term)
    canvas.clear()

    pipe = Pipe(term.width, term.height, border=args.border_method)

    with term.fullscreen(), term.hidden_cursor():
        while True:
            canvas.draw(pipe)
            pipe.move()
            pipe.turn(args.straight_prob)
            time.sleep(1 / args.fps)


if __name__ == "__main__":
    args = parse_args()

    main(args)
