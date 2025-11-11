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


def apply_move(board, row, col, color):
    if not is_valid_move(board, row, col, color):
        return [r[:] for r in board]
    
    new_board = [r[:] for r in board]
    new_board[row][col] = color

    return new_board


def is_game_over(board):
    flag = False
    winner = None

    DIR = [(0, 1), (1, 1), (1, 0), (1, -1)]
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] == 'E':
                continue
            color = board[r][c]
            for dr, dc in DIR:
                streak = 0
                for k in range(5):
                    nr, nc = r + dr*k, c + dc*k
                    if nr < 0 or nr >= BOARD_SIZE or nc < 0 or nc >= BOARD_SIZE:
                        break
                    if board[nr][nc] == color and color in ['B', 'W']:
                        streak += 1
                    else:
                        break

                if streak == 5:
                    flag = True
                    winner = color

    if sum(1 for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] == 'E') == 0:
        flag = True

    return {'flag': flag, 'winner': winner}