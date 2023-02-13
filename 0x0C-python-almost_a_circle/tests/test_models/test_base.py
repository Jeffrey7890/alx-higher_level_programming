#!/usr/bin/python3
"""test for base.py"""


import unittest


class TestBase(unittest.TestCase):
    def setUp(self):
        from models.base import Base
        self.base = Base()

    def test_baseupdate(self):
        dictionary = self.base.to_json_string(None)
        self.assertEqual(dictionary, "[]")

        dictionary = self.base.to_json_string([{"x":2, "height":10}])
        self.assertEqual(dictionary, '[{"x": 2, "height": 10}]')

        dictionary = self.base.to_json_string(1)
        self.assertEqual(dictionary, "[]")

        dictionary = self.base.to_json_string([1, 2, 3])
        self.assertEqual(dictionary, "[]")

        dictionary = self.base.to_json_string([1, 2, {"name":"jeff"}])
        self.assertEqual(dictionary, '[{"name": "jeff"}]')

    def test_basesave_to_file(self):
        from models.rectangle import Rectangle
        from models.base import Base

        list_objs = [Rectangle(10, 7, 2, 8)]

        self.base.save_to_file([24, 32, (1, 2, 3), Base()])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")
