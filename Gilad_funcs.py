#!/usr/bin/env python3
"""
Gilad_funcs module

Uses:
    Map function
"""


def gilad_map(func, items):
    """
    Map function:
        applies on each item in items func

    Params:
        func - The function to apply
        items - List of items

    Return:
        lst - New list with the func applied on each item in items
    """
    lst = []
    for item in items:
        lst.append(func(item))

    return lst


def test_map():
    """
    Function tests gilad_map function
    """
    items = list(range(11))
    print("Items:")
    print(items)
    print("\nFunction to apply: lambda x: x * x\nReturns (x squared)")
    items = gilad_map(lambda x: x * x, items)
    print("\nNew items:")
    print(items)


def main():
    test_map()


if __name__ == '__main__':
    main()
