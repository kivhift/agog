class Point:
    __slots__ = 'row col'.split()

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return (self.row == other.row) and (self.col == other.col)

    def __hash__(self):
        return 139999 * self.row + self.col

    def __str__(self):
        return f'{self.__class__.__name__}({self.row}, {self.col})'

    @property
    def corners(self):
        P, R, C = type(self), self.row, self.col

        yield P(R - 1, C - 1)
        yield P(R - 1, C + 1)
        yield P(R + 1, C + 1)
        yield P(R + 1, C - 1)

    @property
    def neighbors(self):
        P, R, C = type(self), self.row, self.col

        yield P(R - 1, C)
        yield P(R,     C + 1)
        yield P(R + 1, C)
        yield P(R,     C - 1)
