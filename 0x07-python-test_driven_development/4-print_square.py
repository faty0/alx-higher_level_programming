#!/usr/bin/python3
''' a module that contains the function print_square
'''


def print_square(size):
    ''' a function that prints a square with the character #
    '''
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print()
