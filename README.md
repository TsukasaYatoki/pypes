# pypes

A terminal pipes animation, reimplementation of pipes.sh in Python.

## Install

```bash
pipx install git+https://github.com/TsukasaYatoki/pypes.git
```

Or for local development:

```bash
git clone git@github.com:TsukasaYatoki/pypes.git
cd pypes
pipx install -e .
```

## Usage

```
pypes [-h] [-f FPS] [-p TURN_PROB] [-n PIPE_NUM] [-l FRAME_LIMIT] [-t {0,1,2,3,4}] [-b BG_COLOR] [-m {reset,cycle}]
```

| Option | Default | Description |
|--------|---------|-------------|
| `-f, --fps` | 30 | Frames per second |
| `-p, --turn_prob` | 0.1 | Probability of pipe turning |
| `-n, --pipe_num` | 1 | Number of pipes |
| `-l, --frame_limit` | 0 | Frames before reset (0 = infinite) |
| `-t, --pipe_type` | 0 | Pipe character set (0-4) |
| `-b, --bg_color` | black | Background color (name or `#RRGGBB`) |
| `-m, --border_mode` | reset | Border behavior: `reset` or `cycle` |

Press `Ctrl+C` to exit.
