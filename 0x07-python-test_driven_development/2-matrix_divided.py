#!/usr/bin/python3
"""a module containing  the function matrix_divided
"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix
    """
    stri = "matrix must be a matrix (list of lists) of integers/floats"
    new = [[]]
    if not all(
        isinstance(matrix, list) and
        all(isinstance(el, (int, float)) for el in row)
        for row in matrix
    ):
        raise TypeError(stri)
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new = [[round((i / div), 2)for i in row] for row in matrix]
    return new
