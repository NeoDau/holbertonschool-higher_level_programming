#!/usr/bin/python3
"""shebang"""


def append_write(filename="", text=""):
    """äppend file"""
    with open(filename, "a", encoding="utf-8") as f:
        lenFile = f.write(text)
        return lenFile
