#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle():
    """"Represent a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        initialized the width and height with 0, 0 or as given
        
        Args:
            width (int): width of the square
            hegiht (int): heghit of the square
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        Get the current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Get the current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
