#!/usr/bin/python3
"""Test model for square class"""


import unittest


class TestSquare(unittest.TestCase):
    
    def setUp(self):
        from models.square import Square
        self.square = Square(20, 30, 40, 10)

    def test_initsquare(self):
        from models.square import Square
        with self.assertRaises(ValueError):
            Square(-100, 1, 1, 10)
            Square(100, 0, 30, 10)
            Square(200, 10, -20, 10)

        with self.assertRaises(TypeError):
            Square(None, 1, 30, 10)
            Square(20, [], 30, 10)
            Square(10, 1, (1, 2), 10)

            

    def test_validate(self):
        self.square.size = 1234
        self.assertEqual(self.square.size, 1234)
        with self.assertRaises(ValueError):
            self.square.width = 0
            self.square.height = 0
            self.square.x = -2
            self.square.y = -44
            self.square.size = -20

        with self.assertRaises(TypeError):
            self.square.width = {}
            self.square.height = None
            self.square.x = []
            self.square.x = (1, 2)
            self.square.size = None

    def test_updateSquare(self):
        self.square.update(1, 2, 3, 4)
        self.assertEqual(self.square.width, 2)
        self.assertEqual(self.square.id, 1)
        self.assertEqual(self.square.x, 3)
        self.assertEqual(self.square.y, 4)

        self.square.update(id=20, width=3, x=2, y=5)
        self.assertEqual(self.square.width, 3)
        self.assertEqual(self.square.id, 20)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 5)

        with self.assertRaises(TypeError):
            self.square.update(None, 20, 10)
            self.square.update(width = (1, 32))

    def test_strSquare(self):
        self.assertEqual(self.square.__str__(), "[Square] (10) 30/40 - 20")

