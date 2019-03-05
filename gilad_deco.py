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
            memo[args] = func(args)
        return memo[args]
    return wrap


def main():
    pass


if __name__ == '__main__':
    main()
