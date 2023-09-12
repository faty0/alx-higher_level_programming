#!/usr/bin/python3
''' module that contains the function append_after
'''


def append_after(filename="", search_string="", new_string=""):
    '''  inserts a line of text to a file, after each line
    containing a specific string
    '''
    content = ""
    with open(filename, 'r', encoding="utf-8") as f:
        while True:
            line_read = f.readline()
            content += line_read
            if search_string in line_read:
                content += new_string
            if line_read == "":
                break
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(content)
