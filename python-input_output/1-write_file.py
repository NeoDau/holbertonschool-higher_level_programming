#!/usr/bin/python3
"""shebang"""


def write_file(filename="", text=""):
    """append file"""
    with open(filename, "a", encoding="utf-8") as f:
        lenFile = f.write(text)
        return lenFile
