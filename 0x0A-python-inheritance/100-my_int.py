#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Represent a MyInt class using int."""
    def __eq__(self, __value):
        """Override == opeartor with != behavior."""
        return self.real != __value
    
    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
