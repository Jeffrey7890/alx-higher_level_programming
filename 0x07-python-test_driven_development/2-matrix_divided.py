#!/usr/bin/python3

"""Module to represent matrix division

    This module contains the matrix_divided() function,
    It divides a (list of list) matrix by a divisor

    The matrix must contain elements of type integer or
    float, else other it raises other error.

"""


def raise_TypeError(matrix, message):
    """raise_TypeError

    Raise the type Error for matrix argument,
    written to reduce code clutter and to have
    DRY code

    """
    if type(matrix) is not list:
        raise TypeError(message)


def raise_TypeError_number(number, message):
    if type(number) not in [int, float]:
        raise TypeError(message)


def matrix_divided(matrix, div):
    """matrix_divided

    Divides matrix by a number

    Attributes
    ==========

    matrix:
        must be a list of list type and must
        contain either float or int types only.

    div:
        must be either int or float type only

    Returns:
        A new list containing the divided results
        from the original matrix

    """

    TEMsg = "matrix must be a matrix (list of lists) of integers/floats"
    raise_TypeError(matrix, TEMsg)
    raise_TypeError(matrix[0], TEMsg)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    raise_TypeError_number(div, "div must be of type integers/floats")

    row_length = len(matrix[0])
    result = []
    for row in matrix:

        raise_TypeError(row, TEMsg)

        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        result_row = []
        for j in range(row_length):
            raise_TypeError_number(row[j], TEMsg)
            result_row.append(round(row[j] / div, 2))
        result.append(result_row)
    return (result)
