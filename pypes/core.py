import time

from pipe import Pipe
from render import Renderer


class Animation:
    """Main class that runs the pipe animation."""

    def __init__(self, args) -> None:
        self.renderer = Renderer(args.bg_color)

        width, height = self.renderer.get_terminal_size()
        self.pipe = Pipe(
            width, height, args.turn_prob, args.border_mode, args.pipe_type
        )

        self.frame_time = 1 / args.fps

        self.running = False

    def loop(self) -> None:
        """Main animation loop that draws frames and updates the pipe."""
        self.running = True
        with self.renderer.term.fullscreen(), self.renderer.term.hidden_cursor():
            try:
                while self.running:
                    self.renderer.draw(
                        self.pipe.x, self.pipe.y, self.pipe.char, self.pipe.color
                    )
                    self.pipe.move()
                    self.pipe.turn()
                    time.sleep(self.frame_time)
            except KeyboardInterrupt:
                self.running = False
