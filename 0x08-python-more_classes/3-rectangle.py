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

    def area(self):
        """
        returns the rectangle area.
        """
        self.__area = self.__width * self.__height
        return self.__area

    def perimeter(self):
        """
        returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            self.__perimeter = 0
        else:
            self.__perimeter = 2 * self.__width + 2 * self.__height
        return self.__perimeter

    def __str__(self):
        """
        returns a printable string representation for rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rec += "#"
            if i != self.__height - 1:
                rec += "\n"
        return rec
