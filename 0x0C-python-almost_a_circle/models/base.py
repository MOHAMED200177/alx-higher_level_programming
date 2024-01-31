#!/usr/bin/python3
"""base class module"""

from json import dump
from json import dumps
from json import loads
import csv


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init
        id : int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionaries to json"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file csv"""
        mycsv = ""
        flag = -1
        for o in list_objs:
            if o.__class__.__name__ == "Rectangle":
                if flag == -1:
                    mycsv += "id,width,height,x,y\n"
                    flag = 0

                mycsv += f"{o.id},{o.width},{o.height},{o.x},{o.y}\n"

            else:
                if flag == -1:
                    mycsv += "id,size,x,y\n"
                    flag = 0

                mycsv += f"{o.id},{o.size},{o.x},{o.y}\n"

        with open(cls.__name__+".csv", encoding="utf-8", mode="w") as file:
            file.write(mycsv[:-1])

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv"""
        data = []
        with open(cls.__name__+".csv", encoding="utf-8", mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert values to integers
                for key in row:
                    row[key] = int(row[key])
                data.append(row)
        return list(map(lambda obj: cls.create(**obj), data))
