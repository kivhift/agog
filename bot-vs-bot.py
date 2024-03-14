#!/usr/bin/env python3

import time

from go.agent.naive import RandomBot
from go.game import Game
from go.player import Player
from go.utils import print_board, print_move

def main():
    clear_and_home = '\x1b[2J\x1b[H\x1b[0m'
    bots = {
        Player.black: RandomBot(),
        Player.white: RandomBot(),
    }

    game = Game.new(9)
    while not game.is_over:
        time.sleep(.3)

        print(clear_and_home, end='')
        print_board(game.board)
        move = bots[game.next_player].select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)

if '__main__' == __name__:
    main()
