def knight(r, c, board, turn):
    try:
        change = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
        t_moves = []
        for z, y in change:
            t_moves.append([z+r, y+c])
        next_moves = []
        for x, y in t_moves:
            if 0 <= x <= 7 and 0 <= y <= 7 and ((not board[x][y]) or board[x][y][0] != turn):
                next_moves.append([x, y])

        return list(next_moves)
    except Exception as e:
        print("Error in knight function", e)
        return False


def rook(r, c, board, turn):
    try:
        change = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        next_turn = []
        for x in change:
            t_turn = [r, c]
            for z in range(8):
                turn1 = [t_turn[0] + x[0], t_turn[1] + x[1]]
                r1, c1 = turn1
                if 0 <= r1 <= 7 and 0 <= c1 <= 7 and ((not board[r1][c1]) or board[r1][c1][0] != turn):
                    next_turn.append(turn1)
                    t_turn = turn1
                    if board[r1][c1] and board[r1][c1][0] != turn:
                        break  # cuz yk cant move after taking a piece
                else:
                    break

        return next_turn

    except Exception as e:
        print("Error in rook function", e)
        return False


def bishop(r, c, board, turn):
    try:
        change = [[-1, -1], [1, 1], [-1, 1], [1, -1]]
        next_turn = []
        for x in change:
            t_turn = [r, c]
            for z in range(8):
                turn1 = [t_turn[0] + x[0], t_turn[1] + x[1]]
                r1, c1 = turn1
                if 0 <= r1 <= 7 and 0 <= c1 <= 7 and ((not board[r1][c1]) or board[r1][c1][0] != turn):
                    next_turn.append(turn1)
                    t_turn = turn1
                    if board[r1][c1] and board[r1][c1][0] != turn:
                        break  # cuz yk cant move after taking a piece
                else:
                    break

        return next_turn
    except Exception as e:
        print("Error in bishop function", e)
        return False


def queen(r, c, board, turn):
    try:
        change = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
        next_turn = []
        for x in change:
            t_turn = [r, c]
            for z in range(8):
                turn1 = [t_turn[0] + x[0], t_turn[1] + x[1]]
                r1, c1 = turn1
                if 0 <= r1 <= 7 and 0 <= c1 <= 7 and ((not board[r1][c1]) or board[r1][c1][0] != turn):
                    next_turn.append(turn1)
                    t_turn = turn1
                    if board[r1][c1] and board[r1][c1][0] != turn:
                        break  # cuz yk cant move after taking a piece
                else:
                    break

        return next_turn

    except Exception as e:
        print("Error in queen function", e)
        return False


def pawn(r, c, board, turn):
    try:
        next_turn = []
        if turn == 'B':
            change = [[1, 0]]
        else:
            change = [[-1, 0]]

        if turn == 'B':
            take = [[1, -1], [1, 1]]
        else:
            take = [[-1, 1], [-1, -1]]

        if turn == 'B' and r == 1 and not board[3][c] and not board[2][c]:
            next_turn.append([3, c])
            next_turn.append([2, c])
        elif turn == 'W' and r == 6 and not board[4][c] and not board[5][c]:
            next_turn.append([4, c])
            next_turn.append([5, c])

        for x in change:
            for z in range(1):
                go_turn = [r + x[0], c + x[1]]
                r1, c1 = go_turn
                if 0 <= r1 <= 7 and 0 <= c1 <= 7 and not board[r1][c1]:
                    next_turn.append(go_turn)

        for x in take:
            for z in range(1):
                take_turn = [r + x[0], c + x[1]]
                r1, c1 = take_turn
                if 0 <= r1 <= 7 and 0 <= c1 <= 7 and board[r1][c1] and board[r1][c1][0] != turn:
                    next_turn.append(take_turn)

        x = list(next_turn)
        next_turn = []
        for y in x:
            if y not in next_turn:
                next_turn.append(y)

        return list(next_turn)
    except Exception as e:
        print("Error in pawn function", e)
        return False


def king(r, c, board, turn):
    try:
        change = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
        next_turn = []
        for x in change:
            for z in range(1):
                turn1 = [r + x[0], c + x[1]]
                r1, c1 = turn1
                if 0 <= r1 <= 7 and 0 <= c1 <= 7 and ((not board[r1][c1]) or board[r1][c1][0] != turn):
                    next_turn.append(turn1)
                    if board[r1][c1] and board[r1][c1][0] != turn:
                        break  # cuz yk cant move after taking a piece
                else:
                    break

        return next_turn

    except Exception as e:
        print("Error in king function", e)
        return False
