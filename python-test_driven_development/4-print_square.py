#!/usr/bin/python3
"""shebang"""


def print_square(size):
    """print Square"""
    if not isinstance(size, int) or isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for a in range(size):
            print("#", end="")
        print("")
