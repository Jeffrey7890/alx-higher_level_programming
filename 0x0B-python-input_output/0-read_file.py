#!/usr/bin/python3
"""Modudle read file"""


def read_file(filename=""):
    """Reads file with UTF8 format
        prints content of file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
