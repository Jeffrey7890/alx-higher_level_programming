#!/usr/bin/python3
"""Module for JSON demo"""


import json


def load_from_json_file(filename):
    """creates obj from file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.load(f))
