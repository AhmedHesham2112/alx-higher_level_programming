#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in my_list:
        if isinstance(i, int):
            sum += i
    return sum
