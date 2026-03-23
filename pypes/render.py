from blessed import Terminal


class Renderer:  # TODO: not use blessed dependency
    """Small rendering helper that writes pipe frames to the terminal."""

    def __init__(self, bg_color: str = "black") -> None:
        self.term = Terminal()

        if bg_color.startswith("#"):
            self.bg_color = self.term.on_color_hex(bg_color)
        else:
            self.bg_color = getattr(self.term, f"on_{bg_color}")

        self.clear()

    def clear(self) -> None:
        """Clear the screen and move the cursor home before drawing frames."""
        print(self.term.home + self.term.clear + self.bg_color)

    def draw(self, x: int, y: int, glyph: str, color: str) -> None:
        """Draw the current pipe glyph at its terminal coordinates."""
        print(
            self.term.move_xy(x, y) + getattr(self.term, color)(glyph) + self.bg_color,
            end="",
            flush=True,
        )

    def get_terminal_size(self) -> tuple[int, int]:
        """Return the current terminal size as (width, height)."""
        return self.term.width, self.term.height
