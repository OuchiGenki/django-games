from othello.game_logic import init_board

def test_init_board():
    board = init_board()

    # 8x8か？
    assert len(board) == 8
    assert all(len(row) == 8 for row in board)

    # 初期配置が正しいか？
    # W: (3,3), (4,4)
    # B: (3,4), (4,3)
    # E: その他
    assert board[3][3] == 'W'
    assert board[4][4] == 'W'
    assert board[3][4] == 'B'
    assert board[4][3] == 'B'
    for r in range(8):
        for j in range(8):
            if (r, j) not in [(3, 3), (4, 4), (3, 4), (4, 3)]:
                assert board[r][j] == 'E'
