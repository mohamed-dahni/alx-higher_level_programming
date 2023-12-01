#!/usr/bin/python3

from sys import argv


def main():
    arg_count = len(argv) - 1
    print("{} arguments.".format(arg_count))
          
    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
