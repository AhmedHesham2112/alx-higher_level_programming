#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number

while digit >= 10 or digit <= -10:
    digit = digit % 10

if digit < 6 and digit != 0:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
elif digit == 0:
    print(f"Last digit of {number} is {digit} and is 0")
else:
    print(f"Last digit of {number} is {digit} and is greater than 5")
