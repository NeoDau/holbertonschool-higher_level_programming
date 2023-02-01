#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Initialize Squere"""

    def __init__(self, size=0):
        """Initialize class"""
        self.__size = size

    @property
    def size(self):
        """return area"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) == int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value >= 0:
            self.__size = value
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns areas"""
        return self.__size ** 2
