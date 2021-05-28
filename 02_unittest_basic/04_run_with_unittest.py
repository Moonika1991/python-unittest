import unittest


def area(width, height):
    """The function returns the area of the rectangle"""

    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The width and height must be type of int or float.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return width * height


class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20)

    def test_area_incorrect_type_should_raise_error(self):
        # test is ok if function raises TypeError
        self.assertRaises(TypeError, area, '4', 5)
        self.assertRaises(TypeError, area, 4, '5')

    def test_area_inegative_value_should_raise_error(self):
        # test is ok if function raises ValueError
        self.assertRaises(ValueError, area, -4, 5)
        self.assertRaises(ValueError, area, 4, -5)
