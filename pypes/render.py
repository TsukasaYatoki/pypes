from contextlib import contextmanager
from dataclasses import dataclass

# ANSI Escape Sequences
ESC = "\033"
CLEAR = f"{ESC}[2J"
HOME = f"{ESC}[H"
HIDE_CURSOR = f"{ESC}[?25l"
SHOW_CURSOR = f"{ESC}[?25h"
ALTSCREEN_ON = f"{ESC}[?1049h"
ALTSCREEN_OFF = f"{ESC}[?1049l"


@dataclass
class Glyph:
    """Represents a single character to be drawn at specific coordinates with a color."""

    x: int
    y: int
    char: str
    color: str


class Renderer:
    """Small rendering helper that writes pipe frames to the terminal."""

    _color_disc = {
        "black": 0,
        "red": 1,
        "green": 2,
        "yellow": 3,
        "blue": 4,
        "magenta": 5,
        "cyan": 6,
        "white": 7,
    }

    def __init__(self, bg_color: str = "black") -> None:
        self.bg_ansi = self._get_color_ansi(bg_color, background=True)

        self.clear()

    @contextmanager
    def fullscreen(self):
        """Context manager to enter alternate screen and hide cursor."""
        try:
            print(f"{ALTSCREEN_ON}{HIDE_CURSOR}", end="", flush=True)
            yield
        finally:
            print(f"{ALTSCREEN_OFF}{SHOW_CURSOR}", end="", flush=True)

    def _get_color_ansi(self, color: str, background: bool) -> str:
        """Convert color str to ANSI code."""
        layer = 4 if background else 3

        if color.startswith("#"):
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
            color_code = f"8;2;{r};{g};{b}"
        else:
            color_code = self._color_disc.get(color)

        return f"{ESC}[{layer}{color_code}m"

    def _get_pos_ansi(self, x: int, y: int) -> str:
        """Convert (x, y) coordinates to ANSI cursor position code."""
        return f"{ESC}[{y + 1};{x + 1}H"

    def clear(self) -> None:
        """Clear the screen and move the cursor home before drawing frames."""
        print(f"{HOME}{CLEAR}{self.bg_ansi}", end="", flush=True)

    def draw(self, glyphs: list[Glyph]) -> None:
        """Draw a list of Glyphs to the terminal."""
        output = []
        for glyph in glyphs:
            move_ansi = self._get_pos_ansi(glyph.x, glyph.y)
            fg_ansi = self._get_color_ansi(glyph.color, background=False)
            output.append(f"{self.bg_ansi}{move_ansi}{fg_ansi}{glyph.char}")

        print("".join(output), end="", flush=True)
