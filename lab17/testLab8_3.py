#!/usr/bin/env python3
# -*- codding:utf-8 -*-


# Write unit tests for lab8_3


import unittest
from lab8_3 import average
from lab8_3 import median


class MyTestCaseAverage(unittest.TestCase):
    """Testing average value """

    def test_average_normal_list(self):
        source = [3, 1, 6, 7, 3, 6, 8, 5]
        actually = average(source)

        self.assertEqual(actually, float('4.875'))

    def test_average_single_list(self):
        source = [5]
        actually = average(source)

        self.assertEqual(actually, float('5'))

    def test_average_negative_list(self):
        source = [5, 4, -8, 7, -3, 9, -2]
        actually = average(source)

        self.assertEqual(actually, float('1.7142857142857142'))


class MyTestCaseMedian(unittest.TestCase):
    """Testing median value """

    def test_median_normal_list(self):
        source = [3, 1, 6, 7, 3, 6, 8, 5]
        actually = median(source)

        self.assertEqual(actually, float('5.5'))

    def test_median_single_list(self):
        source = [5]
        actually = median(source)

        self.assertEqual(actually, float('5'))

    def test_median_negative_list(self):
        source = [5, 4, -8, 7, -3, 9, -2]
        actually = median(source)

        self.assertEqual(actually, float('4'))

    def test_median_empty_list(self):
        source = []
        actually = median(source)

        self.assertEqual(actually, float('0'))


if __name__ == '__main__':
    unittest.main()

