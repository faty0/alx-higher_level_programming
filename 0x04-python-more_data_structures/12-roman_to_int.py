#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if isinstance(roman_string, str):
        for i in range(0, len(roman_string)):
            if roman_string[i] == 'I':
                num += 1
            if roman_string[i] == 'V':
                num += 5
            if roman_string[i] == 'X':
                num += 10
            if roman_string[i] == 'L':
                num += 50
            if roman_string[i] == 'C':
                num += 100
            if roman_string[i] == 'D':
                num += 500
            if roman_string[i] == 'M':
                num += 1000
    return num
