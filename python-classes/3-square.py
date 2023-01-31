#!/usr/bin/python3
""" Write a class Square that defines a square """


class Square:
    """ Initialize square """
    def __init__(self, size=0):
        self.__size = size
    """ Initialize area """
    def area(self):
        area = self.__size * self.__size
        return (area)
