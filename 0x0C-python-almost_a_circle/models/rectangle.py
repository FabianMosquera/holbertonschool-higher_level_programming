#!/usr/bin/python3
"""
Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Returns rectangl with '#'
        """
        if self.__y != 0:
            for newline in range(self.__y):
                print()
        for row in range(self.__height):
            print((self.__x * " ") + (self.__width * '#'))

    def __str__(self):
        """Display the information of instances
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update Rectangle
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """A dictionary
        """
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
