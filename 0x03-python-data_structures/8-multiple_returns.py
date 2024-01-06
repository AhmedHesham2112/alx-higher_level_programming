#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_0 = ()
    if len(sentence) == 0:
        tuple_0 = 0, "None"
    else:
        tuple_0 = len(sentence), sentence[0]
    return tuple_0
