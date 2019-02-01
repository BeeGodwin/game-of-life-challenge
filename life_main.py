from life import LifeGame

"""Basic terminal based front end to run a LifeGame instance."""


def display_board(life_game):
    """Prints the current board state to the console."""
    # TODO improve display to print nice grid output
    print(life_game.live_cells)


def main():

    print("Welcome to LifeGame")

    live = eval(input("Please enter a comma-separated list of integer 2-tuples"))

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
