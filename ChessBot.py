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
        max_x = 0
        for move in self.board.legal_moves:
            max_move = move
            break
        for move in self.board.legal_moves:
            self.board.push(move)
            x = piece_count(self.board.board_fen())
            if x >= max_x:
                max_x = x
                max_move = move
            #self.move_tree[chess.STARTING_FEN][1][self.board.board_fen()] = (x, move)
            #self.board.pop()

        # black's move
        
        #for move in self.move_tree[chess.STARTING_FEN][1][self.board.board.fen()][1]:
         #   self.board.push(move)
         #   for move2 in self.board.legal_moves:
          #      self.board.push(move)
           #     x = piece_count(self.board.board.fen())
                



            
            #self.board.pop(move)













            
        if self.color == "W":
            return max_move
        else:
            return min_move
