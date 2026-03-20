import random
from enum import IntEnum


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    @property
    def vector(self):
        vectors = {
            Direction.UP: (0, -1),
            Direction.RIGHT: (1, 0),
            Direction.DOWN: (0, 1),
            Direction.LEFT: (-1, 0),
        }
        return vectors[self]


class Pipe:  # TODO: implement trails animation like rainbow or fade
    """A single animated pipe segment that moves across the terminal."""

    _char_set = [
        "┃┏ ┓┛━┓  ┗┃┛┗ ┏━",
        "│┌ ┐┘─┐  └│┘└ ┌─",
        "╿┍ ┑┚╼┒  ┕╽┙┖ ┎╾",
        "║╔ ╗╝═╗  ╚║╝╚ ╔═",
        "│╭ ╮╯─╮  ╰│╯╰ ╭─",
    ]
    _color_set = ["red", "green", "yellow", "blue", "magenta", "cyan"]

    def __init__(
        self,
        max_x: int,
        max_y: int,
        p_turn: float = 0.1,
        border: str = "reset",
        type: int = 0,
    ) -> None:
        self.max_x = max_x
        self.max_y = max_y
        self.border = border
        self.type = type

        self.p_turn = p_turn
        self.p_straight = 1 - p_turn

        self._reset()

    def _reset(self) -> None:
        """Initialize the pipe at a random edge and color."""
        self.direction = random.choice(list(Direction))

        match self.direction:
            case Direction.UP:
                self.x = random.randrange(self.max_x)
                self.y = self.max_y - 1
            case Direction.RIGHT:
                self.x = 0
                self.y = random.randrange(self.max_y)
            case Direction.DOWN:
                self.x = random.randrange(self.max_x)
                self.y = 0
            case Direction.LEFT:
                self.x = self.max_x - 1
                self.y = random.randrange(self.max_y)

        self.char = self._get_char(self.direction)
        self.color = random.choice(self._color_set)

    def _inbounds(self) -> bool:
        """Check if the pipe is within the terminal bounds."""
        return 0 <= self.x < self.max_x and 0 <= self.y < self.max_y

    def _get_char(self, next: Direction) -> str:
        """Get the appropriate pipe character based on the current and next directions."""
        return self._char_set[self.type][(self.direction << 2) | next]

    def _move(self) -> None:
        """Advance one step in the current direction, resetting at the border."""
        dx, dy = self.direction.vector
        self.x += dx
        self.y += dy

        if not self._inbounds():  # TODO: add more border modes like bounce or wrap
            if self.border == "reset":
                self._reset()
            elif self.border == "cycle":
                self.x %= self.max_x
                self.y %= self.max_y

    def _turn(self) -> None:
        """Randomly keep going straight or turn left/right, then update the glyph."""
        choices = [
            self.direction,
            Direction((self.direction + 1) % 4),
            Direction((self.direction - 1) % 4),
        ]
        weights = [self.p_straight, self.p_turn / 2, self.p_turn / 2]

        next_direction = random.choices(choices, weights)[0]

        self.char = self._get_char(next_direction)
        self.direction = next_direction

    def update(self) -> None:
        """Move and turn the pipe for the next frame."""
        self._move()
        self._turn()
