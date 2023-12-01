#!/usr/bin/python3

from sys import argv


def main():
    result = 0

    for arg in argv:
        result = result + int(arg)

    print("{}".format(result))

if __name__ == "__main__":
    main()
