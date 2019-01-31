from life import LifeGame


class TestLifeGame(object):

    def test_neighbours(self):
        """Test not in spec: helper function"""
        game = LifeGame([(0, 0)])
        assert game.neighbours((0, 0)) == 0
        assert game.neighbours((1, 0)) == 1

        game = LifeGame([(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)])
        assert game.neighbours((0, 0)) == 8
        assert game.neighbours((2, 0)) == 3

    def test_bounds(self):
        """Test not in spec: helper function"""
        game = LifeGame([])
        assert game.bounds() == (0, 0, 0, 0)

        game = LifeGame([(0, 0)])
        assert game.bounds() == (-1, -1, 3, 3)

        game = LifeGame([(-1, -1), (1, 1)])
        assert game.bounds() == (-2, -2, 5, 5)

    def test_iterate_empty(self):
        """Given an empty cell with no live neighbours, after 1 iter, it is still empty."""
        pass

    def test_iterate_underpop(self):
        """Given a cell with one neighbour, after 1 iter, it dies."""
        pass

    def test_iterate_overpop(self):
        """Given a cell with more than three neighbours, after 1 iter, it dies."""
        pass

    def test_iterate_survive(self):
        """Given a cell with two or three neighbours, after 1 iter, it lives."""
        pass

    def test_iterate_create(self):
        """Given an empty cell with three neighbours, after 1 iter, it will be live."""
        pass

    def test_empty_grid(self):
        """Scenario 5, empty grid"""
        pass

    def test_line_of_3(self):
        """Scenario 6- line of 3 cells goes from horizontal to vertical and back"""
        pass


