#!/usr/bin/python3
"""shebang"""


class Rectangle:
    """initializanding """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            wh = (self.__width * 2) + (self.__height * 2)
            return wh

    def __str__(self):
        printHa = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for x in range(self.__height):
            for i in range(self.__width):
                printHa += "#"
            printHa += "\n"
        return printHa[:-1]

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        """width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
