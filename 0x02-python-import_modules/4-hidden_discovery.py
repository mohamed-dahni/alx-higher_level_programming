#!/usr/bin/python3

if __name__ == "__main__":
    for i in dir():
        if not i.startswith("__"):
            print(i)
