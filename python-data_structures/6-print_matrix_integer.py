#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        return
    for x in range(len(matrix)):
        for a in range(len(matrix[x])):
            print("{:d}".format(matrix[x][a]), end=" ")
            if a < len(matrix[x]) - 1:
                print(end="")
        print()
