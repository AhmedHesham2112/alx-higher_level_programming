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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
