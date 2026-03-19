from blessed import Terminal
from pipe import Pipe


class Canvas:
    """Small rendering helper that writes pipe frames to the terminal."""

    def __init__(self, term: Terminal) -> None:
        self.term = term

    def clear(self) -> None:
        """Clear the screen and move the cursor home before drawing frames."""
        print(self.term.home + self.term.clear)

    def draw(self, pipe: Pipe) -> None:
        """Draw the current pipe glyph at its terminal coordinates."""
        print(
            self.term.move_xy(pipe.x, pipe.y)
            + getattr(self.term, pipe.color)(pipe.char),
            end="",
            flush=True,
        )
