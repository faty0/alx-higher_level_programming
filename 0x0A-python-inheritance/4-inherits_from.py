#!/usr/bin/python3
''' a module containning inherits_from function
'''


def inherits_from(obj, a_class):
    ''' checks if if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class
	'''
    return issubclass(type(obj), a_class)
