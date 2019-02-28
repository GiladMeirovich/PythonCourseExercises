#!/usr/bin/env python3
"""
Simulation of an ATM
"""


secret_code = "1234"  # The secret code
money = 1000  # The initial amount of money


def check_secret_code():
    """ Checks the secret code given as input
    :return: True if the secret code is correct
    """
    print("Insert the secret code.")
    code = input()
    global secret_code
    return secret_code == code


def menu():
    """
    Represents ATM's menu
    """


def start_atm():
    """
    ATM Stage 1

    Checking for secret code
    """
    if check_secret_code() is True:
        return menu()
    print("Wrong.")
    return start_atm()


def main():
    start_atm()


if __name__ == '__main__':
    main()