#!/usr/bin/python3

from sys import argv


def main():
    print("{} arguments.".format(len(argv)))
          
    for i, arg in enumerate(argv):
        print("{}: {}".format(i + 1, arg))


if __name__ == "__main__":
    main()
