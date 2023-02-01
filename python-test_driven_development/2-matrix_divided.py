#!/usr/bin/python3
"""shebang"""


def matrix_divided(matrix, div):
    """div matrix"""
    ERR = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(ERR)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    newMatrix = []
    for x in matrix:
        new = []
        if len(matrix[0]) != len(x):
            raise TypeError("Each row of the matrix must have the same size")
        for a in x:
            if type(a) is not int and type(a) is not float:
                raise TypeError(ERR)
            result = a / div
            new.append(round(result, 2))
        newMatrix.append(new)
    return newMatrix
