#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """init
        args:
            first_name : string
            last_name : string
            age : int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """class to json"""
        my_dic = self.__dict__
        if attrs is None:
            return my_dic

        new_dict = {}
        for key in attrs:
            value = my_dic.get(key)
            if value:
                new_dict[key] = value
        return new_dict
