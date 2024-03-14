from .player import Player
from .point import Point

COLS = 'ABCDEFGHJKLMNOPQRST'
STONE_TO_STR = {
    None: ' . ',
    Player.black: ' * ',
    Player.white: ' o ',
}

def print_move(player, move):
    if move.is_pass:
        move_str = 'passes'
    elif move.is_resign:
        move_str = 'resigns'
    else:
        move_str = f'{COLS[move.point.col]}{move.point.row + 1}'

    print(f'{player} {move_str}')

def print_board(board):
    lines, line_parts = [], []
    push_line, push_part = lines.append, line_parts.append

    push_part('   ')
    for c in range(board.cols):
        push_part(f' {COLS[c]} ')
    push_line(''.join(line_parts))

    for r in range(board.rows):
        line_parts.clear()
        for c in range(board.cols):
            push_part(STONE_TO_STR[board.color_at(Point(row=r, col=c))])
        push_line(f'{r + 1:2d} {"".join(line_parts)}')

    for line in reversed(lines):
        print(line)
