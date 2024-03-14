import enum

@enum.unique
class Player(enum.IntEnum):
    black = 0
    white = 1

    def __str__(self):
        return self.name

    @property
    def other(self):
        return type(self)(self.value ^ 1)
