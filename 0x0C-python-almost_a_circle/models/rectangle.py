#!/usr/bin/python3
"""rectangle class module"""

from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """inint
            width: int
            hight: int
            x: int
            y: int
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width rectangle  getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width rectangle setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height rectangle  getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height rectangle  setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate rectangle area"""
        return self.height * self.width

    def display(self):
        """rectangle area"""
        display_ractangle = '\n' * self.y +\
              (self.height * (' ' * self.x + self.width * '#' + "\n"))
        
        print(display_ractangle, end="")

    def __str__(self):
        """string method"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} "\
            f"- {self.width}/{self.height}"
    
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
        """retangle to dictionary"""
        retangle_dic = {}
        retangle_dic["id"] = self.id
        retangle_dic["width"] = self.width
        retangle_dic["height"] = self.height
        retangle_dic["x"] = self.x
        retangle_dic["y"] = self.y
        return retangle_dic
