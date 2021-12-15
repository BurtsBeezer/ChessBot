import chess
import sys
from anytree import Node

import PieceCount

class ChessBot:
    """
This is a chess bot.
"""
    def __init__(self,color):
        """ Initializes the bot as the black or white player.
Initializes the root of the tree for the move possibilities
"""
        if color == 'w':
            self.color = "W"
        else:
            self.color = "B"

        self.board = chess.Board()
        root = Node(chess.STARTING_FEN, count = 0)

    def play(self,board_str):
        """ Given the board_fen, returns a move in SAN notation
"""
        self.board.set_fen(board_str)
        for move in self.board.legal_moves:
            #self.board.push_uci(move)
            x = piece_count(self.board.board_fen())
            print(x)
            break
        return move
