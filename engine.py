import Game_rule as gr

pawn_table = [[0, 0, 0, 0, 0, 0, 0, 0],
              [50, 50, 50, 50, 50, 50, 50, 50],
              [10, 10, 20, 30, 30, 20, 10, 10],
              [5, 5, 10, 25, 25, 10, 5, 5],
              [0, 0, 0, 20, 20, 0, 0, 0],
              [5, -5, -10, 0, 0, -10, -5, 5],
              [5, 10, 10, -20, -20, 10, 10, 5],
              [0, 0, 0, 0, 0, 0, 0, 0]]

knight_table = [
    [-50, -40, -30, -30, -30, -30, -40, -50],
    [-40, -20, 0, 0, 0, 0, -20, -40],
    [-30, 0, 10, 15, 15, 10, 0, -30],
    [-30, 5, 15, 20, 20, 15, 5, -30],
    [-30, 0, 15, 20, 20, 15, 0, -30],
    [-30, 5, 10, 15, 15, 10, 5, -30],
    [-40, -20, 0, 5, 5, 0, -20, -40],
    [-50, -40, -30, -30, -30, -30, -40, -50]
]

bishop_table = [
    [-20, -10, -10, -10, -10, -10, -10, -20],
    [-10, 0, 0, 0, 0, 0, 0, -10],
    [-10, 0, 5, 10, 10, 5, 0, -10],
    [-10, 5, 5, 10, 10, 5, 5, -10],
    [-10, 0, 10, 10, 10, 10, 0, -10],
    [-10, 10, 10, 10, 10, 10, 10, -10],
    [-10, 5, 0, 0, 0, 0, 5, -10],
    [-20, -10, -10, -10, -10, -10, -10, -20]
]

rook_table = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [5, 10, 10, 10, 10, 10, 10, 5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [0, 0, 0, 5, 5, 0, 0, 0]
]

queen_table = [
    [-20, -10, -10, -5, -5, -10, -10, -20],
    [-10, 0, 0, 0, 0, 0, 0, -10],
    [-10, 0, 5, 5, 5, 5, 0, -10],
    [-5, 0, 5, 5, 5, 5, 0, -5],
    [0, 0, 5, 5, 5, 5, 0, -5],
    [-10, 5, 5, 5, 5, 5, 0, -10],
    [-10, 0, 5, 0, 0, 0, 0, -10],
    [-20, -10, -10, -5, -5, -10, -10, -20]
]

king_table = [
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-20, -30, -30, -40, -40, -30, -30, -20],
    [-10, -20, -20, -20, -20, -20, -20, -10],
    [20, 20, 0, 0, 0, 0, 20, 20],
    [20, 30, 10, 0, 0, 10, 30, 20]
]


def eval_func(board, turn):
    try:
        score = 0
        for num1, row in enumerate(board):
            for num2, tile in enumerate(row):
                if tile == 0:
                    continue
                elif tile == 'BP':
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
                    score += -0
                elif tile == 'WK':
                    score += 0

                #  Piece square table thing, i understand a bit, im just going off based off that
                #  Generated the piece square table values using AI, but realised that they would be too much according to
                #  my scoring system rn, so imma just divide the values by 10

                if tile == 0:
                    continue
                elif tile == 'BP':
                    score += pawn_table[::-1][num1][num2]/100
                elif tile == 'WP':
                    score += pawn_table[num1][num2]/100
                elif tile == 'BN':
                    score += knight_table[::-1][num1][num2]/100
                elif tile == 'WN':
                    score += knight_table[num1][num2]/100
                elif tile == 'BB':
                    score += bishop_table[::-1][num1][num2]/100
                elif tile == 'WB':
                    score += bishop_table[num1][num2]/100
                elif tile == 'BR':
                    score += rook_table[::-1][num1][num2]/100
                elif tile == 'WR':
                    score += rook_table[num1][num2]/100
                elif tile == 'BQ':
                    score += queen_table[::-1][num1][num2]/100
                elif tile == 'WQ':
                    score += queen_table[num1][num2]/100
                elif tile == 'BK':
                    score += king_table[::-1][num1][num2]/100
                elif tile == 'WK':
                    score += king_table[num1][num2]/100

        return score

    except Exception as e:
        print("Error in eval func function", e)
        return False


def minimax(board, depth, turn, alpha=float('-inf'), beta=float('inf')):
    try:
        if depth == 0:
            return eval_func(board, turn)

        moves = gr.legal_filter(board, turn)
        if len(moves) == 0:
            if gr.check_detection(board, turn):
                return -1000 - depth if turn == 'W' else 1000 + depth
            return 0

        if turn == 'W':
            score_max = float('-inf')
            for source, dest in moves:
                board_temp = [row[:] for row in board]
                board_temp[dest[0]][dest[1]] = board_temp[source[0]][source[1]]
                board_temp[source[0]][source[1]] = 0

                score = minimax(board_temp, depth - 1, 'B', alpha, beta)
                score_max = max(score_max, score)
                alpha = max(alpha, score_max)
                if beta <= alpha:      # Black already has a better option elsewhere
                    break
            return score_max

        else:
            score_min = float('inf')
            for source, dest in moves:
                board_temp = [row[:] for row in board]
                board_temp[dest[0]][dest[1]] = board_temp[source[0]][source[1]]
                board_temp[source[0]][source[1]] = 0

                score = minimax(board_temp, depth - 1, 'W', alpha, beta)
                score_min = min(score_min, score)
                beta = min(beta, score_min)
                if beta <= alpha:      # White already has a better option elsewhere
                    break
            return score_min

    except Exception as e:
        print("Error in minimax function", e)
        return False


def get_best_move(board, depth, turn):
    try:
        if depth == 0:
            x = eval_func(board, turn)
            return x

        elif depth <= 4:
            move_max = []
            if turn == 'W':
                score_max = float('-inf')
                x = gr.legal_filter(board, turn)
                x = sorted(x, key=lambda move: board[move[1][0]][move[1][1]] != 0, reverse=True)
                move_max = list(x[0])
                for y in x:
                    source, dest = y
                    board_temp = [row[:] for row in board]
                    #  Couldn't figure out how to create a changable temp without changing the original board. Ai'ed it
                    board_temp[dest[0]][dest[1]] = board_temp[source[0]][source[1]]
                    board_temp[source[0]][source[1]] = 0
                    score = minimax(board_temp, depth-1, 'B')
                    if score > score_max:
                        score_max = score
                        move_max = [source, dest]

            elif turn == 'B':
                score_max = float('inf')
                x = gr.legal_filter(board, turn)
                x = sorted(x, key=lambda move: board[move[1][0]][move[1][1]] != 0, reverse=True)
                move_max = list(x[0])
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

    except Exception as e:
        print("Error in get best move function", e)
        return False






