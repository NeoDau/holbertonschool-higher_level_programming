#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for x in matrix:
        for a in range(len(x)):
            if a == len(x) - 1:
                print("{:d}".format(x[a]))
            else:
                print("{:d}".format(x[a]), end=" ")
