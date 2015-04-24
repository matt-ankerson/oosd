# Author: Matt Ankerson
# Date: 24 April 2015


class ClosureExamples():

    def __init__(self):
        pass

    # Computes the nth Fibonacci number
    def compute_fibonacci(self, n):
        l = []
        count = 1
        while count < n:
            yield l
            count *= 2