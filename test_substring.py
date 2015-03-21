#!/usr/bin/env python

"""
code that tests the substring functions

can be run with py.test
"""

import pytest  # used for the exception testing
import unittest

from substring import substringDistinct as sD, substringUnique as sU


class MyFuncTestCase(unittest.TestCase):

    def helper_Distinct(self, s, ss):
        self.assertEqual(sD(s, 3), ss)

    def test_substringDistinct(self):
        self.helper_Distinct("", "")
        # self.assertEqual(sD("", 3), "")
        # self.assertEqual(sD("a", 3), "a")
        # self.assertEqual(sD("ab", 3), "ab")
        # self.assertEqual(sD("abc", 3), "abc")
        # self.assertEqual(sD("abcd", 3), "abc")

    def test_substringUnique(self):
        self.assertEqual(sU("", 3), "")
        self.assertEqual(sU("a", 3), "a")
        self.assertEqual(sU("ab", 3), "ab")
        self.assertEqual(sU("abc", 3), "abc")
        self.assertEqual(sU("abcd", 3), "abc")

    def test_DistinctIsUnique(self):
        self.assertEqual(sU("", 3), sD("", 3))
        self.assertEqual(sU("a", 3), sD("a", 3))
        self.assertEqual(sU("ab", 3), sD("ab", 3))
        self.assertEqual(sU("abc", 3), sD("abc", 3))

    def test_DistinctIsNotUnique(self):
        self.assertEqual(sU("aabc", 3), "bc")
        self.assertEqual(sD("aabc", 3), "aabc")
        self.assertNotEqual(sU("aabc", 3), sD("aabc", 3))

if __name__ == "__main__":
    unittest.main()
