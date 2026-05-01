
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


board1 = [["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]]


def minimax(board, depth, turn):
    if depth == 0:
        x = eval_func(board)
        return x

    elif depth < 4:
        score_max = 0
        move_max = []
        if turn == 'W':
            x = gr.legal_filter(board)
            for y in x:
                for source, dest in y:
                    board_temp = [row[:] for row in board]  # Couldnt figure out how to create a changable temp without changing the original board. Ai'ed it
                    board_temp[dest[0]][dest[1]] = board_temp[source[0]][source[1]]
                    board_temp[source[0]][source[1]] = 0
                    score = eval_func(board_temp)
                    if score > score_max:
                        score_max = score









