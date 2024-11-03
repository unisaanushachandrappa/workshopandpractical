from rectangle import Rectangle
import unittest

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        rectangle = Rectangle(3,4)
        self.assertEqual(12, rectangle.calculate_area())
        rectangle = Rectangle(8, 6)
        self.assertEqual(48, rectangle.calculate_area())

    def test_perimeter(self):
        rectangle = Rectangle(3,4)
        self.assertEqual(14, rectangle.calculate_perimeter())
        rectangle = Rectangle(8, 6)
        self.assertEqual(28, rectangle.calculate_perimeter())

    def test_scale(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(12, rectangle.calculate_area())
        rectangle.scale(2)
        self.assertEqual(48, rectangle.calculate_area())
        rectangle.scale(3)
        self.assertEqual(432, rectangle.calculate_area())

if __name__ == '__main__':
    unittest.main()