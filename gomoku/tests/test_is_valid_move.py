from gomoku.game_logic import init_board, is_valid_move, BOARD_SIZE

def test_is_valid_move():
    board = init_board()

    assert is_valid_move(board, 5, 5, 'B') == True
    assert is_valid_move(board, 5, 5, 'W') == True
    assert is_valid_move(board, 5, 5, 'X') == False

    assert is_valid_move(board, 2, 3, 'B') == True
    assert is_valid_move(board, 2, BOARD_SIZE, 'B') == False
    assert is_valid_move(board, -1, 0, 'W') == False

    board[7][7] = 'B'
    assert is_valid_move(board, 7, 7, 'W') == False