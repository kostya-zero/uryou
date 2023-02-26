from argparse import ArgumentParser


def parse_args(argv: list):
    parser = ArgumentParser()

    parser.add_argument("-l", "--location", type=str,
                        help="Show forecast in specified.")
    parser.add_argument("-d", "--detailed", action='store_true', 
                        help="Show detailed information about forecast.")
    parser.add_argument("-b", "--border", action='store_true',
                        help="Add border around the message.")
    parser.add_argument("-t", "--today", action='store_true',
                        help="Show current and today forecast.")
    parser.add_argument("-T", "--today-and-tomorrow", action='store_true',
                        help="Show current, today and tomorrow forecast.")
    parser.add_argument("-n", "--no-color", action='store_true',
                        help="Dont use colors in output.")

    args = parser.parse_args(argv)
    return args

