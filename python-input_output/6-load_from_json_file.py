#!/usr/bin/python3
"""shebang"""
import json


def load_from_json_file(filename):
    """function create obj"""
    with open(filename, "r") as f:
        return json.loads(f)
