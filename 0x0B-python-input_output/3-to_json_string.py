#!/usr/bin/python3
"""Defines module for to_json_to-string method."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object."""
    return json.dumps(my_obj)
