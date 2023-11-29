#!/usr/bin/python3

def fizzbuzz():
    str_to_print = ""

    for i in range(0, 101):
        if (i % 3) == 0 and (i % 5) == 0:
            str_to_print += "FizzBuzz "
        elif (i % 3) == 0:
            str_to_print += "Fizz "
        elif (i % 5) == 0:
            str_to_print += "Buzz "
        else:
            str_to_print += f"{i} "

    print(str_to_print, end="")
