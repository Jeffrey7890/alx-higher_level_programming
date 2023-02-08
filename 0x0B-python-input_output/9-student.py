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

    def to_json(self):
        """returns dictionary repr of student"""
        return (self.__dict__)
