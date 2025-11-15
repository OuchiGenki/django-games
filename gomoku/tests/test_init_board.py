from gomoku.game_logic import init_board, BOARD_SIZE

def test_init_board():
    board = init_board()
    assert all(len(row) == BOARD_SIZE for row in board)
    assert all(cell == 'E' for row in board for cell in row)