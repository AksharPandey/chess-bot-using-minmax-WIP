import Move_Generation as mg

def check_detection(board, turn):
    if turn == 'W':
        kings_pos = []
        for num1, row in enumerate(board):
            for num2, tile in enumerate(row):
                if tile == 'WK':
                    kings_pos.append(num1)
                    kings_pos.append(num2)

        opp_reach = []
        for num1, row in enumerate(board):
            for num2, tile in enumerate(row):
                if tile == 'BQ':
                    opp_reach += mg.queen(num1, num2, board, 'B')

                elif tile == 'BR':
                    opp_reach += mg.rook(num1, num2, board, 'B')

                elif tile == 'BN':
                    opp_reach += mg.knight(num1, num2, board, 'B')

                elif tile == 'BB':
                    opp_reach += mg.bishop(num1, num2, board, 'B')

                elif tile == 'BP':
                    opp_reach += mg.pawn(num1, num2, board, 'B')

        if kings_pos in opp_reach:
            check = True
        else:
            check = False

        return check

    if turn == 'B':
        kings_pos = []
        for num1, row in enumerate(board):
            for num2, tile in enumerate(row):
                if tile == 'WK':
                    kings_pos.append(num1)
                    kings_pos.append(num2)

        opp_reach = []
        for num1, row in enumerate(board):
            for num2, tile in enumerate(row):
                if tile == 'WQ':
                    opp_reach += mg.queen(num1, num2, board, 'W')

                elif tile == 'WR':
                    opp_reach += mg.rook(num1, num2, board, 'W')

                elif tile == 'WN':
                    opp_reach += mg.knight(num1, num2, board, 'W')

                elif tile == 'WB':
                    opp_reach += mg.bishop(num1, num2, board, 'W')

                elif tile == 'WP':
                    opp_reach += mg.pawn(num1, num2, board, 'W')

        if kings_pos in opp_reach:
            check = True
        else:
            check = False

        return check


def legal_filter(board, turn):
    legal_turns = []
    for num1, row in enumerate(board):
        for num2, tile in enumerate(row):
            if tile != 0 and tile[0] == turn:
                if tile[1] == 'K':
                    dest = mg.king(num1, num2, board, turn)
                elif tile[1] == 'Q':
                    dest = mg.queen(num1, num2, board, turn)
                elif tile[1] == 'P':
                    dest = mg.pawn(num1, num2, board, turn)
                elif tile[1] == 'B':
                    dest = mg.bishop(num1, num2, board, turn)
                elif tile[1] == 'N':
                    dest = mg.knight(num1, num2, board, turn)
                elif tile[1] == 'R':
                    dest = mg.rook(num1, num2, board, turn)

                for index, x in enumerate(dest):
                    board_temp = [row[:] for row in board]  # Couldnt figure out how to create a changable temp without changing the original board.
                    board_temp[num1][num2] = 0
                    board_temp[x[0]][x[1]] = tile
                    cd = check_detection(board_temp, turn)
                    if not cd:
                        legal_turns.append([[num1, num2], x])


    return legal_turns









