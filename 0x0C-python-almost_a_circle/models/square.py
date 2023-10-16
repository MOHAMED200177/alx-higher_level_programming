#!/usr/bin/python3
"""square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class representation"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} " \
            f"- {self.height}"

    @property
    def size(self):
        """size getter"""

        return self.width

    @size.setter
    def size(self, value):
        """size getter"""
        self.width = value
        self.height = self.width

    def attr_update(self, id=None, height=None, width=None, x=None, y=None):
        '''updates attributes'''
        if id is not None:
            self.id = id
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update rectangle"""
        if args:
            self.attr_update(*args)
        elif kwargs:
            self.attr_update(**kwargs)

    def to_dictionary(self):
        """square to dictionary"""
        retangle_dict = {}
        retangle_dict["id"] = self.id
        retangle_dict["size"] = self.size
        retangle_dict["x"] = self.x
        retangle_dict["y"] = self.y
        return retangle_dict
