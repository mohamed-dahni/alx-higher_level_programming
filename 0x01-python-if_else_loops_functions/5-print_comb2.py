#!/usr/bin/python3

def main():
    for i in range(0, 100):
        if i == 99:
            print("{:02d}".format(i))
        else:
            print("{:02d}, ".format(i), end="")


if __name__ == "__main__":
    main()
