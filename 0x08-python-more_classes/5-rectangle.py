#!/usr/bin/python3
'''
    This module provides a class to represent a rectangle

    Classes:
        Rectangle: Class defining a rectangle

'''


class Rectangle:
    '''
    Class defining a rectangle

    Attributes:
            width (int, optional): the width of the rectangle
            height (int, optional): the height of the rectangle

    Methods:
            __init__: Constructor method for the Rectangle class
            __str__: Returns a string representation of Rectangle
            __repr__: Return a string representation of the object
            that can be used to recreate the object
            __del__: Print a message when an instance of Rectangle is deleted
            area: Calculate the area of a rectangle
            perimeter: Calculate the rectangle perimeter

    '''

    def __init__(self, width=0, height=0):
        '''
        Constructor method for the Rectangle class

        Args:
            width (int, optional): the width of the rectangle
            height (int, optional): the height of the rectangle

        '''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
        Calculate the area of a rectangle
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        '''
        Calculate the rectangle perimeter
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        '''
        Returns an user-friendly string representation of Rectangle
        '''
        if (self.__width != 0 and self.__height != 0):
            for i in range(self.__height):
                for _ in range(self.__width):
                    print("#", end="")
                if i < (self.__height - 1):
                    print()
        return ""

    def __repr__(self):
        '''
        return a string representation of the object
        that can be used to recreate the object
        '''
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        '''
        Print a message when an instance of Rectangle is deleted
        '''
        print("Bye rectangle...")
