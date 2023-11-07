#!/usr/bin/python3
"""Defines module for from_json_string method."""
import json


def from_json_string(my_str):
    """returns the Python object represented by a JSON string."""
    return json.loads(my_str)
