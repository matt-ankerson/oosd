import unittest
import timeit
from closure_examples import *

# Author: Matt Ankerson
# Date: 24 April 2015


class TestCases(unittest.TestCase):

    def setUp(self):
        self.fib = 8
        self.prime_nos = set([2, 3, 5, 7, 11, 13, 17, 19])

    def test_compute_fibonacci(self):
        self.assertEqual(compute_fibonacci(6), self.fib)

    def test_memoise_fib(self):
        fib = memoise_fib()
        self.assertEqual(fib(6), self.fib)

    def test_speed(self):
        print(timeit.timeit("fib = memoise_fib()", setup="from closure_examples import memoise_fib",  number=100000))
        print(timeit.timeit("compute_fibonacci(6)", setup="from closure_examples import compute_fibonacci", number=100000))

    def test_primes(self):
        self.assertEqual(primes(20), self.prime_nos)

    def test_primes_gen(self):
        gen_primes = set([i for i in primes_gen(20)])
        self.assertEqual(gen_primes, self.prime_nos)


if __name__ == '__main__':
    unittest.main()