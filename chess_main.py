import engine as e
import Game_rule as gr
import random
import time as s

turn = random.choice(['W', 'B'])

board = [["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]]

bh = input("Enter other opponent (Bot/Human): ")
counter = 0
try:
    while True:
        if counter % 2 == 0:
            turn = 'W'
        else:
            turn = 'B'

        print()
        if counter != 0:
            print("(Half) Move: " + str(counter))
        num = 8
        for z in board:
            print([x if x != 0 else '--' for x in z], end='')
            print(num)
            num -= 1
        print('  a  ', '  b  ', '  c  ', '  d  ', '  e  ', '  f  ', '  g  ', '  h  ')
        print()


        if counter % 2 == 0 and bh == 'B':
            print("Bot is thinking", end='')
            move = e.get_best_move(board, 3, turn)
            print('.', end='')

            source, dest = move

            col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            row = [1, 2, 3, 4, 5, 6, 7]

            legal_moves = gr.legal_filter(board, turn)
            if [[source[0], source[1]], [dest[0], dest[1]]] in legal_moves:
                board[dest[0]][dest[1]] = board[source[0]][source[1]]
                board[source[0]][source[1]] = 0

            elif not legal_moves:
                print("Checkmate")
                break

            else:
                print("Bot made invalid move, gotta fix that!!!")
                continue

            s.sleep(0.5)
            print('.', end='')
            s.sleep(0.5)
            print('.')

            print("Bot plays: " + str(board[dest[0]][dest[1]][1]) + col[dest[1]] + str(8 - dest[0]))

        elif counter % 2 == 0 and bh == 'H':
            source = input("Enter source coordinate (R to resign game): ")

            if source == 'R':
                print("Game resigned")    
                break

            dest = input("Enter destination coordinate: ")
            col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            row = [1, 2, 3, 4, 5, 6, 7]

            source2 = col.index(source[0])
            source1 = 8 - int(source[1])
            dest2 = col.index(dest[0])
            dest1 = 8 - int(dest[1])

            legal_moves = gr.legal_filter(board, turn)

            if [[source1, source2], [dest1, dest2]] in legal_moves:
                board[dest1][dest2] = board[source1][source2]
                board[source1][source2] = 0

            elif not legal_moves:
                print("Checkmate")
                break

            else:
                print('Invalid Move')
                continue

        else:
            print("Bot is thinking", end='')
            move = e.get_best_move(board, 3, turn)
            print('.', end='')

            source, dest = move

            col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            row = [1, 2, 3, 4, 5, 6, 7]

            legal_moves = gr.legal_filter(board, turn)
            if [[source[0], source[1]], [dest[0], dest[1]]] in legal_moves:
                board[dest[0]][dest[1]] = board[source[0]][source[1]]
                board[source[0]][source[1]] = 0

            elif not legal_moves:
                print("Checkmate")
                break

            else:
                print("Bot made invalid move, gotta fix that!!!")
                continue

            s.sleep(0.5)
            print('.', end='')
            s.sleep(0.5)
            print('.')

            print("Bot plays: " + str(board[dest[0]][dest[1]][1]) + col[dest[1]] + str(8 - dest[0]))


        counter += 1

except Exception as e:
    print("Error: ", e)
