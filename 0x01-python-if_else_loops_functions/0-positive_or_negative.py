#!/usr/bin/python3
import random

number = random.randint(-10, 10)
description = ""

if number > 0:
    description = "positive"
elif number == 0:
    description = "zero"
else:
    description = "negative"

print(f"{number} is {description}")
