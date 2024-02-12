#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    # Test case to ensure that area calculation is correct
    def test_area(self):
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)

    # Test case to ensure that perimeter calculation is correct
    def test_perimeter(self):
        r = Rectangle(5, 6)
        self.assertEqual(r.perimeter(), 22)

    # Test case to ensure that __str__ method returns the correct string representation
    def test_str(self):
        r = Rectangle(5, 6, 1, 2, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 1/2 - 5/6")
