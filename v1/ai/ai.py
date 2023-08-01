import numpy
from objects.board import Board
from objects.pieces.piece import Piece
from objects.pieces.pawn import Pawn
from objects.pieces.knight import Knight
from objects.pieces.bishop import Bishop
from objects.pieces.rook import Rook
from objects.pieces.queen import Queen
from objects.pieces.king import King
from objects.color import Color

class Heuristics:

    # The tables denote the points scored for the position of the chess pieces on the board.

    PAWN_TABLE = numpy.array([
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 5, 10, 10,-20,-20, 10, 10,  5],
        [ 5, -5,-10,  0,  0,-10, -5,  5],
        [ 0,  0,  0, 20, 20,  0,  0,  0],
        [ 5,  5, 10, 25, 25, 10,  5,  5],
        [10, 10, 20, 30, 30, 20, 10, 10],
        [50, 50, 50, 50, 50, 50, 50, 50],
        [ 0,  0,  0,  0,  0,  0,  0,  0]
    ])

    KNIGHT_TABLE = numpy.array([
        [-50, -40, -30, -30, -30, -30, -40, -50],
        [-40, -20,   0,   5,   5,   0, -20, -40],
        [-30,   5,  10,  15,  15,  10,   5, -30],
        [-30,   0,  15,  20,  20,  15,   0, -30],
        [-30,   5,  15,  20,  20,  15,   0, -30],
        [-30,   0,  10,  15,  15,  10,   0, -30],
        [-40, -20,   0,   0,   0,   0, -20, -40],
        [-50, -40, -30, -30, -30, -30, -40, -50]
    ])

    BISHOP_TABLE = numpy.array([
        [-20, -10, -10, -10, -10, -10, -10, -20],
        [-10,   5,   0,   0,   0,   0,   5, -10],
        [-10,  10,  10,  10,  10,  10,  10, -10],
        [-10,   0,  10,  10,  10,  10,   0, -10],
        [-10,   5,   5,  10,  10,   5,   5, -10],
        [-10,   0,   5,  10,  10,   5,   0, -10],
        [-10,   0,   0,   0,   0,   0,   0, -10],
        [-20, -10, -10, -10, -10, -10, -10, -20]
    ])

    ROOK_TABLE = numpy.array([
        [ 0,  0,  0,  5,  5,  0,  0,  0],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [ 5, 10, 10, 10, 10, 10, 10,  5],
        [ 0,  0,  0,  0,  0,  0,  0,  0]
    ])

    QUEEN_TABLE = numpy.array([
        [-20, -10, -10, -5, -5, -10, -10, -20],
        [-10,   0,   5,  0,  0,   0,   0, -10],
        [-10,   5,   5,  5,  5,   5,   0, -10],
        [  0,   0,   5,  5,  5,   5,   0,  -5],
        [ -5,   0,   5,  5,  5,   5,   0,  -5],
        [-10,   0,   5,  5,  5,   5,   0, -10],
        [-10,   0,   0,  0,  0,   0,   0, -10],
        [-20, -10, -10, -5, -5, -10, -10, -20]
    ])

    @staticmethod
    def evaluate(board):
        material = Heuristics.get_material_score(board)

        pawns = Heuristics.get_piece_position_score(board, Pawn.PIECE_TYPE, Heuristics.PAWN_TABLE)
        knights = Heuristics.get_piece_position_score(board, Knight.PIECE_TYPE, Heuristics.KNIGHT_TABLE)
        bishops = Heuristics.get_piece_position_score(board, Bishop.PIECE_TYPE, Heuristics.BISHOP_TABLE)
        rooks = Heuristics.get_piece_position_score(board, Rook.PIECE_TYPE, Heuristics.ROOK_TABLE)
        queens = Heuristics.get_piece_position_score(board, Queen.PIECE_TYPE, Heuristics.QUEEN_TABLE)

        return material + pawns + knights + bishops + rooks + queens

    # Returns the score for the position of the given type of piece.
    # A piece type can for example be: pieces.Pawn.PIECE_TYPE.
    # The table is the 2d numpy array used for the scoring. Example: Heuristics.PAWN_TABLE
    @staticmethod
    def get_piece_position_score(board, piece_type, table):
        white = 0
        black = 0
        for x in range(8):
            for y in range(8):
                piece = board.chesspieces[x][y]
                if (piece != 0):
                    if (piece.piece_type == piece_type):
                        if (piece.color == Color.WHITE):
                            white += table[x][y]
                        else:
                            black += table[7 - x][y]

        return white - black

    @staticmethod
    def get_material_score(board):
        white = 0
        black = 0
        for x in range(8):
            for y in range(8):
                piece = board.chesspieces[x][y]
                if (piece != 0):
                    if (piece.color == Color.WHITE):
                        white += piece.value
                    else:
                        black += piece.value

        return white - black


