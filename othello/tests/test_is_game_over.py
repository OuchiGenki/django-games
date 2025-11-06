from othello.game_logic import init_board, is_game_over

def test_is_game_over():
    board = init_board()

    # 初期状態ではゲームオーバーではない
    assert is_game_over(board) == False

    # すべてのマスが埋まっている場合
    for r in range(8):
        for c in range(8):
            board[r][c] = 'B'  # すべて'B'で埋める
    assert is_game_over(board) == True


    board = [
        ['E', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
        ['W', 'B', 'W', 'W', 'W', 'W', 'W', 'B'],
        ['W', 'B', 'B', 'W', 'B', 'W', 'W', 'B'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['W', 'B', 'B', 'W', 'B', 'W', 'W', 'B'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'B', 'B'],
        ['W', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ]
    
    # 両プレイヤーに有効な手がない場合
    assert is_game_over(board) == True