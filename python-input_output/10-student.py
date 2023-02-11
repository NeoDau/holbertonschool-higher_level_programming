#!/usr/bin/python3
"""shebang"""


class Student:
    """create class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs == None:
            return self.__dict__
        else:
            newDict = {}
            for x in attrs:
                if x in self.__dict__.keys():
                    newDict[x] = self.__dict__[x]
                return newDict
