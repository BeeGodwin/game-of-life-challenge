from life import LifeGame

"""Basic terminal based front end to run a LifeGame instance."""


def display_board(life_game):
    """Prints the current board state to the console."""

    x_origin, y_origin, width, height = -1, -1, 3, 3  # a 3x3 empty grid

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

    live = eval("[" + input("Please enter a comma-separated list of integer 2-tuples: ") + "]")

    game = LifeGame(live)  # TODO unsafe! Check the input first.

    done = False

    while not done:
        display_board(game)
        choice = input("Enter to iterate, q to quit")
        if len(choice) > 0 and choice.capitalize()[0] == "Q":
            done = True
            continue
        game.iterate()

    print("Bye!")


if __name__ == "__main__":
    main()
