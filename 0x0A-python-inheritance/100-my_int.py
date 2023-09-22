#!/usr/bin/python3
''' a module that contains MyInt class '''


class MyInt(int):
    ''' a class that inherits from int '''

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value != other

    def __ne__(self, other):
        return self.value == other
