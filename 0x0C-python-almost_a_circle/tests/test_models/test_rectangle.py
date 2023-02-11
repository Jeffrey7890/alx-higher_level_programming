import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        from models.rectangle import Rectangle
        self.rectangle = Rectangle(10, 20)

    @unittest.skip("always skip this test")
    def test_private_attribes(self):
        with self.assertRaises(AttributeError):
            print(self.rectangle.width, self.rectangle.height)

    def test_validte_attributes(self):
        from models.rectangle import Rectangle
        with self.assertRaises(ValueError):
            Rectangle(-1, 10)
            Rectangle(0, 203)
            Rectangle(2, 0)
            Rectangle(1, 20, -111)
            Rectangle(10, 20, 34, -11)
            rect = Rectangle(10, 10, 1, 2)
            rect.width = 0
            rect.height = -2
            rect.x = -2200
            rect.y = -34

    def test_validate_attribute_TypeError(self):
        from models.rectangle import Rectangle
        with self.assertRaises(TypeError):
            Rectangle("A", 20)
            Rectangle(10, "B")
            Rectangle(10, 20, "C")
            Rectangle(20, 30, 12, "D")
            rect = Rectangle(10, 20, 20, 10, 20)
            rect.width = "jeffrey"
            rect.height = "B"
            rect.x = "naem"
            rect.y = "age"

