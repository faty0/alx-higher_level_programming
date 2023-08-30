#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    l = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            l += 1
        print()
    except IndexError:
        pass
    finally:
        return l
