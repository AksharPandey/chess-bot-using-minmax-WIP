import engine as e
import Game_rule as gr
import random

turn = random.choice(['W', 'B'])

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
    if counter % 2 == 0:
        turn = 'W'
    else:
        turn = 'B'

    print()
    if counter % 2 == 0:
        num = 8
        for z in board:
            print([x if x != 0 else '--' for x in z], end='')
            print(num)
            num -= 1
        print('  a  ', '  b  ', '  c  ', '  d  ', '  e  ', '  f  ', '  g  ', '  h  ')
        print()

        source = input("Enter source coordinate: ")
        dest = input("Enter destination coordinate: ")
        col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        source2 = col.index(source[0])
        source1 = 8 - int(source[1])
        dest2 = col.index(dest[0])
        dest1 = 8 - int(dest[1])

        print(source2, source1, dest2, dest1)
        legal_moves = gr.legal_filter(board, turn)

        if [[source1, source2], [dest1, dest2]] in legal_moves:
            board[dest1][dest2] = board[source1][source2]
            board[source1][source2] = 0

        else:
            print('Invalid Move')
            continue

    else:
        move = e.get_best_move(board, 3, turn)
        source, dest = move
        board[dest[0]][dest[1]] = board[source[0]][source[1]]
        board[source[0]][source[1]] = 0

    counter += 1


