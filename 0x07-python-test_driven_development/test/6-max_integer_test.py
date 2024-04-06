#!/usr/bin/python3

"""Module using unittest to test the max_integer function"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMax_integer(unittest.TestCase):
    """TestMax_integer unittest class
        
        Tests the max_integer() func for TypeErrors,
        ValueErrors, and assertEqual
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0.1, -2, 3.9, 14.3]), 14.3)
        self.assertEqual(max_integer([]), None)

        self.assertRaises(KeyError, max_integer, {'name': 'jeffrey', 'age': 22})

        with self.assertRaises(TypeError):
            max_integer('jeffrey')
            max_integer(['jeffrey', 'main'])
            max_integer([[1, 2], {2, 3}]) 
            max_integer([1, 2, 3, "jeff", "ogwu"])
            max_integer([(1, 2), (3, 4)])
            max_integer([[1, 3], [2, 3]])
            max_integer([1, 2, 'jeff'])
            max_integer({1, 2, 3, 4})
            max_integer(1.222222)
            max_integer(None)
            max_integer(1)




