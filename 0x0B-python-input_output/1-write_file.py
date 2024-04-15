#!/usr/bin/python3
"""Modudle write file"""


def write_file(filename="", text=""):
    """Writes file with UTF8 format
        writes to the text file, returns
        number of char written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        n = f.write(text)
    return (n)
