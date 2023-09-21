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
        return self.width

    @size.setter
    def size(self, value):
        ''' a setter for size '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' assign atributes '''
        if len(args) != 0:
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.width = v
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        ''' returns the dictionary representation of a Square '''
        dict = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
        return dict

    def to_csv_string(self):
        '''Converts object attributes to a CSV string'''
        return "{},{},{},{}".format(self.id, self.size, self.x, self.y)

    @staticmethod
    def from_csv_string(csv_string):
        '''Parses a CSV string and returns a dictionary of attributes'''
        id, size, x, y = map(int, csv_string.split(','))
        return {'id': id, 'size': size, 'x': x, 'y': y}
