#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = []
    result = 0

    for number in my_list:
        if number not in uniq_list:
            result = result + number
            uniq_list.append(number)
    
    return result
