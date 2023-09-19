#!/usr/bin/python3
''' a module that contains the Base class
'''


class Base:
    ''' a class that is the “base” of all other classes in this project.
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
