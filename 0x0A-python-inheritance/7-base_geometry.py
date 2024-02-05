#!/usr/bin/python3
"""Define BaseGeometry Class"""


class BaseGeometry:
    """Represent base geometry."""
    def area(self):
        """raises exception that it is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
