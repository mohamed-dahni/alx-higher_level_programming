#!/usr/bin/python3
import random

number = random.randint(-10, 10)
answer = ""

if number > 0:
    answer = "positive"
elif number == 0:
    answer = "zero"
else:
    answer = "negative"

print(f"{number} is {answer}")
