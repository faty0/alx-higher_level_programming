#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(0, list_length):
            try:
                res = my_list_1[i] / my_list_2[i]
            except (TypeError, ValueError):
                print("wrong type")
                res = 0
            except ZeroDivisionError:
                print("division by 0")
                res = 0
            finally:
                new_list.append(res)
    except IndexError:
        print("out of range")
        res = 0
        new_list.append(res)
    finally:
        return new_list
