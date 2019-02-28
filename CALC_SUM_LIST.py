#!/usr/bin/env python3
"""
The program calculates the sum of a list given by the user
"""


def single_number_calculating():
    pass


def multi_number_calculating():
    pass


def menu():
    """
    Options of the script

    1 - Calculate one number at a time
    2 - Calculate the whole list at once
    """
    print("Menu:")
    print("1 - Calculate one number at a time")
    print("2 - Calculate the whole list at once")
    option = input()
    if option == 1:
        return single_number_calculating()
    if option == 2:
        return  multi_number_calculating()


def main():
    menu()


if __name__ == '__main__':
    main()