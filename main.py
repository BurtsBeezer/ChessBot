import chess
import sys

import ChessBot

bot1 = ChessBot.ChessBot('w')

move = bot1.play(chess.STARTING_FEN)

print(move)
