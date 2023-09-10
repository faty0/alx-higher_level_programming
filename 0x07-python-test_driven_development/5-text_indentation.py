#!/usr/bin/python3
'''a module that contains the function text_indentation
'''


def text_indentation(text):
    ''' a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    '''
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")

    marks = [".", "?", ":"]
    new = ""
    found = 0
    for i in range(0, len(text)):
        if ((i > 0) and (text[i - 1] in marks)):
            found = 1
            new += "\n\n"
            if (text[i] != " "):
                new += text[i]
        else:
            if (found == 1 and text[i] == " "):
                pass
            else:
                new += text[i]
                found = 0
    print(new)
