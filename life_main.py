import os
from life import LifeGame

"""Simple terminal based front end to run a LifeGame instance."""


def display_board(life_game):
    """Prints the current board state to the console."""

    x_origin, y_origin, width, height = -1, -1, 3, 3  # default: a 3x3 empty grid

    if len(life_game.live_cells) > 0:
        x_origin, y_origin, width, height = life_game.bounds()

    horiz_line = "-" * (width * 2 + 1)


    for j in range(height):
        print(horiz_line)

        row = "|"

        for i in range(width):
            if (i + x_origin, j + y_origin) in life_game.live_cells:
                row += "0|"
            else:
                row += ".|"

        print(row)

    print(horiz_line)


def main():

    print("Welcome to LifeGame")

    good_input = False

    while not good_input:
        try:
            live = eval("[" + " {0} ".format(input("Please enter a comma-separated list of integer 2-tuples: ")) + "]")
            assert type(live) == list

            for item in live:
                assert type(item) == tuple
                assert len(item) == 2
                assert type(item[0]) == int
                assert type(item[1]) == int

            good_input = True

            game = LifeGame(live)

        except (TypeError, NameError, AssertionError, SyntaxError):
            print("Let's try that again. Your list should look like (0, 0), (1, 0), etc.")

    done_iterating = False

    while not done_iterating:

        display_board(game)

        choice = ''

        try:
            choice = input("Enter to iterate, q to quit")
        except SyntaxError as e:
            continue

        if len(choice) > 0 and choice.capitalize()[0] == "Q":
            done_iterating = True
            continue

        game.iterate()

    print("Bye!")

    quit()


if __name__ == "__main__":
    main()
