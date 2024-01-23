#!/usr/bin/python3
"""
Define a class Square.
"""


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
        return self.__size * self.__size

    @property
    def size(self):
        """
        Get the current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Print a square
        """
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
