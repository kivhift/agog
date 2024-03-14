from .point import Point

class Move:
    __slots__ = 'point'.split()

    def __init__(self, point=None):
        self.point = point

    def __str__(self):
        if self.is_play:
            return f'move: {self.point}'
        elif self.is_pass:
            return 'move: pass'

        return 'move: resign'

    @property
    def is_play(self):
        return isinstance(self.point, Point)

    @property
    def is_pass(self):
        return self.point is None

    @property
    def is_resign(self):
        return not (self.is_play or self.is_pass)

    @classmethod
    def play(cls, point):
        return cls(point)

    @classmethod
    def pass_(cls):
        return cls(None)

    @classmethod
    def resign(cls):
        return cls(False)
