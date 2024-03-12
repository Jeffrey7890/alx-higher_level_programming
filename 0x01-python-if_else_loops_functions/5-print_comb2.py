#!/usr/bin/python3
i, j = 0, 0

for _ in range(0, 100):
    if (i == 9 and j == 9):
        print("{}{}".format(i, j))
    else:
        print("{}{}".format(i, j), end=', ')
    j += 1
    if j > 9:
        i += 1
        j = 0
    if i > 9:
        i = 1
