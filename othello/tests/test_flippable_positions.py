from othello.game_logic import init_board, get_flippable_positions

def test_flippable_positions():
    board = init_board()

    # ひっくり返せる石がある場合
    row, col, color = 2, 3, 'B'
    expected = [(3, 3)]
    result = get_flippable_positions(board, row, col, color)
    assert result == expected

    # ひっくり返せる石がない場合
    row, col, color = 0, 0, 'B'
    expected = []
    result = get_flippable_positions(board, row, col, color)
    assert result == expected

    # 無効な色の場合
    row, col, color = 2, 3, 'X'
    result = get_flippable_positions(board, row, col, color)
    assert result == []
