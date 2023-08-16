#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[x ** 2 for x in row] for row in matrix]
    return new
