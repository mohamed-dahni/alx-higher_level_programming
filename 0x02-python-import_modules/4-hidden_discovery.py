#!/usr/bin/python3
import sys
import hidden_4

if __name__ != "__main__":
    exit()

for i in dir(hidden_4):
    if not i.startswith("__"):
        print(i)
