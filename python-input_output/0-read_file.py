#!/usr/bin/python3
"""shebang"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        f = read_file("my_file_0.txt")
        print(f)
