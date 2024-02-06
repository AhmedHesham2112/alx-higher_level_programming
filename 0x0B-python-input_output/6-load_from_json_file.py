#!/usr/bin/python3
"""
Define a load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """
    with open(filename, "r") as f:
        return json.load(f)
