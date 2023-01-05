#!/usr/bin/python3
import os
if __name__ == "__main__":
    line = "#pythoniscool\n"
    os.write(1, line.encode())
