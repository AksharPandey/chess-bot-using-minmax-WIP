
import Game_rule as gr
def eval_func(board):
    score = 0
    for row in board:
        for tile in row:
            if tile == 'BP':
                score += -1
            elif tile == 'WP':
                score += 1
            elif tile == 'BN':
                score += -3
            elif tile == 'WN':
                score += 3
            elif tile == 'BB':
                score += -3
            elif tile == 'WB':
                score += 3
            elif tile == 'BR':
                score += -5
            elif tile == 'WR':
                score += 5
            elif tile == 'BQ':
                score += -9
            elif tile == 'WQ':
                score += 9
            elif tile == 'BK':
                score += -100000
            elif tile == 'WK':
                score += 100000

    
    return score


def minimax(board, depth, turn):
    if depth == 0:
        x = eval_func(board)
        return x

    elif depth < 4:
        if turn == 'W':
            score_max = float('-inf')
            x = gr.legal_filter(board, turn)
            for y in x:
                source, dest = y
                board_temp = [row[:] for row in board]  # Couldnt figure out how to create a changable temp without changing the original board. Ai'ed it
                board_temp[dest[0]][dest[1]] = board_temp[source[0]][source[1]]
                board_temp[source[0]][source[1]] = 0
                score = minimax(board_temp, depth-1, 'B')
                if score > score_max:
                    score_max = score

        elif turn == 'B':
            score_max = float('inf')
            x = gr.legal_filter(board, turn)
            for y in x:
                source, dest = y
                board_temp = [row[:] for row in board]
                board_temp[dest[0]][dest[1]] = board_temp[source[0]][source[1]]
                board_temp[source[0]][source[1]] = 0
                score = minimax(board_temp, depth-1, 'W')
                if score < score_max:
                    score_max = score
    return score_max

def get_best_move(board, depth, turn):
    if depth == 0:
        x = eval_func(board)
        return x

    elif depth < 4:
        move_max = []
        if turn == 'W':
            score_max = float('-inf')
            x = gr.legal_filter(board, turn)
            for y in x:
                source, dest = y
                board_temp = [row[:] for row in board]  # Couldnt figure out how to create a changable temp without changing the original board. Ai'ed it
                board_temp[dest[0]][dest[1]] = board_temp[source[0]][source[1]]
                board_temp[source[0]][source[1]] = 0
                score = minimax(board_temp, depth-1, 'B')
                if score > score_max:
                    score_max = score
                    move_max = [source, dest]

        elif turn == 'B':
            score_max = float('inf')
            x = gr.legal_filter(board, turn)
            for y in x:
                source, dest = y
                board_temp = [row[:] for row in board]
                board_temp[dest[0]][dest[1]] = board_temp[source[0]][source[1]]
                board_temp[source[0]][source[1]] = 0
                score = minimax(board_temp, depth-1, 'W')
                if score < score_max:
                    score_max = score
                    move_max = [source, dest]
    return move_max







