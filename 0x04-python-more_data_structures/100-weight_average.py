#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    num = 0
    for tub in my_list:
        sum += tub[0] * tub[1]
        num += tub[1]
    return sum/num
