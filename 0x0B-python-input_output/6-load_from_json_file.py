#!/usr/bin/python3
"""load from json file"""

from json import load


def load_from_json_file(filename):
    """load_from_json_file
    creates an Object from a “JSON file”:
    arges:
        filename: string file name
    """
    with open(filename, "r", encoding="utf-8") as file:
        return load(file)
