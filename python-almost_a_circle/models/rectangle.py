#!/usr/bin/python3
"""shebang."""
from models.base import Base


class Rectangle(Base):
    """class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """function area"""
        return self.__height * self.__width

    def display(self):
        """function print #"""
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for a in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """function str"""
        x = self.__x
        y = self.__y
        h = self.__height
        w = self.__width
        return (f"[Rectangle] ({self.id}) {x}/{y} - {w}/{h}")

    def update(self, *args, **kwargs):
        """function update"""
        names = ("id", "width", "height", "x", "y")

        if args:
            for key, value in zip(names, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dict f*!k"""
        x = self.x
        y =self.y
        __id = self.id
        height = self.height
        width = self.width

        newDict = {"x": x, "y": y, "id": __id, "height": height, "width": width}
