#!/usr/bin/python3
"""test for base.py"""


import unittest


class TestBase(unittest.TestCase):
    def setUp(self):
        from models.base import Base
        from models.rectangle import Rectangle

        self.rectobj = Rectangle
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

    def test_base_create(self):
        r1 = self.rectobj(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = self.rectobj.create(**r1_dict)


        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
    
    def test_base_create_errors(self):
        r_dict = {'width': None}
        r_dict2 = {'width':12, 'height':-1}
        with self.assertRaises((TypeError, ValueError)):
            r = self.rectobj.create(**r_dict)
            r1 = self.rectobj.create(**r_dict2) 