class AI:

    INFINITE = 10000000

    @staticmethod
    def get_ai_move(chessboard, color, invalid_moves):
        best_move = 0
        best_score = AI.INFINITE
        for move in chessboard.get_possible_moves(color):
            if (AI.is_invalid_move(move, invalid_moves)):
                continue

            copy = Board.clone(chessboard)
            copy.perform_move(move)

            score = AI.alphabeta(copy, 2, -AI.INFINITE, AI.INFINITE, True, color)
            if (score < best_score):
                best_score = score
                best_move = move

        # Checkmate.
        if (best_move == 0):
            return 0

        copy = Board.clone(chessboard)
        copy.perform_move(best_move)
        if (copy.is_check(color)):
            invalid_moves.append(best_move)
            return AI.get_ai_move(chessboard, color, invalid_moves)

        return best_move

    @staticmethod
    def is_invalid_move(move, invalid_moves):
        for invalid_move in invalid_moves:
            if (invalid_move.equals(move)):
                return True
        return False

    @staticmethod
    def minimax(board, depth, maximizing, color):
        if (depth == 0):
            return Heuristics.evaluate(board)

        if color == Color.BLACK:
            if (maximizing):
                best_score = -AI.INFINITE
                for move in board.get_possible_moves(Color.WHITE):
                    copy = Board.clone(board)
                    copy.perform_move(move)

                    score = AI.minimax(copy, depth-1, False)
                    best_score = max(best_score, score)

                return best_score
            else:
                best_score = AI.INFINITE
                for move in board.get_possible_moves(Color.BLACK):
                    copy = Board.clone(board)
                    copy.perform_move(move)

                    score = AI.minimax(copy, depth-1, True)
                    best_score = min(best_score, score)

                return best_score
        else:
            if (maximizing):
                best_score = -AI.INFINITE
                for move in board.get_possible_moves(Color.BLACK):
                    copy = Board.clone(board)
                    copy.perform_move(move)

                    score = AI.minimax(copy, depth-1, False)
                    best_score = max(best_score, score)

                return best_score
            else:
                best_score = AI.INFINITE
                for move in board.get_possible_moves(Color.WHITE):
                    copy = Board.clone(board)
                    copy.perform_move(move)

                    score = AI.minimax(copy, depth-1, True)
                    best_score = min(best_score, score)

                return best_score

    @staticmethod
    def alphabeta(chessboard, depth, a, b, maximizing, color):
        if (depth == 0):
            return Heuristics.evaluate(chessboard)

        if color == Color.BLACK:
            if (maximizing):
                best_score = -AI.INFINITE
                for move in chessboard.get_possible_moves(Color.WHITE):
                    copy = Board.clone(chessboard)
                    copy.perform_move(move)

                    best_score = max(best_score, AI.alphabeta(copy, depth-1, a, b, False, Color.WHITE))
                    a = max(a, best_score)
                    if (b <= a):
                        break
                return best_score
            else:
                best_score = AI.INFINITE
                for move in chessboard.get_possible_moves(Color.BLACK):
                    copy = Board.clone(chessboard)
                    copy.perform_move(move)

                    best_score = min(best_score, AI.alphabeta(copy, depth-1, a, b, True, Color.BLACK))
                    b = min(b, best_score)
                    if (b <= a):
                        break
                return best_score
        else:
            if (maximizing):
                best_score = -AI.INFINITE
                for move in chessboard.get_possible_moves(Color.BLACK):
                    copy = Board.clone(chessboard)
                    copy.perform_move(move)

                    best_score = max(best_score, AI.alphabeta(copy, depth-1, a, b, False, Color.BLACK))
                    a = max(a, best_score)
                    if (b <= a):
                        break
                return best_score
            else:
                best_score = AI.INFINITE
                for move in chessboard.get_possible_moves(Color.WHITE):
                    copy = Board.clone(chessboard)
                    copy.perform_move(move)

                    best_score = min(best_score, AI.alphabeta(copy, depth-1, a, b, True, Color.WHITE))
                    b = min(b, best_score)
                    if (b <= a):
                        break
                return best_score
