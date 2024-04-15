#!/usr/bin/python3
"""Represend student"""


class Student:
    """class that holds data
        on studenst

        Attributes
        ==========

        first_name:
            name of student
        last_name:
            string of last name of student
        age:
            int repr age of student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary repr of student"""
        if type(attrs) is list:
            result = {}
            for i in attrs:
                if i in self.__dict__:
                    result[i] = self.__dict__[i]
            return (result)
        return (self.__dict__)

    def reload_from_json(self, json):
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
