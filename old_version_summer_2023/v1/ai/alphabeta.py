from  ai.heuristics import Heuristics
from objects.color import Color
from objects.board import Board
from config import ai_config

# runs the alphabeta pruning algorithm
# @staticmethod
def alphabeta(chessboard, depth, a, b, maximizing, color):
    if (depth == 0):
        return Heuristics.evaluate(chessboard)

    if color == Color.BLACK:
        if (maximizing):
            best_score = -ai_config.infinity
            for move in chessboard.get_possible_moves(Color.WHITE):
                copy = Board.clone(chessboard)
                copy.perform_move(move)

                best_score = max(best_score, alphabeta(copy, depth-1, a, b, False, Color.WHITE))
                a = max(a, best_score)
                if (b <= a):
                    break
            return best_score
        else:
            best_score = ai_config.infinity
            for move in chessboard.get_possible_moves(Color.BLACK):
                copy = Board.clone(chessboard)
                copy.perform_move(move)

                best_score = min(best_score, alphabeta(copy, depth-1, a, b, True, Color.BLACK))
                b = min(b, best_score)
                if (b <= a):
                    break
            return best_score
    else:
        if (maximizing):
            best_score = -ai_config.infinity
            for move in chessboard.get_possible_moves(Color.BLACK):
                copy = Board.clone(chessboard)
                copy.perform_move(move)

                best_score = max(best_score, alphabeta(copy, depth-1, a, b, False, Color.BLACK))
                a = max(a, best_score)
                if (b <= a):
                    break
            return best_score
        else:
            best_score = ai_config.infinity
            for move in chessboard.get_possible_moves(Color.WHITE):
                copy = Board.clone(chessboard)
                copy.perform_move(move)

                best_score = min(best_score, alphabeta(copy, depth-1, a, b, True, Color.WHITE))
                b = min(b, best_score)
                if (b <= a):
                    break
            return best_score