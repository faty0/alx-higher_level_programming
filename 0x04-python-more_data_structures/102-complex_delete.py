#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    finished = False
    while finished is False:
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break
            finished = True
    return a_dictionary
