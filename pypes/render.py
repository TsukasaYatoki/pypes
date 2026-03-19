from blessed import Terminal
from pipe import Pipe


class Renderer:
    """Small rendering helper that writes pipe frames to the terminal."""

    def __init__(self) -> None:
        self.term = Terminal()

        self.max_x = self.term.width
        self.max_y = self.term.height

        self._clear()

    def _clear(self) -> None:
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
