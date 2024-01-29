#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle():
    """"Represent a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialized the width and height with 0, 0 or as given
        Args:
            width (int): width of the square
            hegiht (int): heghit of the square
        """
        type(self).number_of_instances += 1
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
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            self.__perimeter = 0
        else:
            return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """
        returns a printable string representation for rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rec += str(self.print_symbol)
            if i != self.__height - 1:
                rec += "\n"
        return rec

    def __repr__(self):
        """
        return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        r = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return r

    def __del__(self):
        """
        Print a message for every deletion of a Rectangle.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compares 2 rectangles and returns the biggest
        rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))
