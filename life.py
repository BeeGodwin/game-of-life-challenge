class LifeGame:
    """This class represents a Game of life board.

    This board is an infinite Cartesian plane starting at 0,0, with all points represented by integer tuples (x, y).

    This class has a set, live_cells,  of live cells as (x, y) tuples, and takes a list of (x, y) tuples in its
    constructor as its initial set of living cells.

    The iterate method computes the set of living cells next turn according to the rules of Life
    and stores this new set in live_cells.
    """

    MAX_BOARD_SIZE = 100  # a value much smaller than int max and much higher than the size of the intended game

    def __init__(self, cells):
        """cells is a list of (x, y) tuples describing living cell locations."""
        self.live_cells = set(cells)

    def iterate(self):
        """Apply the Game of Life tests to each cell on the board that is either alive or
        has neighbours (and therefore might be alive next turn.) Store the set of cells that
        will be alive for the next iteration in self.live_cells."""

        # find the set of all cells that are either alive (and therefore might die) or have any neighbours
        # (and therefore might be alive next.) This is the set of all live cells and all their neighbours.
        cells_to_check = set()

        for (x, y) in self.live_cells:
            candidates_to_add = {(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2)}
            for cell in candidates_to_add:
                cells_to_check.add(cell)

        # filter to find cells alive next turn
        alive_next = set(
            filter(lambda c: c in self.live_cells and (3 >= self.count_neighbours(c) >= 2), cells_to_check))
        alive_next = alive_next.union(
            set(filter(lambda c: c not in self.live_cells and self.count_neighbours(c) == 3, cells_to_check)))

        self.live_cells = alive_next

    def cell_at(self, x, y):
        return (x, y) in self.live_cells

    def bounds(self):
        """Finds the bounds of the active area of the board. Pads by one in all directions to allow for the total area
        growing.

        Returns the tuple (x, y, width, height) where x and y are the origin, and width and height describe the
        size."""
        if len(self.live_cells) == 0:
            return 0, 0, 0, 0

        max_b = LifeGame.MAX_BOARD_SIZE

        x_low, x_high, y_low, y_high = max_b, -max_b, max_b, -max_b
        for (x, y) in self.live_cells:
            x_high = max(x, x_high)
            x_low = min (x, x_low)
            y_high = max(y, y_high)
            y_low = min(y, y_low)

        width = x_high - x_low
        height = y_high - y_low

        return x_low - 1, y_low - 1, width + 3, height + 3

    def count_neighbours(self, cell):
        """Computes the neighbouring cells of the (x, y) tuple passed in. Returns the number of living cells in
        its neighbourhood (the eight cells directly and diagonally adjacent.)"""
        count = 0
        x, y = cell
        neighbours = {(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) if i != x or j != y}

        for n in neighbours:
            if n in self.live_cells:
                count += 1

        return count
