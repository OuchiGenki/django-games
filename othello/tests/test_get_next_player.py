from othello.game_logic import get_next_player, init_board

def test_get_next_player():
    board = init_board()
    assert get_next_player(board, 'B') == 'W'

    board = [
        ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
        ['B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ['B', 'B', 'W', 'W', 'W', 'W', 'W', 'W'],
        ['B', 'W', 'B', 'B', 'W', 'W', 'W', 'W'],
        ['E', 'W', 'W', 'B', 'W', 'W', 'W', 'W'],
        ['E', 'E', 'W', 'W', 'W', 'W', 'E', 'E'],
        ['E', 'E', 'W', 'W', 'W', 'W', 'E', 'E'],
    ]
    assert get_next_player(board, 'B') == 'B'  # Wの有効な手がない場合、Bのまま