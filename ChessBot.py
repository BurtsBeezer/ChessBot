import chess
import sys
#from anytree import Node

from PieceCount import *

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
        self.move_tree = dict()
        # root
        self.move_tree[chess.STARTING_FEN] = (0, dict())
        
    def play(self,board_str):
        """ Given the board_fen, returns a move in SAN notation
"""
        self.board.set_fen(board_str)
        max_x, min_x = 0, 0
        for move in self.board.legal_moves:
            max_move, min_move = move, move
        for move in self.board.legal_moves:
            self.board.push(move)
            x = piece_count(self.board.board_fen())
            if x >= max_x:
                max_x = x
                max_move = move
            if x <= min_x:
                min_x = x
                min_move = move
            self.move_tree[chess.STARTING_FEN][1][self.board.board_fen()] = (x, move)
            self.board.pop()
        if self.color == "W":
            return max_move
        else:
            return min_move
