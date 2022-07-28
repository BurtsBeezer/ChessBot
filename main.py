import sys
import chess
import time

import ChessBot

p1 = ChessBot.Bot(max_depth = 2)

timer_start = time.time()
best_move = p1.find_best_move()
timer_end = time.time()
time_elapsed = timer_end - timer_start

print("Best move: {}".format(best_move))
print("Time to find move: {}".format(time_elapsed))
