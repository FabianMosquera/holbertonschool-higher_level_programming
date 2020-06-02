#!/usr/bin/python3
"""
Square #1
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square data that inherits from Rectangle init `size`
    twice because width and height are same in squares
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate area
        """
        return self.__size * self.__size
