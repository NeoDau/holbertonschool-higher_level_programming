#!/usr/bin/python3
"""shebang"""


def read_file(filename=""):
    """Function read"""
    with open(filename, encoding="utf-8") as f:
        x = f.read()
        print(x, end="")
