import engine as e
import Move_Generation as mg
import Game_rule as gr

board = [["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]]

counter = 0
while True:
    turn = ''
    if counter % 2 == 0:
        turn = 'W'
    else:
        turn = 'B'

    if turn == 'W':
        num = 1
        for z in board:
            print([x if x != 0 else '--' for x in z], end='') # Couldn't figure out how to cleanly improvise board visual
            print(num)
            num += 1
        print('  1  ', '  2  ', '  3  ', '  4  ', '  5  ', '  6  ', '  7  ', '  8  ')



        source1 = int(input("Enter starting coordinate for piece (row): ")) - 1
        source2 = int(input("Enter starting coordinate for piece (column): ")) - 1
        dest1 = int(input("Enter ending coordinate for piece (row): ")) - 1
        dest2 = int(input("Enter ending coordinate for piece (column): ")) - 1

        legal_moves = gr.legal_filter(board, turn)

        if [[source1, source2], [dest1, dest2]] in legal_moves:
            board[dest1][dest2] = board[source1][source2]
            board[source1][source2] = 0

        else:
            print('Invalid Move')
            continue

    else:
        move = e.get_best_move(board, 2, turn)
        source, dest = move
        board[dest[0]][dest[1]] = board[source[0]][source[1]]
        board[source[0]][source[1]] = 0

    counter += 1








