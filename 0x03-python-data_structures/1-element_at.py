#!/usr/bin/python3

def element_at(my_list, idx):
    if not my_list or idx > len(my_list)-1 or idx < -1:
        return None

    return my_list[idx]
