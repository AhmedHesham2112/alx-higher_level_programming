#!/usr/bin/python3
"""
Define a Student Class and to_json function
"""


class Student:
    """
    Representation of Student Class
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializing a student

        Args:
        first_name (string): the student's first name
        last_name (string): the student's last name
        age (int): the student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic
