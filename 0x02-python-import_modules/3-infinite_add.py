#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    length = len(argv)
    sums = 0
    if length == 1:
        print("0")
    else:
        for i in range(1, length):
            sums += int(argv[i])
        print(sums)
