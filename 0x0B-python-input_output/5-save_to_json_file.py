#!/usr/bin/python3
"""Module demo Json"""


import json


def save_to_json_file(my_obj, filename):
    """save object to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
