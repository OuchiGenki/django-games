BOARD_SIZE = 8
mid = BOARD_SIZE // 2

def init_board():
    board = [['E' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    board[mid-1][mid-1] = 'W'
    board[mid-1][mid] = 'B'
    board[mid][mid-1] = 'B'
    board[mid][mid] = 'W'

    return board


def get_flippable_positions(board, row, col, color):
    DIRECTIONS = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
    flippable_positions = []

    if color not in ['B', 'W']:
        return flippable_positions

    if board[row][col] != 'E':
        return flippable_positions
    
    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        tmp = []

        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
            if board[r][c] == 'E':
                break
            elif board[r][c] != color:
                tmp.append((r, c))
            else:
                if tmp:
                    flippable_positions += tmp
                break
        
            r += dr
            c += dc
    
    return flippable_positions


def is_valid_move(board, row, col, color):
    if color not in ['B', 'W']:
        return False
    
    if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
        return False

    if board[row][col] != 'E':
        return False

    if get_flippable_positions(board, row, col, color):
        return True
    else:
        return False


def apply_move(board, row, col, color):
    if not is_valid_move(board, row, col, color):
        raise ValueError(f"Invalid move at ({row}, {col}) for color {color}")
    
    positions = get_flippable_positions(board, row, col, color)
    board[row][col] = color

    for r, c in positions:
        board[r][c] = color
    
    return board


def get_valid_moves(board, color):
    positions = []

    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if is_valid_move(board, r, c, color):
                positions.append((r, c))
                
    return positions


def is_game_over(board):
    count = 0
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] != 'E':
                count += 1
    
    if count == BOARD_SIZE * BOARD_SIZE:
        return True
    
    if not get_valid_moves(board, 'B') and not get_valid_moves(board, 'W'):
        return True 
    
    return False


def get_result(board):
    black_count = 0
    white_count = 0

    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] == 'B':
                black_count += 1
            elif board[r][c] == 'W':
                white_count += 1

    if black_count > white_count:
        winner = 'BLACK'
    elif white_count > black_count:
        winner = 'WHITE'
    else:
        winner = 'DRAW'

    return {'black_count': black_count, 'white_count': white_count, 'winner': winner}


def get_next_player(board, current_player):
    next_player = 'W' if current_player == 'B' else 'B'

    if get_valid_moves(board, next_player):
        return next_player
    
    if get_valid_moves(board, current_player):
        return current_player
    
    return None  # ゲーム終了
