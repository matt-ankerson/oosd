import unittest
import timeit
from closure_examples import *

# Author: Matt Ankerson
# Date: 24 April 2015


class TestCases(unittest.TestCase):

    def setUp(self):
        self.fib = 8

    def test_compute_fibonacci(self):
        self.assertEqual(compute_fibonacci(6), self.fib)

    def test_memoise_fib(self):
        fib = memoise_fib()
        self.assertEqual(fib(6), self.fib)

    def test_speed(self):
        print(timeit.timeit("fib = memoise_fib()", setup="from closure_examples import memoise_fib",  number=100000))
        print(timeit.timeit("compute_fibonacci(6)", setup="from closure_examples import compute_fibonacci", number=100000))


if __name__ == '__main__':
    unittest.main()