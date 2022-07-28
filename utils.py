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

def get_a_move(board):
    for m in board.legal_moves:
        cur_best_move = m
        break
    x = 0
    # prioritize castling, then checks, then captures, then pawn moves
    if board.is_castling(cur_best_move):
        x += 0.3
    elif board.gives_check(cur_best_move):
        x += 0.2
    elif board.is_capture(cur_best_move):
        x += 0.1
    san_move = board.san(cur_best_move)
    for l in san_move:
        if l.isupper():
            x -= 0.1
            break
    best_x = x
    for m in board.legal_moves:
        x = 0
        # prioritize castling, then checks, then captures, then pawn moves
        if board.is_castling(m):
            x += 0.3
        elif board.gives_check(m):
            x += 0.2
        elif board.is_capture(m):
            x += 0.1
        san_move = board.san(m)
        for l in san_move:
            if l.isupper():
                x -= 0.1
                break
        if x > best_x:
            best_x = x
            cur_best_move = m
    return cur_best_move



        
