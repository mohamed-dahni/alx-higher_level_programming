#!/usr/bin/python3

def main():
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c not in "qe":
            print("{}".format(c), end="")


if __name__ == "__main__":
    main()
