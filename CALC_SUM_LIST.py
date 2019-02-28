#!/usr/bin/env python3
"""
The program calculates the sum of a list given by the user
"""
from functools import reduce


def single_number_calculating():
    """
    Prints the sum of a list given by user
    """
    print("Enter one number at a time\nInsert 'stop' to stop")
    numbers = []
    number = input()
    while number != 'stop':
        numbers.append(int(number))
        number = input()
    sum_list = sum(numbers)
    print(sum_list)


def multi_number_calculating():
    """
    Prints the sum of a list given by user
    """
    print("Enter the list (Like: '1,2,3,4'")
    numbers = input()
    numbers = numbers.split(',')
    numbers = map(int, numbers)
    sum_list = sum(numbers)
    print(sum_list)


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
    if option == "1":
        single_number_calculating()
    if option == "2":
        multi_number_calculating()


def main():
    menu()


if __name__ == '__main__':
    main()