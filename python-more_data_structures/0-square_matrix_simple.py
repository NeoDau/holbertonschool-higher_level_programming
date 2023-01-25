#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for x in matrix:
        for a in x:
            newMatrix.append(a ** 2)
    return newMatrix
        
