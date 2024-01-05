#!/usr/bin/python3

import sys

argsnum = len(sys.argv) -1

if argsnum <= 0:
    print("0 arguments.")
elif argsnum == 1:
    print("1 argument:")
else:
    print(f"{argsnum} arguments:")

for i in range(1, argsnum + 1):
    print(f"{i}: {sys.argv[i]}")
