#!/usr/bin/python3
''' a module that contains the class square '''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    ''' a class Square that inherits from Rectangle '''

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
