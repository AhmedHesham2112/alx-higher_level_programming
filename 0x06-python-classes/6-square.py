#!/usr/bin/python3
"""
Define a class Square.
"""


class Square():
    """
    Represent a Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize a new Square

        Args:
            size (int): the size of the new square.
            position (int, int): the position in the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if not (isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num > 0 for num in position)):
            raise TypeError("sposition must be a tuple of 2 positive integers")
        self.__size = size
        self.position = position

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
            return
        for i in range(self.__position[1]):
            print()
        for i in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """
        Get the current position of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
