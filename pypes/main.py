import time

from blessed import Terminal
from pipe import Pipe
from render import Canvas


def main():
    term = Terminal()
    canvas = Canvas(term)
    canvas.clear()

    pipe = Pipe(term.width, term.height)

    with term.fullscreen(), term.hidden_cursor():
        while True:
            canvas.draw(pipe)
            pipe.move()
            pipe.turn()
            time.sleep(0.1)


if __name__ == "__main__":
    main()
