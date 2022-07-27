import chess
import sys
from utils import *

class Bot:
    """
This is a chess bot. It is the parent class of a white and black bot.
"""
    def __init__(self, color="w", board=chess.Board(), max_depth = 2):
        """
        Initializes the bot as the white or black player.
        """
        if color != "b" and color != "w":
            raise ValueError("Bot must be initialized as w or b")
        
        self.color = "W" if color == "w" else "B"

        # board is the current game position, initialized with start positions
        self.board = board

        self.max_depth = max_depth
        
    def find_best_move(self):
        """
        Returns the best move it can find, given the current board position.
        This is done with a minimax strategy.
        max_depth: max search depth, d=1 means one move for each
        """

        return minimax(self.board, self.max_depth, self.color)

class WhiteBot(Bot):
    """
Bot with white pieces.
"""

    # Returns move that maximizes piece count
    def Max(self):

        # if no legal moves: (TODO)





        
        for m in self.board.legal_moves:
            max_move = m
            break
        max_count = check_move(self.board, max_move)
    
        for move in self.board.legal_moves:
            count = check_move(self.board, move)
            if count > max_count:
                max_count = count
                max_move = move
        return max_move, max_count
    
class BlackBot(Bot):
    """
Bot with black pieces.
"""
    # Returns move that minimizes piece count
    def Min(self):

        # if no legal moves: (TODO)



        
        for m in self.board.legal_moves:
            min_move = m
            break
        min_count = check_move(self.board, min_move)
        
        for move in self.board.legal_moves:
            count = check_move(self.board, move)
            if count < min_count:
                min_count = count
                min_move = move
        return min_move, min_count

def w_minimax(board, max_depth, cur_depth = 0):
    cur_depth += 1
    if cur_depth == max_depth:
        # check for move that maximizes count after one white and black move
        for m in board.legal_moves:
            cur_best_move = m
            break
        bbot = BlackBot("b", board)
        bbot.board.push(cur_best_move)
        _, cur_best_count = bbot.Min()
        bbot.board.pop()
        
        for move in board.legal_moves:
            bbot.board.push(move)
            _, count = bbot.Min()
            bbot.board.pop()
            if count > cur_best_count:
                cur_best_count = count
                cur_best_move = move
        return cur_best_move, cur_best_count

    if cur_depth < max_depth:
        # do w_minimax for all board positions after one white + black move
        for m in board.legal_moves:
            cur_best_move = m
            break
        board.push(cur_best_move)
        cur_best_count = -2000
        for move in board.legal_moves:
            board.push(move)
            _, count = w_minimax(board, max_depth, cur_depth)
            if count > cur_best_count:
                cur_best_count = count
            board.pop()
        board.pop()

        for w_move1 in board.legal_moves:
            board.push(w_move1)
            for b_move1 in board.legal_moves:
                board.push(b_move1)
                _, count = w_minimax(board, max_depth, cur_depth)
                if count > cur_best_count:
                    cur_best_move = w_move1
                    cur_best_count = count
                board.pop()
            board.pop()
        return cur_best_move, cur_best_count


    
def b_minimax(board, max_depth, cur_depth = 0):
    cur_depth += 1
    if cur_depth == max_depth:
        # check for move that maximizes count after one black and white move
        for m in board.legal_moves:
            cur_best_move = m
            break
        wbot = WhiteBot("w", board)
        wbot.board.push(cur_best_move)
        _, cur_best_count = wbot.Max()
        wbot.board.pop()
        
        for move in board.legal_moves:
            wbot.board.push(move)
            _, count = wbot.Max()
            wbot.board.pop()
            if count < cur_best_count:
                cur_best_count = count
                cur_best_move = move
        return cur_best_move, cur_best_count

    if cur_depth < max_depth:
        # do b_minimax for all board positions after one black + white move
        for m in board.legal_moves:
            cur_best_move = m
            break
        board.push(cur_best_move)
        cur_best_count = 2000
        for move in board.legal_moves:
            board.push(move)
            _, count = b_minimax(board, max_depth, cur_depth)
            if count < cur_best_count:
                cur_best_count = count
            board.pop()
        board.pop()

        for b_move1 in board.legal_moves:
            board.push(b_move1)
            for w_move1 in board.legal_moves:
                board.push(w_move1)
                _, count = b_minimax(board, max_depth, cur_depth)
                if count < cur_best_count:
                    cur_best_move = b_move1
                    cur_best_count = count
                board.pop()
            board.pop()
        return cur_best_move, cur_best_count
    
def minimax(board, max_depth, color, cur_depth = 0):
    if color == "W":
        return w_minimax(board, max_depth)[0]
    return b_minimax(board, max_depth)[0]
