import argparse
import shutil
import time

from pipe import Pipe
from render import Glyph, Renderer


class Animation:
    """Main class that runs the pipe animation."""

    def __init__(self, args: argparse.Namespace) -> None:
        self.frame_time = 1 / args.fps
        self.pipe_num = args.pipe_num
        self.turn_prob = args.turn_prob
        self.border_mode = args.border_mode
        self.pipe_type = args.pipe_type
        self.frame_limit = args.frame_limit

        self.renderer = Renderer(args.bg_color)
        self.pipes = self._init_pipes()
        self.frame_count = 0

        self.running = False

    def _init_pipes(self) -> list[Pipe]:
        """Initialize pipes with random positions and directions."""
        width, height = shutil.get_terminal_size()
        pipes = [
            Pipe(width, height, self.turn_prob, self.border_mode, self.pipe_type)
            for _ in range(self.pipe_num)
        ]
        return pipes

    def _get_glyphs(self) -> list[Glyph]:
        """Convert current pipe states to a list of Glyphs for rendering."""
        glyphs = [
            Glyph(x=pipe.x, y=pipe.y, char=pipe.char, color=pipe.color)
            for pipe in self.pipes
        ]
        return glyphs

    def loop(self) -> None:
        """Main animation loop that draws frames and updates the pipe."""
        self.running = True
        with self.renderer.fullscreen():
            try:
                while self.running:
                    for pipe in self.pipes:  # TODO: draw once per frame, not per pipe
                        glyphs = self._get_glyphs()
                        self.renderer.draw(glyphs)
                        pipe.update()

                    self.frame_count += 1
                    time.sleep(self.frame_time)

                    if self.frame_limit > 0 and self.frame_count >= self.frame_limit:
                        self.renderer.clear()
                        self.pipes = self._init_pipes()
                        self.frame_count = 0
            except KeyboardInterrupt:
                self.running = False
