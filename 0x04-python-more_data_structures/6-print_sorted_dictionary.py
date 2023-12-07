#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys_list = []
    for key in a_dictionary:
        keys_list.append(key)
    
    for key in keys_list.sort():
        print("{}: {}".format(key, a_dictionary[key]))
