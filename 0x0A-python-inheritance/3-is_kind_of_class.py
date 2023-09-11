#!/usr/bin/python3
''' a module containning is_kind_of__class function
'''


def is_kind_of_class(obj, a_class):
    ''' check if an object is an instance of, or if the
    object is an instance of a class that inherited
    from, the specified class
    '''
    return (isinstance(obj, a_class))
