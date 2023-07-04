import chess

def anti_legal_moves(board):
    validmoves = list(board.legal_moves)

    capture_move = []

    for moves in validmoves:
        if board.is_capture(moves):
            capture_move.append(moves)
        if board.is_en_passant(moves):
            capture_move.append(moves)
        else:
            capture_move = capture_move

    if capture_move == []:
        return validmoves
    return capture_move