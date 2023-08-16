#!/usr/bin/python3
def weight_average(my_list=[]):
    mul_couple = 0
    sum_weight = 0
    if my_list:
        for tup in my_list:
            mul_couple += (tup[0] * tup[1])
            sum_weight += tup[1]
        return (mul_couple / sum_weight)
    return 0
