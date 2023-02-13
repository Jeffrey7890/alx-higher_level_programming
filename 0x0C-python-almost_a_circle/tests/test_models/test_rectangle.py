import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        from models.rectangle import Rectangle
        self.rectangle = Rectangle(4, 6, 2, 1, 12)


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

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 24)

    def test_str(self):
        self.assertEqual(self.rectangle.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_Equal(self):
        self.rectangle.update(89, 2, 3, 4, 5)
        id = self.rectangle.id
        width = self.rectangle.width
        height = self.rectangle.height
        x = self.rectangle.x
        y = self.rectangle.y
        
        self.assertEqual(id, 89)
        self.assertEqual(width, 2)
        self.assertEqual(height, 3)
        self.assertEqual(x, 4)
        self.assertEqual(y, 5)

    def test_update_Raise(self):
        with self.assertRaises(IndexError):
            self.rectangle.update(10, 20, 3, 4, 5, 6, 67, 7,10)

    def test_update_RaiseType(self):
        with self.assertRaises(TypeError):
            self.rectangle.update(height = None)

    def test_updateValues(self):
        self.rectangle.update(1, 2, 3, height=10, width=20)                
        height = self.rectangle.height
        width = self.rectangle.width
        self.assertEqual(height, 3)
        self.assertEqual(width, 2)

        self.rectangle.update(id=30, height=20, width=12, x=2, y=1)
        self.assertEqual(self.rectangle.height, 20)
        self.assertEqual(self.rectangle.width, 12)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 1)
        self.assertEqual(self.rectangle.id, 30)
