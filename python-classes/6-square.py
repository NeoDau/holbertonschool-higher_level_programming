#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Initialize Squere"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize class"""
        self.__size = size
        self.__position = position

        if len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(self.__position[0])) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(self.__position[1])) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (self.__position[0] < 0 or self.__position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """return area"""
        return self.__size

    @property
    def position(self):
        """Return position Square"""
        return self.__position

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

    def my_print(self):
        """Print square"""

        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for a in range(self.__size):
                    print("#", end="")
                if i+1 < self.__size:
                    print()
            print()
