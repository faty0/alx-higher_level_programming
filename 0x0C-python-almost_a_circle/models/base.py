#!/usr/bin/python3
''' a module that contains the Base class
'''
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''  returns the JSON string representation of list_dictionaries '''
        if not isinstance(list_dictionaries, list) or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
