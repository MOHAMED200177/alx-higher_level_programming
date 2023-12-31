#!/usr/bin/python3
"""save to json file"""

from json import dump


def save_to_json_file(my_obj, filename):
    """save_to_json_file
        writes an Object to a text file, using a JSON representation:
    arges:
        filename: string file name
        my_obj: json object representation
    """
    with open(filename, "w", encoding="utf-8") as file:
        dump(my_obj, file)
