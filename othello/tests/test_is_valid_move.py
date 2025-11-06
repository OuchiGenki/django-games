from othello.game_logic import init_board, is_valid_move

def test_is_valid_move():
    board = init_board()

    # (2, 3)に'B'を置くのは有効な手
    assert is_valid_move(board, 2, 3, 'B') == True

    # (1, 0)に'B'を置くのは無効な手（ひっくり返せる石がない）
    assert is_valid_move(board, 1, 0, 'B') == False

    # (3, 3)に'B'を置くのは無効な手（すでに石が置かれている）
    assert is_valid_move(board, 3, 3, 'B') == False

    # ボード範囲外の座標は無効な手
    assert is_valid_move(board, -1, 0, 'B') == False
    assert is_valid_move(board, 8, 8, 'W') == False

    # 無効な色の場合は無効な手
    assert is_valid_move(board, 2, 3, 'X') == False
