#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        for i in my_list:
            if my_list.index(i) == idx:
                my_list[my_list.index(i)] = element
    return my_list
