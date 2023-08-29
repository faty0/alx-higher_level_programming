#!/usr/bin/python3
"""
This module provides a Square class that defines a square.

Classes:
    Square

Functions:
    None

Variables:
    None
"""


class Square:
    """
    an empty class Square that defines a square

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__: Initializes a Square object with a given size parameter
        area: Calculates the area of a square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of a square
        """
        return (self.__size * self.__size)
