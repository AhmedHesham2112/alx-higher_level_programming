#!/usr/bin/python3


def remove_char_at(str, n):
    i = 0
    op = ""
    for c in str:
        if i == n:
            i += 1
            continue
        op += c
        i += 1
    return op
