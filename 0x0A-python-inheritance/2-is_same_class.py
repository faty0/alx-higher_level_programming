#!/usr/bin/python3
''' a module containning is_same_class function
'''


def is_same_class(obj, a_class):
    ''' check if an object is an instance of the specified class
    '''
    if type(obj) == a_class:
        return True
    return False
