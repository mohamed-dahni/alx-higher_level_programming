#!/usr/bin/python3

def get_reversed_num(number):
    return number[::-1]


def main():
    unique_list = []

    for i in range(0, 100):
        num = "{:02d}".format(i)
        if num[0] != num[1] and num not in unique_list and get_reversed_num(num) not in unique_list:
            unique_list.append(num)

    print("{}".format(", ".join(unique_list)))


if __name__ == "__main__":
    main()
