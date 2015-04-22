import unittest
from main import *

# Author: Matt Ankerson
# Date: 23 April 2015


class TestCases(unittest.TestCase):

    def setUp(self):
        self.c = "c"
        self.st = "I have become comfortably numb."
        self.st_chars_removed = "I have beome omfortably numb."
        self.st_replaced = "I have beCome Comfortably numb."
        self.c_n_expected = 2
        self.n_words_expected = 1

        # List, expected list and function for testing map functions.
        self.list = [1, 2, 3, 4]
        self.list_expected = [2, 4, 6, 8]
        self.func = lambda a: a * 2

    def test_factorial(self):
        self.assertEqual(factorial(6), 120)

    def test_remove_a_letter(self):
        self.assertEqual(remove_a_letter(self.st, self.c), self.st_chars_removed)

    def test_count_occurences(self):
        self.assertEqual(count_occurences(self.st, self.c), self.c_n_expected)

    def test_count_words(self):
        self.assertEqual(count_words(self.st, self.c), self.n_words_expected)

    def test_replace_with_upper(self):
        self.assertEqual(replace_with_upper(self.st, self.c), self.st_replaced)

    def test_mymap(self):
        self.assertEqual(mymap(self.func, self.list), self.list_expected)

    def test_mymap_recursive(self):
        self.assertEqual(mymap(self.func, self.list), self.list_expected)

if __name__ == '__main__':
    unittest.main()