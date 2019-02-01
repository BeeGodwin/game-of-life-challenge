class LifeGame:
    """This class represents a Game of life board.

    This board is an infinite Cartesian plane starting at 0,0, with all points represented by integer tuples (x, y).

    This class has a set, live_cells,  of live cells as (x, y) tuples, and takes a list of (x, y) tuples in its
    constructor as its intial set of living cells.

    The iterate method computes the set of living cells next turn according to the rules of Life
    and stores this new set in live_cells.
    """

    def __init__(self, cells):
        """cells is a collection of (x, y) tuples describing living cell locations."""
        self.live_cells = set(cells)

    def iterate(self):
        """Apply the Game of Life tests to each cell on the board that is either alive or
        has neighbours (and therefore might be alive next turn.) Return the set of cells that
        will be alive for the next iteration."""

        alive_next = set()

        cells_to_check = set()

        # find the set of all cells that are either alive (and therefore might die) or have any neighbours
        # (and therefore might be alive next.)
        for (x, y) in self.live_cells:
            candidates_to_add = {(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2)}
            for cell in candidates_to_add:
                cells_to_check.add(cell)

        # Check all these cells against the rules of Life. If they're alive next turn add them to the
        # alive_next list. If not, ignore them (if they're not included, they're considered dead.)
        for cell in cells_to_check:
            num_neighbours = self.count_neighbours(cell)
            if cell in self.live_cells and (num_neighbours == 2 or num_neighbours == 3):
                alive_next.add(cell)
            elif cell not in self.live_cells and num_neighbours == 3:
                alive_next.add(cell)

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

        x_low, x_high, y_low, y_high = 1000, -1000, 1000, -1000
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
