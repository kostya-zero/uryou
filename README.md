# Uryou

<img src="icon.png" width=128 align="right">

Uryou is a CLI frontend for wttr.in website designed for easier interaction with `curl`.
It's written in Python and has functionallity that they need.
Uryou calls `curl` with url that have specific options like location, display option and more.
Also, `curl` is required to make application working.
You can use uryou by calling `main.py` file with `python` executable, or build a binary with [Pipe](https://gitlab.com/kostya-zero/pipe) (for Linux only).
You can get help by passing `--help` argument.

## Usage

```shell
# Shows a forecast information based on your location.
python main.py

# Shows help message
python main.py --help

# Shows a forecast information based on location you gave.
python main.py --location "London"

# Show detailed information about today's forecast
python main.py --detailed --today
```
