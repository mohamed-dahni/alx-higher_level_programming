#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if ord(c) >= ord("a") and ord(c) < ord("z"):
            print("{}".format(chr(ord("A") + (ord(c) -ord("a")))), end="")
        print("{}".format(c), end="")


