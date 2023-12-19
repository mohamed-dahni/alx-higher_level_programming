#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_count = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            printed_count = printed_count + 1
        print()
    except IndexError:
        pass

    print("nb_print: {}".format(printed_count))

    return printed_count
