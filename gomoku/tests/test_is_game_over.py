from gomoku.game_logic import is_game_over, init_board, BOARD_SIZE

def test_is_game_over():
    board = init_board()
    assert is_game_over(board) == {'flag': False, 'winner': None}   # 初期盤面

    board = [['X' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]   # 塗りつぶし盤面
    assert is_game_over(board) == {'flag': True, 'winner': None}

    board = init_board()
    for i in range(5):
        board[0][i] = 'B'
    assert is_game_over(board) == {'flag': True, 'winner': 'B'} # 横5連続

    board = init_board()
    for i in range(5):
        board[i][0] = 'W'
    assert is_game_over(board) == {'flag': True, 'winner': 'W'} # 縦5連続

    board = init_board()
    for i in range(5):
        board[i][i] = 'B'
    assert is_game_over(board) == {'flag': True, 'winner': 'B'} # 斜め5連続

    board = init_board()
    for i in range(5):
        board[i][4 - i] = 'W'
    assert is_game_over(board) == {'flag': True, 'winner': 'W'} # 逆斜め5連続

    board = init_board()
    for i in range(5):
        board[0][i] = 'B'
    board[0][2] = 'W'
    assert is_game_over(board) == {'flag': False, 'winner': None} # BBWBB 連続なし