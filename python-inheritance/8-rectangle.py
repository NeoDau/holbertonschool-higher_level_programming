#!/usr/bin/python3
"""shebang"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseException):
    """Initializanding class"""
    def __init__(self, width, height):
        """Function"""
        self.__width = width
        self.__height = height
        super().__init__(width)
        super().__init__(height)
