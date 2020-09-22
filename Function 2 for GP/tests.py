import unittest
from datetime import datetime
from task_refactored import my_datetime


class TestCase(unittest.TestCase):

    # check for empty input
    def test_1_datetime(self):
        sec = ''
        self.assertIsNone(my_datetime(sec))

    # check for non-integers
    def test_2_datetime(self):
        sec = 'abcdefg'
        self.assertIsNone(my_datetime(sec))

    # check for negative integers
    def test_3_datetime(self):
        sec = -12345
        self.assertIsNone(my_datetime(sec))

    # check it can handle a whole amount of years
    def test_4_datetime(self):
        sec = 63072000
        expected = datetime.utcfromtimestamp(63072000).strftime("%m-%d-%Y")
        self.assertEqual(my_datetime(sec), expected)

    # check random number of seconds
    def test_5_datetime(self):
        sec = 47340000
        expected = datetime.utcfromtimestamp(47340000).strftime("%m-%d-%Y")
        self.assertEqual(my_datetime(sec), expected)

    # check random number of seconds
    def test_6_datetime(self):
        sec = 538341884
        expected = datetime.utcfromtimestamp(538341884).strftime("%m-%d-%Y")
        self.assertEqual(my_datetime(sec), expected)

    # check it can handle a small number of days
    def test_7_datetime(self):
        sec = 172800
        expected = datetime.utcfromtimestamp(172800).strftime("%m-%d-%Y")
        self.assertEqual(my_datetime(sec), expected)

    # check it can handle leap years
    def test_8_datetime(self):
        sec = 1091906684
        expected = datetime.utcfromtimestamp(1091906684).strftime("%m-%d-%Y")
        self.assertEqual(my_datetime(sec), expected)

    # check example listed in function
    def test_9_datetime(self):
        sec = 123456789
        expected = datetime.utcfromtimestamp(123456789).strftime("%m-%d-%Y")
        self.assertEqual(my_datetime(sec), expected)

    # check example listed in function
    def test_10_datetime(self):
        sec = 9876543210
        expected = datetime.utcfromtimestamp(9876543210).strftime("%m-%d-%Y")
        self.assertEqual(my_datetime(sec), expected)

    # check current date
    def test_11_datetime(self):
        sec = 1596855644
        expected = datetime.utcfromtimestamp(1596855644).strftime("%m-%d-%Y")
        self.assertEqual(my_datetime(sec), expected)