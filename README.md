# Python Chess Engine
 
A chess engine I built from scratch in Python — no chess libraries, no shortcuts. Every piece of logic from move generation to the minmax algorithm is written manually.
 
Built this as a project to sharpen my logical thinking and programming before starting university. 
Pygame GUI exists but isnt included in the project
 
## What it does
 
- Generates legal moves for all 6 piece types, including edge cases like pins and blocking pieces
- Filters out any move that leaves your own king in check
- Uses minimax search to pick the best move for the bot
- Scores positions based on material count
- Runs as a human vs bot game in the terminal
- Checkmate detection
- Alpha beta pruning implemented

## Project Structure
 
```
chess/
├── main.py              # Game loop and terminal UI
├── Move_Generation.py   # Move generation for each piece type
├── Game_rule.py         # Check detection and legal move filtering
└── engine.py            # Evaluation function, minimax, best move selection
```
 
## How the AI works
 
The bot uses minimax search — it looks ahead a few moves, assumes both sides play optimally, and picks the move that leads to the best position. White tries to maximize the score, black tries to minimize it.
 
Positions are evaluated purely by material:
 
| Piece | Value |
|-------|-------|
| Pawn | ±1 |
| Knight | ±3 |
| Bishop | ±3 |
| Rook | ±5 |
| Queen | ±9 |
| King | ±100000 |
 
Positive = good for white, negative = good for black.
 
## How to run
 
```
chess_main.py
```
 
Enter coordinates as row and column numbers (1-indexed). The board is printed after each move with row numbers on the right and column numbers along the bottom.
 
## Known limitations / planned improvements
 
- No castling or en passant yet
- No pawn promotion
- Terminal UI is minimal / Gonna add a GUI 

## What I learned
 
Writing move generation for sliding pieces taught me a lot about structuring directional loops cleanly. The hardest part was check detection — you have to simulate every candidate move on a board copy before committing, which is expensive but necessary. Minimax clicked once I stopped thinking about it as a tree and started thinking about it as two players taking turns being greedy.

## Bot vs Human Game
<img width="410" height="835" alt="image" src="https://github.com/user-attachments/assets/4849d5fb-6895-4236-ab47-c48b84aaff77" />
<img width="406" height="609" alt="image" src="https://github.com/user-attachments/assets/9136c482-f805-4193-8530-5c2f0206efc1" />


## Bot vs Bot Game
<img width="410" height="837" alt="image" src="https://github.com/user-attachments/assets/c2160c2d-46f0-4f94-bacf-36c5b4b22b19" />



