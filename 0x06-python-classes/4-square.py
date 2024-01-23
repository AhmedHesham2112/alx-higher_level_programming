#!/usr/bin/python3
"""
Define a class Square.
"""


from typing import Any


class Square():
    """
    Represent a Square
    """
    def __init__(self, size=0):
        """
        initialize a new Square

        Args:
            size (int): the size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        returns the area of the square
        """
        self.area = self.__size * self.__size
        return self.area

    @property
    def size(self):
        """
        Get the current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the current size of the square.

        Args:
            value (int): the new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
