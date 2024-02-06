#!/usr/bin/python3
"""
Define a append_write function
"""


def append_write(filename="", text=""):
    """
    appends  a string to a text file (UTF8) and
    returns the number of characters written
    Args:
    filename: the name of the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
