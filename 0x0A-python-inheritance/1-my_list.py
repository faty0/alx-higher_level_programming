#!/usr/bin/python3
''' a module cntainning the Mylist class
'''


class MyList(list):
    ''' class inhereting from list
    '''

    def print_sorted(self):
        sorted_l = sorted(self)
        print(sorted_l)
