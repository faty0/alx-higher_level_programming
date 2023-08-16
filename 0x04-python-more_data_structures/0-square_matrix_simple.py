def square_matrix_simple(matrix=[]):
    new = [[lambda x: x ** 2 for x in row] for row in matrix]
    return new
