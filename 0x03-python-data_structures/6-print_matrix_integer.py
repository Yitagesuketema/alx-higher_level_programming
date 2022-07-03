#!/usr/bin/python3
# File - 6-print_matrix_integer.py
# Lists of lists = Matrix
# Auth - Yitagesu K Areda


def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 0 :
        r = len(matrix) # row
        c = len(matrix[0]) # column
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=" ")
        print ()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer()
