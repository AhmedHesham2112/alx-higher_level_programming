#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (not all(isinstance(element, int) for element in
        [num for row in matrix for num in row]) and not
            all(isinstance(element, float) for element in 
                [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (not all(len(row) == len(matrix[0]) for row in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in matrix:
        row = []
        for j in i:
            row.append(round(j / div, 2))
        new_matrix.append(row)
    return new_matrix

