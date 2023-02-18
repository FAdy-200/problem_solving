#!/usr/bin/env python3
import unittest

from emails import find_email


class EmailTest(unittest.TestCase):
    def test_basic(self):
        testcase = [None, "Bree", "Campbell"]
        expected = "breee@abc.edu"
        self.assertEqual(find_email(testcase), expected)


if __name__ == '__main__':
    unittest.main()
