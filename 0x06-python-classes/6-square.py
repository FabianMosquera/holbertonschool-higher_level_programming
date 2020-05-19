#!/usr/bin/python3
"""
Square Class: Printing a square with # and coordinates
"""


class Square:
    """ class Square that defines a square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize attributes"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size with safe Assignment"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property.position
    def position(self):
        """ gets the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the new position """
        msg = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(msg)
        elif len(value) != 2:
            raise TypeError(msg)
        else:
            for k in value:
                if k < 0:
                    raise TypeError(msg)
                elif type(k) is not int:
                    raise TypeError(msg)
        self.__position = value

    def area(self):
        """ Return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()
        else:
            print()
