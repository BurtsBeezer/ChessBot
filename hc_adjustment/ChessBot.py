import chess


class ChessBot:
    """
    This is a chess bot."""

    def __init__(self, color):
        """Initializes the bot as the black or white player.
        Initializes the root of the tree for the move possibilities"""
        if color == "W":
            self.color = "W"
        else:
            self.color = "B"

        self.board = chess.Board()
        self.move_tree = dict()
        # root
        self.move_tree[chess.STARTING_FEN] = (0, dict())

    def play(self, board_str):
        """Given the board_fen, returns a move in SAN notation"""
        self.board.set_fen(board_str)
        self.board.turn = self.color == "W"
        max_x = 0
        for move in self.board.legal_moves:
            max_move = move
            break
        for move in self.board.legal_moves:
            self.board.push(move)
            x = piece_count(self.board.board_fen(), self.color)
            self.board.pop()
            if x >= max_x:
                max_x = x
                max_move = move

        return max_move


def piece_count(board_str, color="W"):
    """Returns piece count of a chess board. Positive value
    indicates white is leading, negative for black.
    Accepts Forsyth-Edwards Notation for a board position"""
    x = 0
    factor = 1 if (color == "W") else -1
    board = chess.Board(board_str)
    # board_str[:board_str.index(' ')]
    if board.is_checkmate():
        if board.turn:
            return factor * 1000
        else:
            return factor * -1000
    if board.is_stalemate():
        return 0
    for char in board_str:
        if not (char.isalpha()):
            continue
        if char.isupper():
            if char == "P":
                x += 1
            elif char == "R":
                x += 5
            elif char == "B" or char == "N":
                x += 3
            elif char == "Q":
                x += 9
        else:
            if char == "p":
                x -= 1
            elif char == "r":
                x -= 5
            elif char == "b" or char == "n":
                x -= 3
            elif char == "q":
                x -= 9
        if x > 0:
            a = 2
    return factor * x
