#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        if len(matrix[x]) > 0:
            print(end="")
        for a in range(len(x)):
            if a == len(x) - 1:
                print("{:d}".format(x[a]))
            else:
                print("{:d}".format(x[a]), end=" ")
