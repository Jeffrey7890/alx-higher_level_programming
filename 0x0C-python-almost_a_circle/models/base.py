#!/usr/bin/python3
"""Model Base class"""


import json


class Base:
    """Base class of all object in model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization men please ease on the doc"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts list of dictionaries to json strings"""
        if type(list_dictionaries) is not list:
            return ("[]")
        l_dict = []

        for dictionary in list_dictionaries:
            if type(dictionary) is dict:
                l_dict.append(dictionary)

        return (json.dumps(l_dict))

    @classmethod
    def save_to_file(cls, list_objs):
        """saves list of objects to json file"""
        if type(list_objs) is not list:
            raise TypeError("list_objs must be list")

        lt_dict = []
        for obj in list_objs:
            if issubclass(type(obj), Base) is True and type(obj) is not Base:
                lt_dict.append(obj.to_dictionary())
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(lt_dict, f)

    @staticmethod
    def from_json_string(json_string):
        """converts json string to objects"""
        if type(json_string) is not str:
            retrun([])

        return (json.loads(json_string))
