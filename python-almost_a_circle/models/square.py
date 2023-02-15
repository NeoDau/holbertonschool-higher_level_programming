#!/usr/bin/python3
"""shebang"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class saquare"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, id, x, y)
  
    def __str__(self):
        """str init"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}")

    @property
    def size(self):
        return self.height


    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def area(self):
        """function area"""
        return self.size * self.size