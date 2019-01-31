class LifeGame:
    """This class represents a Game of life board.

    This board is an infinite Cartesian plane starting at 0,0.

    This class has a set, live_set,  of live cells as (x, y) tuples, and takes a list of (x, y) tuples in its
    constructor as its intial list of living cells.

    Each time iterate is called, find the bounds of the area of living cells and pad by one.

    For each cell in this plane, compute its 8 neighbouring (x, y) tuples and determine how many living
    neighbours it has. Living cells survive with either 2 or 3 neighbours. Cells are created when an empty cell
    has exactly three neighbours.
    """
    def __init__(self, cells):
        """cells is a collection of (x, y) tuples describing living cell locations."""
        self.liveCells = set(cells)

    def iterate(self):
        """Apply the Game of Life tests to each cell in the active area of the board. Return the set of cells that
        will be alive for the next iteration."""
        pass

    def cell_at(self, x, y):
        return (x, y) in self.liveCells

    def bounds(self):
        """Finds the bounds of the active area of the board. Pads by one in all directions to allow for the total area
        growing.

        Returns the tuple (x, y, len, height)."""
        if len(self.liveCells) == 0:
            return 0, 0, 0, 0

        x_low, x_high, y_low, y_high = 0, 0, 0, 0
        for x, y in self.liveCells:
            x_high = max(x, x_high)
            x_low = min (x, x_low)
            y_high = max(y, y_high)
            y_low = min(y, y_low)

        width = x_high - x_low
        height = y_high - y_low

        return x_low - 1, y_low - 1, width + 3, height + 3

    def neighbours(self, cell):
        """Computes the neighbouring cells of the (x, y) tuple passed in. Returns the number of living cells in
        its neighbourhood (the eight cells directly and diagonally adjacent.)"""
        count = 0
        x, y = cell
        neighbours = {(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) if i != x or j != y}

        for n in neighbours:
            if n in self.liveCells:
                count += 1

        return count





