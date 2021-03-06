from math import sqrt

# Author: Matt Ankerson
# Date: 24 April 2015


# Computes the nth Fibonacci number using iteration
def compute_fibonacci(n):
    a, b, c = 0, 1, 1
    for i in range(0, n):
        a = b
        b = c
        c = a + b
    return a


# Use memoisation to cache results for future reference
def memoise_fib():
    fib_memo = {}

    def compute_fibs(n):
        if n in fib_memo:
            return fib_memo[n]
        else:
            a, b, c = 0, 1, 1
            for i in range(0, n):
                a = b
                b = c
                c = a + b
                fib_memo[n] = a
            return a
    return compute_fibs


# Return the sequence of primes up to n
def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        p = primes(int(sqrt(n)))
        no_p = {j for i in p for j in range(i*2, n, i)}
        p = {x for x in range(2, n) if x not in no_p}
        return p


# Generate the sequence of primes up to n
def primes_gen(n):
    if n == 0 or n == 1:
        yield n
    else:
        p = primes_gen(int(sqrt(n)))
        no_p = {j for i in p for j in range(i*2, n, i)}
        for x in range(2, n):
            if x not in no_p:
                yield x