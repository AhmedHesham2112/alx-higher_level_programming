#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 1:
        i = i-ord('a')+ord('A')
    print("{}".format(chr(i)), end="")
