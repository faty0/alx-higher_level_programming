#!/usr/bin/python3
"""a function that calculates the sum
"""


def add_integer(a, b=98):
    """ a fucntion that returns the integer
        sum of two given inputs
    Args:
        a (int/float): first input
        b (int/float, optional): second input. Defaults to 98.
    Return:
    returns the sum
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
