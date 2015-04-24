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


# Generator function <-- reimplement as generator function. (using the keyword "yield")
# Remember that xrange is a generator function, whereas range is not.
#   The difference is that a generator simply gives us the value we need, when we need it.
#   (Without the expense of constructing the entire list)
# We are probably going to need to implement a closure here to maintain a reference to the current list item.
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