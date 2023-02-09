#!/usr/bin/python3
"""shebang"""


class BaseGeometry:
    """Class BaseGeometry"""
    
    def area(self):
        """initializandig"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
