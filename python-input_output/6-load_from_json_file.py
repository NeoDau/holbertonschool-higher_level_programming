#!/usr/bin/python3
"""shebang"""
import json


def load_from_json_file(filename):
    """function create obj"""
    with open(filename) as f:
        strJson = f.read()
        return json.loads(strJson)
