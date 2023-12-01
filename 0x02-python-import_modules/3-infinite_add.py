#!/usr/bin/python3

from sys import argv


def main():
    result = 0

    for arg in enumerate(argv[1:]):
        result = result + int(arg)

    print("{}".format(result))


if __name__ == "__main__":
    main()
