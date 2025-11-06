from othello.game_logic import get_valid_moves, init_board

def test_get_valid_moves():
    board = init_board()
    assert get_valid_moves(board, 'B') == [(2, 3), (3, 2), (4, 5), (5, 4)]
    assert get_valid_moves(board, 'W') == [(2, 4), (3, 5), (4, 2), (5, 3)]

    board = [
        ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'B', 'E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'B', 'W', 'W', 'E', 'E'],
        ['E', 'E', 'E', 'B', 'B', 'W', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'B', 'W', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
    ]
    assert get_valid_moves(board, 'W') == [(1, 1), (3, 2), (4, 2), (5, 2), (5, 3), (6, 3), (6, 4)]