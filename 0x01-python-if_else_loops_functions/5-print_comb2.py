#!/usr/bin/python3
for i in range(0, 10):
    j = 0
    while (j < 10):
        if (i == 9 and j == 9):
            print("99")
        else:
            print("{}{}".format(i, j), end=", ")
        j += 1
