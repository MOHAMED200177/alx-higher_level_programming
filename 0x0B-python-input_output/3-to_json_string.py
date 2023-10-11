#!/usr/bin/python3
"""json string module"""

from json import dumps


def to_json_string(my_obj):
    """to_json_string
     returns the JSON representation of an object (string):
    arges:
        my_obj: python dictionary
    """

    return dumps(my_obj)
