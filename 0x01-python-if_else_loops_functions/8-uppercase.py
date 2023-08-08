#!/usr/bin/python3
def uppercase(str):
    new = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            new = new + chr(ord(c) - 32)
        else:
            new = new + c
    print(new)
