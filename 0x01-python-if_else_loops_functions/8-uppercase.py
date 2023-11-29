#!/usr/bin/python3

def uppercase(str):
    for c in str:
        char_number = ord(c)
        if ord(c) >= ord("a") and ord(c) < ord("z"):
            print("{}".format(chr(ord(c) - ord("A"))), end="")
        print("{}".format(c), end="")


