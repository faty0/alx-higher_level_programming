#!/usr/bin/python3
''' module that contains the class Student
'''


class Student:
    ''' class that defines a student
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict = self.__dict__
        dict1 = {}
        if (isinstance(attrs, list) and
                all(isinstance(att, str) for att in attrs)):
            for k, v in dict.items():
                if k in attrs:
                    dict1[k] = v
            return dict1
        return dict

    def reload_from_json(self, json):
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
