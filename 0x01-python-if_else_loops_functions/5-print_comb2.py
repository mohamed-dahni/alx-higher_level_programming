#!/usr/bin/python3

def main():
    for i in range(0, 100):
        if i == 99:
            print()
        else:
            print("{}, ".format(i), end="")
    


if __name__ == "__main__":
    main()
