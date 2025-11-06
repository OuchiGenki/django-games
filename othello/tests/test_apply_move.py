from othello.game_logic import init_board, apply_move, is_valid_move
import pytest

def test_apply_move_valid():
    board = init_board()
    # 初期状態で有効な手を適用
    row, col, color = 2, 3, 'B'
    assert is_valid_move(board, row, col, color)  # 有効な手であることを確認
    updated_board = apply_move(board, row, col, color)
    assert updated_board[row][col] == 'B'  # 石が置かれていることを確認
    assert updated_board[3][3] == 'B'  # 反転が正しいことを確認

def test_apply_move_invalid():
    board = init_board()
    # 無効な手を適用
    row, col, color = 0, 0, 'B'
    with pytest.raises(ValueError, match=f"Invalid move at \\({row}, {col}\\) for color {color}"):
        apply_move(board, row, col, color)

def test_apply_move_edge_case():
    board = init_board()
    # 境界条件のテスト
    row, col, color = 0, 7, 'B'
    assert not is_valid_move(board, row, col, color)  # 無効な手であることを確認
    with pytest.raises(ValueError):
        apply_move(board, row, col, color)

def test_apply_move_multiple_flips():
    board = init_board()

    row, col, color = 2, 3, 'B'
    assert apply_move(board, row, col, color)
    row, col, color = 2, 4, 'W'
    assert apply_move(board, row, col, color)
    row, col, color = 2, 5, 'B'
    assert apply_move(board, row, col, color)
    # (2,4)と(3,4)が'B'に反転されていることを確認
    assert board[2][4] == 'B'   
    assert board[3][4] == 'B'
