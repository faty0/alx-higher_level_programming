#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)[-1]
last = int(last)
if number < 0:
    last *= -1
if last > 5:
    description = "greater than 5"
if last == 0:
    description = "0"
if last < 6 and last != 0:
    description = "less than 6 and not 0"
print("Last digit of {:d} is {:d} and is {}".format(number, last, description))
