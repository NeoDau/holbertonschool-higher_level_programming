#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for x in matrix:
        new2 = []
        for a in x:
            new2.append(a ** 2)
        newMatrix.append(new2)
    return newMatrix
        
