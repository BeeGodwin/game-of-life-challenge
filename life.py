class LifeGame:
    """This class represents a Game of life board.

    This board is an infinite Cartesian plane starting at 0,0.

    Each location x, y, where x and y are ints, contains True for a living cell and False for an empty cell.
    This class maintains a two dimensional list to represent the board. The x, y range of the list describes the bounds
    the area containing living cells. This class will adjust storage as needed to cope with larger bounds."""

    # set min board & init buffer
    def __init__(self):
        self.board = [[False]]  # a one-cell board
        self.buffer = [[False]]
        self.origin = (0, 0)  # origin is an (x, y) tuple pointing to the cell in board that represents the origin
        self.buffer_origin = (0, 0)  # when an iteration causes the board to grow, we need the old and new origins.

    def get_cell_at(self, x, y):
        """If the location is on the board, returns True for a living cell or False for an empty cell.
        If the location is not on the board, returns False."""
        pass

    def set_cell_at(self, x, y, live):
        """If the location is on the board, sets this cell in the buffer to the True/False value of live.
        If the location is not on the board, enlarges the buffer appropriately, modifies buffer_origin appropriately."""
        pass

    def iterate(self):
        """Loop through the whole board applying the Game of Life tests to each cell, and copying the results into the
        buffer. Note that you still have to consider 'virtual' cells outside the scope of the current board as they
        can still have three neighbours."""
        pass

    def grow_buffer(self):
        """Determines the bounds of the area of live cells and pads the buffer by one cell in all directions"""
        pass

    def copy_buffer(self):
        """Crops the buffer of excess cells and copies it to the board."""
        pass
