#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:"""

    with open(filename, encoding="utf-8") as file:
        file_read= file.read()
        print(file_read, end="")
