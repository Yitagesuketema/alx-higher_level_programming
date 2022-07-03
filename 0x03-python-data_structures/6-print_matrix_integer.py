#!/usr/bin/python3
# File : 6-print_matrix_integer.py
# Lists of lists = Matrix
# Auth : Yitagesu K Areda


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end="")
                if j != (len(matrix[i]) - 1):
                    print(" ", end="")

        print("")

