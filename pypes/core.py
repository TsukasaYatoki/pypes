import argparse
import time

from pipe import Pipe
from render import Renderer


class Animation:
    """Main class that runs the pipe animation."""

    def __init__(self, args: argparse.Namespace) -> None:
        self.renderer = Renderer()
        self.pipe = Pipe(
            self.renderer.max_x, self.renderer.max_y, args.turn_prob, args.border_method
        )

        self.frame_time = 1 / args.fps

        self.running = False

    def loop(self) -> None:
        """Main animation loop that draws frames and updates the pipe."""
        self.running = True
        with self.renderer.term.fullscreen(), self.renderer.term.hidden_cursor():
            try:
                while self.running:
                    self.renderer.draw(self.pipe)
                    self.pipe.move()
                    self.pipe.turn()
                    time.sleep(self.frame_time)
            except KeyboardInterrupt:
                self.running = False
