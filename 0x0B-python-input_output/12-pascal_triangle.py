#!/usr/bin/python3
"""Module for pascals triangle"""


def pascal_triangle(n):
    """Algorithm for pascals triangle"""
    if n <= 0:
        return ([])

    plist = []
    result = [[1]]
    for i in range(1, n):
        t = []
        t.append(1)
        for j in range(len(plist) - 1):
            t.append(plist[j] + plist[j + 1])
        t.append(1)
        result.append(t)
        plist = t
    return (result)
