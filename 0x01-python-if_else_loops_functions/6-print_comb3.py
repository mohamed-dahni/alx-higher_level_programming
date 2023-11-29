#!/usr/bin/python3

def get_reversed_num(number):
    return number[::-1]


def main():
    for i in range(0, 10):
        for j in range(i, 10):
            if i != j:
                print("{}{}, ".format(i, j), end="")

    print()

if __name__ == "__main__":
    main()
