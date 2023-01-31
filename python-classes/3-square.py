#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    def area (self):
        area = self.__size * self.__size
        return (area)