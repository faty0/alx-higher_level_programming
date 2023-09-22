#!/usr/bin/python3
''' a module that contains the BaseGeometry class
'''


class BaseGeometry:
    ''' class that defines geometry
    '''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (not isinstance(value, int) or value is True):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
