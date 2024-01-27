#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_intgers(self):
        """Test an unordered list of integers."""
        new_list = [1, 2, 5, 7, 3, 2]
        self.assertEqual(max_integer(new_list), 7)

    def test_empty(self):
        """Test an empty list."""
        new_list = []
        self.assertEqual(max_integer(new_list), None)

    def test_floats(self):
        """Test a list of floats."""
        new_list = [2.36, 7.23, -9.85, 10.15, 6.5]
        self.assertEqual(max_integer(new_list), 10.15)

    def test_one_element(self):
        """Tests a list of one element only."""
        new_list = [7]
        self.assertEqual(max_integer(new_list), 7)

    def test_floats_and_intgers(self):
        """Tests a list of floats and intgers."""
        new_list = [1.5, 3, 2, 20.33, 19.8, 23, 52.6, 33]
        self.assertEqual(max_integer(new_list), 52.6)
