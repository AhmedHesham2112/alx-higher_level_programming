#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square using Rectangle."""
    def __init__(self, size):
        """Intialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[Square] "
        string += str(self.__size) + "/" + str(self.__size)
        return string