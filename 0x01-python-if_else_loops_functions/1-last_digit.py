#!/usr/bin/python3

import random

def get_last_digit(number):
    """ Determine the last digit of a number """
    last_digit = abs(number) % 10
    if number < 0:
        last_digit = -last_digit

def main():
    number = random.randint(-10000, 10000)
    last_digit = get_last_digit(number)
    description = ""



    if last_digit > 5:
        description = "greater than 5"
    elif last_digit == 0:
        description = "0"
    else:
        description = "less than 6 and not 0"

    print(f"Last digit of {number} is {last_digit} and is {description}")
