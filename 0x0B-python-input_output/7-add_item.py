#!/usr/bin/python3
"""save args to file"""

from sys import argv

# load functions
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file = "add_item.json"
file_list = list(argv[1:])

try:
    json_object = load_from_json_file(file)
except Exception:
    json_object = []

json_object.extend(file_list)

save_to_json_file(json_object, file)
