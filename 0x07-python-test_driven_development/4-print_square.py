#!/usr/bin/python3
"""
Define a Print Square method.
"""


def print_square(size):
        """
        initialize a new Square

        Args:
            size (int): the size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print()
