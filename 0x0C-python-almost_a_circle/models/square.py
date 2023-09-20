#!/usr/bin/python3
''' a module that contains the Square class
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square class inheriting from class Rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        ''' a getter for size '''
        return self.__width

    @size.setter
    def size(self, value):
        ''' a setter for size '''
        self.__width = value
        self.__height = value
