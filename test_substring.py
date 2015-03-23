#!/usr/bin/env python

"""
code that tests the substring functions

can be run with py.test
"""

import pytest  # used for the exception testing
import unittest

from substring import substring_distinct as sD, substring_unique as sU

# SYMBOLIC CONSTANTS IN UPPERCASE
NULLFUNC = 0


class MyFuncTestCase(unittest.TestCase):

    def helper_assertEqual(self, func1, s, limit1=0, func2=0, ss=0, limit2=0):
        s1 = func1(s, limit1)
        ss = ss or s
        if func2:
            ss = func2(ss, limit2)
        self.assertEqual(s1, ss)

    def helper_assertEqualOneCall(self, func1, s, limit=0, ss=0):
        self.helper_assertEqual(func1, s, limit, NULLFUNC, ss, limit)

    def test_substringDistinct(self):
        self.helper_assertEqualOneCall(sD, "")
        self.helper_assertEqualOneCall(sD, "a", 3)
        self.helper_assertEqualOneCall(sD, "ab", 3)
        self.helper_assertEqualOneCall(sD, "abc", 3)
        self.helper_assertEqualOneCall(sD, "abcd", 3, "abc")
        self.helper_assertEqualOneCall(sD, "abcdefedc", 3, "defed")
        self.helper_assertEqualOneCall(sD, "abcdefedc", 5, "bcdefedc")

    def test_substringUnique(self):
        self.helper_assertEqualOneCall(sU, "", 3)
        self.helper_assertEqualOneCall(sU, "a", 3)
        self.helper_assertEqualOneCall(sU, "ab", 3)
        self.helper_assertEqualOneCall(sU, "abc", 3)
        self.helper_assertEqualOneCall(sU, "abcd", 3, "abc")
        self.helper_assertEqualOneCall(sU, "abcdefedc", 3, "ab")
        self.helper_assertEqualOneCall(sU, "aba", 3, "b")

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
