#!/usr/bin/python3

def main():
    for i in range(0, 10):
        for j in range(i, 10):
            if i != j:
                print("{}{}".format(i, j), end="")
                if i != 8 or j != 9:
                    print("{}".format(", "), end="")

    print()


if __name__ == "__main__":
    main()
