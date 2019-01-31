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
        """cells is a list of (x, y) tuples describing living cell locations."""
        self.liveCells = set(cells)

    def iterate(self):
        """Loop through the whole board applying the Game of Life tests to each cell, and copying the results into the
        buffer. Note that you still have to consider 'virtual' cells outside the scope of the current board as they
        can still have three neighbours."""
        pass


