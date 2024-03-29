#!/usr/bin/python3
"""This module defines a JSON-to-object function"""


import json


def from_json_string(my_str):
    """Returns the python object representation of JSON string"""
    return json.loads(my_str)
