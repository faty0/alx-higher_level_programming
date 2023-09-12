#!/usr/bin/python3
''' module that contains he function class_to_json
'''


def class_to_json(obj):
    ''' returns the dictionary description
    '''
    return obj.__dict__
