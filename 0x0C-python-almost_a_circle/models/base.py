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

    @classmethod
    def save_to_file(cls, list_objs=None):
        ''' writes the JSON string representation of list_objs to a file '''
        new_list = []
        filepath = "{}.json".format(cls.__name__)
        if list_objs is not None and list_objs:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
        with open(filepath, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the JSON string representation json_string '''
        my_list = []
        if isinstance(json_string, str) and json_string:
            my_list = json.loads(json_string)
        return my_list

    @classmethod
    def create(cls, **dictionary):
        ''' returns an instance with all attributes already set '''
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 3)
        if cls.__name__ == "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        ''' returns a list of instances '''
        filename = "{}.json".format(cls.__name__)
        my_objects = []
        try:
            with open(filename, 'r') as f:
                content = f.read()
            listof_dicts = cls.from_json_string(content)
            for dict in listof_dicts:
                obje = cls.create(**dict)
                my_objects.append(obje)
            return my_objects
        except FileNotFoundError as e:
            return my_objects
