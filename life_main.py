from life import LifeGame


def display_board(life_game):
    print(life_game.live_cells)


def main():
    # get a list of tuples from the user
    print("Welcome to LifeGame")
    live = eval(input("Please enter a comma-separated list of integer 2-tuples"))

    game = LifeGame(live)  # unsafe! Check the input first.

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
