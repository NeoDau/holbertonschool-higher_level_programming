#!/usr/bin/python3
"""shebang"""
import json


def save_to_json_file(my_obj, filename):
    """function save txt"""
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
