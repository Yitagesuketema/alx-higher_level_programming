#!/usr/bin/python3
# File : 0-square_matrix_simple.py
# Squared simple
# Auth : Yitagesu K Areda


def square_matrix_simple(matrix=[]):
	"""Compute the square value of all integers of a matrix."""
    return ([list(map(lambda x: x * x, row)) for row in matrix])

