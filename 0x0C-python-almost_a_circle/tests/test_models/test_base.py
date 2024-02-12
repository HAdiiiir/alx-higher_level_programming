#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    # Test case to ensure that IDs are incremented correctly
    def test_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    # Test case to ensure that custom IDs are assigned correctly
    def test_custom_id(self):
        b = Base(100)
        self.assertEqual(b.id, 100)

    # Test case to ensure that negative IDs raise ValueError
    def test_negative_id(self):
        with self.assertRaises(ValueError):
            Base(-1)

    # Test case to ensure that string IDs raise TypeError
    def test_string_id(self):
        with self.assertRaises(TypeError):
            Base("abc")
