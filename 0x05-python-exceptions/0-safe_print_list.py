#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_count = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]))
            printed_count = printed_count + 1
        print()
    except IndexError as er:
        print(er)

    print("nb_print: {}".format(printed_count))
