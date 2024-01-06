#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len == 0:
        tuple_0 = (length, None)
        return tuple_0
    else:
        tuple_0 = (length, sentence[0])
        return tuple_0
