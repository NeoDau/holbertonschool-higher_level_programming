#!/usr/bin/python3
"""base module"""
import json


class Base:
    """decaraion class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function dict to json str"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json save in file"""
        sv = cls.__name__ + ".json"
        tp = []

        if list_objs:
            for x in list_objs:
                tp.append(x.to_dictionary())
        with open(sv, "w") as f:
            f.write(Base.to_json_string(tp))

    def from_json_string(json_string):
        """function rts list of the json str"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """function return set already"""
        if cls.__name__ == "Rectangle":
            x = cls(1, 1)
        if cls.__name__ == "Square":
            x = cls(1)
        x.update(**dictionary)
        return x 
