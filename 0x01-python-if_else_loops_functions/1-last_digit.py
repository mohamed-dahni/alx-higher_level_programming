#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
last_digit = number % 10
answer = ""

if last_digit > 5:
    answer = "and is greater than 5"
elif last_digit == 0:
    answer = "and is 0"
else:
    answer = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} and {answer}")
