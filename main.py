import sys
from include.argparser import parse_args
from os import system


def main():
    sys.dont_write_bytecode = True
    cmd = sys.argv
    cmd.pop(0)
    url = "https://wttr.in/"

    if len(cmd) == 0:
        system(f"curl {url}?0")
        return 
    args = parse_args(cmd)

    if args.location != None:
        url += args.location
    
    url += "?"

    if not args.detailed:
        url += "0"

    if args.border:
        url += "p"

    if args.today:
        url += "1"

    if args.today_and_tomorrow:
        url += "2"

    if args.no_color:
        url += "T"

    system(f"curl {url}")

if __name__ == "__main__":
    main()

