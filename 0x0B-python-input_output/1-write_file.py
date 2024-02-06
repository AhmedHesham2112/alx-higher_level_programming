#!/usr/bin/python3
"""
Define a write_file function
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and
    returns the number of characters written
    Args:
    filename: the name of the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
