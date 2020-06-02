#!/usr/bin/python3
"""
Integer validator
"""


class BaseGeometry:
    """Contain the area(), integer_validator()
    """
    def area(self):
        """Not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
