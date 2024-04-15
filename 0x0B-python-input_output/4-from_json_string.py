#!/usr/bin/python3
"""Converts from string to json"""

import json


def from_json_string(my_str):
    """Converts from string to json
        Returns object
    """
    return (json.loads(my_str))
