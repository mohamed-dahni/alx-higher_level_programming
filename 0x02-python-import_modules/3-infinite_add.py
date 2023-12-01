#!/usr/bin/python3

from sys import argv


def main():
    result = 0

    for i, arg in enumerate(argv):

        result = result + int(arg)

    print("{}".format(result))


if __name__ == "__main__":
    main()
