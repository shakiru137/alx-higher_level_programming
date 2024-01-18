#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    args_list = argv[1:]

    print("{} {}{}{}".format(num_args,
                              "argument" if num_args == 1 else "arguments",
                              ":" if num_args > 0 else ".",
                              "\n" if num_args > 0 else ""))

    for i, arg in enumerate(args_list, start=1):
        print("{}: {}".format(i, arg))
