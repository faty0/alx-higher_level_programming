#!/usr/bin/python3
''' a module  that contains the Rectangle class
'''


class Rectangle(Base):
    ''' class that inherits from Base
    '''
    def __init__(self, width, height, x=0, y=0, id=None): 
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
