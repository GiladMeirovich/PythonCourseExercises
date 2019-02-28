#!/usr/bin/env python3
"""
Simulation of an ATM
"""


secret_code = "1234"  # The secret code
balance = 1000  # The initial amount of money


def check_secret_code():
    """
    Checks the secret code given as input
    :return: True if the secret code is correct
    """
    print("Insert the secret code.")
    code = input()
    global secret_code
    return secret_code == code


def print_menu():
    """
    Prints the menu
    """
    print("ATM Menu:")
    print("A - Check balance")
    print("B - Withdraw")
    print("C - Change secret number")
    print("D - Exit")


def withdraw_menu():
    """
    Submenu to withdraw money
    """
    print("Withdraw Menu:")
    print("A - Withdraw 20 $")
    print("B - Withdraw 50 $")
    print("Or enter the amount of money")
    option = input()
    global balance

    if option == 'A':
        if balance >= 20:
            balance -= 20
        else:
            print("Not enough money.\nAction canceled")
        return

    if option == 'B':
        if balance >= 50:
            balance -= 50
        else:
            print("Not enough money.\nAction canceled")
        return

    try:
        amount = int(option)
        if amount > 0:
            if balance >= amount:
                balance -= amount
            else:
                print("Not enough money.\nAction canceled")
        else:
            print("Cant withdraw negative amount of money.\nAction canceled")
    except:
        print("Wrong input.\nAction canceled")
    finally:
        return


def change_secret_code():
    print("Enter new secret code")
    new_code = input()
    try:
        num = int(new_code)
        if num < 0:
            print("Code cant be a negative number.\nAction canceled")
            return
        else:
            global secret_code
            secret_code = new_code
    except:
        print("Code must be an integer.\nAction canceled")
    finally:
        return


def menu():
    """
    Represents ATM's menu
    """
    print_menu()
    option = input()

    if option not in ['A','B','C','D']:
        print("Wrong option")
        return menu()

    if option != 'D' and check_secret_code() is False:
        print("Wrong code.")
        return menu()

    global balance
    if option == 'A':
        print("Balance is: ", balance, "$")
        return menu()
    if option == 'B':
        withdraw_menu()
        return menu()
    if option == 'C':
        change_secret_code()
        return menu()
    return  # Option D


def start_atm():
    """
    ATM Stage 1

    Checking for secret code
    """
    if check_secret_code() is True:
        return menu()
    else:
        print("Wrong code.")
        return start_atm()


def main():
    start_atm()


if __name__ == '__main__':
    main()