#!/usr/bin/env python3
"""
gilad_deco module
Uses:
    Caching expensive calculation
"""


def cache_decorator(func):
    """
    Cache decorator

    Params:
        func - The function

    Return:
        wrap - Function which stores calculation of func over time
    """
    memo = {}

    def wrap(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return wrap


@ cache_decorator
def fibo(n):
    """
    Fibonacci series

    Params:
        n - Index of the n element in fibonacci series

    Return:
        The value of the the n element in fibonacci series
    """
    if n == 0 or n == 1:
        return n

    return fibo(n - 1) + fibo(n - 2)


def test_decorator():
    """
    Tests cache_decorator on fibo function
    """
    print("Fibonacci 200 element")
    print(fibo(200))
    print("\nFibonacci 500 element after caching 100 element")
    print(fibo(500))
    print("\nFibonacci 700 element after caching 500 element")
    print(fibo(700))


def main():
    test_decorator()


if __name__ == '__main__':
    main()
