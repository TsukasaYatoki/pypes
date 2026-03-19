import random
from enum import IntEnum


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Pipe:
    """A single animated pipe segment that moves across the terminal."""

    _vectors = {
        Direction.UP: (0, -1),
        Direction.RIGHT: (1, 0),
        Direction.DOWN: (0, 1),
        Direction.LEFT: (-1, 0),
    }
    _char = "┃┏ ┓┛━┓  ┗┃┛┗ ┏━"

    def __init__(
        self, max_x: int, max_y: int, p_turn: float = 0.9, border: str = "reset"
    ) -> None:
        self.max_x = max_x
        self.max_y = max_y
        self.border = border

        self.p_turn = p_turn
        self.p_straight = 1 - 2 * p_turn

        self._reset()

    def _reset(self) -> None:
        """Place the pipe on a random edge and choose an initial direction."""
        self.direction = random.choice(list(Direction))

        if self.direction == Direction.UP:
            self.x = random.randrange(self.max_x)
            self.y = self.max_y - 1
        elif self.direction == Direction.RIGHT:
            self.x = 0
            self.y = random.randrange(self.max_y)
        elif self.direction == Direction.DOWN:
            self.x = random.randrange(self.max_x)
            self.y = 0
        else:
            self.x = self.max_x - 1
            self.y = random.randrange(self.max_y)

        self.char = self._char[self.direction * 4 + self.direction]

    def _inbounds(self) -> bool:
        """Check if the pipe is within the terminal bounds."""
        return 0 <= self.x < self.max_x and 0 <= self.y < self.max_y

    def move(self) -> None:
        """Advance one step in the current direction, resetting at the border."""
        dx, dy = self._vectors[self.direction]
        self.x += dx
        self.y += dy

        if not self._inbounds():
            if self.border == "cycle":
                self.x %= self.max_x
                self.y %= self.max_y
            else:
                self._reset()

    def turn(self) -> None:
        """Randomly keep going straight or turn left/right, then update the glyph."""
        choices = [self.direction, (self.direction + 1) % 4, (self.direction - 1) % 4]
        weights = [self.p_straight, self.p_turn, self.p_turn]

        next_direction = random.choices(choices, weights)[0]
        self.char = self._char[self.direction * 4 + next_direction]

        self.direction = next_direction
