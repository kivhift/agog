import random

from . import Agent
from ..move import Move
from ..point import Point

class RandomBot(Agent):
    def select_move(self, state):
        '''Choose a random move that preserves our own eyes.'''

        candidates = []
        for r in range(state.board.rows):
            for c in range(state.board.cols):
                candidate = Point(row=r, col=c)
                if (
                    state.is_valid(Move.play(candidate))
                    and not state.is_an_eye(candidate, state.next_player)
                ):
                    candidates.append(candidate)

        return Move.play(random.choice(candidates)) if candidates else Move.pass_()
