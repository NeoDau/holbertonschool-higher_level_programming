#!/usr/bin/python3
"""shebang"""


def pascal_triangle(n):
    """function triangle pascal"""
    nw = []
    lest = []
    if n <= 0:
        return nw
    for x in range(n):
        nw = [1]
        if x > 0:
            for i in range(x):
                nw.append(sum(lest[-1][i:i+2]))
        lest.append(nw)
    return (lest)
