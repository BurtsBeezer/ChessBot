import sys
import chess

import ChessBot

p1 = ChessBot.Bot(max_depth = 2)

best_move = p1.find_best_move()

print(best_move)
