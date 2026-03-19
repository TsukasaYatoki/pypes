import argparse
import time

from pipe import Pipe
from render import Renderer


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="A terminal animation of pipes flowing across the screen."
    )

    parser.add_argument("--fps", type=int, default=20, help="Frames per second")
    parser.add_argument(
        "--turn_prob", type=float, default=0.1, help="Probability of pipe turning"
    )
    parser.add_argument(
        "--border_method",
        choices=["reset", "cycle"],
        default="reset",
        help="How pipes behave at the border",
    )

    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    renderer = Renderer()
    pipe = Pipe(
        renderer.max_x, renderer.max_y, p_turn=args.turn_prob, border=args.border_method
    )

    with renderer.term.fullscreen(), renderer.term.hidden_cursor():
        while True:
            renderer.draw(pipe)
            pipe.move()
            pipe.turn()
            time.sleep(1 / args.fps)


if __name__ == "__main__":
    args = parse_args()

    main(args)
