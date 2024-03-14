import copy

from .board import Board
from .player import Player
from .point import Point

class GameError(Exception): pass

class Game:
    __slots__ = 'board next_player prev_state last_move'.split()

    def __init__(self, board, next_player, prev_state, last_move):
        self.board = board
        self.next_player = next_player
        self.prev_state = prev_state
        self.last_move = last_move

    def apply_move(self, move):
        if move.is_play:
            next_board = copy.deepcopy(self.board)
            next_board.place_stone(self.next_player, move.point)
        else:
            next_board = self.board

        return type(self)(next_board, self.next_player.other, self, move)

    @classmethod
    def new(cls, size):
        if isinstance(size, int):
            size = (size, size)

        return cls(Board(*size), Player.black, None, None)

    @property
    def is_over(self):
        if self.last_move is None:
            return False

        if self.last_move.is_resign:
            return True

        penul_move = self.prev_state.last_move
        if penul_move is None:
            return False

        return self.last_move.is_pass and penul_move.is_pass

    def is_self_capture(self, player, move):
        if not move.is_play:
            return False

        next_board = copy.deepcopy(self.board)
        next_board.place_stone(player, move.point)

        return 0 == next_board.get_string(move.point).liberty_count

    @property
    def situation(self):
        return (self.next_player, self.board)

    def violates_ko(self, player, move):
        if not move.is_play:
            return False

        next_board = copy.deepcopy(self.board)
        next_board.place_stone(player, move.point)
        next_situation = (player.other, next_board)
        prev_state = self.prev_state
        while prev_state is not None:
            if prev_state.situation == next_situation:
                return True

            prev_state = prev_state.prev_state

        return False

    def is_valid(self, move):
        if self.is_over:
            return False

        if move.is_pass or move.is_resign:
            return True

        return (
            self.board.is_empty(move.point)
            and not (
                self.is_self_capture(self.next_player, move)
                or self.violates_ko(self.next_player, move)
            )
        )

    def is_an_eye(self, point, color):
        board = self.board

        if not board.is_empty(point):
            return False

        for n in point.neighbors:
            if board.is_on_grid(n) and (board.color_at(n) != color):
                return False

        friendlies = 0
        off_boards = 0
        for corner in point.corners:
            if board.is_on_grid(corner):
                if board.color_at(corner) == color:
                    friendlies += 1
            else:
                off_boards += 1

        if off_boards > 0:
            return 4 == (off_boards + friendlies)

        return friendlies >= 3
