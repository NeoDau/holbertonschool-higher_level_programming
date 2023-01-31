#!/usr/bin/python3
""" Write a class Square that defines a square """
class Square:
    """ Declarandin square whit size """
    def __init__(self, size = 0):
        """ initialize squere """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise TypeError ("size must be an integer")
        else:
            raise ValueError ("size must be >= 0")
             
            