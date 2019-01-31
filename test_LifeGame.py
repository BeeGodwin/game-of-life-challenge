from life import LifeGame


class TestLifeGame(object):

    def test_neighbours(self):

        game = LifeGame([(0, 0)])
        assert game.neighbours((0, 0)) == 0
        assert game.neighbours((1, 0)) == 1

        game = LifeGame([(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)])
        assert game.neighbours((0, 0)) == 8
        assert game.neighbours((2, 0)) == 3

    def test_bounds(self):

        game = LifeGame([])
        assert game.bounds() == (0, 0, 0, 0)

        game = LifeGame([(0, 0)])
        assert game.bounds() == (-1, -1, 3, 3)

        game = LifeGame([(-1, -1), (1, 1)])
        assert game.bounds() == (-2, -2, 5, 5)
