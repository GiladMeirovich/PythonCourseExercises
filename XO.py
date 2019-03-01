#!/usr/bin/env python3
"""
XO module

Uses:
    Determines the result of an XO game
"""


def check(game):
    """

    Param:
        game - XO matrix
    Return:
        1 - Player 1 has won
        2 - Player 2 has won
        0 - Draw
    """
    if game[0][0] == game[1][1] == game[2][2] != 0:  # Diagonal
        return game[0][0]

    if game[0][2] == game[1][1] == game[2][0] != 0:  # Secondary diagonal
        return game[0][2]

    if game[0][0] == game[0][1] == game[0][2] != 0:  # First horizontal
        return game[0][0]

    if game[1][0] == game[1][1] == game[1][2] != 0:  # Second horizontal
        return game[1][0]

    if game[2][0] == game[2][1] == game[2][2] != 0:  # Third horizontal
        return game[2][0]

    if game[0][0] == game[1][0] == game[2][0] != 0:  # First vertical
        return game[0][0]

    if game[0][1] == game[1][1] == game[2][1] != 0:  # Second vertical
        return game[0][1]

    if game[0][2] == game[1][2] == game[2][2] != 0:  # Third vertical
        return game[0][2]

    return 0  # Draw


def test():
    """
    Displays a test on check function
    """
    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]
    line = "{line[0]}|{line[1]}|{line[2]}"

    print("Board:")
    print(line.format(line=game[0]))
    print("-"*5)
    print(line.format(line=game[1]))
    print("-"*5)
    print(line.format(line=game[2]))

    result = check(game)

    if result == 1:
        print("Player 1 has won.")
    elif result == 2:
        print("Player 2 has won.")
    else:
        print("Draw.")


def main():
    test()


if __name__ == '__main__':
    main()