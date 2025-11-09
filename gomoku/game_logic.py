BOARD_SIZE = 15

def init_board():
    board = [['E' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    return board


def is_valid_move(board, row, col, color):
    if color not in ['B', 'W']:
        return False
    
    if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
        return False
    
    if board[row][col] != 'E':
        return False
    
    return True


