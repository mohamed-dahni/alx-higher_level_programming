#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        row = []
        for j in i:
            row.append(j**2)
        new_matrix.append(row)

    return new_matrix
