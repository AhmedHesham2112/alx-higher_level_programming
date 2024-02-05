#!/usr/bin/python3
"""Define BaseGeometry Class"""


class BaseGeometry:
    """Represent base geometry."""
    def area(self):
        """raises exception that it is not implemented."""
        raise Exception("area() is not implemented")
