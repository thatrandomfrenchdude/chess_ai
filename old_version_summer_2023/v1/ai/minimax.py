from  ai.heuristics import Heuristics
from objects.color import Color
from objects.board import Board
from config import ai_config

# TODO: break this out to a separate file
# --> make different AI types, with AI as base class

# runs the minimax algorithm
# @staticmethod
def minimax(board, depth, maximizing, color):
    if (depth == 0):
        return Heuristics.evaluate(board)

    if color == Color.BLACK:
        if (maximizing):
            best_score = -ai_config.infinity
            for move in board.get_possible_moves(Color.WHITE):
                copy = Board.clone(board)
                copy.perform_move(move)

                score = minimax(copy, depth-1, False)
                best_score = max(best_score, score)

            return best_score
        else:
            best_score = ai_config.infinity
            for move in board.get_possible_moves(Color.BLACK):
                copy = Board.clone(board)
                copy.perform_move(move)

                score = minimax(copy, depth-1, True)
                best_score = min(best_score, score)

            return best_score
    else:
        if (maximizing):
            best_score = -ai_config.infinity
            for move in board.get_possible_moves(Color.BLACK):
                copy = Board.clone(board)
                copy.perform_move(move)

                score = minimax(copy, depth-1, False)
                best_score = max(best_score, score)

            return best_score
        else:
            best_score = ai_config.infinity
            for move in board.get_possible_moves(Color.WHITE):
                copy = Board.clone(board)
                copy.perform_move(move)

                score = minimax(copy, depth-1, True)
                best_score = min(best_score, score)

            return best_score