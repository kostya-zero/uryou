# Uryou

<img src="icon.png" width=128 align="right">

Uryou is a CLI frontend for wttr.in designed for easier interaction with website by sending requests via `curl`.
It is written in Python and has the functionality they need.
Uryou calls `curl` with URL that has certain parameters such as location, display parameter, and more.
In order `curl` is required for application to work.
You can use Uryou by calling `main.py` file with `python` executable, or build a binary with [Pipe](https://gitlab.com/kostya-zero/pipe) (for Linux only).
You can get help by passing `--help` argument.

## Usage

```shell
# Shows forecast information based on your location.
python main.py

# Shows help message.
python main.py --help

# Shows forecast information based on the location you specified.
python main.py --location "London"

# Shows detailed information about today's forecast.
python main.py --detailed --today
```
