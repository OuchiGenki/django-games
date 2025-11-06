from othello.game_logic import get_result

def test_get_winner():
    board = [['W' for _ in range(8)] for _ in range(8)]
    board[1][1] = 'B'
    board[2][2] = 'B'
    # 'W'の方が多い場合
    result = get_result(board)
    assert result['black_count'] == 2
    assert result['white_count'] == 62
    assert result['winner'] == 'WHITE'

    board = [['B' for _ in range(8)] for _ in range(8)]
    board[7][7] = 'W'
    board[5][5] = 'W'
    board[6][6] = 'W'
    # 'B'の方が多い場合
    result = get_result(board)
    assert result['black_count'] == 61
    assert result['white_count'] == 3
    assert result['winner'] == 'BLACK'

    board = [['W' for _ in range(8)] for _ in range(8)]
    for r in range(8):
        for c in range(8):
            if (r + c) % 2 == 0:
                board[r][c] = 'B'
    # 引き分けの場合
    result = get_result(board)
    assert result['black_count'] == 32
    assert result['white_count'] == 32
    assert result['winner'] == 'DRAW'