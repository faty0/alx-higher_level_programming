#!/usr/bin/python3
''' a module  that contains the Rectangle class
'''
from models.base import Base


class Rectangle(Base):
    ''' class that inherits from Base

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle's position.
        __y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier of the rectangle.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Initializes a Rectangle object.
        '''
        super().__init__(id)

        ''' validating width '''
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        ''' validating height '''
        if (not isinstance(height, int)):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        ''' validating x '''
        if (not isinstance(x, int)):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        ''' validating y '''
        if (not isinstance(y, int)):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        ''' getter for the width attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' setter for the width attribute
        '''
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' getter for the height attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' setter for the height attribute
        '''
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        ''' getter for the x attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' setter for the x attribute
        '''
        if (not isinstance(value, int)):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        ''' getter for the y attribute
        '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' setter for the y attribute
        '''
        if (not isinstance(value, int)):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        ''' returns the area value of the Rectangle instance
        '''
        return (self.width * self.height)

    def display(self):
        ''' prints in stdout the Rectangle instance with the character #
        '''
        dis = "\n".join([(" " * self.x) + "#" * self.width] * self.height)
        print("\n" * self.y, end="")
        print(dis)
        return ("\n" * self.y) + dis

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        ''' assigns an argument to each attribute
        '''
        if len(args) != 0:
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle '''
        dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return dict

    def to_csv_string(self):
        '''Converts object attributes to a CSV string'''
        return "{},{},{},{},{}".format(
            self.id, self.width, self.height, self.x, self.y
        )

    @staticmethod
    def from_csv_string(csv_string):
        '''Parses a CSV string and returns a dictionary of attributes'''
        id, width, height, x, y = map(int, csv_string.split(','))
        return {
            'id': id, 'width': width, 'height': height, 'x': x, 'y': y
        }
