#!/usr/bin/python3


def print_last_digit(number):
    if number < 0:
        number = -number
        while number >= 10:
            number = number % 10
    else:
        while number >= 10:
            number = number % 10
    print("{}".format(number), end="")
    return number
