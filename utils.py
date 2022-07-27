import chess

def piece_count(board_str):
    """Returns piece count of a chess board. Positive value
indicates white is leading, negative for black.
Accepts Forsyth-Edwards Notation for a board position"""
    x = 0
    b = chess.Board(board_str)
    if (b.is_checkmate()):
        for char in board_str:
            if char == 'w':
                return 1000
        return -1000
    if b.is_stalemate():
        return 0
    for char in board_str:
        if not(char.isalpha()):
            continue
        if char.isupper():
            if char == 'P':
                x += 1
            elif char == 'R':
                x += 5
            elif char == 'B' or char == 'N':
                x += 3
            elif char == 'Q':
                x += 9
        else:
            if char == 'p':
                x -= 1
            elif char == 'r':
                x -= 5
            elif char == 'b' or char == 'n':
                x -= 3
            elif char == 'q':
                x -= 9
    return x

def check_move(board, move):
    board.push(move)
    x = piece_count(board.board_fen())
    board.pop()
    return x
