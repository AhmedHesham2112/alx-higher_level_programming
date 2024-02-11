#!/usr/bin/python3
"""Define Base Class"""
import json


class Base:
    """
    Class Base

    Attributes:
        nb_objects (int): Private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                output_list = []
                for i in list_objs:
                    output_list.append(cls.to_dictionary(i))
                string = cls.to_json_string(output_list)
                file.write(string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): is a string representing a list of dictionaries
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances

        Return:
            A list of instances
        """
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r") as f:
            dicts = Base.from_json_string(f.read())
            return [cls.create(**d) for d in dicts]
