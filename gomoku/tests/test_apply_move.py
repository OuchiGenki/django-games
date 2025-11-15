from gomoku.game_logic import init_board, apply_move

def test_apply_move():
    board = init_board()
    assert board[3][3] == 'E'

    row, col, color = 3, 3, 'B'
    board = apply_move(board, row, col, color)
    assert board[3][3] == 'B'