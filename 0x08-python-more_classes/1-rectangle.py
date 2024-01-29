#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle():
    """"Represent a Rectangle"""
    pass

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
        return(self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def width(self):
        """
        Get the current width of the rectangle.
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        self.__width = value
