#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    d = (number % 10) if (number > 10) else number
    print("{}".format(d), end="")
    return d
