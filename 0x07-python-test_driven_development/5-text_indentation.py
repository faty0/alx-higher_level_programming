#!/usr/bin/python3
'''a module that contains the function text_indentation
'''


def text_indentation(text):
    ''' a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    '''
    marks = [".", "?", ":"]
    for i in range(0, len(text)):
        print(text[i], end="")
        if (i > 0):
            if (text[i - 1] in marks):
                print()
                print()
