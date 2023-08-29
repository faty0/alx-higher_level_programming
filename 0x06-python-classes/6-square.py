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
        __position (tuple): The position of the square

    Methods:
        __init__: Initializes a Square object with a given size parameter
        area: Calculates the area of a square
        my_print: Prints in stdout the square with the character #
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple) or
           (position[0] < 0 or position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """
        Calculates the area of a square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or (value[0] < 0 or value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        if (self.__position[0] > 0):
            for i in range(0, self.__position[1]):
                print()
        for i in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
