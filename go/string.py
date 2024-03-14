class StringError(Exception):
    pass

class String:
    __slots__ = 'color stones liberties'.split()

    def __init__(self, color, stones, liberties):
        self.color = color
        st = self.stones = set()
        li = self.liberties = set()

        try:
            st.update(stones)
        except TypeError:
            st.add(stones)

        try:
            li.update(liberties)
        except TypeError:
            li.add(liberties)

    def __eq__(self, other):
        return (
            isinstance(other, type(self))
            and self.color == other.color
            and self.stones == other.stones
            and self.liberties == other.liberties
        )

    def add_liberty(self, liberty):
        self.liberties.add(liberty)

    def remove_liberty(self, liberty):
        self.liberties.remove(liberty)

    def merge(self, other):
        if self.color != other.color:
            raise StringError('Colors must match')

        self.stones |= other.stones
        self.liberties |= other.liberties
        self.liberties -= self.stones

    def merged_with(self, other):
        if self.color != other.color:
            raise StringError('Colors must match')

        combined = self.stones | other.stones

        return type(self)(
            self.color,
            combined,
            (self.liberties | other.liberties) - combined,
        )

    @property
    def liberty_count(self):
        return len(self.liberties)
