from .string import String

class BoardError(Exception):
    pass

class Board:
    __slots__ = 'rows cols _grid'.split()

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self._grid = {}

    def is_on_grid(self, point):
        return (-1 < point.row < self.rows) and (-1 < point.col < self.cols)

    def is_empty(self, point):
        return None is self._grid.get(point)

    def color_at(self, point):
        s = self._grid.get(point)

        return None if s is None else s.color

    def get_string(self, point):
        return self._grid.get(point)

    def _remove_string(self, string):
        for point in string.stones:
            for neigh in point.neighbors:
                neigh_str = self.get_string(neigh)
                if neigh_str is None:
                    continue
                if neigh_str is not string:
                    neigh_str.add_liberty(point)
            self._grid[point] = None

    def place_stone(self, player, point):
        if not self.is_on_grid(point):
            raise BoardError(f'{point} is off grid')

        if not self.is_empty(point):
            raise BoardError(f'{point} is already occupied')

        adj_sames = []
        adj_others = []
        liberties = []

        for neigh in point.neighbors:
            if not self.is_on_grid(neigh):
                continue

            neigh_str = self.get_string(neigh)
            if neigh_str is None:
                liberties.append(neigh)
            elif neigh_str.color == player:
                if neigh_str not in adj_sames:
                    adj_sames.append(neigh_str)
            elif neigh_str not in adj_others:
                adj_others.append(neigh_str)

        new_str = String(player, point, liberties)

        for same in adj_sames:
            new_str.merge(same)

        for pt in new_str.stones:
            self._grid[pt] = new_str

        for other in adj_others:
            other.remove_liberty(point)

        for other in adj_others:
            if 0 == other.liberty_count:
                self._remove_string(other)
