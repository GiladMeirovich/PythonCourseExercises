#!/usr/bin/env python3
"""
id_israel module

Uses:
    Determine if an id is valid
"""


def is_valid_id(id_str):
    """
    Checks if the id is valid

    Params:
        id_str - str type of the id

    Return:
        True - id_str is valid
        False - id_str is'nt valid
    """
    if id_str is None or len(id_str) != 9:
        return False

    digits = list(map(int, list(id_str[:-1])))
    check_digit = int(id_str[-1])
    current_sum = 0
    digits_sum = 0
    counter = 0  # Could have used index() but they may be duplicates
    for digit in digits:
        current_sum = digit * (counter % 2 + 1)
        if current_sum > 9:
            current_sum -= 9
        digits_sum += current_sum
        counter += 1

    return ((digits_sum % 10 + check_digit) % 10) == 0


def test_id():
    """
    tests if the id given as input(promt) is valid
    """
    print("Enter id.")
    usr_id = input()
    if is_valid_id(usr_id) is True:
        print("Id is valid")
    else:
        print("Id is'nt valid")


def main():
    test_id()


if __name__ == '__main__':
    main()
