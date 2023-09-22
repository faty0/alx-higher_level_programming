#!/usr/bin/python3
''' a module that contains a class Rectangle '''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    ''' a class Rectangle that inherits from BaseGeometry '''

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
