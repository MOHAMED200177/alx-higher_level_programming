#!/usr/bin/python3
"""json string module"""

from json import loads


def from_json_string(my_str):
    """from_json_string
        returns an object (Python data structure) represented by a JSON string:
    arges:
        my_str: string json object
    """

    return loads(my_str)
