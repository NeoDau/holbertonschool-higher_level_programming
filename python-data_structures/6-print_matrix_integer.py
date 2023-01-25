#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        if len(matrix) == 0:
            print("{:d}".format(matrix), end="")
        for a in range(len(x)):
            if a == len(x) - 1:
                print("{:d}".format(x[a]))
            else:
                print("{:d}".format(x[a]), end=" ")
