#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) < 1:
        print("$")
        return

    for row in matrix:
        row_count = len(row)
        for i, col in enumerate(row):
            print("{:d}".format(col), end="")
            if i < row_count - 1:
                print(" ", end="")
            else:
                print("$")
