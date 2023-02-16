#!/usr/bin/python3
"""shebang"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class saquare"""
    def __init__(self, size, x=0, y=0, id=None):
        """init new instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str init"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.height = value
        self.width = value
