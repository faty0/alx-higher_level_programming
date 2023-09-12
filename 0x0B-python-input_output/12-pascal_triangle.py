#!/usr/bin/python3
''' module that contains the function pascal_triangle
'''


def pascal_triangle(n):
    ''' returns a list of lists of integers representing
    the Pascal’s triangle of n
    '''
    if n > 2:
        matrix = [[1], [1, 1]]
        for i in range(2, n):
            row = []
            row.append(1)
            for c in range(1, i):
                row.append(matrix[i - 1][c] + matrix[i - 1][c - 1])
            row.append(1)
            matrix.append(row)
    elif n == 1:
        matrix = [[1]]
    elif n == 2:
        matrix = [[1], [1, 1]]
    else:
        matrix = []
    return matrix
